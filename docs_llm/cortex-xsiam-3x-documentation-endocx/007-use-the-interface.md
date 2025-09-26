## Use the interface

Cortex XSIAM provides an easy-to-use interface. Here you can learn more
about the user interface, shortcuts and useful tips.

> **Note**

- > Each SAML login session is valid for 8 hours.

- > Some menu items only appear if you have the relevant license.

Navigation cheat sheet

+-----------------------------------+-------------------------------------------------------+
| Interface                         | Description                                           |
+===================================+=======================================================+
| Dashboard & Reports               | - **Dashboard**---Provides dashboards that you can    |
|                                   |   use to view high-level statistics about your agents |
|                                   |   and cases.                                          |
|                                   |                                                       |
|                                   | - **Reports**---View all the reports that Cortex      |
|                                   |   XSIAM administrators have run.                      |
|                                   |                                                       |
|                                   | - **Dashboard Manager**---Add new dashboards with     |
|                                   |   customized widgets to surface the statistics that   |
|                                   |   matter to you most.                                 |
|                                   |                                                       |
|                                   | - **Report Templates**---Build reports using          |
|                                   |   pre-defined templates, or customize a report.       |
|                                   |   Reports can be generated on-demand scheduled.       |
|                                   |                                                       |
|                                   | - **Widget Library**---Search, view, edit, and create |
|                                   |   widgets based on predefined widgets and             |
|                                   |   user-created custom widgets.                        |
+-----------------------------------+-------------------------------------------------------+
| Cases & Issues                    | - **Cases**---Investigate cases, manually create new  |
|                                   |   cases, manage case severity and status, assign      |
|                                   |   cases, and merge cases.                             |
|                                   |                                                       |
|                                   | - **Issues**---Investigate and manage individual      |
|                                   |   issues. Run a playbook in the **Work Plan** for an  |
|                                   |   individual issue or run the same playbook on        |
|                                   |   multiple issues from the **Issues** table. Run      |
|                                   |   commands in the **War Room**. Navigate to the       |
|                                   |   **Findings** table.                                 |
|                                   |                                                       |
|                                   | - **Case Configuration**---Review playbook trigger    |
|                                   |   recommendations, create new playbook triggers, add  |
|                                   |   case scoring rules, view starred issues, and add    |
|                                   |   featured hosts, users, and IP addresses.            |
+-----------------------------------+-------------------------------------------------------+
| Investigation & Response          | - **Search**                                          |
|                                   |                                                       |
|                                   |   - **Query Builder**---Build complex queries to      |
|                                   |     investigate, identify connections, and expose the |
|                                   |     root cause of issues from your data sources.      |
|                                   |                                                       |
|                                   |   - **Query Center**---View and manage the results of |
|                                   |     all simple and complex queries created from the   |
|                                   |     Query Builder.                                    |
|                                   |                                                       |
|                                   |   - **Scheduled Queries**---View and manage all       |
|                                   |     scheduled and reoccurring queries created from    |
|                                   |     the Query Builder.                                |
|                                   |                                                       |
|                                   | - **Automation**                                      |
|                                   |                                                       |
|                                   |   - **Playbooks**---View, create, and edit playbooks. |
|                                   |                                                       |
|                                   |   - **Scripts**---View, create, and edit scripts. Use |
|                                   |     **Script Helper** to find relevant commands and   |
|                                   |     scripts for your use case.                        |
|                                   |                                                       |
|                                   |   - **Jobs**---Create and manage jobs to run a        |
|                                   |     specific playbook, triggered either by time or a  |
|                                   |     delta in a feed.                                  |
|                                   |                                                       |
|                                   |   - **Playground**---Safely develop and test scripts, |
|                                   |     commands, and more, in a non-production           |
|                                   |     environment not connected to a specific issue or  |
|                                   |     case.                                             |
|                                   |                                                       |
|                                   |   - **Automation Rules**---Automatically respond to   |
|                                   |     events by defining trigger conditions and desired |
|                                   |     actions to perform once the condition is met.     |
|                                   |                                                       |
|                                   | - **Response**                                        |
|                                   |                                                       |
|                                   |   - **Action Center**---Provides a central location   |
|                                   |     from which you can track the progress of all      |
|                                   |     investigation, response, and maintenance actions  |
|                                   |     performed on your endpoints.                      |
|                                   |                                                       |
|                                   |   - **Live Terminal**---Initiate a remote connection  |
|                                   |     to an endpoint enabling you to remotely manage,   |
|                                   |     investigate, and perform response actions on the  |
|                                   |     endpoint.                                         |
|                                   |                                                       |
|                                   |   - **EDL**---Add malicious domains and IP addresses  |
|                                   |     to an external dynamic list enforceable on your   |
|                                   |     Palo Alto Networks firewall.                      |
|                                   |                                                       |
|                                   | - **Forensics**---Streamline your case response, data |
|                                   |   collection, threat hunting, and analyses of your    |
|                                   |   endpoint data to find the source and scope of an    |
|                                   |   attack.                                             |
|                                   |                                                       |
|                                   | - **Notebooks**---Use Jupyter tools to build machine  |
|                                   |   learning models to visualize clusters, identify     |
|                                   |   anomalies, and then feed your findings back into    |
|                                   |   the Cortex XSIAM environment to generate security   |
|                                   |   insights.                                           |
+-----------------------------------+-------------------------------------------------------+
| Threat Management                 | - **Detection Rules**                                 |
|                                   |                                                       |
|                                   |   - **IOC**---Identify specific hashes, IP addresses, |
|                                   |     domains, file names, and paths that indicate a    |
|                                   |     threat.                                           |
|                                   |                                                       |
|                                   |   - **BIOC**---Identify a specific network, process,  |
|                                   |     file, or registry activity that indicates a       |
|                                   |     threat.                                           |
|                                   |                                                       |
|                                   |   - **Correlations**---Analyze correlations of        |
|                                   |     multi-events from multiple sources.               |
|                                   |                                                       |
|                                   |   - **Indicator Rules**---Create rules based on       |
|                                   |     filters that are applied as either SHA256 and MD5 |
|                                   |     prevention rules in specific Agent Prevention     |
|                                   |     Profiles or as file, IP address, and domain       |
|                                   |     detection rules.                                  |
|                                   |                                                       |
|                                   | - **Threat Intelligence**                             |
|                                   |                                                       |
|                                   |   - **Indicators**---Indicators database. Search,     |
|                                   |     review, and interact with indicators including    |
|                                   |     IPs, domains, URLs, hashes, and more.             |
|                                   |                                                       |
|                                   |   - **Sample Analysis**---View detailed file sample   |
|                                   |     analysis results from PANW WildFire. Conduct      |
|                                   |     in-depth research and analysis of file sample     |
|                                   |     behaviors and characteristics based on WildFire's |
|                                   |     sandboxed detonation of the file.                 |
|                                   |                                                       |
|                                   |   - **Sessions & Submissions**---Access, search and   |
|                                   |     view firewall sessions and file sample submission |
|                                   |     data.                                             |
+-----------------------------------+-------------------------------------------------------+
| Posture Management                | - **Vulnerability Management**---View vulnerability   |
|                                   |   issues, vulnerable assets, vulnerabilities, and     |
|                                   |   vulnerability, and vulnerability intelligence.      |
|                                   |                                                       |
|                                   | - **Compliance**                                      |
|                                   |                                                       |
|                                   | - **Rules & Policies**---Create and edit rules and    |
|                                   |   policies for cloud workload, cloud security, and    |
|                                   |   vulnerability management.                           |
+-----------------------------------+-------------------------------------------------------+
| Inventory                         | - **Assets**                                          |
|                                   |                                                       |
|                                   |   - **All Assets**---Provides a central location from |
|                                   |     which you can view and investigate information    |
|                                   |     relating to assets in your network.               |
|                                   |                                                       |
|                                   |   - **Cloud**---Provides a unified, normalized asset  |
|                                   |     inventory for cloud assets in Google Cloud        |
|                                   |     Platform, Microsoft Azure, and Amazon Web         |
|                                   |     Services.                                         |
|                                   |                                                       |
|                                   |   - **Groups**---Create and view groups of assets     |
|                                   |     with shared attributes.                           |
|                                   |                                                       |
|                                   |   - **Network Configuration**---Define your internal  |
|                                   |     IP address ranges and domain names to identify    |
|                                   |     and track your network assets.                    |
|                                   |                                                       |
|                                   |   - **Asset Scores**---Investigate user and host      |
|                                   |     activities, and detect compromised accounts and   |
|                                   |     malicious devices using the Cortex XSIAM          |
|                                   |     calculated User and Host Scores.                  |
|                                   |                                                       |
|                                   | - **Endpoints**                                       |
|                                   |                                                       |
|                                   |   - **All Endpoints**---View and manage endpoints     |
|                                   |     that have registered with your Cortex XSIAM       |
|                                   |     instance.                                         |
|                                   |                                                       |
|                                   |   - **Groups**---Create endpoint groups to which you  |
|                                   |     can perform actions and assign the policy.        |
|                                   |                                                       |
|                                   |   - **Installations**---Create packages of the Cortex |
|                                   |     XSIAM agent software for deployment to your       |
|                                   |     endpoints.                                        |
|                                   |                                                       |
|                                   |   - **Host Inventory** ---Access comprehensive        |
|                                   |     insights into your system\'s components,          |
|                                   |     including applications, services, users, and      |
|                                   |     vulnerability assessments, to maintain visibility |
|                                   |     and security across your environment.             |
|                                   |                                                       |
|                                   |   - **Policy Management**---Configure your endpoint   |
|                                   |     security profiles and assign them to your         |
|                                   |     endpoints.                                        |
|                                   |                                                       |
|                                   |   - **Host Firewall**---Control communications on     |
|                                   |     your endpoints by applying sets of rules that     |
|                                   |     allow or block internal and external traffic.     |
|                                   |                                                       |
|                                   |   - **Device Control Violations**---Monitor all       |
|                                   |     instances where end users attempted to connect    |
|                                   |     restricted USB-connected devices and Cortex XDR   |
|                                   |     blocked them on the endpoint.                     |
|                                   |                                                       |
|                                   |   - **Disk Encryption Visibility**---View and manage  |
|                                   |     endpoints that were encrypted using BitLocker.    |
|                                   |                                                       |
|                                   |   - **Cloud Compliance (Legacy)**---Performs the      |
|                                   |     Center for Internet Security (CIS)                |
|                                   |     benchmarking compliance checks on endpoint        |
|                                   |     resources for Linux and Kubernetes agents.        |
+-----------------------------------+-------------------------------------------------------+
| Modules                           | - **AI Security**---Comprehensive overview of the AI  |
|                                   |   assets within an organization. Designed to ensure   |
|                                   |   AI security by offering tools to review and         |
|                                   |   prioritize AI risks effectively.                    |
|                                   |                                                       |
|                                   | - **Application Security**---Secures your             |
|                                   |   applications by identifying and prioritizing them   |
|                                   |   as a single, logical entity encompassing assets     |
|                                   |   across the entire software development lifecycle    |
|                                   |   (SDLC).                                             |
|                                   |                                                       |
|                                   | - **Attack Surface**---ASM helps you discover and     |
|                                   |   manage your public attack surface, providing        |
|                                   |   visibility into all of your digital assets,         |
|                                   |   including on-prem and cloud. Identify and remediate |
|                                   |   vulnerabilities, enforce compliance policies, and   |
|                                   |   reduce the risk of cyberattacks.                    |
|                                   |                                                       |
|                                   | - **Data Security**---Agentless multi-cloud data      |
|                                   |   security platform that discovers, classifies,       |
|                                   |   protects, and governs sensitive data.               |
|                                   |                                                       |
|                                   | - **Identity**---Runs a proprietary algorithm to      |
|                                   |   calculate effective permissions and entitlements of |
|                                   |   the identities across your cloud service providers  |
+-----------------------------------+-------------------------------------------------------+
| Marketplace                       | Marketplace enables you to install free content packs |
|                                   | to extend Cortex XSIAM.                               |
+-----------------------------------+-------------------------------------------------------+
| Managed Services                  | The Managed Threat Hunting service augments your      |
|                                   | security by providing 24/7, year-round monitoring by  |
|                                   | Palo Alto Networks threat researchers and Unit 42     |
|                                   | experts.                                              |
+-----------------------------------+-------------------------------------------------------+
| Copilot                           | Cortex Copilot is an AI tool specifically developed   |
|                                   | to streamline various processes, including case       |
|                                   | triaging, investigation, and remediation.             |
+-----------------------------------+-------------------------------------------------------+
| Quick Launcher                    | Open an in-context shortcut that you can use to       |
|                                   | search for information, perform common investigation  |
|                                   | tasks, or initiate response actions from any place in |
|                                   | the Cortex XSIAM console.                             |
+-----------------------------------+-------------------------------------------------------+
| Settings                          | From the **Settings** menu, you can view information  |
|                                   | about your Cortex XSIAM license, review logs of       |
|                                   | actions initiated by Cortex XSIAM analysts, health    |
|                                   | alerts, and manage Cortex XSIAM exceptions            |
|                                   | configuration, data sources, and system               |
|                                   | configurations.                                       |
+-----------------------------------+-------------------------------------------------------+
| Tenant Navigator                  | View and switch to tenants to which you have access   |
|                                   | divided per CSP account. You can also navigate        |
|                                   | directly to the Cortex Gateway.                       |
+-----------------------------------+-------------------------------------------------------+
| Notifications                     | View Cortex XSIAM notifications.                      |
+-----------------------------------+-------------------------------------------------------+
| Help                              | Cortex XSIAM offers in-product help providing you     |
|                                   | with guidance directly from within the Cortex XSIAM   |
|                                   | Management Console.                                   |
|                                   |                                                       |
|                                   | From the **Help**, you can choose:                    |
|                                   |                                                       |
|                                   | - **Documentation Portal** to open the Cortex Help    |
|                                   |   Center.                                             |
|                                   |                                                       |
|                                   | - Toggle on/off the **In-App Help Center**. If on,    |
|                                   |   the                                                 |
|                                   |   ![](media/rId176.png){width="0.23026246719160104in" |
|                                   |   height="0.20833333333333334in"} appears at the      |
|                                   |   bottom right side of the page.                      |
|                                   |                                                       |
|                                   | - **Submit a Support Case**                           |
|                                   |                                                       |
|                                   | Click                                                 |
|                                   | ![](media/rId176.png){width="0.23026246719160104in"   |
|                                   | height="0.20833333333333334in"} to open the Help      |
|                                   | Center. The topics listed in the panel reflect the    |
|                                   | current page opened in the Cortex XSIAM Management    |
|                                   | Console. You also have the option of entering a topic |
|                                   | or keyword in the search bar for any information you  |
|                                   | are looking for.                                      |
|                                   |                                                       |
|                                   | Click the star at the top right hand side of the      |
|                                   | topic to add to the list of favorites. The list of    |
|                                   | favorites is saved to the home page of the Cortex     |
|                                   | Help Center panel.                                    |
+-----------------------------------+-------------------------------------------------------+
| User                              | From the User, see who is logged into Cortex XSIAM.   |
|                                   |                                                       |
|                                   | - **About** to view additional version and tenant ID  |
|                                   |   information.                                        |
|                                   |                                                       |
|                                   | - **What's New in this Release** to view selected new |
|                                   |   features available for your license type.           |
|                                   |                                                       |
|                                   | - **What\'s New in XSIAM**                            |
|                                   |                                                       |
|                                   | - **Log Out** to terminate the connection with your   |
|                                   |   Cortex XSIAM Management Console.                    |
+-----------------------------------+-------------------------------------------------------+

