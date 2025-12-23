if spark.catalog.tableExists("datamodeling.bronze.bronze_table"):
    last_load_date = spark.sql("SELECT max(order_date) FROM datamodeling.bronze.bronze_table").collect()[0][0]
else:
    last_load_date = '1000-01-01'


