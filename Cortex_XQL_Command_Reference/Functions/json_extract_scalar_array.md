---
ft:title: "json_extract_scalar_array"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "reference"
---

# json_extract_scalar_array

Use the `json_extract_scalar_array()` function to extract a JSON array containing scalar values (strings, numbers, booleans) from a JSON object and represent it as an XQL array of strings.

## Syntax

```sql
json_extract_scalar_array (<json_array_string>, <json_path>)
```

When a Cortex Data Model (XDM) field is used in the <json_path> and contains a dot (.) character, for example xdm.source.host.device_id, use the syntax:

```sql
json_extract_scalar_array(<json_array_string>, "['<json_field>']")
```

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `json_array_string` | string | Yes | The string that represents a JSON array. If the input is a field, use `to_json_string()` to convert it first. |
| `json_path` | string | Yes | The identifier of the data within the JSON object to extract, using dot-notation. In regular syntax, the root is represented by `$`. If a field name contains special characters (like `.` or `:`), enclose it in single quotes within brackets (for example, `['<json_field>']`). |

## Returns

The `json_extract_scalar_array()` function returns an XQL-native array containing the extracted scalar values. Unlike `json_extract_array()`, the scalar values within the returned array are not enclosed in double quotes. If the target array does not exist, or the JSONPath is invalid, it returns NULL.

## Usage notes

* If the input field is not already a string representing a JSON object or array, you must use the `to_json_string()` function to convert it.
* JSON field names are case-sensitive. The key-to-field pairing in your XQL query must be identical to the JSON for results to be found.
* This function does not support a syntactic sugar format; you must use the regular syntax.
* If a field in the `<json_path>` contains characters like a dot (`.`) or colon (`:`), you must use the bracket notation `['<json_field>']`. Note that for XDM fields, paths requiring escaping for invalid JSON characters might be unsupported.

## Examples

### Example 1: Extracting a scalar array from a nested JSON field (with special characters in path)

**Goal**: Extract the `ipv4_address` array from the `json_with_nested_array` field, handling special characters in the JSON path.

**XQL code**:

```sql
config timeframe = 1d 
| dataset = sample_xql_raw 
| alter json_string_data = to_json_string(json_with_nested_array) 
| alter extracted_ips = json_extract_scalar_array(json_string_data, "$['device.info']['ip.addresses']") 
| fields event_id, json_with_nested_array, extracted_ips 
| limit 3 
```

**Explanation**: The query first converts the `json_with_nested_array` object into a JSON-formatted string using `to_json_string()`. The query then uses `json_extract_scalar_array()` to extract the array found at `$['device.info']['ip.addresses']`. The bracket notation is used because `ip.addresses` contains a dot. The resulting `extracted_ips` array contains scalar values without quotes.

**Output**:

| EVENT_ID | JSON_WITH_NESTED_ARRAY | EXTRACTED_IPS |
| --- | --- | --- |
| 101 | {"device.info": {"ip.addresses": ["172.16.6.7", "172.16.8.9"]}} | [172.16.6.7, 172.16.8.9] |
| 102 | {"device.info": {"ip.addresses": ["10.1.2.3", "10.2.3.4"]}} | [10.1.2.3, 10.2.3.4] |
| 103 | {"metadata": {"tags": ["critical", "event"], "version": "2.1"}} | NULL |

### Example 2: Extracting an Array of String Tags

**Goal**: Extract the array of text tags associated with each alert from a JSON payload.

**XQL Code**:

```sql
config timeframe = 1d  
| dataset = sample_xql_raw  
| filter json_payload != null  
| alter tags_array = json_extract_scalar_array(json_payload, "$.alert.tags")  
| fields event_id, tags_array  
| limit 2
```

**Explanation**: You use the json_extract_scalar_array() function in the alter stage to target the $.alert.tags path within the json_payload string. The function extracts the JSON array of strings and converts it into a standard XQL array assigned to tags_array.

**Output**:

| EVENT_ID | TAGS_ARRAY |
| :---- | :---- |
| 101 | ![][image1] |
| 102 | ![][image2] |

### Example 3: Extracting a Mixed Scalar Array

**Goal**: Extract an array containing mixed scalar types (strings, numbers, booleans) and observe the string conversion.

**XQL Code**:

config timeframe = 1d  
| dataset = sample_xql_raw  
| filter metrics_payload != null  
| alter mixed_array = json_extract_scalar_array(metrics_payload, "$.device.status_codes")  
| fields event_id, mixed_array  
| limit 2

