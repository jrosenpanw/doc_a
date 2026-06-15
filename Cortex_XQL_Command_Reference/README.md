---
ft:title: "Cortex XQL Command Reference"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "concept"
---

# Cortex XQL Command Reference

Cortex XQL (Extended Query Language) is a powerful query language used in the Cortex platform for threat hunting, investigation, and analytics across your security data. This reference provides comprehensive documentation for all XQL functions and pipeline stages.

XQL queries are composed of **stages** connected in a pipeline, with **functions** used within those stages to transform, filter, and analyze data. This reference is organized into two main sections:

- **[Functions](Functions/index.md)** – Built-in functions for data manipulation, type conversion, string operations, mathematical calculations, bitwise operations, and more.
- **[Stages](Stages/index.md)** – Pipeline stages that define the structure and flow of an XQL query.

## Functions

| Function | Description |
|---|---|
| [`acos`](Functions/acos.md) | Calculate the inverse cosine (arccosine) of a numerical expression |
| [`add`](Functions/add.md) | |
| [`approx_count`](Functions/approx_count.md) | |
| [`approx_quantiles`](Functions/approx_quantiles.md) | |
| [`approx_top`](Functions/approx_top.md) | |
| [`asin`](Functions/asin.md) | Calculate the inverse sine (arcsine) of a numerical expression |
| [`array_all`](Functions/array_all.md) | |
| [`array_any`](Functions/array_any.md) | |
| [`array_length`](Functions/array_length.md) | |
| [`arrayconcat`](Functions/arrayconcat.md) | |
| [`arraycreate`](Functions/arraycreate.md) | |
| [`arraydistinct`](Functions/arraydistinct.md) | |
| [`arrayfilter`](Functions/arrayfilter.md) | |
| [`arrayindex`](Functions/arrayindex.md) | |
| [`arrayindexof`](Functions/arrayindexof.md) | |
| [`arraymap`](Functions/arraymap.md) | |
| [`arraymerge`](Functions/arraymerge.md) | |
| [`arrayrange`](Functions/arrayrange.md) | |
| [`arraystring`](Functions/arraystring.md) | |
| [`avg`](Functions/avg_with_comp_stage.md) | |
| [`avg`](Functions/avg_with_windowcomp_stage.md) | |
| [`bitwise_and`](Functions/bitwise_and.md) | Perform a bitwise AND operation between two integer values |
| [`bitwise_or`](Functions/bitwise_or.md) | Perform a bitwise OR operation between two integer values |
| [`bitwise_sleft`](Functions/bitwise_sleft.md) | Perform a bitwise left shift operation on an integer value |
| [`bitwise_sright`](Functions/bitwise_sright.md) | Perform a bitwise right shift operation on an integer value |
| [`bitwise_xor`](Functions/bitwise_xor.md) | Perform a bitwise exclusive OR (XOR) operation between two integer values |
| [`cbrt`](Functions/cbrt.md) | Calculate the cube root of a numeric value |
| [`ceil`](Functions/ceil.md) | Round a number up to the nearest integer |
| [`coalesce`](Functions/coalesce.md) | |
| [`concat`](Functions/concat.md) | |
| [`convert_from_base_64`](Functions/convert_from_base_64.md) | |
| [`convert_to_base_64`](Functions/convert_to_base_64.md) | |
| [`cos`](Functions/cos.md) | Calculate the cosine of a numeric value specified in radians |
| [`cosine_distance`](Functions/cosine_distance.md) | Calculate the cosine distance between two numeric vectors |
| [`cot`](Functions/cot.md) | Calculate the cotangent of a numeric value specified in radians |
| [`count`](Functions/count_with_comp_stage.md) | |
| [`count`](Functions/count_with_windowcomp_stage.md) | |
| [`count_distinct`](Functions/count_distinct.md) | |
| [`csc`](Functions/csc.md) | Calculate the cosecant of a numeric value specified in radians |
| [`current_time`](Functions/current_time.md) | |
| [`date_floor`](Functions/date_floor.md) | |
| [`div`](Functions/div.md) | Perform integer division of two numeric values |
| [`divide`](Functions/divide.md) | |
| [`earliest`](Functions/earliest.md) | |
| [`euclidean_distance`](Functions/euclidean_distance.md) | Calculate the Euclidean distance between two numeric vectors |
| [`exp`](Functions/exp.md) | Calculate the value of e raised to the power of a numeric value |
| [`extract_time`](Functions/extract_time.md) | |
| [`extract_url_host`](Functions/extract_url_host.md) | |
| [`extract_url_pub_suffix`](Functions/extract_url_pub_suffix.md) | |
| [`extract_url_registered_domain`](Functions/extract_url_registered_domain.md) | |
| [`first`](Functions/first.md) | |
| [`first_value`](Functions/first_value.md) | |
| [`floor`](Functions/floor.md) | |
| [`format_string`](Functions/format_string.md) | |
| [`format_timestamp`](Functions/format_timestamp.md) | |
| [`greatest`](Functions/greatest.md) | Return the largest value from a list of expressions |
| [`if`](Functions/if.md) | |
| [`incidr`](Functions/incidr.md) | |
| [`incidr6`](Functions/incidr6.md) | |
| [`incidrlist`](Functions/incidrlist.md) | |
| [`int_to_ip`](Functions/int_to_ip.md) | |
| [`ip_to_int`](Functions/ip_to_int.md) | |
| [`is_ipv4`](Functions/is_ipv4.md) | |
| [`is_ipv6`](Functions/is_ipv6.md) | |
| [`is_known_private_ipv4`](Functions/is_known_private_ipv4.md) | |
| [`is_known_private_ipv6`](Functions/is_known_private_ipv6.md) | |
| [`json_extract`](Functions/json_extract.md) | |
| [`json_extract_array`](Functions/json_extract_array.md) | |
| [`json_extract_scalar`](Functions/json_extract_scalar.md) | |
| [`json_extract_scalar_array`](Functions/json_extract_scalar_array.md) | |
| [`json_path_extract`](Functions/json_path_extract.md) | |
| [`json_functions_reference`](Functions/json_functions_reference.md) | A comprehensive guide to the four JSON extraction functions |
| [`lag`](Functions/lag.md) | |
| [`last`](Functions/last.md) | |
| [`last_value`](Functions/last_value.md) | |
| [`latest`](Functions/latest.md) | |
| [`least`](Functions/least.md) | Return the smallest value from a list of expressions |
| [`len`](Functions/len.md) | |
| [`list (comp)`](Functions/list_with_comp_stage.md) | Collect all values of a field and return them as an array within the comp stage |
| [`ln`](Functions/ln.md) | Calculate the natural logarithm (base e) of a numeric value |
| [`log`](Functions/log.md) | Calculate the logarithm of a numeric value with a specified base |
| [`log10`](Functions/log10.md) | Calculate the base-10 logarithm of a numeric value |
| [`lowercase`](Functions/lowercase.md) | |
| [`ltrim`](Functions/ltrim.md) | |
| [`max (comp)`](Functions/max_with_comp_stage.md) | Return the maximum value of a field within the comp stage |
| [`max (windowcomp)`](Functions/max_with_windowcomp_stage.md) | Compute the maximum value of a field over a window of rows within the windowcomp stage |
| [`md5`](Functions/md5.md) | |
| [`median (comp)`](Functions/median_with_comp_stage.md) | Return the median value of a numeric field within the comp stage |
| [`median (windowcomp)`](Functions/median_with_windowcomp_stage.md) | Compute the median value of a numeric field over a window of rows within the windowcomp stage |
| [`min (comp)`](Functions/min_with_comp_stage.md) | Return the minimum value of a field within the comp stage |
| [`min (windowcomp)`](Functions/min_with_windowcomp_stage.md) | Compute the minimum value of a field over a window of rows within the windowcomp stage |
| [`mod`](Functions/mod.md) | Calculate the remainder (modulus) of the division of two numeric values |
| [`multiply`](Functions/multiply.md) | |
| [`object_create`](Functions/object_create.md) | |
| [`object_merge`](Functions/object_merge.md) | |
| [`parse_epoch`](Functions/parse_epoch.md) | |
| [`parse_timestamp`](Functions/parse_timestamp.md) | |
| [`pow`](Functions/pow.md) | |
| [`power`](Functions/power.md) | Raise a number to the power of another number (alias for pow) |
| [`rand`](Functions/rand.md) | Generate a pseudo-random floating-point number between 0 and 1 |
| [`range_bucket`](Functions/range_bucket.md) | Determine which bucket a numeric value falls into given an array of boundaries |
| [`rank (windowcomp)`](Functions/rank_with_windowcomp_stage.md) | Assign a rank to each row within a partition in the windowcomp stage |
| [`regexcapture`](Functions/regexcapture.md) | |
| [`regextract`](Functions/regextract.md) | Extract a substring from a field value using a regular expression pattern |
| [`replace`](Functions/replace.md) | |
| [`replex`](Functions/replex.md) | |
| [`round`](Functions/round.md) | |
| [`row_number (windowcomp)`](Functions/row_number_with_windowcomp_stage.md) | Assign a unique sequential integer to each row within a partition in the windowcomp stage |
| [`rtrim`](Functions/rtrim.md) | |
| [`safe_add`](Functions/safe_add.md) | Perform addition with overflow protection, returning null on overflow |
| [`safe_divide`](Functions/safe_divide.md) | Perform division with error protection, returning null on division by zero |
| [`safe_multiply`](Functions/safe_multiply.md) | Perform multiplication with overflow protection, returning null on overflow |
| [`safe_negate`](Functions/safe_negate.md) | Negate a numeric value with overflow protection, returning null on overflow |
| [`safe_subtract`](Functions/safe_subtract.md) | Perform subtraction with overflow protection, returning null on overflow |
| [`sec`](Functions/sec.md) | Calculate the secant of a numeric value specified in radians |
| [`sha1`](Functions/sha1.md) | |
| [`sha256`](Functions/sha256.md) | |
| [`sha512`](Functions/sha512.md) | |
| [`sign`](Functions/sign.md) | Determine the sign of a numeric value (-1, 0, or 1) |
| [`sin`](Functions/sin.md) | Calculate the sine of a numeric value specified in radians |
| [`split`](Functions/split.md) | |
| [`sqrt`](Functions/sqrt.md) | Calculate the square root of a numeric value |
| [`stddev_population (comp)`](Functions/stddev_population_with_comp_stage.md) | Compute the population standard deviation of a numeric field within the comp stage |
| [`stddev_population (windowcomp)`](Functions/stddev_population_with_windowcomp_stage.md) | Compute the population standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`stddev_sample (comp)`](Functions/stddev_sample_with_comp_stage.md) | Compute the sample standard deviation of a numeric field within the comp stage |
| [`stddev_sample (windowcomp)`](Functions/stddev_sample_with_windowcomp_stage.md) | Compute the sample standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`string_count`](Functions/string_count.md) | |
| [`subtract`](Functions/subtract.md) | |
| [`sum (comp)`](Functions/sum_with_comp_stage.md) | Compute the sum of a numeric field within the comp stage |
| [`sum (windowcomp)`](Functions/sum_with_windowcomp_stage.md) | Compute the sum of a numeric field over a window of rows within the windowcomp stage |
| [`tan`](Functions/tan.md) | Calculate the tangent of a numeric value specified in radians |
| [`time_frame_end`](Functions/time_frame_end.md) | |
| [`timestamp_diff`](Functions/timestamp_diff.md) | |
| [`timestamp_seconds`](Functions/timestamp_seconds.md) | |
| [`to_boolean`](Functions/to_boolean.md) | |
| [`to_epoch`](Functions/to_epoch.md) | |
| [`to_float`](Functions/to_float.md) | |
| [`to_integer`](Functions/to_integer.md) | |
| [`to_json_string`](Functions/to_json_string.md) | |
| [`to_number`](Functions/to_number.md) | |
| [`to_string`](Functions/to_string.md) | |
| [`to_timestamp`](Functions/to_timestamp.md) | |
| [`trim`](Functions/trim.md) | |
| [`trunc`](Functions/trunc.md) | Truncate a numeric value to a specified number of decimal places |
| [`uppercase`](Functions/uppercase.md) | |
| [`values`](Functions/values.md) | Collect all distinct values of a field and return them as an array within the comp stage |
| [`var`](Functions/var.md) | Compute the variance of a numeric field within the comp stage |
| [`wildcard_match`](Functions/wildcard_match.md) | |

## Stages

| Stage | Description |
|---|---|
| [`alter`](Stages/alter.md) | |
| [`arrayexpand`](Stages/arrayexpand.md) | |
| [`bin`](Stages/bin.md) | |
| [`call`](Stages/call.md) | |
| [`comp`](Stages/comp.md) | |
| [`config`](Stages/config.md) | |
| [`dataset`](Stages/dataset.md) | |
| [`dedup`](Stages/dedup.md) | |
| [`fields`](Stages/fields.md) | |
| [`filter`](Stages/filter.md) | |
| [`iploc`](Stages/iploc.md) | |
| [`join`](Stages/join.md) | |
| [`limit`](Stages/limit.md) | |
| [`presets`](Stages/presets.md) | |
| [`replacenull`](Stages/replacenull.md) | |
| [`search`](Stages/search.md) | |
| [`sort`](Stages/sort.md) | |
| [`tag`](Stages/tag.md) | |
| [`target`](Stages/target.md) | |
| [`top`](Stages/top.md) | |
| [`transaction`](Stages/transaction.md) | |
| [`union`](Stages/union.md) | |
| [`view`](Stages/view.md) | |
| [`windowcomp`](Stages/windowcomp.md) | |
