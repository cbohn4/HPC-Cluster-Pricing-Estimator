import math
import sys
import time

import numpy as np
import pandas as pd
import traceback

providerPricing = {
	# Explanation of pricing can be found in SeatJustification.md
	# Prices are based on an average of VM costs based on "seats"
	# of 1 Core and 4GB or 8GB of memory and increasing the number
	# of seats in a VM. 
    "AWS" :[0.0385,0.0504],
    "GCP" :[0.035,0.0475],
    "MSFT":[0.055,0.07125],
    "DO"  :[0.0446,0.05952],
    "IBM" :[0.053,0.0685],
    "HCC" :[0.004516267,0.007016981],
}

# Convert Sacct Job Time to Job Hours
def sacctTimeToTime(sacct_time):
    """Converts a time format from slurm to hours.
    Function can also accept full hours from datasets and
    return these values directly back.
    
    Args:
        sacct_time (str or int or float): Value of time from Slurm or dataset.
    """   

    hours = 0
    if type(sacct_time) == str:
        if ":" not in sacct_time:
            return(float(sacct_time))
        day_time = sacct_time.split("-")[0]
        if "-" in sacct_time:
            hours += int(sacct_time.split("-")[0])*24
            day_time = sacct_time.split("-")[1]
        day_time = day_time.split(":")
        hours += int(day_time[0])
        hours += int(day_time[1])/60
        hours += int(day_time[2])/3600
        return(hours)
    elif type(sacct_time) == int or type(sacct_time) == float:
        return(sacct_time)
    

## Get basic job info and time
def job_info(job_line):
    """Converts a line from Slurm's sacct data to a 
    more managable format

    Args:
        job_line (pd.Series): Row from a dataframe containing sacct information
    """
    
    job_data = {}
    job_data["node"] = float(job_line["ReqNodes"])
    job_data["cpu"] = float(job_line["AllocCPUS"])
    job_data["time"] = job_line["Elapsed"]
    job_data["time_req"] = sacctTimeToTime(job_line["Timelimit"])
    job_data["hours"] = sacctTimeToTime(job_data["time"])
    job_data["mem"] = slurm_memory(job_line["ReqMem"],job_line["AllocCPUS"],job_line["ReqNodes"])
    job_data["mem_used"] = slurm_memory(job_line["MaxRSS"])
    return(job_data)

def slurm_memory(mem_value, cpu_req=1, node_req=1):
    """Converts the various memory reporting methods in Slurm
    to GB.

    Args:
        mem_value (str): Memory request value for a job.
        cpu_req (int, optional): Number of CPUs requested for a job. Defaults to 1.
        node_req (int, optional): Number of worker nodes requested for a job. Defaults to 1.
    """
    
    if "c" in mem_value:
        multiplier = cpu_req
        mem_value = mem_value.replace("c","")
    elif "n" in mem_value:
        multiplier = node_req
        mem_value = mem_value.replace("n","")
    else:
        multiplier = 1
    if "G" in mem_value:
        return(float(mem_value.replace("G",""))*multiplier)
    elif "M" in mem_value:
        return(float(mem_value.replace("M",""))*multiplier/1000)
    elif "K" in mem_value:
        return(float(mem_value.replace("K",""))*multiplier/1000000)
    elif "T" in mem_value:
        return(float(mem_value.replace("T",""))*multiplier*1000)
    else:
        return(float(mem_value))

def cloud_cost(providers, cores, mem, hours):
    """Generates a cost estimation for a job
    based on total number of requested core, a value of memory, 
    either used (MaxRSS), or requested (ReqMeM), and a value of time, 
    either used (Elapsed) or Requested (Timelimit).

    Args:
        providers (dict): Prices for 1/4 and 1/8 seats in HPC
        cores (int): Number of cores to estimate the price with.
        mem (float): Amount of memory in GB to estimate the price with.
        hours (float): Amount of time in hours to estimate the price with.
    """
    ### Choose 1C/4G seat or 1C/8G seat, default to 1C/4G (Seat 0). Seat 1 is 1C/8G
    seat = 0
    if mem/cores > 4:
        seat = 1
    job_cost = {}
    seats = max(cores,(mem/(4+4*seat)))
    # Math.ceil is used due to some providers rounding up to the nearest hour for billing
    for provider in providers.keys():
        ## Cost           = provider seat cost        *  time             * seats needed (1 core per seat)
        job_cost[provider] = providers[provider][seat] *  math.ceil(hours) * seats 
    return(job_cost)

              

              
