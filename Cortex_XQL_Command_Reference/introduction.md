---
ft:title: "Cortex XQL Command Reference"
Product: "Cortex"
Category: "Reference Guide"
Product_Category: "Cortex XQL"
ft:lang: "en-US"
ft:topicType: "concept"
---

# Cortex XQL Command Reference

Cortex XQL (Cortext Query Language) is a powerful query language used in the Cortex platform for threat hunting, investigation, and analytics across your security data. This reference provides comprehensive documentation for all XQL functions and pipeline stages.

## Overview

XQL queries are composed of **stages** connected in a pipeline, with **functions** used within those stages to transform, filter, and analyze data. This reference is organized into two main sections:

- **Functions** – Built-in functions for data manipulation, type conversion, string operations, mathematical calculations, bitwise operations, and more.
  - **[XQL JSON Functions Reference](Functions/json_functions_reference.md)** – A comprehensive guide to the four JSON extraction functions (`json_extract`, `json_extract_scalar`, `json_extract_array`, `json_extract_scalar_array`).
- **Stages** – Pipeline stages that define the structure and flow of an XQL query.