**Explanation**: The target JSONPath $.device.status_codes points to an array like ["active", 200, true]. The json_extract_scalar_array() function extracts these values and casts the number 200 and the boolean true into strings, resulting in an XQL array of strings: ["active", "200", "true"].

**Output**:

| EVENT_ID | MIXED_ARRAY |
| :---- | :---- |
| 201 | ![][image3] |
| 202 | ![][image4] |

### Example 4: Extract an array of strings using json_extract_scalar_array

**Goal**: Extract strings using json_extract_scalar_array function.

**XQL Code**:

```sql
dataset = xdr_data  
| alter parsed_action_processes = json_extract_scalar_array(action_processes, "$.*")   
| fields parsed_action_processes, action_processes   
| filter parsed_action_processes != null   
| limit 1
```

**Explanation**: The results return an array of strings in the parsed_action_processes field.

**Output**:

| PARSED_ACTION_PROCESSES | ACTION_PROCESSES |
| :---- | :---- |
| ["123", "2039", "332", "0"] | [123, 2039, 332, 0] |

### Example 5: Determine the string length using json_extract_scalar_array and array_length

**Goal**: Find the length of the string array by using json_extract_scalar_array and array_length functions.

**XQL Code**:

```sql
dataset = xdr_data  
| filter action_processes != null   
| alter processes_length = array_length(json_extract_scalar_array(action_processes, "$.*"))  
| fields action_processes, processes_length  
| limit 1
```

**Explanation**: Extracting the array to string format allows you to determine the array's length.

**Output**:

| ACTION_PROCESSES | PROCESSES_LENGTH |
| :---- | :---- |
| [123, 2039, 332, 0] | 4 |

### Example 6: Querying normalized network traffic

**Goal**: Find all blocked network connections across multiple firewall vendors using the unified XDM schema.

**XQL Code**:

```sql
config timeframe = 1d  
| dataset = xdm.network.session  
| filter xdm.event.outcome = "blocked" or xdm.event.outcome = "denied"  
| comp count(xdm.event.id) as block_count by xdm.source.ipv4, xdm.target.ipv4  
| sort desc block_count  
| limit 5
```

**Explanation**: By querying the xdm.network.session dataset, you search across all ingested network logs that have been mapped to the XDM schema, regardless of the original vendor. The query filters for blocked traffic using the normalized xdm.event.outcome field. The query then aggregates the count of blocked events by the normalized source and target IP addresses (xdm.source.ipv4, xdm.target.ipv4), sorts them to find the top offenders, and limits the output to the top 5.

**Output**:

| XDM.SOURCE.IPV4 | XDM.TARGET.IPV4 | BLOCK_COUNT |
| :---- | :---- | :---- |
| 192.168.1.50 | 8.8.8.8 | 4500 |
| 10.0.0.15 | 1.1.1.1 | 3200 |
| 172.16.5.100 | 9.9.9.9 | 1500 |
| 192.168.1.10 | 8.8.4.4 | 850 |
| 10.0.0.55 | 208.67.222.222 | 420 |

### Example 7: Extracting XDM normalized fields

**Goal**: Extract the xdm.file.permissions.owner in the xdm.finding.normalized_fields array, which returns true when the string value is one of the following: r or w.

**XQL Code**:

```sql
dataset = findings   
| filter JSON_EXTRACT_SCALAR_ARRAY(xdm.finding.normalized_fields, "$['xdm.file.permissions.owner']") in ("r", "w")   
| fields xdm.finding.normalized_fields
```

**Explanation**: This query searches the findings dataset. The query uses the JSON_EXTRACT_SCALAR_ARRAY() function to extract the JSON array corresponding to the XDM field xdm.file.permissions.owner from within the xdm.finding.normalized_fields object. The filter stage evaluates to true if the extracted array contains the strings "r" or "w", returning only those relevant records to the result set.

**Output**:

| _TIME | XDM.FINDING.NORMALIZED_FIELDS |
| :---- | :---- |
| Jan 15th 2025 09:10:44 | { "xdm.file.permissions.owner": [ "r", "w", "x" ] } |

## Related articles

* **Stages**: [`alter`](../Stages/alter.md), [`fields`](../Stages/fields.md), [`limit`](../Stages/limit.md)
* **Functions**: [`to_json_string`](to_json_string.md), [`json_extract_array`](json_extract_array.md)
* **Datasets**: [`xdr_data`](https://www.google.com/search?q=%5Bhttps://docs-cortex.paloaltonetworks.com/r/Cortex-XQL-Schema-Reference-Guide/Introduction%5D(https://docs-cortex.paloaltonetworks.com/r/Cortex-XQL-Schema-Reference-Guide/Introduction))
