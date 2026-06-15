---
ft:title: Cortex XQL Command Reference
Product: Cortex
Category: Reference Guide
Product_Category: Cortex XQL
ft:lang: en-US
ft:topicType: concept
---

# Cortex XQL Command Reference

Cortex XQL (Extended Query Language) is a powerful query language used in the Cortex platform for threat hunting, investigation, and analytics across your security data. This reference provides comprehensive documentation for all XQL functions and pipeline stages.

XQL queries are composed of **stages** connected in a pipeline, with **functions** used within those stages to transform, filter, and analyze data. This reference is organized into two main sections:

* [**Functions**](Cortex_XQL_Command_Reference/Functions/index.md) – Built-in functions for data manipulation, type conversion, string operations, mathematical calculations, bitwise operations, and more.
* [**Stages**](Cortex_XQL_Command_Reference/Stages/index.md) – Pipeline stages that define the structure and flow of an XQL query.

## Functions

| Function                                                                                                              | Description                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [`acos`](Cortex_XQL_Command_Reference/Functions/acos.md)                                                              | Calculate the inverse cosine (arccosine) of a numerical expression                                             |
| [`add`](Cortex_XQL_Command_Reference/Functions/add.md)                                                                |                                                                                                                |
| [`approx_count`](Cortex_XQL_Command_Reference/Functions/approx_count.md)                                              |                                                                                                                |
| [`approx_quantiles`](Cortex_XQL_Command_Reference/Functions/approx_quantiles.md)                                      |                                                                                                                |
| [`approx_top`](Cortex_XQL_Command_Reference/Functions/approx_top.md)                                                  |                                                                                                                |
| [`asin`](Cortex_XQL_Command_Reference/Functions/asin.md)                                                              | Calculate the inverse sine (arcsine) of a numerical expression                                                 |
| [`array_all`](Cortex_XQL_Command_Reference/Functions/array_all.md)                                                    |                                                                                                                |
| [`array_any`](Cortex_XQL_Command_Reference/Functions/array_any.md)                                                    |                                                                                                                |
| [`array_length`](Cortex_XQL_Command_Reference/Functions/array_length.md)                                              |                                                                                                                |
| [`arrayconcat`](Cortex_XQL_Command_Reference/Functions/arrayconcat.md)                                                |                                                                                                                |
| [`arraycreate`](Cortex_XQL_Command_Reference/Functions/arraycreate.md)                                                |                                                                                                                |
| [`arraydistinct`](Cortex_XQL_Command_Reference/Functions/arraydistinct.md)                                            |                                                                                                                |
| [`arrayfilter`](Cortex_XQL_Command_Reference/Functions/arrayfilter.md)                                                |                                                                                                                |
| [`arrayindex`](Cortex_XQL_Command_Reference/Functions/arrayindex.md)                                                  |                                                                                                                |
| [`arrayindexof`](Cortex_XQL_Command_Reference/Functions/arrayindexof.md)                                              |                                                                                                                |
| [`arraymap`](Cortex_XQL_Command_Reference/Functions/arraymap.md)                                                      |                                                                                                                |
| [`arraymerge`](Cortex_XQL_Command_Reference/Functions/arraymerge.md)                                                  |                                                                                                                |
| [`arrayrange`](Cortex_XQL_Command_Reference/Functions/arrayrange.md)                                                  |                                                                                                                |
| [`arraystring`](Cortex_XQL_Command_Reference/Functions/arraystring.md)                                                |                                                                                                                |
| [`avg`](Cortex_XQL_Command_Reference/Functions/avg_with_comp_stage.md)                                                |                                                                                                                |
| [`avg`](Cortex_XQL_Command_Reference/Functions/avg_with_windowcomp_stage.md)                                          |                                                                                                                |
| [`bitwise_and`](Cortex_XQL_Command_Reference/Functions/bitwise_and.md)                                                | Perform a bitwise AND operation between two integer values                                                     |
| [`bitwise_or`](Cortex_XQL_Command_Reference/Functions/bitwise_or.md)                                                  | Perform a bitwise OR operation between two integer values                                                      |
| [`bitwise_sleft`](Cortex_XQL_Command_Reference/Functions/bitwise_sleft.md)                                            | Perform a bitwise left shift operation on an integer value                                                     |
| [`bitwise_sright`](Cortex_XQL_Command_Reference/Functions/bitwise_sright.md)                                          | Perform a bitwise right shift operation on an integer value                                                    |
| [`bitwise_xor`](Cortex_XQL_Command_Reference/Functions/bitwise_xor.md)                                                | Perform a bitwise exclusive OR (XOR) operation between two integer values                                      |
| [`cbrt`](Cortex_XQL_Command_Reference/Functions/cbrt.md)                                                              | Calculate the cube root of a numeric value                                                                     |
| [`ceil`](Cortex_XQL_Command_Reference/Functions/ceil.md)                                                              | Round a number up to the nearest integer                                                                       |
| [`coalesce`](Cortex_XQL_Command_Reference/Functions/coalesce.md)                                                      |                                                                                                                |
| [`concat`](Cortex_XQL_Command_Reference/Functions/concat.md)                                                          |                                                                                                                |
| [`convert_from_base_64`](Cortex_XQL_Command_Reference/Functions/convert_from_base_64.md)                              |                                                                                                                |
| [`convert_to_base_64`](Cortex_XQL_Command_Reference/Functions/convert_to_base_64.md)                                  |                                                                                                                |
| [`cos`](Cortex_XQL_Command_Reference/Functions/cos.md)                                                                | Calculate the cosine of a numeric value specified in radians                                                   |
| [`cosine_distance`](Cortex_XQL_Command_Reference/Functions/cosine_distance.md)                                        | Calculate the cosine distance between two numeric vectors                                                      |
| [`cot`](Cortex_XQL_Command_Reference/Functions/cot.md)                                                                | Calculate the cotangent of a numeric value specified in radians                                                |
| [`count`](Cortex_XQL_Command_Reference/Functions/count_with_comp_stage.md)                                            |                                                                                                                |
| [`count`](Cortex_XQL_Command_Reference/Functions/count_with_windowcomp_stage.md)                                      |                                                                                                                |
| [`count_distinct`](Cortex_XQL_Command_Reference/Functions/count_distinct.md)                                          |                                                                                                                |
| [`csc`](Cortex_XQL_Command_Reference/Functions/csc.md)                                                                | Calculate the cosecant of a numeric value specified in radians                                                 |
| [`current_time`](Cortex_XQL_Command_Reference/Functions/current_time.md)                                              |                                                                                                                |
| [`date_floor`](Cortex_XQL_Command_Reference/Functions/date_floor.md)                                                  |                                                                                                                |
| [`div`](Cortex_XQL_Command_Reference/Functions/div.md)                                                                | Perform integer division of two numeric values                                                                 |
| [`divide`](Cortex_XQL_Command_Reference/Functions/divide.md)                                                          |                                                                                                                |
| [`earliest`](Cortex_XQL_Command_Reference/Functions/earliest.md)                                                      |                                                                                                                |
| [`euclidean_distance`](Cortex_XQL_Command_Reference/Functions/euclidean_distance.md)                                  | Calculate the Euclidean distance between two numeric vectors                                                   |
| [`exp`](Cortex_XQL_Command_Reference/Functions/exp.md)                                                                | Calculate the value of e raised to the power of a numeric value                                                |
| [`extract_time`](Cortex_XQL_Command_Reference/Functions/extract_time.md)                                              |                                                                                                                |
| [`extract_url_host`](Cortex_XQL_Command_Reference/Functions/extract_url_host.md)                                      |                                                                                                                |
| [`extract_url_pub_suffix`](Cortex_XQL_Command_Reference/Functions/extract_url_pub_suffix.md)                          |                                                                                                                |
| [`extract_url_registered_domain`](Cortex_XQL_Command_Reference/Functions/extract_url_registered_domain.md)            |                                                                                                                |
| [`first`](Cortex_XQL_Command_Reference/Functions/first.md)                                                            |                                                                                                                |
| [`first_value`](Cortex_XQL_Command_Reference/Functions/first_value.md)                                                |                                                                                                                |
| [`floor`](Cortex_XQL_Command_Reference/Functions/floor.md)                                                            |                                                                                                                |
| [`format_string`](Cortex_XQL_Command_Reference/Functions/format_string.md)                                            |                                                                                                                |
| [`format_timestamp`](Cortex_XQL_Command_Reference/Functions/format_timestamp.md)                                      |                                                                                                                |
| [`greatest`](Cortex_XQL_Command_Reference/Functions/greatest.md)                                                      | Return the largest value from a list of expressions                                                            |
| [`if`](Cortex_XQL_Command_Reference/Functions/if.md)                                                                  |                                                                                                                |
| [`incidr`](Cortex_XQL_Command_Reference/Functions/incidr.md)                                                          |                                                                                                                |
| [`incidr6`](Cortex_XQL_Command_Reference/Functions/incidr6.md)                                                        |                                                                                                                |
| [`incidrlist`](Cortex_XQL_Command_Reference/Functions/incidrlist.md)                                                  |                                                                                                                |
| [`int_to_ip`](Cortex_XQL_Command_Reference/Functions/int_to_ip.md)                                                    |                                                                                                                |
| [`ip_to_int`](Cortex_XQL_Command_Reference/Functions/ip_to_int.md)                                                    |                                                                                                                |
| [`is_ipv4`](Cortex_XQL_Command_Reference/Functions/is_ipv4.md)                                                        |                                                                                                                |
| [`is_ipv6`](Cortex_XQL_Command_Reference/Functions/is_ipv6.md)                                                        |                                                                                                                |
| [`is_known_private_ipv4`](Cortex_XQL_Command_Reference/Functions/is_known_private_ipv4.md)                            |                                                                                                                |
| [`is_known_private_ipv6`](Cortex_XQL_Command_Reference/Functions/is_known_private_ipv6.md)                            |                                                                                                                |
| [`json_extract`](Cortex_XQL_Command_Reference/Functions/json_extract.md)                                              |                                                                                                                |
| [`json_extract_array`](Cortex_XQL_Command_Reference/Functions/json_extract_array.md)                                  |                                                                                                                |
| [`json_extract_scalar`](Cortex_XQL_Command_Reference/Functions/json_extract_scalar.md)                                |                                                                                                                |
| [`json_extract_scalar_array`](Cortex_XQL_Command_Reference/Functions/json_extract_scalar_array.md)                    |                                                                                                                |
| [`json_path_extract`](Cortex_XQL_Command_Reference/Functions/json_path_extract.md)                                    |                                                                                                                |
| [`json_functions_reference`](Cortex_XQL_Command_Reference/Functions/json_functions_reference.md)                      | A comprehensive guide to the four JSON extraction functions                                                    |
| [`lag`](Cortex_XQL_Command_Reference/Functions/lag.md)                                                                |                                                                                                                |
| [`last`](Cortex_XQL_Command_Reference/Functions/last.md)                                                              |                                                                                                                |
| [`last_value`](Cortex_XQL_Command_Reference/Functions/last_value.md)                                                  |                                                                                                                |
| [`latest`](Cortex_XQL_Command_Reference/Functions/latest.md)                                                          |                                                                                                                |
| [`least`](Cortex_XQL_Command_Reference/Functions/least.md)                                                            | Return the smallest value from a list of expressions                                                           |
| [`len`](Cortex_XQL_Command_Reference/Functions/len.md)                                                                |                                                                                                                |
| [`list (comp)`](Cortex_XQL_Command_Reference/Functions/list_with_comp_stage.md)                                       | Collect all values of a field and return them as an array within the comp stage                                |
| [`ln`](Cortex_XQL_Command_Reference/Functions/ln.md)                                                                  | Calculate the natural logarithm (base e) of a numeric value                                                    |
| [`log`](Cortex_XQL_Command_Reference/Functions/log.md)                                                                | Calculate the logarithm of a numeric value with a specified base                                               |
| [`log10`](Cortex_XQL_Command_Reference/Functions/log10.md)                                                            | Calculate the base-10 logarithm of a numeric value                                                             |
| [`lowercase`](Cortex_XQL_Command_Reference/Functions/lowercase.md)                                                    |                                                                                                                |
| [`ltrim`](Cortex_XQL_Command_Reference/Functions/ltrim.md)                                                            |                                                                                                                |
| [`max (comp)`](Cortex_XQL_Command_Reference/Functions/max_with_comp_stage.md)                                         | Return the maximum value of a field within the comp stage                                                      |
| [`max (windowcomp)`](Cortex_XQL_Command_Reference/Functions/max_with_windowcomp_stage.md)                             | Compute the maximum value of a field over a window of rows within the windowcomp stage                         |
| [`md5`](Cortex_XQL_Command_Reference/Functions/md5.md)                                                                |                                                                                                                |
| [`median (comp)`](Cortex_XQL_Command_Reference/Functions/median_with_comp_stage.md)                                   | Return the median value of a numeric field within the comp stage                                               |
| [`median (windowcomp)`](Cortex_XQL_Command_Reference/Functions/median_with_windowcomp_stage.md)                       | Compute the median value of a numeric field over a window of rows within the windowcomp stage                  |
| [`min (comp)`](Cortex_XQL_Command_Reference/Functions/min_with_comp_stage.md)                                         | Return the minimum value of a field within the comp stage                                                      |
| [`min (windowcomp)`](Cortex_XQL_Command_Reference/Functions/min_with_windowcomp_stage.md)                             | Compute the minimum value of a field over a window of rows within the windowcomp stage                         |
| [`mod`](Cortex_XQL_Command_Reference/Functions/mod.md)                                                                | Calculate the remainder (modulus) of the division of two numeric values                                        |
| [`multiply`](Cortex_XQL_Command_Reference/Functions/multiply.md)                                                      |                                                                                                                |
| [`object_create`](Cortex_XQL_Command_Reference/Functions/object_create.md)                                            |                                                                                                                |
| [`object_merge`](Cortex_XQL_Command_Reference/Functions/object_merge.md)                                              |                                                                                                                |
| [`parse_epoch`](Cortex_XQL_Command_Reference/Functions/parse_epoch.md)                                                |                                                                                                                |
| [`parse_timestamp`](Cortex_XQL_Command_Reference/Functions/parse_timestamp.md)                                        |                                                                                                                |
| [`pow`](Cortex_XQL_Command_Reference/Functions/pow.md)                                                                |                                                                                                                |
| [`power`](Cortex_XQL_Command_Reference/Functions/power.md)                                                            | Raise a number to the power of another number (alias for pow)                                                  |
| [`rand`](Cortex_XQL_Command_Reference/Functions/rand.md)                                                              | Generate a pseudo-random floating-point number between 0 and 1                                                 |
| [`range_bucket`](Cortex_XQL_Command_Reference/Functions/range_bucket.md)                                              | Determine which bucket a numeric value falls into given an array of boundaries                                 |
| [`rank (windowcomp)`](Cortex_XQL_Command_Reference/Functions/rank_with_windowcomp_stage.md)                           | Assign a rank to each row within a partition in the windowcomp stage                                           |
| [`regexcapture`](Cortex_XQL_Command_Reference/Functions/regexcapture.md)                                              |                                                                                                                |
| [`regextract`](Cortex_XQL_Command_Reference/Functions/regextract.md)                                                  | Extract a substring from a field value using a regular expression pattern                                      |
| [`replace`](Cortex_XQL_Command_Reference/Functions/replace.md)                                                        |                                                                                                                |
| [`replex`](Cortex_XQL_Command_Reference/Functions/replex.md)                                                          |                                                                                                                |
| [`round`](Cortex_XQL_Command_Reference/Functions/round.md)                                                            |                                                                                                                |
| [`row_number (windowcomp)`](Cortex_XQL_Command_Reference/Functions/row_number_with_windowcomp_stage.md)               | Assign a unique sequential integer to each row within a partition in the windowcomp stage                      |
| [`rtrim`](Cortex_XQL_Command_Reference/Functions/rtrim.md)                                                            |                                                                                                                |
| [`safe_add`](Cortex_XQL_Command_Reference/Functions/safe_add.md)                                                      | Perform addition with overflow protection, returning null on overflow                                          |
| [`safe_divide`](Cortex_XQL_Command_Reference/Functions/safe_divide.md)                                                | Perform division with error protection, returning null on division by zero                                     |
| [`safe_multiply`](Cortex_XQL_Command_Reference/Functions/safe_multiply.md)                                            | Perform multiplication with overflow protection, returning null on overflow                                    |
| [`safe_negate`](Cortex_XQL_Command_Reference/Functions/safe_negate.md)                                                | Negate a numeric value with overflow protection, returning null on overflow                                    |
| [`safe_subtract`](Cortex_XQL_Command_Reference/Functions/safe_subtract.md)                                            | Perform subtraction with overflow protection, returning null on overflow                                       |
| [`sec`](Cortex_XQL_Command_Reference/Functions/sec.md)                                                                | Calculate the secant of a numeric value specified in radians                                                   |
| [`sha1`](Cortex_XQL_Command_Reference/Functions/sha1.md)                                                              |                                                                                                                |
| [`sha256`](Cortex_XQL_Command_Reference/Functions/sha256.md)                                                          |                                                                                                                |
| [`sha512`](Cortex_XQL_Command_Reference/Functions/sha512.md)                                                          |                                                                                                                |
| [`sign`](Cortex_XQL_Command_Reference/Functions/sign.md)                                                              | Determine the sign of a numeric value (-1, 0, or 1)                                                            |
| [`sin`](Cortex_XQL_Command_Reference/Functions/sin.md)                                                                | Calculate the sine of a numeric value specified in radians                                                     |
| [`split`](Cortex_XQL_Command_Reference/Functions/split.md)                                                            |                                                                                                                |
| [`sqrt`](Cortex_XQL_Command_Reference/Functions/sqrt.md)                                                              | Calculate the square root of a numeric value                                                                   |
| [`stddev_population (comp)`](Cortex_XQL_Command_Reference/Functions/stddev_population_with_comp_stage.md)             | Compute the population standard deviation of a numeric field within the comp stage                             |
| [`stddev_population (windowcomp)`](Cortex_XQL_Command_Reference/Functions/stddev_population_with_windowcomp_stage.md) | Compute the population standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`stddev_sample (comp)`](Cortex_XQL_Command_Reference/Functions/stddev_sample_with_comp_stage.md)                     | Compute the sample standard deviation of a numeric field within the comp stage                                 |
| [`stddev_sample (windowcomp)`](Cortex_XQL_Command_Reference/Functions/stddev_sample_with_windowcomp_stage.md)         | Compute the sample standard deviation of a numeric field over a window of rows within the windowcomp stage     |
| [`string_count`](Cortex_XQL_Command_Reference/Functions/string_count.md)                                              |                                                                                                                |
| [`subtract`](Cortex_XQL_Command_Reference/Functions/subtract.md)                                                      |                                                                                                                |
| [`sum (comp)`](Cortex_XQL_Command_Reference/Functions/sum_with_comp_stage.md)                                         | Compute the sum of a numeric field within the comp stage                                                       |
| [`sum (windowcomp)`](Cortex_XQL_Command_Reference/Functions/sum_with_windowcomp_stage.md)                             | Compute the sum of a numeric field over a window of rows within the windowcomp stage                           |
| [`tan`](Cortex_XQL_Command_Reference/Functions/tan.md)                                                                | Calculate the tangent of a numeric value specified in radians                                                  |
| [`time_frame_end`](Cortex_XQL_Command_Reference/Functions/time_frame_end.md)                                          |                                                                                                                |
| [`timestamp_diff`](Cortex_XQL_Command_Reference/Functions/timestamp_diff.md)                                          |                                                                                                                |
| [`timestamp_seconds`](Cortex_XQL_Command_Reference/Functions/timestamp_seconds.md)                                    |                                                                                                                |
| [`to_boolean`](Cortex_XQL_Command_Reference/Functions/to_boolean.md)                                                  |                                                                                                                |
| [`to_epoch`](Cortex_XQL_Command_Reference/Functions/to_epoch.md)                                                      |                                                                                                                |
| [`to_float`](Cortex_XQL_Command_Reference/Functions/to_float.md)                                                      |                                                                                                                |
| [`to_integer`](Cortex_XQL_Command_Reference/Functions/to_integer.md)                                                  |                                                                                                                |
| [`to_json_string`](Cortex_XQL_Command_Reference/Functions/to_json_string.md)                                          |                                                                                                                |
| [`to_number`](Cortex_XQL_Command_Reference/Functions/to_number.md)                                                    |                                                                                                                |
| [`to_string`](Cortex_XQL_Command_Reference/Functions/to_string.md)                                                    |                                                                                                                |
| [`to_timestamp`](Cortex_XQL_Command_Reference/Functions/to_timestamp.md)                                              |                                                                                                                |
| [`trim`](Cortex_XQL_Command_Reference/Functions/trim.md)                                                              |                                                                                                                |
| [`trunc`](Cortex_XQL_Command_Reference/Functions/trunc.md)                                                            | Truncate a numeric value to a specified number of decimal places                                               |
| [`uppercase`](Cortex_XQL_Command_Reference/Functions/uppercase.md)                                                    |                                                                                                                |
| [`values`](Cortex_XQL_Command_Reference/Functions/values.md)                                                          | Collect all distinct values of a field and return them as an array within the comp stage                       |
| [`var`](Cortex_XQL_Command_Reference/Functions/var.md)                                                                | Compute the variance of a numeric field within the comp stage                                                  |
| [`wildcard_match`](Cortex_XQL_Command_Reference/Functions/wildcard_match.md)                                          |                                                                                                                |

