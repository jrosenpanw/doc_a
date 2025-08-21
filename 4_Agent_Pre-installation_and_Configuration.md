# 4. Agent Pre-installation and Configuration

Before deploying Cortex XDR agents, you need to perform several configuration steps to ensure policies are applied correctly and data is collected effectively.

## Define Endpoint Groups

[cite_start]Endpoint groups allow you to apply specific policy rules and manage endpoints collectively. [cite: 568] You can create two types of groups:

* [cite_start]**Dynamic Groups**: Endpoints are automatically added to the group based on characteristics like OS, IP address, or endpoint tags. [cite: 571]
* [cite_start]**Static Groups**: You manually select a specific list of endpoints to include in the group. [cite: 572]

To create a group:
1.  [cite_start]Go to **Inventory > Endpoints > Groups** and click **+Add Group**. [cite: 576]
2.  [cite_start]Enter a name and description. [cite: 580]
3.  [cite_start]Choose whether to create a **Dynamic** group (using filters) or a **Static** group (by selecting endpoints). [cite: 582, 583, 587]
4.  Create the group. [cite_start]It can then be used to assign security profiles. [cite: 593, 594]

## Customize Endpoint Security Profiles

[cite_start]Cortex XSIAM includes default security profiles that offer immediate protection. [cite: 603] [cite_start]These profiles customize and reuse settings across different endpoint groups. [cite: 605] You can find profiles for exploits, malware, agent settings, and exceptions. [cite_start]Review your policy rules and the assigned security profiles to make any necessary adjustments for your environment. [cite: 27]

## Enable Enhanced Data Collection

[cite_start]While Cortex XSIAM provides out-of-the-box protection, you must enable **Data Collection** in an Agent Settings profile to leverage endpoint data for features like Analytics and Host Insights. [cite: 27] [cite_start]This allows the Cortex XDR agent to continuously monitor endpoint activity for malicious events. [cite: 615]

The specific data collected varies by platform (Windows, macOS, Linux) and may include:
* [cite_start]File and process activity [cite: 625, 632, 634]
* [cite_start]Network connections [cite: 625, 632, 634]
* [cite_start]Registry modifications (Windows) [cite: 625]
* [cite_start]Windows Event Logs (requires configuration) [cite: 627, 628]

[cite_start]**Note**: Some advanced data collection, such as for RPC calls or system calls on Windows, requires the **Extended Threat Hunting Data (XTH)** add-on. [cite: 619, 625]

## Configure Global Agent Settings

You can configure global settings that apply to all endpoints in your network. [cite_start]These are found under **Settings > Configurations > General > Agent Configurations**. [cite: 638, 639]

Key global settings include:

* **Global Uninstall Password**: Set a password required to remove a Cortex XDR agent. [cite_start]This can be overridden in individual Agent Settings profiles. [cite: 640, 641, 645]
* **Content Updates Bandwidth and Frequency**:
    * **Bandwidth Control**: Control the network consumption for content updates. [cite_start]Cortex XSIAM provides a calculator to recommend the optimal bandwidth based on the number of agents. [cite: 651, 652]
    * [cite_start]**Minor Content Updates**: Enabled by default, this ensures agents receive the most frequent updates between major content versions. [cite: 655, 656]
* [cite_start]**Agent Auto Upgrade Scheduler**: If auto-upgrades are enabled, you can control the number of parallel upgrades and schedule them for specific days and times. [cite: 665, 668, 670]
* **Advanced Analysis**: Automatically upload alert data for further analysis by Palo Alto Networks. [cite_start]You can also enable automatic creation of exceptions based on the analysis results. [cite: 673, 676, 679]
* **License Revocation and Deletion Period**:
    * [cite_start]**Connection Lost (Days)**: Configure how many days an agent can be disconnected before its license is returned (default is 30 days). [cite: 689, 690]
    * [cite_start]**Agent Deletion (Days)**: Configure how many days after losing connection an agent's data is removed from the console (default is 180 days). [cite: 692, 693]
* [cite_start]**Periodic Duplicate Cleanup**: Enable a periodic cleanup of duplicate endpoint entries in the administration table based on hostname, IP, or MAC address. [cite: 712, 716]
```

-----

### **`05_Agent_Installation_and_Deployment.md`**

```markdown
