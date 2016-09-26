#!/bin/bash

DIR="${BASH_SOURCE%/*}"
source $DIR/config.sh

BAM_PATH=$1
OUTPUT_PATH=$2
BAMBASENAME=$(basename $BAM_PATH)

if [ -L $BAM_PATH ]
then
	BAM_PATH=$(readlink -f $BAM_PATH)
fi

echo $BAM_PATH

if [[ $BAM_PATH =~ \.cram$ ]]
then
	BAM_FIXED=$(eval "echo $BAMBASENAME | sed 's/cram/bam/'")
	$SAMTOOLS view -O BAM --threads 3 $BAM_PATH > $TMP_PATH/$BAM_FIXED
	$SAMTOOLS index $TMP_PATH/$BAM_FIXED
	BAM_PATH=$TMP_PATH/$BAM_FIXED
	BAMBASENAME=$BAM_FIXED
	RM_FLAG=true 
fi

HIST_PATH=$OUTPUT_PATH/$BAMBASENAME.hist.gz
COMMAND="$BEDTOOLS coverage -hist -abam $BAM_PATH -b $INTERVAL_PATH | gzip > $HIST_PATH"
echo $COMMAND

if $RM_FLAG; then
	rm $BAM_PATH
fi