**Filter page results**

To reduce the number of results, you can filter by any heading and
value. When you apply a filter, Cortex XSIAM displays the filter
criteria above the results table. You can also filter individual columns
for specific values using the icon to the right of the column heading.

Some fields also support additional operators such as **=**, **!=**,
**Contains**, **not Contains**, **\***, **!\***.

Filters are persistent. When you navigate away from the page and return,
any filter you added remains active.

To build a filter using one or more fields:

1.  From a Cortex XSIAM page, select filter
    (![](media/rId182.png){width="0.14583333333333334in"
    height="0.20833333333333334in"}).

- Cortex XSIAM adds the filter criteria above the top of the table.

2.  For each field, you would like to filter by:

    a.  Select or search the field.

    b.  Select the operator that matches the criteria.

    - Use **=** to include results that match the value you specify, or
      **!=** to exclude results that match the value.

    c.  Enter a value to complete the filter criteria.

    - > **Note**

      > CMD fields have a 128-character limit. Shorten longer query
      > strings to 127 characters and add an asterisk (\*).

      Alternatively, you can select **Include empty values** to create a
      filter that excludes or includes results when the field has empty
      values.

3.  To add additional filters, click **+AND,** within the filter
    brackets, to display results that must match all specified criteria,
    or **+OR** to display results that match any of the criteria.

4.  To see the results, click out of the filter area.

**Export results to file**

You can export the page results for most pages in Cortex XSIAM to a
tab-separated values (TSV) file.

1.  (**Optional**) Filter page results to reduce the number of results
    for export.

2.  Select export to file
    (![](media/rId185.png){width="0.14583333333333334in"
    height="0.20833333333333334in"}).

- Cortex XSIAM exports any results matching your applied filters in TSV
  format. The TSV format requires a tab separator, automatic detection
  does not work in the case of multi-event exports.

**Save and share views**

You can save and share view across your organization.

1.  Select one or more filters.

2.  Save (![](media/rId188.png){width="0.20833333333333334in"
    height="0.20833333333333334in"}) the active filter(s) as a view.

    a.  Enter a name to identify the view.

    - You can create multiple views with the same name. Saving a view
      with an existing name does not override the existing view.

    b.  Select whether to share the view.

After saving a view, you can set it as your default view, delete the
view, share the view, or unshare it if it is already shared. To access
these settings, click the down arrow next to **Choose View** and click
the three vertical dots menu for the specific view you want to manage.

> **Note**
>
> Deleting a shared view removes it for all users.