job_prices = {}
job_estimates = {}              
start_time = time.time()
jobdf = pd.read_csv(str(sys.argv[1]),sep="|", encoding = "ISO-8859-1")
print(f"Time to load data: {time.time()-start_time} seconds. {len(jobdf)}")

price_results = pd.DataFrame({
    #"JobID":[],
    "Nodes":[],
    "Total Cores":[],
    "CPU Time":[],
    "Total Memory Requested (GB)":[],
    "Total Memory Used (KB)":[],
    "Time Used (Hrs)":[],
    "Time Requested (Hrs)":[],
    "AWS-Usage":[],
    "GCP-Usage":[],
    "MSFT-Usage":[],
    "DO-Usage":[],
    "IBM-Usage":[],
    "HCC-Usage":[],
    "AWS-Requested":[],
    "GCP-Requested":[],
    "MSFT-Requested":[],
    "DO-Requested":[],
    "IBM-Requested":[],
    "HCC-Requested":[]    
})

def compute_prices():
    """Generates the Estimated prices on different platforms
    based on requested and used resources from sacct data. 
    """
    for r,job in  jobdf.iterrows():
        job_data = job_info(job)
        if job_data != {}:
            
            # Actual is based on the elapsed time
            # Requested is based on the slurm time requested
            try:
                #                          Pricing Dataset,  AllocCPUS            , MaxRSS                 , Elapsed
                jobEstimateActual=(cloud_cost(providerPricing,int(job_data["cpu"]),job_data["mem_used"],job_data["hours"]))
                #                          Pricing Dataset, AllocCPUS          , ReqMem              , Timelimit
                jobEstimateReq=(cloud_cost(providerPricing,int(job_data["cpu"]),int(job_data["mem"]),job_data["time_req"]))
                
                price_results = price_results.append({
                    "Nodes":int(job_data["node"]),
                    "Total Cores":int(job_data["cpu"]), 
                    "CPU Time":job["CPUTimeRAW"],
                    "Total Memory Requested (GB)":float(job_data["mem"]),
                    "Total Memory Used (GB)":job_data["mem_used"],
                    "Time Used (Hrs)":float(job_data["hours"]),
                    "Time Requested (Hrs)":float(job_data["time_req"]),
                    "AWS-Usage":float(jobEstimateActual["AWS"]),
                    "GCP-Usage":float(jobEstimateActual["GCP"]),
                    "MSFT-Usage":float(jobEstimateActual["MSFT"]),
                    "DO-Usage":float(jobEstimateActual["DO"]),
                    "IBM-Usage":float(jobEstimateActual["IBM"]),
                    "HCC-Usage":float(jobEstimateActual["HCC"]),
                    "AWS-Requested":float(jobEstimateReq["AWS"]),
                    "GCP-Requested":float(jobEstimateReq["GCP"]),
                    "MSFT-Requested":float(jobEstimateReq["MSFT"]),
                    "DO-Requested":float(jobEstimateReq["DO"]),
                    "IBM-Requested":float(jobEstimateReq["IBM"]),
                    "HCC-Requested":float(jobEstimateReq["HCC"]),    
                    },ignore_index=True)
                
            except Exception as e:
                print(e)
                print(traceback.format_exc())

    print(f"Time to load and process data: {time.time()-start_time} seconds")
    job_stats = {"Total":{},"Average":{}}
    for metric in price_results.columns:
        if metric not in ["JobID","CPU Time","Total Memory Used (KB)","Time Used (Hrs)","Time Requested (Hrs)"]:
            print(metric)
            job_stats["Total"][metric] = sum(price_results[metric])
            job_stats["Average"][metric] = np.mean(price_results[metric])

    price_results.to_csv("priceTest."+str(sys.argv[1])+".csv")
        
if __name__ == "__main__":
    compute_prices()