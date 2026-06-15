---
ft:title: "search"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "reference"
---

# search

Use the `search` stage to perform free-text string searching across your ingested data, allowing you to find specified text strings within fields of single or multiple datasets.

## Syntax

```sql
search "<free_text1>"[,"<free_text2>", ...] [dataset = <dataset name>]
```

## Parameters

| Name          | Type    | Required | Description                                                            |
| ------------- | ------- | -------- | ---------------------------------------------------------------------- |
| `<free_text>` | string  | Yes      | The text string to search for. Multiple strings imply an OR condition. |
| `dataset`     | dataset | No       | Refines the search by explicitly specifying a dataset.                 |

## Returns

The `search` stage returns records containing the specified text string(s). When searching a single dataset, all field columns of that dataset are included. When searching multiple datasets, the results include key columns such as `_time`, `_vendor`, `_product`, `_dataset`, and `raw_data`.

## Usage notes

* The `search` stage must be the first stage in your XQL query, though it can be preceded by a `config` stage.
* Queries containing the `search` stage do not support aggregation stages such as `bin`, `comp`, `top`, or `dedup`.
* Queries using the `search` stage are limited to the last 90 days of data.
* By default, forensic datasets are not included in `search` stage queries unless specifically enabled.
* If searching multiple datasets, the `raw_data` field column contains the JSON with the relevant raw information, allowing for drill-down.

## Examples

### Example 1: Basic free-text search across default datasets

**Goal**: Searches for the phrase "login successful" across all available datasets in the tenant (implicitly).

**XQL code**:

```sql
search "login successful"
```

**Explanation**: This query searches for the string "login successful" across all datasets. In the context of the sample data, it finds the relevant login event.

**Output**:

| _time                   | _dataset       | event_description       | raw_log_data                             |
| ----------------------- | -------------- | ----------------------- | ---------------------------------------- |
| 2023-10-26 10:00:00 UTC | sample_xql_raw | "User login successful" | "User Alice logged in from 192.168.1.10" |

### Example 2: Free-text search within a specific dataset

**Goal**: Explicitly searches for the string "cmd.exe" only within the `sample_xql_raw` dataset.

**XQL code**:

```sql
search "cmd.exe" dataset = sample_xql_raw
```

**Explanation**: This query restricts the free-text search for "cmd.exe" to the specified `sample_xql_raw` dataset.

**Output**:

| _time                   | _dataset       | event_description     | raw_log_data                                      |
| ----------------------- | -------------- | --------------------- | ------------------------------------------------- |
| 2023-10-26 10:05:30 UTC | sample_xql_raw | "File access attempt" | "Process cmd.exe attempted to access /etc/passwd" |

### Example 3: Searching for multiple free-text strings

**Goal**: Searches for events containing either "connection" or "backup" within the `sample_xql_raw` dataset.

**XQL code**:

```sql
search "connection", "backup" dataset = sample_xql_raw
```

**Explanation**: This query searches for records containing either "connection" OR "backup" within the specified dataset.

**Output**:

| _time                   | _dataset       | event_description                | raw_log_data                                           |
| ----------------------- | -------------- | -------------------------------- | ------------------------------------------------------ |
| 2023-10-26 10:15:15 UTC | sample_xql_raw | "Network connection established" | "Outbound connection to 1.1.1.1:443 initiated by AppX" |
| 2023-10-26 11:00:10 UTC | sample_xql_raw | "Database backup completed"      | "Full backup of prod_db to S3 completed."              |

### Example 4: Using config timeframe with search

**Goal**: Searches for "successful" events within the last 24 hours.

**XQL code**:

```sql
config timeframe = 24h
search "successful" dataset = sample_xql_raw
```

**Explanation**: The `config timeframe` stage is used before the `search` stage to limit the query execution window to the last 24 hours.

**Output**:

| _time                   | _dataset       | event_description       | is_successful |
| ----------------------- | -------------- | ----------------------- | ------------- |
| 2023-10-26 10:00:00 UTC | sample_xql_raw | "User login successful" | true          |

## Related articles

* **Stages**: [`config`](config.md)
