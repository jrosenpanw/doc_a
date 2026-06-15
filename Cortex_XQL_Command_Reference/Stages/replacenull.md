---
ft:title: "replacenull"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "reference"
---

# replacenull

Use the `replacenull` stage to ensure data completeness by replacing null values within a specified field.

## Syntax

```sql
replacenull <field> = <text_string>
```

## Parameters

| Name          | Type   | Required | Description                                                                                                                |
| ------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| `field`       | string | Yes      | The name of the field whose null values you wish to replace.                                                               |
| `text_string` | string | Yes      | The literal string value that will replace any `NULL` occurrences in the specified field. This must be enclosed in quotes. |

## Returns

The `replacenull` stage returns the dataset with the specified field modified, where all `NULL` values have been substituted with the provided replacement string.

## Usage notes

* If you employ the `replacenull` stage, any subsequent stages that refer to the modified field's value must use the newly defined replacement string instead of checking for `NULL`.
* Apply `filter` stages as early as possible in your query. This reduces the total dataset size before `replacenull` processes the records, minimizing the amount of data it needs to operate on.
* Utilize the `fields` stage immediately after initial filtering to select only the necessary columns. This reduces the data footprint passed to `replacenull` and subsequent stages, improving overall query performance.

## Examples

### Example 1: Basic replacenull on an existing field with nulls

**Goal**: Replace `NULL` values in a field that inherently contains them in the dataset.

**XQL code**:

```sql
config timeframe = 1d // Use a practical timeframe
| dataset = sample_xql_raw // Specify the dataset
| fields event_id, ipv6_address // Select only necessary fields early
| replacenull ipv6_address = "Not Applicable" // Replace NULL values in ipv6_address
| limit 5 // Limit results for brevity
```

**Explanation**: The `replacenull ipv6_address = "Not Applicable"` stage replaces `NULL` values in the `ipv6_address` field with the string "Not Applicable" for records 101, 102, 104, and 105.

**Output**:

| EVENT_ID | IPV6_ADDRESS   |
| -------- | -------------- |
| 101      | Not Applicable |
| 102      | Not Applicable |
| 103      | 2001:0db8::1   |
| 104      | Not Applicable |
| 105      | Not Applicable |

### Example 2: replacenull on a field derived from a JSON function

**Goal**: Replace `NULL` values in a field created by an `alter` stage using a JSON function, where the extracted value might be `NULL` if the key does not exist.

**XQL code**:

```sql
config timeframe = 1d
| dataset = sample_xql_raw
| fields event_id, simple_json_data // Select relevant fields, including the JSON source
| alter json_code = json_extract_scalar(simple_json_data, "$.code") // Extract 'code' field; can be NULL
| replacenull json_code = "Code Not Found" // Replace NULLs in the new 'json_code' field
| limit 5
```

**Explanation**: The query extracts the value of the "code" key using `json_extract_scalar(simple_json_data, "$.code")`. For records where this key does not exist (102, 103, 104, 105), the result is `NULL`. The `replacenull json_code = "Code Not Found"` stage then replaces these `NULL` values.

**Output**:

| EVENT_ID | SIMPLE_JSON_DATA                                 | JSON_CODE      |
| -------- | ------------------------------------------------ | -------------- |
| 101      | {"status": "ok", "code": 200}                    | 200            |
| 102      | {"status": "fail", "error": "access_denied"}     | Code Not Found |
| 103      | {"connection_id": "CONN-001", "protocol": "TCP"} | Code Not Found |
| 104      | {"health": "good"}                               | Code Not Found |
| 105      | {"transform_stage": 1}                           | Code Not Found |

### Example 3: Filtering based on the replaced value

**Goal**: Demonstrate how subsequent `filter` stages must use the replacement string when querying for values that were originally `NULL`.

**XQL code**:

```sql
config timeframe = 1d
| dataset = sample_xql_raw
| fields event_id, ipv4_address // Select necessary fields
| replacenull ipv4_address = "UNKNOWN_IP" // Replace NULLs in ipv4_address
| filter ipv4_address = "UNKNOWN_IP" // Filter using the replacement string
| limit 5
```

**Explanation**: The `replacenull ipv4_address = "UNKNOWN_IP"` stage replaces `NULL` entries in `ipv4_address`. Since `ipv4_address` is `NULL` for `event_id` 103, 107, and 109, the subsequent filter `filter ipv4_address = "UNKNOWN_IP"` successfully identifies and returns only those records.

**Output**:

| EVENT_ID | IPV4_ADDRESS |
| -------- | ------------ |
| 103      | UNKNOWN_IP   |
| 107      | UNKNOWN_IP   |
| 109      | UNKNOWN_IP   |

## Related articles

* **Stages**: [`alter`](alter.md), [`filter`](filter.md), [`fields`](fields.md)
* **Functions**: [`json_extract_scalar`](../Functions/json_extract_scalar.md)
* **Datasets**: [`xdr_data`](https://www.google.com/search?q=%5Bhttps://docs-cortex.paloaltonetworks.com/r/Cortex-XQL-Schema-Reference-Guide/Introduction%5D(https://docs-cortex.paloaltonetworks.com/r/Cortex-XQL-Schema-Reference-Guide/Introduction))
