## Cortex XSIAM XQL

Understand more about the Cortex Query Language called XQL, so you can
build queries to gain insight from the data contained in the different
data sources in Cortex XSIAM.

### Get started with XQL

XQL is the Cortex Query Language. It allows you to form complex queries
against data stored in Cortex XSIAM. This section introduces XQL, and it
provides reference information on the various stages, functions, and
aggregates that XQL supports.

#### XQL language features

The Cortex Query Language (XQL) enables you to query for information
contained in a wide variety of data sources in Cortex XSIAM for rigorous
endpoint and network event analysis. Queries require a dataset, or data
source, to run against. In a dataset query, unless otherwise specified,
the query runs against the `xdr_data` dataset, which contains all raw
log information that Cortex XSIAM collects from all Cortex product
agents, including EDR data, and PAN NGFW data. In XDM queries, you must
specify the dataset mapped to the XDM that you want to run your query
against. For both types of queries, you can also import data from third
parties and then query against those datasets as well.

You submit XQL queries to Cortex XSIAM using the Investigation &
Response \> Search \> Query Builder user interface.

XQL is similar to other query languages, and it uses some of the same
functions as can be found in many SQL implementations, but it is not
SQL. XQL forms queries in stages. Each stage performs a specific query
operation and is separated by a pipe (`|`) character. To help you create
an eﬀective XQL query with the proper syntax, the query ﬁeld in the user
interface provides suggestions and deﬁnitions as you type. For example,
the following dataset query uses three stages to identify the dataset to
query, identify the field to be retrieved from the dataset, and then set
a filter that identifies which records should be retrieved as part of
the query:

    dataset = xdr_data 
    | fields os_actor_process_file_size as osapfs 
    | filter to_string(osapfs) = "12345"

> **Tip**
>
> When creating XQL queries, you can:

- > Use the up and down arrow keys to navigate through the
  > auto-suggestion commands and definitions.

- > Select an auto-suggestion command by pressing either the **Enter**
  > or **Tab** key.

- > Press **Shift**+**Enter** to add a new line, and easily ignore the
  > auto-suggestion output.

- > Close the auto-suggestion output by pressing the **Esc** key.

XQL supports:

- Simple queries.

- Filters that identify a subset of records to return in the result set.

- Joins and Unions.

- Aggregations.

- Queries against standard datasets.

- Queries against presets, which are collections of information that are
  specific to a given type of network or endpoint activity, such as
  authentication or file transfers.

- Queries against custom imported datasets.

- Queries against the XDM.

#### XQL Language Structure

Cortex Query Language (XQL) queries usually begin by defining a data
source, be it a dataset, preset, or Cortex Data Model (XDM). You must
specify the dataset mapped to the XDM that you want to run your query
against. In a dataset query, unless otherwise specified, the query runs
against the `xdr_data` dataset, which contains all log information
that Cortex XSIAM collects from all Cortex product agents, including EDR
data, and PAN NGFW data. It\'s possible to change the default dataset in
the **Dataset Management** page of Cortex XSIAM. For more information,
see
[/document/preview/952372#UUID-3ef0648c-1032-a887-27be-7c2264b6daf0](/document/preview/952372#UUID-3ef0648c-1032-a887-27be-7c2264b6daf0).

After specifying a data source, you use zero or more stages to form the
XQL query. Each stage is delimited using a pipe character (`|`). The
function performed by each stage is identified by the stage keyword that
you provide. XQL queries can contain different components depending on
the type of query you want to build.

##### Adding comments in queries

You can add comments in any section when building a query in Cortex
Query Language (XQL).

- Comments are added on a single line using the following syntax.

<!-- -->

-  //<comments>

  For example,

      dataset = xdr_data
      | filter event_type=1
      //ENUM.process
      and event_sub_type = 1
      //ENUM.execution

<!-- -->

- To write a comment that extends over multiple lines use the following
  syntax.

<!-- -->

- /*multi-line <comments> */

  For example,

      dataset = xdr_data 
      | filter 
      /*multi-line Adding comments is a great thing.
      Here is an example */ 
      event_type=1

#### Supported operators

Cortex Query Language (XQL) queries support the following comparison,
boolean, string, range, and add operators.

+-----------------------------------+--------------------------------------------------------------------------------------+
| Operator                          | Description                                                                          |
+===================================+======================================================================================+
| Comparison operators              |                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------+
| =, !=                             | Equal, Not equal                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------+
| \<, \<=                           | Less than, Less than or equal to                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------+
| \>, \>=                           | Greater than, Greater than or equal to                                               |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Boolean operators                 |                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------+
| and                               | Boolean and                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| or                                | Boolean or                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------+
| not                               | Boolean not                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| String and range operators        |                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------+
| IN, NOT IN                        | Returns true if the integer or string field value is one of the options specified.   |
|                                   | For example:                                                                         |
|                                   |                                                                                      |
|                                   |     action_local_port in(5900,5999)                                                  |
|                                   |                                                                                      |
|                                   | For string field values, wildcards are supported. In this example a wildcard (`*`)   |
|                                   | is used to search if the value contains the strings `"word_1"` or `"word_2"`         |
|                                   | anywhere in the output, or exactly matches the string `"word"`:                      |
|                                   |                                                                                      |
|                                   |     str_field in ("*word_1*", "*word_2*", "word")                                    |
|                                   |                                                                                      |
|                                   | > **Note**                                                                           |
|                                   | >                                                                                    |
|                                   | > In some cases, using an `IN` or `NOT IN` operator combined with a dataset and      |
|                                   | > [filter](#UUID75b17bafc8212d4207f11d67acd47c76) stage can be a better alternative  |
|                                   | > to using a [join](#UUID01b27dc92ccd24c18588d2388b5a0f90) stage.                    |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CONTAINS, NOT CONTAINS            | Performs a search for an integer or string. Returns true if the speciﬁed string is   |
|                                   | contained in the ﬁeld. `Contains` and `Not Contains` are also supported within       |
|                                   | arrays for integers and strings.                                                     |
|                                   |                                                                                      |
|                                   |     lowercase(actor_process_image_name) contains "psexec"                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| \~=                               | Matches a regular expression.                                                        |
|                                   |                                                                                      |
|                                   |     action_process_image_name ~= ".*?\.(?:pdf|docx)\.exe"                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| INCIDR, NOT INCIDR                | Performs a search for an IPv4 address or IPv4 range using CIDR notation, and returns |
|                                   | true if the address is in range.                                                     |
|                                   |                                                                                      |
|                                   |     action_remote_ip incidr "192.1.1.1/24"                                           |
|                                   |                                                                                      |
|                                   | It is also possible to define multiple CIDRs with comma separated syntax when        |
|                                   | building a XQL query with the Query Builder or in Correlation Rules. When defining   |
|                                   | multiple CIDRs, the logical `OR` is used between the CIDRS listed, so as long as one |
|                                   | address is in range the entire statement returns `true`. The same logic is used when |
|                                   | using the `incidr()` function. For more information on how this logic works to       |
|                                   | determine whether the `incidr` or `not incidr` operators return `true` or `false`,   |
|                                   | see [incidr](#UUID3eed5fd838383904a1b251d4ca998d61).                                 |
|                                   |                                                                                      |
|                                   |     action_remote_ip incidr "192.168.0.0/24, 1.168.0.0/24"                           |
|                                   |                                                                                      |
|                                   | Both the IPv4 address and CIDR ranges can be either an explicit string using quotes  |
|                                   | (`""`), such as `"192.168.0.1"`, or a string field.                                  |
+-----------------------------------+--------------------------------------------------------------------------------------+
| INCIDR6, NOT INCIDR6              | Performs a search for an IPv6 address or IPv6 range using CIDR notation, and returns |
|                                   | true if the address is in range.                                                     |
|                                   |                                                                                      |
|                                   |     action_remote_ip incidr6 “3031:3233:3435:3637:0000:0000:0000:0000/64”            |
|                                   |                                                                                      |
|                                   | It is also possible to define multiple CIDRs with comma separated syntax when        |
|                                   | building a XQL query with the Query Builder or in Correlation Rules. When defining   |
|                                   | multiple CIDRs, the logical `OR` is used between the CIDRS listed, so as long as one |
|                                   | address is in range the entire statement returns `true`. The same logic is used when |
|                                   | using the `incidr6()` function. For more information on how this logic works to      |
|                                   | determine whether the `incidr6` or `not incidr6` operators return `true` or `false`, |
|                                   | see [incidr6](#UUIDebd8bbbe8422a99bbd843078d440abb2).                                |
|                                   |                                                                                      |
|                                   |     action_remote_ip incidr6 "2001:0db8:85a3:0000:0000:8a2e:0000:0000/64, fe80::/10" |
|                                   |                                                                                      |
|                                   | Both the IPv6 address and CIDR ranges can be either an explicit string using quotes  |
|                                   | (`""`), such as `“3031:3233:3435:3637:0000:0000:0000:0000/64”`, or a string field.   |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Add operator for tagging          |                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------+
| add                               | The `add` operator is used in combination with the `tag` command to add a single tag |
|                                   | or list of tags to a ﬁeld that you can easily query in the dataset.                  |
|                                   |                                                                                      |
|                                   | - Adding a Single Tag                                                                |
|                                   |                                                                                      |
|                                   | <!-- -->                                                                             |
|                                   |                                                                                      |
|                                   | - dataset = xdr_data                                                                 |
|                                   |       | tag add "test"                                                               |
|                                   |                                                                                      |
|                                   | <!-- -->                                                                             |
|                                   |                                                                                      |
|                                   | - Adding a List of Tags                                                              |
|                                   |                                                                                      |
|                                   | <!-- -->                                                                             |
|                                   |                                                                                      |
|                                   | - dataset = xdr_data                                                                 |
|                                   |       | tag add "test1", "test2", "test3"                                            |
+-----------------------------------+--------------------------------------------------------------------------------------+

#### Datasets and presets

Every Cortex Query Language (XQL) dataset query begins by identifying a
data source that the query will run against. Each data source has a
unique name, and a series of fields. Your query specifies the data
source, and then provides stages that identify fields of interest and
perform operations against those fields.

You can query against either datasets or
[Presets](#Xa80c6371a99741002f311b0080be865cab9f44e) in a dataset query.
XQL supports using different languages for dataset and field names. In
addition, the dataset formats supported are dependent on the data
retention offerings available in Cortex XSIAM according to whether you
want to query hot storage (default) or cold storage. For more
information, see [XQL Language
Structure](#UUID6542a8d1266e815dfaf2afaf3c1054cc).

##### Datasets

The standard, built-in data source that is available in every Cortex
XSIAM instance is the `xdr_data` dataset. This is a very large dataset
with many available fields. For more information about this dataset, see
[Cortex XQL Schema
Reference](https://docs-cortex.paloaltonetworks.com/r/Cortex-XQL-Schema-Reference-Guide/Introduction).
Cortex Query Language (XQL) supports using different languages for
dataset and field names. In addition, the dataset formats supported are
dependent on the data retention offerings available in Cortex XSIAM
according to whether you want to query hot storage (default) or cold
storage. For more information, see [XQL Language
Structure](#UUID6542a8d1266e815dfaf2afaf3c1054cc).

This dataset is comprised of both raw Endpoint Detection and Response
(EDR) events reported by the Cortex XSIAM agent, and of logs from
different sources such as third-party logs. To help you investigate
events more efficiently, Cortex XSIAM also stitches these logs and
events together into common schemas called stories. These stories are
available using the Cortex XSIAM
[Presets](#Xa80c6371a99741002f311b0080be865cab9f44e).

Building queries in XQL

When building queries in XQL, keep the following in mind about datasets:

- Use the `dataset` keyword to specify a dataset on your query.

- Create custom datasets using the
  [target](#UUID2633c59ff09cbb66a58380019f45d292) stage.

- Dataset names can use uppercase characters, but in queries dataset
  names are always treated as if they are lowercase. In addition,
  dataset names are supported using different languages, numbers
  (`0-9`), and underscores (`_`). Yet, underscores cannot be the first
  character of the name.

- Upon ingestion, all fields are retained even fields with a null value.
  You can also use XQL to query parsing rules for null values.

- Schema changes to datasets may not be reflected in the autocomplete
  suggestions and deﬁnitions as you type in real time the XQL query and
  can appear with a slight delay.

Available datasets

Depending on your integrations, you can have the following datasets
available for queries:

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Data                              | Dataset                                                                                                                                          |
+===================================+==================================================================================================================================================+
| Active Directory via Cloud        | `pan_dss_raw`                                                                                                                                    |
| Identity Engine                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > To set up this Cloud Identity Engine (previously called Directory Sync Service (DSS)) dataset, you need to set up a Cloud Identity Engine.     |
|                                   | > Otherwise, you will not have a `pan_dss_raw` dataset. For more information, see [Set up Cloud Identity                                         |
|                                   | > Engine](#UUID586f81e7ddbd6968328cbd7809bd7eaa).                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Issues table in Cortex XSIAM      | issues                                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - > `INFO` issues are not included in this dataset.                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - > This dataset includes issues from the Security and Health domains. For more information, see [Overview of the Issues                         |
|                                   |   > page](#UUID6e85536cf581499f93b01d0e2c25186d).                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Amazon S3                         | - Audit logs                                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   |   - All logs: `aws_s3_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   |   - Normalize and enrich audit logs: `cloud_audit_logs`                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - Generic logs                                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   |   - `<Vendor>_<Product>_raw`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - Network flow logs                                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   |   - All logs: `aws_s3_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   |   - Normalize and enrich flow logs: `xdr_dataset` dataset with a preset called `network_story`                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Authentication logs (subset of    | Authentication logs, such as Okta: `auth_logs`                                                                                                   |
| xdr_data)                         |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > The fields contained in this dataset are a subset of the fields in the `xdr_data` dataset.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| AWS CloudTrail and Amazon         | `<Vendor>_<Product>_raw`                                                                                                                         |
| CloudWatch                        |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Azure Event Hub                   | - All logs: `MSFT_Azure_raw`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - Normalize and enrich audit logs: `cloud_audit_logs`                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Azure Network Watcher             | - All logs: `MSFT_Azure_raw`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - Normalize and enrich flow logs: `xdr_dataset` dataset with a preset called `network_story`                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| BeyondTrust Privilege Management  | `beyondtrust_privilege_management_raw`                                                                                                           |
| Cloud                             |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Box                               | Events (admin_logs)                                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - `box_admin_logs_raw`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | Box Shield Alerts                                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   | - `box_shield_alerts_raw`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | Users                                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - `box_users_raw`                                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   | Groups                                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `box_groups_raw`                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Checkpoint FW1/VPN1               | `<Vendor>_<Product>_raw`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Cisco ASA                         | Cisco ASA firewalls or Cisco AnyConnect VPN                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - `cisco_asa_raw`                                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Collector status change audit for | `collection_auditing`                                                                                                                            |
| collection integrations, custom   |                                                                                                                                                  |
| collectors, and marketplace       |                                                                                                                                                  |
| collectors.                       |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Corelight Zeek                    | `corelight_zeek_raw`                                                                                                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Correlation rule executions       | `correlations_auditing`                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Cortex Data Lakes                 | `xdr_data`                                                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Cortex XDR Collectors             | `panw_xdrc_raw`                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Cortex XSIAM Host Firewall        | `host_firewall_events`                                                                                                                           |
| enforcement events                |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| CrowdStrike FDR                   | - `crowdstrike_falcon_incident_raw`                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - `crowdstrike_fdr_raw`                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| CSV files in shared Windows       | Custom datasets: Select from pre-existing user-created datasets or add a new dataset.                                                            |
| directory                         |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Database data (MySQL, PostgreSQL, | `<Vendor>_<Product>_raw`                                                                                                                         |
| MSSQL, and Oracle)                |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Data ingestion health metrics     | Datasets:                                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `data_ingestion_health`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | <!-- -->                                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - > **Important**                                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   |   > This dataset will not be updated after June 2024. Use the `health_alerts` dataset instead.                                                   |
|                                   |                                                                                                                                                  |
|                                   | <!-- -->                                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `metrics_source`                                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | Presets:                                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `data_ingestion_metrics` (this preset will be deprecated in the next release and replaced by metrics_view).                                    |
|                                   |                                                                                                                                                  |
|                                   | - `metrics_view`                                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Dropbox                           | Events                                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `dropbox_events_raw`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | Member Devices                                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   | - `dropbox_members_devices_raw`                                                                                                                  |
|                                   |                                                                                                                                                  |
|                                   | Users                                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - `dropbox_users_raw`                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | Groups                                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `dropbox_groups_raw`                                                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Elasticsearch Filebeat            | `<Vendor>_<Product>_raw`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Elasticsearch Winlogbeat          | `<Vendor>_<Product>_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > If the vendor and product are not specified in the Winlogbeat profile's configuration file, Cortex XSIAM creates a default dataset called      |
|                                   | > `microsoft_windows_raw`.                                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Errors related to Parsing Rules   | `parsing_rules_errors`                                                                                                                           |
| and Data Model Rules              |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Errors related to event           | `event_forwarding_errors`                                                                                                                        |
| forwarding                        |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Forcepoint DLP                    | `forcepoint_dlp_endpoint_raw`                                                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Fortinet Fortigate                | `<Vendor>_<Product>_raw`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| GlobalProtect access              | `xdr_data`                                                                                                                                       |
| authentication logs               |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > To ensure GlobalProtect access authentication logs are sent to Cortex XSIAM, verify that your PANW firewall's **Log Settings** for             |
|                                   | > GlobalProtect has the **Cortex Data Lake** checkbox selected.                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Google Cloud Platform (GCP) logs  | - All log types: `google_cloud_logging_raw`                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - Normalize and enrich audit and flow logs: `cloud_audit_logs`                                                                                   |
|                                   |                                                                                                                                                  |
|                                   |   - Audit logs: `cloud_audit_logs`                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   |   - Network flow logs: `xdr_dataset` dataset with a preset called `network_story`                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Google Kubernetes Engine (GKE)    | `<Vendor>_<Product>_raw`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Google Workspace                  | - Google Chrome: `google_workspace_chrome_raw`                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   | - Admin Console: `google_workspace_admin_console_raw`                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - Google Chat: `google_workspace_chat_raw`                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - Enterprise Groups: `google_workspace_enterprise_groups_raw`                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - Login: `google_workspace_login_raw`                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - Rules: `google_workspace_rules_raw`                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - Google drive: `google_workspace_drive_raw`                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - Token: `google_workspace_token_raw`                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - User Accounts: `google_workspace_user_accounts_raw`                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - SAML: `google_workspace_saml_raw`                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - Alerts: `google_workspace_alerts_raw`                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - Emails: `google_gmail_raw`                                                                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Host Inventory and Vulnerability  | - Datasets                                                                                                                                       |
| Assessment                        |                                                                                                                                                  |
|                                   |   - `host_inventory`                                                                                                                             |
|                                   |                                                                                                                                                  |
|                                   |   - `va_cves`                                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   |   - `va_endpoints`                                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | - Presets                                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory`                                                                                                                             |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_accessibility`                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_applications`                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_auto_runs`                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_cpus`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_daemons`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_disks`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_drivers`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_endpoints`                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_extensions`                                                                                                                  |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_groups`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_kbs`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_mounts`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_services`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_shares`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_users`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_volumes`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   |   - `host_inventory_vss`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Cases table in Cortex XSIAM       | `cases`                                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Indicators                        | `indicators`                                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > You must have the Cortex XSIAM Threat Intel Management (TIM) Add-on to use this dataset.                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Indicator relationships           | `indicator_relationship`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > You must have the Cortex XSIAM Threat Intel Management (TIM) Add-on to use this dataset.                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| IT performance metrics            | `it_metrics`                                                                                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| JSON or text logs from            | `<Vendor>_<Product>_raw`                                                                                                                         |
| third-party source over HTTP      |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Login logs (subset of xdr_data)   | Login logs, such as WEC: `login_logs`                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > The fields contained in this dataset are a subset of the fields in the `xdr_data` dataset.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Logs from third party source over | `<Vendor>_<Product>_raw`                                                                                                                         |
| FTP, FTPS, or SFTP                |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Microsoft Defender for Endpoint   | `msft_defender_raw`                                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Microsoft 365 (email)             | - `msft_o365_emails_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_users_raw`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_groups_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_devices_raw`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_mailboxes_raw`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_rules_raw`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `msft_o365_contacts_raw`                                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Microsoft Office 365              | - Microsoft Office 365 audit events from Management Activity API:                                                                                |
|                                   |                                                                                                                                                  |
|                                   |   - Azure AD Activity Logs: `msft_o365_azure_ad_raw`                                                                                             |
|                                   |                                                                                                                                                  |
|                                   |   - Exchange Online: `msft_o365_exchange_online_raw`                                                                                             |
|                                   |                                                                                                                                                  |
|                                   |   - Sharepoint Online: `msft_o365_sharepoint_online_raw`                                                                                         |
|                                   |                                                                                                                                                  |
|                                   |   - DLP: `msft_o365_dlp_raw`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   |   - General: `msft_o365_general_raw`                                                                                                             |
|                                   |                                                                                                                                                  |
|                                   | - Microsoft Office 365 emails via Microsoft's Graph API: `msft_o365_emails_raw`                                                                  |
|                                   |                                                                                                                                                  |
|                                   | - Azure AD authentication events from Microsoft Graph API: `msft_azure_ad_raw`                                                                   |
|                                   |                                                                                                                                                  |
|                                   | - Azure AD audit events from Microsoft Graph API: `msft_azure_ad_audit_raw`                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - Alerts from Microsoft Graph Security API: `msft_graph_security_alerts_raw`                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| NetFlow                           | - `ip_flow_ip_flow_raw` (default)                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   | - When configured, uses the format `<Vendor>_<Product>_raw`                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Network Share logs                | `<Vendor>_<Product>_raw`                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Okta                              | `okta_sso_raw`                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| OneLogin                          | Log collection                                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   | - `onelogin_events_raw`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | Directory                                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `onelogin_users_raw`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `onelogin_groups_raw`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `onelogin_apps_raw`                                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PANW EDR                          | `xdr_data`                                                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PANW IOT Security                 | Alerts                                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `panw_iot_security_alerts_raw`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | Devices                                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `panw_iot_security_devices_raw`                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PANW NGFW                         | `panw_ngfw_*_raw`                                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   | Supports the following logs.                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - [Authentication                                                                                                                                |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-authentication-log.html): |
|                                   |   `panw_ngfw_auth_raw`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - [Configuration                                                                                                                                 |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/common-logs/common-configuration-log):         |
|                                   |   `panw_ngfw_config_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - [File Data                                                                                                                                     |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-file-log.html):           |
|                                   |   `panw_ngfw_filedata_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - [Global Protect                                                                                                                                |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-globalprotect-log.html):  |
|                                   |   `panw_ngfw_globalprotect_raw`                                                                                                                  |
|                                   |                                                                                                                                                  |
|                                   | - \*[Hipmatch                                                                                                                                    |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-hip-match-log.html):      |
|                                   |   `panw_ngfw_hipmatch_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - [System Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/common-logs/common-system-log.html):   |
|                                   |   `panw_ngfw_system_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - \*[Threat                                                                                                                                      |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-threat-log.html):         |
|                                   |   `panw_ngfw_threat_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - \*[Traffic                                                                                                                                     |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-traffic-log.html):        |
|                                   |   `panw_ngfw_traffic_raw`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - \*[URL Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-url-log.html):     |
|                                   |   `panw_ngfw_url_raw`                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - [User ID                                                                                                                                       |
|                                   |   Logs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference/network-logs/network-userid-log.html):         |
|                                   |   `panw_ngfw_userid_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - [Tunnel Logs](https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-tunnel-log): `panw_ngfw_tunnel_raw`  |
|                                   |                                                                                                                                                  |
|                                   | - [Configuration Logs](https://docs.paloaltonetworks.com/strata-logging-service/log-reference/common-logs/common-configuration-log):             |
|                                   |   `panw_ngfw_config_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | \*These datasets use the query field names as described in the [Cortex                                                                           |
|                                   | schema](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/log-forwarding-schema-reference.html) documentation.                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PingFederate                      | `ping_identity_pingfederate_raw`                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PingOne for Enterprise            | `pingone_sso_raw`                                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Playbook runs                     | `playbook_runs`                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Playbook tasks                    | `playbook_tasks`                                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Prisma Access Browser             | `panw_prisma_access_browser_raw`                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Prisma Cloud                      | `prisma_cloud_raw`                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Prisma Cloud Compute              | `prisma_cloud_compute_raw`                                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Proofpoint Targeted Attack        | `proofpoint_tap_raw`                                                                                                                             |
| Protection                        |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Scripts and commands metrics      | `scripts_and_commands_metrics`                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| SentinelOne DeepVisibility        | `sentinelone_deep_visibility_raw`                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ServiceNow CMDB                   | A ServiceNow CMDB dataset is created for each table configured for data collection using the format `servicenow_cmdb_<table name>_raw`.          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Salesforce.com                    | - `salesforce_connectedapplication_raw`                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_permissionset_raw`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_profile_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_groupmember_raw`                                                                                                                   |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_group_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_user_raw`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_userrole_raw`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_document_raw`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_contentfolder_raw`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_attachment_raw`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_contentdistribution_raw`                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_tenantsecuritylogin_raw`                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_useraccountteammember_raw`                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_tenantsecurityuserperm_raw`                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_account_raw`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_audit_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_login_raw`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `salesforce_eventlogfile_raw`                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Syslog/CEF                        | `<CEFVendor>_<CEFProduct>_raw`                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| USB devices connect and           | `xdr_data`                                                                                                                                       |
| disconnect events reported by the |                                                                                                                                                  |
| agent                             | > **Note**                                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - > You can query in XQL for this data and build widgets based on the `xdr_data` dataset or using the preset `device_control`.                   |
|                                   |                                                                                                                                                  |
|                                   | - > To view in an XQL query these events, the **Device Configuration** of the endpoint profile must be set to **Block**. Otherwise, the USB      |
|                                   |   > events are not captured. The events are also captured when a group of device types are blocked on the endpoints with a permanent or          |
|                                   |   > temporary exception in place. For more information, see Ingest Connect and Disconnect Events of USB Devices in                               |
|                                   |   > [/document/preview/1045014#UUID-9975c6ae-5ab4-f038-1a7f-2a1f9c3d12c8](/document/preview/1045014#UUID-9975c6ae-5ab4-f038-1a7f-2a1f9c3d12c8).  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| VPN logs (subset of `xdr_data`)   | VPN logs, such as GlobalProtect: `vpn_logs`                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | > **Note**                                                                                                                                       |
|                                   | >                                                                                                                                                |
|                                   | > The fields contained in this dataset are a subset of the fields in the `xdr_data` dataset.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows Endpoints using Cortex    | - `forensics_amcache`                                                                                                                            |
| XDR Forensics Add-on              |                                                                                                                                                  |
|                                   | - `forensics_application_resource_usage`                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_arp_cache`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_background_activity_monitor`                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_chrome_history`                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_cid_size_mru`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_command_history`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_dns_cache`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_edge_anaheim_history`                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_edge_spartan_history`                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_event_log`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_file_access`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_file_listing`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_firefox_history`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_handles`                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_hosts_file`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_internet_explorer_history`                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_jumplist`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_last_visited_pidl_mru`                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_log_me_in`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_net_sessions`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_network`                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_network_connectivity_usage`                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_network_data_usage`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_open_save_pidl_mru`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_port_listing`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_prefetch`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_process_execution`                                                                                                                  |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_process_listing`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_psreadline`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_recent_files`                                                                                                                       |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_recentfilecache`                                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_recycle_bin`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_registry`                                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_remote_access`                                                                                                                      |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_seven_zip_folder_history`                                                                                                           |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_shellbags`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_shimcache`                                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_team_viewer`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_typed_paths`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_typed_urls`                                                                                                                         |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_user_access_logging`                                                                                                                |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_user_assist`                                                                                                                        |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_windows_activities`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_winrar_arc_history`                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | - `forensics_word_wheel_query`                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows event logs via Cortex XDR | `microsoft_windows_raw`                                                                                                                          |
| Windows agents                    |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows Event Collector (WEC)     | - `xdr_data`                                                                                                                                     |
|                                   |                                                                                                                                                  |
|                                   | - `microsoft_windows_raw`                                                                                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows DHCP using Elasticsearch  | `microsoft_dhcp_raw`                                                                                                                             |
| Filebeat                          |                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows DNS Debug using           | Raw Data                                                                                                                                         |
| Elasticsearch Filebeat            |                                                                                                                                                  |
|                                   | - `microsoft_dns_raw`                                                                                                                            |
|                                   |                                                                                                                                                  |
|                                   | Normalized Stories                                                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | - `xdr_data` with the preset called `network_story`.                                                                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Workday                           | `workday_workday_raw`                                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Zscaler Cloud Firewall            | ZIA                                                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - Firewall logs: `zscaler_nssfwlog_raw`                                                                                                          |
|                                   |                                                                                                                                                  |
|                                   | - Web logs: `zscalar_nssweblog_raw`                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | ZPA                                                                                                                                              |
|                                   |                                                                                                                                                  |
|                                   | - `zscaler_zpa_raw`                                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

##### Presets

Presets offer groupings of `xdr_data` fields that are useful for
analyzing specific areas of network and endpoint activity. All of the
fields available for a preset are also available on the larger
`xdr_data` dataset, but by using the preset your query can run more
efficiently. Presets are sorted at random by the first one million
results found.

Two of the available presets are stories. These contain information
stitched together from Cortex XSIAM agent events and log files to form a
common schema. They are `authentication_story` and `network_story`.

You use the `preset` keyword to specify a dataset in your query.

#### About examples

The examples included in the topics are intended to illustrate the
behavior or usage of a particular stage or function. While these
examples can be based on real data that you could use on real-world
queries, you may need to tweak these queries to perform investigations
or otherwise solve real-world problems.

For examples of queries that illustrate useful investigative queries,
see the example Query Library that is available from the product user
interface:

Investigation & Response \> Search \> Query Builder \> XQL \> Query
Library

#### JSON functions

The Cortex Query Language (XQL) includes a number of JSON functions.
Before using any of these functions, it\'s important to understand how
Cortex XSIAM treats a JSON so you can accurately formulate your queries
using the correct syntax.

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.

##### \<json_path\>

Each JSON function includes defining a `<json_path>` in both the regular
syntax and when using the syntatic sugar format. The `<json_path>`
argument identifies the data of the JSON object you want to extract
using dot-notation. When using the regular syntax, the beginning of the
object is represented by a `$`. This `$` is not required when using the
syntatic sugar format.

If you have the following object:

    {
      "a_field" : "This is a_field value",
      "b_field" : {
                     "c_field" : "This is c_field value"
                  }
    }

Then the path using the regular syntax:

    $.a_field

Returns `"This is a_field value"`, while the path using the regular
syntax:

    $.b_field.c_field

Returns `"This is c_field value"`.

##### Field in \<json_path\> contains characters

###### In the regular syntax

When using the regular syntax to write your XQL queries and a field in
the `<json_path>` contains characters, such as a dot (.) or colon (:),
the syntax needs to be tweaked slightly to account for the
`<json_field>`.

For example, when using the `json_extract` function, the previous
regular syntax would need to be changed to an updated syntax to account
for the field in the `<json_path>` containing characters.

Previous regular syntax for the `json_extract` function:

    json_extract(<json_object_formatted_string>, <json_path>)

Updated regular syntax for the `json_extract` function, where the
`<json_field>` now includes single quotation marks as `'<json_field>'`:

    json_extract(<json_object_formatted_string>, "['<json_field>']")

For each JSON function, the regular syntax can change slightly, but the
`"['<json_field>']"` format is the same. The `"['<json_field>']"`
identifies the data you want to extract using dot-notation, where the
data extracted is dependent on your syntax.

If you have the following JSON object defined:

    {"a.b": 
        {"inn": 
            {"one":1}
        }
    }

To extract the data `{"one":1}`, the `"['<json_field>']"` would need to
be defined as `"$['a.b'].inn"` for all JSON functions. For example, when
using the `json_extract` function, the regular syntax is:

    json_extract(field_json_1, "$['a.b'].inn")

To extract the data `{"inn": {"one":1}}`, the `"['<json_field>']"` would
need to be defined as `"$['a.b']"` for all JSON functions. For example,
when using the `json_extract` function, the regular syntax is:

    json_extract(field_json_1, "$['a.b']")

If you have the following JSON object defined:

    {"a.b": 
        {"inn.inn": 
            {"one":1}
        }
    }

To extract the data `{"one":1}`, the `"['<json_field>']"` would need to
be defined as `"$['a.b']['inn.inn']"` for all JSON functions. For
example, when using the `json_extract` function, the regular syntax is:

    json_extract(json_field, "$['a.b']['inn.inn']")

###### In the syntatic sugar format

To make it easier for you to write your XQL queries, each JSON function
includes an optional syntatic sugar format as opposed to using the
regular syntax. When defining the syntatic sugar format and a field in
the `<json_path>` contains characters, such as a dot (.) or colon (:),
the syntax needs to be tweaked slightly to account for the
`<json_field>`.

For example, when using the `json_extract` function, the previous
syntatic sugar format would need to be changed to an updated syntax to
account for the field in the `<json_path>` containing characters.

Previous syntatic sugar format for the `json_extract` function:

    <json_object_formatted_string> -> <json_path>{}

Updated syntatic sugar format for the `json_extract` function, where the
`<json_field>` now includes quotations as `"<json_field>"`:

    <json_object_formatted_string> -> ["<json_field>"]{}

For each JSON function, the syntax of the syntatic sugar format can
change slightly, but the `["<json_field>"]` format is the same. The
`["<json_field>"]` identifies the data you want to extract using
dot-notation, where the data extracted is dependent on your syntax.

If you have the following JSON object defined:

    {"a.b": 
        {"inn": 
            {"one":1}
        }
    }

To extract the data `{"one":1}`, the `["<json_field>"]` would need to be
defined as `["a.b"].inn` for all JSON functions. For example, when using
the `json_extract` function, the syntatic sugar format is:

    json_field -> ["a.b"].inn{}

To extract the data `{"inn": {"one":1}}`, the `["<json_field>"]` would
need to be defined as `["a.b"]` for all JSON functions. For example,
when using the `json_extract` function, the syntatic sugar format is:

    json_field -> ["a.b"]{}

If you have the following `json_object` defined:

    {"a.b": 
        {"inn.inn": 
            {"one":1}
        }
    }

To extract the data `{"one":1}`, the `["<json_field>"]` would need to be
defined as `["a.b"]["inn.inn"]` for all JSON functions. For example,
when using the `json_extract` function, the syntatic sugar format is:

    json_field -> ["a.b"]["inn.inn"]{}

#### How to filter for empty values in the results table

When building a query, you can filter for empty values in the results
table, which can include or exclude null or empty strings. In the query
syntax, empty strings are represented as `""`, while null fields are
represented as `null`.

- Exclude null and empty strings using the following syntax:

<!-- -->

- <name of field> != null and <field name> != ""

<!-- -->

- Include null or empty strings using the following syntax:

<!-- -->

- <name of field> = null or <field name> = ""

Below is an example of filtering your endpoint data in the results table
to exclude all null values and any empty strings for a user.

    config timeframe = 90d
    | dataset = endpoints
    | filter endpoint_status in (CONNECTED, DISCONNECTED)
    | filter user != null and user != ""
    | fields user, group_names, endpoint_name

#### Understanding string manipulation in XQL

When defining string fields in Cortex Query Language (XQL) queries,
it\'s important to understand the various string manipulations available
and the syntax required to build effective queries that return the
results you\'re expecting. Cortex Query Language (XQL) uses
[RE2](https://github.com/google/re2/wiki/Syntax) for its regular
expression implementation.

Cortex XSIAM enables you to use single double quotes (`"<text>"`) or
triple double quotes (`"""<text>"""`) when defining your XQL syntax for
string manipulation. This specific syntax is used with different stages,
functions, and operators, with or without wildcards. Typically, the
`alter` and `filter` stages are used with single or triple double
quotes, so these stages are used in the examples provided below.

Using single double quotes

Single double quotes (`"<text>"`) include the following functionality:

- Treats the string value literally.

- Wildcards using the asterisk (\*) are processed as XQL wildcards, and
  match any sequence of characters.

- Escape sequences, such as `\n` (new line) or `\t` (tab), are not
  processed and are treated as plain characters.

`"\test\"` means to look for `\test\`

Using triple double quotes

Triple double quotes (`"""<text>"""`) include the following
functionality:

- Enables regex-style pattern matching and escape sequence
  interpretation.

- Escape sequences, such as `\n` (new line) or `\t` (tab), are
  processed.

- Wildcards using the asterisk (\*) are processed as XQL wildcards, and
  match any sequence of characters.

`"""\\test\\"""` means to look for `\test\`

**Understanding the results**:

- The double backslashes (`\\`) at the beginning becomes a single
  backlash (`\`) as it\'s processed as an escaped backslash.

- `test` is interpreted as literal.

- The double backslashes (`\\`) at the end becomes a single backlash
  (`\`) as it\'s processed as an escaped backslash.

Query example using alter

When using the `alter` stage, you can use both single (`"<text>"`) and
triple (`"""<text>"""`) double quotes when specifying string values. The
difference lies in how special characters and pattern matching are
interpreted.

    config timeframe = 10y 
    | dataset = test_dataset  
    | limit 1
    | alter test = "\test\"
    | alter test_triple = """\\\test\\"""
    | fields test, test_triple

**Understanding the query and results**

- `test` field using single double quotes:

  - The field value is `"\test\"`.

  - The output results display `\test\` exactly as defined in the field
    value as no escape sequences are processed.

- `test_triple` field using triple double quotes:

  - The field value is `"""\\\test\\"""`.

  - The output results display `\ est\` (with a tab between `\` and the
    text  `est`) because:

    - `\\`: First two backslashes become single backslash `\`.

    - `\t`: Interpreted as a tab.

    - `est`: Is interpreted as literal.

    - `\\`: Last two backslashes become single backslash `\`.

Query example using filter

When using the `filter` stage, you can use both single (`"<text>"`) and
triple (`"""<text>"""`) double quotes when specifying string values. The
difference lies in how special characters and pattern matching are
interpreted.

The examples provided are based on the following data table for a
dataset called `test_dataset`:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  Mar 26th 2022 19:26:07              12\\t3

  May 7th 2023 15:16:00               12 3

  Jun 8th 2024 16:56:27               1233

  Mar 26th 2024 19:26:07              123

  Apr 5th 2024 11:21:02               12\\t34563

  Apr 9th 2025 13:22:22               1233345

  May 9th 2025 13:22:22               12 35897

  May 30th 2025 21:45:02              116
  -----------------------------------------------------------------------

    config timeframe = 10y 
    | dataset = test_dataset  
    | filter test = "12\t3*"
    | fields test

**Output results table**:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  Mar 26th 2022 19:26:07              12\\t3

  Apr 5th 2024 11:21:02               12\\t34563
  -----------------------------------------------------------------------

**Explanation of results**:

The asterisk (`*`) in `"12\t3*"` means to process the string field as an
XQL wildcard by matching any sequence of characters that begins with
`12\t3`. In addition, the `\t` characters are not processed as an escape
character, but as plain characters.

    config timeframe = 10y 
    | dataset = test_dataset  
    | filter test = """12\t3*"""
    | fields test

**Output results table**:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  May 7th 2023 15:16:00               12 3

  May 9th 2025 13:22:22               12 35897
  -----------------------------------------------------------------------

**Explanation of results**:

The `\t` in `"""12\t3*"""` is processed as a tab escape character. The
asterisk (`*`) in `"""12\t3*"""` means to process the string field as an
XQL wildcard by matching any sequence of characters that begins with
`12<tab>3`.

### Build XQL queries

To support investigation and analysis, you can search your data by
creating queries in the Query Builder. You can create queries with
the Cortex Query Language (XQL) or by using the Query Builder templates.

#### About the Query Builder

The Query Builder aids in the detection of threats by allowing you to
search for indicators of compromise and suspicious patterns within data
sources. It assists in expanding case investigations by identifying
related events and entities, such as activities associated with specific
user accounts or network lateral movement. In addition, the Query
Builder enables data analytics on suspected threats, helping
organizations analyze large volumes of data to identify trends,
anomalies, and correlations that may indicate potential security issues.
The Query Builder also provides an interactive and visually intuitive
way for you to search assets and findings by their relationship types
and map them out in real-time.

To support investigation and analysis, you can search all of the data
ingested by Cortex XSIAM by creating queries in the Query Builder. You
can create queries that investigate leads, expose the root cause of an
issue, perform damage assessment, and hunt for threats from your data
sources.

Cortex XSIAM provides different options in the Query Builder for
creating queries:

- XQL (Build your own queries)

<!-- -->

- You can use the Cortex Query Language (XQL) to build complex and
  flexible queries that search specific datasets or presets, or the
  entire Cortex Data Model (XDM). With XQL Search, you create queries
  based on stages, functions, and operators. To help you build your
  queries, Cortex XSIAM provides tools in the interface that provide
  suggestions as you type, or you can look up predefined queries, common
  stages and examples. For more information, see [How to build XQL
  queries](#UUID125805d7e53750e71a87cb4c4140fa73).

  > **Note**

  > Schema changes to datasets may not be reflected in the autocomplete
  > suggestions and deﬁnitions as you type in real time the XQL query,
  > and can appear with a slight delay.

  > **Tip**

  > When creating XQL queries, you can:

  - > Use the up and down arrow keys to navigate through the
    > auto-suggestion commands and definitions.

  - > Select an auto-suggestion command by pressing either the **Enter**
    > or **Tab** key.

  - > Press **Shift**+**Enter** to add a new line, and easily ignore the
    > auto-suggestion output.

  - > Close the auto-suggestion output by pressing the **Esc** key.

<!-- -->

- Query Builder templates (No XQL knowledge required)

<!-- -->

- You can use the Query Builder templates to access your data without
  prior XQL knowledge. The templates include predefined filtering fields
  and key fieldsets, and can include any field from the XDM schema.

  As the templates are also based on XQL, you can also translate your
  template queries into XQL. With this flexibility, you can enrich the
  basic queries created by templates for more detailed investigation, or
  use the templates as a starting point for creating complex queries
  with full XQL functionality. For more information, see
  [/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834](/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834).

<!-- -->

- Graph Search to build queries to search assets, findings, and their
  contextual data. For more information, see [How to build Graph Search
  queries?](#UUIDb33e2aff7fda7b7becb9ff81ba480cd1).

> **Tip**
>
> If you prefer to use the Query Builder in **Legacy mode**, switch the
> toggle in the header. In Legacy mode, the Query Builder searches
> predefined datasets only. To search the full XDM Data Model, switch to
> **New mode** or select **XQL Search**.

#### How to build XQL queries

The Cortex Query Language (XQL) enables you to query data ingested into
Cortex XSIAM for rigorous endpoint and network event analysis. To help
you create an eﬀective XQL query with the proper syntax, the query ﬁeld
in the user interface provides suggestions and deﬁnitions as you type.

XQL forms queries in stages. Each stage performs a specific query
operation and is separated by a pipe character (\|). Queries require a
dataset, or data source, to run against. You can either query the Cortex
Data Model (XDM) or you can query specific datasets. In a dataset query,
unless otherwise specified, the query runs against the
`xdr_data` dataset, which contains all log information that Cortex XSIAM
collects from all Cortex product agents, including EDR data, and PAN
NGFW data. In XDM queries, you must specify the dataset mapped to the
XDM that you want to run your query against.

> **Important**
>
> Forensic datasets are not inlcuded by default in XQL query results,
> unless the dataset query is explicitly defined to use a forensic
> dataset.

##### Which datasets are mapped to XDM?

The Cortex Query Language (XQL) supports a single Cortex Data Model
(XDM), which is a normalized data structure. Datasets are mapped to the
XDM in 3 different ways:

1.  Automatic default mappings, including the following:

    - The `xdr_data` dataset is automatically mapped to the XDM with
      some data mapping exceptions.

    - Next-Generation Firewall (NGFW) network log data are mapped to the
      XDM from the following datasets:

      - `panw_ngfw_traffic_raw`

      - `panw_ngfw_threat_raw`

      - `panw_ngfw_url_raw`

      - `panw_ngfw_filedata_raw`

      - `panw_ngfw_globalprotect_raw`

      - `panw_ngfw_hipmatch_raw`

2.  Out-of-the-box mappings of the datasets as part of the Data Model
    Rules via the Marketplace. For more information, see [Cortex
    Marketplace](#UUIDbd7bb72a06838e5b74c7b3b159596497).

3.  You can create your own mappings by creating your own Data Model
    Rules. For more information, see [Create Data Model
    Rules](#UUIDae88d6b87191f2aff1599fbe27eb41fe).

For more information on the XDM Schema, specifically the fields,
fieldsets, fields designated as ENUMS (CONST), and aliases, see the
[Cortex XSIAM Data Model
Schema](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-Data-Model-Schema-Guide/Introduction).

##### XDM query syntax

The basic syntax structure for querying the Cortex Data Model (XDM) is:

    datamodel
        | <STAGE> ...
        | <STAGE> ...
        | <STAGE> ...

In a query using the `datamodel` command, unless specific datasets are
specified, a query will run against all mapped datasets, which contain
log information ingested by Cortex XSIAM. You can also install
Marketplace Content Packs, or map an ingested dataset into the XDM, to
query additional datasets.

In XDM queries that specify datasets, use either of the following
syntax:

    datamodel dataset in (<dataset_name>,...) …

or

    datamodel dataset = <dataset_name> …

Adding a wildcard suffix (\*) is supported in the `<dataset_name>`,
which matches all datasets that are mapped to the data model and begin
with the specified text. For example, `datamodel dataset = xdr*` or
`datamodel dataset in (xdr*)`.

When querying the XDM, fields that are not mapped to the XDM are
accessible by `<dataset>.<field>`. They can be used at any stage of a
`datamodel` query.

When creating XDM queries, auto-suggestions are available, according to
the existing XDM fields.

##### Dataset query syntax

In a dataset query, unless otherwise specified, the query runs against
the `xdr_data` dataset, which contains all log information that Cortex
XSIAM collects from all Cortex product agents, including EDR data, and
PAN NGFW data. In a dataset query, if you are running your query against
a dataset that has been set as default, there is no need to specify a
dataset. Otherwise, specify a dataset in your query. The Dataset Queries
lists the available datasets, depending on system configuration.

> **Note**

- > Users with different dataset permissions can receive different
  > results for the same XQL query.

- > An administrator or a user with a predefined user role can create
  > and view queries built with an unknown dataset that currently does
  > not exist in Cortex XSIAM. All other users can only create and view
  > queries built with an existing dataset.

- > When you have more than one dataset or lookup, you can change your
  > default dataset by navigating to Settings \> Configurations \> Data
  > Management \> Dataset Management, right-click on the appropriate
  > dataset, and select **Set as default**. For more information about
  > setting default datasets, see
  > [/document/preview/952274#UUID-ae82030e-2493-a33b-9a9e-a9834e993e93](/document/preview/952274#UUID-ae82030e-2493-a33b-9a9e-a9834e993e93).

The basic syntax structure for querying datasets that are not mapped to
the XDM is:

    dataset = <dataset name> 
        | <stage1> ...
        | <stage2> ... 
        | <stage3> ...

or

    dataset in (<dataset name>)
        | <stage1> ...
        | <stage2> ...
        | <stage3> ...

You can specify a dataset using one of the following formats, which is
based on the data retention offerings available in Cortex XSIAM.

- Hot Storage queries use the format `dataset = <dataset name>`. This is
  the default option.

<!-- -->

- dataset = xdr_data

<!-- -->

- Cold Storage queries use the format `cold_dataset = <dataset name>`.

<!-- -->

- cold_dataset = xdr_data

  > **Note**

  > You can build a query that investigates data in both a cold dataset
  > and a hot dataset in the same query. In addition, as the hot storage
  > dataset format is the default option and represents the fully
  > searchable storage, this format is used throughout this guide for
  > investigation and threat hunting. For more information on hot and
  > cold storage, see
  > [/document/preview/952274#UUID-ae82030e-2493-a33b-9a9e-a9834e993e93](/document/preview/952274#UUID-ae82030e-2493-a33b-9a9e-a9834e993e93).

When using the hot storage default format, this returns every `xdr_data`
record contained in your Cortex XSIAM instance over the time range that
you provide to the Query Builder user interface. This can be a large
amount of data, which may take a long time to retrieve. You can use a
`limit` stage to specify how many records you want to retrieve.

There is no practical limit to the number of stages that you can
specify. See [Stages](#UUID877336c467ba7af1a4331269479e3e8e) for
information on all the supported stages.

In the `xdr_data` dataset, every user ﬁeld included in the raw data for
network, authentication, and login events has an equivalent normalized
user ﬁeld associated with it that displays the user information in the
following standardized format:

`<company domain>\<username>`

For example, the `login_data` ﬁeld has the
`login_data_dst_normalized_user` ﬁeld to display the content in the
standardized format. To ensure the most accurate results, we recommend
that you use these `normalized_user` ﬁelds when building your queries.

##### Additional components

XQL queries can contain different components, such as functions and
stages, depending on the type of query you want to build. For a complete
list of the syntax options available with example queries, see
[Stages](#UUID877336c467ba7af1a4331269479e3e8e) and
[Functions](#UUIDe74efd8b8558b7a11ca8525d6b6a30b2).

##### Get started with XQL queries

Before you begin running XQL queries, consider the following
information:

- Use the interface to help you build queries

<!-- -->

- Cortex XSIAM offers features in the XQL search interface to help you
  build queries. For more information, see [Useful XQL user interface
  features](#UUIDbb726d45b210ab19bb423d3db545b858).

<!-- -->

- Mitigate long-running queries

<!-- -->

- Querying the XDM enables searching of Cortex XSIAM\'s extensive data.
  We recommend that you use filters to streamline your queries. For more
  information, see [XQL Query best
  practices](#UUIDdd21d96bea0bbaad472c6edd7f13392e).

<!-- -->

- Understand query defaults and limitations

<!-- -->

- Before you run a query, review this list to better understand query
  behavior and results. For more information, see [Expected results when
  querying fields](#UUIDd7cc9384a8e5611f2bbe36dc6f725f00).

<!-- -->

- Translate Splunk queries to XQL

<!-- -->

- If you have existing Splunk queries, you can translate them to XQL.
  For more information, see [Translate to
  XQL](#UUIDdba75cce040d194c73378d1c87dc8628).

> **Tip**
>
> If you are new to creating queries, you can also try our simple search
> templates, which can help you get started in understanding how queries
> work. See
> [/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834](/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834).

##### Useful XQL user interface features

The user interface contains several useful features for querying data,
and for viewing results:

- **XQL query**: The XQL query field is where you define the parameters
  of your query. To help you create an effective XQL query, the search
  field provides suggestions and definitions as you type.

<!-- -->

- > **Note**

  > Schema changes to datasets may not be reflected in the autocomplete
  > suggestions and deﬁnitions as you type in real time the XQL query
  > and can appear with a slight delay.

  > **Tip**

  > When creating XQL queries, you can:

  - > Use the up and down arrow keys to navigate through the
    > auto-suggestion command suggestions and definitions.

  - > Select an auto-suggestion command by pressing either the **Enter**
    > or **Tab** key.

  - > Press **Shift**+**Enter** to add a new line, and easily ignore the
    > auto-suggestion output.

  - > Close the auto-suggestion output by pressing the **Esc** key.

<!-- -->

- **Translate to XQL**: Converts your existing Splunk queries to the XQL
  syntax. When you enable Translate to XQL , both an **SPL query** field
  and an **XQL query** field are displayed. You can easily add a Splunk
  query, which is converted automatically into XQL in the **XQL query**
  ﬁeld. This option is disabled by default.

- **Query Results**: After you create and run an XQL query, you can
  view, filter, and visualize your **Query Results**.

- **XQL Helper**: Describes common stage commands and provides examples
  that you can use to build a query.

- **Query Library**: Contains common, predefined queries that you can
  use or modify to your liking. In addition, there is a personal query
  library for saving and managing your own queries so that you can share
  with others, and queries can be shared with you. For more information,
  see [Manage your personal query
  library](#UUID9eadb61fac4a89b3f3165d6bbc06ef1b).

- **Schema**: Contains schema information for every field found in the
  result set. This information includes the field name, data type,
  descriptive text (if available), and the dataset that contains the
  field.

  - For dataset queries, it contains the list of all the fields of all
    the datasets that were involved in the query.

  - For data model queries, it contains the list of all the data model
    fields.

##### XQL Query best practices

Cortex XSIAM includes built-in mechanisms for mitigating long-running
queries, such as default limits for the maximum number of allowed
issues, and for the maximum number of returned rows. Only specified
mapped datasets are searched when querying by the Cortex Data Model
(XDM) to use system resources and time more efficiently. The following
suggestions can help you to streamline your queries:

- Add a smaller limit to queries by using a `limit` stage.

<!-- -->

- To help reduce the Cortex Query Language (XQL) response time, the
  default results for an XDM query or an XQL dataset query is limited to
  1000, when no limit is explicitly stated in the query. This applies to
  basic queries with no stages except the `fields` stage. This default
  limit does not apply to widgets, Correlation Rules, public APIs, saved
  queries, or scheduled queries, where the limit is a maximum of
  1,000,000 results. Queries based on legacy templates are limited to
  10,000 results. Adding a smaller limit can greatly reduce the response
  time.

      datamodel dataset = microsoft_windows_raw 
      | fields *host* 
      | limit 100

<!-- -->

- Use a small time frame for queries by specifying the specific date and
  time in the **Timeframe**, such as selecting **Relative time** and
  defining **Last 30 Minutes**, instead of picking the nearest larger
  option available or defining an extended time period.

- Use filters that exclude data, along with other possible filters.

- Select the specific fields that you would like to see in the query
  results.

##### Expected results when querying fields

The following are returned when querying fields:

- If specific fields are stated in the
  [fields](#UUIDa22fb161beb7d67c6d9bc8c52d66f3bd) stage, those exact
  fields will be returned. 

- If no fields are stated in the query, the `xdm_core` fieldset will be
  returned.

- Unmapped fields are treated as NULL. An unmapped field is an `xdm`
  field that hasn\'t been mapped from the relevant datasets using a Data
  Model Rule.

- By default, the `_time` system field will be added to all data model
  queries. Yet, the `_time` system field will not be added to queries
  that contain the `comp` stage.

- For dataset queries, all current system fields will be returned, even
  if they are not stated in the query.

- For UNION between XDM and dataset, each part of the UNION will return
  its own fields.

- Each new column in the result set created by the
  [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage will be added as
  the last column. You can specify a different column order by modifying
  the field order in the [fields](#UUIDa22fb161beb7d67c6d9bc8c52d66f3bd)
  stage of the query.

- Each new column in the result set created by the
  [/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
  stage will be added as the last column. Other fields that are not in
  the `group by / calculated` column will be removed from the result
  set, including the core fields and `_time` system field.

- When no limit is explicitly stated in a `datamodel` query, a maximum
  of 1000 results are returned (default). When this limit is applied to
  results using the [limit](#UUIDa42977faddf5d14f266e03147a8b4cf3)
  stage, it will be indicated in the user interface.

##### Create XQL query

Review the following topics:

- [How to build XQL queries](#UUID125805d7e53750e71a87cb4c4140fa73)

Build Cortex Query Language (XQL) queries to analyze raw log data stored
in Cortex XSIAM. You can query the Cortex Data Model (XDM) or datasets
using specific syntax.

How to create a XDM query

1.  From Cortex XSIAM, select Investigation & Response \> Search \>
    Query Builder.

2.  Click **XQL**.

3.  *(Optional)* Change the default time period against which to run
    your query from the time picker at the top right of the window. You
    can select the required time period from any of the following
    options available:

    - Preset time ranges easily available to select from, such as
      **24 hours** and **30 days**.

    - Recently used selections from your previous queries.

    - **Relative time**: Define the time frame as the last \<number\>
      minutes, days, or hours by setting the number.

    - **Calendar**: Create a customized time period by selecting the
      date range from the calendar and the specific **Start Time** and
      **End Time**.

- > **Note**

  - > Whenever the time period is changed in the query window, the
    > `config timeframe` is automatically set to the time period
    > defined, but this won\'t be visible as part of the query. Only if
    > you manually type in the `config timeframe` will this be seen in
    > the query.

  - > These time picker options are available in XQL queries when using
    > the Query Builder, XQL Widgets, and when defining XQL Widgets in
    > Reports and Dashboards.

4.  *(Optional)* To translate Splunk queries to XQL queries, enable
    **Translate to XQL**. If you choose to use this feature, enter your
    Splunk query in the **Splunk** field, click the arrow icon to
    convert to XQL, and then go to
    [#UUID5f5b967337c3cb75a413d47e8b461681_N1669623521916](#Xb3f9aeb8c32cc199d334d4945dd6349f40021ed).

5.  Create your query by typing in the query field. Relevant commands,
    their definitions, and operators are suggested as you type.

- > **Tip**

  > When creating XQL queries, you can:

  - > Use the up and down arrow keys to navigate through the
    > auto-suggestion command suggestions and definitions.

  - > Select an auto-suggestion command by pressing either the **Enter**
    > or **Tab** key.

  - > Press **Shift**+**Enter** to add a new line, and easily ignore the
    > auto-suggestion output.

  - > Close the auto-suggestion output by pressing the **Esc** key.

  a.  Specify the datasets to run your query against by typing either
      `datamodel dataset = <dataset name>...` or
      `datamodel dataset in (<dataset name>,...)...`. For example:

  - datamodel dataset in (amazon_aws_raw)

    > **Note**

    > While `datamodel dataset=*` is supported in the query, we
    > recommend that you specify specific datasets for quicker and more
    > efficient results.

  b.  Press Enter, and then type the pipe character (`|`). Select a
      stage, and complete the stage syntax using the suggested options.

  c.  Continue adding stages until your query is complete. For example:

  - datamodel dataset in (amazon_aws_raw)
            | filter xdm.source.ipv4 = "10.9.165.1"
            | fields xdm.source.ipv4, xdm.source.port
            | limit 100  

6.  Choose when to run your query:

    - Run the query immediately.

    - Run the query by the specified date and time, or on a specific
      date, by selecting the calendar icon
      (![](media/rId2810.png){width="0.30302930883639545in"
      height="0.20833333333333334in"}).

7.  *(Optional)* The Save As options save your query for future use:

    - Correlation Rule: When compatible, saves the query as a
      Correlation Rule. For more information, see [What\'s a correlation
      rule?](#UUIDaa8a139a1b00c4c5d40d7c25de20b762).

    - Query to Library: Saves the query to your personal query library.
      For more information, see [Manage your personal query
      library](#UUID9eadb61fac4a89b3f3165d6bbc06ef1b).

    - Widget to Library: For more information, see
      <urn:resource:component:1159521>.

> **Tip**
>
> While the query is running, you can navigate away from the page. A
> notification is sent when the query has finished. You can also
> **Cancel** the query or run a new query, where you have the option to
> **Run only new query (cancel previous)** or **Run both queries**.

How to create a dataset query

1.  From Cortex XSIAM, select Investigation & Response \> Search \>
    Query Builder.

2.  Click **XQL**.

3.  *(Optional)* Change the default time period against which to run
    your query from the time picker at the top right of the window. You
    can select the required **Timeframe** from any of the following
    options available:

    - Preset time ranges easily available to select from, such as
      **24 hours** and **30 days**.

    - Recently used selections from your previous queries.

    - **Relative time**: Define the time frame as the last \<number\>
      minutes, days, or hours by setting the number.

    - **Calendar**: Create a customized time period by selecting the
      date range from the calendar and the specific **Start Time** and
      **End Time**.

- > **Note**

  - > Whenever the time period is changed in the query window, the
    > `config timeframe` is automatically set to the time period
    > defined, but this won\'t be visible as part of the query. Only if
    > you manually type in the `config timeframe` will this be seen in
    > the query.

  - > These time picker options are available in XQL queries when using
    > the Query Builder, XQL Widgets, and when defining XQL Widgets in
    > Reports and Dashboards.

4.  *(Optional)* To translate Splunk queries to XQL queries, enable
    **Translate to XQL**. If you choose to use this feature, enter your
    Splunk query in the **Splunk** field, click the arrow icon
    (![](media/rId2815.png){width="0.3020833333333333in"
    height="0.20833333333333334in"}) to convert to XQL, and then go to
    [#UUID5f5b967337c3cb75a413d47e8b461681_stepidm151669624932174](#Xbae59d30f3ba27fa706bd5689848133f8412c1e).

5.  Create your query by typing in the query field. Relevant commands,
    their definitions, and operators are suggested as you type.

- > **Tip**

  > When creating XQL queries, you can:

  - > Use the up and down arrow keys to navigate through the
    > auto-suggestion command suggestions and definitions.

  - > Select an auto-suggestion command by pressing either the **Enter**
    > or **Tab** key.

  - > Press **Shift**+**Enter** to add a new line, and easily ignore the
    > auto-suggestion output.

  - > Close the auto-suggestion output by pressing the **Esc** key.

  a.  (Optional) Specify a dataset.

  - You only need to specify a dataset if you are running your query
    against a dataset that you have not set as default. Otherwise, the
    query runs against the `xdr_data` dataset. For more information, see
    [How to build XQL queries](#UUID125805d7e53750e71a87cb4c4140fa73).

        dataset = xdr_data

  b.  Press **Enter**, and then type the pipe character (`|`). Select a
      command, and complete the command using the suggested options.

  c.  Continue adding stages until your query is complete.

  - dataset = xdr_data 
        | filter agent_os_type = ENUM.AGENT_OS_MAC
        | limit 250  

6.  Choose when to run your query:

    - Run the query immediately.

    - Run the query by the specified date and time, or on a specific
      date, by selecting the calendar icon
      (![](media/rId2810.png){width="0.30302930883639545in"
      height="0.20833333333333334in"}).

7.  *(Optional)* The Save As options save your query for future use:

    - BIOC Rule: When compatible, saves the query as a BIOC rule. The
      XQL query must contain a filter for the **event_type** field.

    - Correlation Rule: When compatible, saves the query as a
      Correlation Rule. For more information, see [What\'s a correlation
      rule?](#UUIDaa8a139a1b00c4c5d40d7c25de20b762).

    - Query to Library: Saves the query to your personal query library.
      For more information, see [Manage your personal query
      library](#UUID9eadb61fac4a89b3f3165d6bbc06ef1b).

    - Widget to Library: For more information, see
      <urn:resource:component:1159521>.

> **Tip**
>
> While the query is running, you can navigate away from the page. A
> notification is sent when the query has finished. You can also
> **Cancel** the query or run a new query, where you have the option to
> **Run only new query (cancel previous)** or **Run both queries**.

##### Review XQL query results

Review the following topics:

- [How to build XQL queries](#UUID125805d7e53750e71a87cb4c4140fa73)

- [Create XQL query](#UUID5f5b967337c3cb75a413d47e8b461681)

The results of a Cortex Query Language (XQL) query are displayed in a
tab called **Query Results**.

> **Note**
>
> It\'s also possible to graph the results displayed. For more
> information, see [Graph query
> results](#UUID66d5f7c34cf5b98b79e931ea76c83b11).

###### Understanding the options available to investigate results

Use the following options in the **Query Results** tab to investigate
your query results:

+-----------------------------------+---------------------------------------------------------+
| Option                            | Use                                                     |
+===================================+=========================================================+
| Table tab                         | Displays results in rows and columns according to the   |
|                                   | entity ﬁelds. Columns can be filtered, using their      |
|                                   | filter icons.                                           |
|                                   |                                                         |
|                                   | More options (kebab icon                                |
|                                   | ![](media/rId2824.png){width="0.14583333333333334in"    |
|                                   | height="0.20833333333333334in"}) displays table layout  |
|                                   | options, which are divided into different sections:     |
|                                   |                                                         |
|                                   | - In the **Appearance** section, you can                |
|                                   |   **Show line breaks** for any text field in the        |
|                                   |   **Query Results**. By default, the text in these      |
|                                   |   fields are wrapped unless the **Show line breaks**    |
|                                   |   option is selected. In addition, you can change the   |
|                                   |   way rows and columns are displayed.                   |
|                                   |                                                         |
|                                   | - In the **Log Format** section, you can change the way |
|                                   |   that logs are displayed:                              |
|                                   |                                                         |
|                                   |   - **RAW**: Raw format of the entity in the database.  |
|                                   |                                                         |
|                                   |   - **JSON**: Condensed JSON format with key value      |
|                                   |     distinctions. NULL values are not displayed.        |
|                                   |                                                         |
|                                   |   - **TREE**: Dynamic view of the JSON hierarchy with   |
|                                   |     the option to collapse and expand the different     |
|                                   |     hierarchies.                                        |
|                                   |                                                         |
|                                   | - In the **Search column** section, you can find a      |
|                                   |   specific column; enable or disable display of columns |
|                                   |   using the checkboxes.                                 |
|                                   |                                                         |
|                                   | Show and hide rows according to a specific field in a   |
|                                   | specific event: select a cell, right-click it, and then |
|                                   | select either Show rows with ... or Hide rows with ...  |
+-----------------------------------+---------------------------------------------------------+
| Graph tab                         | Use the **Chart Editor** to visualize the query         |
|                                   | results.                                                |
+-----------------------------------+---------------------------------------------------------+
| Advanced tab                      | Displays results in a table format which aggregates the |
|                                   | entity ﬁelds into one column. You can change the        |
|                                   | layout, decide whether to **Show line breaks** for any  |
|                                   | text field in the results table, and change the log     |
|                                   | format from the                                         |
|                                   | ![](media/rId2824.png){width="0.14583333333333334in"    |
|                                   | height="0.20833333333333334in"} menu.                   |
|                                   |                                                         |
|                                   | Select **Show more** to pivot an **Expanded View** of   |
|                                   | the event results that include NULL values. You can     |
|                                   | toggle between the **JSON** and **Tree** views, search, |
|                                   | and **Copy to clipboard**.                              |
+-----------------------------------+---------------------------------------------------------+
| Export to File                    | Exports the results to a TSV (tab-separated values)     |
|                                   | ﬁle.                                                    |
|                                   |                                                         |
|                                   | - More options                                          |
|                                   |   (![](media/rId2824.png){width="0.14583333333333334in" |
|                                   |   height="0.20833333333333334in"}) works in a similar   |
|                                   |   way to how it works on the **Table** tab.             |
|                                   |                                                         |
|                                   | - **Show more** in the bottom left corner of each row   |
|                                   |   opens the **Expanded View** of the event results that |
|                                   |   also include NULL values. Here, you can toggle        |
|                                   |   between the **JSON** and **Tree** views, search, and  |
|                                   |   **Copy to clipboard**.                                |
|                                   |                                                         |
|                                   | - **Log format** options change the way that logs are   |
|                                   |   displayed:                                            |
|                                   |                                                         |
|                                   |   - RAW: Raw format of the entity in the database.      |
|                                   |                                                         |
|                                   |   - JSON: Condensed JSON format with key value          |
|                                   |     distinctions. NULL values are not displayed.        |
|                                   |                                                         |
|                                   |   - TREE: Dynamic view of the JSON hierarchy with the   |
|                                   |     option to collapse and expand the diﬀerent          |
|                                   |     hierarchies.                                        |
+-----------------------------------+---------------------------------------------------------+
| Refresh                           | Refreshes the query results.                            |
+-----------------------------------+---------------------------------------------------------+
| Free text search                  | Searches the query results for text that you specify in |
|                                   | the free text search. Click the **Free text search**    |
|                                   | icon to reveal or hide the free text search field.      |
+-----------------------------------+---------------------------------------------------------+
| Filter                            | Enables you to ﬁlter a particular ﬁeld in the interface |
|                                   | that is displayed to specify your ﬁlter criteria.       |
|                                   |                                                         |
|                                   | For integer, boolean, and timestamp (such as `_time`)   |
|                                   | ﬁelds, we recommend that you use the **Filter** instead |
|                                   | of the **Free text** search, in order to retrieve the   |
|                                   | most accurate query results.                            |
+-----------------------------------+---------------------------------------------------------+
| Fields menu                       | Filters query results. To quickly set a ﬁlter, Cortex   |
|                                   | XSIAM displays the top ten results from which you can   |
|                                   | choose to build your ﬁlter. This option is only         |
|                                   | available in the **Table** and **Advanced** tabs,       |
|                                   |                                                         |
|                                   | From within the Fields menu, click on any ﬁeld          |
|                                   | (excluding JSON and array ﬁelds) to see a histogram of  |
|                                   | all the values found in the result set for that ﬁeld.   |
|                                   | This histogram includes:                                |
|                                   |                                                         |
|                                   | - A count of the total number of times a value was      |
|                                   |   found in the result set.                              |
|                                   |                                                         |
|                                   | - The value\'s frequency as a percentage of the total   |
|                                   |   number of values found for the ﬁeld.                  |
|                                   |                                                         |
|                                   | - A bar chart showing the value\'s frequency.           |
|                                   |                                                         |
|                                   | > **Note**                                              |
|                                   | >                                                       |
|                                   | > In order for Cortex XSIAM to provide a histogram for  |
|                                   | > a ﬁeld, the ﬁeld must not contain an array or a JSON  |
|                                   | > object.                                               |
+-----------------------------------+---------------------------------------------------------+

###### Available options for saving results

The Save As options save your query for future use:

- BIOC Rule: When compatible, saves the query as a BIOC rule. The XQL
  query must contain a filter for the **event_type** field.

- Correlation Rule: When compatible, saves the query as a Correlation
  Rule. For more information, see [What\'s a correlation
  rule?](#UUIDaa8a139a1b00c4c5d40d7c25de20b762).

- Query to Library: Saves the query to your personal query library. For
  more information, see [personal query
  library](#UUID9eadb61fac4a89b3f3165d6bbc06ef1b).

- Widget to Library: For more information, see
  <urn:resource:component:1159521>.

###### Investigating results in the Causality View or Timeline View

You can continue investigating the query results in the Causality View
or Timeline by right-clicking the event and selecting the desired view.
This option is available for the following types of events:

- Process (except for those with an event sub-type of termination)

- Network

- File

- Registry

- Injection

- Load image

- System calls

- Event logs for Windows

- System authentication logs for Linux

For network stories, you can pivot to the Causality View only. For cloud
Cortex XSIAM events and Cloud Audit Logs, you can only pivot to the
Cloud Causality View, while software-as-a-service (SaaS) related issues
for audit stories, such as Office 365 audit logs and normalized logs,
you can only pivot to the SaaS Causality View.

###### Add file path to Malware Profile allowed list

Add a file path to your existing Malware Profile allowed list by
right-clicking a \<path\> field, such as **target_process_path**, and
select **Add \<path type\> to malware profile allow list**.

##### Translate to XQL

To help you easily convert your existing Splunk queries to the Cortex
Query Language (XQL) syntax, Cortex XSIAM includes a toggle called
**Translate to XQL** in the query ﬁeld in the user interface. When
building your XQL query and this option is selected, both a
**SPL query** field and **XQL query** field are displayed, so you can
easily add a Splunk query, which is converted to XQL in the XQL query
field. This option is disabled by default, so only the **XQL query**
field is displayed.

> **Important**
>
> This feature is still in a Beta state and you will find that not all
> Splunk queries can be converted to XQL. This feature will be improved
> upon in the upcoming releases to support greater Splunk query
> translations to XQL.

Supported functions in Splunk

The following table details the supported functions in Splunk that can
be converted to XQL in Cortex XSIAM with an example of a Splunk query
and the resulting XQL query. In each of these examples, the `xdr_data`
dataset is used.

+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Splunk Function/Stage       | Splunk Query Example                                                                                                                                       | Resulting XQL Query Example                                                                                                                                                                                                          |
+=============================+============================================================================================================================================================+======================================================================================================================================================================================================================================+
| `avg`                       | `index=xdr_data | stats avg(dst_association_strength)`                                                                                                     | `dataset in (xdr_data) | comp avg(dst_association_strength)`                                                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `bin`                       | `index = xdr_data | bin _time span=5m`                                                                                                                     | `dataset in (xdr_data) | bin _time span=5m`                                                                                                                                                                                          |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `coalesce`                  | `index= xdr_data | eval product_or_vendor_not_null=coalesce(_product, _vendor )`                                                                           | `dataset in (xdr_data) | alter product_or_vendor_not_null = coalesce(_product, _vendor)`                                                                                                                                             |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `count`                     | `index=xdr_data | stats count(_product) BY _time`                                                                                                          | `dataset in (xdr_data) | comp count(_product) by _time`                                                                                                                                                                              |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ctime`                     | `index=xdr_data | convert ctime(field) as field`                                                                                                           | `dataset in (xdr_data) | alter field = format_timestamp("%m/%d/%Y %H:%M:%S", to_timestamp(field))`                                                                                                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `earliest`                  | `index = xdr_data earliest=24d`                                                                                                                            | `dataset in (xdr_data) | filter _time >= to_timestamp(add(to_epoch(current_time()),2073600000))`                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `eval`                      | `index=xdr_data | eval field = "test"`                                                                                                                     | `dataset in (xdr_data) | alter field = "test"`                                                                                                                                                                                       |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fillnull`                  | `index=xdr_data | fillnull value = "missing ipv6" agent_ip_addresses_v6`                                                                                   | `dataset in (xdr_data) | replacenull agent_ip_addresses_v6 = "missing ipv6"`                                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `floor`                     | `index=xdr_data | eval floor_test = floor(1.9)`                                                                                                            | `dataset in (xdr_data) | alter floor_test = floor(1.9)`                                                                                                                                                                              |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `iplocation`                | `index=xdr_data | inputlookup append=true my_lookup.csv`                                                                                                   | `dataset in (xdr_data) | union (dataset=my_lookup | limit 1000000000)`                                                                                                                                                               |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `iplocation`                | `index = xdr_data | inputlookup agent_ip_addresses`                                                                                                        | `dataset in (xdr_data) | iploc agent_ip_addresses loc_continent AS Continent, loc_country AS Country, loc_region AS Region, loc_city AS City, loc_latlon AS lon`                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `isnotnull`                 | `index=xdr_data | eval x = isnotnull(agent_hostname)`                                                                                                      | `dataset in (xdr_data)\n | alter x = if(agent_hostname != null, true, false)`                                                                                                                                                        |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `isnull`                    | `index=xdr_data | eval x = isnull(agent_hostname)`                                                                                                         | `dataset in (xdr_data)\n | alter x = if(agent_hostname = null, true, false)`                                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `json_extract`              | `index= xdr_data | eval London=json_extract(dfe_labels,"dfe_labels{0}")`                                                                                   | `dataset in (xdr_data) | alter London = dfe_labels -> dfe_labels[0]{}`                                                                                                                                                               |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `join`                      | `join agent_hostname [index = xdr_data]`                                                                                                                   | `join type=left conflict_strategy=right (dataset in (xdr_data)) as inner agent_hostname = inner.agent_hostname`                                                                                                                      |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `latest`                    | `index = xdr_data latest=-24d`                                                                                                                             | `dataset in (xdr_data) |filter _time <= to_timestamp(add(to_epoch(date_floor(current_time(),"d")),-2073600000))`                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `len`                       | `index = xdr_data | where uri != null | eval length = len(agent_ip_address)`                                                                               | `dataset in (xdr_data) | filter agent_ip_addresses != null | alter agent_ip_address_length = len(agent_ip_addresses)`                                                                                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ltrim(<str>,<trim_chars>)` | `index=xdr_data | eval trimed_agent=ltrim("agent_hostname", "agent_")`                                                                                     | `dataset in (xdr_data) | alter trimed_agent = ltrim("agent_hostname", "agent_")`                                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `lower`                     | `index = xdr_data | eval field = lower("TEST")`                                                                                                            | `dataset in (xdr_data) | alter field = lowercase("TEST")`                                                                                                                                                                            |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `max`                       | `index =xdr_data | stats max(action_file_size) by _product`                                                                                                | `dataset in (xdr_data) | comp max(action_file_size) by _product`                                                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `md5`                       | `index=xdr_data | eval md5_test = md5("test")`                                                                                                             | `dataset in (xdr_data) | alter md5_test = md5("test")`                                                                                                                                                                               |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `median`                    | `index = xdr_data | stats median(actor_process_file_size) by _time`                                                                                        | `dataset in (xdr_data) | comp median(actor_process_file_size) by _time`                                                                                                                                                              |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `min`                       | `index =xdr_data | stats min(action_file_size) by _product`                                                                                                | `dataset in (xdr_data) | comp min(action_file_size) by _product`                                                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvcount`                   | `index = xdr_data | where http_data != null | eval http_data_array_length = mvcount(http_data)`                                                            | `dataset in (xdr_data) | filter http_data != null | alter http_data_array_length = array_length(http_data)`                                                                                                                          |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvdedup`                   | `index = xdr_data | eval s=mvdedup(action_app_id_transitions)`                                                                                             | `dataset in (xdr_data) | alter s = arraydistinct(action_app_id_transitions)`                                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvexpand`                  | `index = xdr_data | mvexpand dfe_labels limit = 100`                                                                                                       | `dataset in (xdr_data) | arrayexpand dfe_labels limit 100`                                                                                                                                                                           |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvfilter`                  | `index = xdr_data | eval x = mvfilter(isnull(dfe_labels))`                                                                                                 | `dataset in (xdr_data) | alter x = arrayfilter(dfe_labels, if("@element" = null, true, false) = true)`                                                                                                                               |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvindex`                   | `index=xdr_data | eval field = mvindex(action_app_id_transitions, 0)`                                                                                      | `dataset in (xdr_data) | alter field = arrayindex(action_app_id_transitions, 0)`                                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mvjoin`                    | `index=xdr_data | eval n=mvjoin(action_app_id_transitions, ";")`                                                                                           | `dataset in (xdr_data) | alter n = arraystring(action_app_id_transitions, ";")`                                                                                                                                                      |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pow`                       | `index=xdr_data | eval pow_test = pow(2, 3)`                                                                                                               | `dataset in (xdr_data) | alter pow_test = pow(2, 3)`                                                                                                                                                                                 |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `relative_time(X,Y)`        | - `index ="xdr_data" | where _time > relative_time(now(),"-7d@d")`                                                                                         | - `dataset in (xdr_data) | filter _time > to_timestamp(add(to_epoch(date_floor(current_time(),"d")),-604800000))`                                                                                                                    |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index ="xdr_data" | where _time > relative_time(now(),"+7d@d")`                                                                                         | - `dataset in (xdr_data)| filter _time > to_timestamp(add(to_epoch(date_floor(current_time(),"d")),604800000))`                                                                                                                      |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `replace`                   | `index= xdr_data | eval description = replace(agent_hostname,"\("."NEW")`                                                                                  | `dataset in (xdr_data) | alter description = replace(agent_hostname, concat("\(", "NEW"))`                                                                                                                                           |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rex`                       | `index=xdr_data action_local_ip!="0.0.0.0" | rex field=action_local_ip "(?<src_ip>\d+\.\d+\.\d+\.48)" | where src_ip != "" | table action_local_ip src_ip` | `dataset in (xdr_data) |filter (action_local_ip != "0.0.0.0" AND action_local_ip != null) | alter src_ip = arrayindex(regextract(action_local_ip, "(\d+\.\d+\.\d+\.48)"), 0) | filter src_ip != "" | fields action_local_ip, src_ip` |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `round`                     | `index=xdr_data | eval round_num = round(3.5)`                                                                                                             | `dataset in (xdr_data) | alter round_num = round(3.5)`                                                                                                                                                                               |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rtrim`                     | `index=xdr_data | eval trimed_hostname=rtrim("agent_hostname", "hostname")`                                                                                | `dataset in (xdr_data) | alter trimed_hostname = rtrim("agent_hostname", "hostname")`                                                                                                                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `search`                    | `index = xdr_data | eval ip="192.0.2.56" | search ip="192.0.2.0/24"`                                                                                       | `dataset in (xdr_data) | alter ip = "192.0.2.56" | filter incidr(ip,"192.0.2.0/24") = true`                                                                                                                                          |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sha256`                    | `index = xdr_data | eval sha256_test = sha256("test")`                                                                                                     | `dataset in (xdr_data) | alter sha256_test = sha256("test")`                                                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sort (ascending order)`    | `index = xdr_data | sort action_file_size`                                                                                                                 | `dataset in (xdr_data) | sort asc action_file_size | limit 10000`                                                                                                                                                                    |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sort (descending order)`   | `index = xdr_data | sort -action_file_size`                                                                                                                | `dataset in (xdr_data) | sort desc action_file_size | limit 10000`                                                                                                                                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `spath`                     | `index = xdr_data | spath output=myfield input=action_network_http path=headers.User-Agent`                                                                | `dataset in (xdr_data) | alter myfield = json_extract(action_network_http ,"$.headers.User-Agent")`                                                                                                                                  |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `split`                     | `index = xdr_data | where mac != null | eval split_mac_address = split(mac, ":")`                                                                          | `dataset in (xdr_data)\n | filter mac != null\n | alter split_mac_address = split(mac, ":")`                                                                                                                                         |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stats`                     | `index=xdr_data | stats count(event_type) by _time`                                                                                                        | `dataset in (xdr_data) | comp count(event_type) by _time`                                                                                                                                                                            |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stats dc`                  | `index = xdr_data | stats dc(_product) BY _time`                                                                                                           | `dataset in (xdr_data) | comp count_distinct(_product) by _time`                                                                                                                                                                     |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `strcat`                    | `index=xdr_data | strcat story_id "/" http_req_before_method comboIP`                                                                                      | `dataset in (xdr_data) | alter comboIP=concat(if(story_id!=null,story_id,""),"/",if(http_req_before_method!=null,http_req_before_method,""))`                                                                                        |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sum`                       | `index=xdr_data | where action_file_size != null | stats sum(action_file_size) by _time`                                                                   | `dataset in (xdr_data) | filter action_file_size != null | comp sum(action_file_size) by _time`                                                                                                                                      |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `table`                     | `index = xdr_data | table _time, agent_hostname, agent_ip_addresses, _product`                                                                             | `dataset in (xdr_data) | fields _time, agent_hostname, agent_ip_addresses, _product`                                                                                                                                                 |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `tonumber`                  | `index=xdr_data | eval tonumber_test = tonumber("90210")`                                                                                                  | `dataset in (xdr_data) | alter tonumber_test = to_number("90210")`                                                                                                                                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `top`                       | The following Splunk functions can be translated to XQL:                                                                                                   | - `limit`                                                                                                                                                                                                                            |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `limit`                                                                                                                                                  | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `dataset in (xdr_data) | filter action_app_id_risk > 0 | top 20 action_app_id_risk top_count as count, top_percent as percent`                                                                                                     |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index = xdr_data | where action_app_id_risk > 0 | top limit=20 action_app_id_risk`                                                                      | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `countfield`                                                                                                                                                                                                                       |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `countfield`                                                                                                                                             | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `dataset in (xdr_data) |top 10 agent_hostname by _time top_count as count_agent_hostname, top_percent as percent`                                                                                                                  |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index = xdr_data | top countfield=count_agent_hostname agent_hostname by _time`                                                                         | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `showcount`                                                                                                                                                                                                                        |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `showcount`                                                                                                                                              | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `dataset in (xdr_data) | filter action_app_id_risk > 0 | top 3 action_app_id_risk top_count as count, top_percent as percent`                                                                                                      |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index = xdr_data | where action_app_id_risk > 0 | top 3 showcount=t action_app_id_risk`                                                                 | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `showperc`                                                                                                                                                                                                                         |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `showperc`                                                                                                                                               | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `dataset in (xdr_data) | filter action_app_id_risk > 0 | top 3 action_app_id_risk top_count as count, top_percent as percent`                                                                                                      |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index = xdr_data | where action_app_id_risk > 0 | top 3 showperc=t action_app_id_risk`                                                                  | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `percentfield`                                                                                                                                                                                                                     |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `percentfield`                                                                                                                                           | <!-- -->                                                                                                                                                                                                                             |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | <!-- -->                                                                                                                                                   | - `dataset in (xdr_data) | top 10 agent_hostname by _time top_count as count, top_percent as agent_hostname_percentage`                                                                                                              |
|                             |                                                                                                                                                            |                                                                                                                                                                                                                                      |
|                             | - `index = xdr_data | top percentfield=agent_hostname_percentage agent_hostname by _time`                                                                  |                                                                                                                                                                                                                                      |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `upper`                     | `index=xdr_data | eval field = upper("test")`                                                                                                              | `dataset in (xdr_data) | alter field = uppercase("test")`                                                                                                                                                                            |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `var`                       | `index=xdr_data | stats var (event_type) by _time`                                                                                                         | `dataset in (xdr_data) | comp var(event_type) by _time`                                                                                                                                                                              |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

How to translate a Splunk query to XQL syntax

1.  Select Investigation & Response \> Search \> Query Builder \> XQL.

2.  Toggle to **Translate to XQL**, where both a **SPL query** field and
    **XQL query** field are displayed.

3.  Add your Splunk query to the **SPL query** field.

4.  Click the arrow (![](media/rId2815.png){width="0.3020833333333333in"
    height="0.20833333333333334in"}).

- The **XQL query** field displays the equivalent Splunk query using the
  XQL syntax.

  You can now decide what to do with this query based on the
  instructions explained in [Create XQL
  query](#UUID5f5b967337c3cb75a413d47e8b461681).

##### Graph query results

To help you better understand your Cortex Query Language (XQL) query
results and share your insights with others, Cortex XSIAM enables you to
generate graphs and outputs of your query data directly from query
results page.

1.  Select Investigation & Response \> Search \> Query Builder \> XQL.

2.  Run an XQL query.

- Enter the following query:

      dataset = xdr_data 
      | fields action_total_upload, _time 
      | limit 10

  The query returns the `action_total_upload`, a number field, and
  `_time`, a string field, for up to 10 results.

3.  In the **Query Results** section, to graph the results either:

- Use Chart Editor
  Navigate to Query Results \> Chart Editor
  (![](media/rId2842.png){width="0.2604166666666667in"
  height="0.20833333333333334in"}) to manually build and view the graph
  using the selected graph parameters:

  - **Main**

    - **Graph Type**: Type of graphs and output options available:
      **Area**, **Bubble**, **Column**, **Funnel**, **Gauge**, **Line**,
      **Map**, **Pie**, **Scatter**, **Single Value**, or
      **Word Cloud**.

    <!-- -->

    - > **Note**

      > To display the result of as a time duration, choose the graph
      > type **Single Value** and enable **Show as Time**. You can then
      > select the **Time Unit** (millisecond, second, minute, or hour)
      > and the **Display format**.

    <!-- -->

    - **Subtype** and **Layout**: Depending on the selected type of
      graph, choose from the available display options.

    - **Header**: Title your graph.

    - **Show Callouts**: Display numeric values on the graph.

  - **Data**

    - **X-axis**: Select a field with a string value.

    - **Y-axis**: Select a field with a numeric value.

    - (Optional) **Series**: For an area, bubble, column, line, map, or
      scatter chart, you can specify a field (column) to group chart
      results based on y-axis values. This option is only displayed when
      one of the supported graph types are selected, and a single y-axis
      value is selected.

  - Depending on the selected type of graph, customize the **Color**,
    **Font**, and **Legend**.

  Use XQL query
  Enter the visualization parameters in the XQL query section.

  You can express any chart preferences in XQL. This is helpful when you
  want to save your chart preferences in a query and generate a chart
  every time that you run it. To define the parameters, either:

  - Define the following query:

  <!-- -->

  - dataset = xdr_data 
        | view graph type = column header = "Test 1" xaxis = _time yaxis = action_total_upload series = _vendor

  <!-- -->

  - Select **ADD TO QUERY** to insert your chart preferences into the
    query itself.

4.  (*Optional*) Create a custom widget.

- To easily track your query results, you can create custom widgets
  based on the query results. The custom widgets you create can be used
  in your custom dashboards and reports. For more information, see
  <urn:resource:component:1159521>.

  Select **Save to Widget Library** to pivot to the Widget Library and
  generate a custom widget based on the query results.

#### Query Builder templates

You can use the Query Builder templates to create effective queries
without using the Cortex Query Language (XQL).

From the Query Builder, you can select the following templates:

- **Basic**: Search by IP address, host name, user name, and domain.

- **Free text**: Search for a free text string.

- **Identity**: Search by user name and type.

- **Endpoint**: Search by host name, files, and processes.

- **Network IP**: Search by IP address and connection status.

- **Cloud**: Search by cloud provider and zone.

The templates are configured to run on specific datasets, but it\'s
possible to run them on all datasets. The templates run on the following
datasets by default:

- **Basic**, **Identity**, **Endpoint**, and **Network** templates:
  `xdr_data`

- **Cloud** template: `cloud_audit_logs`

The templates are set up with predefined filtering fields and fieldsets
that are specific to the template type. For example, a query built with
the **Endpoint** template includes fields from `fieldset.xdm_endpoint`.
You can specify values for the default fields and add any other required
fields to refine and adapt your search. The Query Builder templates
support any filtering fields from the Cortex Data Model (XDM) schema.

> **Tip**
>
> To get started with queries, you can run an empty template query with
> no values specified. The query results will include all of the fields
> in the template specific fieldset. Based on the query results, you can
> run subsequent queries to narrow down your search.

##### Get started with Query Builder templates

Before you start running queries with Query Builder templates, consider
the following information:

- **Learn about the templates:** Although the templates don't require
  XQL knowledge, they do require knowledge of operators and other
  factors. Understanding how the templates work will help you to build
  effective queries. For more information, see
  [/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5](/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5).

- **Look up field and alias descriptions:** The templates are based on
  the fields and aliases in the Cortex Data Model (XDM). If you want
  more information about a field or alias, see the [Cortex XSIAM Data
  Model Schema
  Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-Data-Model-Schema-Guide/Introduction).

- **Try out our examples:** To help you feel confident with Query
  Builder templates, start by following our step-by-step examples and
  tailor them for your environment. For more information, see [Query
  Builder template examples](#UUID916e794a9c9e407bd4864e77f4402a76).

##### Considerations for using Query Builder templates

The following sections provide information and considerations for using
Query Builder templates.

###### General considerations

The following general considerations apply to Query Builder templates:

- The templates run on the following datasets by default:

  - **Basic**, **Identity**, **Endpoint**, and **Network** templates:
    `xdr_data`

  - **Cloud** template: `cloud_audit_logs`

<!-- -->

- It is also possible to run the templates on all datasets.

<!-- -->

- The query uses an AND operator between the filtering fields.

- Separate multiple values with pipes and do not add spaces between the
  value and the pipe.

- Some of the filtering fields are aliases and therefore search all
  fields that are associated with the alias.

- Fields with dropdown options support ENUMs and free text values.

- In IP address fields, you can also specify subnets.

- The asterisk (`*`) wildcard is supported, except in subnet values.

- You cannot remove the predefined fields, but you can leave them blank.

- When filtering integer and float fields, you can only specify two
  operators from the four available options.

###### = (equal to) and != (not equal to) operators

Filtering fields support the `=` (equal to) and `!=` (not equal to)
operators, and you can specify both operators for the same field. The
following conditions apply to these operators:

- If you specify multiple values for a field with the `=` operator, the
  OR operator is applied. For example, `User Name = aaa|bbb` searches
  for instances of user name equal to aaa OR bbb.

- If you specify multiple values for a field with the `!=` operator, the
  AND operator is applied. For example, `User Name != aaa|bbb` searches
  for instances of user name not equal to aaa AND bbb.

- If you specify both operators (`=` and `!=`) for the same field, the
  AND operator is applied. For example,
  `COUNTRY = Empty values AND COUNTRY != USA`.

###### \>= (greater than and equal) and \<= (less than and equal) operators

Filtering fields support the `>=` (greater than and equal) and `<=`
(less than and equal) operators, and you can specify both operators for
the same field. The following conditions apply to these operators:

- Cortex XSIAM supports using these operators for integer and float
  fields.

- Empty values are not supported with these operators.

###### Include and exclude empty values

You can use the **Empty values** field to include or exclude fields with
empty values and strings. In the search results, some fields might
return empty values. This occurs if no data is mapped to a field. The
following conditions apply to the **Empty values** field:

- If you specify **=** and select **Empty values**, the query includes
  fields with empty values with an OR operator.

<!-- -->

- For example, `_vendor = aaa OR _vendor = Empty values` searches the
  `_vendor` field for any instances of aaa or empty values.

<!-- -->

- If you specify **!=** and select **Empty values**, the query excludes
  fields with empty values with an AND operator.

<!-- -->

- For example, `_vendor != aaa AND _vendor != Empty values` searches the
  `_vendor` field for values that are not equal to aaa AND do not
  contain empty values.

<!-- -->

- If you specify **!=** and select **Empty values** for an alias, you
  might not receive any results. The query searches all of the fields
  associated with the alias for non-empty values. If any of the
  associated fields contain empty values, no results are returned.

<!-- -->

- For example, `User Name != aaa AND User Name != Empty values` searches
  the User Name alias fields for values that are not equal to aaa AND
  empty values. If the query finds either aaa or empty values in any of
  the alias fields, no results are returned.

##### Create a query from a template

You can use the Query Builder templates to create effective queries
without using the Cortex Query Language (XQL).

Review the following topics:

- [/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834](/document/preview/918018#UUID-e34405b6-a092-2267-2b05-b2e6af734834)

- [Get started with Query Builder
  templates](#UUID6bf5ced752af891dac5a10a43eb93dc9)

- [/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5](/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5)

**How to create a query from a Query Builder template**

1.  Select Investigation & Response \> Search \> Query Builder.

2.  In the Query Builder, select the template that you want to use.

- If you want to use the Free Text Search template, see [Run a free text
  query](#UUID550352451d3f46199906fd9c62aa3d0b).

3.  (Optional) Change the **Run on** option (upper-right corner) that
    controls the datasets configured to run with the template. The
    templates are automatically configured to run on default datasets or
    you can choose to run them on all datasets. The templates run on the
    following datasets by default:

    - **Basic**, **Identity**, **Endpoint**, and **Network** templates:
      `xdr_data`

    - **Cloud** template: `cloud_audit_logs`

4.  Enter values for any of the predefined fields and specify whether to
    include **Empty values** in the query.

- Guidelines
  - The query uses an AND operator between the filtering fields.

  - Separate multiple values with pipes and do not add spaces between
    the value and the pipe.

  - Some of the filtering fields are aliases and therefore search all
    fields that are associated with the alias.

  - You can run an empty template with no values specified. The query
    results will show data from all of the fields in the template
    specific fieldset.

  For more information about using the filtering fields, operators, and
  including **Empty values**, see
  [/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5](/document/preview/922571#UUID-bbfb8b34-3bc0-8015-0244-26914b98f0d5).

5.  (Optional) Click **Add Field** and select the additional filtering
    fields or aliases to include in the query.\"

- > **Note**

  - > Field names and aliases are listed without their prefix, for
    > example **xdm.SOURCE.USER.USERNAME** is listed as
    > **SOURCE.USER.USERNAME** and **XDM_ALIAS.ipv4** is listed as
    > **ipv4**.

  - > Fields that are already included in the query template are shown
    > as grayed out.

  - > In the Identity and Network templates, `xdm.event.outcome` shows
    > as grayed out. In these templates, the **ACTION STATUS** and
    > **CONNECTION STATUS** fields are linked to the `xdm.event.outcome`
    > enum. Therefore, you can\'t duplicate this field in a query.

6.  Click **TIME** and select a time frame for the query.

7.  Click **Run** to start the query, or click **Schedule** to run the
    query at a specific time.

- You can also click **Continue in XQL** to open the XQL Query Builder
  showing the defined XQL fields. In XQL you have the flexibility to add
  additional stages and functions that are not available in the Query
  Builder templates.

8.  Review the **Results**.

- The search is limited to 1,000 results. In the **Fields** column, you
  can see all of the fields that were included in the query in the
  following order: (1) **\_time**, (2) the filtering fields that you
  defined, and (3) the fields from the template specific fieldset.

  > **Note**

  > This order might change if you include a filtering field that is
  > listed in the fieldset. In that case, the field is taken out of the
  > fieldset and ordered at the top of the list with the other filtering
  > fields.

  The query is also saved in the Query Center. In the Query Center, you
  can identify your query by filtering the **Created By** column and
  looking in the **Query Description** column. Queries created from a
  template are prefixed with the template name.

Example

- The following query searches for instances of IP 3.3.3.3 with a source
  host name equal to host1 or host2. IP is an alias field; therefore,
  the query searches all fields associated with the alias.

<!-- -->

- IP ADDRESS = 3.3.3.3, SOURCE.HOST.OS = host1|host2

<!-- -->

- The following query searches for the event outcome success with an
  event duration value that is not equal to null:

<!-- -->

- EVENT.OUTCOME = XDM_CONST.OUTCOME_SUCCESS, EVENT.DURATION != Empty values

###### What to do next

- To edit or rerun the query, click **Back to edit** to review the
  template, or **Continue in XQL** to review the XQL.

- Practice running queries with [Query Builder template
  examples](#UUID916e794a9c9e407bd4864e77f4402a76).

##### Run a free text query

You can use the **Free text** template to query your datasets for
free-text strings without building a Cortex Query Language (XQL) query.
The template queries all of the datasets that are stored in your tenant
and returns up to 1,000 results.

> **Note**
>
> Free-text search is also available in XQL queries. You can use the
> `search` stage to query free-text strings in specific datasets, or all
> of the datasets in your tenant.

**How to run a free text query**

1.  Select Investigation & Response \> Search \> Query Builder.

2.  Under **General Search**, select **Free text**.

3.  In the **Text Contains** field, type one or more strings. Separate
    multiple strings with pipes, which applies the OR operator.

4.  Click **TIME** and select a time frame for the query.

- > **Note**

  > Free text search is limited to the last 90 days of data. Specifying
  > a time frame outside of this limitation will cause the query to
  > fail.

5.  Click **Run** to start the query, or click **Schedule** to run the
    query at a specific time.

- Free text search searches the relevant columns in each dataset.
  Relevant columns are subject to a change and can vary between
  datasets.

  You can also click **Continue in XQL** to translate the query with the
  fields that you specified into XQL. In XQL you have the flexibility to
  add additional stages and functions that are not available in the
  Query Builder templates.

6.  Review the results.

- The searched string is highlighted in the results.

  In the **Fields** column, you can see all of the fields in which the
  string was discovered. Fields are listed in the following order: (1)
  `_time`, (2) `_dataset`, and (3) the fields in which the string was
  discovered, ordered by highest to lowest number of hits.

  In the `RAW_DATA` column, click **Show more** to see the specific row
  in the dataset in which the string was discovered.

###### What to do next

- To edit or rerun the query, click **Back to edit** to review the
  template in the Query Builder, or **Continue in XQL** to review the
  XQL.

- Practice running queries with [Query Builder template
  examples](#UUID916e794a9c9e407bd4864e77f4402a76).

##### Query Builder template examples

The following examples can help familiarize you with running queries.

###### Use the Identity template to search for information about a specific user

**Goal**: Search for information about users working on the system.

This example uses the **Identity** template, but you can apply it to any
of the templates. In the example, we run multiple queries that narrow
down our search results and find the required information we require.

####### Query 1: Search for information about all users

1.  Select Investigation & Response \> Search \> Query Builder.

2.  Select the **Identity** template.

3.  Specify **USER = \*** and do not select **Empty values**.

- This searches for all users, and excludes empty values or strings from
  the results. The `USER` field is an alias so all associated fields are
  also searched.

4.  Specify TIME \> Last 7D.

5.  Click **Run**.

In the **Results** page, scroll through the table to find a value or
string that you want to investigate further. If you are not receiving
results, you can broaden the **TIME** to **Last 30D**.

In this example, the results returned information about **USER66** in
the **XDM.SOURCE.USER.USERNAME** column. To refine the search for
information about this user, run another query.

####### Query 2: Search for information about a specific user

1.  Copy the term that you want to search, in this case **USER66**.

2.  Click **Back to edit**.

- The Identity template opens with the original search options.

3.  Click **Add field** and select **SOURCE.USER.USERNAME**.

4.  Specify **SOURCE.USER.USERNAME = USER66** and do not select
    **Empty values**.

5.  Click **Run**.

The **Results** page provides more information about **USER66**.

Look through the results for anything you would like to investigate
further. In this example, there is information about the operations
performed by this user in the **XDM.EVENT.OPERATION** column. We can
refine the search to see all **FILE_REMOVE** operations for **USER66**.

####### Query 3: Search for FILE_REMOVE operations for a specific user

1.  Click **Back to edit**.

2.  Click **Add field** and select **EVENT.OPERATION**.

3.  Specify **EVENT.OPERATION =** and select
    **XDM_CONST.OPERATION_TYPE_FILE_REMOVE** from the list.

4.  Click **Run**.

Review the **Results** page and continue to refine your search by using
this method.

###### Use the Network template to search for hosts triggering threat events in the United States

**Goal**: Search for information about source hosts in the United States
that caused threat events over the last 7 days.

####### Query 1: Search for network information in the United States

1.  Select Investigation & Response \> Search \> Query Builder.

2.  Select the **Network** template.

3.  Specify **COUNTRY = United States** and do not select
    **Empty values**.

- This searches for network activity in the United States, and excludes
  empty values or strings from the results.

4.  Specify TIME \> Last 7D.

5.  Click **Run**.

In the **Results** page, scroll through the table to find a value or
string for which you would like to find more information.

In this example, the results returned information about
**XDM.EVENT.TYPE = threat** for host **DC3ENX4FGC07** in the
**XDM.SOURCE.HOST.HOSTNAME** column. To refine the search, run another
query.

####### Query 2: Search for information about a specific host and event type

1.  Copy the term that you want to search, in this case
    **DC3ENX4FGC07**.

2.  Click **Back to edit**.

- The Network template opens with the original search options.

3.  Click **Add field** and select **EVENT.TYPE**.

4.  Specify **EVENT.TYPE = threat** and do not select **Empty values**.

5.  Click **Add field** and select **SOURCE.HOST.HOSTNAME**.

6.  Specify **SOURCE.HOST.HOSTNAME = DC3ENX4FGC07** and do not select
    **Empty values**.

7.  Click **Run**.

The **Results** page provides more information about
**EVENT.TYPE = threat** actions from host **DC3ENX4FGC07**.

To investigate further we could run another query, or in this case,
investigate the causality chain of the event. In the search results,
right-click and **Investigate Causality Chain**.

###### Use the Free text template to search for an IP address

**Goal**: Search for information about IP address 175.18.7.29 in the
last 24 hours.

1.  Select Investigation & Response \> Search \> Query Builder.

2.  Select the **Free text** template.

3.  Specify **Text Contains = 175.18.7.29**.

4.  Specify TIME \> Last 24H.

5.  Click **Run**.

In the **Results** page the searched string is highlighted. In
the **Fields** column, you can see all of the fields in which the string
was discovered. In the **RAW_DATA** column, click **Show more** to see
the specific row in the dataset in which the string was discovered.

If you want to deepen your search you can **Continue in XQL**, which
opens an XQL search with the fields you defined in the template. You can
add stages and functions to the XQL that narrow down your search.

#### Edit and run queries in Query Center

The **Query Center** displays information about all queries that were
run in the **Query Builder**. From the **Query Center** you can manage
your Cortex Query Language (XQL) and Graph Search queries by viewing
query results, running queries, adjusting queries, and scheduling when a
query runs. Right-click a query to see the available options, where some
of the options differ depending on the type of query you\'ve selected.
The pivot (right-click) options described below are some of the ones
that may require further explanation.

##### View the results of a query

You can view the original results of an XQL query when it was originally
run in the Query Builder and added to the Query Center.

1.  Select Investigation & Response \> Search \> Query Center.

2.  Identify the XQL query by looking in the **Query Name** and
    **Query Description** columns.

- The **Query Description** column displays the parameters that were
  defined for a query. If necessary, use the filter on the column to
  reduce the number of queries displayed.

  Queries that were created from a Query Builder template are prefixed
  with the template name.

3.  Right-click anywhere in the XQL query row and select
    **Show results**.

- You have the option to **Show results in new tab** or
  **Show results in same tab**.

4.  (*Optional*) **Export to file** to export the results to a
    tab-separated values (TSV) file.

5.  (*Optional*) Perform additional investigation on the issues.

- Right-click a value in the results table to see the options for
  further investigation.

##### Run a query

You can run a query for a Graph Search query.

1.  Select Investigation & Response \> Search \> Query Center.

2.  Identify the Graph Search query by looking in the **Query Name** and
    **Query Description** columns.

- The **Query Description** column displays the parameters that were
  defined for a query. If necessary, use the filter on the column to
  reduce the number of queries displayed.

3.  Right-click anywhere in the Graph Search query row and select
    **Run query**.

- You have the option to **Run in same tab** or **Show in new tab**.

4.  (*Optional*) The Graph Search results are displayed in a graph
    format by default. You can toggle to **Table** to view the results
    in a table format. In addition, you can always export the graph
    results using the icon at the top of the page to a PNG, SVG, or TSV
    file. Table results can only be exported to a TSV file.

5.  (*Optional*) Perform additional investigation on the graph or table
    results.

- On the graph results, you can either hover or select different nodes
  for further investigation. While in the table results, you can select
  any cell in the table for further investigation.

##### Modify a query

After you view the query results of an XQL query or run a Graph Search
query as explained in the tasks above, you can change your search
parameters to refine the search results or correct a search parameter.

- For queries created in XQL, type your changes in the XQL query field
  where the original query is listed and the results are displayed in
  the **Query Results** tab. After modifying the query, you can run,
  schedule, or save the query.

- For queries created with a Query Builder template, the defined
  parameters are shown at the top of the **Results** page. Select
  **Back to edit** to modify the query with the template format or
  **Continue in XQL** to open the query in XQL.

- For Graph Search queries, the graph results are displayed. Click
  anywhere in the Graph Search query interface, where your existing
  query is defined, to display the complete query, update your query,
  and rerun the search.

##### Schedule a query to run

You can schedule an XQL query to run on or before a specific date.
Cortex XSIAM creates a new query in the **Query Center**, and when the
query completes, it displays a notification in the notification bar.

**How to schedule a query**

1.  In the **Query Center**, right-click anywhere in the query and then
    select **Schedule**.

2.  Choose a schedule option and the date and time that the query should
    run:

    - **Run one time query on a specific date**

    - **Run query by date and time**: Schedule a recurring query.

3.  Click **OK** to schedule the query.

- Cortex XSIAM creates a new query and schedules it to run on or by the
  selected date and time.

4.  View the status of the scheduled query on the **Scheduled Queries**
    page.

- You can also make changes to the query, edit the frequency, view when
  the query will next run, or disable the query. For more information,
  see [Manage scheduled queries](#UUIDa6a1c386be83dee6adae90853bd56f0a).

##### Query Center reference information

The table below lists the common fields in the Query Center, where the
options differ for an XQL query versus a Graph Search query.

> **Note**
>
> Certain fields are exposed and hidden by default. An asterisk (\*) is
> beside every field that is exposed by default.

Query Center table

+-----------------------------------+-----------------------------------------------------+
| Field                             | Description                                         |
+===================================+=====================================================+
| **BQL**                           | Indicates whether the Cortex Query Language (XQL)   |
|                                   | query was created by the native search.             |
|                                   |                                                     |
|                                   | Native search has been deprecated; this field       |
|                                   | allows you to view data for XQL queries performed   |
|                                   | before deprecation.                                 |
+-----------------------------------+-----------------------------------------------------+
| **COMPUTE UNIT USAGE**            | For XQL queries, indicates the number of query      |
|                                   | units that were used to execute the API query and   |
|                                   | Cold Storage query.                                 |
+-----------------------------------+-----------------------------------------------------+
| **CREATED BY** \*                 | For XQL queries, indicates the user who created or  |
|                                   | scheduled the query. For Graph Search queries,      |
|                                   | indicates the user who created the query.           |
+-----------------------------------+-----------------------------------------------------+
| **DURATION (SEC)**                | Number of seconds it took to execute the XQL query. |
+-----------------------------------+-----------------------------------------------------+
| **EXECUTION ID**                  | Unique identifier of XQL and Graph Search queries   |
|                                   | in the tenant. The identifier ID generated for      |
|                                   | queries executed in Cortex XSIAM and XQL query API. |
+-----------------------------------+-----------------------------------------------------+
| **NUM OF RESULTS**\*              | Number of results returned by the query.            |
+-----------------------------------+-----------------------------------------------------+
| **PUBLIC API**                    | Whether the source executing the XQL query was an   |
|                                   | XQL query API.                                      |
+-----------------------------------+-----------------------------------------------------+
| **QUERY DESCRIPTION**\*           | Query parameters used to run the query.             |
+-----------------------------------+-----------------------------------------------------+
| **QUERY ID**                      | Unique identifier of the query.                     |
+-----------------------------------+-----------------------------------------------------+
| **QUERY NAME**\*                  | - For saved queries, the **Query Name** identifies  |
|                                   |   the query specified according to a randomly       |
|                                   |   generated number.                                 |
|                                   |                                                     |
|                                   |   - XQL queries use the format                      |
|                                   |     **XQL-QUERY-\<number\>**, such as               |
|                                   |     **XQL-QUERY-12**.                               |
|                                   |                                                     |
|                                   |   - Graph Search queries use the format             |
|                                   |     **Graph-Query-\<number\>**, such as             |
|                                   |     **Graph-Query-1247**.                           |
|                                   |                                                     |
|                                   | - For scheduled queries, the **Query Name**         |
|                                   |   identifies the auto-generated name of the parent  |
|                                   |   XQL query. Scheduled queries also display an icon |
|                                   |   to the left of the name to indicate that the XQL  |
|                                   |   query is recurring.                               |
|                                   |                                                     |
|                                   | ![](media/rId2874.png){width="2.7777777777777777in" |
|                                   | height="0.8194444444444444in"}                      |
+-----------------------------------+-----------------------------------------------------+
| **QUERY STATUS**\*                | Status of the query, where the options differ based |
|                                   | on the query type:                                  |
|                                   |                                                     |
|                                   | - XQL queries:                                      |
|                                   |                                                     |
|                                   |   - **Queued**: The query is queued and will run    |
|                                   |     when there is an available slot.                |
|                                   |                                                     |
|                                   |   - **Running**                                     |
|                                   |                                                     |
|                                   |   - **Failed**                                      |
|                                   |                                                     |
|                                   |   - **Partially completed**: The query was stopped  |
|                                   |     after exceeding the maximum number of permitted |
|                                   |     results. The default results for a Cortex Data  |
|                                   |     Model (XDM) query or an XQL dataset query is    |
|                                   |     limited to 1000, when  no limit is explicitly   |
|                                   |     stated in the query. This applies to basic      |
|                                   |     queries with no stages except the `fields`      |
|                                   |     stage. This default limit does not apply to     |
|                                   |     widgets, Correlation Rules, public APIs, saved  |
|                                   |     queries, or scheduled queries, where the limit  |
|                                   |     is a maximum of 1,000,000 results. Queries      |
|                                   |     based on legacy templates are limited to 10,000 |
|                                   |     results. To reduce the number of results        |
|                                   |     returned, you can adjust the query settings and |
|                                   |     rerun.                                          |
|                                   |                                                     |
|                                   |   - **Stopped**: The query was stopped by an        |
|                                   |     administrator.                                  |
|                                   |                                                     |
|                                   |   - **Completed**                                   |
|                                   |                                                     |
|                                   |   - **Deleted**: The query was pruned.              |
|                                   |                                                     |
|                                   | - Graph Search queries:                             |
|                                   |                                                     |
|                                   |   - **Failed**                                      |
|                                   |                                                     |
|                                   |   - **Completed**                                   |
+-----------------------------------+-----------------------------------------------------+
| **RESULTS SAVED**\*               | For XQL queries, you can choose whether to save the |
|                                   | query results, so the output of the field is either |
|                                   | **Yes** or **No**. Yet, for Graph Search queries,   |
|                                   | the results can\'t be saved and must be run each    |
|                                   | time again, so the field is always **No**.          |
+-----------------------------------+-----------------------------------------------------+
| **SIMULATED COMPUTE UNITS**       | Number of XQL query units that were used to execute |
|                                   | the Hot Storage query.                              |
+-----------------------------------+-----------------------------------------------------+
| **Source**                        | Source from which the query was run, for example    |
|                                   | Playbook, Report, or Investigation.                 |
+-----------------------------------+-----------------------------------------------------+
| **Source ID**                     | ID of the source from where the query was run.      |
+-----------------------------------+-----------------------------------------------------+
| **Source Name**                   | Name of the source from where the query was run.    |
+-----------------------------------+-----------------------------------------------------+
| **TIMESTAMP**\*                   | Date and time the query was created.                |
+-----------------------------------+-----------------------------------------------------+
| **XQL**                           | Indicates whether the XQL query was created by an   |
|                                   | XQL search.                                         |
+-----------------------------------+-----------------------------------------------------+

#### Manage scheduled queries

The **Scheduled Queries** page displays information about your scheduled
and recurring queries. From this page, you can edit scheduled query
parameters, view previous executions, disable, and remove scheduled
queries. Right-click a query to see the available options.

##### View executed queries

1.  Select Investigation & Response \> Search \> Scheduled Queries.

2.  Locate the scheduled query for which you want to view previous
    executions.

- If necessary, use the **Filter** to reduce the number of queries
  returned.

3.  Right-click anywhere in the query row, and select
    **Show executed queries**.

- Cortex XSIAM filters the queries on the **Query Center**.

##### Edit the query frequency

1.  Select Investigation & Response \> Search \> Scheduled Queries.

2.  Locate the scheduled query that you want to edit.

- If necessary, use the **Filter** to reduce the number of queries
  returned.

3.  Right-click anywhere in the query row and then select **Edit**.

4.  Adjust the schedule settings, and then click **OK**.

##### Scheduled Queries reference information

The table below ists the common fields in the **Scheduled Queries**
page.

> **Note**
>
> Certain fields are exposed and hidden by default. An asterisk (\*) is
> beside every field that is exposed by default.

Scheduled Queries table

+-----------------------------------+-----------------------------------------------------+
| Field                             | Description                                         |
+===================================+=====================================================+
| **BQL**                           | Whether the query was created by the native search. |
|                                   |                                                     |
|                                   | Native search has been deprecated, this field       |
|                                   | allows you to view data for queries performed       |
|                                   | before deprecation.                                 |
+-----------------------------------+-----------------------------------------------------+
| **CREATED BY**                    | User who created or scheduled the query.            |
+-----------------------------------+-----------------------------------------------------+
| **MITRE ATT&CK TACTIC**           | MITRE ATT&CK tactics tagged in the scheduled query. |
+-----------------------------------+-----------------------------------------------------+
| **MITRE ATT&CK TECHNIQUE**        | MITRE ATT&CK techniques tagged in the scheduled     |
|                                   | query.                                              |
+-----------------------------------+-----------------------------------------------------+
| **NEXT EXECUTION**                | - For queries that are scheduled to run at a        |
|                                   |   specific frequency, this displays the next        |
|                                   |   execution time.                                   |
|                                   |                                                     |
|                                   | <!-- -->                                            |
|                                   |                                                     |
|                                   | - For queries that were scheduled to run at a       |
|                                   |   specific time and date, this field will show      |
|                                   |   `None`.                                           |
+-----------------------------------+-----------------------------------------------------+
| **PUBLIC API**                    | Whether the source executing the query was an XQL   |
|                                   | query API.                                          |
+-----------------------------------+-----------------------------------------------------+
| **QUERY DESCRIPTION**             | Query parameters used to run the query.             |
+-----------------------------------+-----------------------------------------------------+
| **QUERY ID**                      | Unique identifier of the query.                     |
+-----------------------------------+-----------------------------------------------------+
| **QUERY NAME**                    | - For saved queries, the **Query Name** identifies  |
|                                   |   the query specified by the administrator.         |
|                                   |                                                     |
|                                   | - For scheduled queries, the **Query Name**         |
|                                   |   identifies the auto-generated name of the parent  |
|                                   |   query. Scheduled queries also display an icon to  |
|                                   |   the left of the name to indicate that the query   |
|                                   |   is recurring.                                     |
|                                   |                                                     |
|                                   | ![](media/rId2874.png){width="2.7777777777777777in" |
|                                   | height="0.8194444444444444in"}                      |
+-----------------------------------+-----------------------------------------------------+
| **SCHEDULE TIME**                 | Frequency or time at which the query was scheduled  |
|                                   | to run.                                             |
+-----------------------------------+-----------------------------------------------------+
| **XQL**                           | Whether the query was created by XQL search.        |
+-----------------------------------+-----------------------------------------------------+

#### Manage your personal query library

Cortex XSIAM provides as part of the Query Library a personal query
library for saving and managing your own queries. When creating a query
in XQL Search or managing your queries from the Query Center, you can
save queries to your personal library. You can also decide whether the
query is shared with others (on the same tenant) in their Query Library
or unshare it, so it is only visible to you. You can also view the
queries that are shared by others (on the same tenant) in your Query
Library.

The queries listed in your Query Library have different icons to help
you identify the different states of the queries:

- ![](media/rId2887.png){width="0.20833333333333334in"
  height="0.20833333333333334in"}Created by me and unshared.

- ![](media/rId2890.png){width="0.1762817147856518in"
  height="0.20833333333333334in"}Create by me and shared.

- ![](media/rId2893.png){width="0.18333333333333332in"
  height="0.20833333333333334in"}Created by someone else and shared.

The Query Library contains a powerful search mechanism that enables you
to search in any field related to the query, such as the query name,
description, creator, query text, and labels. In addition, adding a
label to your query enables you to search for these queries using these
labels in the Query Library.

**How to add a query to your personal query library**

1.  Save a query to your personal query library.

- You can do this in two ways:

  - **From the Query Builder**

    1.  Select Investigation & Response \> Search \> Query Builder \>
        XQL.

    2.  In the XQL query field, define the parameters of your query.

    3.  Select Save as \> Query to Library.

  - **From the Query Center**

    1.  Select Investigation & Response \> Search \> Query Center.

    2.  Locate the query that you want to save to your personal query
        library.

    3.  Right-click anywhere in the query row, and select
        **Save query to library**.

2.  Set these parameters.

    - **Query Name**: Specify a unique name for the query. Query names
      must be unique in both private and shared lists, which includes
      other people's queries.

    - **Query Description** (*Optional*): Specify a descriptive name for
      your query.

    - **Labels** (*Optional*): Specify a label that is associated with
      your query. You can select a label from the list of predefined
      labels or add your label and then select **Create Label**. Adding
      a label to your query enables you to search for queries using this
      label in the Query Library.

    - **Share with others**: You can either set the query to be private
      and only accessible by you (default) or move the toggle to
      **Share with others** the query, so that other users using the
      same tenant can access the query in their Query Library.

3.  Click **Save**.

- A notification appears confirming that the query was saved
  successfully to the library, and closes on its own after a few
  seconds.

  The query that you added is now listed as the first entry in the
  **Query Library**. The query editor is opened to the right of the
  query.

4.  Other available options.

- As needed, you can return to your queries in the **Query Library** to
  manage your queries. Here are the actions available to you.

  - Edit the name, description, labels, and parameters of your query by
    selecting the query from the **Query Library**, hovering over the
    line in the query editor that you want to edit, and selecting the
    edit icon to edit the text.

  - **Search query data and metadata**: Use the Query Library's powerful
    search mechanism that enables you to search in any field related to
    the query, such as the query name, description, creator, query text,
    and label. The **Search query data and metadata** field is available
    at the top of your list of queries in the **Query Library**.

  - **Show**: Filter the list of queries from the **Show** menu. You can
    filter by the **Palo Alto Networks** queries provided with Cortex
    XSIAM , filter by the queries **Created by Me**, or filter by the
    queries **Created by Others**. To view the entire list,
    **Select all** (default).

  - **Save as new**: Duplicate the query and save it as a new query.
    This action is available from the query menu by selecting the 3
    vertical dots.

  - **Share with others**: If your query is currently unshared, you can
    share with other users on the same tenant your query, which will be
    available in their Query Library. This action is only available from
    the query menu by selecting the 3 vertical dots when your query is
    unshared.

  - **Unshare**: If your query is currently shared with other users, you
    can **Unshare** the query and remove it from their Query Library.
    This action is only available from the query menu by selecting the 3
    vertical dots when your query is shared with others. You can only
    **Unshare** a query that you created. If another user created the
    query, this option is disabled in the query menu.

  - **Delete** the query. You can only delete queries that you created.
    If another user created the query, this option is disabled in the
    query menu when selecting the 3 vertical dots.

#### Legacy Query Builder

> **Note**
>
> We recommend using the Query Builder in **New mode** to take advantage
> of the Query Builder templates and the ability to search the full
> Cortex Data Model (XDM).
>
> In **Legacy mode**, the Query Builder searches predefined datasets
> only. To search the full XDM, switch to New mode or select XQL Search.

The **Legacy Query Builder** provides queries for the following types of
entities:

- **Process**: Search on process execution and injection by process
  name, hash, path, command line arguments, and more. See [Create
  process query](#UUID8f12835a780c89b8549e7e3760901f1c).

- **File**: Search on file creation and modification activity by file
  name and path. See [Create file
  query](#UUIDd6b444714083281aef441049d18a3b4a).

- **Network**: Search network activity by IP address, port, host name,
  protocol, and more. See [Create network
  query](#UUIDe226ac9a89a002def25ecf8696798a67).

- **Image Load**: Search on module load into process events by module
  IDs and more. See [Create image load
  query](#UUIDede3423c719908f416d95ccfcacd1ce9).

- **Registry**: Search on registry creation and modification activity by
  key, key value, path, and data. See [Create registry
  query](#UUID5e4463ac13f0cc615f8358540f70811c).

- **Event Log**: Search Windows event logs and Linux system
  authentication logs by username, log event ID (Windows only), log
  level, and message. See [Create event log
  query](#UUIDead70f11e1d66a6842584f732ccd000c).

- **Network Connections**: Search security event logs by firewall logs,
  endpoint raw data over your network. See [Create network connections
  query](#UUID220f668affbca82acce73f83317eb797).

- **Authentications**: Search on authentication events by identity,
  target outcome, and more. See [Create authentication
  query](#UUID762652ea2555b6ad9dd86c53ae56a015).

- **All Actions**: Search across all network, registry, file, and
  process activity by endpoint or process. See [Query across all
  entities](#UUIDaadbc5bf8d97ab878c30eb0a64e5a873).

The **Query Builder** also provides flexibility for both on-demand query
generation and scheduled queries.

##### Create authentication query

From the Query Builder, you can investigate authentication activity
across all ingested authentication logs and data.

Some examples of authentication queries you can run include:

- Authentication logs by severity

- Authentication logs by the event message

- Authentication logs for a specific source IP address

**How to build an authentication query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **AUTHENTICATION**.

3.  Enter the search criteria for the authentication query.

- By default, Cortex XSIAM will return the activity that matches all the
  criteria you specify. To exclude a value, toggle the `=` option to
  `=!`.

4.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or Run to run the query immediately and view the results
  in the Query Center.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

5.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create event log query

From the **Query Builder** you can search Windows and Linux event log
attributes and investigate event logs across endpoints with a Cortex XDR
agent installed.

Some examples of event log queries you can run include:

- Critical level messages on specific endpoints.

- Message descriptions with specific keywords on specific endpoints.

**How to build an event log query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **EVENT LOG**.

3.  Enter the search criteria for your Windows or Linux event log query.

- Define any event attributes for which you want to search. By default,
  Cortex XDR will return the events that match the attribute you
  specify. To exclude an attribute value, toggle the `=` option to `=!`.
  Attributes are:

  - **PROVIDER NAME**: The provider of the event log.

  - **USERNAME**: The username associated with the event.

  - **EVENT ID**: The unique ID of the event.

  - **LEVEL**: The event severity level.

  - **MESSAGE**: The description of the event.

  To specify an additional exception (match this value except), click
  the **+** to the right of the value and specify the exception value.

4.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Specify one or more of the following attributes: Use a pipe (**\|**)
  to separate multiple values.

  Use an asterisk (**\***) to match any string of characters.

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector.

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

5.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

6.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the
  page, and a notification is sent when the query completes. You can
  also **Cancel** the query or run a new query, where you have the
  option to **Run only new query (cancel previous)** or
  **Run both queries**.

7.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create file query

From the **Query Builder** you can investigate connections between file
activity and endpoints. The Query Builder searches your logs and
endpoint data for the file activity that you specify. To search for
files on endpoints instead of file-related activity, build an XQL query.
For more information, see [How to build XQL
queries](#UUID125805d7e53750e71a87cb4c4140fa73).

Some examples of file queries you can run include:

- Files modified on specific endpoints.

- Files related to process activity that exist on specific endpoints.

**How to build a file query**

1.  From Cortex XSIAM, select Investigation & Response \> Search \>
    Query Builder.

2.  Select **FILE**.

3.  Enter the search criteria for the file events query.

    - File activity: Select the type or types of file activity you want
      to search: **All**, **Create**, **Read**, **Rename**, **Delete**,
      or **Write**.

    - File attributes: Define any additional process attributes for
      which you want to search. Use a pipe (`|`) to separate multiple
      values (for example `notepad.exe|chrome.exe`). By default, Cortex
      XSIAM will return the events that match the attribute you specify.
      To exclude an attribute value, toggle the `=` option to `=!`.
      Attributes are:

      - **NAME**: File name.

      - **PATH**: Path of the file.

      - **PREVIOUS NAME**: Previous name of a file.

      - **PREVIOUS PATH**: Previous path of the file.

      - **MD5**: MD5 hash value of the file.

      - **SHA256**: SHA256 hash value of the file.

      - **ACTION_DISK_DRIVER_NAME**: The driver where the file was
        created.

      - **FILE_SYSTEM_TYPE**: Operating system type where the file was
        run.

      - **ACTION_IS_VFS**: Denotes if the file is on a virtual file
        system on the disk. This is relevant only for files that are
        written to disk.

      - **DEVICE TYPE**: Type of device used to run the file: Unknown,
        Fixed, Removable Media, CD-ROM.

      - **DEVICE SERIAL NUMBER**: Serial number of the device type used
        to run the file.

    <!-- -->

    - To specify an additional exception (match this value except),
      click the **+** to the right of the value and specify the
      exception value.

4.  (*Optional*) Limit the scope to a specific acting process:

- Select **+PROCESS** and specify one or more of the following
  attributes for the acting (parent) process.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  - **NAME**: Name of the parent process.

  - **PATH**: Path to the parent process.

  - **CMD**: Command-line used to initiate the process, including any
    arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the process.

  - **SHA256**: SHA256 hash value of the process.

  - **USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signature
    Unavailable, Signed, Invalid Signature, Unsigned, Revoked, Signature
    Fail.

  - **SIGNER**: Entity that signed the certificate of the parent
    process.

  - **PID**: Process ID of the parent process.

  - **Run search for process, Causality, and OS actors**---The causality
    actor---also referred to as the causality group owner (CGO)---is the
    parent process in the execution chain that the Cortex XDR agent
    identified as being responsible for initiating the process tree. The
    OS actor is the parent process that creates an OS process on behalf
    of a different indicator. By default, this option is enabled to
    apply the same search criteria to initiating processes. To configure
    different attributes for the parent or initiate the process, clear
    this option.

5.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Select **+Host** and specify one or more of the following attributes:

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  <!-- -->

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector.

  <!-- -->

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create image load query

From the Query Builder, you can investigate connections between image
load activity, acting processes, and endpoints.

Some examples of image load queries you can run include:

- Module load into process events by module path or hash.

**How to build an image load query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **IMAGE LOAD**.

3.  Enter the search criteria for the image load activity query.

    - Type of image activity: **All**, **Image Load**, or
      **Change Page Protection**.

    - Identifying information about the image module: Full
      **Module Path**, **Module MD5**, or **Module SHA256**.

- By default, Cortex XSIAM will return the activity that matches all the
  criteria you specify. To exclude a value, toggle the `=` option to
  `=!`.

4.  (*Optional*) To limit the scope to a specific source, click the
    **+** to the right of the value and specify the exception value.

- Specify one or more attributes for the source.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  - **NAME**: Name of the parent process.

  - **PATH**: Path to the parent process.

  - **CMD**: Command-line used to initiate the process, including any
    arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the process.

  - **SHA256**: SHA256 hash value of the process.

  - **USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signature
    Unavailable, Signed, Invalid Signature, Unsigned, Revoked, Signature
    Fail.

  - **SIGNER**: Entity that signed the certificate of the parent
    process.

  - **PID**: Process ID of the parent process.

  **Run search for both the process and the Causality actor**: The
  causality actor---also referred to as the causality group owner
  (CGO)---is the parent process in the execution chain that the app
  identified as being responsible for initiating the process tree.
  Select this option if you want to apply the same search criteria to
  the causality actor. If you clear this option, you can then configure
  different attributes for the causality actor.

5.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Specify one or more of the following attributes: Use a pipe (**\|**)
  to separate multiple values.

  Use an asterisk (**\***) to match any string of characters.

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  <!-- -->

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector.

  <!-- -->

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create network connections query

From the Query Builder, you can investigate network events stitched
across endpoints and the Palo Alto Networks Next-Generation Firewall
logs.

Some examples of a network query you can run include:

- Source and destination of a process.

- Network connections that included a specific App ID

- Processes that created network connections.

- Network connections between specific endpoints.

**How to build a network connection query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **NETWORK CONNECTIONS**.

3.  Enter the search criteria for the network events query.

    - Network attributes: Define any additional process attributes for
      which you want to search. Use a pipe (`|`) to separate multiple
      values (for example `80|8080`). By default, Cortex XSIAM will
      return the events that match the attribute you specify. To exclude
      an attribute value, toggle the `=` option to `=!`. Options are:

      - **APP ID**: App ID of the network.

      - **PROTOCOL**: Network transport protocol over which the traffic
        was sent.

      - **SESSION STATUS**

      - **FW DEVICE NAME**: Firewall device name.

      - **FW RULE**: Firewall rule.

      - **FW SERIAL ID**: Firewall serial ID.

      - **PRODUCT**

      - **VENDOR**

    <!-- -->

    - To specify an additional exception (match this value except),
      click the **+** to the right of the value and specify the
      exception value.

4.  (*Optional*) To limit the scope to a specific source, click the
    **+** to the right of the value and specify the exception value.

- Specify one or more attributes for the source.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  - **HOST NAME**: Name of the source.

  - **HOST IP**: IP address of the source.

  - **HOST OS**: Operating system of the source.

  - **PROCESS NAME**: Name of the process.

  - **PROCESS PATH**: Path to the process.

  - **CMD**: Command-line used to initiate the process, including any
    arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the process.

  - **SHA256**: SHA256 hash value of the process.

  - **PROCESS USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signature
    Unavailable, Signed, Invalid Signature, Unsigned, Revoked, Signature
    Fail.

  - **PID**: Process ID of the parent process.

  - **IP**: IP address of the process.

  - **PORT**: Port number of the process.

  - **USER ID**: ID of the user who executed the process.

  - **Run search for both the process and the Causality actor**: The
    causality actor---also referred to as the causality group owner
    (CGO)---is the parent process in the execution chain that the app
    identified as being responsible for initiating the process tree.
    Select this option if you want to apply the same search criteria to
    the causality actor. If you clear this option, you can then
    configure different attributes for the causality actor.

5.  (*Optional*) Limit the scope to a destination.

- Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  Specify one or more of the following attributes:

  - **REMOTE IP**: IP address of the destination.

  - **COUNTRY**: Country of the destination.

  - Destination **TARGET HOST**,**NAME**, **PORT**, **HOST NAME**,
    **PROCESS USER NAME**, **HOST IP**, **CMD**, **HOST OS**, **MD5**,
    **PROCESS PATH**, **USER ID**, **SHA256**, **SIGNATURE**, or **PID**

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create network query

From the Query Builder, you can investigate connections between network
activity, acting processes, and endpoints.

Some examples of a network query you can run include:

- Network connections to or from a specific IP address and port number.

- Processes that created network connections.

- Network connections between specific endpoints.

**How to build a network query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **NETWORK**.

3.  Enter the search criteria for the network events query.

    - Network traffic type: Select the type or types of network traffic
      issues you want to search: **Incoming**, **Outgoing**, or
      **Failed**.

    - Network attributes: Define any additional process attributes for
      which you want to search. Use a pipe (`|`) to separate multiple
      values (for example `80|8080`). By default, Cortex XSIAM will
      return the events that match the attribute you specify. To exclude
      an attribute value, toggle the `=` option to `=!`. Options are:

      - **REMOTE COUNTRY**: Country from which the remote IP address
        originated.

      - **REMOTE IP**: Remote IP address related to the communication.

      <!-- -->

      - > **Note**

        > When you run the query, depending on the outcome of the
        > results, the value specified in this field might be displayed
        > in the `dst_ip` field in the query results. This occurs if an
        > RDP event is recorded whereby a user connected from the source
        > IP to the destination IP.

      <!-- -->

      - **REMOTE PORT**: Remote port used to make the connection.

      - **LOCAL IP**: Local IP address related to the communication.
        Matches can return additional data if a machine has more than
        one NIC.

      - **LOCAL PORT**: Local port used to make the connection.

      - **PROTOCOL**: Network transport protocol over which the traffic
        was sent.

    <!-- -->

    - To specify an additional exception (match this value except),
      click the **+** to the right of the value and specify the
      exception value.

4.  (*Optional*) To limit the scope to a specific source, click the
    **+** to the right of the value and specify the exception value.

- Specify one or more attributes for the source.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  - **NAME**: Name of the parent process.

  - **PATH**: Path to the parent process.

  - **CMD**: Command-line used to initiate the process, including any
    arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the process.

  - **SHA256**: SHA256 hash value of the process.

  - **USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signature
    Unavailable, Signed, Invalid Signature, Unsigned, Revoked, Signature
    Fail.

  - **SIGNER**: Entity that signed the certificate of the parent
    process.

  - **PID**: Process ID of the parent process.

  - **Run search for process, Causality, and OS actors**: The causality
    actor---also referred to as the causality group owner (CGO)---is the
    parent process in the execution chain that the Cortex XDR agent
    identified as being responsible for initiating the process tree. The
    OS actor is the parent process that creates an OS process on behalf
    of a different indicator. By default, this option is enabled to
    apply the same search criteria to initiating processes. To configure
    different attributes for the parent or initiate the process, clear
    this option.

5.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Specify one or more of the following attributes: Use a pipe (**\|**)
  to separate multiple values.

  Use an asterisk (**\***) to match any string of characters.

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector.

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create process query

From the **Query Builder** you can investigate connections between
processes, child processes, and endpoints.

For example, you can create a process query to search for processes
executed on a specific endpoint.

**How to build a process query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **PROCESS**.

3.  Enter the search criteria for the process query.

    - Process action: Select the type of process action you want to
      search: On process **Execution** or **Injection** into another
      process.

    - Process attributes---Define any additional process attributes for
      which you want to search.

    <!-- -->

    - Use a pipe (`|`) to separate multiple values. Use an asterisk
      (`*`) to match any string of characters.

      By default, Cortex XSIAM will return results that match the
      attribute you specify. To exclude an attribute value, toggle the
      operator from `=` to `!=`. Attributes are:

      - **NAME**: Name of the process. For example, `notepad.exe`.

      - **PATH**: Path to the process. For example,
        `C:\windows\system32\notepad.exe`.

      - **CMD**: Command-line used to initiate the process including any
        arguments, up to 128 characters.

      - **MD5**: MD5 hash value of the process.

      - **SHA256**: SHA256 hash value of the process.

      - **USER NAME**: User who executed the process.

      - **SIGNATURE**: Signing status of the process: Signature
        Unavailable, Signed, Invalid Signature, Unsigned, Revoked,
        Signature Fail.

      - **SIGNER**: Signer of the process.

      - **PID**: Process ID.

      - **PROCESS_FILE_INFO**: Metadata of the process file, including
        file property details, file entropy, company name, encryption
        status, and version number.

      - **PROCESS_SCHEDULED_TASK_NAME**: Name of the task scheduled by
        the process to run in the Task Scheduler.

      - **PROCESS_TOKEN_INFORMATION**: Bitwise token of the process
        privileges.

      - **DEVICE TYPE**: Type of device used to run the process:
        Unknown, Fixed, Removable Media, CD-ROM.

      - **DEVICE SERIAL NUMBER**: Serial number of the device type used
        to run the process.

      To specify an additional exception (match this value except),
      click the **+** to the right of the value and specify the
      exception value.

4.  (*Optional*) Limit the scope to a specific acting process:

- Select **+PROCESS** and specify one or more of the following
  attributes for the acting (parent) process.

  - **NAME**: Name of the parent process.

  - **PATH**: Path to the parent process.

  - **CMD**: Command-line used to initiate the parent process including
    any arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the parent process.

  - **SHA256**: SHA256 hash value of the process.

  - **USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signed,
    Unsigned, N/A, Invalid Signature, Weak Hash

  - **SIGNER**: Entity that signed the certificate of the parent
    process.

  - **PID**: Process ID of the parent process.

  - **Run search on process, Causality and OS actors**: The causality
    actor---also referred to as the causality group owner (CGO)---is the
    parent process in the execution chain that the Cortex XDR agent
    identified as being responsible for initiating the process tree. The
    OS actor is the parent process that creates an OS process on behalf
    of a different initiator. By default, this option is enabled to
    apply the same search criteria to initiating processes. To configure
    different attributes for the parent or initiate a process,

5.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Select **+HOST** and specify one or more of the following attributes:

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  <!-- -->

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector. For more information about the data collector applet,
    [Activate Pathfinder](#UUIDedfbabf66d30717d0d0ef54801b8cf35).

  <!-- -->

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Create registry query

From the Query Builder you can investigate connections between registry
activity, processes, and endpoints.

Some examples of a registry query you can run include:

- Modified registry keys on specific endpoints.

- Registry keys related to process activity that exist on specific
  endpoints.

**How to build a registry query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **REGISTRY**.

3.  Enter the search criteria for the registry events query.

    - Registry action: Select the type or types of registry actions you
      want to search: **Key Create**, **Key Delete**, **Key Rename**,
      **Value Set**, or **Value Delete**.

    - Registry attributes: Define any additional registry attributes for
      which you want to search. By default, Cortex XSIAM will return the
      events that match the attribute you specify. To exclude an
      attribute value, toggle the `=` option to `=!`. Attributes are:

      - **KEY NAME**: Registry key name.

      <!-- -->

      - > **Important**

        > Ensure the **KEY NAME** is entered as a real registry key
        > name, and not as a symbolic link. Otherwise, the query will
        > not retrieve results.

        > Instead of `HKEY_LOCAL_MACHINE\System\CurrentControlSet`,
        > which is a symbolic link, use
        > `KEY_LOCAL_MACHINE\System\ControlSet001`.

        > Instead of `HKEY_CURRENT_USER`, use `HKEY_USERS\<SID>`, where
        > SID is either a SID of the current user or an asterisk (`*`)
        > to represent any SID.

      <!-- -->

      - **DATA**: Registry key data value.

      - **KEY PREVIOUS NAME**: Name of the registry key before
        modification.

      - **VALUE NAME**: Registry value name.

    <!-- -->

    - To specify an additional exception (match this value except),
      click the **+** to the right of the value and specify the
      exception value.

4.  (*Optional*) To limit the scope to a specific source, click the
    **+** to the right of the value and specify the exception value.

- Specify one or more attributes for the source.

  Use a pipe (**\|**) to separate multiple values. Use an asterisk
  (**\***) to match any string of characters.

  - **NAME**: Name of the parent process.

  - **PATH**: Path to the parent process.

  - **CMD**: Command-line used to initiate the process including any
    arguments, up to 128 characters.

  - **MD5**: MD5 hash value of the process.

  - **SHA256**: SHA256 hash value of the process.

  - **USER NAME**: User who executed the process.

  - **SIGNATURE**: Signing status of the parent process: Signature
    Unavailable, Signed, Invalid Signature, Unsigned, Revoked, Signature
    Fail.

  - **SIGNER**: Entity that signed the certificate of the parent
    process.

  - **PID**: Process ID of the parent process.

  - **Run search for process, Causality, and OS actors**: The causality
    actor---also referred to as the causality group owner (CGO)---is the
    parent process in the execution chain that the Cortex XDR agent
    identified as being responsible for initiating the process tree. The
    OS actor is the parent process that creates an OS process on behalf
    of a different indicator. By default, this option is enabled to
    apply the same search criteria to initiating processes. To configure
    different attributes for the parent or initiate the process, clear
    this option.

5.  (*Optional*) Limit the scope to an endpoint or endpoint attributes:

- Specify one or more of the following attributes: Use a pipe (**\|**)
  to separate multiple values.

  Use an asterisk (**\***) to match any string of characters.

  - **HOST**: **HOST NAME**, **HOST IP** address, **HOST OS**,
    **HOST MAC ADDRESS**, or **INSTALLATION TYPE**.

  - **INSTALLATION TYPE** can be either Cortex XDR agent or Data
    Collector.

  - **PROCESS**: **NAME**, **PATH**, **CMD**, **MD5**, **SHA256**,
    **USER NAME**, **SIGNATURE**, or **PID**.

6.  Specify the time period for which you want to search for events.

- Options are **Last 24H** (hours), **Last 7D** (days), **Last 1M**
  (month), or select a **Custom** time period.

7.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or **Run** to run the query immediately and view the
  results in the **Query Center**.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

8.  When you are ready, view the results of the query. For more
    information, see [Review XQL query
    results](#UUID5d102247d2868bf6813913bc96b33623).

##### Query across all entities

From the **Query Builder** you can perform a simple search for hosts and
processes across all file events, network events, registry events,
process events, event logs for Windows, and system authentication logs
for Linux.

Some examples of queries you can run across all entities include:

- All activities on a host

- All activities initiated by a process on a host

**How to build a query**

1.  From Cortex XSIAM , select Investigation & Response \> Search \>
    Query Builder.

2.  Select **ALL ACTIONS**.

3.  (Optional) Limit the scope to a specific acting process:

- Select Add Process to your search, and specify one or more of the
  following attributes for the acting (parent) process. Use a pipe (\|)
  to separate multiple values. Use an asterisk (\*) to match any string
  of characters.

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  NAME                                Name of the parent process.

  PATH                                Path to the parent process.

  CMD                                 Command line used to initiate the
                                      parent process including any
                                      arguments, up to 128 characters.

  MD5                                 MD5 hash value of the parent
                                      process.

  SHA256                              SHA256 hash value of the process.

  USER NAME                           User who executed the process.

  SIGNATURE                           Signing status of the parent
                                      process: Signed, Unsigned, N/A,
                                      Invalid Signature, Weak Hash.

  SIGNER                              Entity that signed the certificate
                                      of the parent process.

  PID                                 Process ID of the parent process.

  Run search on process, Causality    The causality actor, also referred
  and OS actors                       to as the causality group owner
                                      (CGO), is the parent process in the
                                      execution chain that the agent
                                      identified as being responsible for
                                      initiating the process tree. The OS
                                      actor is the parent process that
                                      creates an OS process on behalf of
                                      a different initiator. By default,
                                      this option is enabled to apply the
                                      same search criteria to initiating
                                      processes. To configure different
                                      attributes for the parent or
                                      initiating process, clear this
                                      option.
  -----------------------------------------------------------------------

4.  (Optional) Limit the scope to an endpoint or endpoint attributes:

- Select Add Host to your search and specify one or more of the
  following attributes:

  - HOST: HOST NAME, HOST IP address, HOST OS, HOST ADDRESS, or
    INSTALLATION TYPE.

  - INSTALLATION TYPE can be either an agent, or data collector.

  - PROCESS: NAME , PATH , CMD , MD5 , SHA256 , USER NAME , SIGNATURE,
    or PID.

  <!-- -->

  - Use a pipe (\|) to separate multiple values. Use an asterisk (\*) to
    match any string of characters.

5.  Specify the time period for which you want to search for events.

- Options are Last 24H (hours), Last7D (days), Last1M (month), or select
  a Custom time period.

6.  Choose when to run the query.

- Select the calendar icon to schedule a query to run on or before a
  specific date or Run the query immediately and view the results in the
  Query Center.

  While the query is running, you can always navigate away from the page
  and a notification is sent when the query completes. You can also
  **Cancel** the query or run a new query, where you have the option to
  **Run only new query (cancel previous)** or **Run both queries**.

7.  When ready, view the results in a query.

### Stages

Stages perform certain operations in evaluating queries. For example,
the `dataset` stage specifies a dataset to run the query. Commonly used
stages include `dataset`, `fields`, `filters`, `join`, and `sort`. The
stages supported in Cortex Query Language are detailed below.

#### alter

Review the following topic:

- [Understanding string manipulation in
  XQL](#UUID30a4eee2b0dcd48ca66d58d24fd98b65)

##### Syntax

    alter <field1> = <function value1> [, <field2> = <function value2>, ...]

##### Description

The `alter` stage is used to change the values of an existing field
(column) or to create a new field (column) based on constant values or
existing fields (columns). The `alter` stage does this by assigning a
value to a field name based on the returned value of the specified
function. The field does not have to be known to the dataset or preset
schema that you are querying. Further, you can overwrite the current
value for a known field using this stage.

After defining a field using the `alter` stage, you can apply other
stages, such as filtering, to the new field or field value.

##### Examples

Given three username fields, use the
[coalesce](#UUIDd1ab43ad8806776edd0c44ebb52fa962) function to return a
username value in the `default_username` field, making sure to never
have a `default_username` that is `root`.

    dataset = xdr_data 
    | fields actor_primary_username, 
             os_actor_primary_username, 
             causality_actor_primary_username 
    | alter default_username = coalesce(actor_primary_username, 
                                        os_actor_primary_username, 
                                        causality_actor_primary_username)
    | filter default_username != "root"

#### arrayexpand

##### Syntax

    arrayexpand <array_field> [limit <limit number>]

##### Description

The `arrayexpand` stage expands the values of a mulit-value array field
into separate events and creates one record in the result set for each
item in the array, up to a `<limit number>` of records.

##### Example

Suppose you have a dataset with a single row like this:

  -------------------------------------------------------------------------
  uid                     username                array_values
  ----------------------- ----------------------- -------------------------
  123456                  ajohnson                \[1,2,3,4,5,6,7,8,9,0\]

  -------------------------------------------------------------------------

Then if you run an `arrayexpand` stage using the `array_values` field,
with a limit of 3, the result set includes the following records:

    dataset=my_dataset 
    | arrayexpand array_values limit 3

  -----------------------------------------------------------------------
  uid                     username                array_values
  ----------------------- ----------------------- -----------------------
  123456                  ajohnson                2

  123456                  ajohnson                1

  123456                  ajohnson                3
  -----------------------------------------------------------------------

> **Note**
>
> The result records created by `arrayexpand` are in no particular
> order. However, you can use the
> [sort](#UUIDb856a4139d2cf09ffea224fbf408c975) stage to sort the
> results:

    dataset=my_dataset 
    | arrayexpand array_values 
    | sort asc array_values

#### bin

##### Syntax

- **Quantity**

<!-- -->

- bin <field> bins = <number>

<!-- -->

- **Time Span**

<!-- -->

- bin <field> span = <time> [timeshift = <epoch time> [timezone = "<time zone>"]]

##### Description

The `bin` stage enables you to group events by quantity or time span.
The most common use case is for timecharts.

You can add the `bin` stage to your queries using two different formats
depending on whether you are grouping events by quantity or time span.
Currently, the `bin` stage is only supported using the equal sign (=)
operator in your queries without any boolean operators (`and`, `or`).

When you group events of a particular field by quantity, the `bin` stage
is used with `bins` to define how to divide the events.

When you group events of a particular field by time, the `bin` stage is
used with `span = <time>`, where `<time>` is a combination of a number
and time suffix. Set one time suffix from the list of available options
listed in the table below. In addition, you can define a particular
start time for grouping the events in your query according to the Unix
epoch time by setting
`timeshift = <epoch time> timezone = "<time zone>"`, which are both
optional. You can configure the `<time zone>` offset using an hours
offset, such as `“+08:00”`, or using a time zone name from the [List of
Supported Time
Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
such as `"America/Chicago"`. The query still runs without defining the
epoch time or time zone. If no
`timeshift = <epoch time> timezone = "<time zone>"` is set, the query
runs according to last time set in the log.

> **Note**
>
> When you group events by quantity, the `<field>` in the `bin` stage
> must be a number, and when you group by time, the `<field>` must be a
> date type. Otherwise, your query will fail.

##### Time Suffixes

  -----------------------------------------------------------------------
  Time Suffix                         Description
  ----------------------------------- -----------------------------------
  MS                                  milliseconds

  S                                   seconds

  M                                   minutes

  H                                   hours

  D                                   days

  W                                   weeks

  MO                                  months

  Y                                   years
  -----------------------------------------------------------------------

> **Note**
>
> The time suffix is not case sensitive.

##### Examples

- **Quantity Example**

<!-- -->

- Return a maximum of 1,000 `xdr_data` records with the events of the
  `action_total_upload` field grouped by 50MB. Records with the
  `action_total_upload` value set to 0 or null are not included in the
  results.

      dataset = xdr_data
      | filter action_total_upload != 0 and action_total_upload != null 
      | bin action_total_upload bins = 50 
      | limit 1000

<!-- -->

- **Time Span Examples**

  - With a time zone configured using an hours offset:

  <!-- -->

  - Return a maximum of 1,000 `xdr_data` records with the events of the
    `_time` field grouped by 1-hour increments starting from the epoch
    time `1615353499`, and includes a time zone using an hours offset of
    `“+08:00”`.

        dataset = xdr_data 
        | bin _time span = 1h timeshift = 1615353499 timezone = “+08:00”
        | limit 1000

  <!-- -->

  - With a time zone name configured:

  <!-- -->

  - Return a maximum of 1,000 `xdr_data` records with the events of the
    `_time` field grouped by 1-hour increments starting from the epoch
    time `1615353499`, and includes an `"America/Los_Angeles"` time
    zone.

        dataset = xdr_data
        | bin _time span = 1h timeshift = 1615353499 timezone = “America/Los_Angeles”
        | limit 1000

#### call

##### Syntax

    call "<name of predefined query>" [<param_name1> = <value1> <param_name2> = <value2>....]

##### Description

The `call` stage is used to reference a predefined query from the Query
Library, including your Personal Query Library. In addition, if your
query includes parameters you can reference them in the `call` stage
using the syntax `<param_name1> = <value1> <param_name2> = <value2>...`.
When using parameters in your `call` stage, you need to ensure that a
query already exists that uses these parameters.

##### Example without Parameters

For the predefined query called \"CreateRole operation parsed to
fields\", returns a maximum of 100 records, where the `accessKeyId`
equals \"1234\".

    call "CreateRole operation parsed to fields"
    | filter accessKeyId = "1234"
    | limit 100

##### Example with Parameters

Using the same example above, this example shows how to use the same
`call` stage with parameters. This example assumes that there is a query
that is already saved with a parameter `$key_id = "1234"`.

Saved query:

    dataset = dataset_name 
    | filter field_name = $key_id

Query to run with using parameters:

    call "CreateRole operation parsed to fields" key_id = "1234"
    | limit 100

#### comp

##### Syntax

    comp <aggregate function1> (<field>) [as <alias>][,<aggregate function2>(<field>) [as <alias>],...] [by <field1>[,<field2>...]]
    [addrawdata = true|false [as <target field>]]

##### Description

The `comp` stage precedes functions calculating statistics for results
to compute values over a group of rows and return a single result for a
group of rows.

- Aggregation functions, such as `sum`, `min`, and `max`

- Approximate aggregate functions, such as `approx_count` or
  `approx_top`

At least one of the [comp aggregate
functions](#Xbe8ef5bed5041d4f7244328f58eeb9ae594e63a) or [comp
approximate aggregate
functions](#X1abbfbf792b310782f5d254eea2273e4683c9fd) must be used. Yet,
it\'s also possible to define a comp stage with both types of aggragate
functions.

Use approximate aggregate functions to produce approximate results,
instead of exact results used with regular aggregate functions, which
are more scalable in terms of memory usage and time.

Use the `alias` clause to provide a column label for the `comp` results,
and is optional.

The `by` clause identifies the rows in the result set that will be
aggregated. This clause is optional. Provide one or more fields to this
clause. All fields with matching values are used to perform the
aggregation. For example, if you had records such as:

    number,id,product
    100,"se1","A55"
    50,"se1","A60"
    50,"se1","A60"
    25,"se2","A55"
    25,"se2","A60" 

The you can aggregate on the number column, and perform aggregation
based on matching values in the id and/or product column. So if you sum
the number column by the id column, you would get two results:

- 200 for \"se1\"

- 50 for \"se2\"

If you summed by id and product, you would get:

- 100 for \"se1\" and \"A55\" (there are no matching pairs).

- 100 for \"se1\" and \"A60\" (there is one matching pair).

- 25 for \"se2\" and \"A55\" (there are no matching pairs).

- 25 for \"se2\" and \"A60\" (there are no matching pairs).

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Wildcard Aggregates

You can use a wildcard to perform an aggregate for every field contained
in the result set, except for the field(s) specified in the `by` clause.

> **Note**
>
> Wildcards are only supported with aggregate functions and not
> approximate aggregate functions.

The syntax for this is:

    comp <aggregate function>(*) as * [by [asc|desc] <field1>[,<field2>...]]
    [addrawdata = true|false as <target field>]

For wildcards to work, all of the fields contained in the result set
that are *not* identified in the `by` clause must be aggregatable.

##### Examples

Sum the action_total_download values for all records with matching pairs
of values for the `actor_process_image_path` and
`actor_process_command_line` fields. The query calculates a maximum of
100 `xdr_data` records and includes a `raw_data` column listing the raw
data events used to display the final comp results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path,
    actor_process_command_line as Process_CMD,
    action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp sum(Download) as total by Process_Path, Process_CMD addrawdata = true as raw_data

Using the `panw_ngfw_traffic_raw` dataset, sum the `bytes_total`,
`bytes_received`, and `bytes_sent` values for every record contained in
the result set with a matching value for `source_ip`. The query
calculates a maximum of 1000 `xdr_data` records and includes a
`raw_data` column listing the raw data events used to display the final
comp results.

> **Note**
>
> The `comp` stage runs on 1000 raw data events, but only a 100 will be
> displayed in the `raw_data` column.

    dataset = panw_ngfw_traffic_raw
    | fields bytes_total, bytes_received, bytes_sent, source_ip
    | limit 1000
    | comp sum(*) as * by source_ip addrawdata = true as raw_data

##### comp Aggregate Functions

The aggregate functions you can use with the `comp` stage are:

- [/document/preview/892171#UUID-9f6b3214-5aa1-eaad-3f4e-8bf749739fe9](/document/preview/892171#UUID-9f6b3214-5aa1-eaad-3f4e-8bf749739fe9)

- [/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9](/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9)

- [/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f](/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f)

- [/document/preview/892108#UUID-3a285088-6527-f654-e309-d9e98abfcaea](/document/preview/892108#UUID-3a285088-6527-f654-e309-d9e98abfcaea)

- [/document/preview/892153#UUID-8bc307ff-d9f5-3c3b-8198-69c157bbd569](/document/preview/892153#UUID-8bc307ff-d9f5-3c3b-8198-69c157bbd569)

- [/document/preview/892117#UUID-7f6757bd-1f85-b533-9e9e-4b98cddd41b5](/document/preview/892117#UUID-7f6757bd-1f85-b533-9e9e-4b98cddd41b5)

- [/document/preview/892189#UUID-7959c792-52e6-76a9-06a8-e632960e6f02](/document/preview/892189#UUID-7959c792-52e6-76a9-06a8-e632960e6f02)

- [/document/preview/892207#UUID-95b5253f-a765-ce01-d2d8-fc1a7585f4e2](/document/preview/892207#UUID-95b5253f-a765-ce01-d2d8-fc1a7585f4e2)

- [/document/preview/892180#UUID-1758f9c8-cd2c-0777-0945-416f46e582e9](/document/preview/892180#UUID-1758f9c8-cd2c-0777-0945-416f46e582e9)

- [/document/preview/892089#UUID-700caa24-e3dd-d598-599c-83de53d71851](/document/preview/892089#UUID-700caa24-e3dd-d598-599c-83de53d71851)

- [/document/preview/892198#UUID-d4cb994e-fd32-87de-212d-8da94900b007](/document/preview/892198#UUID-d4cb994e-fd32-87de-212d-8da94900b007)

- [/document/preview/981701#UUID-217d27f0-b824-4a6a-b4a7-24a3287c86f9](/document/preview/981701#UUID-217d27f0-b824-4a6a-b4a7-24a3287c86f9)

- [/document/preview/981710#UUID-710828b3-097c-646f-6f69-daf6bdb8527b](/document/preview/981710#UUID-710828b3-097c-646f-6f69-daf6bdb8527b)

- [/document/preview/892135#UUID-1b621025-481c-63b7-5ae2-36ae39372270](/document/preview/892135#UUID-1b621025-481c-63b7-5ae2-36ae39372270)

- [/document/preview/892126#UUID-27f42e2a-f98f-4ab4-843b-24c01b21e4e0](/document/preview/892126#UUID-27f42e2a-f98f-4ab4-843b-24c01b21e4e0)

- [/document/preview/892162#UUID-ee0a11fa-efc0-7518-fb1d-0b6b8d5cf293](/document/preview/892162#UUID-ee0a11fa-efc0-7518-fb1d-0b6b8d5cf293)

##### comp Approximate Aggregate Functions

The approximate aggregate functions you can use with the `comp` stage
are:

- [/document/preview/892052#UUID-b8a95aad-4cb9-41b9-2600-fa55f149a297](/document/preview/892052#UUID-b8a95aad-4cb9-41b9-2600-fa55f149a297)

- [/document/preview/892061#UUID-5020c71a-5cd0-113c-451d-c747ae0524f8](/document/preview/892061#UUID-5020c71a-5cd0-113c-451d-c747ae0524f8)

- [/document/preview/892073#UUID-73d82f1b-a18b-5700-23ac-1bbe840a71c9](/document/preview/892073#UUID-73d82f1b-a18b-5700-23ac-1bbe840a71c9)

#### config

##### Syntax

    config <function>

##### Description

The `config` stage configures the query behavior. It must be used with
one of the [config
Functions](#X08fb769edd21013c23063a1e8f9b21f52488f22). This stage must
be presented as the first stage in the query.

##### config Functions

These functions you can use with the `config` stage:

- [case_sensitive](#UUID9f824266c5a69741595880c4fc6793fa)

- [timeframe](#UUIDa087d2382f623b58fb8834e5bbc7c8f6)

##### case_sensitive

###### Syntax

    config case_sensitive = true | false

###### Description

The `case_sensitive` configuration identifies whether field values are
evaluated as case sensitive or case insensitive. The
`config case_sensitive` stage must be added at the beginning of the
query. You can also add another `config case_sensitive` stage when
adding a [join](#UUID01b27dc92ccd24c18588d2388b5a0f90) or
[union](#UUIDa68d2e4ff3de66effe819dda04ffc24b) stage to a query.

If you do not provide this stage in your query, the default behavior is
`false`, and case is not considered when evaluating field values.

Things to keep in mind about before implementing this stage

- The Settings \> Configurations \> XQL Configuration \> Case
  Sensitivity (case_sensitive) setting can overwrite this
  `case_sensitive` configuration for all fields in the application,
  except for BIOCs, which will remain case insensitive no matter what
  this setting is set to.

- The `config case_sensitive` stage can\'t be used to compare a field to
  an inner query. In this situation, ensure to use the `lowercase` or
  `uppercase` functions on the field and inner query stages and
  functions syntax.

<!-- -->

- This query won\'t provide the correct results of comparing the
  `agent_hostname` field with the inner query:

      config case_sensitive = false 
      | dataset = xdr_data 
      | fields agent_hostname
      | filter agent_hostname in (dataset = <lookup dataset> | fields agent_hostname)

  This query will provide the correct output:

      config case_sensitive = false  
      | dataset = xdr_data
      | fields agent_hostname 
      | filter lowercase(agent_hostname) in (dataset = <lookup dataset> | alter lower_agent_hostname = lowercase(agent_hostname) | fields lower_agent_hostname)

<!-- -->

- The `config case_sensitive` stage can\'t be used to compare a field to
  an array that contains non-literal strings, for example a field name
  or function.

<!-- -->

- The results of this example are true, where the left side
  (`uppercase("a")`) is lowercase as it\'s not an array, and the right
  side (`("x", "A")`) is also an array that contains only literal
  strings.

      | alter field_name = if(uppercase("a") in ("x", "A"), true, false)

  The results of this example are false, where the left side
  (`uppercase("a")`) is lowercase as it\'s not an array, and the right
  side (`"x", uppercase("a"))`) is an array that contains a function
  (`uppercase("a")`).

      | alter field_name = if(uppercase("a") in ("x", uppercase("a")),true, false)

###### Examples

    config case_sensitive = true 
    | dataset = xdr_data 
    | fields actor_process_image_name as apin 
    | filter apin != NULL and apin contains "python" 
    | limit 100

##### timeframe

###### Syntax

- **Exact Time**

<!-- -->

- config timeframe between "<Year-Month-Day H:M:S ±Timezone>" and "<Year-Month-Day H:M:S ±Timezone>"

<!-- -->

- **Relative Time**

<!-- -->

- config timeframe = <number><time unit>

      config timeframe between "<+|-><number><time unit>" and "now"

      config timeframe between "begin" and "<+|-><number><time unit>"

      config timeframe between "<+|-><number><time unit>" and "<+|-><number><time unit>"

###### Description

The `timeframe` configuration enables you to perform searches within a
specific time frame from the query execution. The results for the time
frame are based on times listed in the `_Time` column in the results
table.

You can add the `timeframe` configuration to your queries using
different formats depending on whether the time frame you are setting is
an exact time or relative time.

When you set an exact time, include the `config timeframe` details:
`between "<Year-Month-Day H:M:S ±Timezone>" and "<Year-Month-Day H:M:S ±Timezone>"`.
The `±Timezone` format is: `±xxxx`. When you do not configure a
timezone, the default is `UTC`. The exact time is based on a static time
frame according to when the query is sent.

When you set a relative time, you have a few options for setting the
`config timeframe`, where the syntax `<+|->` indicates whether to go
back (`-`) or forward (`+`) in time. The default is back (`-`).

- <number><time unit>

<!-- -->

- Enables setting a static time frame according to when the query is
  sent, where you choose the `<time unit>` from the available time unit
  options listed in the table below.

<!-- -->

- between "<+|-><number><time unit>" and "now"

<!-- -->

- Enables setting a time frame between a defined start time, where you
  choose the `<time unit>` from the available time unit options listed
  in the table below, and the end time as the time the query is run with
  the preset keyword \"now\".

<!-- -->

- between "begin" and "<+|-><number><time unit>"

<!-- -->

- Enables setting a time frame between a preset start time according to
  the Unix epoch time 00:00:00 UTC on 1 January 1970 with the \"begin\"
  keyword, and a defined ending time, where you choose the `<time unit>`
  from the available time unit options listed in the table below.

<!-- -->

- between "<+|-><number><time unit>" and "<+|-><number><time unit>"

<!-- -->

- Enables setting a time frame between a defined starting and ending
  time, where you choose the `<time unit>` from the available time unit
  options listed in the table below.

> **Important**
>
> When a query includes any inner queries, the inner queries receives
> its time frame from the outer query unless the inner query has a
> separate time frame defined.

###### Connection to the time period in the Query Builder

When using the Query Builder to define a query, the time period can be
set at the top right of the query window using the time picker, and the
default is 24 hours. Whenever the time period is changed in the query
window, the `config timeframe` is automatically set to the time period
defined, but this won\'t be visible as part of the query. Only if you
manually type in the `config timeframe` will this be seen in the query.

###### Available time units

  -----------------------------------------------------------------------
  Time Unit                           Description
  ----------------------------------- -----------------------------------
  S                                   seconds

  M                                   minutes

  H                                   hours

  D                                   days

  W                                   weeks

  MO                                  months

  Y                                   years
  -----------------------------------------------------------------------

> **Note**
>
> The time unit is not case sensitive.

###### Examples

####### Relative Time

- Example of `<number><time unit>`

<!-- -->

- For the last 10 hours from when the query is sent, return a maximum of
  100 `xdr_data` records.

      config timeframe = 10h
      | dataset = xdr_data
      | limit 100

<!-- -->

- Example of `between "<+|-><number><time unit>" and "now"`

<!-- -->

- Since the last two days until now when the query is run, return a
  maximum of 100 `xdr_data` records.

      config timeframe between "2d" and "now"
      | dataset = xdr_data
      | limit 100

<!-- -->

- Example of `between "begin" and "<+|-><number><time unit>"`

<!-- -->

- Since the Unix epoch time 00:00:00 UTC on 1 January 1970 until the
  past 2 years when the query is run, return a maximum of 100 `xdr_data`
  records.

      config timeframe between "begin" and "2y"
      | dataset = xdr_data
      | limit 100

<!-- -->

- Example of
  `between "<+|-><number><time unit>" and "<+|-><number><time unit>"`

<!-- -->

- Since the last four days until the next 5 days when the query is run,
  return a maximum of 100 `xdr_data` records.

      config timeframe between "-4d" and "+5d"
      | dataset = xdr_data
      | limit 100

####### Exact Time

From April 1, 2021 at 9:00 a.m. UTC -02:00 until April 2, 2021 at 10:00
a.m. UTC -02:00, return a maximum of 100 `xdr_data` records.

    config timeframe between "2021-04-01 09:00:00 -0200" and "2021-04-02 10:00:00 -0200" 
    | dataset = xdr_data 
    | limit 100

#### dedup

##### Syntax

    dedup <field1>[,<field2>, ...] by asc | desc <field>

##### Description

The `dedup` stage removes all records that contain duplicate values (or
duplicate sets of values) from the result set. The record that is
returned is identified by the `by` clause, which selects the record by
either the first or last occurance of the field specified in this
clause.

> **Note**
>
> The `dedup` stage can only be used with fields that contain numbers or
> strings.

##### Examples

Return unique values for the `actor_primary_username` field. For any
given field value, return the first chronologically occurring record.

    dataset = xdr_data 
    | fields actor_primary_username as apu 
    | filter apu != null 
    | dedup apu by asc _time

Return the last chronologically occurring record for any given
`actor_primary_username` value.

    dataset = xdr_data 
    | fields actor_primary_username as apu 
    | filter apu != null 
    | dedup apu by desc _time

Return the first occurrence seen by for any given
`actor_primary_username`. field value.

    dataset = xdr_data 
    | fields actor_primary_username as apu 
    | filter apu != null 
    | dedup apu by asc apu

Return unique groups of `actor_primary_username` and
`os_actor_primary_username` field values. For each unique grouping,
return the pair that first appears on a record with a non-NULL
`action_file_size` field.

    dataset = xdr_data 
    | fields actor_primary_username as apu, 
             os_actor_primary_username as oapu, 
             action_file_size as afs 
    | filter apu != null and afs != null 
    | dedup apu, oapu by asc afs

#### fields

##### Syntax

- Dataset Queries

<!-- -->

- fields [-] <field_1> [as <name1>], <field_2> [as <name2>], ...

<!-- -->

- Cortex Data Model (XDM) Queries

  - fields [-] <field_1> [as <name1>], <field_2> [as <name2>], ...

  - fields [-] fieldset.xdm_<fieldset name1>, fieldset.xdm_<fieldset name2>, ...

  - Combination of both options above are supported with fields and
    fieldsets in any order:

  <!-- -->

  - fields [-] fieldset.xdm_<fieldset name1> , <field_1> as [as <name1>], fieldset.xdm_<fieldset name2>network , <field_2>

> **Note**
>
> When creating XDM queries, the raw dataset fields are accessible by
> `<dataset>.<field>`, such as `fields amazon_eks_raw.logStream`.

##### Description

The `fields` stage declares which fields are returned in the result set,
including name changes. If this stage is used, then subsequent stages
can operate only on the fields identified by this stage. The syntax for
this stage differs depending on the type of query you are running.

##### Both Dataset and XDM Queries

For both dataset and XDM queries, your `fields` stage syntax can include
the following elements:

###### Wildcards

Use a wildcard (`*`) to include all fields that match the pattern, where
wildcards can only be added at the beginning or end of a string. The
following table explains the different scenarios for using wildcards in
fields with examples:

> **Note**
>
> Wildcards are not supported in fieldsets.

+-----------------------------------+-----------------------------------+
| Wildcard Scenarios                | Examples                          |
+===================================+===================================+
| Adding at the end of a field.     | - Dataset Queries                 |
|                                   |                                   |
|                                   |   - `event_*`                     |
|                                   |                                   |
|                                   | - XDM Queries                     |
|                                   |                                   |
|                                   |   - `xdm.source*`                 |
|                                   |                                   |
|                                   |   - `xdm.source.*`                |
|                                   |                                   |
|                                   |   - `xdm.source.a*`               |
+-----------------------------------+-----------------------------------+
| Adding at the beginning of a      | - Supported syntax                |
| field, when there is no period    |                                   |
| anywhere else in the field.       |   - `*ipv4`                       |
|                                   |                                   |
|                                   | - Unsupported syntax              |
|                                   |                                   |
|                                   |   - `*.ipv4`                      |
|                                   |                                   |
|                                   |   - `*source.ipv4`                |
+-----------------------------------+-----------------------------------+
| Adding at both the beginning and  | - Supported syntax                |
| end of a field has the same       |                                   |
| limitations as using it at the    |   - `*ipv4*`                      |
| beginning of a field.             |                                   |
|                                   | - Unsupported syntax              |
|                                   |                                   |
|                                   |   - `*.ipv4*`                     |
|                                   |                                   |
|                                   |   - `*ipv4.*`                     |
|                                   |                                   |
|                                   |   - `*source.ipv4*`               |
+-----------------------------------+-----------------------------------+
| Workaround syntax using the       | - `` *`.ipv4` ``                  |
| `` ` `` character can be used,    |                                   |
| which does not support the        | - `` *`source.ipv4` ``            |
| auto-suggest feature during XQL   |                                   |
| query creation.                   |                                   |
+-----------------------------------+-----------------------------------+

###### Minus Character

Use a minus character (`-`) to exclude a field from the result set. For
example,  `| fields - <field1>, <field2>` will exclude both `<field1>`
and `<field2>` fields in your query results.

The following system fields cannot be excluded and are always displayed,
if they exist:

- Dataset queries: `_time`, `_insert_time`, `_raw_log`, `_product`,
  `_vendor`, `_tag`, `_snapshot_id`, `_snapshot_log_count`,
  `_snapshot_collection_ts`, `_id`

- XDM queries: `_time`

###### As Clause

Use the `as` clause to set an alias for a field. If you use the `as`
clause, then subsequent stages must use that alias to refer to the
field.

##### XDM Queries

For XDM queries, your `fields` stage syntax can include the following
additional elements:

###### Fieldsets

Use a `fieldset` within the `fields` stage to refine queries on the XDM
by limiting the analysis to a specific set of fields. Fieldsets contain
a group of related fields, for example, the `fieldset.xdm_endpoint`
includes fields that are related to endpoints.

The `xdm_core` fieldset contains fields typically queried by users,
including commonly used event, source, and target fields. When no
specific fields are specified in a query, the following fields will be
returned by default: `_time`, `xdm.event.type`, `xdm.event.description`,
`xdm.event.operation`, `xdm.event.operation_sub_type`,
`xdm.event.outcome`, `xdm.source.host.hostname`,
`xdm.source.user.username`, `xdm.source.user.user_type`,
`xdm.source.sent_bytes`, `xdm.source.agent.identifier`,
`xdm.source.user_agent`, `xdm.source.process.name`,
`xdm.source.process.executable.path`,
`xdm.source.process.executable.filename`, `xdm.source.ipv4`,
`xdm.source.port`, `xdm.target.host.hostname`,
`xdm.target.user.username`, `xdm.target.process.executable.path`,
`xdm.target.ipv4`, `xdm.target.port`, `xdm.target.user.user_type`,
`xdm.target.sent_bytes`, `xdm.target.agent.identifier`,
`xdm.target.url`, `xdm.target.domain`, `xdm.target.process.name`,
`xdm.target.process.executable.filename`, `xdm.event.outcome_reason`,
`xdm.observer.product`, `xdm.event.is_completed`, `xdm.event.duration`

For more information on these fields, see the [Cortex Data Model Schema
Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-Data-Model-Schema-Guide/Introduction).

###### Wildcards

When combining the results of a dataset and XDM query using the
[join](#UUID01b27dc92ccd24c18588d2388b5a0f90) stage, the wildard (\*)
relates to both. For example, this query will return both `datamodel`
fields that contain "host" and `xdr_data` fields that contain "host".

    datamodel
        | join (dataset=xdr_data) as x xdm.original_event_id = x.event_id 
        | fields *host*

##### Dataset Query Example

Return the `action_country` field from all `xdr_data` records where the
`action_country` field is both not null and not \"-\". Also include all
fields with names that match `event_*` except for `event_type`.

    dataset = xdr_data 
    | fields action_country as ac 
    | fields event_* 
    | fields - event_type 
    | filter ac != null and ac != "-" 

##### XDM Query Example

Return the XDM fields that are related to the network
(`fieldset.xdm_network`), fields that are related to endpoints
(`fieldset.xdm_endpoint`), and the `xdm.alert.name` field.

    datamodel dataset = xdr_data
    | fields fieldset.xdm_network, fieldset.xdm_endpoint, xdm.alert.name 

##### XDM Query using a Wildcard

Return the XDM fields that are related to the `xdm.source.*` and
`xdm.email.*` fields, where the `xdm.source.user.username` is `newman`.

    datamodel dataset = xdr_data
    | filter xdm.source.user.username = "newman"
    | fields xdm.source.*, xdm.email.*

#### filter

##### Syntax

    filter <boolean expr>

##### Description

The `filter` stage identifies which data records should be returned by
the query. Filters are boolean expressions that can use a wide range of
functions and operators to express the filter. If a record matches the
filter as the filter expression returns `true` when applied to the
record, the record is returned in the query\'s result set.

The functions you can use with a filter are described in
[Functions](#UUIDe74efd8b8558b7a11ca8525d6b6a30b2). For a list of
supported operators, see [Supported
operators](#UUIDf250f6fc117feefa485a8b5165cd7e32).

Single vs triple double quotes behavior

Cortex XSIAM enables you to use single double quotes (`"<text>"`) or
triple double quotes (`"""<text>"""`) when defining your XQL syntax for
string manipulation. This specific syntax is used with different stages,
functions, and operators, with or without wildcards. Typically, the
`alter` and `filter` stages are used with single or triple double
quotes.

Using single double quotes

Single double quotes (`"<text>"`) include the following functionality:

- Treats the string value literally.

- Wildcards using the asterisk (\*) are processed as XQL wildcards, and
  match any sequence of characters.

- Escape sequences, such as `\n` (new line) or `\t` (tab), are not
  processed and are treated as plain characters.

`"\test\"` means to look for `\test\`

Using triple double quotes

Triple double quotes (`"""<text>"""`) include the following
functionality:

- Enables regex-style pattern matching and escape sequence
  interpretation.

- Escape sequences, such as `\n` (new line) or `\t` (tab), are
  processed.

- Wildcards using the asterisk (\*) are processed as XQL wildcards, and
  match any sequence of characters.

`"""\\test\\"""` means to look for `\test\`

**Understanding the results**:

- The double backslashes (`\\`) at the beginning becomes a single
  backlash (`\`) as it\'s processed as an escaped backslash.

- `test` is interpreted as literal.

- The double backslashes (`\\`) at the end becomes a single backlash
  (`\`) as it\'s processed as an escaped backslash.

Query example using filter

When using the `filter` stage, you can use both single (`"<text>"`) and
triple (`"""<text>"""`) double quotes when specifying string values. The
difference lies in how special characters and pattern matching are
interpreted.

The examples provided are based on the following data table for a
dataset called `test_dataset`:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  Mar 26th 2022 19:26:07              12\\t3

  May 7th 2023 15:16:00               12 3

  Jun 8th 2024 16:56:27               1233

  Mar 26th 2024 19:26:07              123

  Apr 5th 2024 11:21:02               12\\t34563

  Apr 9th 2025 13:22:22               1233345

  May 9th 2025 13:22:22               12 35897

  May 30th 2025 21:45:02              116
  -----------------------------------------------------------------------

    config timeframe = 10y 
    | dataset = test_dataset  
    | filter test = "12\t3*"
    | fields test

**Output results table**:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  Mar 26th 2022 19:26:07              12\\t3

  Apr 5th 2024 11:21:02               12\\t34563
  -----------------------------------------------------------------------

**Explanation of results**:

The asterisk (`*`) in `"12\t3*"` means to process the string field as an
XQL wildcard by matching any sequence of characters that begins with
`12\t3`. In addition, the `\t` characters are not processed as an escape
character, but as plain characters.

    config timeframe = 10y 
    | dataset = test_dataset  
    | filter test = """12\t3*"""
    | fields test

**Output results table**:

  -----------------------------------------------------------------------
  \_TIME                              TEST
  ----------------------------------- -----------------------------------
  May 7th 2023 15:16:00               12 3

  May 9th 2025 13:22:22               12 35897
  -----------------------------------------------------------------------

**Explanation of results**:

The `\t` in `"""12\t3*"""` is processed as a tab escape character. The
asterisk (`*`) in `"""12\t3*"""` means to process the string field as an
XQL wildcard by matching any sequence of characters that begins with
`12<tab>3`.

##### Dataset Query Examples

Return `xdr_data` records where the `event_type` is `NETWORK` and the
`event_sub_type` is `NETWORK_HTTP_HEADER`.

    dataset = xdr_data 
    | filter event_type = NETWORK and event_sub_type = NETWORK_HTTP_HEADER

> **Note**
>
> When adding filters to an XQL query, possible field values for `enum`
> fields are available using the auto-complete feature. Yet, the
> autocomplete can only show enum values that are known to the schema.
> In some cases, on data import an enum value is included that is not
> known to the defined schema. In this case, the value will appear in
> the result set as an unknown value, such as `event_type_unknown_4`. Be
> aware that even though this value appears in the result set, you
> cannot create a filter using it. For example, this query will fail,
> even if you know the value appears in your result set:

    dataset = xdr_data 
    | filter event_type = event_type_unknown_4

When using fields of type `ENUM`, the following syntax is supported:

**Syntax format A**

    | filter event_type = ENUM.FILE

**Syntax format B**

    | filter event_type = FILE

##### XDM Query Examples

Return the XDM fields that are related to the `xdm.source.*` and
`xdm.email.*` fields, where the `xdm.source.user.username` is `newman`.

    datamodel dataset = xdr_data
    | filter xdm.source.user.username = "newman"
    | fields xdm.source.*, xdm.email.*

##### XDM CONSTS (ENUMS)

When using fields of type ENUM, you can map values from a predefined
list of ENUMs. For example, the field `xdm.network.ip_protocol` is
defined as `Enum.IP_PROTOCOL`, so you can assign it values such as
`XDM_CONST.IP_PROTOCOL_TCP`. The full list can be found in the
automatically suggested values for the relevant fields. This syntax is
not mandatory.

    datamodel dataset = xdr_data
        | filter xdm.network.ip_protocol = XDM_CONST.IP_PROTOCOL_TCP

For more information on the XDM CONST fields, see the [Cortex Data Model
Schema
Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-Data-Model-Schema-Guide/Introduction).

##### XDM Aliases

The Cortex Data Model (XDM) includes aliases. These are predefined sets
of fields that can be used to simplify your filter. When the `XDM_ALIAS`
keyword is added while writing a query, a list of available predefined
aliases and a tooltip are displayed. The tooltip provides more details
about the selected alias. The aliases support these Cortex Query
Language (XQL) operators: `comparison`, `string`, and `range`.

For example, when you type this query to search the IPv4 field in the
XDM,

    datamodel dataset = xdr_data
    | filter XDM_ALIAS.ipv4 = "10.10.10.10"

the tooltip displays the fields that will be searched for the alias
`XDM_ALIAS.ipv4`:

`xdm.network.dchp.ciaddr`, `xdm.target.ipv4`, `xdm.network.dhcp.giaddr`,
`xdm.source.ipv4`, `xdm.intermediate.ipv4`, `xdm.network.dhcp.yiaddr`,
`xdm.network.dhcp.siaddr`

The query above is the equivalent to the following syntax, which does
not contain a predefined alias, and displays the rows that match the
alias `XDM_ALIAS.ipv4` equaling \"10.10.10.10\" at least once in the
fields that make up the alias:

    datamodel dataset = xdr_data
        | filter xdm.network.dchp.ciaddr = "10.10.10.10"
        or xdm.target.ipv4 = "10.10.10.10"
        or xdm.network.dhcp.giaddr = "10.10.10.10"
        or xdm.source.ipv4 = "10.10.10.10"
        or xdm.intermediate.ipv4 = "10.10.10.10"
        or xdm.network.dhcp.yiaddr = "10.10.10.10"
        or xdm.network.dhcp.siaddr = "10.10.10.10"

In this example, when you type this query to search the IPv4 field in
the XDM,

    datamodel dataset = xdr_data
    | filter XDM_ALIAS.ipv4 != "10.10.10.10"

the tooltip displays the fields that will be searched for the alias
`XDM_ALIAS.ipv4`:

`xdm.network.dchp.ciaddr`, `xdm.target.ipv4`, `xdm.network.dhcp.giaddr`,
`xdm.source.ipv4`, `xdm.intermediate.ipv4`, `xdm.network.dhcp.yiaddr`,
`xdm.network.dhcp.siaddr`

The query above is the equivalent to the following syntax, which does
not contain a predefined alias, and does not display any rows that match
the alias `XDM_ALIAS.ipv4` equaling \"10.10.10.10\" at least once in the
fields that make up the alias:

    datamodel dataset = xdr_data
        | filter xdm.network.dchp.ciaddr != "10.10.10.10"
        and xdm.target.ipv4 != "10.10.10.10"
        and xdm.network.dhcp.giaddr != "10.10.10.10"
        and xdm.source.ipv4 != "10.10.10.10"
        and xdm.intermediate.ipv4 != "10.10.10.10"
        and xdm.network.dhcp.yiaddr != "10.10.10.10"
        and xdm.network.dhcp.siaddr != "10.10.10.10"

#### getrole

> **Note**
>
> This stage requires an Identity Threat Module license to view the
> results.
>
> **Important**
>
> This stage is unsupported in BIOCs and real-time Correlation Rules.

##### Syntax

    getrole <field> [as <alias>]

##### Description

The `getrole` stage enriches events with specific roles associated with
usernames or endpoints. The `getrole` stage receives as an input a
string field that is either a username in the `NETBIOS\SAM` format, such
as `mydomain\myuser`, or the agent ID of a host. The agent ID can be
found in the `endpoints` dataset as `endpoint_id` or in the `xdr_data`
dataset as `agent_id`.

The roles for this field are displayed in a column called
**asset_roles** in the results table. If there is one or more roles
associated with the field, the values are represented as a string array,
such as `['ADMIN', 'USER']`, and are listed in the **asset_roles**
column. If there are no roles, the resulting column is an empty array.

You can also change the name of the column using `as` in the syntax to
define an alias: `getrole <field> as <alias>`.

In addition, it is possible to use the `filter` stage with a new `ROLE`
prefix to display the results of a particular role using the syntax:

- To include one specific role:

  - `filter <field> = ROLE.<role name>`

  - `filter array_length(arrayfilter(<field>, "@element" = ROLE.<role name> )) > 0`

- To include more than one specific role:

  - `filter <field> in (ROLE.<role name1>, ROLE.<role name2>, ....)`

- To exclude one specific role:

  - `filter array_length(arrayfilter(<field>, "@element" = ROLE.<role name> )) = 0`

- To exclude more than one specific role:

  - `filter array_length(arrayfilter(<field>, "@element" in (ROLE.<role name1>, ROLE.<role name2>, ....))) = 0`

##### Examples

Return a maximum of 100 `xdr_data` records with the enriched events
including specific roles associated with usernames. If there are one or
more roles associated with the value of the `user_id` string field
column, the output is displayed in the **asset_roles** column in the
results table. Otherwise, the field is empty.

    dataset = xdr_data
    | limit 100
    | getrole user_id

Return a maximum of 100 `xdr_data` records of all the powershell
executions made by the `SERVICE_ACCOUNTS` user role in the organization.
The first `filter` stage indicates how to filter for the parent process,
which is powershell.exe. The `fields` stage indicates the field columns
to include in the results table and which ones are renamed in the table:
`action_process_image_name` to `process_name` and
`action_process_image_command_line` to `process_cmd`. The `getrole`
stage indicates the enriched events to include for the specific roles
associated with usernames. If the `ROLE.SERVICE_ACCOUNTS` role is
associated with any values in the `actor_effective_username` string
field column, the row is displayed in the results table. Otherwise, the
entire row is excluded from the results table.

    dataset = xdr_data
    | filter event_type = ENUM.PROCESS  and event_sub_type = ENUM.PROCESS_START and lowercase(actor_process_image_name) = "powershell.exe"
    | fields action_process_image_name as process_name, action_process_image_command_line as process_cmd, event_id, actor_effective_username
    | getrole actor_effective_username as user_roles
    | filter user_roles = ROLE.SERVICE_ACCOUNTS
    | limit 100

#### iploc

##### Syntax

    iploc <field>

##### Description

The `iploc` stage associates the IPv4 address of any field to a list of
predefined attributes related to the geolocation. By default, when using
this stage in your queries, the geolocation data is added to the results
table in these predefined column names: **LOC_ASN_ORG**, **LOC_ASN**,
**LOC_CITY**, **LOC_CONTINENT**, **LOC_COUNTRY**, **LOC_LATLON**,
**LOC_REGION**, and **LOC_TIMEZONE**.

> **Note**
>
> The `loc_latlon` field contains a string that is a combination of two
> floating numbers representing the latitude and longitude separated by
> a comma, for example, "32.0695,34.7621\".

The following options are available to you when using this stage in your
queries:

- You can specify the geolocation fields that you want added to the
  results table.

- You can append a suffix to the name of the geolocation field column in
  the results table.

- You can change the name of the geolocation field column in the results
  table.

- You can also view the geolocation data on a graph type called map,
  where the `xaxis` is set to either `loc_country` or `loc_latlon`, and
  the `yaxis` is a number field.

> **Note**

- > The `iploc` stage can only be used with fields that contain numbers
  > or strings.

- > To improve your query performance, we recommend that you `filter`
  > the data in your query before the `iploc` stage is run. In addition,
  > limiting the number of fields in the results table further improves
  > the performance.

##### Examples

Return a maximum of 1000 `xdr_data` records with the specific
geolocation data associated with the `action_remote_ip` field, where no
record with a null value for `action_remote_ip` is included, and
displays the name of the city in a column called `city` and a
combination of the latitude and longitude in a column called
`loc_latlon` with comma-separated values of latitude and longitude.

    dataset = xdr_data
    | limit 1000 
    | filter action_remote_ip != null 
    | iploc action_remote_ip loc_city as city, loc_latlon

Return a maximum of 1000 `xdr_data` records with all the available
geolocation data with the predefined column names, and add the specified
`suffix _remote_id` to each predefined column name, where no record with
a null value for `action_remote_ip` is included.

    dataset = xdr_data 
    | limit 1000
    | filter action_remote_ip != null
    | iploc action_remote_ip suffix=_remote_id 

Return a maximum of 1000 `xdr_data` records with the specific
geolocation data associated with the `action_remote_ip` field that
includes the name of the country (contained in `loc_country`) in a
column called `country`, where no record with a null value for either
`country` or `action_remote_ip` is included. The comp stage is used to
count the number of IP addresses per country. The results are displayed
in a graph type `of kind` map, where the x-axis represents the `country`
and the y-axis the `action_remote_ip`.

    dataset = xdr_data 
    | limit 1000
    | iploc action_remote_ip loc_country as country  
    | filter country != null and action_remote_ip  != null
    | comp count() as ip_count by country 
    | view graph type = map xaxis = country yaxis = ip_count

#### join

##### Syntax

    join conflict_strategy = both|left|right 
         type = inner|left|right 
         ((<xql query>) 
         as <execution_name> 
         <boolean_expr>)

##### Description

The `join()` stage combines the results of two queries into a single
result set. This stage is conceptually identical to a SQL join.

+-----------------------------------+---------------------------------------+
| Parameter/Clause                  | Description                           |
+===================================+=======================================+
| `conflict_strategy`               | Identifies the join conflict strategy |
|                                   | when there is a conflict in the       |
|                                   | column names between the 2 result     |
|                                   | sets which one should be chosen,      |
|                                   | either:                               |
|                                   |                                       |
|                                   | - `right`: The column from the inner  |
|                                   |   `join` query is used (default),     |
|                                   |   which implements a right outer      |
|                                   |   join.                               |
|                                   |                                       |
|                                   | - `left`: The column from the orignal |
|                                   |   result set in the dataset is used,  |
|                                   |   which implements a left outer join. |
|                                   |                                       |
|                                   | - `both`: Both columns are used. The  |
|                                   |   original result set column from the |
|                                   |   dataset keeps the current name,     |
|                                   |   while the inner `join` query result |
|                                   |   set column name includes the        |
|                                   |   following suffix added to the       |
|                                   |   current name `_joined_10`, such as  |
|                                   |   `<original column name>_joined_10`, |
|                                   |   and depending on the number of      |
|                                   |   conflicted fields the suffix        |
|                                   |   increases to `_joined_11`,          |
|                                   |   `_joined_12`\....                   |
+-----------------------------------+---------------------------------------+
| `type`                            | Identifies the join type.             |
|                                   |                                       |
|                                   | - `inner`                             |
|                                   |                                       |
|                                   | <!-- -->                              |
|                                   |                                       |
|                                   | - Returns all the records in common   |
|                                   |   between the queries that are being  |
|                                   |   joined. This is the default join    |
|                                   |   type.                               |
|                                   |                                       |
|                                   | <!-- -->                              |
|                                   |                                       |
|                                   | - `right`                             |
|                                   |                                       |
|                                   | <!-- -->                              |
|                                   |                                       |
|                                   | - Returns all records from the join   |
|                                   |   result set, plus any records from   |
|                                   |   the parent result set that          |
|                                   |   intersect with the join result set. |
|                                   |                                       |
|                                   | <!-- -->                              |
|                                   |                                       |
|                                   | - `left`                              |
|                                   |                                       |
|                                   | <!-- -->                              |
|                                   |                                       |
|                                   | - Returns all records from the parent |
|                                   |   result set, plus any records from   |
|                                   |   the join result set that intersect  |
|                                   |   with the parent result set.         |
+-----------------------------------+---------------------------------------+
| \<*xql query*\>                   | Provides the XQL query to be joined   |
|                                   | with the parent query.                |
+-----------------------------------+---------------------------------------+
| as \<*execution_name*\>           | Provides an alias for the join        |
|                                   | query\'s result set. For example, if  |
|                                   | you specify an execution name of      |
|                                   | `join1`, and in the join query you    |
|                                   | return field `agent_id`, then you can |
|                                   | subsequently refer to that field as   |
|                                   | `join1.agent_id`.                     |
+-----------------------------------+---------------------------------------+
| \<*boolean_expr*\>                | Identifies the conditions that must   |
|                                   | be met in order to place a record in  |
|                                   | the join result set.                  |
+-----------------------------------+---------------------------------------+

> **Note**
>
> This stage does not preserve sort order. If you are combing this stage
> with a [sort](#UUIDb856a4139d2cf09ffea224fbf408c975) stage, specify
> the `sort` stage after the `join`.

###### Examples

Return `microsoft_windows_raw` records, which are combined with the
`xdr_data` records to include a new column called `edr`. For the
`event_type` set to `EVENT_LOG`, the `actor_process_image_name` and
`event_id` fields are returned from all `xdr_data` records, which are
then compared to the fields inside the `microsoft_windows_raw` dataset,
where `edr.event_id = edr_event_id`, and the results are added to the
new `edr` column.

    dataset  = microsoft_windows_raw 
    | join (dataset = xdr_data | filter event_type = EVENT_LOG | fields actor_process_image_name, event_id ) 
    as edr edr.event_id = edr_event_id

Return a maximum of 100 `xdr_data` records with the events of the
`agent_id`, `event_id` , and `_product` fields, where the `_product`
field is displayed as `product`. The `agent_id`, `event_id`, and
`_product` fields are returned from all `xdr_data` records and are then
compared to the fields inside the `panw_ngfw_filedata_raw` dataset,
where `_time = panw.time`, and the results are added to the new `panw`
column. When there is a conflict in the column names between the 2
result sets both columns are used.

    dataset = xdr_data 
    | fields agent_id, event_id, _product as product
    | join conflict_strategy = both (dataset = panw_ngfw_filedata_raw | fields _product as product)
    as panw _time = panw._time
    | limit 100

#### limit

##### Syntax

    limit <number>

##### Description

The `limit` stage sets the maximum number of records that can be
returned in the result set. To help reduce the Cortex Query Language
(XQL) response time, the default results for a Cortex Data Model (XDM)
query or an XQL basic query is limited to 1000, when  no limit is
explicitly stated in the query. This applies to basic queries with no
stages except the `fields` stage. This default limit does not apply to
widgets, Correlation Rules, public APIs, saved queries, or scheduled
queries, where the limit is a maximum of 1,000,000 results.

Using a small limit can greatly increase the performance of your query
by reducing the number of records that Cortex XSIAM can return in the
result set.

##### Examples

Set the maximum number of records returned by the query to 10.

    dataset = xdr_data | limit 10

#### replacenull

##### Syntax

    replacenull <field> = <text string>

##### Description

The `replacenull` stage replaces null field values with the specified
text string. This guarantees that every field in your result set will
contain a value.

If you use the `replacenull` stage, then all subsequent stages that
refer to the field\'s null value must use the replacement text string.

##### Examples

Return the `action_country` field from every `xdr_data` records where
the `action_country` field is null, using the text string `N/A` in the
place of an empty field value.

    dataset = xdr_data 
    | fields action_country as ac 
    | replacenull ac = "N/A" 
    | filter ac = "N/A"

#### search

##### Syntax

    search "<free_text1>"[,"<free_text2>", ...]

##### Description

The `search` stage searches for free text strings across single or
multiple datasets, including all the dataset fields (columns), that are
stored in your Cortex XSIAM tenant. This search is a manual process that
isn\'t meant to be included in any features where you can include Cortex
Query Language (XQL) queries, such as rules or widgets. Since this
search runs on all your data, it can take time for the query to
complete.

Search results are presented differently depending on the number of
datasets included in the search query:

- Single dataset: All dataset field columns are included in the
  resulting table.

- Multiple datasets: The resulting table includes a limited number of
  field columns, specifically the `_time`, `_vendor`, `_product`,
  `_dataset`, and `raw_data` field columns. The `raw_data` field column
  includes the JSON with the relevant raw information from the datasets.

<!-- -->

- `search` should be the first stage in the query. Only the `config`
  stage can precede `search`.

- You can refine the search to specify datasets.

<!-- -->

- Only datasets are supported. You can\'t refine by preset or search the
  Cortex Data Model (XDM) schema.

  > **Note**

  - > If you *do not* specify a dataset in the query, Cortex XSIAM
    > searches all of the existing datasets on your tenant.

  - > Free text search searches the relevant columns in each dataset.
    > Relevant columns are subject to a change and can vary between
    > datasets.

<!-- -->

- When more than one dataset is included in the search, a new column
  called `raw_data` is displayed in the **Query Results** table. This
  column lists all the fields from the original datasets schema, which
  you can use to drilldown to specific data in your queries.

- Queries containing `search` do not support the `bin`, `comp`, `top`,
  or `dedup` stages.

- Queries using the `search` stage are limited to the last 90 days of
  data. Specifying a time frame outside of this limitation will cause
  the query to fail.

- Some settings for the free text search are dependent on your
  configuration of this feature. By default, the standard behavior is
  followed unless you\'ve requested to disable or enable certain
  configurations for this feature. Here is a list of the default
  settings that can be configured:

  - All datasets are included in the search unless you enabled the
    option to ignore certain datasets.

  - Forensic datasets are not included in the search by default unless
    you enable the option to include forensic datasets in the free text
    search. When forensic datasets are configured to be included in the
    free text search, the forensic datasets are only searched if all
    datasets in the search command are forensic. This means that
    forensic datasets are ignored in mixed dataset searches.

  - Snapshots are searched by default unless you enabled the option to
    ignore snapshots. In addition, the search includes all data in the
    dataset, across all snapshots, unless you enabled the option to
    limit the free text search to only search for values in the latest
    snapshot as defined by the Snapshot SQL.

  - All the rows in the table are searched by default unless you set an
    XQL `text_search_force_limit_size` that defines a maximum number of
    rows per dataset table so only those rows are searched.

  - All JSON fields are searched by default unless you configured the
    system to skip JSON fields.

  - Any hidden fields configured to be excluded from the correlation
    dataset are by default not included in the search.

##### Examples

Returns instances of `"MacOs"` in the `endpoints` dataset.

    search "MacOs" dataset = endpoints

Returns instances of `"MacOs"` or `"failed"` in the `endpoints` and
`agent_auditing` datasets.

    search “MacOs”,“failed” dataset in (endpoints, agent_auditing)

#### sort

##### Syntax

    sort asc|desc <field1>[, asc|desc <field2>...]

##### Description

The `sort` stage identifies the sort order for records returned in the
result set. Records can be returned in ascending (`asc`) or descending
(`desc`) order. If you include more than one field in the `sort` stage,
records are sorted in field specification order.

Keep the following points in mind before running a query with the sort
stage:

- To acheive the correct sorting results when a query includes strings
  representing numbers, it\'s recommend to sort by integer fields and to
  convert all string fields to integers; for example, by using the
  `to_integer` function.

- When sorting by multiple columns, the sort is saved correctly, but the
  user interface will only display the results according to the first
  sorted column.

##### Examples

Return the `action_boot_time` and `event_timestamp` fields from all
`xdr_data` records. Sort the result set first by the `action_boot_time`
field value in descending order, then by `event_timestamp` field in
ascending order.

    dataset = xdr_data 
    | fields action_boot_time as abt, event_timestamp as et 
    | sort desc abt, asc et
    | limit 1

#### Tag

##### Syntax

- Add a single tag:

<!-- -->

- | tag add <tag name>

<!-- -->

- Add a list of tags:

<!-- -->

-  | tag add "<tag name1>", "<tag name2>", "<tag name3>",.....

##### Description

The `tag` stage is used in combination with the `add` operator to append
a single tag or list of tags to the `_tag` system ﬁeld, which you can
easily query in the dataset.

##### Examples

In the `xdr_data` dataset, add a single tag called `"test"` to the
`_tag` system field.

    dataset = xdr_data
    | tag add "test"

In the `xdr_data` dataset, add a list of tags, `"test1"`, `"test2"`, and
`"test3"`, to the `_tag` system field.

    dataset = xdr_data
    | tag add "test1", "test2", "test3"

#### target

##### Syntax

    target type=dataset|lookup [append=true|false] <dataset name>

##### Description

The `target()` stage saves query results to a named dataset or lookup.
These are persistent and can be used in subsequent queries. This stage
must be the last stage specified in the query.

The `type` argument defines the type of dataset to create, when a new
one needs to be created. The following types are supported:

- `dataset`: A regular dataset of type `USER`. Use `dataset` if you are
  saving the query results for use in future queries.

- `lookup`: A small lookup table with a 50 MB limit. When uploading a
  lookup dataset from the **Dataset Management** page, the limit is 30
  MB. This lookup table can be used with parsing rules and downloaded as
  a JSON file. Use `lookup` if you want to export the query results to a
  disk.

> **Note**
>
> Dataset and lookup tables support low frequency changes of up to 1200
> modifications per day. Changes are implemented whenever a dataset or
> lookup dataset are edited.

###### Optional Append

Use `append` to define whether the data from the current query should be
appended to the dataset (`true`) or re-created as a new dataset
(`false`). If no `append` is included, the default is `false`. This
means that after the query runs the data in an existing dataset is
replaced with the new data.

##### Example 1

Save the results of a simple query to a named dataset.

    dataset = xdr_data 
    | fields action_boot_time as abt
    | filter abt != null
    | target type=dataset abt_dataset

Subsequently, you can query the new dataset. Notice that the field names
used by the new dataset conform to the aliases that you used when you
created the dataset:

    dataset = abt_dataset 
    | filter abt = 1603986614040

##### Example 2

The following example creates a dataset with the number of agents per
country.

    dataset = xdr_data
    | fields agent_id,  action_country
    | comp count_distinct(agent_id) as count by action_country
    | target type=dataset append=false agents_per_country

This results in the following XQL JSON:

    {
        "tables": [
            "xdr_data"
        ],
        "original_query": "\n
        dataset=xdr_data\n
        | fields agent_id,  action_country \n
        | comp count_distinct(agent_id) as count by action_country\n
        | target type=dataset append=false agents_per_country\n
        ",    "stages":
     [
            {
                "FIELD_SELECT": {
                    "fields": [
                        {                        "name": "agent_id",                        "as": None
                        },
                        {                        "name": "action_country",                        "as": None
                        }
                    ],
                    "exclude": []
                }
            },
            {
                "GROUP": {
                    "aggregations": [
                        {
                            "function": "count_distinct",
                            "parameters": [
                                "$agent_id"
                            ],
                            "name": "count"
                        }
                    ],
                    "key": [
                        "action_country"
                    ]
                }
            }
        ],
        "output": [
            {
                "TARGET": {
                    "type": "dataset",
                    "target": "agents_per_country",
                    "append": False
                }
            }
        ]
    }

#### top

> **Note**
>
> This stage is unsupported with Correlation Rules.

##### Syntax

    top <integer> <field> [by <field1> ,<field2>...] [top_count as <column name>, top_percent as <column name>]

##### Description

The `top` stage returns the approximate count of top elements for a
given field and the percentage of the count results relative to the
total number of values for the designated field. Use this top stage to
produce approximate results, which are more scalable in terms of memory
usage and time.

The *\<integer\>* in the syntax represents the number of top elements to
return. If a number is not specified, up to 10 elements are returned by
default. The approximate count is listed in the results table in a
column called **TOP_COUNT** and the percentage in a column called
**TOP_PERCENT**. You can update the column names for both tables by
defining `top_count as` *\<column name\>* , top_percent as
*\<column name\>* in the syntax. If you only define one column name to
update in the syntax, the results table displays that column without
displaying the other column.

##### Examples

Returns a table with 3 columns called **EVENT_ID**, **TOP_COUNT**, and
**TOP_PERCENT** with up to 10 unique values for `event_id` with the
corresponding counts and percentages.

    dataset = xdr_data 
    | top event_id

Returns a table with 3 columns called **ACTION_COUNTRY**, **EVENT_ID**,
and **TOTAL** with a single unique value for the `event_id` for each
`action_country` with the corresponding count in the **TOTAL** column.

    dataset = xdr_data 
    | top 1 event_id by action_country top_count as total

#### transaction

> **Note**
>
> This stage is unsupported with RT Correlation Rules.

##### Syntax

    transaction <field_1, field_2, ...>  [span = <time> [timeshift = <epoch time> [timezone = "<time zone>"]] | startswith = <condition> endswith = <condition> allowunclosed= true|false] maxevents = <number of events per transaction>

##### Description

The `transaction` stage is used to find transactions based on events
that meet certain constraints. This stage aggregates all fields in a
JSON string array by fields defined as transaction fields. For example,
using the `transaction` stage to find transactions based on the `user`
and `user_ip` fields will make the  aggregation of json strings of all
fields by the `user` and `user_ip` fields. A maximum of 50 fields can be
aggregated in a `transation` stage.

You can also configure whether the transactions falls within a certain
time frame, which is optional to define. You can set one of the
following:

- `span=<time>`: Use this command to set a time frame per transaction,
  where `<time>` is a combination of a number and time suffix. Set one
  time suffix from the list of available options listed in the table
  below. In addition, you can define a particular start time for
  grouping the events in your query according to the Unix epoch time by
  setting `timeshift = <epoch time> timezone = "<time zone>"`, which are
  both optional. You can configure the `<time zone>` offset using an
  hours offset, such as `“+08:00”`, or using a time zone name from the
  [List of Supported Time
  Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
  such as `"America/Chicago"`. The query still runs without defining the
  epoch time or time zone. If no
  `timeshift = <epoch time> timezone = "<time zone>"` is set, the query
  runs according to last time set in the log.

- `startswith` and `endswith`: Use these commands to set a condition for
  the beginning or end of the transaction, where the condition can be a
  logical expression or free text search.

Set the `allowunclosed` flag to `true` to include transactions which
don\'t contain an ending event. The last event will be 12 hours after
the starting event. By default, this is set to `true` and transactions
without an ending event are included.

Use the `maxevents` command to define the maximum number of events to
include per transaction. If this command is not set, the default value
is 100.

When using the transaction stage, 5 additional fields are added to the
results displayed:

- `_start_time`: Indicates the initial timestamp of the transaction.

- `_end_time`: Indicates the last timestamp for the transaction.

- `_duration`: Displays the difference in seconds between the timestamps
  for the first and last events in the transaction.

- `_num_of_rows`: Indicates the number of events in the transaction.

- `_transaction_id`: Displays the unique transaction ID.

  -----------------------------------------------------------------------
  Time Suffix                         Description
  ----------------------------------- -----------------------------------
  MS                                  milliseconds

  S                                   seconds

  M                                   minutes

  H                                   hours

  D                                   days

  W                                   weeks

  MO                                  months

  Y                                   years
  -----------------------------------------------------------------------

##### Example using Span

Return a maximum of 10 events per transaction from the `xdr_data`
records based on the `user` and `agent_id` fields, where the transaction
time frame is 1 hour.

    dataset=xdr_data
    |transaction user, agent_id span=1h timeshift = 1615353499 
    timezone = “+08:00” maxevents=10

This query results in the following XQL JSON:

    {'TRANSACTION': {'fields': ['user', 'agent_id'], 'maxevents': 10, 'span': {'amount': 1, 'units': 'h', 'timeshift': None}}}

##### Example using Startswith and Endswith

Return a maximum of 99 events per transaction from the `xdr_data`
records based on the `f1` and `f2` fields. The starting event of each
transaction is an event, where one of the fields contains a string
`"str_1"`, and the ending event of each transaction is an event, where
one of the fields contains a string `"str_2"`.

    dataset=xdr_data
    | transaction f1, f2 startswith="str_1" endswith="str2" maxevents=99

This query results in the following XQL JSON:

    {'TRANSACTION': {'fields': ['f1', 'f2'], 'search': {'startswith': {'filter': {'free_text': 'str_1'}}, 'endswith': {'filter': {'free_text': 'str2'}}}, 'maxevents': 99}}

#### union

##### Syntax

    union <datasetname>
    union (<inner xql query>)

##### Description

The `union()` stage combines two result sets into one result. It can be
used in two different ways.

If a dataset name is provided with no other arguments, the two datasets
are combined for the duration of the query, and the fields in both
datasets are available to subsequent stages.

If a Cortex Query Language (XQL) query is provided to this stage, the
result set from that XQL union query is combined with the result set
from the rest of the query. This is effectively an inner join statement.

##### Examples

First, create a dataset using the
[target](#UUID2633c59ff09cbb66a58380019f45d292) stage. This results in a
persistent stage that we can use later with a `union` stage.

    dataset = xdr_data
    | filter event_type = FILE and event_sub_type = FILE_WRITE 
    | fields agent_id, action_file_sha256 as file_hash, agent_hostname 
    | target type=dataset file_event

Then run a second query, using `union` so that the query can access the
contents of the `file_event` dataset. Notice that this second query uses
the `file_hash` alias that was defined for the `file_event` dataset.

    dataset = xdr_data 
    | filter event_type = PROCESS and event_sub_type = PROCESS_START 
    | union file_event
    | fields agent_id, agent_hostname, file_hash, 
          actor_process_image_path as executed_by, 
          actor_process_signature_vendor as executor_signer 
    | filter file_hash != null and executed_by != null

#### view

##### Syntax

    view highlight fields = <field1>[,<field2>,...] values = <value1>[,<value2>,...]
    view graph type = column|line|pie xaxis = <field1> 
         yaxis = <field2> [<optional parameters>]

- Optional `series` parameter:

<!-- -->

- | view graph type = area | bubble | column | line | map | scatter
      xaxis = <field1>
      yaxis = <field2> [<optional parameters>]
      [series = <field3> [<optional parameters>] ]

<!-- -->

    view column order = default|populated

##### Description

The `view()` stage configures the display of the result set in the
following ways:

- `highlight`: Highlights specified strings that Cortex XSIAM finds on
  specified fields. The highlight values that you provide are performed
  as a substring search, so only partial value can be highlighted in the
  final results table.

- `graph type`: Creates an `area`, `bubble`, `column`, `funnel`,
  `gauge`, `line`, `map`, `pie`, `scatter`, `single`, or `wordcloud`
  chart based on the values found for the fields specified in the
  `xaxis` and `yaxis` parameters. In this mode, `view` also offers a
  large number of parameters that allow you to control colors,
  decorations, and other behavior used for the final chart, where the
  options can differ depending on the type of graph selected. You can
  also define a graph `subtype`, when setting the `graph type` to either
  `column` or `pie`.

  - (Optional) `series`: When creating an `area`, `bubble`, `column`,
    `line`, `map`, or `scatter` chart, you can define a `series`
    parameter by specifying a field (column) to group chart results
    based on y-axis values. The series parameter is only supported when
    defining a single y-axis value.

<!-- -->

- You can also generate graphs and outputs of your query data directly
  in the Query Builder after running a Cortex Query Language (XQL) query
  in the **Query Results** tab without having to add the syntax in the
  query. For more information, see [Graph query
  results](#UUID66d5f7c34cf5b98b79e931ea76c83b11).

  > **Note**

  > If you use `graph type`, the fields specified for `xaxis` and
  > `yaxis` must be collatable or the query will fail.

<!-- -->

- `column order`: Enables you to list the query results by popularity,
  where the most non-null returned fields are displayed first using the
  syntax `view column order = populated`. By default, if `column order`
  is not defined (or `view column order=default`), the original column
  order is used.

<!-- -->

- > **Note**

  > This option does not apply to Cortex Query Language (XQL) queries in
  > widgets, Correlation Rules, public APIs, reports, and dashboards. If
  > you include the `view column order` syntax in these types of
  > queries, Cortex XSIAM disregards the stage from the query and
  > completes the rest of the query.

##### Examples

Use the [dedup stage](#UUID9ca262399c1d7020771dd7b5498cf3e7) collect
unique combinations of `event_type` and `event_sub_type` values.
Highlight the word \"STREAM\" when it appears in the result set.

    dataset = xdr_data 
    | fields event_type, event_sub_type 
    | dedup event_type, event_sub_type by asc _time 
    | view highlight fields = event_sub_type values = "STREAM"

Count the number of unique files accessed by each user, and show a
column graph of the results, where the number of unique files are
grouped by username. This query uses [comp
count_distinct](/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f)
to calculate the number of unique files per username.

    dataset = xdr_data 
    | fields actor_effective_username as username, action_file_path as file_path 
    | filter file_path != null and username != null 
    | comp count_distinct(file_path) as file_count by username 
    | view graph type = column xaxis = username yaxis = file_count series = username

Count the number of unique files accessed by each user, and display the
results by popularity according to the most non-null values returned
fields. This query uses [comp
count_distinct](/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f)
to calculate the number of unique files per username.

    dataset = xdr_data 
    | fields actor_effective_username as username, action_file_path as file_path 
    | filter file_path != null and username != null 
    | comp count_distinct(file_path) as file_count by username 
    | view column order = populated

#### windowcomp

##### Syntax

    windowcomp <analytic function> (<field>)[by <fieldA> [,<fieldB>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

> **Note**
>
> Defining a field with an analytic function is optional when using a
> [/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9](/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9)
> function. For [rank](#UUIDe908925c9998cc1ec228e437b1f2816a) and
> [row_number](#UUIDe89b5a346b5812ed0ccd591b8cadac9d) functions, it\'s
> not allowed.

##### Description

The `windowcomp` stage precedes functions calculating statistics. The
results compute values over a group of rows and return a single result
for each row, for all records that contain matching values for the
fields identified using a combination of the by clause, sort, and range.
Only one function can be defined per field, while the other parameters
are optional. Yet, it\'s possible to define multiple fields.

    | windowcomp sum(field_1) by field_2 sort field_3 as field_4, min(field_5) by field_6 sort field_7 as field_8

Supported functions

This stage includes the following functions:

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Function Type                     | Function                                                                                                                                   |
+===================================+============================================================================================================================================+
| Numbering functions               | - [rank](#UUIDe908925c9998cc1ec228e437b1f2816a)                                                                                            |
|                                   |                                                                                                                                            |
|                                   | - [row_number](#UUIDe89b5a346b5812ed0ccd591b8cadac9d)                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Navigation functions              | - [first_value](#UUID8b8aac48f0a6724d770892c56376d7ee)                                                                                     |
|                                   |                                                                                                                                            |
|                                   | - [lag](#UUIDf9a9cd28d571232b5cb17597ace36a69)                                                                                             |
|                                   |                                                                                                                                            |
|                                   | - [last_value](#UUIDd6aafcca30225fafbfb36e1869b5d075)                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Statistical aggregate functions   | - [/document/preview/981710#UUID-710828b3-097c-646f-6f69-daf6bdb8527b](/document/preview/981710#UUID-710828b3-097c-646f-6f69-daf6bdb8527b) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/981701#UUID-217d27f0-b824-4a6a-b4a7-24a3287c86f9](/document/preview/981701#UUID-217d27f0-b824-4a6a-b4a7-24a3287c86f9) |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Aggregate functions               | - [/document/preview/892171#UUID-9f6b3214-5aa1-eaad-3f4e-8bf749739fe9](/document/preview/892171#UUID-9f6b3214-5aa1-eaad-3f4e-8bf749739fe9) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9](/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/892180#UUID-1758f9c8-cd2c-0777-0945-416f46e582e9](/document/preview/892180#UUID-1758f9c8-cd2c-0777-0945-416f46e582e9) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/892089#UUID-700caa24-e3dd-d598-599c-83de53d71851](/document/preview/892089#UUID-700caa24-e3dd-d598-599c-83de53d71851) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/892198#UUID-d4cb994e-fd32-87de-212d-8da94900b007](/document/preview/892198#UUID-d4cb994e-fd32-87de-212d-8da94900b007) |
|                                   |                                                                                                                                            |
|                                   | - [/document/preview/892135#UUID-1b621025-481c-63b7-5ae2-36ae39372270](/document/preview/892135#UUID-1b621025-481c-63b7-5ae2-36ae39372270) |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Optional parameters

The optional parameters available to define in the `windowcomp` function
are explained in the following table:

+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Optional parameters   | Syntax                                                               | Description                                                                           |
+=======================+======================================================================+=======================================================================================+
| By clause             | `[by <fieldA> [,<fieldB>,...]`                                       | The `by` clause is used to break up the input field rows into separate partitions,    |
|                       |                                                                      | over which the `windowcomp` function is independently evaluated.                      |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - Multiple partition fields are allowed when using a partition `by` clause.           |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - When this optional clause is omitted, all rows in the input table comprise a single |
|                       |                                                                      |   partition.                                                                          |
+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Sort                  | `[sort [asc|desc] <field1> [,[asc|desc] <field2>,...]]`              | Defines how field rows are ordered within a partition as either ascending (`asc`) or  |
|                       |                                                                      | descending (`desc`). This clause is optional in most situations, but is required in   |
|                       |                                                                      | some cases for navigation functions and `rank` function.                              |
+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Between window frame  | `[between 0|null|<number>|-<number> [and 0|null|<number>|-<number>]` | Sets the window frame around the current row within a partition, over which the       |
| clause                |                                                                      | window function is evaluated. Numbering functions and the `lag` function can\'t be    |
|                       |                                                                      | used in the window frame clause. Creates a window frame with a lower and upper        |
|                       |                                                                      | boundary. The first boundary represents the lower boundary. The second boundary       |
|                       |                                                                      | represents the upper boundary. Every boundary can include the following options:      |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - `null`: Starts at the beginning or at the end of the partition, depending on the    |
|                       |                                                                      |   placement of the `null`.                                                            |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - `0`: Is set to the current row, where the window frame starts or ends at the        |
|                       |                                                                      |   current row.                                                                        |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - positive/negative `<number>`: The end of the window frame or the start of the       |
|                       |                                                                      |   window frame relative to the current row.                                           |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |   - If only a start `<number>` is defined, only a negative number is allowed:         |
|                       |                                                                      |     `-<number>`.                                                                      |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |   - If a start `<number>` and end `<number>` are defined, the end `<number>` must be  |
|                       |                                                                      |     greater than the start `<number>`.                                                |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | If the `sort` is included, but the window frame clause isn\'t, the following window   |
|                       |                                                                      | frame clause is used by default:                                                      |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |     between null and 0                                                                |
+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| frame_type            | `[frame_type=rows| range]`                                           | Defines the option of the frame as either:                                            |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - `rows` (default): Computes the window frame based on physical offsets from the      |
|                       |                                                                      |   current row. For example, you could include two rows before and after the current   |
|                       |                                                                      |   row. To apply the default `frame_type=rows`, nothing needs to be added to the       |
|                       |                                                                      |   `windowcomp` stage syntax as it\'s automatically built into the query.              |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - `range`: Computes the window frame based on a logical range of rows around the      |
|                       |                                                                      |   current row, based on the current row's sort key value. The provided range value is |
|                       |                                                                      |   added or subtracted to the current row\'s key value to define a starting or ending  |
|                       |                                                                      |   range boundary for the window frame. Setting the `range` with start or end numeric, |
|                       |                                                                      |   nonzero boundaries requires using exactly one numeric type of sort field.           |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | <!-- -->                                                                              |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | - When setting `frame_type=range`, the `sort` must be included in the `windowcomp`    |
|                       |                                                                      |   stage syntax; otherwise, only `between null and null` is supported.                 |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |   This is unsupported:                                                                |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |       | windowcomp sum(field_a) between -2 and 0 frame_type = range                   |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |   Yet, the following is supported:                                                    |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |       | windowcomp sum(field_a) sort desc field_b between -1 and 1 frame_type = range |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |   Or                                                                                  |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |       | windowcomp sum(field_a) between null and null frame_type = range              |
+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Alias clause          | `[as <alias>]`                                                       | Use the `alias` clause to provide a column label (field name) for the `windowcomp`    |
|                       |                                                                      | results.                                                                              |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | When the new field name already exists in the schema, it\'s replaced with the new     |
|                       |                                                                      | name.                                                                                 |
|                       |                                                                      |                                                                                       |
|                       |                                                                      | If the `xdr_data` dataset already has a field in the schema called `existing_field`,  |
|                       |                                                                      | the new `existing_field` replaces the old one.                                        |
|                       |                                                                      |                                                                                       |
|                       |                                                                      |     dataset = xdr_data                                                                |
|                       |                                                                      |     | windowcomp sum(field_a) as existing_field                                       |
+-----------------------+----------------------------------------------------------------------+---------------------------------------------------------------------------------------+

##### Examples

Data table for ips dataset

The examples provided are based on the following data table for a
dataset called `ips`:

  -----------------------------------------------------------------------
  ip                      category                logins
  ----------------------- ----------------------- -----------------------
  192.168.10.1            pc                      23

  192.168.10.2            server                  2

  192.168.20.1            pc                      9

  192.168.20.4            server                  8

  192.168.20.5            pc                      2

  192.168.30.1            pc                      10
  -----------------------------------------------------------------------

Query 1: Compute the total logins for all IPs

    dataset = ips 
    | windowcomp sum(logins) as total_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          total_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            54

  192.168.20.5      2                 pc                54

  192.168.20.4      8                 server            54

  192.168.20.1      9                 pc                54

  192.168.30.1      10                pc                54

  192.168.10.1      23                pc                54
  -----------------------------------------------------------------------

Query 2: Compute a subtotal for each category

    dataset = ips 
    | windowcomp sum(logins) by category sort asc logins between null and null as total_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          total_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            10

  192.168.20.4      8                 server            10

  192.168.20.5      2                 pc                44

  192.168.20.1      9                 pc                44

  192.168.30.1      10                pc                44

  192.168.10.1      23                pc                44
  -----------------------------------------------------------------------

Query 3: Compute a cumulative sum for each category

The sum is computed with respect to the order defined using the `sort`
clause. These two queries produce the same results:

    dataset = ips 
    | windowcomp sum(logins) by category sort asc logins between null and 0 as total_logins

OR

    dataset = ips 
    | windowcomp sum(logins) by category sort asc logins between null as total_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          total_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            2

  192.168.20.4      8                 server            10

  192.168.20.5      2                 pc                2

  192.168.20.1      9                 pc                11

  192.168.30.1      10                pc                21

  192.168.10.1      23                pc                44
  -----------------------------------------------------------------------

Query 4: Compute a cumulative sum, where only preceding rows are
analyzed.

The analysis starts two rows before the current row in the partition.

    dataset = ips 
    | windowcomp sum(logins) sort asc logins between null and -2 as total_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          total_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            NULL

  192.168.20.5      2                 pc                NULL

  192.168.20.4      8                 server            2

  192.168.20.1      9                 pc                4

  192.168.30.1      10                pc                12

  192.168.10.1      23                pc                21
  -----------------------------------------------------------------------

Query 5: Compute a changing average

The lower boundary is 1 row before the current row. The upper boundary
is 1 row after the current row.

    dataset = ips 
    | windowcomp avg(logins) sort asc logins between -1 and 1 as avg_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          avg_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            2

  192.168.20.5      2                 pc                4

  192.168.20.4      8                 server            6.33333

  192.168.20.1      9                 pc                9

  192.168.30.1      10                pc                14

  192.168.10.1      23                pc                16.5
  -----------------------------------------------------------------------

Query 6: Retrieve the most popular IP in each category

Defines how rows in a window are partitioned and ordered in each
partition.

    dataset = ips 
    | windowcomp last_value(ip) by category sort asc logins between null and null as most_popular

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          most_popular
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            192.168.20.4

  192.168.20.4      8                 server            192.168.20.4

  192.168.20.5      2                 pc                192.168.10.1

  192.168.20.1      9                 pc                192.168.10.1

  192.168.30.1      10                pc                192.168.10.1

  192.168.10.1      23                pc                192.168.10.1
  -----------------------------------------------------------------------

Query 7: Calculate the rank of each IP within the category based on the
login

    dataset = ips 
    | windowcomp rank() by category sort asc logins as rank

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          rank
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            1

  192.168.20.4      8                 server            2

  192.168.20.5      2                 pc                1

  192.168.20.1      9                 pc                2

  192.168.30.1      10                pc                3

  192.168.10.1      23                pc                4
  -----------------------------------------------------------------------

Query 8: Retrieve the most popular IP in a specific window frame by
range and not category

The window frame analyzes up to three rows at a time.

    dataset = ips 
    | windowcomp last_value(ip) by category sort asc logins between -1 and 1 as most_popular

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          most_popular
  ----------------- ----------------- ----------------- -----------------
  192.168.10.2      2                 server            192.168.20.4

  192.168.20.4      8                 server            192.168.20.4

  192.168.20.5      2                 pc                192.168.20.1

  192.168.20.1      9                 pc                192.168.30.1

  192.168.30.1      10                pc                192.168.10.1

  192.168.10.1      23                pc                192.168.10.1
  -----------------------------------------------------------------------

Query 9: Retrieve the number of IPs that have similar logins

Count in range of -1 and 1 from their login value.

    dataset = ips | fields ip, category , logins 
    | windowcomp count() sort asc logins between -1 and 1 frame_type = range as similar_logins

Output results table

  -----------------------------------------------------------------------
  ip                logins            category          similar_logins
  ----------------- ----------------- ----------------- -----------------
  192.168.10.5      2                 pc                2

  192.168.10.2      2                 server            2

  192.168.20.4      8                 server            2

  192.168.20.1      9                 pc                3

  192.168.30.1      10                pc                2

  192.168.10.1      23                pc                1
  -----------------------------------------------------------------------

### Functions

Some Cortex Query Language (XQL) stages can call XQL functions to
convert the data to a desired format. For example, the `current_time()`
function returns the current timestamp, while the `extract_time()`
function can obtain the hour information in the timestamp. Functions may
or may not need input parameters. The `filter` and `alter` stages are
the two stages that can use functions for data transformations.

#### add

##### Syntax

    add (<string> | <integer>, <string> | <integer>)

##### Description

The `add()` function adds two positive integers. Parameters can be
either integer literals, or integers as a string type, such as might be
contained in a data field.

##### Example

    dataset = xdr_data 
    | alter mynum = add(action_file_size, 3) 
    | fields action_file_size, mynum 
    | filter action_file_size > 0 
    | limit 1 

#### approx_count

##### Syntax

    comp approx_count(<field>) [as <alias>] [by <field1>[,<field2>...]] [addrawdata = true|false [as <target field>]]

##### Description

The `approx_count` approximate aggregate is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that counts the number of distinct values in the given field over a
group of rows. For the group of rows, the function returns an
approximate result as a single interger value, for all records that
contain matching values for the fields identified in the `by` clause.
Use this approximate aggregate function to produce approximate results,
instead of exact results used with regular aggregate functions, which
are more scalable in terms of memory usage and time. This approximate
aggregate function is used in combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting addrawdata to either `true` or `false` (default), which are
used to configure the final comp results. When including raw data events
in your query, the query runs for up to 50 fields that you define and
displays up to 100 events.

##### Example

Returns a single integer value after approximately counting the number
of distinct values in the `event_id` field over a group of rows.

    dataset = xdr_data
    | fields event_id
    | comp approx_count(event_id)

#### approx_quantiles

##### Syntax

    comp approx_quantiles(<field>, <number>, <true|false>) [as <alias>] [by <field1>[,<field2>...]][addrawdata = true|false [as <target field>]]

##### Description

The `approx_quantiles` approximate aggregate is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
returns the approximate boundaries as a single value for a group of
distinct or non-distinct values (default `false`) for the specified
field over a group of rows, for all records that contain matching values
for the fields identified in the `by` clause. This function returns an
array of `<number>` + 1 elements, where the first element is the
approximate minimum and the last element is the approximate maximum. Use
this approximate aggregate function to produce approximate results,
instead of exact results used with regular aggregate functions, which
are more scalable in terms of memory usage and time. This approximate
aggregate function is used in combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

###### Distinct Values Example

Returns the approximate boundaries for a group of distinct values in the
`event_id` field.

    dataset = xdr_data
    | fields event_id
    | comp approx_quantiles(event_id, 100, true)

###### Non-Distinct Values Example

Returns the approximate boundaries for a group of non-distinct values in
the `event_id` field.

    dataset = xdr_data
    | fields event_id
    | comp approx_quantiles(event_id, 100)

#### approx_top

##### Syntax

###### comp approx_top as count

    comp approx_top(<string field>, <number>) [as <alias>] [by <field1>[,<field2>...]][addrawdata = true|false [as <target field>]] 

###### comp approx_top as sum

    comp approx_top(<string field>, <number>, <weight string field>) [as <alias>] [by <field1>[,<field2>...]][addrawdata = true|false [as <target field>]]

##### Description

The `approx_top` approximate aggregate is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that, depending on the number of parameters, returns either an
approximate count or sum of top elements. This approximate aggregate
function returns a single value for the given field over a group of
rows, for all records that contain matching values for the fields
identified in the `by` clause. This function is used in combination with
a `comp` stage. When a third parameter is specified, it references a
field that contains a numeric value (weight) that is used to calculate a
sum. The return value is an array with up to `<number>` of JSON strings.
Each string represents an object (struct) containing 2 keys and
corresponding values. The keys depend on whether a third parameter has
been supplied or not.

When defining `approx_top` to count and the third parameter is omitted,
each struct will have these keys: \"value\" and \"count\", where the
\"value\" specifies a unique field value and \"count\" specifies the
number of occurrences. When the third parameter is specified in
`approx_top`, it has to be a name of a field that contains a numeric
value that is used to calculate the final sum for each unique value in
the first specified field. Each struct in this case will have these
keys: \"value\" and \"sum\".

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

Use this approximate aggregate function to produce approximate results,
instead of exact results used with regular aggregate functions, which
are more scalable in terms of memory usage and time.

##### Examples

###### comp approx_top as count

Returns an approximate count of the top 10 agent IDs in the `agent_id`
field that appear the most frequently. The return value is an array
containing 10 JSON strings with a \"value\" and \"count\".

    dataset = xdr_data
    | fields agent_id
    | comp approx_top(agent_id, 10)

###### comp approx_top as sum

Returns an approximate sum of the top 10 agent IDs in the `agent_id`
field by their `action_session_duration`. The return value is an array
containing 10 JSON strings with a \"value\" and \"sum\" for each
`agent_id`.

    dataset = xdr_data
    | fields agent_id, action_session_duration
    | comp approx_top(agent_id, 10, action_session_duration)

#### array_all

##### Syntax

    array_all(<array>, "@element"<operator>"<array element>")

> **Note**
>
> The `<operator>` can be any of the ones supported, such as `=` and
> `!=`.

##### Description

The `array_all()` function returns `true` when all the elements in a
particular array match the condition in the specified array element.
Otherwise, the function returns `false`.

##### Example

When the `dfe_labels` array is not empty, use
the [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage to create a new
column called `x` that returns true when all the elements in the
`dfe_labels` array is equal to `network`; otherwise, the function
returns `false`.

    dataset = xdr_data
    | filter dfe_labels != null
    | alter x = array_all(dfe_labels , "@element" = "network")
    | fields x, dfe_labels
    | limit 100

#### array_any

##### Syntax

    array_any(<array>, "@element"<operator>"<array element>") 

> **Note**
>
> The `<operator>` can be any of the ones supported, such as `=` and
> `!=`.

##### Description

The `array_any()` function returns `true` when at least 1 element in a
particular array matches the condition in the specified array element.
Otherwise, the function returns `false`.

##### Example

When the `dfe_labels` array is not empty, use
the [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage to create a new
column called `x` that returns true when at least 1 element in the
`dfe_labels` array is equal to `network`; otherwise, the function
returns `false`.

    dataset = xdr_data
    | filter dfe_labels != null
    | alter x = array_any(dfe_labels , "@element" = "network")
    | fields x, dfe_labels
    | limit 100

#### arrayconcat

##### Syntax

    arrayconcat (<array1>,<array2>[,<array3>...])

##### Description

The `arrayconcat()` function accepts two or more arrays, and it joins
them into a single array.

##### Example

Given three arrays:

    first_array : [1,2,3]
    second_array : [44,55]
    third_array : [4,5,6] 

Using this query:

    alter all_arrays = arrayconcat(first_array, second_array, third_array)

Results in an `all_arrays` field containing:

    [1,2,3,44,55,4,5,6]

#### arraycreate

##### Syntax

    arraycreate ("<array element1>", "<array element2>",...)

##### Description

The `arraycreate()` function returns an array based on the given
parameters defined for the array elements.

##### Example

Returns a final array to a field called x that is comprised of the
elements \[1,2\].

    dataset = xdr_data
    | alter x = arraycreate("1", "2")
    | fields x

#### arraydistinct

##### Syntax

    arraydistinct (<array>)

##### Description

The `arraydistinct()` function accepts an array, and it returns a new
array containing only unique elements found in the original array. That
is, given the array:

    [0,1,1,1,4,5,5]

This function returns:

    [0,1,4,5]

#### arrayfilter

##### Syntax

    arrayfilter(<array>, <condition>)
    arrayfilter(<array>, "@element"<operator>"<array element>")

> **Note**
>
> The \<*operator*\> can be any of the ones supported, such as *=* and
> *!=*.

##### Description

The `arrayfilter()` function returns a new array with the elements which
meet the given condition. The function does this by filtering the
results of an array in one of the following ways:

- Returns the results when a certain condition is applied to the array.

- Returns the results when a particular array is set to a specified
  array element.

Though it\'s possible to define the `arrayfilter()` function with any
condition, the examples below focus on conditions using the `@element`
that are based on the current element being tested.

##### Basic Example

When the `dfe_labels` array is not empty, use the
[alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage to assign a value
to a field called `x` that returns the value of the `arrayfilter`
function. The `arrayfilter` function filters the `dfe_labels` array for
the array element set to `network`.

    dataset = xdr_data 
    | filter dfe_labels != null
    | alter x = arrayfilter(dfe_labels , "@element" = "network") 
    | fields x, dfe_labels 
    | limit 100 

##### Advanced Example

This queries below illustrate how to check whether any IPs are included
or not included in the blocked list called CIDRS. The Query Results
tables are also included to help explain what happens as the
`arrayfilter()` function is slightly modified.

###### Return Non-Matching CIDRS

This query returns results for each IP that don\'t match anything in the
CIDRS array blocked list:

    dataset = xdr_data
    | limit 1
    | alter cidrs = arraycreate("10.0.0.0/8","172.16.0.0/16"), ip = arraycreate("192.168.1.1", "172.16.20.18")
    | fields cidrs, ip
    | arrayexpand ip
    | alter non_matching_cidrs = arrayfilter(cidrs, ip not incidr "@element")

Results:

The following table details for each IP the logic that is first
performed before the final results for the query are displayed:

  -----------------------------------------------------------------------
  IP                      Statement               TRUE/FALSE
  ----------------------- ----------------------- -----------------------
  192.168.1.1             not in 10.0.0.0/8       TRUE

  192.168.1.1             not in 172.16.0.0/16    TRUE

  172.16.20.18            not in 10.0.0.0/8       TRUE

  172.16.20.18            not in 172.16.0.0/16    FALSE
  -----------------------------------------------------------------------

For each IP, an array of **CIDRS** is returned in the
**NON_MATCHING_CIDRS** column, which doesn\'t match the **CIDRS** array.
In addition, from the above table, `arrayfilter()` only returns anything
that resolves as TRUE. This explains the query results displayed in the
following table:

  -----------------------------------------------------------------------------
  IP                      CIDRS                      NON_MATCHING_CIDRS
  ----------------------- -------------------------- --------------------------
  192.168.1.1             10.0.0.0/8,172.16.0.0/16   10.0.0.0/8,172.16.0.0/16

  172.16.20.18            10.0.0.0/8,172.16.0.0/16   10.0.0.0/8
  -----------------------------------------------------------------------------

###### Return Matching CIDRS

Now, let\'s update the query to return results for each IP that match
anything in the CIDRS array:

    dataset = xdr_data
    | limit 1
    | alter cidrs = arraycreate("10.0.0.0/8","172.16.0.0/16"), ip = arraycreate("192.168.1.1", "172.16.20.18")
    | fields cidrs, ip
    | arrayexpand ip
    | alter matching_cidrs = arrayfilter(cidrs, ip incidr "@element")

Results:

The following table details for each IP the logic that is first
performed before the final results for the query are displayed:

  -----------------------------------------------------------------------
  IP                      Statement               TRUE/FALSE
  ----------------------- ----------------------- -----------------------
  192.168.1.1             in 10.0.0.0/8           FALSE

  192.168.1.1             in 172.16.0.0/16        FALSE

  172.16.20.18            in 10.0.0.0/8           FALSE

  172.16.20.18            in 172.16.0.0/16        TRUE
  -----------------------------------------------------------------------

For each IP, an array of **CIDRS** is returned in the **MATCHING_CIDRS**
column, which matches the **CIDRS** array. In addition, from the above
table, `arrayfilter()` only returns anything that resolves as TRUE. This
explains the query results displayed in the following table:

  --------------------------------------------------------------------------
  IP                      CIDRS                      MATCHING_CIDRS
  ----------------------- -------------------------- -----------------------
  192.168.1.1             10.0.0.0/8,172.16.0.0/16   empty array

  172.16.20.18            10.0.0.0/8,172.16.0.0/16   172.16.0.0/16
  --------------------------------------------------------------------------

#### arrayindex

##### Syntax

    arrayindex(<array>, <index>)

##### Description

The `arrayindex()` function returns the value contained in the specified
array position. Arrays are 0-based, and negative indexing is supported.

##### Examples

Use the [split](#UUIDb083e6971c7eeaed3f9287dcb32b6937) function to split
IP addresses into an array of octets. Return the 3rd octet contained in
the IP address.

    dataset = xdr_data 
    | fields action_local_ip  as alii 
    | alter ip_third_octet = arrayindex(split(alii, "."), 2) 
    | filter alii != null and alii != "0.0.0.0" 
    | limit 10 

#### arrayindexof

##### Syntax

    arrayindexof(<array>, <condition>)
    arrayindexof(<array>, "@element"<operator>"<array element>")

> **Note**
>
> The `<operator>` can be any of the ones supported, such as `=` and
> `!=`.

##### Description

The `arrayindexof()` function enables you to return a value related to
an array in one of the following ways.

- Returns 0 if a particular array is not empty and the specified
  condition is true. If the condition is not met, a NULL value is
  returned.

- Returns the 0-based index of a particular array element if a
  particular array is not empty and the specified condition using an
  `@element` is true. If the condition is not met, a NULL value is
  returned.

##### Examples

###### Condition

Use the [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage to assign a
value returned by the `arrayindexof` function to a field called `x`. The
`arrayindexof` function reviews the `dfe_labels` array and returns 0 if
the array is not empty and the `backtrace_identities` array contains
more than 1 element. Otherwise, a NULL value is assigned to the `x`
field.

    dataset in (xdr_data) 
    | alter x = arrayindexof(dfe_labels , array_length(backtrace_identities) > 1) 
    | fields x, dfe_labels 
    | limit 100 

###### \@Element

When the `dfe_labels` array is not empty, use the
[alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage to assign the
0-based index value returned by the `arrayindexof` function to a field
called `x`. The `arrayindexof` function reviews the `dfe_labels` array
and looks for the array element set to `network`. Otherwise, a NULL
value is assigned to the `x` field.

    dataset = xdr_data 
    | filter dfe_labels != null
    | alter x = arrayindexof(dfe_labels , "@element" = "network") 
    | fields x, dfe_labels 
    | limit 100 

#### array_length

##### Syntax

    array_length (<array>)

##### Description

The `array_length()` function returns the number of elements in an
array.

##### Example

    dataset = xdr_data 
    | fields action_local_ip as alii 
    | alter ip_len = array_length(split(alii, ".")) 
    | filter alii != null and alii != "0.0.0.0" 
    | limit 1

#### arraymap

##### Syntax

    arraymap (<array>, <function()>)

##### Description

The `arraymap()` function applies a specified function to every element
of an array. For functions that require a fieldname, use `"@element"`.

##### Examples

Extract the MAC address from the `agent_interface_map` field. This
example uses the
[json_extract_scalar](#UUIDecb1e8c53780d41f6cde0d5e85f70216),
[to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e),
[json_extract_array](#UUIDc0bcb6ff04b8c1e080b351616ef4c84f), and
[arraystring](#UUIDbd7ced12f277fa9c9b35a9d734d09cfa) functions to
extract the desired information.

    dataset = xdr_data 
    | alter mac = 
        arraystring (
            arraymap (
                json_extract_array (to_json_string(agent_interface_map),"$."),
                json_extract_scalar ("@element", "$.mac")
            ), ",")

#### arraymerge

##### Syntax

    arraymerge(<field>)

##### Description

The `arraymerge()` function returns an array, which is created from a
merge of the inner json-string arrays, including merging a number of
[arraymap()](#UUIDf05b2b4dca16124c82d35b07b7fb2ed2) function arrays.
This function accepts a single array of json-strings, which is the
`<field>` in the syntax.

##### Example 1

Returns a final array called `result` that is created from a merge of
the inner json-string arrays from array `x` and array `y` with the
values \[\"a\", \"b\", \"c\", \"d\"\].

    dataset = xdr_data  
    | alter x= to_json_string(arraycreate("a","b")), y = to_json_string(arraycreate("c","d"))
    | alter xy = arraycreate(x,y) 
    | alter xy=arraymerge(xy)

##### Example 2

Returns a final array that is created from a merge of the
[arraymap](#UUIDf05b2b4dca16124c82d35b07b7fb2ed2) by extracting the IP
address from the agent_interface_map field and the first IPV4 address
found in the first element of the `agent_interface_map` array. This
example uses the [to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e)
and [json_extract_array](#UUIDc0bcb6ff04b8c1e080b351616ef4c84f)
functions to extract the desired information.

    dataset = xdr_data
    | alter a =
    arraymerge (arraymap (agent_interface_map, to_json_string (json_extract_array (to_json_string("@element"), "$.ipv4") ) ) )

#### arrayrange

##### Syntax

    arrayrange (<array>, <start>, <end>)

##### Description

The `arrayrange()` function returns a portion, or a slice, of an array
given a start and end range. Indices are 0-based, and the start range is
inclusive, but the end range is exclusive.

##### Example

So if you have an array:

    [0,1,2,3,4,5,6]

and you specify:

    arrayrange(<array>, 2, 4)

the function will return:

    [2,3]

If you specify an end index that is higher than the last element in the
array, the resulting array contains the starting element to the end of
the array.

    arrayrange(<array>, 2, 8)

The function will return:

    [2,3,4,5,6]

#### arraystring

##### Syntax

    arraystring (<string>, <delimiter>)

##### Description

The `arraystring()` function returns a string from an array, where each
array element is joined by a defined delimiter.

##### Examples

Retrieve all `action_app_id_transitions` that are not null, combine each
array into a string where array elements are delimited by \" : \", and
then use [dedup](#UUID9ca262399c1d7020771dd7b5498cf3e7) the resulting
string.

    dataset = xdr_data 
    | fields action_app_id_transitions  as aait 
    | alter transitions_string = arraystring(aait, " : ") 
    | dedup transitions_string by asc _time 
    | filter aait != null

#### avg

##### Syntax

comp stage

    comp avg(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp avg(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

##### Description

The `avg()` function is used to return the average value of an integer
field over a group of rows. The function syntax and application is based
on the preceding stage:

comp stage

When the `avg` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single average value of an integer field
for a group of rows, for all records that contain matching values for
the fields identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `avg` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single average value of an integer field for each row in the
group of rows, for all records that contain matching values for the
fields identified using a combination of the `by` clause, `sort`, and
`between` window frame clause. The results are provided in a new column
in the results table.

##### Examples

comp example

Return a single average value of the `action_total_download` field for a
group of rows, for all records that have matching values for their
`actor_process_image_path` and `actor_process_command_line` values. The
query calculates a maximum of 100 `xdr_data` records and includes a
`raw_data` column listing a single value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp avg(Download) as average_download by Process_Path, Process_CMD
    addrawdata = true as raw_data

windowcomp example

Return the events that are above average per `Process_Path` and
`Process_CMD`. The query returns a maximum of 100 `xdr_data` records in
a column called `avg_download`.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | windowcomp avg(Download) by Process_Path, Process_CMD as avg_download
    | filter Download > avg_download

#### coalesce

##### Syntax

    coalesce (<field_1>, <field_2>,...<field_n>)

##### Description

The `coalesce()` function takes an arbitrary number of arguments and
returns the first value that is not NULL.

##### Example

Given a list of fields that contain usernames, select the first one that
is not `null` and display it in the `username` column.

    dataset = xdr_data 
    | fields actor_primary_username,
           os_actor_primary_username,
           causality_actor_primary_username 
    | alter username = coalesce(actor_primary_username,
                              os_actor_primary_username,
                              causality_actor_primary_username) 

#### concat

##### Syntax

    concat (<string1>, <string2>, ...)

##### Description

The `concat()` function joins multiple strings into a single string.
When using the `concat()` function with multiple fields and any of the
fields have a null/empty value, the function returns empty.

##### Example

Display the first non-NULL `action_boot_time` field value. In a second
column called `abt_string`, use the `concat()` function to prepend
\"str: \" to the value, and then display it.

    dataset = xdr_data 
    | fields action_boot_time as abt 
    | filter abt != null 
    | alter abt_string = concat("str: ", to_string(abt)) 
    | limit 1 

#### convert_from_base_64

##### Syntax

    convert_from_base_64("<base64-encoded input>")

##### Description

The `convert_from_base_64()` function converts the base64-encoded input
to the decoded string format.

##### Example

Returns the decoded string format `Hello world` from the base64-encoded
input `"SGVsbG8gd29ybGQ="`.

    convert_from_base_64("SGVsbG8gd29ybGQ=")

#### count

##### Syntax

comp stage

    comp count([<field>]) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp count([<field>]) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

##### Description

The `count()` function is used to return a single count for the number
of rows either for a field over a group of rows, where only the number
of non-null values found are returned, or without a field to count the
number of rows, including null values. The function syntax and
application is based on the preceding stage:

comp stage

When the `count` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns one of the following:

- With a field: Returns a single count for the number of non-null rows,
  for all records that contain matching values for the fields identified
  in the `by` clause.

- Without a field: Counts the number of rows and includes null values.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

Use
[/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f](/document/preview/892144#UUID-35c41b93-82ad-cbeb-8f5a-ec155f1aaa3f)
to retrieve the number of unique values in the result set.

windowcomp stage

When the `count` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns one of the following:

- With a field: Returns a single count for the number of non-null rows
  for all records that contain matching values for the fields identified
  using a combination of the `by` clause, `sort`, and `between` window
  frame clause. The results are provided in a new column in the results
  table.

- Without a field: Counts the number of rows and includes null values.

##### Examples

comp example

Return a single count of all values found for the
`actor_process_image_path` field in the group of rows, for all records
that have matching values for their `actor_process_image_path` and
`actor_process_command_line` values. The query calculates a maximum of
100 `xdr_data` records and includes a `raw_data` column listing a single
value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp count(Process_Path) as num_process_path by process_path, process_cmd addrawdata = true as raw_data
    | sort desc process_path

windowcomp example

Return a single count for the number of values found in the
`dns_query_name` field for each row in the group of rows, for all
records that contain matching values in the `agent_ip_addresses` field.
The query returns a maximum of 100 `xdr_data` records. The results are
provided in the `count_dns_query_name` column.

    dataset = xdr_data
    | limit 100
    | windowcomp count(dns_query_name) by agent_ip_addresses as count_dns_query_name

#### count_distinct

##### Syntax

    comp count_distinct(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata= true|false [as <target field>]]

##### Description

The `count_distinct` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns a single value for the number of unique values found for a
field over a group of rows, for all records that contain matching values
for the fields identified in the `by` clause. This aggregate function is
used in combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

Use
[/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9](/document/preview/892216#UUID-228ee005-77b6-0108-0a09-ffb5f8d0b9e9)
to retrieve the total number of values in the result set.

##### Examples

Return a single count of the number of unique values found for the
`actor_process_image_path` field over a group of rows, for all records
that have matching values for their `actor_process_image_path` and
`actor_process_command_line values`. The query calculates a maximum of
100 `xdr_data` records and includes a `raw_data` column listing the raw
data events used to display the final `comp` results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp count_distinct(Process_Path) as num_process_path by process_path, process_cmd addrawdata = true as raw_data
    | sort desc process_path

#### current_time

##### Syntax

    current_time()

##### Description

The `current_time()` function returns a timestamp value representing the
current time in the format `MMM dd YYYY HH:mm:ss`, such as
`Jul 12th 2023 20:51:34`.

##### Example

From the `xdr_data` dataset, returns the events of the last 24 hours
whose actor process started running more than 30 days ago.

    dataset = xdr_data
    | filter timestamp_diff(current_time(),to_timestamp(actor_process_execution_time, "MILLIS"), "DAY") > 30

#### date_floor

##### Syntax

    date_floor (<timestamp field>, "<time unit>" [, "<time zone>")

##### Description

The `date_floor()` function converts a timestamp value for a particular
field or function result that contains a number, and returns a timestamp
rounded down to the nearest whole value of a specified `<time unit>`,
including a year (y), month (mo), week (w), day (d), or hour (h). The
`<time zone>` offset is optional to configure using an hours offset,
such as "+08:00", or using a time zone name from the [List of Supported
Time
Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
such as \"America/Chicago\". When you do not configure a time zone, the
default is UTC.

##### Example

Returns a maximum of 100 `xdr_data` records with the events of the
`_time` field that are less than equal to a timestamp value. The
timestamp value undergoes a number of different function manipulations.
The current time is first rounded to the nearest whole value for the
week according to the America/Los_Angeles time zone. This timestamp
value is then converted to the Unix epoch timestamp format in seconds
and is added to the -2073600 Unix epoch time. This Unix epoch time value
in seconds is then converted to the final timestamp value that is used
to filter the `_time` fields and return the resulting records.

    dataset = xdr_data
    | filter _time < to_timestamp(add(to_epoch(date_floor(current_time(),"w", "America/Los_Angeles")),-2073600))
    | limit 100

#### divide

##### Syntax

    divide (<string> | <integer>, <string> | <integer>)

##### Description

The `divide()` function divides two positive integers. Parameters can be
either integer literals, or integers as a string type, such as might be
contained in a data field.

##### Example

    dataset = xdr_data 
    | alter mynum = divide(action_file_size, 3) 
    | fields action_file_size, mynum 
    | filter action_file_size > 3 
    | limit 1

#### earliest

##### Syntax

    comp earliest(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `earliest` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns the chronologically earliest value found for a field over a
group of rows that has matching values for the fields identified in the
`by` clause. This function is dependent on a time-related field, so for
your query to be considered valid, ensure that the dataset running this
query contains a time-related field. This function is used in
combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

Return the chronologically earliest timestamp found for any given
`action_total_download` value for all records that have matching values
for their `actor_process_image_path` and `actor_process_command_line`
fields. The query calculates a maximum of 100 `xdr_data` records and
includes a `raw_data` column listing the raw data events used to display
the final `comp` results.

    dataset = xdr_data
    | fields _time, actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp earliest(_time) as download_time by Process_Path, Process_CMD addrawdata = true as raw_data

#### extract_time

##### Syntax

    extract_time (<timestamp>, <part>)

##### Description

> **Important**
>
> The `extract_time` values are based on the GMT time, even if you\'ve
> adjusted the **Timezone** or **Timestamp Format** server settings as
> these configurations only affect how to display in Cortex XSIAM. For
> more information on the server settings, see [Configure server
> settings](#UUID438a8ca5fdec3ab6369be7ae1de6f037).

The `extract_time()` function returns a specified part of a timestamp.
The `part` parameter must be one of the following keywords:

- `DAY`

- `DAYOFWEEK`

- `DAYOFYEAR`

- `HOUR`

- `MICROSECOND`

- `MILLISECOND`

- `MINUTE`

- `MONTH`

- `QUARTER`

- `SECOND`

- `YEAR`

##### Example

    dataset = xdr_data 
    | alter timepart = extract_time(current_time(), "HOUR") 
    | fields timepart 
    | limit 1 

#### extract_url_host

##### Syntax

    extract_url_host ("<URL>")

##### Description

The `extract_url_host()` function returns the host of the URL. The
function always returns a value in lowercase characters even if the URL
provided contains uppercase characters.

##### Example

###### Output examples when using the function

Returns `paloaltonetworks.com` from the complete URL:
`https://www.paloaltonetworks.com`.

    extract_url_host ("https://www.paloaltonetworks.com")

Returns `a.b` for the URL: `//user:password@a.b:80/path?query`

    extract_url_host ("//user:password@a.b:80/path?query")

Returns `www.example.co.uk` in lowercase for the complete URL:
`www.Example.Co.UK`, which includes uppercase characters.

    extract_url_host ("www.Example.Co.UK")

Returns `www.test.paloaltonetworks.com` for the following URL containing
suffixes: `https://www.test.paloaltonetworks.com/suffix/another_suffix`

    extract_url_host ("https://www.test.paloaltonetworks.com/suffix/another_suffix")

###### Complete XQL Query Example

Returns one `xdr_data` record in the results table where the host of the
URL `https://www.test.paloaltonetworks.com` is listed in the `URL_HOST`
column as `www.test.paloaltonetworks.com`.

    dataset = xdr_data 
    | alter url_host = extract_url_host("https://www.test.paloaltonetworks.com") 
    | fields url_host 
    | limit 1

#### extract_url_pub_suffix

##### Syntax

    extract_url_pub_suffix ("<URL>")

##### Description

The `extract_url_pub_suffix()` function returns the public suffix of the
URL, such as com, org, or net. The function always returns a value in
lowercase characters even if the URL provided contains uppercase
characters.

##### Example

###### Output examples when using the function

Returns `com` for the following URL: `https://paloaltonetworks.com`

    extract_url_pub_suffix ("https://paloaltonetworks.com")

Returns `com` for the following URL containing suffixes:
`https://www.test.paloaltonetworks.com/suffix/another_suffix`

    extract_url_pub_suffix ("https://www.test.paloaltonetworks.com/suffix/another_suffix")

###### Complete XQL Query Example

Returns one `xdr_data` record in the results table where the public
suffix of the URL `https://www.paloaltonetworks.com` is listed in the
`URL_PUB_SUFFIX` column as `com`.

    dataset = xdr_data 
    | alter url_pub_suffix = extract_url_pub_suffix("https://paloaltonetworks.com") 
    | fields url_pub_suffix 
    | limit 1

#### extract_url_registered_domain

##### Syntax

    extract_url_registered_domain ("<URL>")

##### Description

The `extract_url_registered_domain()` function returns the registered
domain or registerable domain, the public suffix plus one preceding
label, of a URL. The function always returns a value in lowercase
characters even if the URL provided contains uppercase characters.

##### Examples

###### Output examples when using the function

Returns `paloaltonetworks.com` from the complete URL:
`https://www.paloaltonetworks.com`.

    extract_url_registered_domain ("https://www.paloaltonetworks.com")

Returns NULL for the URL: `//user:password@a.b:80/path?query`

    extract_url_registered_domain ("//user:password@a.b:80/path?query")

Returns `example.co.uk` in lowercase for the complete URL:
`www.Example.Co.UK`, which includes uppercase characters.

    extract_url_registered_domain ("www.Example.Co.UK")

Returns `paloaltonetworks.com` for the following URL containing
suffixes: `https://www.test.paloaltonetworks.com/suffix/another_suffix`

    extract_url_registered_domain ("https://www.test.paloaltonetworks.com/suffix/another_suffix")

###### Complete XQL query example

Returns one `xdr_data` record in the results table where the registered
domain of the URL `https://www.test.paloaltonetworks.com` is listed in
the `REGISTERED_DOMAIN` column as `paloaltonetworks.com`.

    dataset = xdr_data 
    | alter registered_domain = extract_url_registered_domain("https://www.test.paloaltonetworks.com") 
    | fields registered_domain 
    | limit 1

#### first

##### Syntax

    comp first(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `first` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns a single first value found for a field in the dataset over
a group of rows that has matching values for the fields identified in
the `by` clause. This function is dependent on a time-related field, so
for your query to be considered valid, ensure that the dataset running
this query contains a time-related field. This function is used in
combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

Return the first timestamp found in the dataset for any given
`action_total_download` value for all records that have matching values
for their `actor_process_image_path` and `actor_process_command_line`
fields. The query calculates a maximum of 100 `xdr_data` records and
includes a `raw_data` column listing the raw data events used to display
the final `comp` results.

    dataset = xdr_data
    | fields _time,actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp first(_time) as download_time by Process_Path, Process_CMD addrawdata = true as raw_data

#### first_value

##### Syntax

    windowcomp first_value(<field>) [by <field> [,<field>,...]] sort [asc|desc] <field1> [, [asc|desc] <field2>,...] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

##### Description

The `first_value()` function is a navigation function that is used in
combination with a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5)
stage. This function is used to return a single value of a field for the
first row of each row in the group of rows in the current window frame,
for all records that contain matching values for the fields identified
using a combination of the `by` clause, `sort` (mandatory), and
`between` window frame clause.

##### Example

Return the first IP address a user authenticated from successfully.

    preset = authentication_story
    | filter auth_identity not in (null, """""") and auth_outcome = """SUCCESS""" and action_country != UNKNOWN
    | alter et = to_epoch(_time), t = _time
    | bin t span = 1d
    | limit 100
    | windowcomp first_value(action_local_ip) by auth_identity, t sort asc et between null and null as first_action_local_ip
    | fields auth_identity , *action_local_ip

#### floor

##### Syntax

    floor (<number>)

##### Description

The `floor()` function converts a field that contains a number, and
returns an integer rounded down to the nearest whole number.

#### format_string

##### Syntax

    format_string("<format string>", <field_1>, <field_2>,...<field_n> )

##### Description

The `format_string()` function returns a string from a format string
that contains zero or more format specifiers, along with a variable
length list of additional arguments that matches the format specifiers.
A format specifier is initiated by the % symbol, and must map to one or
more of the remaining arguments. Usually, this is a one-to-one mapping,
except when the \* specifier is used.

##### Examples

- STRING

<!-- -->

- dataset = xdr_data 
      | alter stylished_action_category_appID = format_string("-%s-", action_category_of_app_id )
      | fields stylished_action_category_appID 
      | limit 100

<!-- -->

- Simple integer

<!-- -->

- dataset = xdr_data 
      | filter action_remote_ip_int != null
      | alter simple_int = format_string("%d", action_remote_ip_int)
      | fields simple_int 
      | limit 100

<!-- -->

- Integer with left blank padding

<!-- -->

- dataset = xdr_data 
      | filter action_remote_ip_int != null
      | alter int_with_left_blank = format_string("|%100d|", action_remote_ip_int)
      | fields int_with_left_blank 
      | limit 100

<!-- -->

- Integer with left zero padding

<!-- -->

- dataset = xdr_data 
      | filter action_remote_ip_int != null
      | alter int_with_left_zero_padding = format_string("+%0100d+", action_remote_ip_int)
      | fields int_with_left_zero_padding 
      | limit 100

#### format_timestamp

##### Syntax

    format_timestamp("<format string>", <timestamp field>)
    format_timestamp("<format string>", <timestamp field>, "<time zone>")

##### Description

The `format_timestamp()` function returns a string after formatting a
timestamp according to a specified string format. The `<time zone>` is
optional to configure using an hours offset, such as "+08:00", or using
a time zone name from the [List of Supported Time
Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
such as \"America/Chicago\". The `format_timestamp()` function should
include an [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage. For
more information, see the examples below.

**Examples**

- **Without a time zone configured**

<!-- -->

- Returns a maximum of 100 `xdr_data` records, which includes a string
  field called `new_time` in the format `YYYY/MM/dd HH:mm:ss`, such as
  2021/11/12 12:10:30. This format is detailed in the `format_timestamp`
  function, which defines retrieving the new_time (`%Y/%m/%d %H:%M:%S`)
  from the `_time` field.

      dataset = xdr_data
      | alter new_time = format_timestamp("%Y/%m/%d %H:%M:%S", _time) 
      | fields new_time 
      | limit 100

<!-- -->

- **With a time zone configured using an hours offset**

<!-- -->

- Returns a maximum of 100 `xdr_data` records, which includes a string
  field called new_time in the format YYYY/MM/dd HH:mm:ss, such as
  2021/11/12 01:53:35. This format is detailed in the `format_timestamp`
  function, which defines the retrieving the new_time
  (`%Y/%m/%d %H:%M:%S`) from the `_time` field and adding +03:00 hours
  as the time zone format.

      dataset = xdr_data  
      | alter new_time = format_timestamp("%Y/%m/%d %H:%M:%S", _time, "+03:00") 
      | fields new_time 
      | limit 100

<!-- -->

- **With a time zone name configured**

<!-- -->

- Returns a maximum of 100 `xdr_data` records, which includes a string
  field called `new_time` in the format `YYYY/MM/dd HH:mm:ss`, such as
  `2021/11/12 01:53:35`. This format is detailed in the
  `format_timestamp` function, which defines the retrieving the
  `new_time` (`%Y/%m/%d %H:%M:%S`) from the `_time` field, and includes
  an \"America/Chicago\" time zone.

      dataset = xdr_data 
      | fields _time
      | alter new_time = format_timestamp("%Y/%m/%d %H:%M:%S", _time, "America/Chicago")
      | fields new_time
      | limit 100

#### if

##### Syntax

Regular if statement

    if (<boolean expression>, <true return expression>[, <false return expression>])

Nested if/else statement

- if(<boolean expression1>, <true return expression1>, <boolean expression2>, <true return expression2>[, <boolean expression3>, <true return expression3>,...][, <false return expression>])

- if(<boolean expression1>, if(<boolean expression2>, <true return expression2> [,<false return expression2>])...[,<false return expression1>])

<!-- -->

- > **Note**

  > In the above
  > syntax,  `if(<boolean expression2>, <true return expression2> [,<false return expression2>])` represents
  > the `<true return expression1>`.

##### Description

The `if()` function evaluates a single expression or group of
expressions depending on the syntax used to define the function. The
syntax can be set up in the following ways:

- Regular if statement: A single boolean expression is evaluated. If the
  expression evaluates as `true`, the function returns the results
  defined in the second function argument. If the expression evaluates
  as `false` and a false return expression is defined, the function
  returns the results of the third function argument; otherwise, if no
  false return expression is set, returns null.

- Nested if/else statment: At least two boolean expressions and two true
  return expressions are required when using this option. The first
  boolean expression is evaluated. If the first expression evaluates as
  `true`, the function returns the results defined in the second
  function argument. The second boolean expression is evaluated. If the
  second expression evaluates as `true`, the function returns the
  results defined in the fourth function argument. If there are any
  other boolean expressions defined, they are evaluated following the
  same pattern when evaluated as `true`. If any of the expressions
  evaluates as `false` and a false return expression is defined, the
  function returns the results defined in the last function argument for
  the false return expression; otherwise, if no false return expression
  is set, returns null.

##### Examples

Regular if statement

If \'.exe\' is present on the `action_process_image_name` field value,
replace that substring with an empty string. This example uses the
[/document/preview/645242#UUID-461618d4-5593-409d-20a1-02db8b53e011](/document/preview/645242#UUID-461618d4-5593-409d-20a1-02db8b53e011)
and
[/document/preview/645232#UUID-3ca3f512-7ead-9756-42a9-6ecce7753b68](/document/preview/645232#UUID-3ca3f512-7ead-9756-42a9-6ecce7753b68)
functions, as well as the
[contains](/document/preview/645109#UUID-7613e92e-9180-95b2-c376-d6844ce46b47)
operator to perform the conditional check. When the \'.exe\' is not
present, the value is returned as is.

    dataset = xdr_data 
    | fields action_process_image_name as apin 
    | filter apin != null 
    | alter remove_exe_process = 
        if(lowercase(apin) contains ".exe",  // boolean expression
           replace(lowercase(apin),".exe",""), // return if true
           lowercase(apin))  // return if false
    | limit 10

Nested if/else statement

Return a maximum of 1 `xdr_data` record from the past 7 days. The table
results include a new column called `check_ip`, which evaluates and
returns the following:

- If the `action_local_ip` contains an IP address that begins with 10,
  return `Local 10`.

- If the `action_local_ip` contains an IP address that begins with 172,
  return `Local 172 ?`.

- If the `action_local_ip` contains an IP address that begins with
  192.168, return `Local 192`.

- If all the above expressions evaluate as `false`, return null.

<!-- -->

    config timeframe = 7d | dataset = xdr_data 
    | limit 1
    | alter 
        check_ip = if(action_local_ip ~= "^10",//boolean expression1
                   "Local 10", // true return expression1
                   action_local_ip ~= "^172", //boolean expression2
                   "Local 172 ?", //true return expression2
                   action_local_ip ~= "^192\.168", //boolean expression3
                   "Local 192") //true return expression3

#### incidr

##### Syntax

    incidr(<IPv4_address>, <CIDR1_range1> | <CIDR1_range1, CIDR2_range2, ...>)

##### Description

The `incidr()` function accepts an IPv4 address, and an IPv4 range or
comma separated IPv4 ranges using CIDR notation, and returns `true` if
the address is in range. Both the IPv4 address and CIDR ranges can be
either an explicit string using quotes (`""`), such as `"192.168.0.1"`,
or a string field.

> **Note**
>
> The first parameter must contain an IPv4 address contained in an IPv4
> field. For production purposes, this IPv4 address will normally be
> carried in a field that you retrieve from a dataset. For manual usage,
> assign the IPv4 address to a field, and then use that field with this
> function.

Multiple CIDRs are defined with comma separated syntax when building an
XQL query with the Query Builder or in Correlation Rules. When defining
multiple CIDRs, the logical `OR` is used between the CIDRS listed, so as
long as one address is in range the entire statement returns `true`.
Here are a few examples of how this logic works to determine whether the
`incidr()` function returns `true` and displays results or `false`,
where no results are displayed:

- Function returns `true` and results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "192.168.0.1" 
      | filter incidr(ip_address, "192.168.0.0/24, 1.168.0.0/24") = true

<!-- -->

- Function returns `false` and no results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "192.168.0.1" 
      | filter incidr(ip_address, "2.168.0.0/24, 1.168.0.0/24") = true

<!-- -->

- Function returns `false` and no results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "192.168.0.1" 
      | filter incidr(ip_address, "192.168.0.0/24, 1.168.0.0/24") = false

<!-- -->

- Function returns `true` and results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "192.168.0.1" 
      | filter incidr(ip_address, "2.168.0.0/24, 1.168.0.0/24") = false

> **Note**
>
> The same logic is used when using the `incidr` and `not incidr`
> operators. For more information, see [Supported
> operators](#UUIDf250f6fc117feefa485a8b5165cd7e32).

##### Examples

Return a maximum of 10 `xdr_data` records, if the IPV4 address
(`192.168.10.14`) is in range by verifying against a single CIDR
(`192.168.10.0/24`):

    alter my_ip = "192.168.10.14"
    | alter inrange = incidr(my_ip, "192.168.10.0/24")
    | fields inrange
    | limit 10
          

Return a maximum of 10 `xdr_data` records, if the IPV4 address
(`192.168.0.1`) is in range by verifying against multiple CIDRs
(`192.168.0.0/24` or `1.168.0.0/24`):

    dataset = xdr_data 
    | alter ip_address = "192.168.0.1" 
    | filter incidr(ip_address, "192.168.0.0/24, 1.168.0.0/24") = true 
    | limit 10

#### incidr6

##### Syntax

    incidr6(<IPv6_address>, <CIDR1_range1> | <CIDR1_range1, CIDR2_range2, ...>)

##### Description

The `incidr6()` function accepts an IPv6 address, and an IPv6 range or
comma separated IPv6 ranges using CIDR notation, and returns `true` if
the address is in range. Both the IPv6 address and CIDR ranges can be
either an explicit string using quotes (`""`), such as
`"3031:3233:3435:3637:3839:4041:4243:4445"`, or a string field.

> **Note**
>
> The first parameter must contain an IPv6 address contained in an IPv6
> field. For production purposes, this IPv6 address will normally be
> carried in a field that you retrieve from a dataset. For manual usage,
> assign the IPv6 address to a field, and then use that field with this
> function.

Multiple CIDRs are defined with comma separated syntax when building an
XQL query with the Query Builder or in Correlation Rules. When defining
multiple CIDRs, the logical `OR` is used between the CIDRS listed, so as
long as one address is in range the entire statement returns `true`.
Here are a few examples of how this logic works to determine whether the
`incidr6()` function returns `true` and displays results or `false`,
where no results are displayed:

- Function returns `true` and results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "3031:3233:3435:3637:3839:4041:4243:4445" 
      | filter incidr(ip_address, "3031:3233:3435:3637:0000:0000:0000:0000/64, 6081:6233:6435:6637:0000:0000:0000:0000/64") = true

<!-- -->

- Function returns `false` and no results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "3031:3233:3435:3637:3839:4041:4243:4445" 
      | filter incidr(ip_address, "6081:6233:6435:6637:0000:0000:0000:0000/64, 7081:7234:7435:7737:0000:0000:0000:0000/64, fe80::/10") = true

<!-- -->

- Function returns `false` and no results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "3031:3233:3435:3637:3839:4041:4243:4445" 
      | filter incidr(ip_address, "3031:3233:3435:3637:0000:0000:0000:0000/64, 7081:7234:7435:7737:0000:0000:0000:0000/64, fe80::/10") = false

<!-- -->

- Function returns `true` and results are displayed:

<!-- -->

- dataset = test 
      | alter ip_address = "3031:3233:3435:3637:3839:4041:4243:4445" 
      | filter incidr(ip_address, "6081:6233:6435:6637:0000:0000:0000:0000/64, 7081:7234:7435:7737:0000:0000:0000:0000/64, fe80::/10") = false

> **Note**
>
> The same logic is used when using the `incidr6` and `not incidr6`
> operators. For more information, see [Supported
> operators](#UUIDf250f6fc117feefa485a8b5165cd7e32).

##### Example

Return a maximum of 10 `xdr_data` records, if the IPV6 address
(`3031:3233:3435:3637:3839:4041:4243:4445`) is in range by verifying
against a single CIDR (`3031:3233:3435:3637:0000:0000:0000:0000/64`):

    alter my_ip = "3031:3233:3435:3637:3839:4041:4243:4445"
    | alter inrange = incidr6(my_ip, "3031:3233:3435:3637:0000:0000:0000:0000/64")
    | fields inrange
    | limit 10

Return a maximum of 10 `xdr_data` records, if the IPV6 address
(`3031:3233:3435:3637:3839:4041:4243:4445`) is in range by verifying
against multiple CIDRs (`2001:0db8:85a3:0000:0000:8a2e:0000:0000/64` or
`fe80::/10`):

    dataset = xdr_data 
    | alter ip_address = "fe80::1" 
    | filter incidr6(ip_address, "2001:0db8:85a3:0000:0000:8a2e:0000:0000/64, fe80::/10") = true 
    | limit 10

#### incidrlist

##### Syntax

    incidrlist(<IP_address list>, <CIDR_range>)

##### Description

The `incidrlist()` function accepts a string containing a
comma-separated list of IP addresses, and an IP range using CIDR
notation, and returns `true` if all the addresses are in range.

##### Examples

Return `true` if the list of IP addresses fall within the specified IP
range. Note that the input type is a comma-separated list of IP
addresses, and not an array of IP addresses.

    alter inrange = incidrlist("192.168.10.16,192.168.10.3", 
                               "192.168.10.0/24")
    | fields inrange
    | limit 1
          

If you want to evaluate a true array of IP addresses, convert the array
to a comma-separated list using
[arraystring()](#UUIDbd7ced12f277fa9c9b35a9d734d09cfa). For example,
using the `pan_ngfw_traffic_raw` dataset:

    dataset = panw_ngfw_traffic_raw 
    | filter dest_ip != null
    | comp values(dest_ip) as dips by source_ip,action
    | alter dips = arraystring(dips, ", ")
    | alter inrange = incidrlist(dips, "192.168.10.0/24")
    | fields source_ip, action, dips, inrange
    | limit 100

#### int_to_ip

##### Syntax

    int_to_ip(<IPv4_integer>)

##### Description

The `int_to_ip()` function tries to safely convert a signed integer
representation of an IPv4 address into its string equivalent.

##### Examples

Returns the IPv4 address \"4.130.58.140\" from the integer
representation of the IPv4 address provided as 75643532.

    int_to_ip(75643532)

Returns the IPv4 address \"251.125.197.116\" from the integer
representation of the IPv4 address provided as -75643532.

    int_to_ip(-75643532)

#### ip_to_int

##### Syntax

    ip_to_int(<IPv4_address>)

> **Note**
>
> This function was previously called `safe_ip_to_int()` and was renamed
> to `ip_to_int()`.

##### Description

The `ip_to_int()` function tries to safely convert a string
representation of an IPv4 address into its integer equivalent.

##### Example

Returns the integer 808530483 from the string representation of the IPv4
address provided as \"48.49.50.51\".

    ip_to_int("48.49.50.51")

#### is_ipv4

##### Syntax

    is_ipv4(<IPv4_address>)

##### Description

The `is_ipv4()` function accepts a string, and returns `true` if the
string is a valid IPv4 address. The IPv4 address can be either an
explicit string using quotes (`""`), such as `"192.168.0.1"`, or a
string field.

> **Note**
>
> The `<IPv4_address>` must contain an IPv4 address in an IPv4 field.
> For production purposes, this IPv4 address will normally be carried in
> a field that you retrieve from a dataset. For manual usage, assign the
> IPv4 address to a field, and then use that field with this function.

##### Example

Data table for ips_test_raw dataset

The example provided is based on the following data table for a dataset
called `ips_test_raw`:

  ----------------------------------------------------------------------------
  \_TIME            IP                     \_VENDOR          \_PRODUCT
  ----------------- ---------------------- ----------------- -----------------
  Mar 26th 2025     1.1.1.1                ips               test
  19:26:07                                                   

  Mar 26th 2025     192.168.1.100          ips               test
  19:26:07                                                   

  Mar 26th 2025     FF0E::1                ips               test
  19:26:07                                                   

  Mar 26th 2025     127.0.0.1              ips               test
  19:26:07                                                   

  Mar 26th 2025     172.32.0.1             ips               test
  19:26:07                                                   

  Mar 26th 2025     2606:4700:4700::1111   ips               test
  19:26:07                                                   
  ----------------------------------------------------------------------------

Query: Filter the IPv4 addresses

    dataset = ips_test_raw
    | alter IsIpv4 = is_ipv4(ip)
    | filter IsIpv4

Output results table

Returns all the IPv4 addresses from the `ip` field in the `ips_test_raw`
dataset. When the `is_ipv4` function returns `true`, the results are
displayed with a new **IsIpv4** column (field) indicating a **true**
value. If the function returns `false`, no results are returned.

  ---------------------------------------------------------------------------
  \_TIME         IP              \_VENDOR       \_PRODUCT      ISIPV4
  -------------- --------------- -------------- -------------- --------------
  Mar 26th 2025  1.1.1.1         ips            test           true
  19:26:07                                                     

  Mar 26th 2025  192.168.1.100   ips            test           true
  19:26:07                                                     

  Mar 26th 2025  127.0.0.1       ips            test           true
  19:26:07                                                     

  Mar 26th 2025  172.32.0.1      ips            test           true
  19:26:07                                                     
  ---------------------------------------------------------------------------

#### is_known_private_ipv4

##### Syntax

    is_known_private_ipv4(<IPv4_address>)

##### Description

The `is_known_private_ipv4()` function accepts an IPv4 address, and
returns `true` if the IPv4 string address belongs to any of the
following known set of private network IPs:

- 10.0.0.0/8

- 172.16.0.0/12

- 192.168.0.0/16

The IPv4 address can be either an explicit string using quotes (`""`),
such as `"192.168.0.1"`, or a string field.

> **Note**
>
> The `<IPv4_address>` must contain an IPv4 address in an IPv4 field.
> For production purposes, this IPv4 address will normally be carried in
> a field that you retrieve from a dataset. For manual usage, assign the
> IPv4 address to a field, and then use that field with this function.

##### Example

Data table for ips_test_raw dataset

The example provided is based on the following data table for a dataset
called `ips_test_raw`:

  ----------------------------------------------------------------------------
  \_TIME            IP                     \_VENDOR          \_PRODUCT
  ----------------- ---------------------- ----------------- -----------------
  Mar 26th 2025     1.1.1.1                ips               test
  19:26:07                                                   

  Mar 26th 2025     192.168.1.100          ips               test
  19:26:07                                                   

  Mar 26th 2025     FF0E::1                ips               test
  19:26:07                                                   

  Mar 26th 2025     127.0.0.1              ips               test
  19:26:07                                                   

  Mar 26th 2025     172.32.0.1             ips               test
  19:26:07                                                   

  Mar 26th 2025     2606:4700:4700::1111   ips               test
  19:26:07                                                   
  ----------------------------------------------------------------------------

Query: Filter the IPv4 addresses belonging to a set of known private
network IPs

    dataset = ips_test_raw
    | alter IsKnownPrivateIpv4 = is_known_private_ipv4(ip)
    | filter IsKnownPrivateIpv4

Output results table

Returns all the IPv4 addresses that belong to a set of known private
network IPs from the `ip` field in the `ips_test_raw` dataset. When the
`is_known_private_ipv4` function returns `true`, the results are
displayed with a new **IsKnownPrivateIpv4** column (field) indicating a
**true** value. If the function returns `false`, no results are
returned.

  ---------------------------------------------------------------------------------
  \_TIME         IP              \_VENDOR       \_PRODUCT      ISPKNOWNRIVATEIPV4
  -------------- --------------- -------------- -------------- --------------------
  Mar 26th 2025  192.168.1.100   ips            test           true
  19:26:07                                                     

  ---------------------------------------------------------------------------------

#### is_ipv6

##### Syntax

    is_ipv6(<IPv6_address>)

##### Description

The `is_ipv6()` function accepts a string, and returns `true` if the
string is a valid IPv6 address. The IPv6 address can be either an
explicit string using quotes (`""`), such as
`"3031:3233:3435:3637:3839:4041:4243:4445"`, or a string field.

> **Note**
>
> The `<IPv6_address>` must contain an IPv6 address in an IPv6 field.
> For production purposes, this IPv6 address will normally be carried in
> a field that you retrieve from a dataset. For manual usage, assign the
> IPv6 address to a field, and then use that field with this function.

##### Example

Data table for ips_test_raw dataset

The example provided is based on the following data table for a dataset
called `ips_test_raw`:

  ----------------------------------------------------------------------------
  \_TIME            IP                     \_VENDOR          \_PRODUCT
  ----------------- ---------------------- ----------------- -----------------
  Mar 26th 2025     1.1.1.1                ips               test
  19:26:07                                                   

  Mar 26th 2025     192.168.1.100          ips               test
  19:26:07                                                   

  Mar 26th 2025     FF0E::1                ips               test
  19:26:07                                                   

  Mar 26th 2025     127.0.0.1              ips               test
  19:26:07                                                   

  Mar 26th 2025     172.32.0.1             ips               test
  19:26:07                                                   

  Mar 26th 2025     2606:4700:4700::1111   ips               test
  19:26:07                                                   
  ----------------------------------------------------------------------------

Query: Filter the IPv6 addresses

    dataset = ips_test_raw
    | alter IsIpv6 = is_ipv6(ip)
    | filter IsIpv6

Output results table

Returns all the IPv6 addresses from the `ip` field in the `ips_test_raw`
dataset. When the `is_ipv6` function returns `true`, the results are
displayed with a new **IsIpv6** column (field) indicating a **true**
value. If the function returns `false`, no results are returned.

  ----------------------------------------------------------------------------------
  \_TIME         IP                     \_VENDOR       \_PRODUCT      ISIPV6
  -------------- ---------------------- -------------- -------------- --------------
  Mar 26th 2025  FF0E::1                ips            test           true
  19:26:07                                                            

  Mar 26th 2025  2606:4700:4700::1111   ips            test           true
  19:26:07                                                            
  ----------------------------------------------------------------------------------

#### is_known_private_ipv6

##### Syntax

    is_known_private_ipv6(<IPv6_address>)

##### Description

The `is_known_private_ipv6()` function accepts an IPv6 address, and
returns `true` if the IPv6 string address belongs to any of the
following known set of private network IPs:

- FC00::/7

- FD00::/7

The IPv6 address can be either an explicit string using quotes (`""`),
such as `"3031:3233:3435:3637:3839:4041:4243:4445"`, or a string field.

> **Note**
>
> The `<IPv6_address>` must contain an IPv6 address in an IPv6 field.
> For production purposes, this IPv6 address will normally be carried in
> a field that you retrieve from a dataset. For manual usage, assign the
> IPv6 address to a field, and then use that field with this function.

##### Example

Data table for ips_test_raw dataset

The example provided is based on the following data table for a dataset
called `ips_test_raw`:

  ----------------------------------------------------------------------------
  \_TIME            IP                     \_VENDOR          \_PRODUCT
  ----------------- ---------------------- ----------------- -----------------
  Mar 26th 2025     FC00::1                ips               test
  19:26:07                                                   

  Mar 26th 2025     192.168.1.100          ips               test
  19:26:07                                                   

  Mar 26th 2025     FF0E::1                ips               test
  19:26:07                                                   

  Mar 26th 2025     127.0.0.1              ips               test
  19:26:07                                                   

  Mar 26th 2025     172.32.0.1             ips               test
  19:26:07                                                   

  Mar 26th 2025     2606:4700:4700::1111   ips               test
  19:26:07                                                   
  ----------------------------------------------------------------------------

Query: Filter the IPv6 addresses belonging to a set of known private
network IPs

    dataset = ips_test_raw
    | alter IsKnownPrivateIpv6 = is_known_private_ipv6(ip)
    | filter IsKnownPrivateIpv6

Output results table

Returns all the IPv6 addresses that belong to a set of known private
network IPs from the `ip` field in the `ips_test_raw` dataset. When the
`is_known_private_ipv6` function returns `true`, the results are
displayed with a new **IsKnownPrivateIpv6** column (field) indicating a
**true** value. If the function returns `false`, no results are
returned.

  --------------------------------------------------------------------------------
  \_TIME         IP             \_VENDOR       \_PRODUCT      ISKNOWNPRIVATEIPV6
  -------------- -------------- -------------- -------------- --------------------
  Mar 26th 2025  FC00::1        ips            test           true
  19:26:07                                                    

  --------------------------------------------------------------------------------

#### json_extract

> **Important**
>
> Before using this JSON function, it\'s important that you understand
> how Cortex XSIAM treats a JSON in the Cortex Query Language. For more
> information, see [JSON
> functions](#UUIDc0f2174a3c1a9cacf7a7f2707aa1a59f).

##### Syntax

###### Regular Syntax

    json_extract(<json_object_formatted_string>, <json_path>)

When a field in the \<json_path\> contains characters, such as a dot (.)
or colon (:), use the syntax:

    json_extract(<json_object_formatted_string>, "['<json_field>']")

###### Syntactic Sugar Format

To make it easier for you to write your XQL queries, you can also use
the following syntactic sugar format.

    <json_object_formatted_string> -> <json_path>{}

When a field in the `<json_path>` contains characters, such as a dot (.)
or colon (:), use the syntax:

    <json_object_formatted_string> -> ["<json_field>"]{}

##### Description

The `json_extract()` function extracts inner JSON objects by retrieving
the value from the identified field. The returned datatype is always a
string. If the input string does not represent a JSON object, this
function fails to parse. To convert a string field to a JSON object, use
the [to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e) function.

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.
>
> **Note**
>
> The field value is always returned as a string. To return the scalar
> values, which are not an object or an array, use
> [json_extract_scalar](#UUIDecb1e8c53780d41f6cde0d5e85f70216).

##### Examples

Return the `storage_device_name` value from the
`action_file_device_info` field.

    dataset = xdr_data 
    | fields action_file_device_info as afdi 
    | alter sdn = json_extract(to_json_string(afdi), "$.storage_device_name") 
    | filter afdi != null

Using Syntactic Sugar Format

The same example above with a syntactic sugar format.

    dataset = xdr_data
    | fields action_file_device_info as afdi
    | alter sdn = to_json_string(afdi)->storage_device_name{}
    | filter afdi != null

#### json_extract_array

> **Important**
>
> Before using this JSON function, it\'s important that you understand
> how Cortex XSIAM treats a JSON in the Cortex Query Language. For more
> information, see [JSON
> functions](#UUIDc0f2174a3c1a9cacf7a7f2707aa1a59f).

##### Syntax

###### Regular Syntax

    json_extract_array(<json_array_string>, <json_path>)

When a field in the `<json_path>` contains characters, such as a dot (.)
or colon (:), use the syntax:

    json_extract_array(<json_array_string>, "['<json_field>']")

###### Syntactic Sugar Format

To make it easier for you to write your XQL queries, you can also use
the following syntactic sugar format.

    <json_array_string> -> <json_path>[]

When a field in the `<json_path>` contains characters, such as a dot (.)
or colon (:), use the syntax:

    <json_array_string> -> ["<json_field>"][]

##### Description

The `json_extract_array()` function accepts a string representing a JSON
array, and returns an XQL-native array. To convert a string field to a
JSON object, use the
[to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e) function.

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.

##### Examples

###### Regular Syntax

Extract the first IPV4 address found in the first element of the
`agent_interface_map` array.

    dataset = xdr_data 
    | fields agent_interface_map as aim 
    | alter ipv4 = json_extract_array(to_json_string(arrayindex(aim, 0)) , "$.ipv4") 
    | filter aim != null 
    | limit 10

###### Syntactic Sugar Format

The same example above with a syntactic sugar format.

    dataset = xdr_data
    | fields agent_interface_map as aim
    | alter ipv4 = to_json_string(aim)->[0].ipv4[0]
    | filter aim != null
    | limit 10

#### json_extract_scalar

> **Important**
>
> Before using this JSON function, it\'s important that you understand
> how Cortex XSIAM treats a JSON in the Cortex Query Language. For more
> information, see [JSON
> functions](#UUIDc0f2174a3c1a9cacf7a7f2707aa1a59f).

##### Syntax

###### Regular Syntax

    json_extract_scalar(<json_object_formatted_string>, <field_path>)

When a field in the `<json_path>` contains characters, such as a dot (.)
or colon (:), use the syntax:

    json_extract_scalar(<json_object_formatted_string>, "['<json_field>']")

###### Syntactic Sugar Format

To make it easier for you to write your XQL queries, you can also use
the following syntactic sugar format:

    <json_object_formatted_string> -> <field_path>

When a field in the `<json_path>` contains characters, such as a dot (.)
or colon (:), use the syntax:

    <json_object_formatted_string> -> ["<json_field>"]

##### Description

The `json_extract_scalar()` function accepts a string representing a
JSON object, and it retrieves the value from the identified field as a
string. This function always returns a string. If the JSON field is an
object or array, it will return a null value. To retrieve an XQL-native
datatype, use an appropriate function, such as `to_float` or
`to_integer`. If the input string does not represent a JSON object, this
function fails to parse. To convert a string field to a JSON object, use
the [to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e) function.

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.

##### Examples

Return the `storage_device_drive_type` value from the
`action_file_device_info` field, and return the record if it is 1.

There are two ways that you can build this query either with a filter
using an XQL-native datatype or string.

Option A - Filter using an XQL-native datatype

    dataset = xdr_data 
    | fields action_file_device_info as afdi 
    | alter sdn = to_integer(json_extract_scalar(to_json_string(afdi), "$.storage_device_drive_type")) 
    | filter sdn = 1 
    | limit 10

Option B - Filter using a string

    dataset = xdr_data 
    | fields action_file_device_info as afdi 
    | alter sdn = json_extract_scalar(to_json_string(afdi), "$.storage_device_drive_type") 
    | filter sdn = "1" 
    | limit 10

Using Syntactic Sugar Format

The same example above with a syntactic sugar format.

    dataset = xdr_data
    | fields action_file_device_info as afdi
    | alter sdn = to_integer(to_json_string(afdi)->storage_device_drive_type)
    | filter sdn = 1
    | limit 10

#### json_extract_scalar_array

> **Important**
>
> Before using this JSON function, it\'s important that you understand
> how Cortex XSIAM treats a JSON in the Cortex Query Language. This
> function doesn\'t have a syntatic sugar format. For more information,
> see [JSON functions](#UUIDc0f2174a3c1a9cacf7a7f2707aa1a59f).

##### Syntax

    json_extract_scalar_array(<json_array_string>, <json_path>)

> **Important**
>
> When a Cortex Data Model (XDM) field is used in the `<json_path>` and
> contains a dot (`.`) character, such as `xdm.source.host.device_id`,
> use the syntax:

    json_extract_scalar_array(<json_array_string>, "['<json_field>']")

> All other characters in the `<json_path>`, such as colon (`:`), should
> be escaped as it\'s an invalid JSON path, and are currently
> unsupported.

##### Description

The `json_extract_scalar_array()` function accepts a string representing
a JSON array, and returns an XQL-native array. This function is
equivalent to the
[json_extract_array](#UUIDc0bcb6ff04b8c1e080b351616ef4c84f) except that
the final output isn\'t displayed in double quotes (\"\...\"). To
convert a string field to a JSON object, use the
[to_json_string](#UUID3b6e4928c1f843a531328bb522b1b31e) function.

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.

##### Examples

Dataset query example

Extract the first IPV4 address found in the first element of the
`agent_interface_map` array. The values of the IPv4 addresses in the
array will not contain any double quotes.

    dataset = xdr_data 
    | fields agent_interface_map as aim 
    | alter ipv4 = json_extract_scalar_array(to_json_string(arrayindex(aim, 0)) , "$.ipv4") 
    | filter aim != null 
    | limit 10

Final output with 1 row from the results table. Notice that the IPV4
column doesn\'t contain any double quotes (`" "`) around the IP address
`172.16.15.42`:

  ---------------------------------------------------------------------------------------------------------------------------------------------
  \_TIME      AIM                                                                     \_PRODUCT   \_VENDOR    INSERT_TIMESTAMP   IPV4
  ----------- ----------------------------------------------------------------------- ----------- ----------- ------------------ --------------
  Aug 9th     `[{"ipv4":["172.16.15.42"], "ipv6": [], "mac": "00:50:56:9f:30:a9"}]`   XDR agent   PANW        Aug 17th 2023      172.16.15.42
  2023                                                                                                        19:25:48           
  10:04:39                                                                                                                       

  ---------------------------------------------------------------------------------------------------------------------------------------------

In contrast, compare the above results to the same query using the
`json_extract_array()` function. The final output with the same row from
the results table has in the IPV4 column the IP address in double quotes
`"172.16.15.42"`.

  -------------------------------------------------------------------------------------------------------------------------------------------------
  \_TIME      AIM                                                                     \_PRODUCT   \_VENDOR    INSERT_TIMESTAMP   IPV4
  ----------- ----------------------------------------------------------------------- ----------- ----------- ------------------ ------------------
  Aug 9th     `[{"ipv4":["172.16.15.42"], "ipv6": [], "mac": "00:50:56:9f:30:a9"}]`   XDR agent   PANW        Aug 17th 2023      \"172.16.15.42\"
  2023                                                                                                        19:25:48           
  10:04:39                                                                                                                       

  -------------------------------------------------------------------------------------------------------------------------------------------------

XDM example

Extract the `xdm.file.permissions.owner` in the
`xdm.finding.normalized_fields` array, which returns true when the
string value is one of the following: `r` or `w`.

    dataset = findings 
    | filter JSON_EXTRACT_SCALAR_ARRAY(xdm.finding.normalized_fields, "$['xdm.file.permissions.owner']") in ("r", "w") 
    | fields xdm.finding.normalized_fields

Output results:

+-----------------------------------+----------------------------------------+
| \_TIME                            | XDM.FINDING.NORMALIZED_FIELDS          |
+===================================+========================================+
| Jan 15th 2025 09:10:44            |     {  "xdm.file.permissions.owner": [ |
|                                   |         "r",                           |
|                                   |         "w",                           |
|                                   |         "x"                            |
|                                   |       ]                                |
|                                   |     }                                  |
+-----------------------------------+----------------------------------------+

#### json_path_extract

> **Important**

- > The `<json_path>` referred to in this JSON function contains new
  > options that aren\'t available in the other Cortex Query Language
  > (XQL) JSON functions as explained in
  > [/document/preview/1090614#UUID-bd36eadb-1561-9157-7ff8-32c3e4cec961](/document/preview/1090614#UUID-bd36eadb-1561-9157-7ff8-32c3e4cec961).
  > For more information on the `<json_path>` used in this function, see
  > [JSONPath - XPath for
  > JSON](https://goessner.net/articles/JsonPath/).

- > Be aware that using this function can be very heavy as it requires a
  > lot of resources to run.

##### Syntax

###### Regular Syntax

    json_path_extract(<json_field>, <json_path>)

###### Syntactic Sugar Format

To make it easier for you to write your XQL queries, you can also use
the following syntactic sugar format:

- Using triple quotes:

<!-- -->

- <json_field> ->-> """<json_path>"""

<!-- -->

- Using single quotes:

<!-- -->

- <json_field> ->-> "<json_path>"

##### Description

The `json_path_extract()` function extracts values from the JSON as
defined in the `<json_path>`. This function always returns a string. The
syntax used in this function is based on what\'s used in JavaScript as
explained in the [jsonpath
package](https://www.npmjs.com/package/jsonpath).

> **Important**
>
> JSON field names are case sensitive, so the key to field pairing must
> be identical in an XQL query for results to be found. For example, if
> a field value is `"TIMESTAMP"` and your query is defined to look for
> \"timestamp\", no results will be found.

##### Examples

Defines a JSON object called `Firewall`, which is contained in the JSON
file called `json_field`, to extract different string fields called `a`,
`b`, `c`, `d`, `e`, `f`, `g`, `h`, and `i`. This example illustrates
many different ways you can use the `json_path_extract` function to
extract data. Here are how the different fields are configured in the
example below to extract data:

- `a`: Outputs all of the values for the `author` key in
  the `ServerAccessConfig` JSON array as displayed in column A of the
  query output below.

- `b`: Outputs all of the values for the `author` key, where the value
  for the `priority` key is `22.99` as displayed in column B of the
  query output below.

- `c`: Outputs all of the values for the `author` key anywhere found in
  the JSON as displayed in column C of the query output below.

- `d`: Outputs  all of the values under the `Firewall` key as displayed
  in column D of the query output below.

- `e`: Outputs all of the values under the `Firewall` key for
  the `priority` key as displayed in column E of the query output below.

- `f`: Outputs the JSON array Index value from
  the `ServerAccessConfig` JSON array according to its index location
  from the end of the array as displayed in column F of the query output
  below.

- `g`: Outputs all of the JSON array Index values from
  the `ServerAccessConfig` JSON array according to its index location
  from the end of the array as displayed in column G of the query output
  below.

- `h`: Outputs a specific set of JSON array index values (one or more)
  from the `ServerAccessConfig` JSON array according to its index
  location as displayed in column H of the query output below.

- `i`: Outputs all of the JSON array Index values from
  the `ServerAccessConfig` JSON array according to its index location
  from the start (0 Index) to the mentioned index value as displayed in
  column I of the query output below.

<!-- -->

    dataset = xdr_data | limit 1 
    | alter 
        json_field = "{\"Firewall\": {\"ServerAccessConfig\": [{\"category\": \"policy\",\"author\": \"NRees\",\"name\": \"CustomerSuccess_NoAccess\",\"priority\": 8.95},{\"category\": \"rule\",\"author\": \"EWaugh\",\"name\": \"AllowAccess_10_10_10_10\",\"id\": \"0-553-21311-3\",\"priority\": 12.99},{\"category\": \"policy\",\"author\": \"HMelville\",\"name\": \"SOC_Access\",\"priority\": 8.99},{\"category\": \"rule\",\"author\": \"JTolkien\",\"name\": \"AllowAccess_JIT\",\"id\": \"0-395-19395-8\",\"priority\": 22.99}],\"Reviewer\": {\"UserName\": \"jdow\",\"Role\": \"Admin\"}}}"
    | alter a = json_path_extract(json_field, "$.Firewall.ServerAccessConfig[*].author") 
    | alter b = json_path_extract(json_field, "$..*[?(@.priority==22.99)].author") 
    | alter c = json_path_extract(json_field, "$..author") 
    | alter d = json_path_extract(json_field, "$.Firewall.*") 
    | alter e = json_path_extract(json_field, "$.Firewall..priority") 
    | alter f = json_path_extract(json_field, "$..ServerAccessConfig[(@.length-1)]") 
    | alter g = json_path_extract(json_field, "$..ServerAccessConfig[-1:]") 
    | alter h = json_path_extract(json_field, "$..ServerAccessConfig[0,1]") 
    | alter i = json_path_extract(json_field, "$..ServerAccessConfig[:2]")
    | fields json_field, a, b, c, d, e, f, g, h, i

**Sample output of query**

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th>_TIME</th>
<th>JSON_FIELD</th>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
<th>E</th>
<th>F</th>
<th>G</th>
<th>H</th>
<th>I</th>
<th>_PRODUCT</th>
<th>_VENDOR</th>
<th>INSERT_TIMESTAMP</th>
</tr>
</thead>
<tbody>
<tr>
<td>Jan 20th 2025 18:51:42</td>
<td><pre><code>{  &quot;Firewall&quot;: { 
   &quot;ServerAccessConfig&quot;: [ 
     { 
       &quot;category&quot;: &quot;policy&quot;,
        &quot;author&quot;: &quot;NRees&quot;,
        &quot;name&quot;: &quot;CustomerSuccess_NoAccess&quot;, 
       &quot;priority&quot;: 8.95
      },
      {
        &quot;category&quot;: &quot;rule&quot;,
        &quot;author&quot;: &quot;EWaugh&quot;,
        &quot;name&quot;: &quot;AllowAccess_10_10_10_10&quot;,
        &quot;id&quot;: &quot;0-553-21311-3&quot;,
        &quot;priority&quot;: 12.99
      },
      {
        &quot;category&quot;: &quot;policy&quot;,
        &quot;author&quot;: &quot;HMelville&quot;,
        &quot;name&quot;: &quot;SOC_Access&quot;,
        &quot;priority&quot;: 8.99
      },
      {
        &quot;category&quot;: &quot;rule&quot;, 
       &quot;author&quot;: &quot;JTolkien&quot;,
        &quot;name&quot;: &quot;AllowAccess_JIT&quot;,
        &quot;id&quot;: &quot;0-395-19395-8&quot;, 
       &quot;priority&quot;: 22.99
      }
    ],
    &quot;Reviewer&quot;: {
      &quot;UserName&quot;: &quot;jdow&quot;,
      &quot;Role&quot;: &quot;Admin&quot;
    }  }}</code></pre></td>
<td>NRees, EWaugh, HMelville, JTolkien</td>
<td>JTolkien</td>
<td>NRees, EWaugh, HMelville ,JTolkien</td>
<td><pre><code>{ 
   &quot;ServerAccessConfig&quot;: [ 
     { 
       &quot;category&quot;: &quot;policy&quot;,
        &quot;author&quot;: &quot;NRees&quot;,
        &quot;name&quot;: &quot;CustomerSuccess_NoAccess&quot;, 
       &quot;priority&quot;: 8.95
      },
      {
        &quot;category&quot;: &quot;rule&quot;,
        &quot;author&quot;: &quot;EWaugh&quot;,
        &quot;name&quot;: &quot;AllowAccess_10_10_10_10&quot;,
        &quot;id&quot;: &quot;0-553-21311-3&quot;,
        &quot;priority&quot;: 12.99
      },
      {
        &quot;category&quot;: &quot;policy&quot;,
        &quot;author&quot;: &quot;HMelville&quot;,
        &quot;name&quot;: &quot;SOC_Access&quot;,
        &quot;priority&quot;: 8.99
      },
      {
        &quot;category&quot;: &quot;rule&quot;, 
       &quot;author&quot;: &quot;JTolkien&quot;,
        &quot;name&quot;: &quot;AllowAccess_JIT&quot;,
        &quot;id&quot;: &quot;0-395-19395-8&quot;, 
       &quot;priority&quot;: 22.99
      }
    ],
    &quot;Reviewer&quot;: {
      &quot;UserName&quot;: &quot;jdow&quot;,
      &quot;Role&quot;: &quot;Admin&quot;
    }  }</code></pre></td>
<td>8.95, 12.99, 8.99, 22.99</td>
<td><pre><code>[ 
 {
    &quot;category&quot;: &quot;rule&quot;,
    &quot;author&quot;: &quot;JTolkien&quot;,
    &quot;name&quot;: &quot;AllowAccess_JIT&quot;,
    &quot;id&quot;: &quot;0-395-19395-8&quot;,
    &quot;priority&quot;: 22.99
  }
]</code></pre></td>
<td><pre><code>[
  {
    &quot;category&quot;: &quot;rule&quot;,
    &quot;author&quot;: &quot;JTolkien&quot;,
    &quot;name&quot;: &quot;AllowAccess_JIT&quot;,
    &quot;id&quot;: &quot;0-395-19395-8&quot;,
    &quot;priority&quot;: 22.99
  }
]</code></pre></td>
<td><pre><code>[
  {
    &quot;category&quot;: &quot;policy&quot;,
    &quot;author&quot;: &quot;NRees&quot;,
    &quot;name&quot;: &quot;CustomerSuccess_NoAccess&quot;,
    &quot;priority&quot;: 8.95
  },
  {
    &quot;category&quot;: &quot;rule&quot;,
    &quot;author&quot;: &quot;EWaugh&quot;,
    &quot;name&quot;: &quot;AllowAccess_10_10_10_10&quot;,
    &quot;id&quot;: &quot;0-553-21311-3&quot;,
    &quot;priority&quot;: 12.99
  }
]</code></pre></td>
<td><pre><code>[
  {
    &quot;category&quot;: &quot;policy&quot;,
    &quot;author&quot;: &quot;NRees&quot;,
    &quot;name&quot;: &quot;CustomerSuccess_NoAccess&quot;,
    &quot;priority&quot;: 8.95  },
  {
    &quot;category&quot;: &quot;rule&quot;,
    &quot;author&quot;: &quot;EWaugh&quot;,
    &quot;name&quot;: &quot;AllowAccess_10_10_10_10&quot;,
    &quot;id&quot;: &quot;0-553-21311-3&quot;,
    &quot;priority&quot;: 12.99
  }
]</code></pre></td>
<td>Fusion</td>
<td>PANW</td>
<td>Jan 20th 2025 19:09:12</td>
</tr>
</tbody>
</table>

#### lag

##### Syntax

    windowcomp lag(<field>) [by <field> [,<field>,...]] sort [asc|desc] <field1> [, [asc|desc] <field2>,...] [as <alias>]

##### Description

The `lag()` function is a navigation function that is used in
combination with a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5)
stage. This function is used to return a single value of a field on a
preceding row for each row in the group of rows using a combination of
the `by` clause and `sort` (mandatory).

##### Example

Retrieve for each event the timestamp of the previous successful login
since the last one.

    preset = authentication_story
    | filter auth_identity not in (null, """""") and auth_outcome = """SUCCESS"""
    | alter ep = to_epoch(_time)
    | limit 100
    | windowcomp lag(_time) by auth_identity sort asc ep as previous_login

#### last

##### Syntax

    comp last(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `last` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns the last value found for a field in the dataset over a
group of rows that has matching values for the fields identified in the
`by` clause. This function is dependent on a time-related field, so for
your query to be considered valid, ensure that the dataset running this
query contains a time-related field. This function is used in
combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

Return the last timestamp found in the dataset for any given
`action_total_download` value for all records that have matching values
for their `actor_process_image_path` and `actor_process_command_line`
fields. The query calculates a maximum of 100 `xdr_data` records and
includes a `raw_data` column listing the raw data events used to display
the final `comp` results.

    dataset = xdr_data
    | fields _time, actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp last(_time) as download_time by Process_Path, Process_CMD addrawdata = true as raw_data

#### last_value

##### Syntax

    windowcomp last_value(<field>) [by <field> [,<field>,...]] sort [asc|desc] <field1> [, [asc|desc] <field2>,...] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

##### Description

The `last_value()` function is a navigation function that is used in
combination with a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5)
stage. This function is used to return a single value of a field for the
last row of each row in the group of rows in the current window frame,
for all records that contain matching values for the fields identified
using a combination of the `by` clause, `sort` (mandatory), and
`between` window frame clause.

##### Example

Return the last IP address a user authenticated from successfully.

    preset = authentication_story
    | filter auth_identity not in (null, """""") and auth_outcome = """SUCCESS""" and action_country != UNKNOWN
    | alter et = to_epoch(_time), t = _time
    | bin t span = 1d
    | limit 100
    | windowcomp last_value(action_local_ip) by auth_identity, t sort asc et between null and null as first_action_local_ip
    | fields auth_identity , *action_local_ip

#### latest

##### Syntax

    comp latest(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `latest` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns a single chronologically latest value found for a field
over a group of rows that has matching values for the fields identified
in the `by` clause. This function is dependent on a time-related field,
so for your query to be considered valid, ensure that the dataset
running this query contains a time-related field. This function is used
in combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

Return the chronologically latest timestamp found for any given
`action_total_download` value for all records that have matching values
for their `actor_process_image_path` and `actor_process_command_line`
fields. The query calculates a maximum of 100 `xdr_data` records and
includes a `raw_data` column listing the raw data events used to display
the final `comp` results.

    dataset = xdr_data
    | fields _time, actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp latest(_time) as download_time by Process_Path, Process_CMD addrawdata = true as raw_data

#### len

##### Syntax

    len (<string>)

##### Description

The `len()` function returns the number of characters contained in a
string.

##### Examples

Show domain names that are more than 100 characters in length.

    dataset = xdr_data 
    | fields dns_query_name 
    | filter len(dns_query_name) > 100 
    | limit 10 

#### list

##### Syntax

    comp list(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `list` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns a single array of up to 100 values found for a given field
over a group of rows, for all records that contain matching values for
the fields identified in the `by` clause. The array values are all
non-null, so null values are filtered out. The values returned in the
array are non-unique, so if a value repeats multiple times it is
included as part of the list of up to 100 values. This function is used
in combination with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Examples

Return an array containing up to 100 values seen for the
`action_total_download` field over a group of rows, for all records that
have matching values for their `actor_process_image_path` and
`actor_process_command_line` values. The query calculates a maximum of
100 `xdr_data` records and includes a `raw_data` column listing the raw
data events used to display the final `comp` results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download Download
    | filter Download > 0
    | limit 100
    | comp list(Download) as list_download by Process_Path, Process_CMD addrawdata = true as raw_data

#### lowercase

##### Syntax

    lowercase (<string>)

##### Description

The `lowercase()` function converts a string field value to all
lowercase.

##### Examples

Convert all `actor_process_image_name` field values that are not null to
lowercase, and return a list of unique values.

    dataset = xdr_data 
    | fields actor_process_image_name as apin 
    | dedup apin by asc _time 
    | filter apin != null 
    | alter apin = lowercase(apin)

#### ltrim, rtrim, trim

##### Syntax

    trim (<string>,[trim_characters])
    rtrim (<string>,[trim_characters])
    ltrim (<string>,[trim_characters])

##### Description

- The `trim()` function removes all instances of the specified
  `trim_characters` defined in the second parameter of the function from
  the beginning and end of the string defined in the first parameter of
  the function.

- The `rtrim()` function removes all instances of the specified
  `trim_characters` defined in the second parameter of the function from
  the end of the string defined in the first parameter of the function.

- The `ltrim()` function removes all instances of the specified
  `trim_characters` defined in the second parameter of the function from
  the beginning of the string defined in the first parameter of the
  function.

Keep in mind the following important points before using these
functions, where relevant examples are provided:

- The specified `trim_characters` do not need to be in any order.

<!-- -->

- Either of these yield the same result:

      rtrim("explorer.exe", ".ex")

      rtrim("explorer.exe", ".exe")

      rtrim("explorer.exe", "x.e")

  Output result:

      "explorer"

<!-- -->

- trim_characters don\'t support regular expressions or escape
  characters.

<!-- -->

- ltrim("***a*aapple*", "*a")

  Output results:

      "pple*"

<!-- -->

- All occurrences of the `trim_characters` supplied are removed from
  left to right until it reaches a letter that is not part of the
  supplied letters.

<!-- -->

- ltrim("hello world", "leh")

  Output results:

      "o world"

<!-- -->

- A space in the string can also be considered a character.

- The `ltrim()`, `rtrim()`, and `trim()` functions are case sensitive
  unless there is an override.

<!-- -->

- ltrim("***a*aapple*", "*A")

  Output results:

      "a*aapple*"

<!-- -->

- If you do not specify `trim_characters`, then whitespace (spaces and
  tabs) are removed.

<!-- -->

- ltrim("  apple*")

  Output results:

      "apple*"

##### Examples

A complete query example, where the output results of each `ltrim()`,
`rtrim()`, and `trim()` function is detailed in the comments.

    config timeframe = 1w | dataset = xdr_data
    | limit 1
    | alter
        example_1 = rtrim("explorer.exe", "x.e"), // ---> "explorer"
        example_2 = ltrim("hello world", "leh"), // ---> "o world"
        example_3 = trim("  apple*  ", " "), // ---> "apple*"
        example_4 = ltrim("***a*aapple*", "*A") // ---> "a*aapple*"
    | fields example*

#### max

##### Syntax

comp stage

    comp max(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp max(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

##### Description

The `max()` function is used to return the maximum value of an integer
field over a group of rows. The function syntax and application is based
on the preceding stage:

comp stage

When the `max` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single maximum value of an integer field
for a group of rows, for all records that contain matching values for
the fields identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `max` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single maximum value of an integer field for each row in the
group of rows, for all records that contain matching values for the
fields identified using a combination of the `by` clause, `sort`, and
`between` window frame clause. The results are provided in a new column
in the results table.

##### Examples

comp example

Return a single maximum value of the `action_total_download` field for a
group of rows, for all records that have matching values for their
`actor_process_image_path` and `actor_process_command_line` values. The
query calculates a maximum of 100 `xdr_data` records and includes a
`raw_data` column listing a single value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp max(Download) as max_download by Process_Path, Process_CMD addrawdata = true as raw_data

windowcomp example

Return the last login time. The query returns a maximum of 100
`authentication_story` records in a column called `action_user_agent`.

    preset = authentication_story
    | limit 100
    | windowcomp max(_time) by action_user_agent

#### median

##### Syntax

comp stage

    comp median(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp median(<field>) [by <field> [,<field>,...]] [as <alias>] 

##### Description

The `median()` function is used to return the median value of a field
over a group of rows. The function syntax and application is based on
the preceding stage:

comp stage

When the `median` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single median value of a field for a group
of rows, for all records that contain matching values for the fields
identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `median` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single median value of a field for each row in the group of
rows, for all records that contain matching values for the fields
identified in the `by` clause. In a median function, the `sort` and
`between` window frame clause are not used. The results are provided in
a new column in the results table.

##### Examples

comp example

Return a single median value of the `action_total_download` field over a
group of rows, for all records that have matching values for their
`actor_process_image_path` and `actor_process_command_line` values. The
query calculates a maximum of 100 `xdr_data` records and includes a
`raw_data` column listing a single value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp median(Download) as median_download by Process_Path, Process_CMD
    addrawdata = true as raw_data

windowcomp example

Return all events where the `Download` field is greater than the median
by reviewing each individual event and how it compares to the median.
The query returns a maximum of 100 `xdr_data` records in a column called
`median_download`.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | windowcomp median(Download) by Process_Path, Process_CMD as median_download
    | filter Download > median_download 

#### min

##### Syntax

comp stage

    comp min(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp min(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

##### Description

The `min()` function is used to return the minimum value of an integer
field over a group of rows. The function syntax and application is based
on the preceding stage:

comp stage

When the `min` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single minimum value of an integer field
for a group of rows, for all records that contain matching values for
the fields identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `min` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single minimum value of an integer field for each row in the
group of rows, for all records that contain matching values for the
fields identified using a combination of the by clause, sort, and
between window frame clause. The results are provided in a new column in
the results table.

##### Examples

comp example

Return a single minimum value of the `action_total_download` field for a
group of rows, for all records that have matching values for their
`actor_process_image_path` and `actor_process_command_line` values. The
query calculates a maximum of 100 `xdr_data` records and includes a
`raw_data` column listing a single value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp min(Download) as min_download by Process_Path, Process_CMD addrawdata = true as raw_data

windowcomp example

Return the first login time. The query returns a maximum of 100
`authentication_story` records in a column called `action_user_agent`.

    preset = authentication_story
    | limit 100
    | windowcomp min(_time) by action_user_agent

#### multiply

##### Syntax

    multiply (<string> | <integer>, <string> | <integer>)

##### Description

The `multiply()` function multiplies two positive integers. Parameters
can be either integer literals, or integers as a string type such as
might be contained in a data field.

##### Example

    dataset = xdr_data 
    | alter mynum = multiply(action_file_size, 3) 
    | fields action_file_size, mynum 
    | filter action_file_size > 0 
    | limit 1

#### object_create

##### Syntax

    object_create ("<key1>", "<value1>", "<key2>", "<value2>",...)

##### Description

The `object_create()` function returns an object based on the given
parameters defined for the key and value pairs. Accepts n \> 1 even
number of parameters.

##### Example

Returns a final object to a field called `a` that contains the key and
value pair `{“2”:“password”}`, where the \"password\" value is comprised
by joining 2 values together.

    dataset = xdr_data
    | alter a = object_create("2", concat("pass", "word"))
    | fields a

#### object_merge

##### Syntax

    object_merge(<obj1>, <obj2>, <obj3>, ...)

##### Description

The `object_merge()` function returns a new object, which is created
from a merge of a number of objects. When there is a key name that is
duplicated in any of the objects, the value in the new object is
determined by the latter argument.

##### Example

Two objects are created and merged, where some key names are duplicated,
including `name`, `last_name`, and `age`. Since the `name` value is the
same for both objects, the same name is used in the new object. Yet, the
`last_name` and `age` key values differ, so the values from the second
object are used in the new object.

    dataset = xdr_data
    | alter
      obj1 = object_create("name", "jane", "last_name", "doe", "age", 33),
      obj2 = object_create("name", "jane", "last_name", "simon", "age", 34, "city", "new-york")
    | alter result = object_merge(obj1, obj2)
    | fields result

The function returns the following new object in the **RESULT** column
of the results table:

    {"name": "jane", "last_name": "simon", "age": 34, "city": "new-york"}

#### parse_epoch

##### Syntax

    parse_epoch("<format string>", <timestamp field>[, "<time zone>",] ["<time unit>"])

##### Description

The `parse_epoch()` function returns a Unix epoch TIMESTAMP object after
converting a string representation of a timestamp. The `<time zone>`
offset is optional to configure using an hours offset, such as "+08:00",
or using a time zone name from the [List of Supported Time
Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
such as \"America/Chicago\". When you do not configure a timezone, the
default is `UTC`. The `<time unit>` is optional to configure and
indicates whether the Unix epoch integer value represents seconds,
milliseconds, or microseconds. These values are supported, and the
default is used when none is configured:

- SECONDS (default)

- MILLIS

- MICROS

> **Important**
>
> The order of the `<time zone>` and `<time unit>` matters. The
> `<time zone>` must be defined first followed by the `<time unit>`. If
> the `<time zone>` is set after the `<time unit>`, the default time
> zone is used and the configured value is ignored.

##### Examples

- With a time zone configured:

<!-- -->

- Returns a maximum of 100 `xdr_data` records, which includes a
  timestamp field called `new_time` in the format
  `MMM dd YYYY HH:mm:ss`, such as `Dec 25th 2008 04:30:00`. This
  `new_time` field is comprised by taking a character string
  representation of a timestamp \"Thu Dec 25 07:30:00 2008\" and adding
  to it +03:00 hours as the time zone format. This string timestamp is
  then converted to a Unix epoch TIMESTAMP object in milliseconds using
  the `parse_epoch` function, and this resulting value is converted to
  the final timestamp using the
  [to_timestamp](#UUIDe0ead2f8b9ce2f1663e62f44842a933e) function.

      dataset = xdr_data
      | alter new_time = to_timestamp(parse_epoch("%c", "Thu Dec 25 07:30:00 2008", "+3", "millis"))
      | fields new_time
      | limit 100

<!-- -->

- Without a time zone or time unit configured:

<!-- -->

- Returns a maximum of 100 `xdr_data` records, which includes a
  timestamp field called `new_time` in the format
  `MMM dd YYYY HH:mm:ss`, such as `Dec 25th 2008 04:30:00`. This
  `new_time` field is comprised by taking a character string
  representation of a timestamp \"Thu Dec 25 07:30:00 2008\" and adding
  to it a UTC time zone format (default when none configured). This
  string timestamp is then converted to a Unix epoch TIMESTAMP object in
  seconds (default when none configured) using the `parse_epoch`
  function, and this resulting value is converted to the final timestamp
  using the [to_timestamp](#UUIDe0ead2f8b9ce2f1663e62f44842a933e)
  function.

      dataset = xdr_data
      | alter new_time = to_timestamp(parse_epoch("%c", "Thu Dec 25 07:30:00 2008"))
      | fields new_time
      | limit 100

#### parse_timestamp

##### Syntax

    parse_timestamp("<format time string>", "<time string>" | format_string(<time field>) | <time string field>)
    parse_timestamp("<format time string>", "<time string>" | format_string(<time field>) | <time string field>, "<time zone>")

##### Description

The `parse_timestamp()` function returns a TIMESTAMP object after
converting a string representation of a timestamp. The `<time zone>`
offset is optional to configure using an hours offset, such as "+08:00",
or using a time zone name from the [List of Supported Time
Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
such as \"America/Chicago\". The `parse_timestamp()` function can
include both an [alter](#UUID29adfeb71cc64bb046509f7b4089e1b5) stage and
[format_string](#UUID14386a0ee575919e2f8bacb7d2251d88) function. For
more information, see the examples below. The `format_string` function
contains the format elements that define how the `parse_timestamp`
string is formatted. Each element in the `parse_timestamp` string must
have a corresponding element in `format_string`. The location of each
element in the `format_string` must match the location of each element
in `parse_timestamp`.

##### Examples

- **Without a time zone configured**

<!-- -->

- Returns a maximum of 100 `microsoft_dhcp_raw` records, which includes
  a TIMESTAMP object in the `p_t_test` field in the format MMM dd YYYY
  HH:mm:ss, such as Jun 25th 2021 18:31:25. This format is detailed in
  the `format_string` function, which includes merging both the `date`
  and `time` fields.

      dataset = microsoft_dhcp_raw 
      | alter p_t_test = parse_timestamp("%m/%d/%Y %H:%M:%S", format_string("%s %s", date, time)) 
      | fields p_t_test 
      | limit 100

<!-- -->

- **With a time zone name configured**

<!-- -->

- Returns a maximum of 100 `microsoft_dhcp_raw` records, which includes
  a TIMESTAMP object in the `p_t_test` field in the format MMM dd YYYY
  HH:mm:ss, such as Jun 25th 2021 18:31:25. This format is detailed in
  the `format_string` function, which includes merging both the `date`
  and `time` fields, and includes a \"Asia/Singapore\" time zone.

      dataset = microsoft_dhcp_raw 
      | alter p_t_test = parse_timestamp("%m/%d/%Y %H:%M:%S", format_string("%s %s", date, time), "Asia/Singapore") 
      | fields p_t_test 
      | limit 100

<!-- -->

- **With a time zone configured using an hours offset**

<!-- -->

- Returns a maximum of 100 `microsoft_dhcp_raw` records, which includes
  a TIMESTAMP object in the `p_t_test` field in the format MMM dd YYYY
  HH:mm:ss, such as Jun 25th 2021 18:31:25. This format is detailed in
  the `format_string` function, which includes merging both the `date`
  and `time` fields, and includes a time zone using an hours offset of
  \"+08:00\".

      dataset = microsoft_dhcp_raw 
      | alter p_t_test = parse_timestamp("%m/%d/%Y %H:%M:%S", format_string("%s %s", date, time), "+08:00") 
      | fields p_t_test 
      | limit 100

<!-- -->

- **Convert a time string that contains milliseconds**

<!-- -->

- Returns a single `xdr_data` record, which includes both, a manually
  added time string, \"Jun 25 2024 18:31:25.723\", in the `time_string`
  field and a TIMESTAMP object in the `p_t_test` field, such as Jun 25
  2024 18:31:25, as the result of the `parse_timestamp()` function.
  Notice that the format element `%E*S` is used to capture seconds
  including any level of factional precision, such as milliseconds.

      dataset = xdr_data  
      | limit 1
      | alter time_string = "Jun 25 2024 18:31:25.723"
      | alter p_t_test = parse_timestamp("%h %d %Y %H:%M:%E3S", time_string) 
      | fields p_t_test, time_string  

#### pow

##### Syntax

    pow (<x,n>)

##### Description

The `pow()` function returns the value of a number (`x`) raised to the
power of another number (`n`).

#### rank

##### Syntax

    windowcomp rank() [by <field> [,<field>,...]] sort [asc|desc] <field1> [, [asc|desc] <field2>,...] [as <alias>]

##### Description

The `rank()` function is a numbering function that is used in
combination with a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5)
stage. This function is used to return a single value for the ordinal
(1-based) rank for each row in the group of rows using a combination of
the `by` clause and `sort` (mandatory).

##### Example

Return an average ranking for the avgerage CPU usage on
`metric_type=HOST`. Allows you to see changes in the CPU usage compared
to all hosts in the environment. The query returns a maximum of 100
`it_metrics` records. The results are ordered by `ft` in decending order
in the `rank` column.

      dataset = it_metrics
    | filter metric_type = HOST
    | alter cpu_avg_str = to_string(cpu_avg)
    | alter ft = date_floor(_time, "w")
    | alter dt = date_floor(_time, "d")
    | limit 100
    | windowcomp rank() by ft sort desc cpu_avg_str as rank
    | filter (agent_hostname contains $host_name)
    | comp avg(rank) by dt

#### regexcapture

> **Important**
>
> The `regexcapture()` function is only supported in the XQL syntax for
> Parsing Rules.

##### Syntax

    regexcapture(<field>, "<pattern>")

##### Description

In Parsing Rules, the `regexcapture()` function is used to extract data
from fields using regular expression named groups from a given string
and returns a JSON object with captured groups. This function can be
used in any section of a Parsing Rule. The `regexcapture()` function is
useful when the regex pattern is not identical throughout the log, which
is required when using the
[regextract](#UUID52e57b04d631a29dcc44b5a8e4278d96) function.

XQL uses [RE2](https://github.com/google/re2/wiki/Syntax) for its
regular expression implementation. When using the `(?i)` syntax for
case-insensitive mode in your query, this syntax should be added only
once at the  beginning of the inline regular expression.

##### Example

Parsing Rule to ceate a dataset called `my_regexcapture_test`, where the
vendor and product that the specified Parsing Rules applies to is called
`regexcapture_vendor` and `regexcapture_product`. The output results
includes a new field called `regexcaptureResult`, which extract data
from the `_raw_log` field using regular expression named groups as
defined and returns the captured groups.

Parsing Rule:

    [INGEST:vendor="regexcapture_vendor", product="regexcapture_product", target_dataset="my_regexcapture_test"]
    alter regexcaptureResult = regexcapture(_raw_log,"^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (?P<user>\w+) \[(?P<timestamp>.+)\] (?P<request>.+) (?P<status>\d{3}) (?P<bytes>\d+)");

Log:

    192.168.1.1 - john [10/Mar/2024:12:34:56 +0000] GET /index.html HTTP/1.1 200 1234

XQL Query:

For the `my_regexcapture_test` dataset, returns the `regexcaptureResult`
field output.

    dataset = my_regexcapture_test 
    | fields regexcaptureResult

regexcaptureResult field output:

    {
      "ip": "192.168.1.1",
      "user": "john",
      "timestamp": "10/Mar/2024:12:34:56 +0000",
      "request": "GET /index.html HTTP/1.1",
      "status": "200",
      "bytes": "1234"
    }

#### regextract

##### Syntax

    regextract (<string_value>, <pattern>)

##### Description

The `regextract()` function accepts a string and a regular expression,
and it returns an array containing substrings that match the expression.

Cortex Query Language (XQL) uses
[RE2](https://github.com/google/re2/wiki/Syntax) for its regular
expression implementation. While capturing multiple groups is
unsupported, capturing one group in queries is supported.

When using the `(?i)` syntax for case-insensitive mode in your query,
this syntax should be added only once at the  beginning of the inline
regular expression.

> **Note**
>
> Capturing multiple groups is supported in Parsing Rules when using the
> [regexcapture](#UUID8faa08e9fc957f2287f3b9865b94acaa) function.

##### Examples

Without a capturing group

Extract the `Account Name` from the `action_evtlog_message`. Use the
[arrayindex](#UUID3b34d8d054146fb950c55877f8ee2eeb) and
[split](#UUIDb083e6971c7eeaed3f9287dcb32b6937) functions to extract the
actual account name from the array created by `regextract`.

    dataset = xdr_data 
    | fields action_evtlog_message as aem 
    | filter aem != null 
    | alter account_name = 
        arrayindex(
            split(
                arrayindex(
                    regextract(aem, "Account Name:\t\t.*\r\n")
                ,0)
            , ":")
        ,1) 
    | filter account_name != null 
    | limit 10 

Using one capturing group

Extract from the `log_example` field all of the values included for
the id objects.

    dataset = xdr_data 
    | limit 1
    | alter
        log_example = "{\"events\":[{\"id\": \"1\", \"type\": \"process\", \"size\": 123, \"processID\": 40540},{\"id\": \"2\", \"type\": \"request\", \"size\": 456, \"srcOS\": \"MAC\"}],\"host\": \"LocalHost\",\"date\": {\"day\": 4, \"month\": 7, \"year\": 2024},\"tags\":[\"agent\", \"auth\", \"low\"]}"
    | alter 
        one_capture_group_usage = regextract(log_example, "\"id\":\s*\"([^\"]+)\"")
    | fields log_example, one_capture_group_usage

#### replace

##### Syntax

    replace (<field>, "<old_substring>", "<new_string>")

##### Description

The `replace()` function accepts a string field, and replaces all
occurrences of a substring with a replacement string.

##### Examples

If \'.exe\' is present on the `action_process_image_name` field value,
replace that substring with an empty string. This example uses the
[if](#UUID2b285e075b1c97aef1621fd0c6884c1a) and
[lowercase](#UUIDed525d313e9f4c67c36db153b26e864f) functions, as well as
the contains operator to perform the conditional check.

    dataset = xdr_data 
    | fields action_process_image_name as apin 
    | filter apin != null 
    | alter remove_exe_process = if(lowercase(apin) contains ".exe",
                                  replace(lowercase(apin),".exe",""),
                                  lowercase(apin)) 
    | limit 10

See also the [ltrim, rtrim, trim](#UUIDc26ba83dd495000766b65404b8e9d686)
function example.

#### replex

##### Syntax

    replex (<string>, <pattern>, <new_string>)

##### Description

The `replex()` function accepts a string, and then uses a regular
expression to identify a substring, and then replaces matching
substrings with a new string.

XQL uses [RE2](https://github.com/google/re2/wiki/Syntax) for its
regular expression implementation.

##### Examples

For any `agent_id` that contains a dotted decimal IP address, mask the
IP address. Use the [dedup stage](#UUID9ca262399c1d7020771dd7b5498cf3e7)
to reduce the result set to first-seen `agent_id` values.

    dataset = xdr_data 
    | fields agent_id 
    | alter clean_agent_id = replex(agent_id, 
                                  "[\d]+\.[\d]+\.[\d]+\.[\d]+", 
                                  "xxx.xxx.xx.xx") 
    | dedup agent_id by asc _time

#### round

##### Syntax

    round (<float> | <integer>)

##### Description

The `round()` function accepts either a float or an integer as an input
value, and it returns the input value rounded to the nearest integer.

##### Example

    dataset = xdr_data 
    | alter mynum = divide(action_file_size, 7) 
    | alter mynum2 = round(mynum)  
    | fields action_file_size, mynum, mynum2 
    | filter action_file_size > 3 
    | limit 1 

#### row_number

##### Syntax

    windowcomp row_number() [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [as <alias>]

##### Description

The `row_number()` function is a numbering function that is used in
combination with a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5)
stage. This function is used to return a single value for the sequential
row ordinal (1-based) for each row from a group of rows using a
combination of the `by` clause and `sort`.

##### Example

Return a single value for the sequential row ordinal (1-based) for each
row in the group of rows. The query returns a maximum of 100 `xdr_data`
records. The results are ordered by the `source_ip` in ascending order
in the `row_number_dns_query_name` column.

    dataset = xdr_data                                                                                          
    | limit 100                                                                      
    | windowcomp row_number() sort source_ip as row_number_dns_query_name

#### split

##### Syntax

    split (<value> [, <string_delimiter>])

##### Description

The `split()` function splits a string using an optional delimiter, and
returns the resulting substrings in an array. If no delimiter is
specified or an empty string is specified as a delimiter, a space (\'
\') is used.

##### Examples

Split IP addresses into an array, each element of the array containing
an IP octet.

    dataset = xdr_data 
    | fields action_local_ip  as alii 
    | alter ip_octets = split(alii, ".") 
    | limit 10 

#### stddev_population

##### Syntax

comp stage

    comp stddev_population(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp stddev_population(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

##### Description

The `stddev_population()` function is used to return a single population
(biased) variance value of a field for a group of rows. The function
syntax and application is based on the preceding stage:

comp stage

When the `stddev_population` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single population (biased) variance value
of a field over a group of rows, for all records that contain matching
values for the fields identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `stddev_population` statistical aggregate function is used with
a [windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the
function returns a single population (biased) variance value of a field
for each row in the group of rows, for all records that contain matching
values for the fields identified using a combination of the `by` clause,
`sort`, and `between` window frame clause. The results are provided in a
new column in the results table.

##### Examples

comp example

Calculates a maximum of 100 `metrics_source` records, where the
`_broker_device_id` is `655AYUWF`, and include a single population
(biased) variance value of the `total_size_rate` field for a group of
rows.

    dataset = metrics_source 
    | filter _broker_device_id = "655AYUWF" 
    | comp stddev_population(total_size_rate)
    | limit 100

windowcomp example

Return maximum of 100 `metrics_source` records and include a single
population (biased) variance value of the `total_size_rate` field for
each row in the group of rows, for all records that contain matching
values in the `_broker_device_id` field. The results are provided in the
`stddev_population` column.

    dataset = metrics_source
    | limit 100
    | windowcomp stddev_population(total_size_rate) by _broker_device_id as `stddev_population`

#### stddev_sample

##### Syntax

comp stage

    comp stddev_sample(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp stage

    windowcomp stddev_sample(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>]

##### Description

The `stddev_sample()` function is used to return a single sample
(unbiased) standard deviation value of a field for a group of rows. The
function syntax and application is based on the preceding stage:

comp stage

When the `stddev_sample` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single sample (unbiased) standard
deviation value of a field over a group of rows, for all records that
contain matching values for the fields identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `stddev_sample` statistical aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single sample (unbiased) standard deviation value of a field
for each row in the group of rows, for all records that contain matching
values for the fields identified using a combination of the `by` clause,
`sort`, and `between` window frame clause. The results are provided in a
new column in the results table.

##### Examples

comp stage example

Calculate a maximum of 100 `metrics_source` records, where the
`_broker_device_ip` is `172.16.1.25`, and include a single sample
(unbiased) standard deviation value of the `total_size_bytes` field for
a group of rows.

    dataset = metrics_source 
    | filter _broker_device_ip = "172.16.1.25" 
    | comp stddev_sample(total_size_bytes)
    | limit 100

windowcomp stage example

Return a maximum of 100 `metrics_source` records and include a single
sample (unbiased) standard deviation value of the `total_size_rate`
field for each row in the group of rows, for all records that contain
matching values in the `_broker_device_id` field. The results are
provided in the `stddev_sample` column.

    dataset = metrics_source
    | limit 100
    | windowcomp stddev_sample(total_size_rate) by _broker_device_id as `stddev_sample` 

#### string_count

##### Syntax

    string_count (<string>, <pattern>)

##### Description

The `string_count()` function returns the number of times a substring
appears in a string.

##### Example

    dataset = xdr_data 
    | fields actor_primary_username as apu 
    | filter string_count(apu, "e") > 1 

#### subtract

##### Syntax

    subtract (<string1> | <integer1>, <string2> | <integer2>)

##### Description

The `subtract()` function subtracts two positive integers by subtracting
the second argument from the first argument. Parameters may be either
integer literals, or integers as a string type such as might be
contained in a data field.

##### Example

    dataset = xdr_data 
    | alter mynum = subtract(action_file_size, 3) 
    | fields action_file_size, mynum 
    | filter action_file_size > 3 
    | limit 1 

#### sum

##### Syntax

comp stage

    comp sum(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

windowcomp

    windowcomp sum(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

##### Description

The `sum()` function is used to return the sum of an integer field over
a group of rows. The function syntax and application is based on the
preceding stage:

comp stage

When the `sum` aggregation function is used with a
[/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
stage, the function returns a single sum of an integer field for a group
of rows, for all records that contain matching values for the fields
identified in the `by` clause.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

windowcomp stage

When the `sum` aggregate function is used with a
[windowcomp](#UUID6c8ad1ac68d140768416853f92bfb0a5) stage, the function
returns a single sum of an integer field for each row in the group of
rows, for all records that contain matching values for the fields
identified using a combination of the `by` clause, `sort`, and `between`
window frame clause. The results are provided in a new column in the
results table.

##### Examples

comp example

Return a single sum of the `action_total_download` field for a group of
rows, for all records that have matching values for their
`actor_process_image_path` and `actor_process_command_line` values. The
query calculates a maximum of 100 `xdr_data` records and includes a
`raw_data` column listing a single value for the results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp sum(Download) as total_download by Process_Path, Process_CMD addrawdata = true as raw_data

windowcomp

Return the download to upload ratio per process. The query returns a
maximum of 100 `xdr_data` records in new columns called `sum_upload` and
`sum_download`.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download, action_total_upload as Upload
    | filter Download > 0
    | limit 100
    | windowcomp sum(Download) by Process_Path, Process_CMD as sum_download
    | windowcomp sum(Upload) by Process_Path, Process_CMD as sum_upload
    | fields - Download ,Upload
    | dedup Process_CMD, Process_Path, sum_download ,sum_upload
    | alter ration = divide(sum_download ,sum_upload)

#### time_frame_end

##### Syntax

    time_frame_end(<time frame>)

##### Description

The `time_frame_end()` function returns the timestamp object for the
string representation of the end of the time frame configured for the
query in the format MMM dd YYYY HH:mm:ss, such as Jun 8th 2022 15:20:06.
You can configure the time frame using the config
[timeframe](#UUIDa087d2382f623b58fb8834e5bbc7c8f6) function, where the
range can be relative or exact.

If the time frame is relative, for example last 24H, the function
returns the [current_time](#UUIDffd7c1230844e74fb41cd88827f88f30). This
function is useful when the query uses a custom time frame whose end
time is in the past.

##### Example 1 - Relative Time

For the last 5 days from when the query is sent, returns a maximum of
100 `xdr_data` records with the events of the \_time field with a new
field called \"x\". The \"x\" field lists the final timestamp at the end
of 5 days from when the query was sent for the events in descending
order. For more information on this relative timeframe range, see the
config [timeframe](#UUIDa087d2382f623b58fb8834e5bbc7c8f6) function.

    config timeframe = 5d
    | dataset = xdr_data
    | alter x = time_frame_end()
    | fields x
    | sort desc x

##### Example 2 - Relative Time

For the last 5 days from when the query is run until now, returns a
maximum of 100 xdr_data records with the events of the \_time field with
a new field called \"x\". The \"x\" field lists the final timestamp at
the end of 5 days from when the query runs for the events in descending
order. For more information on this relative time frame range, see the
config [timeframe](#UUIDa087d2382f623b58fb8834e5bbc7c8f6) function.

    config timeframe = between "5d" and "now"
    | dataset = xdr_data
    | alter x = time_frame_end()
    | fields x
    | sort desc

#### timestamp_diff

##### Syntax

    timestamp_diff (<timestamp1>, <timestamp2>, <part>)

##### Description

The `timestamp_diff()` function returns the difference between two
timestamp objects. The units used to express the difference is
identified by the `part` parameter. The second timestamp is subtracted
from the first timestamp. If the first timestamp is greater than the
second, a positive value is returned. If the result of this function is
between 0 and 1, 0 is returned.

Supported parts are:

- `DAY`

- `HOUR`

- `MINUTE`

- `SECOND`

- `MILLISECOND`

- `MICROSECOND`

##### Example

    dataset = xdr_data 
    | filter story_publish_timestamp != null 
    | alter ts = to_timestamp(story_publish_timestamp, "MILLIS") 
    | alter ct = current_time() 
    | alter diff = timestamp_diff(ct, ts, "MINUTE") 
    | fields ts, ct, diff 
    | limit 1

#### timestamp_seconds

##### Syntax

    timestamp_seconds (<integer>)

##### Description

The `timestamp_seconds()` function converts an epoch time Integer value
in seconds to a TIMESTAMP compatible value.

> **Note**
>
> Endpoint Detection and Response (EDR) columns store epoch milliseconds
> values so this function is more useful for values that you insert.

##### Example

Display a human-readable timestamp for the `action_file_access_time`
field.

    alter access_timestamp = timestamp_seconds(1611882205) | limit 1 

#### to_boolean

##### Syntax

    to_boolean(<string>)

##### Description

The `to_boolean()` function converts a string that represents a boolean
to a boolean value.

The input value to this string must be either `TRUE` or `FALSE`, case
insensitive.

#### to_epoch

##### Syntax

    to_epoch (<timestamp>, <time unit>)

##### Description

The `to_epoch()` function converts a timestamp value for a particular
field or function to the Unix epoch timestamp format. This function
requires a `<time unit>` value, which indicates whether the integer
value for the Unix epoch timestamp format represents seconds (default),
milliseconds, or microseconds. If no `<time unit>` is configured, the
default is used. Supported values are:

- SECONDS

- MILLIS

- MICROS

##### Example

Returns a maximum of 100 `xdr_data` records with the events of the
`_time` field, which includes a timestamp field in the Unix epoch format
called `ts`. The ts field contains the equivalent Unix epoch values in
milliseconds for the timestamps listed in the `_time` field.

    dataset = xdr_data
    | filter _time != null
    | alter ts = to_epoch(_time, "MILLIS")
    | fields ts
    | limit 100

#### to_float

##### Syntax

    to_float(<string>)

##### Description

The `to_float()` function converts a string that represents a number to
a floating point number. This function is identical to the
[to_number](#UUID23ea4a80d0a6ed6c23733a5ec45ad523) function.

##### Examples

Display the first 10 IP addresses that begin with a value greater than
`192`. Use the [split](#UUIDb083e6971c7eeaed3f9287dcb32b6937) function
to split the IP address by \'.\', and then use the
[arrayindex](#UUID3b34d8d054146fb950c55877f8ee2eeb) function to retrieve
the first value in the resulting array. Convert this to a number and
perform an arithmetic compare to arrive at a result set.

    dataset = xdr_data 
    | fields action_local_ip  as alii 
    | filter to_float(arrayindex(split(alii, "."),0))  > 192 
    | limit 10 

#### to_integer

##### Syntax

    to_integer(<string>)

##### Description

The `to_integer()` function converts a string value that represents a
number of a given field to an integer. A good application of using the
`to_integer` function is when querying for USB vendor IDs and USB
product IDs, which are usually provided in a hex format.

It is an error to provide a string to this function that contains a
floating point number.

##### Examples

Display the first 10 IP addresses that begin with a value greater than
192. Use the [split](#UUIDb083e6971c7eeaed3f9287dcb32b6937) function to
split the IP address by \'.\', and then use the
[arrayindex](#UUID3b34d8d054146fb950c55877f8ee2eeb) function to retrieve
the first value in the resulting array. Convert this to a number and
perform an arithmetic compare to arrive at a result set.

    dataset = xdr_data 
    | fields action_local_ip  as alii 
    | filter to_integer(arrayindex(split(alii, "."),0))  > 192 
    | limit 10 

#### to_json_string

##### Syntax

    to_json_string(<data type>)

##### Description

The `to_json_string()` function accepts all data types, such as
integers, booleans, strings, and returns it as a JSON formatted string.
This function always returns a string. When the input is an object or an
array, the function returns a JSON formatted string of the input. When
the input string is a string, it returns the string as is. You can then
use the JSON formatted string or string returned by this function with
the [json_extract](#UUIDccf9233d0f75a245d130bb032e1f6687),
[json_extract_array](#UUIDc0bcb6ff04b8c1e080b351616ef4c84f), and
[json_extract_scalar](#UUIDecb1e8c53780d41f6cde0d5e85f70216) functions.

##### Examples

Return the `action_file_device_info` field in JSON format.

    dataset = xdr_data 
    | fields action_file_device_info as afdi
    | filter afdi != null  
    | alter the_json_string = to_json_string(afdi) 
    | limit 10

#### to_number

##### Syntax

    to_number (<string>)

##### Description

The `to_number()` function converts a string that represents a number to
a floating point number. This function is identical to the
[to_float](#UUID0cc419338ed7a4a934b8d0e542b51320) function.

##### Examples

Display the first 10 IP addresses that begin with a value greater than
192. Use the [split](#UUIDb083e6971c7eeaed3f9287dcb32b6937) function to
split the IP address by \'.\', and then use the
[arrayindex](#UUID3b34d8d054146fb950c55877f8ee2eeb) function to retrieve
the first value in the resulting array. Convert this to a number and
perform an arithmetic compare to arrive at a result set.

    dataset = xdr_data 
    | fields action_local_ip  as alii 
    | filter to_number(arrayindex(split(alii, "."),0))  > 192 
    | limit 10 

#### to_string

##### Syntax

    to_string (<field>)

##### Description

The `to_string()` function converts a number value of a given field to a
string.

##### Examples

Display the first non-NULL `action_boot_time` field value. In a second
column called `abt_string`, use the
[concat](#UUID53a3a68c2ac139b715a5df4747070967) function to prepend
\"str: \" to the value, and then display it.

    dataset = xdr_data 
    | fields action_boot_time as abt 
    | filter abt != null 
    | alter abt_string = concat("str: ", to_string(abt)) 
    | limit 1 

#### to_timestamp

##### Syntax

    to_timestamp (<integer>, <units>)

##### Description

The `to_timestamp()` function converts an integer to a timestamp. This
function requires a `units` value, which indicates whether the integer
represents seconds, milliseconds, or microseconds since the Unix epoch.
Supported values are:

- `SECONDS`

- `MILLIS`

- `MICROS`

##### Example

    dataset = xdr_data 
    | filter story_publish_timestamp != null 
    | alter ts = to_timestamp(story_publish_timestamp, "MILLIS") 
    | fields ts 

#### uppercase

##### Syntax

    uppercase (<string>)

##### Description

The `uppercase()` function converts a string field value to all
uppercase.

##### Examples

Convert all `actor_process_image_name` field values that are not null to
uppercase, and return a list of unique values.

    dataset = xdr_data 
    | fields actor_process_image_name as apin 
    | dedup apin by asc _time 
    | filter apin != null 
    | alter apin = uppercase(apin)

#### values

##### Syntax

    comp values(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `values` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns an array of all the values found for a given field over a
group of rows, for all records that contain matching values for the
fields identified in the `by` clause. The array values are all non-null.
Each value appears in the array only once, even if a given value repeats
multiple times in the result set. This function is used in combination
with a `comp` stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Example

Return an array containing all the values seen for the
`action_total_download` field for all records that have matching values
for their `actor_process_image_path` and `actor_process_command_line`
values. The query calculates a maximum of 100 `xdr_data` records and
includes a `raw_data` column listing the raw data events used to display
the final `comp` results. In addition, this example contains a number of
fields defined as aliases: `actor_process_image_path` uses the alias
`Process_Path`, `actor_process_command_line` uses the alias
`Process_CMD`, `action_total_download` uses the alias `Download`, and
`Download` uses the alias `values_download`.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp values(Download) as values_download by Process_Path, Process_CMD addrawdata = true as raw_data

#### var

##### Syntax

    comp var(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]]

##### Description

The `var` aggregation is a [comp
function](/document/preview/892018#UUID-bab9ca82-561c-c7a9-8a37-f9c42a06e8f3)
that returns a single variance value of a field over a group of rows,
for all records that contain matching values for the fields identified
in the `by` clause. This function is used in combination with a `comp`
stage.

In addition, you can configure whether the raw data events are displayed
by setting `addrawdata` to either `true` or `false` (default), which are
used to configure the final `comp` results. When including raw data
events in your query, the query runs for up to 50 fields that you define
and displays up to 100 events.

##### Example

Return the variance of the `action_total_download` field for all records
that have matching values for their `actor_process_image_path` and
`actor_process_command_line` values. The query calculates a maximum of
100 `xdr_data` records and includes a `raw_data` column listing the raw
data events used to display the final `comp` results.

    dataset = xdr_data
    | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download
    | filter Download > 0
    | limit 100
    | comp var(Download) as variance_download by Process_Path, Process_CMD
    addrawdata = true as raw_data

#### wildcard_match

##### Syntax

    wildcard_match (<string_value>, <wildcard_pattern>)

##### Description

The `wildcard_match()` function accepts a string and a wildcard pattern
including `*` and `?`, and returns `true` when the `<string_value>`
matches the `<wildcard_pattern>`. When using a wildcard pattern, keep in
mind the difference between the following metacharacters used as
repetition operators:

- `*`: Returns all results following the pattern for a sequence of zero
  or more (possibly different) strings.

- `?`: Returns a single character result following the pattern for a
  sequence of zero or one in the string.

XQL uses [RE2](https://github.com/google/re2/wiki/Syntax) for its
regular expression implementation. When using the `(?i)` syntax for
case-insensitive mode in your query, this syntax should be added only
once at the  beginning of the inline regular expression.

##### Examples

Lookup dataset sample data

The examples provided below are based on running queries using a lookup
dataset called `lookup_app_category`. Here\'s some sample data of the
dataset table:

  -----------------------------------------------------------------------
  \_TIIME                             APP_CATEGORY
  ----------------------------------- -----------------------------------
  Aug 31 2024 12:13:48                general-internet

  Sep 1st 2024 12:13:11               general-internet

  Sep 2th 2024 01:13:17               general-internet

  Sep 3th 2024 09:13:37               general-ip

  Sep 4th 2024 11:13:25               general-ip

  Sep 5th 2024 03:13:19               general-dns

  Sep 6th 2024 12:05:03               general-internet

  Sep 6th 2024 15:22:36               multicast-ip
  -----------------------------------------------------------------------

Example 1: wildcard_match with filter and \*

Return a maximum of 100 records from a lookup dataset called
`lookup_app_category`. The `pattern` field defines the wildcard pattern
as `general-*`. When this wildcard pattern is found in the
`app_category` field, the `wildcard_match` returns `true` and the
matching events are listed in the table results with the `pattern` field
displaying the defined pattern.

    dataset = lookup_app_category 
    | alter pattern = "general-*" 
    | filter wildcard_match(app_category , pattern)
    | fields pattern, app_category
    | limit 100

Sample output table results:

  -----------------------------------------------------------------------
  PATTERN                 \_TIIME                 APP_CATEGORY
  ----------------------- ----------------------- -----------------------
  general-\*              Aug 31 2024 12:13:48    general-internet

  general-\*              Sep 1st 2024 12:13:11   general-internet

  general-\*              Sep 2th 2024 01:13:17   general-internet

  general-\*              Sep 3th 2024 09:13:37   general-ip

  general-\*              Sep 4th 2024 11:13:25   general-ip

  general-\*              Sep 5th 2024 03:13:19   general-dns

  general-\*              Sep 6th 2024 12:05:03   general-internet
  -----------------------------------------------------------------------

Example 2: wildcard_match with filter and ?

Return a maximum of 100 records from a lookup dataset called
`lookup_app_category`. The `pattern` field defines the wildcard pattern
as `general-??`. When this wildcard pattern is found in the
`app_category` field, the `wildcard_match` returns `true` and the
matching events are listed in the table results with the `pattern` field
displaying the defined pattern.

    dataset = lookup_app_category 
    | alter pattern = "general-??" 
    | filter wildcard_match(app_category , pattern)
    | fields pattern, app_category
    | limit 100

Sample output table results:

  -----------------------------------------------------------------------
  PATTERN                 \_TIIME                 APP_CATEGORY
  ----------------------- ----------------------- -----------------------
  general-??              Sep 3th 2024 09:13:37   general-ip

  general-??              Sep 4th 2024 11:13:25   general-ip
  -----------------------------------------------------------------------

Example 3: wildcard_match with alter, \*, and ?

Return a maximum of 100 records from a lookup dataset called
`lookup_app_category`. The `pattern` field defines the wildcard pattern
as `*-i??`. When this wildcard pattern is found in the `app_category`
field, the `wildcard_match` returns `true` and is passed to the
`pattern` field, and the events found are listed in the table results.

    dataset = lookup_app_category 
    | alter pattern = "*-i??" 
    | alter test = wildcard_match(app_category , pattern)
    | fields test, pattern, app_category
    | limit 100

Sample output table results:

  -----------------------------------------------------------------------
  PATTERN                 \_TIIME                 APP_CATEGORY
  ----------------------- ----------------------- -----------------------
  true                    Sep 3th 2024 09:13:37   general-ip

  true                    Sep 4th 2024 11:13:25   general-ip

  true                    Sep 6th 2024 15:22:36   multicast-ip
  -----------------------------------------------------------------------

