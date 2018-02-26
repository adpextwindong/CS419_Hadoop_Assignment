#!/bin/sh
hdfs dfs -copyFromLocal gramsci.txt gramsci.txt

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reduce.py -mapper "mapper.py" -reducer "reduce.py" -input gramsci.txt -output test
