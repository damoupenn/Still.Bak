#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -N POWER_Mx
#$ -o /home/obs/Share/grid_output
#$ -e /home/obs/Share/grid_output

echo "hostname"
python /home/obs/Share/StillScripts/FillUpCore.py 10
echo "======="
