from spark_connection import spark


# Sample data: list of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Define column names
columns = ["Name", "Age"]

# Create a DataFrame from the data
df = spark.createDataFrame(data, columns)

# Dataframe 2
data_jobs = [("Alice", "Engineer"), ("Bob", "Doctor")]
df_jobs = spark.createDataFrame(data_jobs, ["Name", "Job"])


# Register the DataFrame as a temporary view
df.createOrReplaceTempView("people")
df_jobs.createOrReplaceTempView("jobs")

# SQL join query
result = spark.sql("""
    SELECT p.Name, p.Age, j.Job 
    FROM people p
    JOIN jobs j ON p.Name = j.Name
""")

result.show()