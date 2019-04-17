# Hadoop word count
Simple implement of word count application on Hadoop framework using that write by python.
# How use it
First copy files to HDFS using the following command:
```console
hdfs dfs -copyFromLocal articles /articles
```
And run your mapper and reducer code using this:
```console
hadoop jar <path to haddoop home>/hadoop-<version>/share/hadoop/tools/lib/hadoop-￼streaming-<version>.jar -files mapper.py,reducer.py -mapper mapper.py -reducer ￼reducer.py -input /articles/*.txt -output /output.txt
```
