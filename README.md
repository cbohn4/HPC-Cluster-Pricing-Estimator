# Slurm Job Cost Estimation
This repository is used to provide a quick estimation of the cost of a large number of slurm jobs in a shorter period of time.
This is accomplished by using a "seat" model for slurm jobs rather than direct resource requests. (See SeatJustification.md).

Example `sacct` command to get required fields:

```
sacct -a -S 2021-10-20 -E 2021-10-22 -o ReqNodes,AllocCPUS,Elapsed,ReqMem,Timelimit,MaxRSS > slurm_data.sacct
```