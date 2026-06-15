---
ft:title: "approx_top"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "reference"
---

# approx_top

Use the `approx_top()` function to return the most frequently occurring elements or highest-sum elements for a specified field. This approximate aggregate function produces results that are highly scalable in terms of memory usage and time compared to exact results from regular aggregate functions.

## Syntax

```SQL  
comp approx_top(<string field>, <number>) [as <alias>[] [by <field1>[,<field2>...[][] [addrawdata = true|false [as <target field>[][]
```
```sql
comp approx_top(<string field>, <number>, <weight string field>) [as <alias>[] [by <field1>[,<field2>...[][][addrawdata = true|false [as <target field>[][]
```

## Parameters

| Name | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| string field | string | Yes | The field for which to find the top elements. |
| number | integer | No | An integer specifying the number of top elements to return. If omitted, it defaults to up to 10 elements. |
| weight string field | numeric | No | A numeric field used to calculate the sum for each unique value in the first specified field, causing the function to return approximate sums instead of counts. |

## Returns

The approx_top() function returns a single array containing up to the specified number of JSON objects (structs). For the count variant, each struct will have "value" (the unique field value) and "count" (its approximate number of occurrences) keys. For the sum variant, each struct will have "value" and "sum" keys, representing the approximate sum calculated using the weight string field.

## Usage Notes

* The comp stage must always precede an approximate aggregate function like approx_top().

* You can use the optional `by` clause to group rows based on one or more specified fields, which allows approx_top() to compute the approximate top elements independently for each group.

* When you set the optional addrawdata parameter to true, the query processes up to 50 defined fields and includes a raw_data column displaying up to 100 raw data events that contributed to the aggregate result.

* New columns created by the comp stage are typically added as the last columns in the result set, and any other fields not explicitly included in the `by` clause or as part of a calculated column is removed from the result set, including the _time system field.

## Examples

### Example 1: Calculating approximate top counts (no weight field)

**Goal**: Calculate the top 2 approximate counts of is_successful statuses across the entire dataset.

**XQL Code**:

```SQL
config timeframe = 1d   
| dataset = sample_xql_raw   
| comp approx_top(is_successful, 2) as top_successful_statuses 
```

**Explanation**: The code identifies the top 2 most frequent values in the is_successful field. The result is an array of JSON objects, each with a "value" and a "count".

**Output**:

| top_successful_statuses |
| :---- |
| [{"value": true, "count": 7}, {"value": false, "count": 3}[] |

### Example 2: Calculating approximate top sums (with weight field)

**Goal**: Calculate the top 2 dst_domain values by the sum of their duration_seconds across the entire dataset.

**XQL Code**:

```SQL
config timeframe = 1d   
| dataset = sample_xql_raw   
| comp approx_top(dst_domain, 2, duration_seconds) as top_domains_by_duration_sum
```

**Explanation**: The code computes the sum of duration_seconds for each unique dst_domain and then returns the top 2 dst_domain values based on these sums.

**Output**:

| top_domains_by_duration_sum |
| :---- |
| [{"value": "www.mongodb.com", "sum": 60.0}, {"value": "downloads.teamviewer.com", "sum": 15.3}[] |

### Example 3: Calculating approximate top sums grouped by another field

**Goal**: Calculate the top 1 dst_domain by the sum of duration_seconds separately for is_successful = true and is_successful = false events.

**XQL Code**:

```SQL

config timeframe = 1d   
| dataset = sample_xql_raw   
| comp approx_top(dst_domain, 1, duration_seconds) as top_domain_durations_by_status by is_successful
```

**Explanation**: Groups records by their is_successful status and calculates the single dst_domain with the highest sum of duration_seconds for each group.

**Output**:

| is_successful | top_domain_durations_by_status |
| :---- | :---- |
| true | [{"value": "www.mongodb.com", "sum": 60.0}[] |
| false | [{"value": "sharepoint.microsoft.com", "sum": 2.1}[] |

### Example 4: Calculating approximate top counts with raw data inclusion

**Goal**: Include the raw events that contribute to the approximate top count calculation by using the addrawdata = true option.

**XQL Code**:

```SQL
config timeframe = 1d   
| dataset = sample_xql_raw   
| comp approx_top(is_successful, 1) addrawdata = true as raw_data_for_top_is_successful
```

**Explanation**: The code computes the top 1 most frequent is_successful value and automatically generates a new column named raw_data_for_top_is_successful containing a JSON representation of the raw events that contributed to this result.

**Output**:

| top_successful_statuses | raw_data_for_top_is_successful |
| :---- | :---- |
| [{"value": true, "count": 7}[] | [{"event_id": 101, "is_successful": true, ...}, {"event_id": 103, "is_successful": true, ...}, ...[] (up to 100 events) |

## Related Articles**

* **Stages**: [comp](../Stages/comp.md), [alter](../Stages/alter.md), [config](../Stages/config.md), timeframe  
* **Functions**: [approx_count](approx_count.md), [approx_quantiles](approx_quantiles.md)  
