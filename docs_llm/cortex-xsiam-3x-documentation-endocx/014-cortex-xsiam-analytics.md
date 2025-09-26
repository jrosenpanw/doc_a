## Cortex XSIAM - Analytics

The Cortex XSIAM Analytics engine enables Cortex XSIAM to analyze data
from a variety of sensors and develop a baseline to raise analytics
alerts when anomalies and malicious behaviors are detected.

> **Prerequisite**
>
> Before Cortex XSIAM - Analytics can start to analyze your endpoint
> data, perform the following steps:

1.  > Configure Cortex XSIAM network parameters to monitor your internal
    > networks.

2.  > Enable the Analytics Engine.

3.  > Make sure Cloud Identity Engine is set up.

4.  > Enable Identity Analytics.

### Configure Cortex XSIAM network parameters

Define your internal IP address ranges and domain names to enable Cortex
XSIAM to identify, track, and analyze network assets.

#### Define internal IP address ranges

The **IP Address Ranges** page displays the address ranges that Cortex
XSIAM Analytics monitors. Addresses are pre-populated with the default
IPv4 and IPv6 address spaces. The names you define appears when
investigating the network-related events in Cortex XSIAM.

You can add a new IP address range manually or upload IP address ranges
from a CSV file.

**How to define internal IP address ranges**

1.  Select Inventory \> Assets \> Network Configuration \> Internal IP
    Address Ranges.

2.  Do one of the following:

+-----------------------------------+-------------------------------------------------------+
| To                                | Do this                                               |
+===================================+=======================================================+
| Add a new IP address manually     | 1.  Click Add New Range \> Create New, and then enter |
|                                   |     the IP address name and IP address range or CIDR  |
|                                   |     values.                                           |
|                                   |                                                       |
|                                   | - By default, Cortex XSIAM creates Private Network    |
|                                   |   ranges that specify reserved industry-approved      |
|                                   |   ranges. Private Network ranges are marked with a    |
|                                   |   ![](media/rId336.png){width="0.14583333333333334in" |
|                                   |   height="0.20833333333333334in"} icon and you can    |
|                                   |   only edit the name.                                 |
|                                   |                                                       |
|                                   |   > **Note**                                          |
|                                   |                                                       |
|                                   |   > You can add a range that is fully contained in an |
|                                   |   > existing range, however, you cannot add a new     |
|                                   |   > range that partially intersects with another      |
|                                   |   > range.                                            |
|                                   |                                                       |
|                                   | 2.  Click **Save**.                                   |
+-----------------------------------+-------------------------------------------------------+
| Upload IP address ranges from a   | 1.  Select Inventory \> Assets \> Network             |
| CSV file                          |     Configuration \> IP Address Ranges.               |
|                                   |                                                       |
|                                   | 2.  Click Add New Range \> Upload from File.          |
|                                   |                                                       |
|                                   | 3.  Locate the CSV file you want to upload, and then  |
|                                   |     click **Add**.                                    |
+-----------------------------------+-------------------------------------------------------+

#### Define internal domain names

1.  Select Inventory \> Assets \> Network Configuration \> Internal
    Domain Suffixes.

2.  Type the domain suffix you want to include as part of your internal
    network, for example, `acme.com`.

3.  Select ![](media/rId340.png){width="0.14583333333333334in"
    height="0.20833333333333334in"} to add the suffix to the
    **Domains List**.

### Enable the Analytics Engine and Identity Analytics

Cortex XSIAM  - Analytics includes the following:

- **Cortex XSIAM Analytics Engine:** Analyzes your endpoint data to
  develop a baseline and raise Analytics and Analytics BIOC alerts when
  anomalies and malicious behaviors are detected.

- **Identity Analytics:** Allows the Cortex XSIAM  Analytics engine to
  aggregate and display user profile details, activities, and alerts
  related to a user-based Analytics type alert and Analytics BIOC rule
  during an investigation.

> **Prerequisite**
>
> **Analytics Engine**
>
> To create a baseline for enabling analytics, Cortex XSIAM requires a
> minimum of one of the following data sets:

- > EDR or Network logs from at least 30 endpoints over a minimum of 2
  > weeks

- > Cloud audit logs over a minimum of 5 days

> **Identity Analytics**

- > Cortex XSIAM - Analytics must be activated.

- > Cloud Identity Engine must be set up. For more information, see
  > [Cloud Identity Engine](#UUID586f81e7ddbd6968328cbd7809bd7eaa).

**How to enable analytics**

1.  Select Settings \> Configurations \> Cortex XSIAM - Analytics.

2.  Click **Enable**. Creating a baseline can take up to three hours.

- Adding Windows DHCP logs can enhance the Analytics Engine. For more
  information, see Ingest Windows DHCP Logs with an XDR Collector
  Profile.

3.  Activate **Identity Analytics** by turning on the toggle.

