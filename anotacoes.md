# Docker ommands
docker-compose up -d 
docker start spark_on_docker-spark-master-1


docker-compose down


# Now we need to get the address where our spark master is running. To do that, we need to use docker logs command.
docker logs spark_on_docker-spark-master-1

# Now we need to execute the pyspark file using the following command
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/gen_fake_records.py

docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/anyfilename.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/basics/create_rdd.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/basics/dataframe_join.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/basics/create_dataframe.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/basics/ranking.py
docker-compose exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/app/basics/read_stream.py




docker exec -it spark_on_docker-spark-master-1 bash python3 -c "from faker import Faker; print(Faker().name())"


# references
https://medium.com/@mehmood9501/using-apache-spark-docker-containers-to-run-pyspark-programs-using-spark-submit-afd6da480e0f
https://medium.com/@nomannayeem/pyspark-made-simple-from-basics-to-big-data-mastery-cb1d702968be
https://medium.com/@yoloshe302/pyspark-tutorial-read-and-write-streaming-data-401ed3d860e7
https://www.macrometa.com/event-stream-processing/spark-structured-streaming


# git (root user)
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
git add .
git commit -m "Ranking app"
git push
