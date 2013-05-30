#! /bin/bash

ARGS=$*
STARTPATH=`pwd`
ENDPATH=/home/obs/Share/output_data
SCRATCH=/home/obs/Scratch

for FILE in $ARGS; do
    echo ===================================
    echo --- Working on $FILE ---
    echo ===================================
    if ls ${FILE}cRRE &> /dev/null; then
        echo Output file exists, skipping...
    fi
    FILEBASE=`python -c "import os; print os.path.basename('$FILE')"`
    
    for TFILE in `python get_uv_neighbor.py $FILE`; do
        #This is where things can potentially go wrong
        TFILEBASE=`python -c "import os; print os.path.basename('$TFILE')"`
        if ls ${SCRATCH}/${TFILEBASE}cR &> /dev/null; then
            echo Using ${SCRATCH}/${TFILEBASE}cR
            continue
        fi
        echo cp -r $TFILE ${SCRATCH}/${TFILEBASE}
        echo correct_psa128.py ${SCRATCH}/${TFILEBASE}
        echo rm -rf ${SCRATCH}/${TFILEBASE}
        echo xrfi_simple.py -a 1 --combine -t 20 -c 0_130,755_777,1540,1704,1827,1868,1885_2047 --df=6 ${SCRATCH}/${TFILEBASE}
        echo rm -rf ${SCRATCH}/${TFILEBASE}c
    done
    
    echo cd $SCRATCH
    echo data_redux.sh ${FILEBASE}cR
    ./data_redux.sh ${FILEBASE}cR
    echo cd -
    echo cp -r ${SCRATCH}/${FILEBASE}cRR[DEF] ${ENDPATH}/
    echo cp ${SCRATCH}/${FILEBASE}cRE.npz ${ENDPATH}/
done