## Stages

| Stage                                                               | Description |
| ------------------------------------------------------------------- | ----------- |
| [`alter`](Cortex_XQL_Command_Reference/Stages/alter.md)             |             |
| [`arrayexpand`](Cortex_XQL_Command_Reference/Stages/arrayexpand.md) |             |
| [`bin`](Cortex_XQL_Command_Reference/Stages/bin.md)                 |             |
| [`call`](Cortex_XQL_Command_Reference/Stages/call.md)               |             |
| [`comp`](Cortex_XQL_Command_Reference/Stages/comp.md)               |             |
| [`config`](Cortex_XQL_Command_Reference/Stages/config.md)           |             |
| [`dataset`](Cortex_XQL_Command_Reference/Stages/dataset.md)         |             |
| [`dedup`](Cortex_XQL_Command_Reference/Stages/dedup.md)             |             |
| [`fields`](Cortex_XQL_Command_Reference/Stages/fields.md)           |             |
| [`filter`](Cortex_XQL_Command_Reference/Stages/filter.md)           |             |
| [`iploc`](Cortex_XQL_Command_Reference/Stages/iploc.md)             |             |
| [`join`](Cortex_XQL_Command_Reference/Stages/join.md)               |             |
| [`limit`](Cortex_XQL_Command_Reference/Stages/limit.md)             |             |
| [`presets`](Cortex_XQL_Command_Reference/Stages/presets.md)         |             |
| [`replacenull`](Cortex_XQL_Command_Reference/Stages/replacenull.md) |             |
| [`search`](Cortex_XQL_Command_Reference/Stages/search.md)           |             |
| [`sort`](Cortex_XQL_Command_Reference/Stages/sort.md)               |             |
| [`tag`](Cortex_XQL_Command_Reference/Stages/tag.md)                 |             |
| [`target`](Cortex_XQL_Command_Reference/Stages/target.md)           |             |
| [`top`](Cortex_XQL_Command_Reference/Stages/top.md)                 |             |
| [`transaction`](Cortex_XQL_Command_Reference/Stages/transaction.md) |             |
| [`union`](Cortex_XQL_Command_Reference/Stages/union.md)             |             |
| [`view`](Cortex_XQL_Command_Reference/Stages/view.md)               |             |
| [`windowcomp`](Cortex_XQL_Command_Reference/Stages/windowcomp.md)   |             |
