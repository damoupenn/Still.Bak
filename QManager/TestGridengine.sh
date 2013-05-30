#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -N test
#$ -o /home/obs/Share/grid_output
#$ -e /home/obs/Share/grid_output

echo "hostname"
hostname
echo "======="
