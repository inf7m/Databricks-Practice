# Databricks notebook source
# SETUP metadata about Azure-BLOB
storage_account_name = "dbstorageg3tjdyu4uhw2a"
storage_account_access_key = "xspRfjDWb//kxxteOv711eDMYFYra5/6QcHl2oFBQ3oMdnUOsh7k6SQKAkmWH6/sXF4FSMEI0JLH+ASt1xY2UQ=="
container_name = "container1"
mount_point = "/mnt/blob-storage"




# COMMAND ----------


# Mount Stage
dbutils.fs.mount(
    source=f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
    mount_point=mount_point,
    extra_configs={
        f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": f"{storage_account_access_key}"
    }
)
# Refresh - make sure everything is up-to-date

# COMMAND ----------

# Setup the configuration for Spark
spark.conf.set(
  "fs.azure.account.key."+storage_account_name+".blob.core.windows.net",
  storage_account_access_key)

# COMMAND ----------

# Refresh the `Data Explorer` -> make sure everything is upto date
dbutils.fs.refreshMounts()

# COMMAND ----------

# Dataframe loading
df = spark.read.format("csv").option("header","true").load("/mnt/blob-storage/spotify_data.csv")

# Saving the Dataframe in Delta Lake
df.write.mode("overWrite").saveAsTable("SP1")

# COMMAND ----------



# COMMAND ----------


