---
ft:title: "Functions List"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "reference"
---

# Functions list

The following table lists all available XQL functions:

| Function | Description |
|---|---|
| [`acos`](acos.md) | Calculate the inverse cosine (arccosine) of a numerical expression |
| [`add`](add.md) | Calculate the sum of two numbers |
| [`approx_count`](approx_count.md) | Return an approximate count of distinct values |
| [`approx_quantiles`](approx_quantiles.md) | Return approximate quantile boundaries |
| [`approx_top`](approx_top.md) | Return the approximate top values |
| [`asin`](asin.md) | Calculate the inverse sine (arcsine) of a numerical expression |
| [`array_all`](array_all.md) | Check if all elements in an array match a condition |
| [`array_any`](array_any.md) | Check if any element in an array matches a condition |
| [`array_length`](array_length.md) | Return the number of elements in an array |
| [`arrayconcat`](arrayconcat.md) | Concatenate two arrays |
| [`arraycreate`](arraycreate.md) | Create an array from a list of values |
| [`arraydistinct`](arraydistinct.md) | Return an array with duplicate values removed |
| [`arrayfilter`](arrayfilter.md) | Filter elements of an array based on a condition |
| [`arrayindex`](arrayindex.md) | Return the element at a specified index in an array |
| [`arrayindexof`](arrayindexof.md) | Return the index of a value in an array |
| [`arraymap`](arraymap.md) | Apply a function to each element of an array |
| [`arraymerge`](arraymerge.md) | Merge multiple arrays into one |
| [`arrayrange`](arrayrange.md) | Create an array of sequential integers |
| [`arraystring`](arraystring.md) | Convert an array to a string |
| [`avg` (with comp stage)](avg_with_comp_stage.md) | Calculate the average value using the comp stage |
| [`avg` (with windowcomp stage)](avg_with_windowcomp_stage.md) | Calculate the average value using the windowcomp stage |
| [`bitwise_and`](bitwise_and.md) | Perform a bitwise AND operation between two integer values |
| [`bitwise_or`](bitwise_or.md) | Perform a bitwise OR operation between two integer values |
| [`bitwise_sleft`](bitwise_sleft.md) | Perform a bitwise left shift operation on an integer value |
| [`bitwise_sright`](bitwise_sright.md) | Perform a bitwise right shift operation on an integer value |
| [`bitwise_xor`](bitwise_xor.md) | Perform a bitwise exclusive OR (XOR) operation between two integer values |
| [`cbrt`](cbrt.md) | Calculate the cube root of a numeric value |
| [`ceil`](ceil.md) | Round a number up to the nearest integer |
| [`coalesce`](coalesce.md) | Return the first non-null value from a list |
| [`concat`](concat.md) | Concatenate two or more strings |
| [`convert_from_base_64`](convert_from_base_64.md) | Decode a Base64-encoded string |
| [`convert_to_base_64`](convert_to_base_64.md) | Encode a string to Base64 |
| [`cos`](cos.md) | Calculate the cosine of a numeric value specified in radians |
| [`cosine_distance`](cosine_distance.md) | Calculate the cosine distance between two numeric vectors |
| [`cot`](cot.md) | Calculate the cotangent of a numeric value specified in radians |
| [`count` (with comp stage)](count_with_comp_stage.md) | Count values using the comp stage |
| [`count` (with windowcomp stage)](count_with_windowcomp_stage.md) | Count values using the windowcomp stage |
| [`count_distinct`](count_distinct.md) | Count distinct values |
| [`csc`](csc.md) | Calculate the cosecant of a numeric value specified in radians |
| [`current_time`](current_time.md) | Return the current timestamp |
| [`date_floor`](date_floor.md) | Round a timestamp down to a specified time unit |
| [`div`](div.md) | Perform integer division of two numeric values |
| [`divide`](divide.md) | Divide one number by another |
| [`earliest`](earliest.md) | Return the earliest timestamp value |
| [`euclidean_distance`](euclidean_distance.md) | Calculate the Euclidean distance between two numeric vectors |
| [`exp`](exp.md) | Calculate the value of e raised to the power of a numeric value |
| [`extract_time`](extract_time.md) | Extract a time component from a timestamp |
| [`extract_url_host`](extract_url_host.md) | Extract the host from a URL |
| [`extract_url_pub_suffix`](extract_url_pub_suffix.md) | Extract the public suffix from a URL |
| [`extract_url_registered_domain`](extract_url_registered_domain.md) | Extract the registered domain from a URL |
| [`first`](first.md) | Return the first value in a group |
| [`first_value`](first_value.md) | Return the first value in a window |
| [`floor`](floor.md) | Round a number down to the nearest integer |
| [`format_string`](format_string.md) | Format a string using a template |
| [`format_timestamp`](format_timestamp.md) | Format a timestamp as a string |
| [`greatest`](greatest.md) | Return the largest value from a list of expressions |
| [`if`](if.md) | Return one of two values based on a condition |
| [`incidr`](incidr.md) | Check if an IPv4 address is within a CIDR range |
| [`incidr6`](incidr6.md) | Check if an IPv6 address is within a CIDR range |
| [`incidrlist`](incidrlist.md) | Check if an IP address is within a list of CIDR ranges |
| [`int_to_ip`](int_to_ip.md) | Convert an integer to an IP address string |
| [`ip_to_int`](ip_to_int.md) | Convert an IP address string to an integer |
| [`is_ipv4`](is_ipv4.md) | Check if a value is a valid IPv4 address |
| [`is_ipv6`](is_ipv6.md) | Check if a value is a valid IPv6 address |
| [`is_known_private_ipv4`](is_known_private_ipv4.md) | Check if an IPv4 address is a known private address |
| [`is_known_private_ipv6`](is_known_private_ipv6.md) | Check if an IPv6 address is a known private address |
| [`json_extract`](json_extract.md) | Extract a value from a JSON string |
| [`json_extract_array`](json_extract_array.md) | Extract an array from a JSON string |
| [`json_extract_scalar`](json_extract_scalar.md) | Extract a scalar value from a JSON string |
| [`json_extract_scalar_array`](json_extract_scalar_array.md) | Extract a scalar array from a JSON string |
| [`json_path_extract`](json_path_extract.md) | Extract a value from a JSON string using a JSONPath expression |
| [`json_functions_reference`](json_functions_reference.md) | Decide which JSON functions to use |
| [`lag`](lag.md) | Return the value of a field from a previous row in a window |
| [`last`](last.md) | Return the last value in a group |
| [`last_value`](last_value.md) | Return the last value in a window |
| [`latest`](latest.md) | Return the latest timestamp value |
| [`least`](least.md) | Return the smallest value from a list of expressions |
| [`len`](len.md) | Return the length of a string or array |
| [`list` (with comp stage)](list_with_comp_stage.md) | Collect all values of a field and return them as an array within the comp stage |
| [`ln`](ln.md) | Calculate the natural logarithm (base e) of a numeric value |
| [`log`](log.md) | Calculate the logarithm of a numeric value with a specified base |
| [`log10`](log10.md) | Calculate the base-10 logarithm of a numeric value |
| [`lowercase`](lowercase.md) | Convert a string to lowercase |
| [`ltrim`](ltrim.md) | Remove leading whitespace from a string |
| [`max` (with comp stage)](max_with_comp_stage.md) | Return the maximum value of a field within the comp stage |
| [`max` (with windowcomp stage)](max_with_windowcomp_stage.md) | Compute the maximum value of a field over a window of rows within the windowcomp stage |
| [`md5`](md5.md) | Calculate the MD5 hash of a string |
| [`median` (with comp stage)](median_with_comp_stage.md) | Return the median value of a numeric field within the comp stage |
| [`median` (with windowcomp stage)](median_with_windowcomp_stage.md) | Compute the median value of a numeric field over a window of rows within the windowcomp stage |
| [`min` (with comp stage)](min_with_comp_stage.md) | Return the minimum value of a field within the comp stage |
| [`min` (with windowcomp stage)](min_with_windowcomp_stage.md) | Compute the minimum value of a field over a window of rows within the windowcomp stage |
| [`mod`](mod.md) | Calculate the remainder (modulus) of the division of two numeric values |
| [`multiply`](multiply.md) | Multiply two numbers |
| [`object_create`](object_create.md) | Create a JSON object from key-value pairs |
| [`object_merge`](object_merge.md) | Merge two JSON objects |
| [`parse_epoch`](parse_epoch.md) | Parse an epoch timestamp |
| [`parse_timestamp`](parse_timestamp.md) | Parse a timestamp string |
| [`pow`](pow.md) | Raise a number to a power |
| [`power`](power.md) | Raise a number to the power of another number (alias for pow) |
| [`rand`](rand.md) | Generate a pseudo-random floating-point number between 0 and 1 |
| [`range_bucket`](range_bucket.md) | Determine which bucket a numeric value falls into given an array of boundaries |
| [`rank` (with windowcomp stage)](rank_with_windowcomp_stage.md) | Assign a rank to each row within a partition in the windowcomp stage |
| [`regexcapture`](regexcapture.md) | Extract substrings using a regular expression |
| [`regextract`](regextract.md) | Extract a substring from a field value using a regular expression pattern |
| [`replace`](replace.md) | Replace occurrences of a substring |
| [`replex`](replex.md) | Replace substrings using a regular expression |
| [`round`](round.md) | Round a number to a specified number of decimal places |
| [`row_number` (with windowcomp stage)](row_number_with_windowcomp_stage.md) | Assign a unique sequential integer to each row within a partition in the windowcomp stage |
| [`rtrim`](rtrim.md) | Remove trailing whitespace from a string |
| [`safe_add`](safe_add.md) | Perform addition with overflow protection, returning null on overflow |
| [`safe_divide`](safe_divide.md) | Perform division with error protection, returning null on division by zero |
| [`safe_multiply`](safe_multiply.md) | Perform multiplication with overflow protection, returning null on overflow |
| [`safe_negate`](safe_negate.md) | Negate a numeric value with overflow protection, returning null on overflow |
| [`safe_subtract`](safe_subtract.md) | Perform subtraction with overflow protection, returning null on overflow |
| [`sec`](sec.md) | Calculate the secant of a numeric value specified in radians |
| [`sha1`](sha1.md) | Calculate the SHA-1 hash of a string |
| [`sha256`](sha256.md) | Calculate the SHA-256 hash of a string |
| [`sha512`](sha512.md) | Calculate the SHA-512 hash of a string |
| [`sign`](sign.md) | Determine the sign of a numeric value (-1, 0, or 1) |
| [`sin`](sin.md) | Calculate the sine of a numeric value specified in radians |
| [`split`](split.md) | Split a string into an array |
| [`sqrt`](sqrt.md) | Calculate the square root of a numeric value |
| [`stddev_population` (with comp stage)](stddev_population_with_comp_stage.md) | Compute the population standard deviation of a numeric field within the comp stage |
| [`stddev_population` (with windowcomp stage)](stddev_population_with_windowcomp_stage.md) | Compute the population standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`stddev_sample` (with comp stage)](stddev_sample_with_comp_stage.md) | Compute the sample standard deviation of a numeric field within the comp stage |
| [`stddev_sample` (with windowcomp stage)](stddev_sample_with_windowcomp_stage.md) | Compute the sample standard deviation of a numeric field over a window of rows within the windowcomp stage |
| [`string_count`](string_count.md) | Count occurrences of a substring in a string |
| [`subtract`](subtract.md) | Subtract one number from another |
| [`sum` (with comp stage)](sum_with_comp_stage.md) | Compute the sum of a numeric field within the comp stage |
| [`sum` (with windowcomp stage)](sum_with_windowcomp_stage.md) | Compute the sum of a numeric field over a window of rows within the windowcomp stage |
| [`tan`](tan.md) | Calculate the tangent of a numeric value specified in radians |
| [`time_frame_end`](time_frame_end.md) | Return the end of a time frame |
| [`timestamp_diff`](timestamp_diff.md) | Calculate the difference between two timestamps |
| [`timestamp_seconds`](timestamp_seconds.md) | Convert a timestamp to seconds |
| [`to_boolean`](to_boolean.md) | Convert a value to a boolean |
| [`to_epoch`](to_epoch.md) | Convert a timestamp to an epoch value |
| [`to_float`](to_float.md) | Convert a value to a float |
| [`to_integer`](to_integer.md) | Convert a value to an integer |
| [`to_json_string`](to_json_string.md) | Convert a value to a JSON string |
| [`to_number`](to_number.md) | Convert a value to a number |
| [`to_string`](to_string.md) | Convert a value to a string |
| [`to_timestamp`](to_timestamp.md) | Convert a value to a timestamp |
| [`trim`](trim.md) | Remove leading and trailing whitespace from a string |
| [`trunc`](trunc.md) | Truncate a numeric value to a specified number of decimal places |
| [`uppercase`](uppercase.md) | Convert a string to uppercase |
| [`values`](values.md) | Collect all distinct values of a field and return them as an array within the comp stage |
| [`var`](var.md) | Compute the variance of a numeric field within the comp stage |
| [`wildcard_match`](wildcard_match.md) | Check if a string matches a wildcard pattern |
