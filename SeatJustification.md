# Justification and Reason for "Seat Pricing"
With many cloud hosting providers, there is not a central way to get the pricing of different
virtual machines (VM) in an efficient manner. Amazon's AWS Platform does offer this, however
the other providers used in this script, Google Cloud Platform, Microsoft Azure, IBM Cloud, 
Digital Ocean as well as a local comparison to the lease pricing for the Holland Computing
Center do not. 

In order to simplify the programming and logic of the script, a "Seat Pricing" model is used
to estimate the cost of a computing job. A seat will be used as a portion of a compute node,
either with 1 CPU Core and 4 GB of RAM or 1 CPU Core and 8 GB of RAM as the unit. For example, 
a HPC job requesting 4 CPU cores and 20GB of RAM would require a minimum of 4 "seats". The RAM 
requirement could fit in 3 8 GB seats or 5 4GB seats. Which ever of the two combinations is the
lowest will be the price used as the estimated cost of the job being analyzed. 


# Pricing Calculations

## Google Cloud Platform 
For the Google Cloud Platform, the prices were calculated using the pricing calculator with the
following settings.
Operating System: Free
Machine Class: E2
Datacenter Location: Iowa (us-central1)
Run time: 24 Hours / day, 7 Days / Week
Prices: https://cloud.google.com/products/calculator

#### 1 Core / 4 GB Seat
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |8         |e2-standard-2   |0.07       |2        |0.035          |
|4       |16        |e2-standard-4   |0.13       |4        |0.0325         |
|8       |32        |e2-standard-8   |0.27       |8        |0.03375        |
|16      |64        |e2-standard-16  |0.54       |16       |0.03375        |
|32      |128       |e2-standard-16  |1.07       |32       |0.03344        |
|Average |          |                |           |         |**0.03369**    |

#### 1 Core / 8 GB Seat
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |16        |e2-highmem-2    |0.09       |2        |0.045          |
|4       |32        |e2-highmem-4    |0.18       |4        |0.045          |
|8       |64        |e2-highmem-8    |0.36       |8        |0.045          |
|16      |128       |e2-highmem-16   |0.72       |16       |0.045          |
|Average |          |                |           |         |**0.045**      |


## Microsoft Azure 
For the Microsoft Azure platform, the prices were calculated using the pricing calculator with the
following settings.
Operating System: CentOS
Tier: Standard
Region: West US 2
Run time: 24 Hours / day, 7 Days / Week
Prices: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/

#### 1 Core / 4 GB Seat - D2 – D64 v4
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |8         |D2 v4           |0.096      |2        |0.048          |
|4       |16        |D4 v4           |0.192      |4        |0.048          |
|8       |32        |D8 v4           |0.384      |8        |0.048          |
|16      |64        |D16 v4          |0.768      |16       |0.048          |
|32      |128       |D32 v4          |1.536      |32       |0.048          |
|48      |192       |D48 v4          |2.304      |48       |0.048          |
|64      |256       |D64 v4          |3.072      |64       |0.048          |
|Average |          |                |           |         |**0.048**      |

#### 1 Core / 8 GB Seat - E2 – E96 v5
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |16        |E2 v5           |0.063      |2        |0.0315         |
|4       |32        |E4 v5           |0.126      |4        |0.0315         |
|8       |64        |E8 v5           |0.252      |8        |0.0315         |
|16      |128       |E16 v5          |0.504      |16       |0.0315         |
|20      |160       |E20 v5          |0.630      |20       |0.0315         |
|32      |256       |E32 v5          |1.008      |32       |0.0315         |
|48      |384       |E48 v5          |1.512      |48       |0.0315         |
|64      |512       |E64 v5          |2.016      |64       |0.0315         |
|96      |672       |E96 v5          |3.024      |96       |0.0315         |
|Average |          |                |           |         |**0.0315**     |


## Digital Ocean 
For Digital Ocean, the prices were calculated using the pricing calculator with the
following settings.

Prices: https://www.digitalocean.com/pricing

#### 1 Core / 4 GB Seat - General Purpose Droplets
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |8         |General Purpose |0.08929    |2        |0.044645       |
|4       |16        |General Purpose |0.17857    |4        |0.0446425      |
|8       |32        |General Purpose |0.35714    |8        |0.0446425      |
|16      |64        |General Purpose |0.71429    |16       |0.044643125    |
|32      |128       |General Purpose |1.42857    |32       |0.044642813    |
|40      |192       |General Purpose |1.78571    |40       |0.04464275     |
|Average |          |                |           |         |**0.044643115**|

#### 1 Core / 8 GB Seat - Memory Optimized Droplets
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |16        |Memory Optimized|0.11905    |2        |0.059525       |
|4       |32        |Memory Optimized|0.23810    |4        |0.059525       |
|8       |64        |Memory Optimized|0.47619    |8        |0.05952375     |
|16      |128       |Memory Optimized|0.95238    |16       |0.05952375     |
|24      |192       |Memory Optimized|1.42857    |24       |0.05952375     |
|32      |256       |Memory Optimized|1.90476    |32       |0.05952375     |
|Average |          |                |           |         |**0.059524167**|



