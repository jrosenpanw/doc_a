# 8. Post-Deployment and Maintenance

After the initial deployment and configuration, you should perform health checks and set up your environment for ongoing operations.

## Perform Health Checks

[cite_start]It is recommended to perform the following health checks to validate your deployment[cite: 1584]:

1.  [cite_start]**Update Prevention Policies**: Ensure that policies and profiles have their action modes set to **Block** for active prevention. [cite: 1585]
2.  **Monitor Operational Status**: Verify that Cortex XDR agents are protecting endpoints as expected. You can check the **Operational Status** column in **Endpoints > All Endpoints**. [cite_start]The status can be `Protected`, `Partially protected`, or `Unprotected`. [cite: 1587, 1601, 1602, 1603, 1605]
3.  [cite_start]**Test Sample Malware**: Use a test malware file (e.g., an EICAR file) to verify end-to-end sample processing by WildFire. [cite: 1589]
4.  **Validate Detectors and Log Ingestion**:
    * [cite_start]Check that issues are being generated from their expected sources (e.g., WildFire malware issues, NGFW issues). [cite: 1591, 1593, 1594]
    * [cite_start]Verify that logs from external integrations are being ingested correctly by checking the **Dataset Management** page. [cite: 1595]

## Configure Server and Security Settings

You can customize various server and security settings to create a more personalized and secure user experience.

### Server Settings

[cite_start]Navigate to **Settings > Configurations > General > Server Settings** to configure the following[cite: 1615]:

* [cite_start]**Timezone and Timestamp Format**: Set your preferred timezone and format, which applies only to your user account. [cite: 1617, 1618]
* [cite_start]**Password Protection for Downloads**: Enable password protection for files retrieved from an endpoint to prevent accidental execution of malicious files. [cite: 1618]
* **Scope-Based Access Control (SBAC)**: Enforce granular scoping for users. [cite_start]This is disabled by default. [cite: 1618]
* [cite_start]**Data Ingestion Monitoring**: Enable health alerts for disruptions in data collection. [cite: 1618]

### Security Settings

[cite_start]Navigate to **Settings > Configurations > General > Security Settings** to configure[cite: 1621]:

* [cite_start]**Session Expiration**: Set the number of hours after which a user's session expires. [cite: 1623]
* [cite_start]**Approved IP Ranges**: Restrict user login access to Cortex XSIAM from specific IP ranges. [cite: 1623]
* [cite_start]**Allowed Domains**: Specify which domain names can be used in distribution lists for reports to prevent sending them outside your organization. [cite: 1623]

## Log Forwarding

[cite_start]You can forward logs from Cortex XSIAM to external services like an email distribution list, a Slack channel, or a syslog receiver to stay informed about important events. [cite: 1627, 1628]

### How to Configure Log Forwarding

1.  **Integrate the External Service**:
    * **For a Syslog Receiver**: Go to `Settings > Configurations > Integrations > External Applications`. Add a new server, specifying its destination, port, and protocol. [cite_start]You must enable access to the appropriate Cortex XSIAM IP addresses in your firewall. [cite: 1643, 1645, 1646, 1647]
    * [cite_start]**For Slack**: Use the provided link under `External Applications` to install the Cortex XSIAM app in your Slack workspace. [cite: 1663, 1664]
2.  **Create a Forwarding Configuration**:
    * [cite_start]Go to **Settings > Configurations > General > Notifications**. [cite: 1683]
    * [cite_start]Click **+ Add Forwarding Configuration**. [cite: 1684]
    * [cite_start]Select the **log type** to forward (e.g., Issues, Agent Audit Logs, Management Audit Logs). [cite: 1686]
    * [cite_start]Use the **Scope** filter to specify the exact criteria for events you want to forward (e.g., `Severity = High`). [cite: 1697]
    * [cite_start]Define the destination (email list, Slack channel, or syslog receiver). [cite: 1700, 1708]

## Monitor Administrative Activity

[cite_start]The **Management Audit Logs** (**Settings > Management Audit Logs**) track all administrative and investigative actions performed in the tenant. [cite: 1720] [cite_start]Logs are stored for 365 days. [cite: 1721] [cite_start]You can filter the logs and configure forwarding to stay informed about important changes. [cite: 1722, 1723]
```

-----

### **`09_Remote_Repository_for_Content_Development.md`**

```markdown
