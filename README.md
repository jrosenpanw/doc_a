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

* [**Functions**](readme/functions/) – Built-in functions, indexes, and detailed reference pages.
* [**Stages**](readme/stages/) – Pipeline stages, indexes, and detailed reference pages.

## Functions

| Function                                                                                        | Description                                                                                                    |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [`acos`](readme/functions/acos.md)                                                              | Calculate the inverse cosine (arccosine) of a numerical expression                                             |
| [`add`](readme/functions/add.md)                                                                |                                                                                                                |
| [`approx_count`](readme/functions/approx_count.md)                                              |                                                                                                                |
| [`approx_quantiles`](readme/functions/approx_quantiles.md)                                      |                                                                                                                |
| [`approx_top`](readme/functions/approx_top.md)                                                  |                                                                                                                |
| [`asin`](readme/functions/asin.md)                                                              | Calculate the inverse sine (arcsine) of a numerical expression                                                 |
| [`array_all`](readme/functions/array_all.md)                                                    |                                                                                                                |
| [`array_any`](readme/functions/array_any.md)                                                    |                                                                                                                |
| [`array_length`](readme/functions/array_length.md)                                              |                                                                                                                |
| [`arrayconcat`](readme/functions/arrayconcat.md)                                                |                                                                                                                |
| [`arraycreate`](readme/functions/arraycreate.md)                                                |                                                                                                                |
| [`arraydistinct`](readme/functions/arraydistinct.md)                                            |                                                                                                                |
| [`arrayfilter`](readme/functions/arrayfilter.md)                                                |                                                                                                                |
| [`arrayindex`](readme/functions/arrayindex.md)                                                  |                                                                                                                |
| [`arrayindexof`](readme/functions/arrayindexof.md)                                              |                                                                                                                |
| [`arraymap`](readme/functions/arraymap.md)                                                      |                                                                                                                |
| [`arraymerge`](readme/functions/arraymerge.md)                                                  |                                                                                                                |
| [`arrayrange`](readme/functions/arrayrange.md)                                                  |                                                                                                                |
| [`arraystring`](readme/functions/arraystring.md)                                                |                                                                                                                |
| [`avg`](readme/functions/avg_with_comp_stage.md)                                                |                                                                                                                |
| [`avg`](readme/functions/avg_with_windowcomp_stage.md)                                          |                                                                                                                |
| [`bitwise_and`](readme/functions/bitwise_and.md)                                                | Perform a bitwise AND operation between two integer values                                                     |
| [`bitwise_or`](readme/functions/bitwise_or.md)                                                  | Perform a bitwise OR operation between two integer values                                                      |
| [`bitwise_sleft`](readme/functions/bitwise_sleft.md)                                            | Perform a bitwise left shift operation on an integer value                                                     |
| [`bitwise_sright`](readme/functions/bitwise_sright.md)                                          | Perform a bitwise right shift operation on an integer value                                                    |
| [`bitwise_xor`](readme/functions/bitwise_xor.md)                                                | Perform a bitwise exclusive OR (XOR) operation between two integer values                                      |
| [`cbrt`](readme/functions/cbrt.md)                                                              | Calculate the cube root of a numeric value                                                                     |
| [`ceil`](readme/functions/ceil.md)                                                              | Round a number up to the nearest integer                                                                       |
| [`coalesce`](readme/functions/coalesce.md)                                                      |                                                                                                                |
| [`concat`](readme/functions/concat.md)                                                          |                                                                                                                |
| [`convert_from_base_64`](readme/functions/convert_from_base_64.md)                              |                                                                                                                |
| [`convert_to_base_64`](readme/functions/convert_to_base_64.md)                                  |                                                                                                                |
| [`cos`](readme/functions/cos.md)                                                                | Calculate the cosine of a numeric value specified in radians                                                   |
| [`cosine_distance`](readme/functions/cosine_distance.md)                                        | Calculate the cosine distance between two numeric vectors                                                      |
| [`cot`](readme/functions/cot.md)                                                                | Calculate the cotangent of a numeric value specified in radians                                                |
| [`count`](readme/functions/count_with_comp_stage.md)                                            |                                                                                                                |
| [`count`](readme/functions/count_with_windowcomp_stage.md)                                      |                                                                                                                |
| [`count_distinct`](readme/functions/count_distinct.md)                                          |                                                                                                                |
| [`csc`](readme/functions/csc.md)                                                                | Calculate the cosecant of a numeric value specified in radians                                                 |
| [`current_time`](readme/functions/current_time.md)                                              |                                                                                                                |
| [`date_floor`](readme/functions/date_floor.md)                                                  |                                                                                                                |
| [`divide`](readme/functions/divide.md)                                                          |                                                                                                                |
| [`earliest`](readme/functions/earliest.md)                                                      |                                                                                                                |
| [`euclidean_distance`](readme/functions/euclidean_distance.md)                                  | Calculate the Euclidean distance between two numeric vectors                                                   |
| [`exp`](readme/functions/exp.md)                                                                | Calculate the value of e raised to the power of a numeric value                                                |
| [`extract_time`](readme/functions/extract_time.md)                                              |                                                                                                                |
| [`extract_url_host`](readme/functions/extract_url_host.md)                                      |                                                                                                                |
| [`extract_url_pub_suffix`](readme/functions/extract_url_pub_suffix.md)                          |                                                                                                                |
| [`extract_url_registered_domain`](readme/functions/extract_url_registered_domain.md)            |                                                                                                                |
| [`first`](readme/functions/first.md)                                                            |                                                                                                                |
| [`first_value`](readme/functions/first_value.md)                                                |                                                                                                                |
| [`floor`](readme/functions/floor.md)                                                            |                                                                                                                |
| [`format_string`](readme/functions/format_string.md)                                            |                                                                                                                |
| [`format_timestamp`](readme/functions/format_timestamp.md)                                      |                                                                                                                |
| [`greatest`](readme/functions/greatest.md)                                                      | Return the largest value from a list of expressions                                                            |
| [`if`](readme/functions/if.md)                                                                  |                                                                                                                |
| [`incidr`](readme/functions/incidr.md)                                                          |                                                                                                                |
| [`incidr6`](readme/functions/incidr6.md)                                                        |                                                                                                                |
| [`incidrlist`](readme/functions/incidrlist.md)                                                  |                                                                                                                |
| [`int_to_ip`](readme/functions/int_to_ip.md)                                                    |                                                                                                                |
| [`ip_to_int`](readme/functions/ip_to_int.md)                                                    |                                                                                                                |
| [`is_ipv4`](readme/functions/is_ipv4.md)                                                        |                                                                                                                |
| [`is_ipv6`](readme/functions/is_ipv6.md)                                                        |                                                                                                                |
| [`is_known_private_ipv4`](readme/functions/is_known_private_ipv4.md)                            |                                                                                                                |
| [`is_known_private_ipv6`](readme/functions/is_known_private_ipv6.md)                            |                                                                                                                |
| [`json_extract`](readme/functions/json_extract.md)                                              |                                                                                                                |
| [`json_extract_array`](readme/functions/json_extract_array.md)                                  |                                                                                                                |
| [`json_extract_scalar`](readme/functions/json_extract_scalar.md)                                |                                                                                                                |
| [`json_extract_scalar_array`](readme/functions/json_extract_scalar_array.md)                    |                                                                                                                |
| [`json_path_extract`](readme/functions/json_path_extract.md)                                    |                                                                                                                |
| [`json_functions_reference`](readme/functions/json_functions_reference.md)                      | A comprehensive guide to the four JSON extraction functions                                                    |
| [`lag`](readme/functions/lag.md)                                                                |                                                                                                                |
| [`last`](readme/functions/last.md)                                                              |                                                                                                                |
| [`last_value`](readme/functions/last_value.md)                                                  |                                                                                                                |
| [`latest`](readme/functions/latest.md)                                                          |                                                                                                                |
| [`least`](readme/functions/least.md)                                                            | Return the smallest value from a list of expressions                                                           |
| [`len`](readme/functions/len.md)                                                                |                                                                                                                |
| [`list (comp)`](readme/functions/list_with_comp_stage.md)                                       | Collect all values of a field and return them as an array within the comp stage                                |
| [`ln`](readme/functions/ln.md)                                                                  | Calculate the natural logarithm (base e) of a numeric value                                                    |
| [`log`](readme/functions/log.md)                                                                | Calculate the logarithm of a numeric value with a specified base                                               |
| [`log10`](readme/functions/log10.md)                                                            | Calculate the base-10 logarithm of a numeric value                                                             |
| [`lowercase`](readme/functions/lowercase.md)                                                    |                                                                                                                |
| [`ltrim`](readme/functions/ltrim.md)                                                            |                                                                                                                |
| [`max (comp)`](readme/functions/max_with_comp_stage.md)                                         | Return the maximum value of a field within the comp stage                                                      |
| [`max (windowcomp)`](readme/functions/max_with_windowcomp_stage.md)                             | Compute the maximum value of a field over a window of rows within the windowcomp stage                         |
| [`md5`](readme/functions/md5.md)                                                                |                                                                                                                |
| [`median (comp)`](readme/functions/median_with_comp_stage.md)                                   | Return the median value of a numeric field within the comp stage                                               |
| [`median (windowcomp)`](readme/functions/median_with_windowcomp_stage.md)                       | Compute the median value of a numeric field over a window of rows within the windowcomp stage                  |
| [`min (comp)`](readme/functions/min_with_comp_stage.md)                                         | Return the minimum value of a field within the comp stage                                                      |
| [`min (windowcomp)`](readme/functions/min_with_windowcomp_stage.md)                             | Compute the minimum value of a field over a window of rows within the windowcomp stage                         |
| [`mod`](readme/functions/mod.md)                                                                | Calculate the remainder (modulus) of the division of two numeric values                                        |
| [`multiply`](readme/functions/multiply.md)                                                      |                                                                                                                |
| [`object_create`](readme/functions/object_create.md)                                            |                                                                                                                |
| [`object_merge`](readme/functions/object_merge.md)                                              |                                                                                                                |
| [`parse_epoch`](readme/functions/parse_epoch.md)                                                |                                                                                                                |
| [`parse_timestamp`](readme/functions/parse_timestamp.md)                                        |                                                                                                                |
| [`pow`](readme/functions/pow.md)                                                                |                                                                                                                |
| [`power`](readme/functions/power.md)                                                            | Raise a number to the power of another number (alias for pow)                                                  |
| [`rand`](readme/functions/rand.md)                                                              | Generate a pseudo-random floating-point number between 0 and 1                                                 |
| [`range_bucket`](readme/functions/range_bucket.md)                                              | Determine which bucket a numeric value falls into given an array of boundaries                                 |
| [`rank (windowcomp)`](readme/functions/rank_with_windowcomp_stage.md)                           | Assign a rank to each row within a partition in the windowcomp stage                                           |
| [`regexcapture`](readme/functions/regexcapture.md)                                              |                                                                                                                |
| [`regextract`](readme/functions/regextract.md)                                                  | Extract a substring from a field value using a regular expression pattern                                      |
| [`replace`](readme/functions/replace.md)                                                        |                                                                                                                |
| [`replex`](readme/functions/replex.md)                                                          |                                                                                                                |
| [`round`](readme/functions/round.md)                                                            |                                                                                                                |
| [`row_number (windowcomp)`](readme/functions/row_number_with_windowcomp_stage.md)               | Assign a unique sequential integer to each row within a partition in the windowcomp stage                      |
| [`rtrim`](readme/functions/rtrim.md)                                                            |                                                                                                                |
| [`safe_add`](readme/functions/safe_add.md)                                                      | Perform addition with overflow protection, returning null on overflow                                          |
| [`safe_divide`](readme/functions/safe_divide.md)                                                | Perform division with error protection, returning null on division by zero                                     |
| [`safe_multiply`](readme/functions/safe_multiply.md)                                            | Perform multiplication with overflow protection, returning null on overflow                                    |
| [`safe_negate`](readme/functions/safe_negate.md)                                                | Negate a numeric value with overflow protection, returning null on overflow                                    |
| [`safe_subtract`](readme/functions/safe_subtract.md)                                            | Perform subtraction with overflow protection, returning null on overflow                                       |
| [`sec`](readme/functions/sec.md)                                                                | Calculate the secant of a numeric value specified in radians                                                   |
| [`sha1`](readme/functions/sha1.md)                                                              |                                                                                                                |
| [`sha256`](readme/functions/sha256.md)                                                          |                                                                                                                |
| [`sha512`](readme/functions/sha512.md)                                                          |                                                                                                                |
| [`sign`](readme/functions/sign.md)                                                              | Determine the sign of a numeric value (-1, 0, or 1)                                                            |
| [`sin`](readme/functions/sin.md)                                                                | Calculate the sine of a numeric value specified in radians                                                     |
| [`split`](readme/functions/split.md)                                                            |                                                                                                                |
| [`sqrt`](readme/functions/sqrt.md)                                                              | Calculate the square root of a numeric value                                                                   |
| [`stddev_population (comp)`](readme/functions/stddev_population_with_comp_stage.md)             | Compute the population standard deviation of a numeric field within the comp stage                             |
| [`stddev_population (windowcomp)`](readme/functions/stddev_population_with_windowcomp_stage.md) | Compute the population standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`stddev_sample (comp)`](readme/functions/stddev_sample_with_comp_stage.md)                     | Compute the sample standard deviation of a numeric field within the comp stage                                 |
| [`stddev_sample (windowcomp)`](readme/functions/stddev_sample_with_windowcomp_stage.md)         | Compute the sample standard deviation of a numeric field over a window of rows within the windowcomp stage     |
| [`string_count`](readme/functions/string_count.md)                                              |                                                                                                                |
| [`subtract`](readme/functions/subtract.md)                                                      |                                                                                                                |
| [`sum (comp)`](readme/functions/sum_with_comp_stage.md)                                         | Compute the sum of a numeric field within the comp stage                                                       |
| [`sum (windowcomp)`](readme/functions/sum_with_windowcomp_stage.md)                             | Compute the sum of a numeric field over a window of rows within the windowcomp stage                           |
| [`tan`](readme/functions/tan.md)                                                                | Calculate the tangent of a numeric value specified in radians                                                  |
| [`time_frame_end`](readme/functions/time_frame_end.md)                                          |                                                                                                                |
| [`timestamp_diff`](readme/functions/timestamp_diff.md)                                          |                                                                                                                |
| [`timestamp_seconds`](readme/functions/timestamp_seconds.md)                                    |                                                                                                                |
| [`to_boolean`](readme/functions/to_boolean.md)                                                  |                                                                                                                |
| [`to_epoch`](readme/functions/to_epoch.md)                                                      |                                                                                                                |
| [`to_float`](readme/functions/to_float.md)                                                      |                                                                                                                |
| [`to_integer`](readme/functions/to_integer.md)                                                  |                                                                                                                |
| [`to_json_string`](readme/functions/to_json_string.md)                                          |                                                                                                                |
| [`to_number`](readme/functions/to_number.md)                                                    |                                                                                                                |
| [`to_string`](readme/functions/to_string.md)                                                    |                                                                                                                |
| [`to_timestamp`](readme/functions/to_timestamp.md)                                              |                                                                                                                |
| [`trim`](readme/functions/trim.md)                                                              |                                                                                                                |
| [`trunc`](readme/functions/trunc.md)                                                            | Truncate a numeric value to a specified number of decimal places                                               |
| [`uppercase`](readme/functions/uppercase.md)                                                    |                                                                                                                |
| [`values`](readme/functions/values.md)                                                          | Collect all distinct values of a field and return them as an array within the comp stage                       |
| [`var`](readme/functions/var.md)                                                                | Compute the variance of a numeric field within the comp stage                                                  |
| [`wildcard_match`](readme/functions/wildcard_match.md)                                          |                                                                                                                |