## IBM Cloud
For IBM Cloud, the prices were calculated using the pricing calculator with the
following settings.
Operating System: CentOS
Type of virtual Server: Public
Region: Dallas 2
Prices: https://cloud.ibm.com/vpc-ext/provision/vs

#### 1 Core / 4 GB Seat - Balanced
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |8         |bx2-2x8         |0.096      |2        |0.048          |
|4       |16        |bx2-4x16        |0.192      |4        |0.048          |
|8       |32        |bx2-8x32        |0.384      |8        |0.048          |
|16      |64        |bx2-16x64       |0.768      |16       |0.048          |
|32      |128       |bx2-32x128      |1.536      |32       |0.048          |
|48      |192       |bx2-48x192      |2.305      |48       |0.048020833    |
|64      |256       |bx2-64x256      |3.073      |64       |0.048015625    |
|96      |384       |bx2-96x384      |4.609      |96       |0.048010417    |
|128     |512       |bx2-128x512     |6.146      |128      |0.048015625    |
|Average |          |                |           |         |**0.048006944**|

#### 1 Core / 8 GB Seat - Memory
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |16        |mx2-2x16        |0.124      |2        |0.062          |
|4       |32        |mx2-4x32        |0.248      |4        |0.062          |
|8       |64        |mx2-8x64        |0.497      |8        |0.062125       |
|16      |128       |mx2-16x128      |0.994      |16       |0.062125       |
|32      |256       |mx2-32x256      |1.987      |32       |0.06209375     |
|48      |384       |mx2-48x384      |2.981      |48       |0.062104167    |
|64      |512       |mx2-64x512      |3.974      |64       |0.06209375     |
|96      |768       |mx2-96x768      |5.961      |96       |0.06209375     |
|128     |1024      |mx2-128x1024    |7.949      |128      |0.062101563    |
|Average |          |                |           |         |**0.062081887**|


## Amazon Web Services
For Amazons Web Services, the prices were calculated using the pricing calculator with the
following settings.
Operating System: CentOS
Type of virtual Server: Public
Region: US East (Ohio)
Prices: https://calculator.aws/#/createCalculator/EC2
Pricing: On Demand

#### 1 Core / 4 GB Seat 
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |8         |t4g.large       |0.0672     |2        |0.0336         |
|4       |16        |t4g.xlarge      |0.1344     |4        |0.0336         |
|8       |32        |t4g.2xlarge     |0.2688     |8        |0.0336         |
|16      |64        |m6g.4xlarge     |0.616      |16       |0.0385         |
|32      |128       |m6g.8xlarge     |1.232      |32       |0.0385         |
|48      |192       |m6g.12xlarge    |1.848      |48       |0.0385         |
|64      |256       |m6g.16xlarge    |2.464      |64       |0.0385         |
|96      |384       |m5a.24xlarge    |4.128      |96       |0.043          | 
|128     |512       |m6i.32xlarge    |6.144      |128      |0.048          |
|Average |          |                |           |         |**0.038422222**|

#### 1 Core / 8 GB Seat
|Cores   |RAM (GB)  |Instance Name   |Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|---------|---------------|
|2       |16        |r6g.large       |0.1008     |2        |0.0504         |
|4       |32        |r6g.xlarge      |0.2016     |4        |0.0504         |
|8       |64        |r6g.2xlarge     |0.4032     |8        |0.0504         |
|16      |128       |r6g.4xlarge     |0.8064     |16       |0.0504         |
|32      |256       |r6g.8xlarge     |1.6128     |32       |0.0504         |
|48      |384       |r6g.12xlarge    |2.4192     |48       |0.0504         |
|64      |512       |r6g.metal       |3.2256     |64       |0.0504         |
|96      |768       |r5a.24xlarge    |5.424      |96       |0.0565         |
|Average |          |                |           |         |**0.0511625**  |



## Holland Computing Center
For the Holland Computing Center, the prices were calculated using the pricing calculator with the
following settings.
Prices: https://calculator.aws/#/createCalculator/EC2


#### 1 Core / 4 GB Seat 
|Cores   |RAM (GB)  |Instance Name   |Yearly Cost|Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|-----------|---------|---------------|
|16      |64        |Crane           |633        |0.072260274|16       |0.00451626712  |


#### 1 Core / 8 GB Seat *
|Cores   |RAM (GB)  |Instance Name   |Yearly Cost|Hourly Cost| Seats   | Cost per Seat |
|--------|----------|----------------|-----------|-----------|---------|---------------|
|36      |256       |CraneOPA        |1967       |0.224543379|32       |0.00701698059  |

* CraneOPA for the purpose of this model is using 32 seats at 1 CPU Core and 8GB of RAM
  in order to have a price for the 1 CPU core. 
