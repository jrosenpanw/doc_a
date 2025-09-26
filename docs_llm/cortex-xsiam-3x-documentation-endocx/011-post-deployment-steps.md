## Post-deployment steps

Perform post-deployment tasks such as setting up your environment,
creating automation rules, and managing user roles and access
management.

### Perform health checks

As part of the onboarding process, it is recommended to perform the
following health checks:

- **Update prevention policies:** Update policies and profiles and
  ensure that all action modes are set to Block. For more information,
  see Set up endpoint profiles and exception rules in the Cortex XSIAM
  Administrator Guide.

- **Monitor operational status: ** Verify that Cortex XDR agents are
  protecting endpoints according to predefined security policies and
  profiles. For more information, see [Monitor agent operational status
  in Cortex XSIAM](#UUID834d8a10e55efbba8d8d1363f1b9506a).

- **Test sample malware:** Use a malware PE, MacOSX, or APK test file,
  to test end-to-end WildFire sample processing. For more information
  see, [Get a Malware Test
  File](https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api/get-wildfire-information-through-the-wildfire-api/get-a-malware-test-file-wildfire-api).

- **Validate detectors for issues and cases:** Check issues and their
  associated sources. Validate that all the configurations on the policy
  level and on the agent deployment level meet the requirements to
  generate alerts and cases on Cortex XSIAM. For example, check the
  following:

  - Cortex XDR agent generates WildFire malware issues.

  - NFGW issues are listed by PAN NGFW.

- **Validate log ingestion from external integrations:** Verify what
  datasets are being created. The **Dataset Management** page enables
  you to manage your datasets and understand your overall data storage
  duration for different retention periods and datasets based on your
  Hot and Cold Storage licenses, and retention add-ons to extend your
  storage. For more information, see [Data storage
  lifecycle](#UUID037d006bbc29ad8ae262676b49ae2a6b).

#### Monitor agent operational status in Cortex XSIAM

Cortex XSIAM provides you with information about the XDR agent
operational status on an endpoint and indicates whether the agent is
protecting according to its predefined security policies and profiles.
This can help you identify when the agent may suffer from a technical
issue or misconfiguration that interferes with the agent's protection
capabilities or interaction with Cortex XSIAM and other applications.

The XDR agent reports the operational status as follows:

- **Protected:** Indicates that the XDR agent is running as configured
  and did not report any exceptions to Cortex XSIAM.

- **Partially protected:** Indicates that the XDR agent reported one or
  more exceptions to Cortex XSIAM.

- **Unprotected:** Indicates the XDR agent is not enforcing protection
  on the endpoint.

- **Local Resource Impact:** Indicates that the XDR agent machine
  resources currently available for use, are not enough for the agent to
  operate smoothly.

You can monitor the Cortex XDR agent **Operational Status** in Endpoints
\> All Endpoints.

The operational status that the agent reports varies according to the
exceptions reported by the XDR agent.

+-----------------------------------+-----------------------------------+
| Status                            | Description                       |
+===================================+===================================+
| **Protected**                     | (*Windows, Mac, and Linux*)       |
|                                   | Indicates all protection modules  |
|                                   | are running as configured on the  |
|                                   | endpoint.                         |
+-----------------------------------+-----------------------------------+
| **Partially protected**           | *Windows*                         |
|                                   |                                   |
|                                   | - XDR data collection is not      |
|                                   |   running, or not set             |
|                                   |                                   |
|                                   | - Behavioral threat protection is |
|                                   |   not running                     |
|                                   |                                   |
|                                   | - Malware protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | - Exploit protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | *Mac*                             |
|                                   |                                   |
|                                   | - Operating system adaptive       |
|                                   |   mode\*                          |
|                                   |                                   |
|                                   | - XDR Data Collection is not      |
|                                   |   running, or not set             |
|                                   |                                   |
|                                   | - Behavioral threat protection is |
|                                   |   not running                     |
|                                   |                                   |
|                                   | - Malware protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | - Exploit protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | *Linux*                           |
|                                   |                                   |
|                                   | - Kernel module not loaded\*\*    |
|                                   |                                   |
|                                   | - Kernel module compatible but    |
|                                   |   not loaded\*\*                  |
|                                   |                                   |
|                                   | - Kernel version not              |
|                                   |   compatible\*\*                  |
|                                   |                                   |
|                                   | - XDR Data Collection is not      |
|                                   |   running, or not set             |
|                                   |                                   |
|                                   | - Behavioral threat protection is |
|                                   |   not running                     |
|                                   |                                   |
|                                   | - Anti-malware flow is            |
|                                   |   asynchronous                    |
|                                   |                                   |
|                                   | - Malware protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | - Exploit protection is not       |
|                                   |   running                         |
|                                   |                                   |
|                                   | <!-- -->                          |
|                                   |                                   |
|                                   | - > **Note**                      |
|                                   |                                   |
|                                   |   > Any of the listed items could |
|                                   |   > lead to a partially protected |
|                                   |   > state. Refer to the Cortex    |
|                                   |   > XSIAM management console for  |
|                                   |   > specific reasons for the      |
|                                   |   > state.                        |
+-----------------------------------+-----------------------------------+
| **Unprotected**                   | *Windows, Mac, and Linux*:        |
|                                   |                                   |
|                                   | - Behavioral threat protection    |
|                                   |   and Malware protection are not  |
|                                   |   running                         |
|                                   |                                   |
|                                   | - Exploit protection and malware  |
|                                   |   protection are not running      |
|                                   |                                   |
|                                   | - The content is unavailable.     |
+-----------------------------------+-----------------------------------+
| **Local Resource Impact**         | *Windows, Mac, Linux*             |
|                                   |                                   |
|                                   | - Machine CPU impact on the agent |
|                                   |   operation                       |
|                                   |                                   |
|                                   | - Machine memory impact on the    |
|                                   |   agent operation                 |
|                                   |                                   |
|                                   | In addition to the status, either |
|                                   | one of the following sub-statuses |
|                                   | appear:                           |
|                                   |                                   |
|                                   | - Low local available memory      |
|                                   |                                   |
|                                   | - No local available memory       |
+-----------------------------------+-----------------------------------+
| > **Caution**                     |                                   |
| >                                 |                                   |
| > Status can have the following   |                                   |
| > implications on the endpoint:   |                                   |
|                                   |                                   |
| - > \*(`Status`): The exploit     |                                   |
|   > protection module is not      |                                   |
|   > running.                      |                                   |
|                                   |                                   |
| - > \*\*(`Status`):               |                                   |
|                                   |                                   |
|   - > XDR data collection is not  |                                   |
|     > running                     |                                   |
|                                   |                                   |
|   - > Behavioral threat           |                                   |
|     > protection is not running   |                                   |
|                                   |                                   |
|   - > Anti-malware flow is        |                                   |
|     > asynchronous                |                                   |
|                                   |                                   |
|   - > Local privilege escalation  |                                   |
|     > protection is asynchronous  |                                   |
+-----------------------------------+-----------------------------------+

### Set up your environment

To create a more personalized user experience, Cortex XSIAM enables you
to customize and configure the following:

- Server settings

- Security settings

- Log forwarding

#### Configure server settings

You can configure server settings such as keyboard shortcuts, timezone,
and timestamp format, to create a more personalized user experience in
Cortex XSIAM. Go to Settings \> Configurations \> General \> Server
Settings.

> **Note**
>
> Keyboard shortcuts, timezone, and timestamp format are not set
> universally and only apply to the user who sets them.

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Server Setting                    | Description                                                                                                                               |
+===================================+===========================================================================================================================================+
| Keyboard Shortcuts                | Enables you to change the default shortcut settings.  The shortcut value must be a keyboard letter, A through Z, and cannot be the same   |
|                                   | for both shortcuts.                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Timezone                          | Select a specific timezone. The timezone affects the timestamps displayed in Cortex XSIAM, auditing logs, and when exporting files.       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Timestamp Format                  | The format in which to display Cortex XSIAM data. The format affects the timestamps displayed in Cortex XSIAM, auditing logs, and when    |
|                                   | exporting files.                                                                                                                          |
|                                   |                                                                                                                                           |
|                                   | This setting is configured per user and not per tenant.                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Email Contacts                    | A list of email addresses  Cortex XSIAM can use as a distribution list. The defined email addresses are used to send product              |
|                                   | maintenance, updates, and new version notifications. These addresses are in addition to email addresses registered with your Customer     |
|                                   | Support Portal account.                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Password Protection (for          | Enable password protection when downloading retrieved files from an endpoint. This prevents users from opening potentially malicious      |
| downloaded files)                 | files.                                                                                                                                    |
|                                   |                                                                                                                                           |
|                                   | Administrator permissions required.                                                                                                       |
|                                   |                                                                                                                                           |
|                                   | > **Note**                                                                                                                                |
|                                   | >                                                                                                                                         |
|                                   | > If the **Password Protection (for downloaded files)** setting under Settings \> Configuration \> General \> Server Settings is enabled, |
|                                   | > enter the password \'suspicious\' to download the file.                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Google Maps Key                   | Enter the Google Maps API key to display the physical location of an entity on a Google map.                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Scope-Based Access Control (SBAC) | Enforces granular scoping on users with a scoping configuration. A user can inherit scoping configurations from a user group, or have the |
|                                   | scoping configuration applied directly on top of the role assigned from either a user group or generated API Key.                         |
|                                   |                                                                                                                                           |
|                                   | By default, **Enable Scope Based Access Control** is disabled and granular scoping is not enforced. Before enabling SBAC, we recommend    |
|                                   | that an administrator or a user with **Access Management** permissions first ensures that the users, user groups, and API Keys defined in |
|                                   | Cortex XSIAM are granted the required access by assigning the relevant scopes. For more information, see [Manage user                     |
|                                   | scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).                                                                                            |
|                                   |                                                                                                                                           |
|                                   | (Optional) If enabled, you can select the **Endpoint Scoping Mode**, which is defined per tenant:                                         |
|                                   |                                                                                                                                           |
|                                   | - **Permissive:** Enables users with at least one scope tag to access the relevant entity with that same tag.                             |
|                                   |                                                                                                                                           |
|                                   | - **Restrictive:** Users must have all the scoped tags that are tagged within the relevant entity of the system.                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Data Ingestion Monitoring (Beta)  | Data ingestion health monitors the availability and overall health of data collection. When enabled, Cortex XSIAM creates the following   |
|                                   | types of alerts:                                                                                                                          |
|                                   |                                                                                                                                           |
|                                   | - **Ingestion health alerts:** Based on the data ingestion metrics and indicate disruptions in data collection                            |
|                                   |                                                                                                                                           |
|                                   | - **Collection health alerts:** Based on error statuses in collection integrations and indicate that a collector is not connected         |
|                                   |                                                                                                                                           |
|                                   | If you disable data ingestion monitoring, Cortex XSIAM continues to collect metrics, but alerts are not created.                          |
|                                   |                                                                                                                                           |
|                                   | **Related information**                                                                                                                   |
|                                   |                                                                                                                                           |
|                                   | - Use data ingestion health metrics in Cortex Query Language queries and to create correlation rules with your data ingestion logic. For  |
|                                   |   more information, see [Monitor data ingestion health](#UUID87fabbdc1cb768aac217c01716bb9832).                                           |
|                                   |                                                                                                                                           |
|                                   | - View all health alerts on the Health Alerts page. For more information, see [About health                                               |
|                                   |   issues](#UUIDdfd48b778b41de7955182409372663e9).                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| XQL Configuration                 | Enables setting case sensitivity across Cortex XSIAM.                                                                                     |
|                                   |                                                                                                                                           |
|                                   | By default, this setting is set to `false` and field values are evaluated as case insensitive.                                            |
|                                   |                                                                                                                                           |
|                                   | This setting overwrites any other default configuration except for BIOCs, which will remain case-insensitive no matter what this          |
|                                   | configuration is set to.                                                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Define the cases target MTTR per  | Determines within how many days and hours you want issues resolved according to the issue severity **Critical**, **High**, **Medium**,    |
| issue severity                    | and **Low**.                                                                                                                              |
|                                   |                                                                                                                                           |
|                                   | The defined MTTR is used to display the Resolved Issue MTTR dashboard widgets.                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Impersonation Role                | The type of role permissions granted to the Palo Alto Networks Support team when opening support tickets. We recommend that role          |
|                                   | permissions be granted only for a specific time frame, and full administrative permissions be granted only when specifically requested by |
|                                   | the Support team.                                                                                                                         |
|                                   |                                                                                                                                           |
|                                   | Role permissions include:                                                                                                                 |
|                                   |                                                                                                                                           |
|                                   | - **Read-only:** Default setting; grants read-only access to your tenant.                                                                 |
|                                   |                                                                                                                                           |
|                                   | - **Support-related actions:** Grants permissions to tech support file collection, dump file collection, investigation query, correlation |
|                                   |   rule, BIOC and IOC rule editing, alert starring, exclusion, and exception editing                                                       |
|                                   |                                                                                                                                           |
|                                   | - **Full role permissions:** No limitations are applied; grants full permissions to all actions and content on your tenant                |
|                                   |                                                                                                                                           |
|                                   | **Permission Reset Timeframe:** Determines how long role permissions are valid.                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Prisma Cloud Compute Tenant       | > **Note**                                                                                                                                |
| Pairing                           | >                                                                                                                                         |
|                                   | > Requires a Cortex XSIAM or Cortex XDR Pro license                                                                                       |
|                                   |                                                                                                                                           |
|                                   | To enable the capabilities of the Cloud Security Agent, the Prisma Cloud Compute tenant must be paired with an existing Cortex            |
|                                   | XSIAM tenant. Pairing is one-to-one, with the two tenants being in the same region.                                                       |
|                                   |                                                                                                                                           |
|                                   | For more information, see [Pairing Prisma Cloud with Cortex                                                                               |
|                                   | XSIAM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Documentation/Pairing-Prisma-Cloud-Compute-with-Cortex-XSIAM) |
|                                   | .                                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Custom Content                    | - **Export all custom content:** Exports custom content, such as playbooks and scripts as a content bundle, which you can import to       |
|                                   |   another Cortex XSIAM tenant.                                                                                                            |
|                                   |                                                                                                                                           |
|                                   | - **Upload custom content:** Imports custom content created from another Cortex XSIAM tenant.                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Issues                            | Create timer fields that display in the issues table and issue layouts. For more information, see [Configure issue timer                  |
|                                   | fields](#UUID468fe7f02dc4e45c77dec77741dd50e5).                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Indicators                        | > **Note**                                                                                                                                |
|                                   | >                                                                                                                                         |
|                                   | > Requires the TIM add-on.                                                                                                                |
|                                   | >                                                                                                                                         |
|                                   | > By default, system-wide automatic indicator extraction and enrichment is disabled. However, if you migrated from Cortex XSIAM 2.x       |
|                                   | > to Cortex XSIAM 3.x, system-wide automatic indicator extraction and enrichment is enabled.                                              |
|                                   |                                                                                                                                           |
|                                   | If you have the TIM add-on, you can enable or disable system-wide automatic indicator extraction and enrichment from issues.              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Unified Case View                 | > **Note**                                                                                                                                |
|                                   | >                                                                                                                                         |
|                                   | > Requires an MSSP License and RBAC permissions to Cases & Issues and Investigation & Response \> Automation.                             |
|                                   | >                                                                                                                                         |
|                                   | > This setting is available for the parent tenant only.                                                                                   |
|                                   |                                                                                                                                           |
|                                   | Enable the **Unified Case View** to see a consolidated view of all cases across your distributed environment and perform actions on child |
|                                   | tenants.                                                                                                                                  |
|                                   |                                                                                                                                           |
|                                   | If this setting is disabled, the **Cases** page displays a single tenant at a time with a drop down list to move between tenants in       |
|                                   | read-only mode.                                                                                                                           |
|                                   |                                                                                                                                           |
|                                   | For more information, see [Unified case view](#UUID4f6473efa9821e3d0efe39a89e559a39).                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

#### Configure security settings

You can configure security settings such as how long users can be logged
in Cortex XSIAM, and from which domains and IP ranges users can log in.

Go to Settings \> Configurations \> General \> Security Settings.

+-----------------------+-----------------------+-----------------------+
| Settings              | Options               | Description           |
+=======================+=======================+=======================+
| Session Expiration    | User Login Expiration | The number of hours   |
|                       |                       | (between 1 and 24)    |
|                       |                       | after which the       |
|                       |                       | user\'s login session |
|                       |                       | expires. You can also |
|                       |                       | choose to             |
|                       |                       | automatically log     |
|                       |                       | users out after a     |
|                       |                       | specified period of   |
|                       |                       | inactivity.           |
+-----------------------+-----------------------+-----------------------+
| Dashboard Expiration  | Whether the           |                       |
|                       | **Dashboard** page    |                       |
|                       | expires at the same   |                       |
|                       | time as the user      |                       |
|                       | login session or      |                       |
|                       | after seven days.     |                       |
|                       | This is useful when   |                       |
|                       | you view a dashboard  |                       |
|                       | on a separate screen. |                       |
|                       |                       |                       |
|                       | For example, if you   |                       |
|                       | select seven days for |                       |
|                       | dashboards and eight  |                       |
|                       | hours for login       |                       |
|                       | expiration, and you   |                       |
|                       | are currently viewing |                       |
|                       | the **Dashboard**     |                       |
|                       | page, the dashboard   |                       |
|                       | expiration takes      |                       |
|                       | priority (seven       |                       |
|                       | days). This ensures   |                       |
|                       | that the              |                       |
|                       | **Dashboard** page    |                       |
|                       | continues to display  |                       |
|                       | the widgets for an    |                       |
|                       | extended period.      |                       |
+-----------------------+-----------------------+-----------------------+
| Allowed Sessions      | Approved Domains      | The domains from      |
|                       |                       | which you want to     |
|                       |                       | allow user access     |
|                       |                       | (login) to Cortex     |
|                       |                       | XSIAM. You can add or |
|                       |                       | remove domains as     |
|                       |                       | necessary.            |
+-----------------------+-----------------------+-----------------------+
| Approved IP Ranges    | The IP ranges from    |                       |
|                       | which you want to     |                       |
|                       | allow user access     |                       |
|                       | (login) to Cortex     |                       |
|                       | XSIAM. You can also   |                       |
|                       | choose to limit API   |                       |
|                       | access from specific  |                       |
|                       | IP addresses.         |                       |
+-----------------------+-----------------------+-----------------------+
| User Expiration       | Deactivate Inactive   | Deactivate an         |
|                       | User                  | inactive user, and    |
|                       |                       | also set the user     |
|                       |                       | deactivation trigger  |
|                       |                       | period. By default,   |
|                       |                       | user expiration is    |
|                       |                       | disabled. When        |
|                       |                       | enabled, enter the    |
|                       |                       | number of days after  |
|                       |                       | which inactive users  |
|                       |                       | should be             |
|                       |                       | deactivated.          |
+-----------------------+-----------------------+-----------------------+
| Allowed Domains       | Domain Name           | The domain names that |
|                       |                       | can be used in your   |
|                       |                       | distribution lists    |
|                       |                       | for reports. For      |
|                       |                       | example, when         |
|                       |                       | generating a report,  |
|                       |                       | ensure the reports    |
|                       |                       | are not sent to email |
|                       |                       | addresses outside     |
|                       |                       | your organization.    |
+-----------------------+-----------------------+-----------------------+

#### Log forwarding

Logs provide information about events that occur in the system. These
logs are a valuable tool in troubleshooting issues that might arise in
your Cortex XSIAM tenant.

To stay informed about important alerts and events, you can configure
your notifications and specify the type of logs you want to forward. You
can choose to receive these notifications through an email account, a
Slack channel, or a syslog receiver.

##### Forward logs from Cortex XSIAM to external services

You can forward logs from Cortex XSIAM to an external service. This
allows you to stay updated on important issues and events. Available
services include the following:

- **Slack channel and/or syslog receiver:** Integrate the service with
  Cortex XSIAM. Once the integration is complete, configure notification
  forwarding, specifying the log type you want to forward.

- **Email distribution list:** Configure notification forwarding,
  specifying the log type you want to forward.

The following table shows the log types supported for each notification
type:

+-----------------+-----------------+-----------------+-----------------+
| Log Type        | Email           | Slack           | Syslog          |
+=================+=================+=================+=================+
| Issues          | ✓               | ✓               | ✓               |
+-----------------+-----------------+-----------------+-----------------+
| Agent Audit log | ✓               | ---             | ✓               |
|                 |                 |                 |                 |
| > **Note**      |                 |                 |                 |
| >               |                 |                 |                 |
| > Requires      |                 |                 |                 |
| > Cortex XDR    |                 |                 |                 |
| > per Endpoint  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Management      | ✓               | ---             | ✓               |
| Audit Log       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Data Ingestion  | ✓               | ✓               | ✓               |
| Health Issues   |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Reports         | ✓               | ✓               | ---             |
+-----------------+-----------------+-----------------+-----------------+

###### Integrate a syslog receiver

A syslog receiver can be a physical or virtual server, a SaaS solution,
or any service that accepts syslog messages.

To send Cortex XSIAM notifications to your syslog receiver, you first
need to define the settings for the syslog receiver. After this is
complete, you can configure notification forwarding.

**How to send logs to a syslog receiver**

Before you begin, enable access to the following Cortex XSIAM IP
addresses for your region in your firewall.

+-----------------------------------+-----------------------------------+
| Region                            | Log Forwarding IP Addresses       |
+===================================+===================================+
| United States - Americas (US)     | - 35.232.87.9                     |
|                                   |                                   |
|                                   | - 35.224.66.220                   |
+-----------------------------------+-----------------------------------+
| Germany (DE)                      | - 35.234.95.96                    |
|                                   |                                   |
|                                   | - 35.246.192.146                  |
+-----------------------------------+-----------------------------------+
| Netherlands - Europe (EU)         | - 34.90.202.186                   |
|                                   |                                   |
|                                   | - 34.90.105.250                   |
+-----------------------------------+-----------------------------------+
| Canada (CA)                       | - 35.203.54.204                   |
|                                   |                                   |
|                                   | - 35.203.52.255                   |
+-----------------------------------+-----------------------------------+
| United Kingdom (UK)               | - 34.105.227.105                  |
|                                   |                                   |
|                                   | - 34.105.149.197                  |
+-----------------------------------+-----------------------------------+
| Singapore (SG)                    | - 35.240.192.37                   |
|                                   |                                   |
|                                   | - 34.87.125.227                   |
+-----------------------------------+-----------------------------------+
| Japan (JP)                        | - 34.84.88.183                    |
|                                   |                                   |
|                                   | - 35.243.76.189                   |
+-----------------------------------+-----------------------------------+
| Australia (AU)                    | - 35.189.38.167                   |
|                                   |                                   |
|                                   | - 34.87.219.39                    |
+-----------------------------------+-----------------------------------+
| United States - Government        | - 104.198.222.185                 |
|                                   |                                   |
|                                   | - 35.239.59.210                   |
+-----------------------------------+-----------------------------------+
| India (IN)                        | - 34.93.247.41                    |
|                                   |                                   |
|                                   | - 34.93.183.131                   |
+-----------------------------------+-----------------------------------+
| Switzerland (CH)                  | - 34.65.228.95                    |
|                                   |                                   |
|                                   | - 34.65.74.83                     |
+-----------------------------------+-----------------------------------+
| Warsaw (PL)                       | - 34.118.45.145                   |
|                                   |                                   |
|                                   | - 34.118.126.170                  |
+-----------------------------------+-----------------------------------+
| Taiwan (TW)                       | - 35.234.2.208                    |
|                                   |                                   |
|                                   | - 35.185.171.91                   |
+-----------------------------------+-----------------------------------+
| Qatar (QT)                        | - 34.18.48.182                    |
|                                   |                                   |
|                                   | - 34.18.43.40                     |
+-----------------------------------+-----------------------------------+
| France (FA)                       | - 34.163.100.253                  |
|                                   |                                   |
|                                   | - 34.155.72.149                   |
+-----------------------------------+-----------------------------------+
| Israel (IL)                       | - 34.165.194.4                    |
|                                   |                                   |
|                                   | - 34.165.101.105                  |
+-----------------------------------+-----------------------------------+
| Saudi Arabia (SA)                 | - 34.166.50.215                   |
|                                   |                                   |
|                                   | - 34.166.55.72                    |
+-----------------------------------+-----------------------------------+
| Indonesia (ID)                    | - 34.101.248.99                   |
|                                   |                                   |
|                                   | - 34.101.176.232                  |
+-----------------------------------+-----------------------------------+
| Spain (ES)                        | - 34.175.83.90                    |
|                                   |                                   |
|                                   | - 34.175.230.150                  |
+-----------------------------------+-----------------------------------+
| Italy (IT)                        | - 34.154.0.173                    |
|                                   |                                   |
|                                   | - 34.154.71.94                    |
+-----------------------------------+-----------------------------------+
| South Korea (KR)                  | - 34.64.198.58                    |
|                                   |                                   |
|                                   | - 34.47.86.20                     |
+-----------------------------------+-----------------------------------+
| South Africa (ZA)                 | - 34.35.70.253                    |
|                                   |                                   |
|                                   | - 34.35.10.167                    |
+-----------------------------------+-----------------------------------+

1.  Select Settings \> Configurations \> Integrations \> External
    Applications.

2.  In **Syslog Servers**, click **+ New Server**.

3.  Define the following parameters:

+-----------------------------------+---------------------------------------------+
| Parameter                         | Description                                 |
+===================================+=============================================+
| Name                              | Unique name for the server profile.         |
+-----------------------------------+---------------------------------------------+
| Destination                       | IP address or fully qualified domain name   |
|                                   | (FQDN) of the syslog receiver.              |
+-----------------------------------+---------------------------------------------+
| Port                              | Port number on which to send syslog         |
|                                   | messages.                                   |
+-----------------------------------+---------------------------------------------+
| Facility                          | Select one of the syslog standard values.   |
|                                   | The value maps to how your syslog server    |
|                                   | uses the facility field to manage messages. |
|                                   | For details on the facility field, see [RFC |
|                                   | 5424](https://tools.ietf.org/html/rfc5424). |
+-----------------------------------+---------------------------------------------+
| Protocol                          | Method of communication with the syslog     |
|                                   | receiver:                                   |
|                                   |                                             |
|                                   | - **TCP:** No validation is made on the     |
|                                   |   connection with the syslog receiver.      |
|                                   |   However, if an error occurred with the    |
|                                   |   domain used to make the connection, the   |
|                                   |   **Test** connection will fail.            |
|                                   |                                             |
|                                   | - **UDP:** No error checking, error         |
|                                   |   correction, or acknowledgment. No         |
|                                   |   validation is done for the connection or  |
|                                   |   when sending data.                        |
|                                   |                                             |
|                                   | - **TCP + SSL:** Cortex XSIAM validates the |
|                                   |   syslog receiver certificate and uses the  |
|                                   |   certificate signature and public key to   |
|                                   |   encrypt the data sent over the            |
|                                   |   connection.                               |
+-----------------------------------+---------------------------------------------+
| Certificate                       | The communication between Cortex XSIAM and  |
|                                   | the syslog destination can use TLS. In this |
|                                   | case, upon connection, Cortex XSIAM         |
|                                   | validates that the syslog receiver has a    |
|                                   | certificate signed by either a trusted root |
|                                   | CA or a self-signed certificate. You may    |
|                                   | need to merge the Root and Intermediate     |
|                                   | certificate if you receive a certificate    |
|                                   | error when using a public certificate.      |
|                                   |                                             |
|                                   | If your syslog receiver uses a self-signed  |
|                                   | CA, upload your self-signed syslog receiver |
|                                   | CA. If you only use a trusted root CA leave |
|                                   | the certificate field empty.                |
|                                   |                                             |
|                                   | > **Note**                                  |
|                                   |                                             |
|                                   | - > Up to TLS 1.3 is supported.             |
|                                   |                                             |
|                                   | - > Make sure the self-signed CA includes   |
|                                   |   > your public key.                        |
|                                   |                                             |
|                                   | You can ignore certificate errors. For      |
|                                   | security reasons, this is not recommended.  |
|                                   | If you choose this option, logs will be     |
|                                   | forwarded even if the certificate contains  |
|                                   | errors.                                     |
+-----------------------------------+---------------------------------------------+

4.  Test the parameters to ensure a valid connection, and click
    **Create** when ready.

- You can define up to five syslog receivers. Upon success, the table
  displays the syslog servers and their status.

**What to do next**

After you integrate with your syslog receiver, configure your forwarding
settings. For more information see, [Configure notification
forwarding](#UUID3738ce324545c768e170afa247d5abc2).

####### Syslog receiver test message errors

When configuring a syslog message, Cortex XSIAM sends a test message. If
a test message cannot be sent, Cortex XSIAM displays an error message to
help you troubleshoot.

The following table includes descriptions and suggested solutions for
the error messages:

+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Error Message         | Description           | Suggested Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+=======================+=======================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Host Resolving Failed | The IP address or     | Ensure you have the correct IP address or the hostname.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                       | hostname you provided |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | doesn\'t exist, or    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | can\'t be resolved.   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configured Local      | The IP address or     | Ensure you have the correct IP address or the hostname.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Address               | hostname you provided |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | is internal and       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | can\'t be used.       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wrong Certificate     | The certificate you   | Re-create the certificate in the correct format, for example:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Format                | uploaded is in an     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | unexpected format and |     -----BEGIN CERTIFICATE-----MIIDHTCCAgWgAwIBAgIQSwieRyGdh6BNRQyp406bnTANBgkqhkiG9w0BAQsFADAhMR8wHQYDVQQDExZTVVJTLUNoYXJsaWVBbHBoYS1Sb290MB4XDTIwMDQzMDE4MjEzNFoXDTMwMDQzMDE4MzEzNFowITEfMB0GA1UEAxMWU1VSUy1DaGFybGllQWxwaGEtUm9vdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJHH2HR/CzVzm9lOIu6rrtF9opYeIJdtgJR2Le7w4M56lFKIoziAfZD9qR0DqXpAV+42PZC8Oe4ueweD44OKTnaofbOxQvygelvHkFyAj+oz0VppzhmeUXh1Eux96QKB+Q+vSm8FbNlBL2SI8RhceYsWtZe5vBm/zDdV2alO5LJ3rEj9ycG1a7re1wSDQ67NaSrny+C/7IL5utlVspcgjslEiGM7D30uKszpq3CCeV9f7aPHCVZbbFRBxe4cbgZjGvE7Mm1OBbsypMT3z8jmSj7Kz5ui6R8mlqtll5MkIGtvmc1aypJHKrobwcs2ozEmLiVR0F1oJrl+PIZy5MXhBUcCAwEAAaNRME8wCwYDVR0PBAQDAgGGMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFIJ1ZhG0dkgwF8OOB/eT4u/9yowaMBAGCSsGAQQBgjcVAQQDAgEAMA0GCSqGSIb3DQEBCwUAA4IBAQBvDQ4Epr0zxQHuyziDtlauddVsrLpckljHc+dCIhBvGMzGEj47Cb0c/eNt6tHrPThyzRxOHd9GBMX4AxLccPNuCZdWIRTgb4SYzDspGEYDK7v/N5+FvpYdWRgB4msUXhHt36ivH450XuY8Slt+qbQWNVU2+xIkMSSA3mUwnK+hz1GwO/Zc2JYOaVZUrW39EuzNePJ+O6BlgMRMRPNGzgT+xSxt316r/QnVA2sk4IXshdGGMG0VcuzBCyeuiCRP5/2QeFthas5EoXbdlB5eK3VzqLtiKyua/kS/hPuKahN9mI8FZ4TNB+nd6+eRQs2nsnbVOFmmOYu5KkGnDOjTzRh4-----END CERTIFICATE----- |
|                       | can\'t be used. The   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | certificate must be   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | an ASCII string or a  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | bytes-like object.    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connection Timed Out  | Cortex XSIAM didn't   | Check the firewall logs and the connection using WireShark.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | connect to the syslog |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | receiver in the       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | expected time. This   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | could be because your |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | firewall blocked the  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection or because |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the configuration of  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the syslog server     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | caused it to drop the |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection.           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connection Refused    | The syslog receiver   | Check the firewall logs and the connection using WireShark.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | refused the           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection. This      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | could be because your |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | firewall blocked the  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection or because |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the configuration of  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the syslog server     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | caused it to drop the |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection.           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connection Reset      | The connection was    | Check the firewall logs and the connection using WireShark.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | reset by the syslog   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | receiver. This could  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | be because your       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | firewall blocked the  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection or because |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the configuration of  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the syslog receiver   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | caused it to drop the |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection.           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Certificate           | The uploaded          | - Incorrect certificate: to check that the certificate you are uploading corresponds to the server syslog certificate, use the following openssl command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Verification Failed   | certificate couldn't  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | be verified for one   | <!-- -->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | of the following      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | reasons.              | - openssl verify -verbose -CAfile cortex_upload_certificate syslog_certificate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                       |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | - The certificate     |   If the certificate is correct, the result is `syslog_certificate: OK`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       |   doesn\'t correspond |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   to the certificate  | <!-- -->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       |   on the syslog       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   receiver and can\'t | - Incorrect hostname: make sure that the hostname/ip in the certificate matches the syslog server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                       |   be validated.       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |                       | - Certificate chain: If you are using a list of certificates, merge the chain into one certificate. You can concatenate the certificates using the following cat command in Linux or macOS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                       | - The certificate     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   doesn't have the    | <!-- -->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       |   correct hostname.   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |                       | - cat intermediate_cert root_cert > merged_syslog.crt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                       | - You are using a     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   certificate chain   |   If the concatenated certificate doesn't work, change the order of the root and intermediate certificates, and try again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                       |   and didn't merge    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   the certificates    |   To verify that the chain certificate was saved correctly, use the following openssl command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                       |   into one            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |   certificate.        |       openssl verify -verbose -CAfile cortex_upload_certificate syslog_certificate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                       |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       |                       |   If the certificate is correct, the result is `syslog_certificate: OK`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connection Terminated | The firewall or the   | Check the firewall logs and the connection using WireShark.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Abruptly              | syslog receiver       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | dropped the           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | unexpectedly. This    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | could be because the  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | firewall on the       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | customer side limits  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the number of         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connections, the      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | configuration on the  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | syslog receiver drops |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the connection, or    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | the network is        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | unstable.             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Host Unreachable      | The network           | Check the network configuration to make sure that everything is configured correctly like a firewall or a load balancer which may be accidentally directing the connection to a dead server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                       | configuration is      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | faulty and the        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | connection can\'t     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | reach the syslog      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                       | receiver.             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SSL Error             | Unknown SSL error.    | To investigate the issue, contact support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connection            | General error.        | To investigate the issue, contact support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Unavailable           |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### Integrate Slack for outbound notifications

Integrate Cortex XSIAM with your Slack workspace to manage and highlight
your issues and reports. Creating a Cortex XSIAM Slack channel ensures
that defined issues are exposed on laptop and mobile devices using the
Slack interface. Unlike email notifications, Slack channels provide
dedicated spaces where you can contact specific members regarding your
issues.

**How to integrate Slack with Cortex XSIAM**

1.  From Cortex XSIAM, select Settings \> Configurations \> Integrations
    \> External Applications.

2.  Select the provided link to install Cortex XSIAM on your Slack
    workspace.

- > **Note**

  > You are directed to the Slack browser to install Cortex XSIAM. You
  > can only use this link to install Cortex XSIAM on Slack. Attempting
  > to install from Slack Marketplace will redirect you to Cortex XSIAM
  > documentation.

3.  Click **Submit**.

- Upon successful installation, Cortex XSIAM displays the workspace to
  which you connected.

**What to do next**

After you integrate with your Slack workspace, configure your forwarding
settings. For more information see, [Configure notification
forwarding](#UUID3738ce324545c768e170afa247d5abc2).

###### Configure notification forwarding

After you integrate with an external service such as Slack or a syslog
receiver, create a forwarding configuration that specifies the log type
you want to forward. You can configure notifications for issues, agent
audit logs, and management audit logs. To receive notifications about
reports, see Create a report from scratch.

> **Prerequisite**
>
> Before you can select a syslog receiver or a Slack channel, you must
> integrate these external services with Cortex XSIAM.
>
> For more information, see:

- > [Integrate a syslog receiver](#UUID218d87cf0fa5bccd27b3bb119b0567ea)

- > [Integrate Slack for outbound
  > notifications](#UUID49a9a09cf0b44048aec98ff52278bda2)

**How to configure notifications**

1.  Select Settings \> Configurations \> General \> Notifications.

2.  Click **+ Add Forwarding Configuration**.

3.  Enter a name and description for the configuration.

4.  Select the log type you want to forward:

    - **Issues:** Send notifications for specific issue types.

    <!-- -->

    - > **Note**

      > To configure notification forwarding for issues by domain,
      > select **Log Type = Issues** and filter the Issues table by
      > **Issue Domain**.

    <!-- -->

    - **Agent Audit Logs:** Send notifications for audit logs reported
      by your Cortex XDR agents.

    - **Management Audit Logs:** Send notifications for audit logs about
      events related to your Cortex XSIAM tenant.

    - **Health Issues**---Send notifications for health issues. (for
      example, Ingestion, Event Forwarding, and Correlation rule
      errors).

    <!-- -->

    - > **Note**

      > This option will be deprecated in the next release. Configure
      > issues with the filter **Issue Domain = Health** instead.

    <!-- -->

    - **Cases**---Send notifications for specific cases (for example,
      Security or Posture cases)

5.  Click **Next**, and under **Scope**, filter the type of information
    you want included in a notification.

- For example, for a filter set to
  `Severity = Medium, Category = Configuration`, Cortex XSIAM sends the
  issues or events matching this filter as a notification.

6.  Click **Next**.

7.  (*Optional*) Define your email configuration:

    a.  In the **Distribution List**, add the email addresses to which
        you want to send email notifications.

    b.  In the **Grouping Timeframe**, define the time frame, in
        minutes, to specify how often Cortex XSIAM sends notifications.
        Every 20 issues or 20 events aggregated within this time frame
        are sent together in one notification, sorted according to
        severity. To send a notification when one issue or event is
        generated, set the time frame to `0`.

    c.  Choose whether you want Cortex XSIAM to provide an
        auto-generated subject.

    d.  Choose the format you want to send the email. If you choose
        **Alert**, you can choose the **Standard** or **Legacy** format.
        For more information about the legacy format, see [Log format
        for IOC and BIOC issues](#UUID724ff79edf21c9cbf29a8e2df5d7aec6).

8.  Depending on the notification integrations supported by the log
    type, configure the Slack channel or syslog receiver notification
    settings. For a list of log types supported in each notification
    type, see [Forward logs from Cortex XSIAM to external
    services](#UUID8cf9dc23530e9c2389bc9ebfccd6b949).

    a.  Enter the Slack channel name and select from the list of
        available channels. Slack channels are managed independently of
        Cortex XSIAM in your Slack workspace. After integrating your
        Slack account with your Cortex XSIAM tenant, Cortex XSIAM
        displays a list of specific Slack channels associated with the
        integrated Slack workspace.

    b.  Select a syslog receiver. Cortex XSIAM displays the list of
        receivers integrated with your Cortex XSIAM tenant.

    c.  Choose the format you want to send the syslog. If you choose
        **Alert**, you can choose the **Standard** or **Legacy** format.
        For more information about the legacy format, see [Log format
        for IOC and BIOC issues](#UUID724ff79edf21c9cbf29a8e2df5d7aec6).

9.  Click **Done** to create the forwarding configuration.

- > **Note**

  > When a notification is sent for each configured format.

###### Monitor administrative activity

From Settings \> Management Audit Logs, you can track the status of all
administrative and investigative actions. Cortex XSIAM stores audit logs
for 365 days (instead of 180 days, which was the retention period in the
past). Use the page filters to narrow the results or manage tables to
add or remove fields as needed.

To ensure you and your colleagues stay informed about administrative
activity, you can configure notification forwarding to forward your
Management Audit log to an email distribution list, Syslog server, or
Slack channel.

The following table describes the default **and optional fields** that
you can view in alphabetical order.

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Email                             | Email address of the              |
|                                   | administrative user               |
+-----------------------------------+-----------------------------------+
| Description                       | Descriptive summary of the        |
|                                   | administrative action. Hover over |
|                                   | this field to view more detailed  |
|                                   | information in a popup tooltip.   |
|                                   | This enables you to know exactly  |
|                                   | what has changed, and, if         |
|                                   | necessary, roll back the change.  |
+-----------------------------------+-----------------------------------+
| Host Name                         | Name of any relevant affected     |
|                                   | hosts                             |
+-----------------------------------+-----------------------------------+
| ID                                | Unique ID of the action           |
+-----------------------------------+-----------------------------------+
| Result                            | Result of the administrative      |
|                                   | action: Success, Partial, or      |
|                                   | Fail.                             |
+-----------------------------------+-----------------------------------+
| Subtype                           | Subcategory of action             |
+-----------------------------------+-----------------------------------+
| Timestamp                         | Time and date of the action       |
+-----------------------------------+-----------------------------------+
| Type                              | Type of activity logged, one of   |
|                                   | the following:                    |
|                                   |                                   |
|                                   | - Agent Configuration:            |
|                                   |   Configuration of a particular   |
|                                   |   Cortex XDR agent on a           |
|                                   |   particular endpoint.            |
|                                   |                                   |
|                                   | - Agent Installation:             |
|                                   |   Installation of the Cortex XDR  |
|                                   |   agent on a particular endpoint. |
|                                   |                                   |
|                                   | - Alert Exclusions: Suppression   |
|                                   |   of particular issues from       |
|                                   |   Cortex XSIAM .                  |
|                                   |                                   |
|                                   | - Alert Fields: Modification of   |
|                                   |   issue fields.                   |
|                                   |                                   |
|                                   | - Alert Layouts: Modification of  |
|                                   |   issue layouts.                  |
|                                   |                                   |
|                                   | - Alert Layout Rules:             |
|                                   |   Modification of issue layout    |
|                                   |   rules.                          |
|                                   |                                   |
|                                   | - Alert Notifications:            |
|                                   |   Modification of the format or   |
|                                   |   timing of issues.               |
|                                   |                                   |
|                                   | - Alert Rules: Modification of    |
|                                   |   issue rules.                    |
|                                   |                                   |
|                                   | - API Key: Modification of the    |
|                                   |   Cortex XSIAM API key.           |
|                                   |                                   |
|                                   | - Authentication: User sessions   |
|                                   |   started, along with the user    |
|                                   |   name that started the session.  |
|                                   |                                   |
|                                   | - Broker API: Operation related   |
|                                   |   to the Broker application       |
|                                   |   programming interface (API).    |
|                                   |                                   |
|                                   | - Broker VM: Operation related to |
|                                   |   the Broker virtual machine      |
|                                   |   (VM).                           |
|                                   |                                   |
|                                   | - Dashboards: Use of particular   |
|                                   |   dashboards.                     |
|                                   |                                   |
|                                   | - Device Control Permanent        |
|                                   |   Exceptions: Modification of     |
|                                   |   permanent device control        |
|                                   |   exceptions.                     |
|                                   |                                   |
|                                   | - Device Control Profile:         |
|                                   |   Modification of a device        |
|                                   |   control profile.                |
|                                   |                                   |
|                                   | - Device Control Temporary        |
|                                   |   Exceptions: Modification of     |
|                                   |   temporary device control        |
|                                   |   exceptions.                     |
|                                   |                                   |
|                                   | - Disk Encryption Profile:        |
|                                   |   Modification of a disk          |
|                                   |   encryption profile.             |
|                                   |                                   |
|                                   | - Endpoint Administration:        |
|                                   |   Management of endpoints.        |
|                                   |                                   |
|                                   | - Endpoint Groups: Management of  |
|                                   |   endpoint groups.                |
|                                   |                                   |
|                                   | - Extensions Policy: Modification |
|                                   |   of extension policy settings,   |
|                                   |   including host firewall and     |
|                                   |   disk encryption.                |
|                                   |                                   |
|                                   | - Extensions Profiles:            |
|                                   |   Modification of extension       |
|                                   |   profile settings.               |
|                                   |                                   |
|                                   | - Global Exceptions: Management   |
|                                   |   of global exceptions.           |
|                                   |                                   |
|                                   | - Host Firewall Profile:          |
|                                   |   Modification of a host firewall |
|                                   |   profile.                        |
|                                   |                                   |
|                                   | - Host Insights: Initiation of    |
|                                   |   Host Insights data collection   |
|                                   |   scan (Host Inventory and        |
|                                   |   Vulnerability Assessment).      |
|                                   |                                   |
|                                   | - Case Management: Actions taken  |
|                                   |   on cases and on the assets,     |
|                                   |   issues, and artifacts in cases. |
|                                   |                                   |
|                                   | - Ingest Data: Import of data for |
|                                   |   immediate use or storage in a   |
|                                   |   database.                       |
|                                   |                                   |
|                                   | - Integrations: Integration       |
|                                   |   operations, such as integrating |
|                                   |   Slack for outbound              |
|                                   |   notifications.                  |
|                                   |                                   |
|                                   | - Licensing: Any                  |
|                                   |   licensing-related operation.    |
|                                   |                                   |
|                                   | - Live Terminal: Remote terminal  |
|                                   |   sessions created and actions    |
|                                   |   taken in the file manager or    |
|                                   |   task manager, a complete        |
|                                   |   history of commands issued,     |
|                                   |   their success, and the          |
|                                   |   response.                       |
|                                   |                                   |
|                                   | - Managed Threat Hunting:         |
|                                   |   Activity relating to managed    |
|                                   |   threat hunting.                 |
|                                   |                                   |
|                                   | - MSSP: Management of security    |
|                                   |   services providers.             |
|                                   |                                   |
|                                   | - Policy & Profiles: Activity     |
|                                   |   related to managing policies    |
|                                   |   and profiles.                   |
|                                   |                                   |
|                                   | - Prevention Policy Rules:        |
|                                   |   Modification of prevention      |
|                                   |   policy rules.                   |
|                                   |                                   |
|                                   | - Protection Policy: Modification |
|                                   |   of the protection policy.       |
|                                   |                                   |
|                                   | - Protection Profile:             |
|                                   |   Modification of the protection  |
|                                   |   profile.                        |
|                                   |                                   |
|                                   | - Public API: Authentication      |
|                                   |   activity using an associated    |
|                                   |   Cortex XSIAM API key.           |
|                                   |                                   |
|                                   | - Query Center: Operations in the |
|                                   |   Query Center.                   |
|                                   |                                   |
|                                   | - Remediation: Remediation        |
|                                   |   operations.                     |
|                                   |                                   |
|                                   | - Reporting: Any reporting        |
|                                   |   activity.                       |
|                                   |                                   |
|                                   | - Response: Remedial actions      |
|                                   |   taken. For example: Isolate a   |
|                                   |   host, undo host isolation, add  |
|                                   |   a file hash signature to the    |
|                                   |   block list, or undo the         |
|                                   |   addition to the block list.     |
|                                   |                                   |
|                                   | - Rules: Modification of rules.   |
|                                   |                                   |
|                                   | - Rules Exceptions: Creation,     |
|                                   |   editing, or deletion under      |
|                                   |   Rules exceptions.               |
|                                   |                                   |
|                                   | - SaaS Collection: Any collected  |
|                                   |   SaaS data.                      |
|                                   |                                   |
|                                   | - Script Execution: Any script    |
|                                   |   execution.                      |
|                                   |                                   |
|                                   | - Starred Cases: Modification of  |
|                                   |   starred cases.                  |
|                                   |                                   |
|                                   | - Vulnerability Assessment: Any   |
|                                   |   vulnerability assessment        |
|                                   |   activity.                       |
+-----------------------------------+-----------------------------------+
| User Name                         | The user who performed the        |
|                                   | action.                           |
+-----------------------------------+-----------------------------------+

##### Log notification formats

When Cortex XSIAM issues and audit logs are forwarded to an external
data source, notifications are sent according to the necessary format
(syslog messages, email, or Slack notifications). If you prefer Cortex
XSIAM to forward logs in legacy format, select the legacy option in your
log forwarding configuration.

###### Management audit log messages

Cortex XSIAM management audit log messages are sent based on the various
log types, for example, Action Center, Issue Rules, or Authentication.

List of log types

- Action Center

- Agent Configuration

- Agent Exception Rules

- Issue Exclusion

- Issue Management

- Issue Notifications

- Issue Rules

- Issue Exclusions

- Allowed Domains

- API Key

- Apps

- Asset Inventory

- Asset Roles

- Asset Tag Rules

- Asset Uploads

- Authentication

- Automation Rules

- Automation Settings

- Broker API

- Broker VMs

- Business Unit Change

- SaaS Collection

- Custom Fields

- Dashboards

- Datasets

- Dataset Views

- Data Retention

- Device Control Custom Device

- Device Control Permanent Exceptions

- Extensions Policy Rules

- Device Control Profile

- Device Control Temporary Exceptions

- Agent Installation

- EDL Management

- Effective IP Ranges

- Endpoint Groups

- Endpoint Administration

- Event Forwarding

- Device Control Violations

- Device Permanent Exceptions

- Device Temp Exceptions

- Disk Encryption Visibility

- Featured Alert Fields

- Forensics

- Global Exceptions

- Host Insights

- Disk Encryption Profile

- Host Firewall

- Host Firewall Profile

- Incident Domains

- Incident Layout Rules

- Incident Management

- Incident Properties

- Incident Timeline Event

- Indicator rules

- Ingest Data

- Integrations

- Layout Rules

- Licensing

- Live Terminal

- Lookups

- Managed Detection & Response

- Managed Threat Hunting

- MSSP

- Permissions

- Playbook Triggers

- Policy & Profiles

- Prevention Policy Rules

- Prisma Integration

- Extensions Profile

- Public API

- Query Center

- Query Library

- Remediation

- Remediation Path Rules

- Reporting

- Response

- Rules

- Rules Exceptions

- Scoring Rules

- XDR Collector Configuration

- XDR Collectors Groups

- XDR Collectors Policy

- XDR Collectors Profile

- Script Execution

- Security Settings

- Server Settings

- Starred Incidents

- Support

- System

- Tenant Takeover

- Vulnerability Assessment

- Vulnerability Tests

- XCloud Integration

- XDM Config

- XQL Parsing Rules

- Public API

- Cortex Automation

  - Sub Type---Command - War Room

    - Status---Success

    - Severity---Informational

    - Details---
      `IncidentID:({ID}), IncidentType:({type}), IncidentName:({name}), Command:({command}), Arguments:({arg1})="arg1val" ({arg2})="arg2val" ({argn})="argnval", ID: ({num})`

  - Sub Type---Command - Playground

    - Status---Success

    - Severity---Informational

- XSOAR Migration

###### Issue notification format

Cortex XDR agent, BIOC, IOC, analytics, correlation, and third-party
issues are forwarded to external data resources according to the email,
Slack, or syslog format.

####### Email account

Cortex XSIAM sends issue notifications to email accounts based on the
settings you configure. Email messages also include an issue code
snippet of the fields according to the columns in the Issue table.

The notification format is as follows:

- If only one issue exists in the queue, a single-issue email format is
  sent.

- If more than one issue was grouped in the time frame, all the issues
  in the queue are forwarded together in a grouped email format.

 

Single-issue email message

    Email Subject: Issue: <issue_name>
        Email Body:
            Issue Name: Suspicious Process Creation
            Severity: High
            Source: Correlation
            Category: Malware 
            Action: Detected
            Host: <host name>
            Username:<user name>
            Excluded: No
            Starred: Yes 
            Issue: <link to the tenant issue view>
            Case: <link to the tenant case view>

 

Grouped issue email message

    Email Subject: Issues: <first_highest_severity_issue> + x others
        Email Body:
           Issue Name: Suspicious Process Creation
           Severity: High
           Source: Correlation
           Category: MalwareAction: Detected
           Host: <host name>
           Username:<user name>
           Excluded:No
           Starred: Yes
           Issue: <link to the tenant issue view>
               Case: <link to the tenant case view>
           Issue Name: Behavioral Threat Protection
           Issue ID: 2412
           Description: A really cool detection
           Severity: Medium
           Source: Correlation
           Category: Exploit
           Action: Prevented
           Host: <host name>
           Starred: Yes
           Case: <link to the tenant issue view>
           Issue: <link to the tenant case view>
           Notification Name: “My notification policy 2 ”
           Notification Description: “Starred issues with medium severity”

 

Email body

    {
        "original_issue_json":{
            "uuid":"<UUID Value>",
            "recordType":"threat",
            "customerId":"<Customer ID>",
            "severity":4,
            "...",
            
        "is_pcap":null,
        "contains_featured_host":[
            "NO"
        ],
        "contains_featured_user":[
            "YES"
        ],
        "contains_featured_ip":[
            "YES"
        ],
        "events_length":1,
        "is_excluded":false
        
    }

####### Slack channel

You can send issue notifications to a single Slack contact or a Slack
channel. Notifications are similar to the email format.

####### Syslog receiver

Issue notifications forwarded to a syslog receiver are sent in a CEF
format RF 5425.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Section                             Description
  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Syslog header                       `<9>: PRI (considered a priority field)1: version number2020-03-22T07:55:07.964311Z: timestamp of when alert/log was sentcortexxdr: host name`

  CEF header                          `HEADER/Vendor="Palo Alto Networks" (as a constant string)HEADER/Device Product="Cortex XDR" (as a constant string)HEADER/Product Version= Cortex XDR version (2.0/2.1....)HEADER/Severity=(integer/0 - Unknown, 6 - Low, 8 - Medium, 9 - High)HEADER/Device Event Class ID=alert sourceHEADER/name =alert name`

  CEF body                            `end=timestamp shost=endpoint_name deviceFacility=facility cat=category externalId=external_id request=request cs1=initiated_by_process cs1Label=Initiated by (constant string) cs2=initiator_commande cs2Label=Initiator CMD (constant string) cs3=signature cs3Label=Signature (constant string) cs4=cgo_name cs4Label=CGO name (constant string) cs5=cgo_command cs5Label=CGO CMD (constant string) cs6=cgo_signature cs6Label=CGO Signature (constant string) dst=destination_ip dpt=destination_port src=source_ip spt=source_port fileHash=file_hash filePath=file_path targetprocesssignature=target_process_signature tenantname=tenant_name tenantCDLid=tenant_id CSPaccountname=account_name initiatorSha256=initiator_hash initiatorPath=initiator_path osParentName=parent_name osParentCmd=parent_command osParentSha256=parent_hash osParentSignature=parent_signature osParentSigner=parent_signer incident=incident_id act=action suser=actor_effective_username`
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    end=timestamp shost=endpoint_name deviceFacility=facility cat=category externalId=external_id request=request cs1=initiated_by_process cs1Label=Initiated by (constant string) cs2=initiator_commande cs2Label=Initiator CMD (constant string) cs3=signature cs3Label=Signature (constant string) cs4=cgo_name cs4Label=CGO name (constant string) cs5=cgo_command cs5Label=CGO CMD (constant string) cs6=cgo_signature cs6Label=CGO Signature (constant string) dst=destination_ip dpt=destination_port src=source_ip spt=source_port fileHash=file_hash filePath=file_path targetprocesssignature=target_process_signature tenantname=tenant_name tenantCDLid=tenant_id CSPaccountname=account_name initiatorSha256=initiator_hash initiatorPath=initiator_path osParentName=parent_name osParentCmd=parent_command osParentSha256=parent_hash osParentSignature=parent_signature osParentSigner=parent_signer incident=incident_id act=action suser=actor_effective_username

###### Agent Audit log notification format

Cortex XSIAM forwards the Agent Audit log to these external data
resources:

- **Email account:** Sent according to the settings you configured

- **Syslog receiver:** Sent in a [CEF format RFC
  5425](https://tools.ietf.org/html/rfc5425) according to the following
  mapping:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Section                             Description
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Syslog header                       `<9>: PRI (considered a prioirty field)1: version number2020-03-22T07:55:07.964311Z: timestamp of when issue/log was sentcortexxdr: host name`

  CEF hHeader                         `HEADER/Vendor="Palo Alto Networks" (as a constant string)HEADER/Device Product="Cortex XDR Agent" (as a constant string)HEADER/Device Version= Cortex XDR Agent version (7.0/7.1....)HEADER/Severity=(integer/0 - Unknown, 6 - Low, 8 - Medium, 9 - High)HEADER/Device Event Class ID="Agent Audit Logs" (as a constant string)HEADER/name = type`

  CEF body                            `dvchost=domain shost=endpoint_name cat=category end=timestamp rt=received_time cs1Label=agentversion (constant string) cs1=agent_version cs2Label=subtype (constant string) cs2=subtype cs3Label=result (constant string) cs3=result cs4Label=reason (constant string) cs4=reason msg=event_description tenantname=tenant_name tenantCDLid=tenant_id CSPaccountname=csp_id`
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    <182>1 2020-10-04T10:41:14.608731Z cortexxdr - - - - CEF:0|Palo Alto Networks|Cortex XDR Agent|Cortex XDR Agent 7.2.0.63060|Agent Audit Logs|Agent Service|9|dvchost=WORKGROUP shost=Test-Agent cat=Monitoring end=1601808073102 rt=1601808074596 cs1Label=agentversion cs1=7.2.0.63060 cs2Label=subtype cs2=Stop cs3Label=result cs3=N\/A cs4Label=reason cs4=None msg=XDR service cyserver was stopped on Test-Agent tenantname=Test tenantCDLid=123456 CSPaccountname=1234

###### Management Audit log notification format

Cortex XSIAM forwards the Management Audit log to these external data
sources:

- **Email account:** Sent according to the settings you configured

- **Syslog receiver:** Sent in a [CEF format RFC
  5425](https://tools.ietf.org/html/rfc5425) according to the following
  mapping:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Section                             Description
  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Syslog header                       `<9>: PRI (considered a prioirty field)1: version number2020-03-22T07:55:07.964311Z: timestamp of when issue /log was sentcortexxdr: host name`

  CEF header                          `HEADER/Vendor="Palo Alto Networks" (as a constant string)HEADER/Device Product="Cortex XDR" (as a constant string)HEADER/Device Version= Cortex XDR version (2.0/2.1....)HEADER/HEADER/Severity=(integer/0 - Unknown, 6 - Low, 8 - Medium, 9 - High)HEADER/Device Event Class ID="Management Audit Logs" (as a constant string)HEADER/name = type`

  CEF body                            `suser=user end=timestamp externalId=external_id cs1Label=email (constant string) cs1=user_mail cs2Label=subtype (constant string) cs2=subtype cs3Label=result (constant string) cs3=result cs4Label=reason (constant string) cs4=reason msg=event_description tenantname=tenant_name tenantCDLid=tenant_id CSPaccountname=csp_id`
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    3/18/2012:05:17.567 PM<14>1 2020-03-18T12:05:17.567590Z cortexxdr - - - CEF:0|Palo Alto Networks|Cortex XDR|Cortex XDR x.x |Management Audit Logs|REPORTING|6|suser=test end=1584533117501 externalId=5820 cs1Label=email cs1=test@paloaltonetworks.com cs2Label=subtype cs2=Slack Report cs3Label=result cs3=SUCCESS cs4Label=reason cs4=None msg=Slack report 'scheduled_1584533112442' ID 00 to ['CUXM741BK', 'C01022YU00L', 'CV51Y1E2X', 'CRK3VASN9'] tenantname=test tenantCDLid=11111 CSPaccountname=00000

###### Log format for IOC and BIOC issues

Cortex XSIAM logs IOC and BIOC issues. If you configure Cortex XSIAM to
forward logs in the legacy format, when issue logs are forwarded from
Cortex XSIAM, each log record has the following format:

- **Email account:** Each field is labeled, one line per field.

<!-- -->

- edrData/action_country: 
      edrData/action_download: 
      edrData/action_external_hostname: 
      edrData/action_external_port: 
      edrData/action_file_extension: pdf
      edrData/action_file_md5: null
      edrData/action_file_name: XORXOR2614081980.pdf
      ...
      xdr_sub_type: BIOC - Credential Access
      bioc_category_enum_key: null
      alert_action_status: null
      agent_data_collection_status: null
      attempt_counter: null
      case_id: null
      global_content_version_id: 
      global_rule_id: 
      is_whitelisted: false

<!-- -->

- **Syslog format**

<!-- -->

- "/edrData/action_country","/edrData/action_download","/edrData/action_external_hostname","/edrData/action_external_port","/edrData/action_file_extension","/edrData/action_file_md5","/edrData/action_file_name","/edrData/action_file_path","/edrData/action_file_previous_file_extension","/edrData/action_file_previous_file_name","/edrData/action_file_previous_file_path","/edrData/action_file_sha256","/edrData/action_file_size","/edrData/action_file_remote_ip","/edrData/action_file_remote_port","/edrData/action_is_injected_thread","/edrData/action_local_ip","/edrData/action_local_port","/edrData/action_module_base_address","/edrData/action_module_image_size","/edrData/action_module_is_remote","/edrData/action_module_is_replay","/edrData/action_module_path","/edrData/action_module_process_causality_id","/edrData/action_module_process_image_command_line","/edrData/action_module_process_image_extension","/edrData/action_module_process_image_md5","/edrData/action_module_process_image_name","/edrData/action_module_process_image_path","/edrData/action_module_process_image_sha256","/edrData/action_module_process_instance_id","/edrData/action_module_process_is_causality_root","/edrData/action_module_process_os_pid","/edrData/action_module_process_signature_product","/edrData/action_module_process_signature_status","/edrData/action_module_process_signature_vendor","/edrData/action_network_connection_id","/edrData/action_network_creation_time","/edrData/action_network_is_ipv6","/edrData/action_process_causality_id","/edrData/action_process_image_command_line","/edrData/action_process_image_extension","/edrData/action_process_image_md5","/edrData/action_process_image_name","/edrData/action_process_image_path","/edrData/action_process_image_sha256","/edrData/action_process_instance_id","/edrData/action_process_integrity_level","/edrData/action_process_is_causality_root","/edrData/action_process_is_replay","/edrData/action_process_is_special","/edrData/action_process_os_pid","/edrData/action_process_signature_product","/edrData/action_process_signature_status","/edrData/action_process_signature_vendor","/edrData/action_proxy","/edrData/action_registry_data","/edrData/action_registry_file_path","/edrData/action_registry_key_name","/edrData/action_registry_value_name","/edrData/action_registry_value_type","/edrData/action_remote_ip","/edrData/action_remote_port","/edrData/action_remote_process_causality_id","/edrData/action_remote_process_image_command_line","/edrData/action_remote_process_image_extension","/edrData/action_remote_process_image_md5","/edrData/action_remote_process_image_name","/edrData/action_remote_process_image_path","/edrData/action_remote_process_image_sha256","/edrData/action_remote_process_is_causality_root","/edrData/action_remote_process_os_pid","/edrData/action_remote_process_signature_product","/edrData/action_remote_process_signature_status","/edrData/action_remote_process_signature_vendor","/edrData/action_remote_process_thread_id","/edrData/action_remote_process_thread_start_address","/edrData/action_thread_thread_id","/edrData/action_total_download","/edrData/action_total_upload","/edrData/action_upload","/edrData/action_user_status","/edrData/action_username","/edrData/actor_causality_id","/edrData/actor_effective_user_sid","/edrData/actor_effective_username","/edrData/actor_is_injected_thread","/edrData/actor_primary_user_sid","/edrData/actor_primary_username","/edrData/actor_process_causality_id","/edrData/actor_process_command_line","/edrData/actor_process_execution_time","/edrData/actor_process_image_command_line","/edrData/actor_process_image_extension","/edrData/actor_process_image_md5","/edrData/actor_process_image_name","/edrData/actor_process_image_path","/edrData/actor_process_image_sha256","/edrData/actor_process_instance_id","/edrData/actor_process_integrity_level","/edrData/actor_process_is_special","/edrData/actor_process_os_pid","/edrData/actor_process_signature_product","/edrData/actor_process_signature_status","/edrData/actor_process_signature_vendor","/edrData/actor_thread_thread_id","/edrData/agent_content_version","/edrData/agent_host_boot_time","/edrData/agent_hostname","/edrData/agent_id","/edrData/agent_ip_addresses","/edrData/agent_is_vdi","/edrData/agent_os_sub_type","/edrData/agent_os_type","/edrData/agent_session_start_time","/edrData/agent_version","/edrData/causality_actor_causality_id","/edrData/causality_actor_effective_user_sid","/edrData/causality_actor_effective_username","/edrData/causality_actor_primary_user_sid","/edrData/causality_actor_primary_username","/edrData/causality_actor_process_causality_id","/edrData/causality_actor_process_command_line","/edrData/causality_actor_process_execution_time","/edrData/causality_actor_process_image_command_line","/edrData/causality_actor_process_image_extension","/edrData/causality_actor_process_image_md5","/edrData/causality_actor_process_image_name","/edrData/causality_actor_process_image_path","/edrData/causality_actor_process_image_sha256","/edrData/causality_actor_process_instance_id","/edrData/causality_actor_process_integrity_level","/edrData/causality_actor_process_is_special","/edrData/causality_actor_process_os_pid","/edrData/causality_actor_process_signature_product","/edrData/causality_actor_process_signature_status","/edrData/causality_actor_process_signature_vendor","/edrData/event_id","/edrData/event_is_simulated","/edrData/event_sub_type","/edrData/event_timestamp","/edrData/event_type","/edrData/event_utc_diff_minutes","/edrData/event_version","/edrData/host_metadata_hostname","/edrData/missing_action_remote_process_instance_id","/facility","/generatedTime","/recordType","/recsize","/trapsId","/uuid","/xdr_unique_id","/meta_internal_id","/external_id","/is_visible","/is_secdo_event","/severity","/alert_source","/internal_id","/matching_status","/local_insert_ts","/source_insert_ts","/alert_name","/alert_category","/alert_description","/bioc_indicator","/matching_service_rule_id","/external_url","/xdr_sub_type","/bioc_category_enum_key","/alert_action_status","/agent_data_collection_status","/attempt_counter","/case_id","/global_content_version_id","/global_rule_id","/is_whitelisted"

Field prefixes for BIOC and IOC issue logs

  -----------------------------------------------------------------------
  Field Name                          Description
  ----------------------------------- -----------------------------------
  /edrData/action_file\*              Fields that begin with this prefix
                                      describe attributes of a file for
                                      which Traps reported activity.

  edrData/action_module\*             Fields that begin with this prefix
                                      describe attributes of a module for
                                      which Traps reported module loading
                                      activity.

  edrData/action_module_process\*     Fields that begin with this prefix
                                      describe attributes and activity
                                      related to processes reported by
                                      Traps that load modules such as
                                      DLLs on the endpoint.

  edrData/action_process_image\*      Fields that begin with this prefix
                                      describe attributes of a process
                                      image for which Traps reported
                                      activity.

  edrData/action_registry\*           Fields that begin with this prefix
                                      describe registry activity and
                                      attributes such as key name, data,
                                      and previous value for which Traps
                                      reported activity.

  edrData/action_network              Fields that begin with this prefix
                                      describe network attributes for
                                      which Traps reported activity.

  edrData/action_remote_process\*     Fields that begin with this prefix
                                      describe attributes of remote
                                      processes for which Traps reported
                                      activity.

  edrData/actor\*                     Fields that begin with this prefix
                                      describe attributes about the
                                      acting user that initiated the
                                      activity on the endpoint.

  edrData/agent\*                     Fields that begin with this prefix
                                      describe attributes about the Traps
                                      agent deployed on the endpoint.

  edrData/causality_actor\*           Fields that begin with this prefix
                                      describe attributes about the
                                      causality group owner.
  -----------------------------------------------------------------------

Additional fields for BIOC and IOC issue logs

+-----------------------------------+-------------------------------------------------------+
| Field Name                        | Description                                           |
+===================================+=======================================================+
| /severity                         | Severity assigned to the issue:                       |
|                                   |                                                       |
|                                   | - SEV_010_INFO                                        |
|                                   |                                                       |
|                                   | - SEV_020_LOW                                         |
|                                   |                                                       |
|                                   | - SEV_030_MEDIUM                                      |
|                                   |                                                       |
|                                   | - SEV_040_HIGH                                        |
|                                   |                                                       |
|                                   | - SEV_090_UNKNOWN                                     |
+-----------------------------------+-------------------------------------------------------+
| /alert_source                     | Source of the issue: BIOC or IOC                      |
+-----------------------------------+-------------------------------------------------------+
| /local_insert_ts                  | Date and time when Cortex XSIAM -- Investigation and  |
|                                   | Response ingested the app.                            |
+-----------------------------------+-------------------------------------------------------+
| /source_insert_ts                 | Date and time the issue was reported by the issue     |
|                                   | source.                                               |
+-----------------------------------+-------------------------------------------------------+
| /alert_name                       | If the issue was generated by Cortex XSIAM --         |
|                                   | Investigation and Response, the issue name will be    |
|                                   | the specific Cortex XSIAM rule that created the issue |
|                                   | (BIOC or IOC rule name). If from an external system,  |
|                                   | it will carry the name assigned to it by Cortex XSIAM |
|                                   | .                                                     |
+-----------------------------------+-------------------------------------------------------+
| /alert_category                   | Issue category based on the issue source.             |
|                                   |                                                       |
|                                   | - BIOC issue categories:                              |
|                                   |                                                       |
|                                   |   - OTHER                                             |
|                                   |                                                       |
|                                   |   - PERSISTENCE                                       |
|                                   |                                                       |
|                                   |   - EVASION                                           |
|                                   |                                                       |
|                                   |   - TAMPERING                                         |
|                                   |                                                       |
|                                   |   - FILE_TYPE_OBFUSCATION                             |
|                                   |                                                       |
|                                   |   - PRIVILEGE_ESCALATION                              |
|                                   |                                                       |
|                                   |   - CREDENTIAL_ACCESS                                 |
|                                   |                                                       |
|                                   |   - LATERAL_MOVEMENT                                  |
|                                   |                                                       |
|                                   |   - EXECUTION                                         |
|                                   |                                                       |
|                                   |   - COLLECTION                                        |
|                                   |                                                       |
|                                   |   - EXFILTRATION                                      |
|                                   |                                                       |
|                                   |   - INFILTRATION                                      |
|                                   |                                                       |
|                                   |   - DROPPER                                           |
|                                   |                                                       |
|                                   |   - FILE_PRIVILEGE_MANIPULATION                       |
|                                   |                                                       |
|                                   |   - RECONNAISSANCE                                    |
|                                   |                                                       |
|                                   | - IOC issue categories:                               |
|                                   |                                                       |
|                                   |   - HASH                                              |
|                                   |                                                       |
|                                   |   - IP                                                |
|                                   |                                                       |
|                                   |   - PATH                                              |
|                                   |                                                       |
|                                   |   - DOMAIN_NAME                                       |
|                                   |                                                       |
|                                   |   - FILENAME                                          |
|                                   |                                                       |
|                                   |   - MIXED                                             |
+-----------------------------------+-------------------------------------------------------+
| /alert_description                | Text summary of the event including the issue source, |
|                                   | issue name, severity, and file path. For alerts       |
|                                   | generated by BIOC and IOC rules, Cortex XSIAM         |
|                                   | displays detailed information about the rule.         |
+-----------------------------------+-------------------------------------------------------+
| /bioc_indicator                   | A JSON representation of the rule characteristics.    |
|                                   | For example:                                          |
|                                   |                                                       |
|                                   |     [{""pretty_name"":""File"",""data_type"":null,    |
|                                   |     ""render_type"":""entity"",""entity_map"":null},  |
|                                   |     {""pretty_name"":""action type"",                 |
|                                   |     ""data_type"":null,""render_type"":""attribute"", |
|                                   |     ""entity_map"":null},{""pretty_name"":""="",      |
|                                   |     ""data_type"":null,""render_type"":""operator"",  |
|                                   |     ""entity_map"":null},{""pretty_name"":""all"",    |
|                                   |     ""data_type"":null,""render_type"":""value"",     |
|                                   |     ""entity_map"":null},{""pretty_name"":""AND"",    |
|                                   |     ""data_type"":null,""render_type"":""connector"", |
|                                   |     ""entity_map"":null},{""pretty_name"":""name"",   |
|                                   |     ""data_type"":""TEXT"",                           |
|                                   |     ""render_type"":""attribute"",                    |
|                                   |     ""entity_map"":""attributes""},                   |
|                                   |     {""pretty_name"":""="",""data_type"":null,        |
|                                   |     ""render_type"":""operator"",                     |
|                                   |     ""entity_map"":""attributes""},                   |
|                                   |     {""pretty_name"":""*.pdf"",""data_type"":null,    |
|                                   |     ""render_type"":""value"",                        |
|                                   |     ""entity_map"":""attributes""}]"                  |
+-----------------------------------+-------------------------------------------------------+
| /bioc_category_enum_key           | Issue category based on the issue source. An example  |
|                                   | of a BIOC issue category is Evasion. An example of a  |
|                                   | Traps issue category is Exploit Modules.              |
+-----------------------------------+-------------------------------------------------------+
| /alert_action_status              | Action taken by the issue sensor with action status   |
|                                   | displayed in parenthesis:                             |
|                                   |                                                       |
|                                   | - Detected                                            |
|                                   |                                                       |
|                                   | - Detected (Download)                                 |
|                                   |                                                       |
|                                   | - Detected (Post Detected)                            |
|                                   |                                                       |
|                                   | - Detected (Prompt Allow)                             |
|                                   |                                                       |
|                                   | - Detected (Reported)                                 |
|                                   |                                                       |
|                                   | - Detected (Scanned)                                  |
|                                   |                                                       |
|                                   | - Prevented (Blocked)                                 |
|                                   |                                                       |
|                                   | - Prevented (Prompt Block)                            |
+-----------------------------------+-------------------------------------------------------+
| /case_id                          | Unique identifier for the incident.                   |
+-----------------------------------+-------------------------------------------------------+
| /global_content_version_id        | Unique identifier for the content version in which a  |
|                                   | Palo Alto Networks global BIOC rule was released.     |
+-----------------------------------+-------------------------------------------------------+
| /global_rule_id                   | Unique identifier for an issue generated by a Palo    |
|                                   | Alto Networks global BIOC rule.                       |
+-----------------------------------+-------------------------------------------------------+
| /is_whitelisted                   | Boolean indicating whether the issue is excluded or   |
|                                   | not.                                                  |
+-----------------------------------+-------------------------------------------------------+

###### Analytics log format

Cortex XSIAM Analytics logs issues as analytics issue logs. If you
configure Cortex XSIAM to forward logs in the legacy format, each log
record has the following format:

- **Syslog format:**

<!-- -->

- sub_type,time_generated,id,version_info/document_version,version_info/magnifier_version,version_info/detection_version,alert/url,alert/category,alert/type,alert/name,alert/description/html,alert/description/text,alert/severity,alert/state,alert/is_whitelisted,alert/ports,alert/internal_destinations/single_destinations,alert/internal_destinations/ip_ranges,alert/external_destinations,alert/app_id,alert/schedule/activity_first_seen_at,alert/schedule/activity_last_seen_at,alert/schedule/first_detected_at,alert/schedule/last_detected_at,user/user_name,user/url,user/display_name,user/org_unit,device/id,device/url,device/mac,device/hostname,device/ip,device/ip_ranges,device/owner,device/org_unit,files

<!-- -->

- **Email account:** Each field is labeled, one line per field.

<!-- -->

- sub_type: Update
      time_generated: 1547717480
      id: 4
      version_info/document_version: 1
      version_info/magnifier_version: 1.8
      version_info/detection_version: 2019.2.0rc1
      alert/url: https:\/\/ddc1...
      alert/category: Recon
      alert/type: Port Scan
      alert/name: Port Scan 
      alert/description/html: \t<ul>\n\t\t<li>The device....
      alert/description/text: The device ...
      ...
      device/id: 2-85e40edd-b2d1-1f25-2c1e-a3dd576c8a7e
      device/url: https:\/\/ddc1 ...
      device/mac: 00-50-56-a5-db-b2
      device/hostname: DC1ENV3APC42
      device/ip: 10.201.102.17
      device/ip_ranges: "[{""max_ip"":""..."",""name"":""..."",""min_ip"":""..."",""asset"":""""}]"
      device/owner: 
      device/org_unit: 
      files: []

Fields for analytics issue logs

+-------------------------------------------------+------------------------------------+
| Field Name                                      | Definition                         |
+=================================================+====================================+
| sub_type                                        | Issue log subtype. Values are:     |
|                                                 |                                    |
|                                                 | - `New:` First log record for the  |
|                                                 |   issue with this record `id`.     |
|                                                 |                                    |
|                                                 | - `Update:` Log record identifies  |
|                                                 |   an update to a previously logged |
|                                                 |   issue.                           |
|                                                 |                                    |
|                                                 | - `StateOnlyUpdate:`Issue state is |
|                                                 |   updated. For internal use only.  |
+-------------------------------------------------+------------------------------------+
| time_generated                                  | Time the log record was sent to    |
|                                                 | the Cortex XSIAM tenant. Value is  |
|                                                 | a Unix Epoch timestamp.            |
+-------------------------------------------------+------------------------------------+
| id                                              | Unique identifier for the issue.   |
|                                                 | Any given issue can generate       |
|                                                 | multiple log records---one when    |
|                                                 | the issue is initially generated,  |
|                                                 | and then additional records every  |
|                                                 | time the issue status changes.     |
|                                                 | This ID remains constant for all   |
|                                                 | such issue records.                |
|                                                 |                                    |
|                                                 | You can obtain the current status  |
|                                                 | of the issue by looking for log    |
|                                                 | records with this id and the most  |
|                                                 | recent                             |
|                                                 | `alert/schedule/last_detected_at`  |
|                                                 | timestamp.                         |
+-------------------------------------------------+------------------------------------+
| version_info/document_version                   | Identifies the log schema version  |
|                                                 | number used for this log record.   |
+-------------------------------------------------+------------------------------------+
| version_info/magnifier_version                  | The version number of the Cortex   |
|                                                 | XSIAM -- Analytics instance that   |
|                                                 | wrote this log record.             |
+-------------------------------------------------+------------------------------------+
| version_info/detection_version                  | Identifies the version of the      |
|                                                 | Cortex XSIAM -- Analytics          |
|                                                 | detection software used to         |
|                                                 | generate the issue.                |
+-------------------------------------------------+------------------------------------+
| alert/url                                       | Provides the full URL to the issue |
|                                                 | page in the Cortex XSIAM --        |
|                                                 | Analytics user interface.          |
+-------------------------------------------------+------------------------------------+
| alert/category                                  | Identifies the issue category,     |
|                                                 | which is a reflection of the       |
|                                                 | anomalous network activity         |
|                                                 | location in the attack life cycle. |
|                                                 | Possible categories are:           |
|                                                 |                                    |
|                                                 | - `C&C:` The network activity is   |
|                                                 |   possibly the result of malware   |
|                                                 |   attempting to connect to its     |
|                                                 |   Command & Control server.        |
|                                                 |                                    |
|                                                 | - `Exfiltration:` A large amount   |
|                                                 |   of data is being transferred to  |
|                                                 |   an endpoint that is external to  |
|                                                 |   the network.                     |
|                                                 |                                    |
|                                                 | - `Lateral:` The network activity  |
|                                                 |   is indicative of an attacker who |
|                                                 |   is attempting to move from one   |
|                                                 |   endpoint to another on the       |
|                                                 |   network.                         |
|                                                 |                                    |
|                                                 | - `Malware:` A file has been       |
|                                                 |   discovered on an endpoint that   |
|                                                 |   is probably malware or riskware. |
|                                                 |   Malware issues can also be       |
|                                                 |   generated based on network       |
|                                                 |   activity that is indicative of   |
|                                                 |   automated malicious traffic      |
|                                                 |   generation.                      |
|                                                 |                                    |
|                                                 | - `Recon:` The network activity is |
|                                                 |   indicative an attacker that is   |
|                                                 |   exploring the network for        |
|                                                 |   endpoints and other resources to |
|                                                 |   attack.                          |
+-------------------------------------------------+------------------------------------+
| alert/type                                      | Identifies the categorization to   |
|                                                 | which the issue belongs. For       |
|                                                 | example *Tunneling Process*,       |
|                                                 | *Sandbox Detection*, *Malware*,    |
|                                                 | and so forth.                      |
+-------------------------------------------------+------------------------------------+
| alert/name                                      | The issue name as it appears in    |
|                                                 | the Cortex XSIAM -- Analytics user |
|                                                 | interface.                         |
+-------------------------------------------------+------------------------------------+
| alert/description/html                          | The issue textual description in   |
|                                                 | HTML formatting.                   |
+-------------------------------------------------+------------------------------------+
| alert/description/text                          | The issue textual description in   |
|                                                 | plain text.                        |
+-------------------------------------------------+------------------------------------+
| alert/severity                                  | Identifies the issue severity.     |
|                                                 | These severities indicate the      |
|                                                 | likelihood that the anomalous      |
|                                                 | network activity is a real attack. |
|                                                 |                                    |
|                                                 | - `High:` The issue is confirmed   |
|                                                 |   to be a network attack.          |
|                                                 |                                    |
|                                                 | - `Medium:` The issue is           |
|                                                 |   suspicious enough to require     |
|                                                 |   additional investigation.        |
|                                                 |                                    |
|                                                 | - `Low:` The issue is unverified.  |
|                                                 |   Whether the issue is indicative  |
|                                                 |   of a network attack is unknown.  |
+-------------------------------------------------+------------------------------------+
| alert/state                                     | Identifies the issue state.        |
|                                                 |                                    |
|                                                 | - `Open:` The issue is currently   |
|                                                 |   active and should be undergoing  |
|                                                 |   triage or investigation by the   |
|                                                 |   network security analysts.       |
|                                                 |                                    |
|                                                 | - `Reopened:` The issue was        |
|                                                 |   previously resolved or           |
|                                                 |   dismissed, but new network       |
|                                                 |   activity has caused Cortex XSIAM |
|                                                 |   -- Analytics to reopen the       |
|                                                 |   issue.                           |
|                                                 |                                    |
|                                                 | - `Archived:` No action was taken  |
|                                                 |   on the issue in the Cortex XSIAM |
|                                                 |   -- Analytics user interface, and |
|                                                 |   no further network activity has  |
|                                                 |   occurred that caused it to       |
|                                                 |   remain active.                   |
|                                                 |                                    |
|                                                 | - `Resolved:` Network personnel    |
|                                                 |   have taken enough action to end  |
|                                                 |   the attack.                      |
|                                                 |                                    |
|                                                 | - `Dismissed:` The anomaly has     |
|                                                 |   been examined and deemed to be   |
|                                                 |   normal, sanctioned, network      |
|                                                 |   activity.                        |
+-------------------------------------------------+------------------------------------+
| alert/is_whitelisted                            | Indicates whether the issue is     |
|                                                 | whitelisted. Whitelisting          |
|                                                 | indicates that anomalous-appearing |
|                                                 | network activity is legitimate. If |
|                                                 | an issue is whitelisted, then it   |
|                                                 | is not visible in the Cortex XSIAM |
|                                                 | -- Analytics user interface.       |
|                                                 | Issues can be dismissed or         |
|                                                 | archived and still have a          |
|                                                 | whitelist rule.                    |
+-------------------------------------------------+------------------------------------+
| alert/ports                                     | List of ports accessed by the      |
|                                                 | network entity during its          |
|                                                 | anomalous behavior.                |
+-------------------------------------------------+------------------------------------+
| alert/internal_destinations/single_destinations | Network destinations that the      |
|                                                 | entity reached, or tried to reach, |
|                                                 | during the course of the network   |
|                                                 | activity that caused Cortex XSIAM  |
|                                                 | -- Analytics to generate the       |
|                                                 | issue. This field contains a       |
|                                                 | sequence of JSON objects, each of  |
|                                                 | which contains the following       |
|                                                 | fields:                            |
|                                                 |                                    |
|                                                 | - `ip:` The destination IP         |
|                                                 |   address.                         |
|                                                 |                                    |
|                                                 | - `name:` The destination name     |
|                                                 |   (for example, a host name).      |
+-------------------------------------------------+------------------------------------+
| alert/internal_destinations/ip_ranges           | IP address range subnets that the  |
|                                                 | entity reached, or tried to reach, |
|                                                 | during the course of the network   |
|                                                 | activity that caused Cortex XSIAM  |
|                                                 | -- Analytics to generate the       |
|                                                 | issue. This field contains a       |
|                                                 | sequence of JSON objects, each of  |
|                                                 | which contains the following       |
|                                                 | fields:                            |
|                                                 |                                    |
|                                                 | - `max_ip:` Last IP address in the |
|                                                 |   subnet.                          |
|                                                 |                                    |
|                                                 | - `min_ip:` First IP address in    |
|                                                 |   the subnet.                      |
|                                                 |                                    |
|                                                 | - `name:` Subnet name.             |
+-------------------------------------------------+------------------------------------+
| alert/external_destinations                     | Provides a list of destinations    |
|                                                 | external to the monitored network  |
|                                                 | that the entity tried to reach, or |
|                                                 | actually reached, during the       |
|                                                 | activity that generated this       |
|                                                 | issue. This list can contain IP    |
|                                                 | addresses or fully qualified       |
|                                                 | domain names.                      |
+-------------------------------------------------+------------------------------------+
| alert/app_id                                    | The App-ID associated with this    |
|                                                 | issue.                             |
+-------------------------------------------------+------------------------------------+
| alert/schedule/activity_first_seen_at           | Time when Cortex XSIAM --          |
|                                                 | Analytics first detected the       |
|                                                 | network activity that caused it to |
|                                                 | generate the issue. Be aware that  |
|                                                 | there is frequently a delay        |
|                                                 | between this timestamp, and the    |
|                                                 | time when Cortex XSIAM --          |
|                                                 | Analytics generates an issue (see  |
|                                                 | the                                |
|                                                 | `alert/schedule/first_detected_at` |
|                                                 | field).                            |
+-------------------------------------------------+------------------------------------+
| alert/schedule/activity_last_seen_at            | Time when Cortex XSIAM --          |
|                                                 | Analytics last detected the        |
|                                                 | network activity that caused it to |
|                                                 | generate the issue.                |
+-------------------------------------------------+------------------------------------+
| alert/schedule/first_detected_at                | Time when Cortex XSIAM --          |
|                                                 | Analytics first alerted on the     |
|                                                 | network activity.                  |
+-------------------------------------------------+------------------------------------+
| alert/schedule/last_detected_at                 | Time when Cortex XSIAM --          |
|                                                 | Analytics last alerted on the      |
|                                                 | network activity.                  |
+-------------------------------------------------+------------------------------------+
| user/user_name                                  | The name of the user associated    |
|                                                 | with this issue. This name is      |
|                                                 | obtained from Active Directory.    |
+-------------------------------------------------+------------------------------------+
| user/url                                        | Provides the full URL to the user  |
|                                                 | page in the Cortex XSIAM --        |
|                                                 | Analytics user interface for the   |
|                                                 | user who is associated with the    |
|                                                 | issue.                             |
+-------------------------------------------------+------------------------------------+
| user/display_name                               | The user name as retrieved from    |
|                                                 | Active Directory. This is the user |
|                                                 | name displayed within the Cortex   |
|                                                 | XSIAM -- Analytics user interface  |
|                                                 | for the user who is associated     |
|                                                 | with this issue.                   |
+-------------------------------------------------+------------------------------------+
| user/org_unit                                   | The organizational unit of the     |
|                                                 | user associated with this issue,   |
|                                                 | as identified using Active         |
|                                                 | Directory.                         |
+-------------------------------------------------+------------------------------------+
| device/id                                       | A unique ID assigned by Cortex     |
|                                                 | XSIAM -- Analytics to the device.  |
|                                                 | All issues generated due to        |
|                                                 | activity occurring on this         |
|                                                 | endpoint will share this ID.       |
+-------------------------------------------------+------------------------------------+
| device/url                                      | Provides the full URL to the       |
|                                                 | device page in the Cortex XSIAM -- |
|                                                 | Analytics user interface.          |
+-------------------------------------------------+------------------------------------+
| device/mac                                      | The MAC address of the network     |
|                                                 | card in use on the device.         |
+-------------------------------------------------+------------------------------------+
| device/hostname                                 | The device host name.              |
+-------------------------------------------------+------------------------------------+
| device/ip                                       | The device IP address.             |
+-------------------------------------------------+------------------------------------+
| device/ip_ranges                                | Identifies the subnet or subnets   |
|                                                 | that the device is on. This        |
|                                                 | sequence can contain multiple      |
|                                                 | inclusive subnets. Each element in |
|                                                 | this sequence is a JSON object     |
|                                                 | with the following fields:         |
|                                                 |                                    |
|                                                 | - `asset:` The asset name assigned |
|                                                 |   to the device from within the    |
|                                                 |   Cortex XSIAM -- Analytics user   |
|                                                 |   interface.                       |
|                                                 |                                    |
|                                                 | - `max_ip:` Last IP address in the |
|                                                 |   subnet.                          |
|                                                 |                                    |
|                                                 | - `min_ip:` First IP address in    |
|                                                 |   the subnet.                      |
|                                                 |                                    |
|                                                 | - `name:` Subnet name.             |
+-------------------------------------------------+------------------------------------+
| device/owner                                    | The user name of the person who    |
|                                                 | owns the device.                   |
+-------------------------------------------------+------------------------------------+
| device/org_unit                                 | The organizational unit that owns  |
|                                                 | the device, as identified by       |
|                                                 | Active Directory.                  |
+-------------------------------------------------+------------------------------------+
| files                                           | Identifies the files associated    |
|                                                 | with the issue. Each element in    |
|                                                 | this sequence is a JSON object     |
|                                                 | with the following fields:         |
|                                                 |                                    |
|                                                 | - `full_path:` The file full path  |
|                                                 |   (including the file name).       |
|                                                 |                                    |
|                                                 | - `md5:` The file MD5 hash.        |
+-------------------------------------------------+------------------------------------+

###### Log formats

The following lists the fields for each log type that Cortex XSIAM can
forward to an external server or email destination.

Keep in mind the following:

- When log forwarding to a syslog receiver, Cortex XSIAM sends logs in
  the IETF syslog message format defined in [RFC
  5425](https://tools.ietf.org/html/rfc5425). To facilitate parsing, the
  delimiter is a comma and each field is a comma-separated value (CSV)
  string.

<!-- -->

- > **Note**

  > The FUTURE_USE tag applies to fields that Cortex XSIAM does not
  > currently implement.

<!-- -->

- When log forwarding to an email account, Cortex XSIAM sends an email
  with each field on a separate line in the email body.

####### Threat logs

The syslog format is as follows:

    recordType, class, FUTURE_USE, eventType, generatedTime, serverTime, agentTime, tzOffset, FUTURE_USE, facility, customerId, trapsId, serverHost, serverComponentVersion, regionId, isEndpoint, agentId, osType, isVdi, osVersion, is64, agentIp, deviceName, deviceDomain, severity, trapsSeverity, agentVersion, contentVersion, protectionStatus, preventionKey, moduleId, profile, moduleStatusId, verdict, preventionMode, terminate, terminateTarget, quarantine, block, postDetected, eventParameters(Array), sourceProcessIdx(Array), targetProcessIdx(Array), fileIdx(Array), processes(Array), files(Array), users(Array), urls(Array), description(Array)

Fields for threat logs

+-----------------------------------+--------------------------------------------------+
| Field Name                        | Description                                      |
+===================================+==================================================+
| recordType                        | Record type associated with the event and that   |
|                                   | you can use when managing logging quotas. In     |
|                                   | this case, the record type is threat which       |
|                                   | includes logs related to security events that    |
|                                   | occur on the endpoints.                          |
+-----------------------------------+--------------------------------------------------+
| class                             | Class of Cortex XDR agent log: config, policy,   |
|                                   | system, or agent_log.                            |
+-----------------------------------+--------------------------------------------------+
| eventType                         | Subtype of event: AgentActionReport,             |
|                                   | AgentDeviceControlViolation,                     |
|                                   | AgentGenericMessage, AgentSamReport,             |
|                                   | AgentScanReport, AgentSecurityEvent,             |
|                                   | AgentStatistics, AgentTimelineEvent,             |
|                                   | ServerLogPerAgent, ServerLogPerTenant, or        |
|                                   | ServerLogSystem.                                 |
+-----------------------------------+--------------------------------------------------+
| generatedTime                     | Coordinated Universal Time (UTC) equivalent of   |
|                                   | the time at which an event was logged. For agent |
|                                   | events, this represents the time on the          |
|                                   | endpoint. For policy, configuration, and system  |
|                                   | events, this represents the time on Cortex XSIAM |
|                                   | in ISO-8601 string representation (for example,  |
|                                   | 2017-01-24T09:08:59Z).                           |
+-----------------------------------+--------------------------------------------------+
| serverTime                        | Coordinated Universal Time (UTC) equivalent of   |
|                                   | the time at which the server generated the log.  |
|                                   | If the log was generated on an endpoint, this    |
|                                   | field identifies the time the server received    |
|                                   | the log in ISO-8601 string representation (for   |
|                                   | example, 2017-01-24T09:08:59Z).                  |
+-----------------------------------+--------------------------------------------------+
| agentTime                         | Coordinated Universal Time (UTC) equivalent of   |
|                                   | the time at which an agent logged an event in    |
|                                   | ISO-8601 string representation.                  |
+-----------------------------------+--------------------------------------------------+
| tzOffset                          | Effective endpoint time zone offset from UTC, in |
|                                   | minutes.                                         |
+-----------------------------------+--------------------------------------------------+
| facility                          | The Cortex XSIAM system component that initiated |
|                                   | the event, for example: TrapsAgent,              |
|                                   | TrapsServiceCore, TrapsServiceManagement, and    |
|                                   | TrapsServiceBackend.                             |
+-----------------------------------+--------------------------------------------------+
| customerId                        | The ID that uniquely identifies the Cortex XSIAM |
|                                   | tenant instance which received this log record.  |
+-----------------------------------+--------------------------------------------------+
| trapsId                           | Tenant external ID.                              |
+-----------------------------------+--------------------------------------------------+
| serverHost                        | Hostname of Cortex XSIAM.                        |
+-----------------------------------+--------------------------------------------------+
| serverComponentVersion            | Software version of Cortex XSIAM.                |
+-----------------------------------+--------------------------------------------------+
| regionId                          | ID of Cortex XSIAM region:                       |
|                                   |                                                  |
|                                   | - **10:** Americas (N. Virginia)                 |
|                                   |                                                  |
|                                   | - **70:** EMEA (Frankfurt)                       |
+-----------------------------------+--------------------------------------------------+
| isEndpoint                        | Indicates whether the event occurred on an       |
|                                   | endpoint.                                        |
|                                   |                                                  |
|                                   | - **0:** No, host is not an endpoint.            |
|                                   |                                                  |
|                                   | - **1:** Yes, host is an endpoint.               |
+-----------------------------------+--------------------------------------------------+
| agentId                           | Unique identifier for the Cortex XDR agent.      |
+-----------------------------------+--------------------------------------------------+
| osType                            | Operating system of the endpoint:                |
|                                   |                                                  |
|                                   | - **1:** Windows                                 |
|                                   |                                                  |
|                                   | - **2:** OS X/macOS                              |
|                                   |                                                  |
|                                   | - **3:** Android                                 |
|                                   |                                                  |
|                                   | - **4:** Linux                                   |
+-----------------------------------+--------------------------------------------------+
| isVdi                             | Indicates whether the endpoint is a virtual      |
|                                   | desktop infrastructure (VDI):                    |
|                                   |                                                  |
|                                   | - **0:** The endpoint is not a VDI               |
|                                   |                                                  |
|                                   | - **1:** The endpoint is a VDI                   |
+-----------------------------------+--------------------------------------------------+
| osVersion                         | Full version number of the operating system      |
|                                   | running on the endpoint. For example,            |
|                                   | 6.1.7601.19135.                                  |
+-----------------------------------+--------------------------------------------------+
| is64                              | Indicates whether the endpoint is running a      |
|                                   | 64-bit version of Windows:                       |
|                                   |                                                  |
|                                   | - **0:** The endpoint is not running x64         |
|                                   |   architecture                                   |
|                                   |                                                  |
|                                   | - **1:** The endpoint is running x64             |
|                                   |   architecture                                   |
+-----------------------------------+--------------------------------------------------+
| agentIp                           | IP address of the endpoint.                      |
+-----------------------------------+--------------------------------------------------+
| deviceName                        | Hostname of the endpoint on which the event was  |
|                                   | logged.                                          |
+-----------------------------------+--------------------------------------------------+
| deviceDomain                      | Domain to which the endpoint belongs.            |
+-----------------------------------+--------------------------------------------------+
| severity                          | Syslog severity level associated with the event. |
|                                   |                                                  |
|                                   | - **2:** Critical. Used for events that require  |
|                                   |   immediate attention.                           |
|                                   |                                                  |
|                                   | - **3:** Error. Used for events that require     |
|                                   |   special handling.                              |
|                                   |                                                  |
|                                   | - **4:** Warning. Used for events that sometimes |
|                                   |   require special handling.                      |
|                                   |                                                  |
|                                   | - **5:** Notice. Used for normal but significant |
|                                   |   events that can require attention.             |
|                                   |                                                  |
|                                   | - **6:** Informational. Informational events     |
|                                   |   that do not require attention.                 |
|                                   |                                                  |
|                                   | Each event also has an associated Cortex XSIAM   |
|                                   | severity. See the `messageData.trapsSeverity`    |
|                                   | field for details.                               |
+-----------------------------------+--------------------------------------------------+
| trapsSeverity                     | Severity level associated with the event defined |
|                                   | for Cortex XSIAM. Each of these severities       |
|                                   | corresponds to a syslog severity level:          |
|                                   |                                                  |
|                                   | - **0:** Informational. Informational messages   |
|                                   |   that do not require attention. Identical to    |
|                                   |   the syslog 6 (Informational) severity level.   |
|                                   |                                                  |
|                                   | - **1:** Low. Used for normal but significant    |
|                                   |   events that can require attention. Corresponds |
|                                   |   to the syslog 5 (Notice) severity level.       |
|                                   |                                                  |
|                                   | - **2:** Medium. Used for events that sometimes  |
|                                   |   require special handling. Corresponds to the   |
|                                   |   syslog 4 (Warning) severity level.             |
|                                   |                                                  |
|                                   | - **3:** High. Used for events that require      |
|                                   |   special handling. Corresponds to the syslog 3  |
|                                   |   (Error) severity level.                        |
|                                   |                                                  |
|                                   | - **4:** Critical. Used for events that require  |
|                                   |   immediate attention. Corresponds to the syslog |
|                                   |   2 (Critical) severity level.                   |
|                                   |                                                  |
|                                   | See also the `severity` log field.               |
+-----------------------------------+--------------------------------------------------+
| agentVersion                      | Version of the Cortex XDR agent.                 |
+-----------------------------------+--------------------------------------------------+
| contentVersion                    | Content version in the local security policy.    |
+-----------------------------------+--------------------------------------------------+
| protectionStatus                  | Cortex XDR agent protection status:              |
|                                   |                                                  |
|                                   | - **0:** Protected                               |
|                                   |                                                  |
|                                   | - **1:** OsVersionIncompatible                   |
|                                   |                                                  |
|                                   | - **2:** AgentIncompatible                       |
+-----------------------------------+--------------------------------------------------+
| preventionKey                     | Unique identifier for security events.           |
+-----------------------------------+--------------------------------------------------+
| moduleId                          | Security module name.                            |
+-----------------------------------+--------------------------------------------------+
| profile                           | Name of the security profile that triggered the  |
|                                   | event.                                           |
+-----------------------------------+--------------------------------------------------+
| moduleStatusId                    | Identifies the specific component of Cortex      |
|                                   | XSIAM modules.                                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_ABNORMAL_PROCESS_TERMINATION`        |
|                                   |                                                  |
|                                   | - `CYSTATUS_ALIGNED_HEAP_SPRAY_DETECTED`         |
|                                   |                                                  |
|                                   | - `CYSTATUS_CHILD_PROCESS_BLOCKED`               |
|                                   |                                                  |
|                                   | - `CYSTATUS_CORE_LIBRARY_LOADED`                 |
|                                   |                                                  |
|                                   | - `CYSTATUS_CORE_LIBRARY_UNLOADING`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_CPLPROT_BLACKLIST`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_CPLPROT_REMOTE_DRIVE`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_CPLPROT_REMOVABLE_DRIVE`             |
|                                   |                                                  |
|                                   | - `CYSTATUS_CYINJCT_DISPATCH`                    |
|                                   |                                                  |
|                                   | - `CYSTATUS_CYINJCT_MAPPING`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_CYVERA_PREVENTION`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_DANGEROUS_SYSTEM_SERVICE_CALLED`     |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEMO_EVENT`                          |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEP_SEH_INF_VIOLATION`               |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEP_SEH_VIOLATION`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEP_VIOLATION`                       |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEP_VIOLATION_UNALLOCATED`           |
|                                   |                                                  |
|                                   | - `CYSTATUS_DEVICE_BLOCKED`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_DLLPROT_BLACKLIST`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_DLLPROT_CURRENT_WORKING_DIRECTORY`   |
|                                   |                                                  |
|                                   | - `CYSTATUS_DLLPROT_REMOTE_DRIVE`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_DLLPROT_REMVABLE_DRIVE`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_DOTNET_CRITICAL`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_DSE`                                 |
|                                   |                                                  |
|                                   | - `CYSTATUS_EPM_INIT_FAILED`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_FAILED_CHECK_MEDIA`                  |
|                                   |                                                  |
|                                   | - `CYSTATUS_FILE_DELETION_BOOT_DONE`             |
|                                   |                                                  |
|                                   | - `CYSTATUS_FILE_DELETION_FAILED`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_FILE_DELETION_SUCCEEDED`             |
|                                   |                                                  |
|                                   | - `CYSTATUS_FINGERPRINTING_ATTEMPT`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_FONT_PROT_DUQU`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_FORBIDDEN_MEDIA`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_FORBIDDEN_OPTICAL_MEDIA`             |
|                                   |                                                  |
|                                   | - `CYSTATUS_FORBIDDEN_REMOTE_MEDIA`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_FORBIDDEN_REMOVABLE_MEDIA`           |
|                                   |                                                  |
|                                   | - `CYSTATUS_GS_COOKIE_CORRUPTED_COOKIE`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_GUARD_PAGE_VIOLATION`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_HASH_CONTROL`                        |
|                                   |                                                  |
|                                   | - `CYSTATUS_HEAP_CORRUPTION`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_HOOKING_ENTRY_POINT_FAILED`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_HOTPATCH_HIJACKING`                  |
|                                   |                                                  |
|                                   | - `CYSTATUS_ILLEGAL_EXECUTABLE`                  |
|                                   |                                                  |
|                                   | - `CYSTATUS_ILLEGAL_UNSIGNED_EXECUTABLE`         |
|                                   |                                                  |
|                                   | - `CYSTATUS_INJ_APPCONTAINER_FAILURE`            |
|                                   |                                                  |
|                                   | - `CYSTATUS_INJ_CTX_FAILURE`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_JAVA_FILE`                           |
|                                   |                                                  |
|                                   | - `CYSTATUS_JAVA_PROC`                           |
|                                   |                                                  |
|                                   | - `CYSTATUS_JAVA_REG`                            |
|                                   |                                                  |
|                                   | - `CYSTATUS_JIT_EXCEPTION`                       |
|                                   |                                                  |
|                                   | - `CYSTATUS_LINUX_BRUTEFORCE_PREVENTED`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_LINUX_ROOT_ESCALATION_PREVENTED`     |
|                                   |                                                  |
|                                   | - `CYSTATUS_LINUX_SHELLCODE_PREVENTED`           |
|                                   |                                                  |
|                                   | - `CYSTATUS_LINUX_SOCKET_SHELL_PREVENTED`        |
|                                   |                                                  |
|                                   | - `CYSTATUS_LOCAL_ANALYSIS`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_DLPROT_CWD_HIJACK`             |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_DLPROT_DUPLICATE_PATH_CHECK`   |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_G02_BLOCK_ALL`                 |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_G02_SIGNER_NAME_MISMATCH`      |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_G02_SIGN_LEVEL_BELOW_MIN`      |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_G02_SIGN_LEVEL_BELOW_PARENT`   |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_MALICIOUS_DYLIB`               |
|                                   |                                                  |
|                                   | - `CYSTATUS_MACOS_ROOT_ESCALATION_PREVENTED`     |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_APK`                       |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_DLL`                       |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_EXE`                       |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_EXE_ASYNC`                 |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_MACRO`                     |
|                                   |                                                  |
|                                   | - `CYSTATUS_MALICIOUS_STRING_DETECTED`           |
|                                   |                                                  |
|                                   | - `CYSTATUS_MEMORY_USAGE_LIMIT_EXCEEDED`         |
|                                   |                                                  |
|                                   | - `CYSTATUS_NOP_SLED_DETECTED`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_NO_MEMORY`                           |
|                                   |                                                  |
|                                   | - `CYSTATUS_NO_REGISTER_CORRECTED`               |
|                                   |                                                  |
|                                   | - `CYSTATUS_PREALLOCATED_ADDR_ACCESSED`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_PROCESS_CREATION_VIOLATION`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_QUARANTINE_FAILED`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_QUARANTINE_SUCCEEDED`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_RANSOMWARE`                          |
|                                   |                                                  |
|                                   | - `CYSTATUS_RESTORE_FAILED`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_RESTORE_SUCCEEDED`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_ROP_MITIGATION`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_SEH_CRITICAL`                        |
|                                   |                                                  |
|                                   | - `CYSTATUS_SEH_INF_CRITICAL`                    |
|                                   |                                                  |
|                                   | - `CYSTATUS_SHELL_CODE_TRAP_CALLED`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_STACK_OVERFLOW`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_SUSPENDED_PROCESS_BLOCKED`           |
|                                   |                                                  |
|                                   | - `CYSTATUS_SUSPICIOUS_APC`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_SUSPICIOUS_LINK_FILE`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_SYSTEM_SCAN_FINISHED`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_SYSTEM_SCAN_STARTED`                 |
|                                   |                                                  |
|                                   | - `CYSTATUS_THREAD_INJECTION`                    |
|                                   |                                                  |
|                                   | - `CYSTATUS_TLA_MODEL_NOT_LOADED`                |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_FILE_OPERATION`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_PROCESS_CREATED`         |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_REGISTRY_OPERATION`      |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_THREAD_CREATED`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_THREAD_INJECTED`         |
|                                   |                                                  |
|                                   | - `CYSTATUS_TOKEN_THEFT_THREAD_STARTED`          |
|                                   |                                                  |
|                                   | - `CYSTATUS_UASLR_CRITICAL`                      |
|                                   |                                                  |
|                                   | - `CYSTATUS_UNALLOWED_CODE_SEGMENT`              |
|                                   |                                                  |
|                                   | - `CYSTATUS_UNAUTHORIZED_CALL_TO_SYSTEM_SERVICE` |
|                                   |                                                  |
|                                   | - `CYSTATUS_UNSIGNED_CHILD_PROCESS_BLOCKED`      |
|                                   |                                                  |
|                                   | - `CYSTATUS_WILDFIRE_GRAYWARE`                   |
|                                   |                                                  |
|                                   | - `CYSTATUS_WILDFIRE_MALWARE`                    |
|                                   |                                                  |
|                                   | - `CYSTATUS_WILDFIRE_UNKNOWN`                    |
+-----------------------------------+--------------------------------------------------+
| verdict                           | Verdict for the file:                            |
|                                   |                                                  |
|                                   | - **0:** Benign                                  |
|                                   |                                                  |
|                                   | - **1:** Malware                                 |
|                                   |                                                  |
|                                   | - **2:** Grayware                                |
|                                   |                                                  |
|                                   | - **4:** Phishing                                |
|                                   |                                                  |
|                                   | - **99:** Unknown                                |
+-----------------------------------+--------------------------------------------------+
| preventionMode                    | Action carried out by the Cortex XDR agent       |
|                                   | (block or notify). The prevention mode is        |
|                                   | specified in the rule configuration.             |
+-----------------------------------+--------------------------------------------------+
| terminate                         | Termination action taken on the file.            |
|                                   |                                                  |
|                                   | - **0:** Cortex XSIAM did not terminate the      |
|                                   |   file.                                          |
|                                   |                                                  |
|                                   | - **1:** Cortex XSIAM terminated the file.       |
+-----------------------------------+--------------------------------------------------+
| terminateTarget                   | Termination action taken on the target file      |
|                                   | (relevant for some child process execution       |
|                                   | events where we terminate the child process but  |
|                                   | not the parent process):                         |
|                                   |                                                  |
|                                   | - **0:** Target file was not terminated.         |
|                                   |                                                  |
|                                   | - **1:** Target file was terminated.             |
+-----------------------------------+--------------------------------------------------+
| quarantine                        | Quarantine action taken on the file:             |
|                                   |                                                  |
|                                   | - **0:** File was not quarantined.               |
|                                   |                                                  |
|                                   | - **1:** File was quarantined.                   |
+-----------------------------------+--------------------------------------------------+
| block                             | Block action taken on the file:                  |
|                                   |                                                  |
|                                   | - **0:** File was not blocked                    |
|                                   |                                                  |
|                                   | - **1:** File was blocked.                       |
+-----------------------------------+--------------------------------------------------+
| postDetected                      | Post detection status of the file:               |
|                                   |                                                  |
|                                   | - **0:** Initial prevention.                     |
|                                   |                                                  |
|                                   | - **1:** Detected after an initial execution.    |
+-----------------------------------+--------------------------------------------------+
| eventParameters(Array)            | Parameters associated with the type of event.    |
|                                   | For example, username, endpoint hostname, and    |
|                                   | filename.                                        |
+-----------------------------------+--------------------------------------------------+
| sourceProcessIdx(Array)           | The prevention source process index in the       |
|                                   | processes array.                                 |
+-----------------------------------+--------------------------------------------------+
| targetProcessIdx(Array)           | Target process index in the processes array. A   |
|                                   | missing or negative value means there is no      |
|                                   | target process.                                  |
+-----------------------------------+--------------------------------------------------+
| fileIdx(Array)                    | Index of target files for specific security      |
|                                   | events such as: Scanning, Malicious DLL,         |
|                                   | Malicious Macro events.                          |
+-----------------------------------+--------------------------------------------------+
| processes(Array)                  | All related details for the process file that    |
|                                   | triggered an event:                              |
|                                   |                                                  |
|                                   | - **1:** System process ID                       |
|                                   |                                                  |
|                                   | - **2:** Parent process ID                       |
|                                   |                                                  |
|                                   | - **3:** File object corresponding to the        |
|                                   |   process executable file                        |
|                                   |                                                  |
|                                   | - **4:** Command line arguments (if any)         |
|                                   |                                                  |
|                                   | - **5:** Description field of the VERSIONINFO    |
|                                   |   resource                                       |
|                                   |                                                  |
|                                   | - **6:** File version field of the VERSIONINFO   |
|                                   |   resource                                       |
+-----------------------------------+--------------------------------------------------+
| files(Array)                      | File object includes:                            |
|                                   |                                                  |
|                                   | - **1:** SHA256 hash value of the file           |
|                                   |                                                  |
|                                   | - **2:** SHA256 hash value of the macro          |
|                                   |                                                  |
|                                   | - **3:** Raw full filepath                       |
|                                   |                                                  |
|                                   | - **4:** A predefined drive type: local, network |
|                                   |   mapped drive, UNC path host, removable media,  |
|                                   |   etc.                                           |
|                                   |                                                  |
|                                   | - **5:** File name (with no extension), such as  |
|                                   |   AdapterTroubleshooter                          |
|                                   |                                                  |
|                                   | - **6:** File extension (for example, EXE or     |
|                                   |   DLL)                                           |
|                                   |                                                  |
|                                   | - **7:** File type defined by the XDR agent      |
|                                   |                                                  |
|                                   | - **8:** UTC file creation time                  |
|                                   |                                                  |
|                                   | - **9:** UTC file modification time              |
|                                   |                                                  |
|                                   | - **10:** UTC file access time                   |
|                                   |                                                  |
|                                   | - **11:** File attributes bitmask                |
|                                   |                                                  |
|                                   | - **12:** File size in bytes                     |
|                                   |                                                  |
|                                   | - **13:** Signer field of the code signing       |
|                                   |   certificate                                    |
+-----------------------------------+--------------------------------------------------+
| users(Array)                      | Details about the active user on the endpoint    |
|                                   | when the event occurred:                         |
|                                   |                                                  |
|                                   | - **1:** Username of the active user on the      |
|                                   |   endpoint.                                      |
|                                   |                                                  |
|                                   | - **2:** Domain to which the user account        |
|                                   |   belongs.                                       |
+-----------------------------------+--------------------------------------------------+
| urls(Array)                       | Additional details related to a URL:             |
|                                   |                                                  |
|                                   | - **1:** Raw URL                                 |
|                                   |                                                  |
|                                   | - **2:** URL schema; For example: HTTP, HTTPS,   |
|                                   |   FTP, LDAP                                      |
|                                   |                                                  |
|                                   | - **3:** Hostname in punycode                    |
|                                   |                                                  |
|                                   | - **4: **Host port                               |
|                                   |                                                  |
|                                   | - **5:** Canonicalized URL path part according   |
|                                   |   to schema requirements                         |
|                                   |                                                  |
|                                   | - **6:** Query parameters (for http\\s only)     |
|                                   |                                                  |
|                                   | - **7:** Fragment parameters (for http\\s only)  |
+-----------------------------------+--------------------------------------------------+
| description(Array)                | (*Mac only*) Description of components related   |
|                                   | to Cortex XSIAM . For example, the description   |
|                                   | of the ROP, JIT, Dylib hijacking modules for Mac |
|                                   | endpoints is Memory Corruption Exploit.          |
+-----------------------------------+--------------------------------------------------+

####### Config logs

The syslog format is as follows:

    recordType, class, FUTURE_USE, subClassId, eventType, eventCategory, generatedTime, serverTime, FUTURE_USE, facility, customerId, trapsId, serverHost, serverComponentVersion, regionId, isEndpoint, severity, trapsSeverity, messageCode, friendlyName, FUTURE_USE, msgTextEn, userFullName, userName, userRole, userDomain, additionalData(Array), messageCode, errorText, errorData, resultData

Fields for config logs

+-----------------------------------+---------------------------------------+
| Field Name                        | Description                           |
+===================================+=======================================+
| recordType                        | Record type associated with the event |
|                                   | and that you can use when managing    |
|                                   | logging quotas. In this case, the     |
|                                   | record type is config which includes  |
|                                   | logs related to Cortex XSIAM          |
|                                   | administration and configuration      |
|                                   | changes.                              |
+-----------------------------------+---------------------------------------+
| class                             | Class of Cortex XSIAM log. System     |
|                                   | logs have a value of system.          |
+-----------------------------------+---------------------------------------+
| subClass                          | Subclass of event. Used to categorize |
|                                   | logs in Cortex XSIAM.                 |
+-----------------------------------+---------------------------------------+
| subClassId                        | Numeric representation of the         |
|                                   | subClass field for easy sorting and   |
|                                   | filtering.                            |
+-----------------------------------+---------------------------------------+
| eventType                         | Subtype of event.                     |
+-----------------------------------+---------------------------------------+
| eventCategory                     | Category of event, used internally    |
|                                   | for processing the flow of logs.      |
|                                   | Event categories vary by class:       |
|                                   |                                       |
|                                   | - **config:** deviceManagement,       |
|                                   |   distributionManagement,             |
|                                   |   reportManagement,                   |
|                                   |   securityEventManagement,            |
|                                   |   systemManagement                    |
|                                   |                                       |
|                                   | - **policy:** exceptionManagement,    |
|                                   |   policyManagement,                   |
|                                   |   profileManagement, sam              |
|                                   |                                       |
|                                   | - **system:** licensing,              |
|                                   |   provisioning, tenant,               |
|                                   |   userAuthentication,                 |
|                                   |   workerProcessing                    |
|                                   |                                       |
|                                   | - **agent_log:** agentFlow            |
+-----------------------------------+---------------------------------------+
| generatedTime                     | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | event was logged. For agent events,   |
|                                   | this represents the time on the       |
|                                   | endpoint. For policy, configuration,  |
|                                   | and system events, this represents    |
|                                   | the time on Cortex XSIAM in ISO-8601  |
|                                   | string representation (for example,   |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| serverTime                        | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which the   |
|                                   | server generated the log. If the log  |
|                                   | was generated on an endpoint, this    |
|                                   | field identifies the time the server  |
|                                   | received the log in ISO-8601 string   |
|                                   | representation (for example,          |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| facility                          | The Cortex XSIAM system component     |
|                                   | that initiated the event, for         |
|                                   | example: TrapsAgent,                  |
|                                   | TrapsServiceCore,                     |
|                                   | TrapsServiceManagement, and           |
|                                   | TrapsServiceBackend.                  |
+-----------------------------------+---------------------------------------+
| customerId                        | The ID that uniquely identifies the   |
|                                   | Cortex XSIAM tenant instance which    |
|                                   | received this log record.             |
+-----------------------------------+---------------------------------------+
| trapsId                           | Tenant external ID.                   |
+-----------------------------------+---------------------------------------+
| serverHost                        | Hostname of Cortex XSIAM.             |
+-----------------------------------+---------------------------------------+
| serverComponentVersion            | Software version of Cortex XSIAM.     |
+-----------------------------------+---------------------------------------+
| regionId                          | ID of Cortex XSIAM region:            |
|                                   |                                       |
|                                   | - **10:** Americas (N. Virginia)      |
|                                   |                                       |
|                                   | - **70:** EMEA (Frankfurt)            |
+-----------------------------------+---------------------------------------+
| isEndpoint                        | Indicates whether the event occurred  |
|                                   | on an endpoint.                       |
|                                   |                                       |
|                                   | - **0:** No, host is not an endpoint. |
|                                   |                                       |
|                                   | - **1:** Yes, host is an endpoint.    |
+-----------------------------------+---------------------------------------+
| agentId                           | Unique identifier for the Cortex XDR  |
|                                   | agent.                                |
+-----------------------------------+---------------------------------------+
| severity                          | Syslog severity level associated with |
|                                   | the event.                            |
|                                   |                                       |
|                                   | - **2:** Critical. Used for events    |
|                                   |   that require immediate attention.   |
|                                   |                                       |
|                                   | - **3:** Error. Used for events that  |
|                                   |   require special handling.           |
|                                   |                                       |
|                                   | - **4:** Warning. Used for events     |
|                                   |   that sometimes require special      |
|                                   |   handling.                           |
|                                   |                                       |
|                                   | - **5:** Notice. Used for normal but  |
|                                   |   significant events that can require |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | - **6:** Informational. Informational |
|                                   |   events that do not require          |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | Each event also has an                |
|                                   | associated Cortex XSIAM severity. See |
|                                   | the `messageData.trapsSeverity` field |
|                                   | for details.                          |
+-----------------------------------+---------------------------------------+
| trapsSeverity                     | Severity level associated with the    |
|                                   | event defined for Cortex XSIAM. Each  |
|                                   | of these severities corresponds to a  |
|                                   | syslog severity level:                |
|                                   |                                       |
|                                   | - **0:** Informational. Informational |
|                                   |   messages that do not require        |
|                                   |   attention. Identical to the syslog  |
|                                   |   6 (Informational) severity level.   |
|                                   |                                       |
|                                   | - **1:** Low. Used for normal but     |
|                                   |   significant events that can require |
|                                   |   attention. Corresponds to the       |
|                                   |   syslog 5 (Notice) severity level.   |
|                                   |                                       |
|                                   | - **2:** Medium. Used for events that |
|                                   |   sometimes require special handling. |
|                                   |   Corresponds to the syslog 4         |
|                                   |   (Warning) severity level.           |
|                                   |                                       |
|                                   | - **3:** High. Used for events that   |
|                                   |   require special handling.           |
|                                   |   Corresponds to the syslog 3 (Error) |
|                                   |   severity level.                     |
|                                   |                                       |
|                                   | - **4:** Critical. Used for events    |
|                                   |   that require immediate attention.   |
|                                   |   Corresponds to the syslog 2         |
|                                   |   (Critical) severity level.          |
|                                   |                                       |
|                                   | See also the `severity` log field.    |
+-----------------------------------+---------------------------------------+
| messageCode                       | System-wide unique message code.      |
+-----------------------------------+---------------------------------------+
| friendlyName                      | Descriptive log message name.         |
+-----------------------------------+---------------------------------------+
| msgTextEn                         | Description of the event, in English. |
+-----------------------------------+---------------------------------------+
| userFullName                      | Full username of Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userName                          | Username associated with Cortex XSIAM |
|                                   | user.                                 |
+-----------------------------------+---------------------------------------+
| userRole                          | Role assigned to Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userDomain                        | Domain to which the user belongs.     |
+-----------------------------------+---------------------------------------+
| agentTime                         | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | agent logged an event in ISO-8601     |
|                                   | string representation.                |
+-----------------------------------+---------------------------------------+
| tzOffset                          | Effective endpoint time zone offset   |
|                                   | from UTC, in minutes.                 |
+-----------------------------------+---------------------------------------+
| osType                            | Operating system of the endpoint:     |
|                                   |                                       |
|                                   | - **1:** Windows                      |
|                                   |                                       |
|                                   | - **2:** OS X/macOS                   |
|                                   |                                       |
|                                   | - **3:** Android                      |
|                                   |                                       |
|                                   | - **4:** Linux                        |
+-----------------------------------+---------------------------------------+
| isVdi                             | Indicates whether the endpoint is a   |
|                                   | virtual desktop infrastructure (VDI): |
|                                   |                                       |
|                                   | - **0:** The endpoint is not a VDI    |
|                                   |                                       |
|                                   | - **1:** The endpoint is a VDI        |
+-----------------------------------+---------------------------------------+
| osVersion                         | Full version number of the operating  |
|                                   | system running on the endpoint. For   |
|                                   | example, 6.1.7601.19135.              |
+-----------------------------------+---------------------------------------+
| is64                              | Indicates whether the endpoint is     |
|                                   | running a 64-bit version of Windows:  |
|                                   |                                       |
|                                   | - **0:** The endpoint is not running  |
|                                   |   x64 architecture                    |
|                                   |                                       |
|                                   | - **1: **The endpoint is running x64  |
|                                   |   architecture                        |
+-----------------------------------+---------------------------------------+
| agentIp                           | IP address of the endpoint.           |
+-----------------------------------+---------------------------------------+
| deviceName                        | Hostname of the endpoint on which the |
|                                   | event was logged.                     |
+-----------------------------------+---------------------------------------+
| deviceDomain                      | Domain to which the endpoint belongs. |
+-----------------------------------+---------------------------------------+
| agentVersion                      | Version of the Cortex XSIAM agent.    |
+-----------------------------------+---------------------------------------+
| contentVersion                    | Content version in the local security |
|                                   | policy.                               |
+-----------------------------------+---------------------------------------+
| protectionStatus                  | Cortex XSIAM agent protection status: |
|                                   |                                       |
|                                   | - **0:** Protected                    |
|                                   |                                       |
|                                   | - **1:** OsVersionIncompatible        |
|                                   |                                       |
|                                   | - **2:** AgentIncompatible            |
+-----------------------------------+---------------------------------------+
| userFullName                      | Full name of Cortex XSIAM user.       |
+-----------------------------------+---------------------------------------+
| userName                          | Username associated with Cortex XSIAM |
|                                   | user.                                 |
+-----------------------------------+---------------------------------------+
| userRole                          | Role assigned to Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userDomain                        | Domain to which the user belongs.     |
+-----------------------------------+---------------------------------------+
| messageName                       | Name of the message.                  |
+-----------------------------------+---------------------------------------+
| messageId                         | Unique numeric identifier of the      |
|                                   | message.                              |
+-----------------------------------+---------------------------------------+
| processStatus                     | State of the process related to the   |
|                                   | event.                                |
+-----------------------------------+---------------------------------------+
| errorText                         | If known, a description of the        |
|                                   | documented error.                     |
+-----------------------------------+---------------------------------------+
| errorData                         | Parameters related to an event error. |
+-----------------------------------+---------------------------------------+
| resultData                        | Parameters related to a successful    |
|                                   | event.                                |
+-----------------------------------+---------------------------------------+
| parameters                        | Parameters supplied in the log        |
|                                   | message.                              |
+-----------------------------------+---------------------------------------+
| additionalData(Array)             | Additional information regarding      |
|                                   | event parameters.                     |
+-----------------------------------+---------------------------------------+
| loggedInUser                      | User that is logged in to the Cortex  |
|                                   | XSIAM.                                |
+-----------------------------------+---------------------------------------+

####### Analytics logs

The syslog format is as follows:

    recordType, class, FUTURE_USE, eventType, eventCategory, generatedTime, serverTime, agentTime, tzOffset, FUTURE_USE, facility, customerId, trapsId, serverHost, serverComponentVersion, regionId, isEndpoint, agentId, osType, isVdi, osVersion, is64, agentIp, deviceName, deviceDomain, severity, agentVersion, contentVersion, protectionStatus, sha256, type, parentSha256, lastSeen, fileName, filePath, fileSize, localAnalysisResult, reported, blocked, executionCount

Fields for analytics logs

+-----------------------------------+---------------------------------------+
| Field Name                        | Description                           |
+===================================+=======================================+
| recordType                        | Record type associated with the event |
|                                   | and that you can use when managing    |
|                                   | logging quotas. In this case, the     |
|                                   | record type is analytics which        |
|                                   | includes hash execution reports from  |
|                                   | the agent.                            |
+-----------------------------------+---------------------------------------+
| class                             | Class of Cortex XSIAM log: config,    |
|                                   | policy, system, and agent_log.        |
+-----------------------------------+---------------------------------------+
| eventType                         | Subtype of event.                     |
+-----------------------------------+---------------------------------------+
| eventCategory                     | Category of event, used internally    |
|                                   | for processing the flow of logs.      |
|                                   | Event categories vary by class:       |
|                                   |                                       |
|                                   | - **config:** deviceManagement,       |
|                                   |   distributionManagement,             |
|                                   |   securityEventManagement,            |
|                                   |   systemManagement                    |
|                                   |                                       |
|                                   | - **policy:** exceptionManagement,    |
|                                   |   policyManagement,                   |
|                                   |   profileManagement, sam              |
|                                   |                                       |
|                                   | - **system:** licensing,              |
|                                   |   provisioning, tenant,               |
|                                   |   userAuthentication,                 |
|                                   |   workerProcessing                    |
|                                   |                                       |
|                                   | - **agent_log:** agentFlow            |
+-----------------------------------+---------------------------------------+
| generatedTime                     | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | event was logged. For agent events,   |
|                                   | this represents the time on the       |
|                                   | endpoint. For policy, configuration,  |
|                                   | and system events, this represents    |
|                                   | the time on Cortex XSIAM in ISO-8601  |
|                                   | string representation (for example,   |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| serverTime                        | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which the   |
|                                   | server generated the log. If the log  |
|                                   | was generated on an endpoint, this    |
|                                   | field identifies the time the server  |
|                                   | received the log in ISO-8601 string   |
|                                   | representation (for example,          |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| agentTime                         | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | agent logged an event in ISO-8601     |
|                                   | string representation.                |
+-----------------------------------+---------------------------------------+
| tzOffset                          | Effective endpoint time zone offset   |
|                                   | from UTC, in minutes.                 |
+-----------------------------------+---------------------------------------+
| facility                          | The Cortex XSIAM system component     |
|                                   | that initiated the event, for         |
|                                   | example: TrapsAgent,                  |
|                                   | TrapsServiceCore,                     |
|                                   | TrapsServiceManagement, and           |
|                                   | TrapsServiceBackend.                  |
+-----------------------------------+---------------------------------------+
| customerId                        | The ID that uniquely identifies the   |
|                                   | Cortex XSIAM tenant instance which    |
|                                   | received this log record.             |
+-----------------------------------+---------------------------------------+
| trapsId                           | Tenant external ID.                   |
+-----------------------------------+---------------------------------------+
| serverHost                        | Hostname of Cortex XSIAM.             |
+-----------------------------------+---------------------------------------+
| serverComponentVersion            | Software version of Cortex XSIAM.     |
+-----------------------------------+---------------------------------------+
| regionId                          | ID of Cortex XSIAM region:            |
|                                   |                                       |
|                                   | - **10:** Americas (N. Virginia)      |
|                                   |                                       |
|                                   | - **70:** EMEA (Frankfurt)            |
+-----------------------------------+---------------------------------------+
| isEndpoint                        | Indicates whether the event occurred  |
|                                   | on an endpoint.                       |
|                                   |                                       |
|                                   | - **0:** No, host is not an endpoint. |
|                                   |                                       |
|                                   | - **1:** Yes, host is an endpoint.    |
+-----------------------------------+---------------------------------------+
| agentId                           | Unique identifier for the Cortex XDR  |
|                                   | agent.                                |
+-----------------------------------+---------------------------------------+
| osType                            | Operating system of the endpoint:     |
|                                   |                                       |
|                                   | - **1:** Windows                      |
|                                   |                                       |
|                                   | - **2:** OS X/macOS                   |
|                                   |                                       |
|                                   | - **3:** Android                      |
|                                   |                                       |
|                                   | - **4:** Linux                        |
+-----------------------------------+---------------------------------------+
| isVdi                             | Indicates whether the endpoint is a   |
|                                   | virtual desktop infrastructure (VDI): |
|                                   |                                       |
|                                   | - **0:** The endpoint is not a VDI    |
|                                   |                                       |
|                                   | - **1:** The endpoint is a VDI        |
+-----------------------------------+---------------------------------------+
| osVersion                         | Full version number of the operating  |
|                                   | system running on the endpoint. For   |
|                                   | example, 6.1.7601.19135.              |
+-----------------------------------+---------------------------------------+
| is64                              | Indicates whether the endpoint is     |
|                                   | running a 64-bit version of Windows:  |
|                                   |                                       |
|                                   | - **0:** The endpoint is not running  |
|                                   |   x64 architecture                    |
|                                   |                                       |
|                                   | - **1:** The endpoint is running x64  |
|                                   |   architecture                        |
+-----------------------------------+---------------------------------------+
| agentIp                           | IP address of the endpoint.           |
+-----------------------------------+---------------------------------------+
| deviceName                        | Hostname of the endpoint on which the |
|                                   | event was logged.                     |
+-----------------------------------+---------------------------------------+
| deviceDomain                      | Domain to which the endpoint belongs. |
+-----------------------------------+---------------------------------------+
| severity                          | Syslog severity level associated with |
|                                   | the event.                            |
|                                   |                                       |
|                                   | - **2:** Critical. Used for events    |
|                                   |   that require immediate attention.   |
|                                   |                                       |
|                                   | - **3:** Error. Used for events that  |
|                                   |   require special handling.           |
|                                   |                                       |
|                                   | - **4:** Warning. Used for events     |
|                                   |   that sometimes require special      |
|                                   |   handling.                           |
|                                   |                                       |
|                                   | - **5:** Notice. Used for normal but  |
|                                   |   significant events that can require |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | - **6:** Informational. Informational |
|                                   |   events that do not require          |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | Each event also has an                |
|                                   | associated Cortex XSIAM severity. See |
|                                   | the `messageData.trapsSeverity` field |
|                                   | for details.                          |
+-----------------------------------+---------------------------------------+
| agentVersion                      | Version of the Cortex XDR agent.      |
+-----------------------------------+---------------------------------------+
| contentVersion                    | Content version in the local security |
|                                   | policy.                               |
+-----------------------------------+---------------------------------------+
| protectionStatus                  | Cortex XDR agent protection status:   |
|                                   |                                       |
|                                   | - **0:** Protected                    |
|                                   |                                       |
|                                   | - **1: **OsVersionIncompatible        |
|                                   |                                       |
|                                   | - **2:** AgentIncompatible            |
+-----------------------------------+---------------------------------------+
| sha256                            | Hash of the file using SHA256         |
|                                   | encoding.                             |
+-----------------------------------+---------------------------------------+
| type                              | Type of file:                         |
|                                   |                                       |
|                                   | - **0:** Unknown                      |
|                                   |                                       |
|                                   | - **1:** PE                           |
|                                   |                                       |
|                                   | - **2:** Mach-o                       |
|                                   |                                       |
|                                   | - **3:** DLL                          |
|                                   |                                       |
|                                   | - **4:** Office file (containing a    |
|                                   |   macro)                              |
+-----------------------------------+---------------------------------------+
| parentSha256                      | Hash of the parent file using SHA256  |
|                                   | encoding.                             |
+-----------------------------------+---------------------------------------+
| lastSeen                          | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time when the file  |
|                                   | last ran on an endpoint in ISO-8601   |
|                                   | string representation (for example,   |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| fileName                          | File name, without the path or the    |
|                                   | file type extension.                  |
+-----------------------------------+---------------------------------------+
| filePath                          | Full path, aligned to the OS format.  |
+-----------------------------------+---------------------------------------+
| fileSize                          | Size of the file in bytes.            |
+-----------------------------------+---------------------------------------+
| localAnalysisResult               | This object includes the content      |
|                                   | version, local analysis module        |
|                                   | version, verdict result, file signer, |
|                                   | and trusted signer result. The        |
|                                   | trusted signer result is an integer   |
|                                   | value:                                |
|                                   |                                       |
|                                   | - **0:** Cortex XSIAMdid not evaluate |
|                                   |   the signer of the file.             |
|                                   |                                       |
|                                   | - **1:** The signer is trusted.       |
|                                   |                                       |
|                                   | - **2:** The signer is not trusted.   |
+-----------------------------------+---------------------------------------+
| reported                          | Reporting status of the file, in      |
|                                   | integer value:                        |
|                                   |                                       |
|                                   | - **0:** Cortex XSIAM did not report  |
|                                   |   the security event.                 |
|                                   |                                       |
|                                   | - **1:** Cortex XSIAM reported the    |
|                                   |   security event.                     |
+-----------------------------------+---------------------------------------+
| blocked                           | Blocking status of the file, in       |
|                                   | integer value:                        |
|                                   |                                       |
|                                   | - **0:** Cortex XSIAM did not block   |
|                                   |   the process or file.                |
|                                   |                                       |
|                                   | - **1:** Cortex XSIAM blocked the     |
|                                   |   process or file.                    |
+-----------------------------------+---------------------------------------+
| executionCount                    | The total number of times a file      |
|                                   | identified by a specific hash was     |
|                                   | executed.                             |
+-----------------------------------+---------------------------------------+

####### System logs

The syslog format is as follows:

    recordType, class, FUTURE_USE, subClassId, eventType, eventCategory, generatedTime, serverTime, FUTURE_USE, facility, customerId, trapsId, serverHost, serverComponentVersion, regionId, isEndpoint, agentId, severity, trapsSeverity, messageCode, friendlyName, FUTURE_USE, msgTextEn, userFullName, username, userRole, userDomain, agentTime, tzOffset, osType, isVdi, osVersion, is64, agentIp, deviceName, deviceDomain, agentVersion, contentVersion, protectionStatus, userFullName, username, userRole, userDomain, messageName, messageId, processStatus, errorText, errorData, resultData, parameters, additionalData(Array)

Fields for system logs

+-----------------------------------+---------------------------------------+
| Field Name                        | Description                           |
+===================================+=======================================+
| recordType                        | Record type associated with the event |
|                                   | and that you can use when managing    |
|                                   | logging quotas. In this case, the     |
|                                   | record type is system which includes  |
|                                   | logs related to automated system      |
|                                   | management and agent reporting        |
|                                   | events.                               |
+-----------------------------------+---------------------------------------+
| class                             | Class of Cortex XSIAM log. System     |
|                                   | logs have a value of system.          |
+-----------------------------------+---------------------------------------+
| subClass                          | Subclass of event. Used to categorize |
|                                   | logs in Cortex XSIAM user interface.  |
+-----------------------------------+---------------------------------------+
| subClassId                        | Numeric representation of the         |
|                                   | subClass field for easy sorting and   |
|                                   | filtering.                            |
+-----------------------------------+---------------------------------------+
| eventType                         | Subtype of event.                     |
+-----------------------------------+---------------------------------------+
| eventCategory                     | Category of event, used internally    |
|                                   | for processing the flow of logs.      |
|                                   | Event categories vary by class:       |
|                                   |                                       |
|                                   | - **config:** deviceManagement,       |
|                                   |   distributionManagement,             |
|                                   |   securityEventManagement,            |
|                                   |   systemManagement                    |
|                                   |                                       |
|                                   | - **policy: **exceptionManagement,    |
|                                   |   policyManagement,                   |
|                                   |   profileManagement, sam              |
|                                   |                                       |
|                                   | - **system:** licensing,              |
|                                   |   provisioning, tenant,               |
|                                   |   userAuthentication,                 |
|                                   |   workerProcessing                    |
|                                   |                                       |
|                                   | - **agent_log:** agentFlow            |
+-----------------------------------+---------------------------------------+
| generatedTime                     | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | event was logged. For agent events,   |
|                                   | this represents the time on the       |
|                                   | endpoint. For policy, configuration,  |
|                                   | and system events, this represents    |
|                                   | the time on Cortex XSIAM in ISO-8601  |
|                                   | string representation (for example,   |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| serverTime                        | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which the   |
|                                   | server generated the log. If the log  |
|                                   | was generated on an endpoint, this    |
|                                   | field identifies the time the server  |
|                                   | received the log in ISO-8601 string   |
|                                   | representation (for example,          |
|                                   | 2017-01-24T09:08:59Z).                |
+-----------------------------------+---------------------------------------+
| facility                          | The Cortex XSIAM system component     |
|                                   | that initiated the event, for         |
|                                   | example: TrapsAgent,                  |
|                                   | TrapsServiceCore,                     |
|                                   | TrapsServiceManagement, and           |
|                                   | TrapsServiceBackend.                  |
+-----------------------------------+---------------------------------------+
| customerId                        | The ID that uniquely identifies the   |
|                                   | Cortex XSIAM tenant instance which    |
|                                   | received this log record.             |
+-----------------------------------+---------------------------------------+
| trapsId                           | Tenant external ID.                   |
+-----------------------------------+---------------------------------------+
| serverHost                        | Hostname of Cortex XSIAM.             |
+-----------------------------------+---------------------------------------+
| serverComponentVersion            | Software version of Cortex XSIAM.     |
+-----------------------------------+---------------------------------------+
| regionId                          | ID of Cortex XSIAM region:            |
|                                   |                                       |
|                                   | - **10:** Americas (N. Virginia)      |
|                                   |                                       |
|                                   | - **70** EMEA (Frankfurt)             |
+-----------------------------------+---------------------------------------+
| isEndpoint                        | Indicates whether the event occurred  |
|                                   | on an endpoint.                       |
|                                   |                                       |
|                                   | - **0:** No, host is not an endpoint. |
|                                   |                                       |
|                                   | - **1:** Yes, host is an endpoint.    |
+-----------------------------------+---------------------------------------+
| agentId                           | Unique identifier for the Cortex XDR  |
|                                   | agent.                                |
+-----------------------------------+---------------------------------------+
| severity                          | Syslog severity level associated with |
|                                   | the event.                            |
|                                   |                                       |
|                                   | - **2:** Critical. Used for events    |
|                                   |   that require immediate attention.   |
|                                   |                                       |
|                                   | - **3:** Error. Used for events that  |
|                                   |   require special handling.           |
|                                   |                                       |
|                                   | - **4:** Warning. Used for events     |
|                                   |   that sometimes require special      |
|                                   |   handling.                           |
|                                   |                                       |
|                                   | - **5:** Notice. Used for normal but  |
|                                   |   significant events that can require |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | - **6: **Informational. Informational |
|                                   |   events that do not require          |
|                                   |   attention.                          |
|                                   |                                       |
|                                   | Each event also has an                |
|                                   | associated Cortex XSIAM severity. See |
|                                   | the `messageData.trapsSeverity` field |
|                                   | for details.                          |
+-----------------------------------+---------------------------------------+
| trapsSeverity                     | Severity level associated with the    |
|                                   | event defined for Cortex XSIAM. Each  |
|                                   | of these severities corresponds to a  |
|                                   | syslog severity level:                |
|                                   |                                       |
|                                   | - **0:** Informational. Informational |
|                                   |   messages that do not require        |
|                                   |   attention. Identical to the syslog  |
|                                   |   6 (Informational) severity level.   |
|                                   |                                       |
|                                   | - **1:** Low. Used for normal but     |
|                                   |   significant events that can require |
|                                   |   attention. Corresponds to the       |
|                                   |   syslog 5 (Notice) severity level.   |
|                                   |                                       |
|                                   | - **2:** Medium. Used for events that |
|                                   |   sometimes require special handling. |
|                                   |   Corresponds to the syslog 4         |
|                                   |   (Warning) severity level.           |
|                                   |                                       |
|                                   | - **3:** High. Used for events that   |
|                                   |   require special handling.           |
|                                   |   Corresponds to the syslog 3 (Error) |
|                                   |   severity level.                     |
|                                   |                                       |
|                                   | - **4:** Critical. Used for events    |
|                                   |   that require immediate attention.   |
|                                   |   Corresponds to the syslog 2         |
|                                   |   (Critical) severity level.          |
|                                   |                                       |
|                                   | See also the `severity` log field.    |
+-----------------------------------+---------------------------------------+
| messageCode                       | System-wide unique message code.      |
+-----------------------------------+---------------------------------------+
| friendlyName                      | Descriptive log message name.         |
+-----------------------------------+---------------------------------------+
| msgTextEn                         | Description of the event, in English. |
+-----------------------------------+---------------------------------------+
| userFullName                      | Full username of Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userName                          | Username associated with Cortex XSIAM |
|                                   | user.                                 |
+-----------------------------------+---------------------------------------+
| userRole                          | Role assigned to Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userDomain                        | Domain to which the user belongs.     |
+-----------------------------------+---------------------------------------+
| agentTime                         | Coordinated Universal Time (UTC)      |
|                                   | equivalent of the time at which an    |
|                                   | agent logged an event in ISO-8601     |
|                                   | string representation.                |
+-----------------------------------+---------------------------------------+
| tzOffset                          | Effective endpoint time zone offset   |
|                                   | from UTC, in minutes.                 |
+-----------------------------------+---------------------------------------+
| osType                            | Operating system of the endpoint:     |
|                                   |                                       |
|                                   | - **1:** Windows                      |
|                                   |                                       |
|                                   | - **2: **OS X/macOS                   |
|                                   |                                       |
|                                   | - **3:** Android                      |
|                                   |                                       |
|                                   | - **4:** Linux                        |
+-----------------------------------+---------------------------------------+
| isVdi                             | Indicates whether the endpoint is a   |
|                                   | virtual desktop infrastructure (VDI): |
|                                   |                                       |
|                                   | - **0:** The endpoint is not a VDI    |
|                                   |                                       |
|                                   | - **1:** The endpoint is a VDI        |
+-----------------------------------+---------------------------------------+
| osVersion                         | Full version number of the operating  |
|                                   | system running on the endpoint. For   |
|                                   | example, 6.1.7601.19135.              |
+-----------------------------------+---------------------------------------+
| is64                              | Indicates whether the endpoint is     |
|                                   | running a 64-bit version of Windows:  |
|                                   |                                       |
|                                   | - **0:** The endpoint is not running  |
|                                   |   x64 architecture                    |
|                                   |                                       |
|                                   | - **1:** The endpoint is running x64  |
|                                   |   architecture                        |
+-----------------------------------+---------------------------------------+
| agentIp                           | IP address of the endpoint.           |
+-----------------------------------+---------------------------------------+
| deviceName                        | Hostname of the endpoint on which the |
|                                   | event was logged.                     |
+-----------------------------------+---------------------------------------+
| deviceDomain                      | Domain to which the endpoint belongs. |
+-----------------------------------+---------------------------------------+
| agentVersion                      | Version of the Cortex XDR agent.      |
+-----------------------------------+---------------------------------------+
| contentVersion                    | Content version in the local security |
|                                   | policy.                               |
+-----------------------------------+---------------------------------------+
| protectionStatus                  | Cortex XDR agent protection status:   |
|                                   |                                       |
|                                   | - **0:** Protected                    |
|                                   |                                       |
|                                   | - **1:** OsVersionIncompatible        |
|                                   |                                       |
|                                   | - **2:** AgentIncompatible            |
+-----------------------------------+---------------------------------------+
| userFullName                      | Full name of Cortex XSIAM user.       |
+-----------------------------------+---------------------------------------+
| userName                          | Username associated with Cortex XSIAM |
|                                   | user.                                 |
+-----------------------------------+---------------------------------------+
| userRole                          | Role assigned to Cortex XSIAM user.   |
+-----------------------------------+---------------------------------------+
| userDomain                        | Domain to which the user belongs.     |
+-----------------------------------+---------------------------------------+
| messageName                       | Name of the message.                  |
+-----------------------------------+---------------------------------------+
| messageId                         | Unique numeric identifier of the      |
|                                   | message.                              |
+-----------------------------------+---------------------------------------+
| processStatus                     | State of the process related to the   |
|                                   | event.                                |
+-----------------------------------+---------------------------------------+
| errorText                         | If known, a description of the        |
|                                   | documented error.                     |
+-----------------------------------+---------------------------------------+
| errorData                         | Parameters related to an event error. |
+-----------------------------------+---------------------------------------+
| resultData                        | Parameters related to a successful    |
|                                   | event.                                |
+-----------------------------------+---------------------------------------+
| parameters                        | Parameters supplied in the log        |
|                                   | message.                              |
+-----------------------------------+---------------------------------------+
| additionalData(Array)             | Additional information regarding      |
|                                   | event parameters.                     |
+-----------------------------------+---------------------------------------+
| loggedInUser                      | User that is logged in to the Cortex  |
|                                   | XSIAM.                                |
+-----------------------------------+---------------------------------------+

### Remote repository management

Use a content management system with a remote repository to develop and
test content before using it in production.

#### Cortex XSIAM development tenant

A development tenant is a test environment where you can create and
check content before using it live in a production tenant.

Before explaining more about development tenants, it is important to
understand what content is.

##### Content

Content includes integrations, automation scripts, playbooks, and other
components that enhance Cortex XSIAM capabilities for case response and
threat intelligence management. There are two types of content:

- System content - content packs you can download from Marketplace.
  Packs are groups of components that implement use cases. Content packs
  are created by Palo Alto Networks, technology partners, consulting
  companies, MSSPs, customers, and individual contributors. Depending on
  the use case, each content pack includes a combination of different
  components, such as integrations, scripts, playbooks, and widgets.

- Custom or user-defined content - custom components you can develop to
  meet your business needs.

##### Development tenants

The development tenant provides a safe environment to develop and test
the functionality of content before using it in a production
environment.

> **Important**
>
> Development tenants are not intended for performance checks; they
> cannot access production data, and they are connected to a limited
> number of endpoints. As a result, all development tenants have fewer
> resources than the production tenant, including data ingestion
> capacity and performance, and compute capabilities. In a development
> tenant, extreme demand for resources for data ingestion or compute may
> affect performance and cause latency issues.

After you develop your content, if you want it to be available as part
of a content update for the production tenant or additional development
tenants, you must push the content from the development tenant to a
remote repository.

##### Content management using a remote repository

In Cortex XSIAM you can use a content management system with a remote
repository to develop and test content. You can choose which type of
remote repository you want to use, either the Cortex XSIAM built-in
remote repository (default), or you can add any private content
repository that is Git-based, including GitHub, GitLab, and Bitbucket.
In addition, on-premise repositories are also supported.

The development tenant pushes content to a remote repository, and the
production tenant or additional development tenants pull content from
the remote repository.

**Push and pull content between tenants**

In a cluster of tenants that includes one production tenant and one or
more development tenants, only one development tenant pushes (the push
tenant). The production tenant and any other development tenants pull
content from the push tenant (pull tenants).

**Push and pull system content**

Only the development push tenant manages the system content and updates.
Pull tenants cannot manage system content, meaning they cannot download,
install, edit, create, or update system content; they are configured to
only pull system content from the push tenant. Only the development push
tenant has access to Marketplace, so system content updates from
Marketplace are delivered only to the development push tenant. Pull
tenants do not have Marketplace, so all system content must first be
downloaded and installed on the push tenant, pushed to the remote
repository, and then pulled into the pull tenants.

**Push and pull custom content**

Not all custom content can be pushed/pulled. Content that cannot be
pushed/pulled can be developed wherever you prefer - in both the
development and production tenants, or copied from the development
tenant into the production tenant. For example, content that cannot be
pushed/pulled includes dashboards and lists, parsing rules, data
modeling rules, and correlation rules.

The following system and user-defined content types are push/pull
supported:

- Issue types and fields

- Indicator types and fields

- Issue and indicator layouts

- Layouts

- Classifiers

- Integrations

- Playbooks

- Scripts

For custom content that can be pushed/pulled, when pushing content from
the development tenant, the content is pulled into the production or
other development pull tenants as content updates. You can decide which
updates you want to push from the development push tenant to pull
tenants via the remote repository.

#### Set up a remote repository

When you set up a remote repository, you can use the Cortex XSIAM
built-in remote repository, add any private remote repository that is
Git-based, or use an on-prem repository.

**Considerations**

- When you activate a tenant and enable the content repository in Cortex
  Gateway, Cortex XSIAM by default uses the the built-in repository. The
  built-in remote repository requires fewer configurations than using a
  private remote repository and cannot be accessed directly. If you want
  to use a private remote repository, you need to configure it when you
  enable the remote repository in the tenant.

- When activating a new development tenant in Cortex Gateway for remote
  repository (adding it to a cluster), all tenants already in the
  cluster need to be activated and enabled for push/pull.

- After the remote repository is enabled in the production tenant as a
  pull tenant, by default, the first activated development tenant is set
  to push content to the remote repository. When you add additional
  development tenants, they are automatically set to pull content from
  the remote repository.

- If the content repository option is disabled for the production or
  development tenant (under Settings \> Configurations \> General \>
  Remote Repository Settings, toggle the **Content repository** slider
  to off), the tenant becomes standalone and does not push or pull
  content.

<!-- -->

- If you disable the remote repository feature, content on the tenant is
  not deleted. If you enable the remote repository feature again and the
  remote repository contains content, you need to choose which content
  to keep, either the content on the tenant or the content on the remote
  repository. We recommend backing up any content that you want to keep
  before enabling again.

<!-- -->

- When enabling a remote repository in a tenant:

  - If the relevant repository branch is empty, it inherits the content
    of the tenant.

  - If the relevant branch is not empty, you can select which content to
    keep, either the existing content on your tenant or the existing
    content on the specified repository. If you want to keep the content
    on the tenant, you need to first disable the remote repository in
    the other tenants in the cluster (making them standalone). If even
    one tenant has remote repository enabled, you can only keep the
    existing content on the specified repository.

- For a simple one-branch deployment, we recommend using the built-in
  repository. If you want to use multiple branches, or if you need
  access to the content repository outside the Cortex XSIAM platform
  (for example to implement some scanners) you must use a private
  repository.

<!-- -->

- If you want to use a private remote repository with one or more
  branches, you need to enable the remote repository in each tenant and
  then set up the different branches you want to use in each tenant.

<!-- -->

- Activation may take some time. You should receive notification by
  email that the production or development tenant has completed the
  activation process.

- Once the activation completes, you can only change content repository
  settings within the tenant.

**Before you begin**

- If you are changing your remote repository settings, back up existing
  content to your local computer by navigating to Settings \>
  Configurations \> General \> Server Settings \> Custom Content and
  click **Export all custom content**.

- You must have Instance Administrator or Account Admin permission to
  set up a remote repository.

##### Set up a built-in remote repository

The following are typical scenarios for setting up a built-in remote
repository for the production and one or more development tenants.

> **Note**
>
> Once enabled, development tenants have a red banner on the top left
> showing **DEV**.

###### New development tenant and new or existing production tenant

In this scenario, the production tenant is first activated as a
standalone (by default), and the built-in remote repository is then
enabled in the production tenant (as a pull tenant). Once enabled, the
first development tenant becomes the push tenant and any additional
tenants become pull tenants.

Perform the following procedures in the order listed below.

####### Task 1. Enable the built-in repository in the production tenant.

1.  In the production tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction is **Pull**.

2.  In the **Repository type** field, select **Built-in**, and save the
    settings.

####### Task 2. Activate a new development tenant in Cortex Gateway for a built-in repository.

1.  In [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/accounts) ,
    locate the Cortex XSIAM production tenant where you enabled the
    built-in repository in task 1.

2.  Hover over the Cortex XSIAM tenant and click
    **Activate Dev Tenant**.

3.  Define the following fields:

  -------------------------------------------------------------------------------------------------
  Name                                Details
  ----------------------------------- -------------------------------------------------------------
  DEV TENANT NAME                     Give the Cortex XSIAM dev tenant an easily recognizable name.
                                      Choose a name that is 59 or fewer characters and is unique
                                      across your company account.

  REGION                              Select the region in which you want to set up the Cortex
                                      XSIAM dev tenant.

  DEV TENANT SUBDOMAIN                Give your Cortex XSIAM dev instance an easy to recognize name
                                      that is used to access the tenant directly using the full URL
                                      (`https://<subdomain>xsiam.<region>.paloaltonetworks.com`).
  -------------------------------------------------------------------------------------------------

4.  Select **ENABLE CONTENT REPOSITORY**.

5.  Accept the terms and conditions and activate the tenant.

6.  Repeat this task to activate any additional development tenants in
    Cortex Gateway. They will automatically be set to pull.

###### Existing development and production tenants

In this scenario, the production and development tenants were managed in
parallel with different sets of content. Since they were already
activated in Cortex Gateway, their remote repository settings can only
be changed within the tenants.

> **Note**
>
> The first tenant that is enabled pushes its content to the remote
> repository first. For example, these instructions describe enabling
> the production tenant first, so the remote repository will initially
> contain production tenant content. You can enable a development tenant
> first if you want the remote repository to initially contain the
> content from the development tenant.

Perform the following procedures in the order listed below.

####### Task 1. Enable the built-in repository in the production tenant.

1.  In the production tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction is **Pull**.

2.  In the **Repository type** field, select **Built-in**, and save the
    settings.

####### Task 2. Enable the built-in remote repository in the development tenants.

Once enabled, the first development tenant automatically becomes the
push tenant. For more details about push and pull tenants, see [Cortex
development tenant](#UUIDcd0108ce11b11a2c747b1c6b4ab07d62).

1.  In the development tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction for the first development
  tenant is **Push**. The sync direction for any additional development
  tenants is **Pull**.

2.  In the **Repository type** field, select **Built-in**, and save the
    settings.

3.  Select which content to keep and which to overwrite. If there are
    any discrepancies between the development tenant and remote
    repository (which in this example initially contains the production
    tenant content after it is enabled), the
    **Specified repository is not empty** window opens. Options are:

    - **Existing content on your tenant**: Keeps the existing content on
      your tenant and replaces the content on the specified repository.
      Cortex XSIAM checks if any other tenants are using the remote
      repository. If yes, this option is disabled. In this example, the
      remote repository was already enabled in the production tenant, so
      the remote repository holds production content. If you want to
      keep the content on the development tenant:

      1.  Disable the remote repository in any additional enabled
          tenants. In this case, for the first development tenant, only
          the production tenant must be disabled.

      2.  Select **Existing content on your tenant** for this tenant.

      3.  Complete synchronization.

      4.  Re-enable the remote repository in any additional tenants and
          select **Existing content on the specified repository** in
          each additional tenant.

    - **Existing content on the specified repository**: Deletes the
      existing content on your tenant and replaces it with content from
      the specified repository.

4.  Click **Continue**.

##### Set up a Private Remote Repository

Before you begin, verify that you have network connectivity from Cortex
XSIAM to the private remote repository. All communication goes through
Cortex XSIAM, so it must have access to the remote repository. If direct
access from Cortex XSIAM is not enabled you can use engines with access
to the repository.

> **Tip**
>
> Due to security concerns, there is a closed allow list of approved
> URLs for private repositories. If you want to use a URL that is
> excluded from the allow list, use an engine (engine groups are not
> supported).

The following are typical scenarios for setting up a private remote
repository for the production and one or more development tenants.

> **Note**
>
> Once enabled, the development push tenant has a red banner on the top
> left showing **DEV**.

###### New development tenant and new or existing production tenant

In this scenario, the production tenant is first activated as a
standalone (by default), and the built-in remote repository is then
enabled in the production tenant (as a pull tenant). Once enabled, the
first development tenant becomes the push tenant and any additional
tenants become pull tenants.

Perform the following procedures in the order listed below.

####### Task 1. Enable the private remote repository for the production tenant

1.  In the production tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction is **Pull**.

2.  In the **Repository type** field, select **Private**, and save the
    settings.

3.  Define the Git settings using HTTPS or SSH.

- > **Note**

  - > For repository vendors that use tokens, enter the token type in
    > the **username** field and the token in the **password** field.
    > Verify details with your vendor.

  <!-- -->

  - > If your private Git remote repository uses personal access tokens
    > instead of usernames and passwords, enter the token type in the
    > **username** field and the access token in the **password** field.
    > For example, if you use an OAuth2 token, enter `oauth2` in the
    > **username** field.

    > For Github, enter your username in the **username** field.

  <!-- -->

  - > If using SSH, RSA or ed25519 algorithm private keys are supported.
    > If your SSH connection uses a port other than port 22 (the default
    > SSH port), you must include the SSH string and port number in the
    > **Repository URL** field. In the following example, we use port
    > 20017:

  <!-- -->

  - > `ssh://git@content.demisto.com:20017/~/my-project.git`

  a.  Select the active branch on which you will be working.

  b.  In the **Advanced** section, the engine is set by default. You can
      change the engine by selecting from the list of available engines.

  - > **Note**

    > You can\'t add an engine that has been added to a Load-Balancing
    > Group.

####### Task 2. Activate a new development tenant in Cortex Gateway for a private remote repository

1.  In [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/accounts) ,
    locate the Cortex XSIAM production tenant where you enabled the
    private repository in Task 1.

2.  Hover over the Cortex XSIAM tenant and click
    **Activate Dev Tenant**.

3.  Define the following fields:

  -------------------------------------------------------------------------------------------------
  Name                                Details
  ----------------------------------- -------------------------------------------------------------
  DEV TENANT NAME                     Give the Cortex XSIAM dev tenant an easily recognizable name.
                                      Choose a name that is 59 or fewer characters and is unique
                                      across your company account.

  REGION                              Select the region in which you want to set up the Cortex
                                      XSIAM dev tenant.

  DEV TENANT SUBDOMAIN                Give your Cortex XSIAM dev instance an easy-to-recognize name
                                      that is used to access the tenant directly using the full URL
                                      (`https://<subdomain>xsiam.<region>.paloaltonetworks.com`).
  -------------------------------------------------------------------------------------------------

4.  Accept the terms and conditions and activate the tenant.

####### Task 3. Enable the private remote repository in the development tenants

The first development tenant automatically becomes the push tenant. For
more details about push and pull tenants, see [Cortex development
tenant](#UUIDcd0108ce11b11a2c747b1c6b4ab07d62).

1.  In the development tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction for the first development
  tenant is **Push**. The sync direction for any additional development
  tenants is **Pull**.

2.  In the **Repository type** field, select **Private**.

3.  Define the GitHub settings using HTTPS or SSH.

- > **Note**

  - > If your private Git remote repository uses personal access tokens
    > instead of usernames and passwords, enter the access token in the
    > password field and leave the username field blank.

  - > For repository vendors that use tokens, the token type is entered
    > in the username field and the token is entered in the password
    > field. Verify details with your vendor.

  - > If using SSH, only RSA private keys are supported. If your SSH
    > connection uses a port other than port 22 (the default SSH port),
    > you must include the SSH string and port number in the
    > **Repository URL** field. In the following example, we use port
    > 20017:

  <!-- -->

  - > `ssh://git@content.demisto.com:20017/~/my-project.git`

  a.  Select the active branch on which you will be working.

  - You can either use the same branch as for the pull tenant
    (production or additional development tenant), or a different
    branch. If using a different branch, you need to define a manual or
    automatic merge between branches which is done outside Cortex XSIAM.

  b.  In the **Advanced** section, the engine is set by default. You can
      change the engine by selecting from the list of available engines.

4.  Save the settings.

5.  Repeat tasks 2 and 3 to enable the private remote repository in each
    additional development tenant. They will automatically be set to
    pull.

###### Existing development and production tenants

In this scenario, the production and development tenants were managed in
parallel with different sets of content. Since they were already
activated in Cortex Gateway, their remote repository settings can only
be changed within the tenants.

> **Note**
>
> The first tenant that is enabled pushes its content to the remote
> repository first. For example, these instructions describe enabling
> the production tenant first, so the remote repository will initially
> contain production tenant content. You can enable a development tenant
> first if you want the remote repository to initially contain the
> content from the development tenant.

Perform the following procedures in the order listed below.

####### Task 1. Enable the private remote repository for the production tenant

1.  In the production tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction is **Pull**.

2.  In the **Repository type** field, select **Private**, and save the
    settings.

3.  Define the Git settings using HTTPS or SSH.

- > **Note**

  - > For repository vendors that use tokens, enter the token type in
    > the **username** field and the token in the **password** field.
    > Verify details with your vendor.

  <!-- -->

  - > If your private Git remote repository uses personal access tokens
    > instead of usernames and passwords, enter the token type in the
    > **username** field and the access token in the **password** field.
    > For example, if you use an OAuth2 token, enter `oauth2` in the
    > **username** field.

    > For Github, enter your username in the **username** field.

  <!-- -->

  - > If using SSH, RSA or ed25519 algorithm private keys are supported.
    > If your SSH connection uses a port other than port 22 (the default
    > SSH port), you must include the SSH string and port number in the
    > **Repository URL** field. In the following example, we use port
    > 20017:

  <!-- -->

  - > `ssh://git@content.demisto.com:20017/~/my-project.git`

  a.  Select the active branch on which you will be working.

  b.  In the **Advanced** section, the engine is set by default. You can
      change the engine by selecting from the list of available engines.

  - > **Note**

    > You can\'t add an engine that has been added to a Load-Balancing
    > Group.

####### Task 2. Enable the private remote repository in the development tenants.

Once enabled, the first development tenant automatically becomes the
push tenant. For more details about push and pull tenants, see [Cortex
development tenant](#UUIDcd0108ce11b11a2c747b1c6b4ab07d62).

1.  In the development tenant, go to Settings \> Configurations \>
    General \> Remote Repository Settings and toggle the
    **Content repository** slider to enable the remote repository.

- When set to **On**, the sync direction for the first development
  tenant is **Push**. The sync direction for any additional development
  tenants is **Pull**.

2.  In the **Repository type** field, select **Private**.

3.  Define the GitHub settings using HTTPS or SSH.

- > **Note**

  - > If your private Git remote repository uses personal access tokens
    > instead of usernames and passwords, enter the access token in the
    > password field and leave the username field blank.

  - > For repository vendors that use tokens, the token type is entered
    > in the username field and the token is entered in the password
    > field. Verify details with your vendor.

  - > If using SSH, only RSA private keys are supported. If your SSH
    > connection uses a port other than port 22 (the default SSH port),
    > you must include the SSH string and port number in the
    > **Repository URL** field. In the following example, we use port
    > 20017:

  <!-- -->

  - > `ssh://git@content.demisto.com:20017/~/my-project.git`

  a.  Select the active branch on which you will be working.

  b.  In the **Advanced** section, add any engines you want to connect.

4.  Select which content to keep and which to overwrite. If there are
    any discrepancies between the development tenant and remote
    repository (which in this example initially contains the production
    tenant content after it is enabled), the
    **Specified repository is not empty** window opens. Options are:

    - **Existing content on your tenant**: Keeps the existing content on
      your tenant and replaces the content on the specified repository.
      Cortex XSIAM checks if any other tenants are using the remote
      repository. If yes, this option is disabled. In this example, the
      remote repository was already enabled in the production tenant, so
      the remote repository holds production content. If you want to
      keep the content on the development tenant:

      1.  Disable the remote repository in any additional enabled
          tenants. In this case, for the first development tenant, only
          the production tenant must be disabled.

      2.  Select **Existing content on your tenant** for this tenant.

      3.  Complete synchronization.

      4.  Re-enable the remote repository in any additional tenants and
          select **Existing content on the specified repository** in
          each additional tenant.

    - **Existing content on the specified repository**: Deletes the
      existing content on your tenant and replaces it with content from
      the specified repository.

5.  Click **Continue**.

#### Push and pull content

**Push content from the development tenant**

When content you develop in the development tenant is ready to be
available as a content update in the production tenant, you must push
the changes from the development tenant.

**Considerations for pushing content**

- Do not manually export content from the development tenant to import
  to the production tenant. Use only the procedures outlined in the
  documentation to ensure that your content is properly updated in the
  production tenant.

- We do not recommend pushing content from a development tenant to a
  production tenant if they have different versions. This helps avoid
  compatibility conflicts, versioning errors, and unintended behavior in
  the production environment.

**Development and production environments in different deployment
phases**

Separating your development and production environments into different
deployment phases enables testing an upgrade version in the development
environment before upgrading the production environment. Since new
features available in the upgrade version may not function in the
pre-upgrade environment, Cortex XSIAM provides warning messages and
visual indicators to alert users about incompatible items between
development and production environments, and collapsible release notes
in the list of changes.

**How to push content from the development tenant**

On each page you can decide whether to include or exclude items, which
prevents them from being pushed to production, on a temporary or
permanent basis. You can only exclude individual content items, not
content packs.

1.  In the development tenant, go to Settings \> Configurations \>
    Remote Repository Content \> User-Defined Content.

2.  Under the **Included for Prod** tab, search for the items you want
    to push. The results are displayed in a table according to:

    - **NAME**: The name of the content item.

    - **TYPE**: The content type, for example playbook, script, issue
      layout, and issue field.

    - **STATUS**: The date the content item was created.

    - **MESSAGE**: Additional details about the content item that were
      added by the content owner.

    - **BY**: The content item owner.

3.  Select the items you want to push to production, and click
    **Push to Prod**.

4.  If the items have dependencies, review the contents and click
    **Push**.

- Sometimes you may not want to push all content, content pack
  dependencies, etc. For example, when a user makes a change in a
  playbook that includes a script dependency to which another user is
  adding a feature, and the change does not require the new feature
  (version) of the script, you can push the playbook without the new
  script.

5.  In the dialog box, add an optional message and click **Push**.

6.  Pull the content into the production tenant.

**Pull content into the production tenant**

After you push content from the development tenant, the navigation bar
in the production tenant will notify
**Remote Repository Content Available**. In case of conflicts, you have
the choice whether to keep local content or delete and replace.

1.  If you click **Remote Repository Content Available** in the
    navigation bar, the **Content update available** window opens with a
    list of content available for installation, including content packs
    and content items.

2.  Click **Check for new content** or **Install content**.

3.  If conflicts appear, click **Resolve conflicts**.

4.  In the **Action** column, select one of the following:

    - **Skip**: Keeps the local content in your production environment.

    - **Replace**: Deletes the local content and installs the content
      from the content repository.

5.  Click **Continue** to install the content.

#### Remote repository troubleshooting

The following scenarios can occur when managing the remote repository.

**Pointing to a non-empty branch when enabling a tenant**

If you configure a tenant to use a remote repository, you have two
options:

- Overwrite all content in the tenant with content from the repository.

- Overwrite all content in the remote repository with content from the
  tenant. 

<!-- -->

- To overwrite the remote repository with content from the tenant, you
  must use an empty branch. If the branch is not empty, you will get an
  error message prompting you to select an empty branch. Alternatively,
  you can select the first option and overwrite all content in the
  tenant with the content from the remote repository.

**Switching between remote repository types**

If you switch between built-in and private remote repository types, you
get a warning that switching between repository types may result in the
loss of all version history.

To keep your content history, select **Existing content on your tenant**
to overwrite all content in the remote repository with content from your
tenant.

### Manage user roles and access management

> **Prerequisite**
>
> Managing users, roles, scopes, user groups, authentication settings in
> Cortex XSIAM Access Management requires **View/Edit** RBAC permissions
> for **Access Management** (under **Configurations**). Account Admin
> and Instance Administrator roles are granted this permission by
> default. For more information, see [Predefined user
> roles](#UUIDc0966cb32b3c88e214d33131de93fa8a).

Access management enables you to control who can access the different
parts of your organization\'s resources. It ensures only authorized
users can interact with sensitive data.

Cortex XSIAM uses a combination of Role-Based Access Control (RBAC) and
Scope-Based Access Control (SBAC) to ensure scalability and granular
control.

What is the difference between RBAC and SBAC?

RBAC assigns permissions based on a user\'s organizational role, such as
Investigator or Responder, establishing a clear hierarchy and set of
capabilities for each role and simplifying management by linking access
to job functions. RBAC does this by helping to manage access to Cortex
XSIAM components and Cortex Query Language (XQL) datasets, so that
users, based on their roles, are granted minimal access required to
accomplish their tasks.

SBAC refines RBAC by granting access only to the relevant data that the
user requires for their designated role. Users with
**Access Management** permission apply scopes to limit the data and
content that users can be granted access to in Cortex XSIAM, which are
divided into different scoping areas. The scoping areas include Assets,
Cases and Issues, and Endpoints, which can be applied as relevant to the
enforcement area or entity.

For example, an Investigator role might have access to asset information
based on the RBAC permissions, but SBAC granular scoping could limit
that investigator\'s view and control to only assets within a particular
scoping area. This hybrid approach ensures scalability and granular
control, significantly strengthening system security.

Understanding more about access management concepts

You can manage access for users, and create and assign user roles and
user groups for a specific tenant. When Single Sign-On (SSO) is enabled,
you can manage SSO for users.

**Users**

You can manage access permissions and activities for users allocated to
a specific Customer Support Portal account and tenant. All users must
belong to a user group or have an assigned role.

**User roles**

User roles enable you to define the type of access and actions a user
can perform. User roles are assigned to users, user groups, or API keys.

> **Note**
>
> For more information on assigning user roles when generating an API
> key, see [Manage API keys](#UUID53429804098d70e4f8c0ac853b973a2b).

Predefined user roles

Cortex XSIAM provides predefined built-in user roles that provide
specific access rights that cannot be modified. You can also create
custom, editable user roles. To view the predefined permissions for each
default role, go to Settings \> Configurations \> Access Management \>
Roles.

Dataset access permissions

You can also set dataset access permissions using user roles or set
specific permissions using role-based access control (RBAC). Configuring
administrative access depends on the security requirements of your
organization. Dataset permissions control dataset access for all
components, while RBAC controls access to a specific component. By
default, dataset access management is disabled, and users have access to
all datasets. If you enable dataset access management, you must
configure access permissions for each dataset type, and for each user
role. When a dataset component is enabled for a particular role, the
Issues and Cases pages include information about datasets. For more
information on how to set dataset access permissions, see [Manage user
roles](#UUID751d26ed9390ddddd4f6bb1f20db3a1d).

> **Note**
>
> Some features are license-dependent. Accordingly, users may not see a
> specific feature if the feature is not supported by the license type
> or if they do not have access based on their assigned role or scope.

**User groups and scoping areas**

You can use user groups to streamline configuration activities by
grouping together users whose access permission requirements are
similar. Import user groups from Active Directory, or create them from
scratch in Cortex XSIAM.

Users with **Access Management** permission can further restrict access
of these user groups, specifically for the designated role and list of
users configured in the user group by granting access only to the
relevant data that the user requires for their designated role. This is
performed by applying scopes to limit the data and content that users
can be granted access to in Cortex XSIAM, which are divided into
different scoping areas. The scoping areas include Assets, Cases and
Issues, and Endpoints, which can be applied as relevant to the
enforcement area or entity. This enables you to adhere to your
company\'s security policies of limiting user access by specifying, for
example, which groups of assets users can access and what actions they
can perform.

> **Note**
>
> For features where scoping is not applicable, Role-Based Access
> Control (RBAC) is used and can be configured when managing user roles.
> For more information, see [Manage user
> roles](#UUID751d26ed9390ddddd4f6bb1f20db3a1d).

**Single Sign-On**

Manage your SSO integration with the Security Assertion Markup Language
(SAML) 2.0 standard to securely authenticate system users across
enterprise-wide applications and websites, with one set of credentials.
This configuration allows system users to authenticate using your
organization\'s Identity Provider (IdP), such as Okta or PingOne. You
can integrate any IdP with Cortex XSIAM supported by SAML 2.0.

SSO with SAML 2.0 configuration activities are dependent on your
organization's IdP. Some of the field values need to be obtained from
your organization's IdP, and some values need to be added to your
organization's IdP. It is your responsibility to understand how to
access your organization's IdP to provide these fields, and to add any
fields from Cortex XSIAM to your IdP.

After SSO configuration is complete, when you sign in as an SSO user,
the Cortex XSIAM permissions granted to you after logging in, either
from the group mapping or from the default role configuration, are
effective throughout the entire session for the defined maximum session
length. Maximum session length is defined in your Cortex XSIAM Session
Security Settings. This applies even if the default role configuration
is updated, or the group membership settings were changed.

#### Manage user roles

> **Prerequisite**
>
> Managing user roles in Cortex XSIAM Access Management requires
> **View/Edit** RBAC permissions for **Access Management** (under
> **Configurations**). Account Admin and Instance Administrator roles
> are granted this permission by default. For more information, see
> [Predefined user roles](#UUIDc0966cb32b3c88e214d33131de93fa8a).

Review the following topics:

- [Assign user roles and groups](#UUIDc0966cb32b3c88e214d33131de93fa8a)

- [Manage user roles and access
  management](#UUIDe2101b004c635051f5a3eda9ac39aa5e)

Manage user roles that are assigned to Cortex XSIAM users, user groups,
or API keys. User roles enable you to define the type of access and
actions a user can perform.

You can only set dataset access permissions from a user role in Cortex
XSIAM **Access Management** for the tenant. When creating user roles
from the Cortex Gateway, these settings are disabled. By default,
dataset access management is disabled, and users have access to all
datasets. If you enable dataset access management, you must configure
access permissions for each dataset type, and for each user role. When a
dataset component is enabled for a particular role, the Issues and Cases
pages include information about datasets.

##### Create user role

1.  Select Settings \> Configurations \> Access Management \> Roles.

2.  Click **New Role**.

3.  Under **Role Name**, enter a name for the user role.

4.  (Optional) Under **Description**, enter a description for the user
    role.

5.  Under **Components**, expand each list and select the permissions
    for each of the components.

6.  Under **Datasets (Disabled)**, you have two options for setting the
    Cortex Query Language (XQL) dataset access permissions for the user
    role:

    - Set the user role with access to all XQL datasets by leaving the
      dataset access management as disabled (default).

    - Set the user role with limited access to certain XQL datasets by
      selecting the **Enable dataset access management** toggle and
      selecting the datasets under the different dataset category
      headings.

7.  Click **Save**.

##### Edit user role

1.  Select Settings \> Configurations \> Access Management \> Roles.

2.  Right-click the relevant user role, and select **Edit Role**.

3.  (Optional) Under **Role Name**, modify the name for the user role.

4.  (Optional) Under **Description**, enter a description for the user
    role or modify the current description.

5.  Under **Components**, expand each list and select the permissions
    for each of the components.

6.  Under **Datasets**, you have two options for setting the Cortex
    Query Language (XQL) dataset access permissions for the user role:

    - Set the user role with access to all XQL datasets by disabling the
      **Enable dataset access management** toggle.

    - Set the user role with limited access to certain XQL datasets by
      selecting the **Enable dataset access management** toggle and
      selecting the datasets under the different dataset category
      headings.

7.  Click **Save**.

##### Create new role based on an existing role

1.  Select Settings \> Configurations \> Access Management \> Roles.

2.  Right-click the relevant user role, and select **Save As New Role**.

3.  (Optional) Under **Role Name**, modify the name for the user role.

4.  (Optional) Under **Description**, enter a description for the user
    role or modify the current description.

5.  Under **Components**, expand each list and select the permissions
    for each of the components.

6.  Under **Datasets**, you have two options for setting the Cortex
    Query Language (XQL) dataset access permissions for the user role:

    - Set the user role with access to all XQL datasets by disabling the
      **Enable dataset access management** toggle.

    - Set the user role with limited access to certain XQL datasets by
      selecting the **Enable dataset access management** toggle and
      selecting the datasets under the different dataset category
      headings.

7.  Click **Save**.

#### Manage user access

> **Prerequisite**
>
> Managing users, roles, scopes, user groups, authentication settings in
> Cortex XSIAM Access Management requires **View/Edit** RBAC permissions
> for **Access Management** (under **Configurations**). Account Admin
> and Instance Administrator roles are granted this permission by
> default. For more information, see [Predefined user
> roles](#UUIDc0966cb32b3c88e214d33131de93fa8a).

Review the following topics:

- [Assign user roles and groups](#UUIDc0966cb32b3c88e214d33131de93fa8a)

- [Manage user roles and access
  management](#UUIDe2101b004c635051f5a3eda9ac39aa5e)

- [Manage user scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8)

Manage access permissions for Cortex XSIAM users.

##### Edit user permissions

Update a user\'s role and scope, add a user to a user group, and view
permissions based on the role, scope, and user groups assigned to the
user.

You can configure granular scoping for Scope-Based Access Control (SBAC)
by granting access only to the relevant data that the user requires for
their designated role. Administrators apply scopes to limit the data and
content that users can be granted access to in Cortex XSIAM, which are
divided into different scoping areas. The scoping areas include Assets,
Cases and Issues, and Endpoints, which can be applied as relevant to the
enforcement area or entity. For more information, see [Manage user
scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

> **Note**
>
> You can only reduce the permissions of an Account Admin user via
> Cortex Gateway.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Edit User Permissions**.

- > **Tip**

  > To apply the same settings to multiple users, select them, and then
  > right-click and select **Edit User Permissions**.

3.  In the **Role** tab, under **Role**, select the default or custom
    role.

4.  (Optional) Under **User Groups**, add the user to a group.

5.  (Optional) Under **Show Accumulated Permissions**:

    a.  Do one of the following:

        - Select all to view the combined permissions for every role and
          user group assigned to the user.

        - Select a specific role assigned to the user to view the
          available permissions for that role.

    b.  Under **Components**, expand each list to view the permissions
        to the various Cortex XSIAM components.

    c.  Under **Datasets**, there are two possibilities for viewing a
        user\'s dataset access permissions:

        - When dataset access management is enabled and the user has
          access to certain Cortex Query Language (XQL) datasets, the
          datasets are listed.

        - When dataset access management is disabled and users have
          access to all XQL datasets, the text
          **No dataset has been selected** is displayed.

- > **Note**

  > User permissions for components and datasets are based on the access
  > permissions set in the user role. For more information on editing
  > these user role permissions, see [Manage user
  > roles](#UUID751d26ed9390ddddd4f6bb1f20db3a1d).

6.  (Optional) You can configure granular scoping:

    a.  Click the **Scope** tab.

    b.  Under **Scope Definition**, expand the scoping areas that you
        want to grant the user role access to in the tenant by clicking
        the chevron icon (**\>**) beside the scoping area title, and
        make any changes required. The following table explains the
        options available to configure:

    - > **Important**

      > Before configuring, ensure that you review
      > **Understand scoping** in the [Manage user
      > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8) section.

+-----------------------------------+-------------------------------------------------+
| Scoping Area                      | Granular Scoping Configurations                 |
+===================================+=================================================+
| Assets                            | The scoping of assets also affects the scoping  |
|                                   | of cases, issues, and findings. Set the         |
|                                   | **Scope** by selecting one of the following:    |
|                                   |                                                 |
|                                   | - **No assets**: No asset is accessible.        |
|                                   |                                                 |
|                                   | - **All assets**: Defines access to all assets. |
|                                   |                                                 |
|                                   | - **Select asset groups**: Defines access to    |
|                                   |   the specific assets associated with the Asset |
|                                   |   Groups selected, and to view all their        |
|                                   |   related cases, issues, and findings for these |
|                                   |   specific assets and Asset Groups. Under       |
|                                   |   **Select asset groups**, define the specific  |
|                                   |   asset groups that you want to grant access.   |
|                                   |   Only the asset attributes listed in [Manage   |
|                                   |   user                                          |
|                                   |   scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8) |
|                                   |   (under Understand scoping \> Scoping Areas \> |
|                                   |   Assets) can be used for access scoping here.  |
+-----------------------------------+-------------------------------------------------+
| Cases and Issues                  | Set the **Scope** by selecting one of the       |
|                                   | following:                                      |
|                                   |                                                 |
|                                   | - **No cases and issues**: Defines access to no |
|                                   |   cases and issues.                             |
|                                   |                                                 |
|                                   | - **All cases and issues**: Defines access to   |
|                                   |   all cases and issues. Users can view cases or |
|                                   |   issues referencing assets within their scope. |
|                                   |   Use the **Assets** section to define which    |
|                                   |   assets are in scope.                          |
|                                   |                                                 |
|                                   | - **Select domains**: Defines access to the     |
|                                   |   domains selected with the ability to view     |
|                                   |   their related cases and issues. Under         |
|                                   |   **Select domains**, define the specific       |
|                                   |   domains that you want to grant access.        |
|                                   |                                                 |
|                                   | <!-- -->                                        |
|                                   |                                                 |
|                                   | - Users can view cases or issues referencing    |
|                                   |   assets with their scope. Use the **Assets**   |
|                                   |   section to define which assets are in scope.  |
+-----------------------------------+-------------------------------------------------+
| Endpoints                         | Set the **Scope** by selecting one of the       |
|                                   | following:                                      |
|                                   |                                                 |
|                                   | - **No endpoints**: Defines access to no        |
|                                   |   endpoints with no ability to view their       |
|                                   |   related agent management and enterprise       |
|                                   |   policies.                                     |
|                                   |                                                 |
|                                   | - **All endpoints**: Defines access to all      |
|                                   |   endpoints with the ability to view their      |
|                                   |   related agent management and enterprise       |
|                                   |   policies. This configuration can impact the   |
|                                   |   visibility of related **Security** domain     |
|                                   |   **Cases and Issues**, but will not affect     |
|                                   |   asset visibility.                             |
|                                   |                                                 |
|                                   | - **Select specific (at least one required)**:  |
|                                   |   Defines specific access to all endpoint       |
|                                   |   groups by selecting **Endpoint Groups** or    |
|                                   |   all endpoint tags by selecting                |
|                                   |   **Endpoint Tags** to view their related agent |
|                                   |   management and enterprise policies. This      |
|                                   |   configuration can impact the visibility of    |
|                                   |   related **Security** domain                   |
|                                   |   **Cases and Issues**, but will not affect     |
|                                   |   asset visibility.                             |
+-----------------------------------+-------------------------------------------------+

- > **Important**

  > By default, **Enable Scope Based Access Control** is disabled in
  > Settings \> Configurations \> General \> Server Settings, and
  > granular scoping is not enforced. Before enabling SBAC, we recommend
  > that an administrator or a user with **Access Management**
  > permissions first ensures that the users, user groups, and API Keys
  > defined in Cortex XSIAM are granted the required access by assigning
  > the relevant scopes. For more information, see [Manage user
  > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

7.  Click Save.

##### Import multiple users

Use a CSV file to import users who belong to a Customer Support Portal
account, and assign them roles that are defined in Cortex XSIAM. You can
use the CSV template provided in Cortex XSIAM, or prepare a CSV file
from scratch.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Click **Import Multiple User Roles**.

3.  Do one of the following:

    - To use the CSV template, click **Download example file**, and
      replace the example values with your values.

    - Prepare a CSV file from scratch. Make sure the file includes these
      columns:

      - User email: Email address of the user belonging to a Customer
        Support Portal account, for example,
        john.smith1@exampleCompany.com.

      - Role name: Name of the role that you want to assign to this
        user, for example, Privileged Responder. The role must already
        exist in Cortex XSIAM.

      - Is an account role: A boolean value that defines whether the
        user is designated with an Account Admin role in Cortex Gateway.
        Set the value to TRUE; otherwise, the value is set to FALSE
        (default).

4.  Locate the file and drag it to the dialog box.

5.  Click **Import**.

##### View user permissions

View all of the permissions currently assigned to a user.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Edit User Permissions**.

- > **Tip**

  > To apply the same settings to multiple users, select them, and then
  > right-click and select **Edit User Permissions**.

3.  In the **Role** tab, under **Show Accumulated Permissions**, do one
    of the following:

    - Select all to view the combined permissions for every role and
      user group assigned to the user.

    - Select a specific role assigned to the user to view the available
      permissions for that role.

4.  Under **Components**, expand each list to view the permissions to
    the various Cortex XSIAM components.

5.  Under **Datasets**, there are two possibilities for viewing a
    user\'s dataset access permissions:

    - When dataset access management is enabled and the user has access
      to certain Cortex Query Language (XQL) datasets, the datasets are
      listed.

    - When dataset access management is disabled and users have access
      to all XQL datasets, the text **No dataset has been selected** is
      displayed.

6.  To view the granular scoping configurations granted to the user
    role, click the **Scope** tab, and under **Scope Definition**,
    expand the scoping areas to view the settings by clicking the
    chevron icon (**\>**) beside the scoping area title. The scoping
    areas include - Assets, Cases and Issues, and Endpoints.

##### Hide user

There might be instances where you want to hide a user from the list of
users, for example, a user that has a Customer Support Portal Super User
role but isn\'t active on your Cortex XSIAM tenant. After you hide a
user, they will no longer be displayed in the list of users when
**Show User Subset** is selected on the **Users** page.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Hide User**.

##### Add user to a user group

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Edit User Permissions**.

- > **Tip**

  > To apply the same settings to multiple users, select them, and then
  > right-click and select **Edit User Permissions**.

3.  Under **User Groups**, add the user to a group.

4.  Click **Save**.

##### Deactivate user

You cannot deactivate a user who has an Account Admin role.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Deactivate User**.

3.  Click **Deactivate**.

##### Remove role assigned to user

You cannot remove a user who has an Account Admin role.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Remove User Role**.

3.  Click **Remove**.

##### User access reference information

The following is a list of common fields on the **Users** page:

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Show User Subset                  | Displays all users except for     |
|                                   | hidden users.                     |
+-----------------------------------+-----------------------------------+
| User Type                         | Indicates whether a user was      |
|                                   | defined in Cortex XSIAM using     |
|                                   | the Customer Support Portal, SSO  |
|                                   | (single sign-on) using your       |
|                                   | organization's IdP, or            |
|                                   | both Customer Support Portal/SSO. |
+-----------------------------------+-----------------------------------+
| Direct XDR Role                   | Name of the role specifically     |
|                                   | assigned to a user. When a user   |
|                                   | does not have any Cortex          |
|                                   | XSIAM access permissions assigned |
|                                   | specifically to them, the field   |
|                                   | displays **No-Role**.             |
+-----------------------------------+-----------------------------------+
| Groups                            | Lists the groups to which a user  |
|                                   | belongs. Any group that was       |
|                                   | imported from Active Directory    |
|                                   | displays **AD** beside the group  |
|                                   | name.                             |
|                                   |                                   |
|                                   | If a user group has scoping       |
|                                   | permissions, the users in the     |
|                                   | group are granted permissions     |
|                                   | according to the user group       |
|                                   | settings, even if the user does   |
|                                   | not have configured scope         |
|                                   | settings.                         |
+-----------------------------------+-----------------------------------+
| Group Roles                       | Lists the group roles based on    |
|                                   | the groups to which a user        |
|                                   | belongs. Hovering over the group  |
|                                   | role displays the group           |
|                                   | associated with this role.        |
+-----------------------------------+-----------------------------------+
| Scope                             | Lists a summary of the granular   |
|                                   | scoping configured for the user.  |
+-----------------------------------+-----------------------------------+
| Groups Scope                      | Lists a summary of the granular   |
|                                   | scoping configured in the user    |
|                                   | groups that the user belongs to   |
+-----------------------------------+-----------------------------------+

#### Manage user scope

> **Prerequisite**

- > Configuring user scopes in Cortex XSIAM Access Management requires
  > **View/Edit** RBAC permissions for **Access Management** (under
  > **Configurations**). Account Admin and Instance Administrator roles
  > are granted this permission by default. For more information, see
  > [Predefined user roles](#UUIDc0966cb32b3c88e214d33131de93fa8a).

- > By default, **Enable Scope Based Access Control** is disabled in
  > Settings \> Configurations \> General \> Server Settings, and
  > granular scoping is not enforced. Before enabling SBAC, we recommend
  > that you first ensure that the users, user groups, and API Keys
  > defined in Cortex XSIAM are granted the required access by assigning
  > the relevant scopes.

Review the following topics:

- [Assign user roles and groups](#UUIDc0966cb32b3c88e214d33131de93fa8a)

- [Manage user roles and access
  management](#UUIDe2101b004c635051f5a3eda9ac39aa5e)

##### What is SBAC?

Cortex XSIAM enables you to use Scope-Based Access Control (SBAC) in
combination with Role-Based Access Control (RBAC) to define precise
access controls according to your organization\'s security policies.
While RBAC defines what a role can access and the actions that can be
performed, SBAC determines the specific data and content displayed when
accessing these areas and performing those actions.

Users with **Access Management** permission apply scopes to limit the
data and content that users can be granted access to in Cortex XSIAM,
which are divided into different scoping areas. The scoping areas
include Assets, Cases and Issues, and Endpoints, which can be applied as
relevant to the enforcement area or entity. For example, an Investigator
role might have access to asset information based on the RBAC
permissions, but the SBAC granular scoping configuration could limit
that investigator\'s view and control to only assets within a particular
scoping area. This hybrid approach ensures scalability and granular
control, significantly strengthening system security by ensuring only
authorized users are granting access to the relevant data that the user
requires for their designated role.

Granular scoping is configured in users, user groups, or API Keys
according to the designated user role. Users are granted granular
scoping access based on the user role assigned to them either in a user
group or directly.

##### Things to consider before configuring SBAC

Before you begin setting Scope-Based Access Control (SBAC) granular
scoping, consider the following information:

- SBAC is disabled by default, which means that users have access to all
  content and data in the areas they have access to according to the
  RBAC permissions defined in their role.

- To best address Cases that span across all scopes, we recommend that
  there always be designated users with full access to all cases,
  issues, assets, and findings.

- Policies and playbook execution can affect items outside the user's
  scope, even though scoped users can't view them. As a result, we
  recommend that the users who write policies be granted access to all
  relevant policy assets, so they can review the affects of the
  policies.

- Some areas and features in Cortex XSIAM do not comply with SBAC. In
  these cases, use RBAC permissions to restrict access. For more
  information, see [Functional areas that respect and don\'t respect
  SBAC](#X4ee4ab2532274603a4583101c66629668e0622d) and .

- Respecting SBAC has some performance overhead when opening the Cases,
  Issues, Findings, and Assets tables, which can take more time.

- In Reports, SBAC applies when a report is manually generated, not when
  it is accessed in any other way. Scheduled reports do not run in any
  user context and are not subject to SBAC.

- For users who upgraded from a previous version of Cortex XSIAM to the
  current version, see the [What\'s New in Cortex XSIAM 3.x
  Guide](https://docs-cortex.paloaltonetworks.com/r/Beta/Cortex-XSIAM/What-s-new-in-XSIAM-3.x/What-s-New-in-Cortex-XSIAM-3.x)
  for specific changes that you should know about.

##### Understand scoping

###### Scoping areas

User Groups, Users, and API Keys can be scoped according to the
following scoping areas:

- **Assets**: Provides access to the assets associated with asset
  groups, and enables you to access their related cases, issues, and
  findings. When using asset groups, you can limit access based only on
  this list of attributes: Asset Class, Category, Provider, Region,
  Organization, Realm, Kubernetes Cluster, Kubernetes Namespace, Code
  Repository, and Asset Tags.

  - When you create or edit an Asset Group, the changes are applied
    immediately to new assets and to existing assets that have been
    updated. Yet, it can take a few hours for the changes to appear on
    existing assets that have not been updated.

- **Cases and Issues**: Provides access to domains to view their related
  cases and issues.

- **Endpoints**: Applies SBAC scoping on an endpoint as an entity and
  provides access to **Endpoint Groups** and **Endpoint Tags** to view
  their related agent management and enterprise policies.

<!-- -->

- > **Note**

  > This configuration can impact the visibility of the related
  > **Security** domain in the **Cases and Issues** scope area, but with
  > not affect asset visibility.

###### Scoping Behaviors

- When applicable, all conditions must be met to apply the scope
  configuration. For example, an issue with an affected asset is
  accessible only if the asset is in scope and the issue\'s domain is in
  scope.

- SBAC allows viewing cases and issues with no affected assets or
  endpoints, or when at least one affected assets is in the user's
  scope. The user can see all affected assets, including those not in
  scope, but won\'t be able to see more details about the assets not in
  scope, including opening their card.

- Cases and Issues of deleted assets do not have affected assets and so
  are not affected by asset-led SBAC or Endpoints, and are only based on
  the Cases and Issues domain.

- SBAC allows viewing cases where at least one of its issue's domains is
  in the user's scope. The user can see all issues, including those not
  in scope, but won\'t be able to see more details about the issues not
  in scope, including opening their card.

- Behavior of cases and issues with affected endpoints depends on the
  **Endpoint Scoping mode**.

- XQL queries that use the `cases`, `issues`, `findings`, and
  `asset_inventory` datasets, respect only the **Assets** scoping area
  configurations.

##### Functional areas that respect and don\'t respect SBAC

It is important to review both the functional areas and features in
Cortex XSIAM that are respected and not fully respected so you can
decide what actions to take in your tenant.

###### Functional areas respected

Scope-Based Access Control (SBAC) applies to the following functional
areas in Cortex XSIAM:

+-----------------------+-----------------------+------------------------+
| Functional Area       | Description           | Related scoping area   |
+=======================+=======================+========================+
| Cases, Issues,        | View and manage       | - **Assets**           |
| Findings, and Assets  | cases, issues,        |                        |
| tables                | findings, and assets, | - **Cases and Issues** |
|                       | and take actions in   |                        |
|                       | these tables.         | - **Endpoints**        |
+-----------------------+-----------------------+------------------------+
| Dashboard and Reports | Scoping takes place   | - **Assets**           |
|                       | only on the           |                        |
|                       | following:            | - **Cases and Issues** |
|                       |                       |                        |
|                       | - XQL-related widgets | - **Endpoints**        |
|                       |   based on XQL        |                        |
|                       |   queries that use    |                        |
|                       |   the `cases`,        |                        |
|                       |   `issues`,           |                        |
|                       |   `findings`, and     |                        |
|                       |   `asset_inventory`   |                        |
|                       |   datasets, and       |                        |
|                       |   respect only the    |                        |
|                       |   **Assets** scoping  |                        |
|                       |   area                |                        |
|                       |   configurations.     |                        |
|                       |                       |                        |
|                       | - Agent-related       |                        |
|                       |   widgets.            |                        |
+-----------------------+-----------------------+------------------------+
| Public APIs           | Public APIs that      | - **Assets**           |
|                       | access Cases, Issues, |                        |
|                       | Findings, and Assets  | - **Cases and Issues** |
|                       | information respect   |                        |
|                       | Scope-Based Access    |                        |
|                       | Control (SBAC).       |                        |
+-----------------------+-----------------------+------------------------+
| Cortex Query Language | When using XQL with   | **Assets**             |
| (XQL)                 | `cases`, `issues`,    |                        |
|                       | `findings`, and       |                        |
|                       | `asset_inventory`     |                        |
|                       | datasets, keep in the |                        |
|                       | mind the following:   |                        |
|                       |                       |                        |
|                       | - XQL respects        |                        |
|                       |   asset-led SBAC when |                        |
|                       |   accessing these     |                        |
|                       |   datasets, including |                        |
|                       |   when using XQL      |                        |
|                       |   queries and XQL     |                        |
|                       |   widgets.            |                        |
|                       |                       |                        |
|                       | - XQL queries that    |                        |
|                       |   use these datasets, |                        |
|                       |   respect only the    |                        |
|                       |   **Assets** scoping  |                        |
|                       |   area                |                        |
|                       |   configurations.     |                        |
|                       |                       |                        |
|                       | <!-- -->              |                        |
|                       |                       |                        |
|                       | - > **Note**          |                        |
|                       |                       |                        |
|                       |   > For Cases and     |                        |
|                       |   > Issues domains, a |                        |
|                       |   > workaround is to  |                        |
|                       |   > create a Dataset  |                        |
|                       |   > View for each     |                        |
|                       |   > required          |                        |
|                       |   > combination of    |                        |
|                       |   > domains, and      |                        |
|                       |   > allow the         |                        |
|                       |   > relevant entity   |                        |
|                       |   > access only to    |                        |
|                       |   > this Dataset      |                        |
|                       |   > View, not to the  |                        |
|                       |   > underlying        |                        |
|                       |   > `cases` and       |                        |
|                       |   > `issues`          |                        |
|                       |   > datasets.         |                        |
+-----------------------+-----------------------+------------------------+
| Endpoint              | View endpoints and    | **Endpoints**          |
| Administration table  | take actions on       |                        |
|                       | endpoints.            |                        |
+-----------------------+-----------------------+------------------------+
| Policy Management     | Create and edit       | **Endpoints**          |
|                       | Prevention policies   |                        |
|                       | and profiles,         |                        |
|                       | Extension policies    |                        |
|                       | and profiles, and     |                        |
|                       | global and device     |                        |
|                       | Exceptions that are   |                        |
|                       | within the scope of   |                        |
|                       | the user.             |                        |
+-----------------------+-----------------------+------------------------+
| Action Center         | View and take actions | **Endpoints**          |
|                       | only on endpoints     |                        |
|                       | that are within the   |                        |
|                       | scope of the user.    |                        |
+-----------------------+-----------------------+------------------------+
| Identity Security     | View and manage       | - **Assets**           |
|                       | identity assets,      |                        |
|                       | permissions, and      | - **Cases and Issues** |
|                       | issues that are       |                        |
|                       | within the scope of   |                        |
|                       | the user.             |                        |
+-----------------------+-----------------------+------------------------+

> **Important**
>
> Some areas and features in Cortex XSIAM do not respect SBAC. In these
> cases, use RBAC permissions to restrict access.

###### SBAC not fully respected functional areas

Ensure that you review the points below that explain the main functional
areas with limitations with respecting SBAC, so you can decide how to
handle this in your tenant. A suggested action is provided when
applicable.

- Access to datasets: Access to the `alerts` and `incidents` datasets do
  not support SBAC.

<!-- -->

- Suggested action: Consider limiting users from accessing these
  datasets by excluding access to the datasets mentioned above using
  Dataset Views, and only enable access to `cases` and `issues` datasets
  that respect SBAC.

<!-- -->

- Graph Search: Graph Search does not support SBAC, It is currently a
  Beta feature and is only available in the tenant using a feature flag.

- Command Centers: Aggregative numbers in Command Centers can also sum
  up data, which is not in the user scope. When pivoting from Command
  Centers to the Cases, Issues, Findings, and Assets tables, these
  tables do respect SBAC.

<!-- -->

- Suggested action: We recommend limiting the users who access Command
  Centers and these users should be granted a broader scope. For all
  other users, disable access in RBAC settings (Dashboards & Reports \>
  Command Center Dashboards).

<!-- -->

- Host Insights

<!-- -->

- Suggested action: Disable access in RBAC settings (Investigation &
  Response \> Search \> Host Insights).

<!-- -->

- Timeline widget

<!-- -->

- Suggested action: As a workaround, you can disable access through RBAC
  permissions by disabling Dashboards (Dashboards & Reports \>
  Dashboards).

<!-- -->

- Notification Center

- Agent Installation widget: This widget not available for scoped users.

- Drop-downs of cases and issues domains: Drop-downs of these domains
  display all domains.

- KSPM dashboard: Users can access all information on the dashboard when
  their user access is scoped to view **All assets** or assigned to the
  Instance Administrator role. Otherwise, users with granular scoping
  set to **No assets** or **Select asset groups** will have limited
  access to the dashboard. For more information on the KSPM dashboard,
  see [Predefined dashboards](#UUIDf653abffde9e95ed7b64bdea77e15c6f).

##### How to configure granular scoping

Granular scoping is configured in users, user groups, or API keys, and
applied to the user roles assigned. Users are then granted granular
scoping access according to the user roles assigned to them in a user
group or directly. The instructions below explain how to configure
granular scoping according to Palo Alto Networks best practices.

Granular scoping is disabled and not enforced in Cortex XSIAM by
default. Before enabling SBAC, we recommend that an administrator or a
user with **Access Management** permissions first ensures that the
users, user groups, and API Keys defined in Cortex XSIAM are granted the
required access by assigning the relevant scopes. This user can then
assign a scoping area to a Cortex XSIAM user (non-administrator), so the
non-administrator user can manage only the specific scoping areas that
are predefined within that scope.

> **Note**
>
> Make sure to assign the required default granular scoping for users.
> This depends on the structure and divisions within your organization
> and the particular purpose of each organizational unit to which scoped
> users belong.

1.  Ensure that you have necessary administrator level permissions.

2.  Verify that the users, user groups, and API keys defined in Cortex
    XSIAM are assigned the relevant scopes.

    - To verify the granular scoping of a user, select Settings \>
      Configurations \> Access Management \> Users, right-click the user
      name, and select **Edit User Permissions**.

    - To verify the granular scoping of a user group, select Settings \>
      Configurations \> Access Management \> User Groups, right-click
      the user group, and select **Edit Group**.

    - To verify the granular scoping of an API key, select Settings \>
      Configurations \> Integrations \> API Keys, right-click the API
      key, and select **Edit**.

3.  In the **Scope** tab, expand the scoping areas to review the current
    granular scoping definitions by clicking the chevron icon (**\>**)
    beside the scoping area title, and make any changes required. The
    following table explains the options available to configure:

- > **Important**

  > Before configuring, ensure that you review the [Understand
  > scoping](#Xe6c2a44e6d69fdf485e619ec8c23b57fbb6002f) section.

+-----------------------------------+-------------------------------------------------+
| Scoping Area                      | Granular Scoping Configurations                 |
+===================================+=================================================+
| Assets                            | The scoping of assets also affects the scoping  |
|                                   | of cases, issues, and findings. Set the         |
|                                   | **Scope** by selecting one of the following:    |
|                                   |                                                 |
|                                   | - **No assets**: No asset is accessible.        |
|                                   |                                                 |
|                                   | - **All assets**: Defines access to all assets. |
|                                   |                                                 |
|                                   | - **Select asset groups**: Defines access to    |
|                                   |   the specific assets associated with the Asset |
|                                   |   Groups selected, and to view all their        |
|                                   |   related cases, issues, and findings for these |
|                                   |   specific assets and Asset Groups. Under       |
|                                   |   **Select asset groups**, define the specific  |
|                                   |   asset groups that you want to grant access.   |
|                                   |   Only the asset attributes listed in [Manage   |
|                                   |   user                                          |
|                                   |   scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8) |
|                                   |   (under Understand scoping \> Scoping Areas \> |
|                                   |   Assets) can be used for access scoping here.  |
+-----------------------------------+-------------------------------------------------+
| Cases and Issues                  | Set the **Scope** by selecting one of the       |
|                                   | following:                                      |
|                                   |                                                 |
|                                   | - **No cases and issues**: Defines access to no |
|                                   |   cases and issues.                             |
|                                   |                                                 |
|                                   | - **All cases and issues**: Defines access to   |
|                                   |   all cases and issues. Users can view cases or |
|                                   |   issues referencing assets within their scope. |
|                                   |   Use the **Assets** section to define which    |
|                                   |   assets are in scope.                          |
|                                   |                                                 |
|                                   | - **Select domains**: Defines access to the     |
|                                   |   domains selected with the ability to view     |
|                                   |   their related cases and issues. Under         |
|                                   |   **Select domains**, define the specific       |
|                                   |   domains that you want to grant access.        |
|                                   |                                                 |
|                                   | <!-- -->                                        |
|                                   |                                                 |
|                                   | - Users can view cases or issues referencing    |
|                                   |   assets with their scope. Use the **Assets**   |
|                                   |   section to define which assets are in scope.  |
+-----------------------------------+-------------------------------------------------+
| Endpoints                         | Set the **Scope** by selecting one of the       |
|                                   | following:                                      |
|                                   |                                                 |
|                                   | - **No endpoints**: Defines access to no        |
|                                   |   endpoints with no ability to view their       |
|                                   |   related agent management and enterprise       |
|                                   |   policies.                                     |
|                                   |                                                 |
|                                   | - **All endpoints**: Defines access to all      |
|                                   |   endpoints with the ability to view their      |
|                                   |   related agent management and enterprise       |
|                                   |   policies. This configuration can impact the   |
|                                   |   visibility of related **Security** domain     |
|                                   |   **Cases and Issues**, but will not affect     |
|                                   |   asset visibility.                             |
|                                   |                                                 |
|                                   | - **Select specific (at least one required)**:  |
|                                   |   Defines specific access to all endpoint       |
|                                   |   groups by selecting **Endpoint Groups** or    |
|                                   |   all endpoint tags by selecting                |
|                                   |   **Endpoint Tags** to view their related agent |
|                                   |   management and enterprise policies. This      |
|                                   |   configuration can impact the visibility of    |
|                                   |   related **Security** domain                   |
|                                   |   **Cases and Issues**, but will not affect     |
|                                   |   asset visibility.                             |
+-----------------------------------+-------------------------------------------------+

4.  Click **Save**.

5.  Repeat **steps 2 to 4** until you have configured all users, user
    groups, and API keys with the correct granular scoping access.

6.  Enable granular scoping in Cortex XSIAM.

    a.  Select Settings \> Configurations \> General \> Server Settings,
        and select the **Enable Scope Based Access Control** toggle.

    b.  (Optional) You can select the **Endpoint Scoping Mode**, which
        is defined per tenant:

        - **Permissive:** Enables users with at least one scope tag to
          access the relevant entity with that same tag.

        - **Restrictive:** Users must have all the scoped tags that are
          tagged within the relevant entity of the system.

    c.  Click **Save**.

- When you are finished, all the users in Cortex XSIAM are now able to
  use Cortex XSIAM only within the granular scoping granted according to
  their assigned user roles.

### Dashboards and reports

Dashboards consist of visualized data powered by fully customizable
widgets, which enable you to analyze data from inside or outside Cortex
XSIAM, in different formats such as graphs, pie charts, or text. Cortex
XSIAM displays the predefined dashboards when you log in. You can also
create custom dashboards that are based on the predefined dashboards, or
built to your specifications, and you can save any of your dashboards as
reports.

Cortex XSIAM also provides Command Center dashboards that display
interactive overviews of your system activity, with drilldowns to
additional dashboards and associated pages.

From the **Dashboard & Reports** menu, you can view and manage your
dashboards and reports from the dashboard and incidents table, and view
alert exclusions.

- **Dashboard:** Provides dashboards that you can use to view high-level
  statistics about your agents and incidents.

- **Reports:** View all the reports that Cortex XSIAM administrators
  have run.

- **Customize:** Create and manage a new dashboard and reports.

  - **Dashboards Manager:** Add new dashboards with customized widgets
    to surface the statistics that matter to you most.

  - **Reports Templates:** Build reports using pre-defined templates, or
    customize a report. Reports can be generated on-demand scheduled.

  - **Widget Library:** Search, view, edit, and create widgets based on
    predefined widgets and user-created custom widgets.

