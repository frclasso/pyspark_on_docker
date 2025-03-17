# Use Bitnami Spark as the base image
FROM bitnami/spark:latest

# Set the working directory inside the container
WORKDIR /opt/bitnami/spark

# Copy your Python script into the container
COPY your_program.py /opt/bitnami/spark/anyfilename.py

# Set appropriate permissions (optional)
RUN chmod +x /opt/bitnami/spark/anyfilename.py

# Default command to start Spark Master
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