## Stages

| Stage                                          | Description |
| ---------------------------------------------- | ----------- |
| [`alter`](readme/stages/alter.md)              |             |
| [`arrayexpand`](readme/stages/arrayexpand.md)  |             |
| [`bin`](readme/stages/bin.md)                  |             |
| [`call`](readme/stages/call.md)                |             |
| [`comp`](readme/stages/comp.md)                |             |
| [`config`](readme/stages/config.md)            |             |
| [`dataset`](readme/stages/dataset.md)          |             |
| [`dedup`](readme/stages/dedup.md)              |             |
| [`fields`](readme/stages/fields.md)            |             |
| [`filter`](readme/stages/filter.md)            |             |
| [`iploc`](readme/stages/iploc.md)              |             |
| [`join`](readme/stages/join.md)                |             |
| [`limit`](readme/stages/limit.md)              |             |
| [`presets`](readme/stages/presets.md)          |             |
| [`replacenull`](readme/stages/replacenull.md)  |             |
| [`search`](/broken/pages/IgFVkMwRDVqsKrJVWpPI) |             |
| [`sort`](readme/stages/sort.md)                |             |
| [`tag`](readme/stages/tag.md)                  |             |
| [`target`](readme/stages/target.md)            |             |
| [`top`](readme/stages/top.md)                  |             |
| [`transaction`](readme/stages/transaction.md)  |             |
| [`union`](readme/stages/union.md)              |             |
| [`view`](readme/stages/view.md)                |             |
| [`windowcomp`](readme/stages/windowcomp.md)    |             |
