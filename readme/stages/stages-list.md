---
ft:title: Stages List
Product: Cortex
Category: Reference Guide
Product_Category: Cortex XQL
ft:lang: en-US
ft:topicType: reference
---

# Stages list

The following table lists all available XQL pipeline stages:

| Stage                                                                                                     | Description                                                                                      |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [`alter`](alter.md)                                                                                       | Manipulate data by changing existing field values or creating new fields                         |
| [`arrayexpand`](arrayexpand.md)                                                                           | Expand an array field into multiple rows                                                         |
| [`bin`](bin.md)                                                                                           | Group numeric values into bins                                                                   |
| [`call`](call.md)                                                                                         | Call a saved XQL query                                                                           |
| [`comp`](comp.md)                                                                                         | Aggregate data using grouping and aggregate functions                                            |
| [`config`](config.md)                                                                                     | Configure query settings                                                                         |
| [`dataset`](dataset.md)                                                                                   | Specify the dataset to query                                                                     |
| [`dedup`](dedup.md)                                                                                       | Remove duplicate rows                                                                            |
| [`fields`](fields.md)                                                                                     | Select or exclude specific fields                                                                |
| [`filter`](filter.md)                                                                                     | Filter rows based on a condition                                                                 |
| [`iploc`](iploc.md)                                                                                       | Enrich IP addresses with geolocation data                                                        |
| [`join`](join.md)                                                                                         | Join two datasets                                                                                |
| [`limit`](limit.md)                                                                                       | Limit the number of rows returned                                                                |
| [`pivot`](pivot.md)                                                                                       | Rotate row-level data into columns using aggregate functions                                     |
| [`preset`](presets.md)                                                                                    | Apply preset configurations                                                                      |
| [`replacenull`](replacenull.md)                                                                           | Replace null values with a specified value                                                       |
| [`search`](search.md)                                                                                     | Search for records matching a text query                                                         |
| [`sort`](sort.md)                                                                                         | Sort rows by one or more fields                                                                  |
| [`tag`](tag.md)                                                                                           | Add tags to query results                                                                        |
| [`target`](target.md)                                                                                     | Specify the target output for query results                                                      |
| [`top`](top.md)                                                                                           | Return the top N rows by a specified field                                                       |
| [`transaction`](transaction.md)                                                                           | Group events into transactions                                                                   |
| [`transpose`](https://github.com/jrosenpanw/doc_a/blob/main/Cortex_XQL_Command_Reference/Q4/transpose.md) | Transpose rows into columns                                                                      |
| [`union`](union.md)                                                                                       | Combine the results of two or more queries                                                       |
| [`view`](view.md)                                                                                         | Query a saved view                                                                               |
| [`windowcomp`](windowcomp.md)                                                                             | Perform analytic (window) functions over a defined window of rows without collapsing the dataset |
