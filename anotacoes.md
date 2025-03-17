docker-compose up -d

docker-compose down


# Now we need to get the address where our spark master is running. To do that, we need to use docker logs command.
docker logs spark_on_docker-spark-master-1

# Now we need to execute the pyspark file using the following command
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/anyfilename.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/create_rdd.py


# references
https://medium.com/@mehmood9501/using-apache-spark-docker-containers-to-run-pyspark-programs-using-spark-submit-afd6da480e0f
https://medium.com/@nomannayeem/pyspark-made-simple-from-basics-to-big-data-mastery-cb1d702968be