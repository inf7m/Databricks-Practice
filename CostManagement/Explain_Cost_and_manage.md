# Manage the cost

The most basic "currency" is:

**DBU - Databrucks Unit**

the price of DBU is really depends on which types of workloads we're going to use!!!

Check it out at:
https://www.databricks.com/product/pricing/product-pricing/instance-types


## Manage the cost while using Databricks

## 1.Through Cluster Policies

Setup by json file
Sample:

{
  "autoscale.max_workers": {
    "type": "range",
    "maxValue": 4
  },

  "autoscale.min_workers": {
    "type": "fixed",
    "value": 1
  },

  "autotermination_minutes": {
    "type": "fixed",
    "value": 60,
    "hidden": true
  },
  "runtime_engine": {
    "type": "fixed",
    "value": 12.2
  }
}

In here:
I will be running 4 workers, minimum worker as 1

Automatically Terminate -> after 60 minutes
Runtime Engine as “Standard”

## 2.Cloud provider costs

As a cloud-based platform, it will need the following things:
The price is relied on the Cloud Provider (such as: AWS, GCP, Azure)

+ Storage

+ Networking

+ Serverless Compute

