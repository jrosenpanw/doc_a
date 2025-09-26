## Monitor dashboards and reports

### About dashboards

Dashboards offer graphical overviews of your tenant\'s activities,
enabling you to effectively monitor your cases and overall activity in
your environment. Each dashboard comprises widgets that summarize
information about your endpoint in a graphical or tabular format.

![](media/rId1151.png){width="4.083333333333333in"
height="2.1947911198600174in"}

When you sign in to Cortex XSIAM your default dashboard is displayed. To
change the displayed dashboard, in the dashboard header choose from the
list of predefined and custom dashboards. You can also manage all of
your dashboards from the **Dashboard Manager**.

On each dashboard, you can you can see the selected **Time Range** on
the right side of the header. To see the last updated status for each
widget, hover over a widget and if required, **Refresh** the data. You
can also select widget specific time frames from the menu on an XQL
widget. If you select a different time frame for a widget, a clock icon
is displayed.

Predefined dashboard filters are displayed in the dashboard header. A
filter icon on a widget indicates that the widget data is filtered.
Hover over the icon to see details of the filters applied. A filter icon
on a widget indicates that the widget data is filtered. Hover over the
icon to see details of the filters applied.

Click the dashboard menu to see additional actions, including the option
to save the dashboard as a report template, set it as your default
dashboard, and pause automatic dashboard refresh.

#### Types of dashboards

Cortex XSIAM provides the following types of dashboards:

- Command Center dashboards

<!-- -->

- Command Center dashboards provide instant visibility into your
  security operations, with drilldowns to additional dashboards and
  associated pages. For more information, see [Command Center
  dashboards](#UUIDe471dedd394748391919f80b8a68b582).

<!-- -->

- Predefined dashboards

<!-- -->

- Predefined dashboards are configured for different system setups and
  use cases, and to assist SOC analysts in their investigations. You can
  create reports and custom dashboards that are based on predefined
  dashboards. For more information, see [Predefined
  dashboards](#UUIDf653abffde9e95ed7b64bdea77e15c6f).

<!-- -->

- Custom dashboards

<!-- -->

- Custom dashboards provide the flexibility to design dashboards that
  are built to your own specifications. You can base custom dashboards
  on the predefined dashboards or create a new dashboard from scratch,
  and save your custom dashboards as reports. For more information, see
  [/document/preview/1159518#UUID-c8552db8-9c43-cfc5-23e6-f1073c85aebd](/document/preview/1159518#UUID-c8552db8-9c43-cfc5-23e6-f1073c85aebd).

#### Manage your dashboards

You can see all of your predefined and custom dashboards in the
**Dashboard Manager**, and take the following actions:

- Create, edit, and delete custom dashboards

<!-- -->

- > **Note**

  > You cannot edit the predefined dashboards but you can create a new
  > dashboard that is based on a dashboard template. In addition,
  > private dashboards can only be viewed, edited, and deleted by the
  > dashboard creator.

<!-- -->

- Select your default dashboard

- Create a report template based on a dashboard

- Import and export dashboards

<!-- -->

- You can import and export dashboards in a JSON format, which enables
  you to transfer your configurations between environments for
  onboarding, migration, backup, and sharing. You can also bulk export
  and import multiple dashboards at a time.

  > **Note**

  - > Dashboards that are based on custom infrastructure cannot be
    > exported.

  - > If you import a dashboard template that already exists in the
    > system, the imported template will overwrite the existing
    > template. If you do not want to overwrite the existing template,
    > duplicate and rename the existing template before importing the
    > new template.

#### Command Center dashboards

The Command Center dashboards provide interactive overviews of your
Cortex XSIAM system status, including data ingestion metrics, case and
issue data, automations, and more.

From the Command Center dashboards, click on elements of interest to
drill down to additional dashboards and associated pages.

> **Note**

- > Access to the dashboards requires RBAC **View** permissions
  > for **Dashboards & Reports** and **Command Center Dashboards**.

- > The dashboards are available in dark mode only. They are not
  > editable, and you can\'t create dashboard templates or reports from
  > them.

- > Some of the dashboard's animations are not fully supported by the
  > Safari web browser. We recommend that you view the dashboard with an
  > alternative web browser.

##### Cortex Command Center

> **Note**
>
> The **Cortex Command Center** requires RBAC View permissions for
> **Dashboards**, **Command Center Dashboards**, and
> **Asset Inventory**.

The **Cortex Command Center** is a unified view for complete asset
visibility, providing full organizational visibility across your cloud
and enterprise environments. By combining cloud security data with SOC
insights, the **Cortex Command Center** offers a detailed view of cloud
and enterprise assets, including asset risk levels and active threats to
assets. This dashboard helps you gain key insights into your
environment, including:

- **A complete overview of your assets:** Understand asset distribution
  across your organization, with a comprehensive breakdown of assets by
  class, provider, and region.

- **Assets at risk due to posture issues:** Identify assets with open
  posture issues that require attention to prevent threats from
  occurring in your environment.

<!-- -->

- Posture issues are associated with risk management activities to
  detect and mitigate risks to assets in the environment before they
  occur in runtime, and improve resilience. For example,
  misconfigurations in cloud instances, over-permissive users, or the
  detection of secrets or shadow data.

<!-- -->

- **Assets with active runtime threats:** Identify assets with open
  security issues that require immediate attention.

<!-- -->

- Security issues are associated with case response activities for
  detecting, preventing, and blocking threats as they occur in runtime.
  For example, identification of malware in a file, a compromised
  endpoint, or a phishing attempt.

<!-- -->

- **Assets with active threats and posture issues:** Highlight assets
  with open security and posture issues. These are assets with active
  threats that might have already been exploited, and require immediate
  attention.

- **Data Ingestion in your environment:** See the total amount of
  ingested data in your environment over the last 24 hours, with a
  breakdown by data source. Click the widget to see a full breakdown on
  the **Data Ingestion** dashboard.

![](media/rId1157.png){width="0.19166666666666668in"
height="0.20833333333333334in"} Show me more

![](media/rId1160.gif){width="5.833333333333333in" height="3.28125in"}

When you access the **Cortex Command Center**, the dashboard displays a
view of all monitored assets. On the left side of the dashboard, you can
see the total number of monitored assets, and a breakdown by status. On
the right side, the radar provides a visual representation of your
assets. The data on this dashboard shows the current status of your
environment and is updated every 20 minutes. You can take the following
actions to investigate your assets:

- **Refine the displayed data:** Use the severity filters in the
  top-right corner. By default, assets with High and Critical issues are
  displayed. You can also change the radar view to display data by asset
  class, provider, or region, and drill down on assets by status: assets
  with active threats, assets at risk from posture issues, and assets
  with both active threats and posture issues.

<!-- -->

- Drill down further on an asset class, provider, or region by clicking
  on the radar to open a side view with a breakdown of the selected
  option.

<!-- -->

- **Identify unprotected assets:** Filter by asset class **Compute** to
  see the number of Compute assets that are being protected by the
  Cortex Agent. This information can help you to identify unprotected
  assets, and ensure complete coverage in your environment. Click on the
  number of agents to see more information on the **Agent Management**
  dashboard.

- **Investigate open issues for an asset type:** Click a group (such as
  Identity) to see the number of open issues for each asset status.
  Click on the number of issues to open the Issues page, filtered for
  the asset type and status.

- **See asset details:** On the radar, each dot represents a group of
  assets, color-coded by their collective status. Click a dot to view
  details about the assets in the group. Use the arrows to click through
  the assets, click See details to open the asset card for a specific
  asset or click **See All** to open the **Asset Inventory**, filtered
  to display all assets in the group.

**Limitations**

The **Cortex Command Center** currently has the following limitations:

- Only assets that are included in the **Asset Inventory** are displayed
  on the dashboard.

- In the region view, the location is based on cloud provider region and
  its data center location and therefore the map view shows only cloud
  assets.

- When you click **See All** assets in the **Asset Inventory**, the
  listed assets are limited to 1,000.

##### XSIAM Command Center

The **XSIAM Command Center** dashboard provides a dynamic overview of
your security operations processes, and supports drilldowns to
additional dashboards and dedicated pages. The dashboard gives a
visualization of the current status of your tenant and its activity
during the selected time frame. Click on any element to drill down to
dashboards or pages displaying data that is filtered by your selection.

![](media/rId1165.png){width="5.833333333333333in"
height="3.317707786526684in"}

The **XSIAM Command Center** includes incoming data, cases, and issues,
and key performance indicators. The following table describes each of
these sections:

+-----------------------------------+-------------------------------------+
| Section                           | Details                             |
+===================================+=====================================+
| Incoming data                     | - Number of connected Cortex XDR    |
|                                   |   agent endpoints providing EDR     |
|                                   |   data.                             |
|                                   |                                     |
|                                   | - Data source instances grouped by  |
|                                   |   integration and ordered by        |
|                                   |   ingestion volume. Integrations    |
|                                   |   shown in red indicate there is    |
|                                   |   currently an error.               |
|                                   |                                     |
|                                   | Click on any of these items to      |
|                                   | explore                             |
|                                   | your **Data Inventory**. Breakdowns |
|                                   | of data ingestion by data source,   |
|                                   | including ingestion rates, trends,  |
|                                   | and prevented events, are           |
|                                   | displayed.                          |
+-----------------------------------+-------------------------------------+
| Cases and issues                  | - The number of issues opened       |
|                                   |   during the time frame.            |
|                                   |                                     |
|                                   | - The number of cases that were     |
|                                   |   created in response to the        |
|                                   |   issues.                           |
|                                   |                                     |
|                                   | <!-- -->                            |
|                                   |                                     |
|                                   | - Cases are split into manual cases |
|                                   |   and automated cases, where        |
|                                   |   automated cases contain at least  |
|                                   |   one playbook. You can also see    |
|                                   |   the number of resolved cases and  |
|                                   |   open cases broken down by         |
|                                   |   severity.                         |
|                                   |                                     |
|                                   | Click on any of the case metrics to |
|                                   | open the **Cases Overview** ,       |
|                                   | showing a breakdown of your cases.  |
|                                   | You can also click on the           |
|                                   | concentric circle to see a live     |
|                                   | feed of Cortex XSIAM activity on    |
|                                   | the **Dynamic View**.               |
+-----------------------------------+-------------------------------------+
| Key performance indicators        | - The amount of data and events     |
|                                   |   ingested during the time frame    |
|                                   |   and the ingestion rate.           |
|                                   |                                     |
|                                   | - The number of currently open      |
|                                   |   cases broken down by severity.    |
|                                   |   This number represents all open   |
|                                   |   cases on the system, and is not   |
|                                   |   time frame specific.              |
|                                   |                                     |
|                                   | - The number of attacks prevented   |
|                                   |   by Cortex XSIAM during the time   |
|                                   |   frame.                            |
|                                   |                                     |
|                                   | Click on the key performance        |
|                                   | indicators to drill down to         |
|                                   | dedicated pages for further         |
|                                   | investigation.                      |
|                                   |                                     |
|                                   | The trend percentages for the key   |
|                                   | performance indicators are          |
|                                   | calculated by comparing the totals  |
|                                   | from the current time frame with    |
|                                   | the totals of the previous time     |
|                                   | frame. An arrow indicates whether   |
|                                   | the rates are rising or falling in  |
|                                   | comparison to the previous time     |
|                                   | frame\'s total.                     |
+-----------------------------------+-------------------------------------+

From the **XSIAM Command Center**, you can drill down to the following
dashboards:

###### Data Inventory

The **Data Inventory** provides a dynamic view of the data sources that
are ingesting data into Cortex XSIAM. You can see breakdowns of data
ingestion by data source, ingestion rates, trends, and prevented events.

You can access the dashboard from the **XSIAM Command Center** by
clicking a data source, the number of **Endpoints** or
**VM Brokers/XDRCs**. The **Data Inventory** includes incoming data
sources and key performance indicators. The following table describes
each of these sections:

+-----------------------------------+-----------------------------------+
| Section                           | Details                           |
+===================================+===================================+
| Data sources                      | Data sources are broken down into |
|                                   | categories. Depending on the      |
|                                   | selected data source, the         |
|                                   | dashboard opens the relevant      |
|                                   | category. You can expand a        |
|                                   | category to see details of        |
|                                   | individual data sources and hover |
|                                   | over a data source to see more    |
|                                   | details. You can also click on a  |
|                                   | data source to link to a drill    |
|                                   | down view, filtered by your       |
|                                   | selection:                        |
|                                   |                                   |
|                                   | - Connected endpoints             |
|                                   |                                   |
|                                   | - PANW integrations               |
|                                   |                                   |
|                                   | - 3rd party data sources          |
|                                   |                                   |
|                                   | <!-- -->                          |
|                                   |                                   |
|                                   | - Only registered Cortex XSOAR    |
|                                   |   data sources are displayed in   |
|                                   |   this view. To register a data   |
|                                   |   source, install the relevant    |
|                                   |   integration in the Marketplace. |
+-----------------------------------+-----------------------------------+
| Key performance indicators        | - **Event Ingestion** and         |
|                                   |   **Data Ingestion** display the  |
|                                   |   amount of data and events       |
|                                   |   ingested during the time frame  |
|                                   |   and the ingestion rate.         |
|                                   |                                   |
|                                   | <!-- -->                          |
|                                   |                                   |
|                                   | - The trend percentages for the   |
|                                   |   key performance indicators are  |
|                                   |   calculated by comparing the     |
|                                   |   totals from the current time    |
|                                   |   frame with the totals of the    |
|                                   |   previous time frame. An arrow   |
|                                   |   indicates whether the rates are |
|                                   |   rising or falling in comparison |
|                                   |   to the previous time frame\'s   |
|                                   |   total.                          |
|                                   |                                   |
|                                   | <!-- -->                          |
|                                   |                                   |
|                                   | - **Collection errors** displays  |
|                                   |   the number of collection errors |
|                                   |   that occurred in the time       |
|                                   |   frame. Collection errors occur  |
|                                   |   when integration instances that |
|                                   |   fetch data have an error        |
|                                   |   status.                         |
|                                   |                                   |
|                                   | Click on the key performance      |
|                                   | indicators to drilldown to        |
|                                   | dedicated pages for further       |
|                                   | investigation.                    |
+-----------------------------------+-----------------------------------+

###### Dynamic View

The **Dynamic View** provides an overview of Cortex XSIAM activity in
real-time. You can see the data sources that are sending data to Cortex
XSIAM, data sources with connection errors, playbooks being triggered,
and the issues and cases being created.

To access the **Dynamic View** click on the concentric circle in the
**XSIAM Command Center**. The **Dynamic View** includes the concentric
circle, the live feed, and the key performance indicators. The following
table describes each of these sections:

+-----------------------------------+-----------------------------------+
| Section                           | Details                           |
+===================================+===================================+
| Concentric circle                 | Shows an animation of Cortex      |
|                                   | XSIAM activity in real-time.      |
|                                   | Icons represent issues and cases. |
|                                   | Data sources are displayed on the |
|                                   | outside of the circle, and are    |
|                                   | color coordinated to represent    |
|                                   | their connection status. The      |
|                                   | center of the circle displays     |
|                                   | statistics about open cases,      |
|                                   | automatically resolved cases, and |
|                                   | manually resolved cases.          |
|                                   |                                   |
|                                   | Click on any of the elements to   |
|                                   | drilldown to dedicated pages for  |
|                                   | further investigation.            |
+-----------------------------------+-----------------------------------+
| Live feed                         | Reports the following types of    |
|                                   | activity on the tenant:           |
|                                   |                                   |
|                                   | - An issue is added to a case.    |
|                                   |                                   |
|                                   | - A case is created, resolved, or |
|                                   |   reopened.                       |
|                                   |                                   |
|                                   | - A playbook is triggered.        |
|                                   |                                   |
|                                   | - A data source ingested data.    |
|                                   |                                   |
|                                   | - A data source is in error       |
|                                   |   status.                         |
|                                   |                                   |
|                                   | Click on any of the live feed     |
|                                   | elements to link to dedicated     |
|                                   | pages that can assist you with    |
|                                   | your investigation.               |
+-----------------------------------+-----------------------------------+
| Key performance indicators        | Displays information about data   |
|                                   | ingested during the time frame,   |
|                                   | and the number of open cases. The |
|                                   | ingestion rate trend percentage   |
|                                   | is calculated by comparing the    |
|                                   | ingestion total of the current    |
|                                   | time frame with the ingestion     |
|                                   | total of the previous time frame. |
|                                   | An arrow indicates whether the    |
|                                   | rates are rising or falling in    |
|                                   | comparison to the previous time   |
|                                   | frame\'s total.                   |
|                                   |                                   |
|                                   | Click on the key performance      |
|                                   | indicators to drilldown to        |
|                                   | dedicated pages for further       |
|                                   | investigation.                    |
+-----------------------------------+-----------------------------------+

###### Cases Overview

The **Cases Overview** provides a breakdown of your cases, including
MITRE ATT&CK tactic details, automation suggestions, and top resolving
assignees. You can click different elements on the dashboard to link to
dedicated pages for further investigation.

You can access the **Cases Overview** from the **XSIAM Command Center**
by clicking on any of the case metrics. The **Cases Overview** displays
the following information:

  -----------------------------------------------------------------------
  Section                             Details
  ----------------------------------- -----------------------------------
  Automation suggestions              Displays the number of cases that
                                      could have been automated, and the
                                      number of playbook recommendations.

  Resolved cases                      Displays the number of resolved
                                      cases in the time frame, and
                                      provides a breakdown of top
                                      resolving assignees.

  Open cases                          Displays a breakdown of open cases
                                      by severity, and details of the
                                      MITRE ATT&CK tactics identified in
                                      the cases.

  Key performance indicators          Displays information about data
                                      ingested during the time frame, and
                                      the number of assets affected by
                                      the cases. The ingestion rate trend
                                      percentage is calculated by
                                      comparing the ingestion total of
                                      the current time frame with the
                                      ingestion total of the previous
                                      time frame. An arrow indicates
                                      whether the rates are rising or
                                      falling in comparison to the
                                      previous time frame\'s total.
  -----------------------------------------------------------------------

##### Cloud Detection and Response (CDR) Command Center

The Cloud Detection and Respond (CDR) Command Center dashboard provides
a dynamic overview of your cloud-based security operations. It includes
details about your cloud assets and projects, related cases, risks, and
vulnerabilities. From the dashboard, you can drill down to dedicated
views for further investigation into your platform.

![](media/rId1172.png){width="4.083333333333333in" height="3.5525in"}

The following table describes each section on the
**Cloud Detection and Respond (CDR) Command Center**:

+-----------------------------------+-----------------------------------+
| Section                           | Details                           |
+===================================+===================================+
| Accounts                          | Displays information about your   |
|                                   | cloud accounts, the total number  |
|                                   | of assets configured per account, |
|                                   | and the total number of cloud     |
|                                   | projects from your cloud          |
|                                   | accounts. Hover over the total    |
|                                   | number of assets to see a         |
|                                   | breakdown by category, and click  |
|                                   | on an account to drill down to    |
|                                   | the assets for the selected       |
|                                   | account.                          |
|                                   |                                   |
|                                   | Line colors represent the         |
|                                   | connectivity status of the        |
|                                   | assets. You can hover over the    |
|                                   | lines to see a breakdown of data  |
|                                   | ingestion or details of           |
|                                   | collection errors.                |
+-----------------------------------+-----------------------------------+
| Cases                             | Displays the total number of      |
|                                   | cases opened in the timeframe     |
|                                   | that are associated with your     |
|                                   | cloud assets, broken down by      |
|                                   | severity. Cases are broken down   |
|                                   | into automated and manual cases,  |
|                                   | where automated cases contain at  |
|                                   | least one playbook. You can also  |
|                                   | see the top nine open cases as    |
|                                   | ranked by SmartScore.             |
+-----------------------------------+-----------------------------------+
| Key performance indicators        | - Risks identified, including     |
|                                   |   attack paths, configurations,   |
|                                   |   and vulnerabilities.            |
|                                   |                                   |
|                                   | - Total number of assets          |
|                                   |   discovered in the cloud.        |
|                                   |                                   |
|                                   | - Cloud data ingested by your     |
|                                   |   cloud platforms in the          |
|                                   |   timeframe, including flow logs  |
|                                   |   and audit logs.                 |
+-----------------------------------+-----------------------------------+

##### Cloud Security Command Center

###### Cloud Security Command Center

Cortex Cloud's Cloud Security Command Center dashboard provides a
high-level, holistic view of your organization\'s cloud security
posture. It provides insights into data ingestion, asset coverage,
security risks, and recommended posture cases. The dashboard simplifies
monitoring the overall security landscape to improve your overall cloud
security posture.

Key features include:

- A high-level overview of the cloud security environment that you can
  share with leadership to view the most recent attack paths, risks, and
  the recommended remediation steps.

- Real-time visibility into key metrics such as assets covered, security
  issues detected, and actions taken.

- Guided next steps leveraging Posture Cases to help resolve attack
  paths and risks with the most impact instead of sifting through
  individual issues.

- Centralized, top-down view of assets with security metrics across
  connected cloud providers.

- Integrated focus on security posture, including risks, attack paths,
  and business value metrics such as time saved and resources protected.

> **Note**
>
> The Cloud Security Command Center dashboard is currently only
> available by default to users with the Instance Administrator and
> Viewer roles. Custom roles, which include the Cloud Security Command
> Center View/Edit role permissions, also have access.

####### Fine-Tune your Investigation

Choose from a range of Command Center filters to help you focus on
specific issues that have the highest return on investment. Select one
of the options below to fine tune your search:

- On the Cloud Security Command Center dashboard note that by default
  the dashboard is set to Asset Class view. Select the **View By**
  button to switch to a view of risks by Cloud Service Provider (CSP),
  or Region.

- Once you've selected a view you can also further narrow your search,
  by limiting your view by a specific listed CSP and time window under
  **View By**.

![](media/rId1176.gif){width="5.833333333333333in"
height="3.1645833333333333in"}

######## Data Sources

The left portion of the dashboard highlights the sources ingested and
scanned to identify potential security vulnerabilities. The dashboard
ingests the following data sources to detect security issues:

- Audit Log

- Flow Log

- Cloud Configs

- Workloads

Hovering over data types such as Audit and Flow Logs reveals the volume
and count of data ingested and detailed information on any ingestion
issues, whereas Cloud Configs and Workloads indicate the count of
ingested data. In the event of a data ingestion error, select a data
source to be redirected to the Data Sources page to investigate the
ingestion issue.

######## Assets with Vulnerabilities

The central portion of the dashboard provides a high-level view of the
total assets monitored, broken out by asset class and associated
security posture, highlighting assets with incidents, attack paths and
risks. Assets are visualized as bubbles and broken down into the
following classes:

- AI

- Compute

- Data

- Identity

- Network

- APIs

- Other

Inside each asset bubble, the highlighted dots represent the assets with
security issues. The dots are color coded to indicate issues of varying
number and severity as detailed below:

- Gray - Assets with no issues detected

- Yellow -Assets with risks

- Red - Assets with attack paths

- Purple - Assets with incidents

Assets with more than one type of issue will be color coded based on the
following priority: incidents \> attack paths \> risks.

You also have the option to use the **View By** filters to further drill
down. Select **View By \> Provider** to see all the assets with
vulnerabilities grouped by CSP. Alternatively, click on
**View By \> Region** to see assets at risk by geographical area.

######## Security Outcomes

The Security Outcomes portion of the dashboard highlights incidents that
generated Security Cases and attack paths, and risks that feed into
Posture Cases. Reference the sections below to learn more about Security
and Posture Cases:

######### Security Cases

Security cases provide a count of open and resolved cases, and
additional details on the incident including asset classes that comprise
the case.

######### Posture Cases

Posture cases summarize security tasks, providing you with a clear
direction of what problems to address, their potential impact on overall
security, specific orchestration options and outcomes. Posture cases are
dynamically updated based on your current security posture. Hover over
any asset bubble to view a dynamically updated count of Posture Cases.

The steps below use one sample asset class to outline how you can get
the most out of Posture Cases in the Command Center dashboard:

1.  On the Cloud Security Command Center dashboard select the Identity
    bubble.

- ![](media/rId1182.png){width="5.833333333333333in"
  height="3.492707786526684in"}

2.  Select from one of the Asset Categories provided on the left to
    further narrow your search. For example, for the IAM asset class
    filtering options include: Human/Non-Human Identity, Cloud Service
    Account, IAM Group, and Policy.

3.  Select an Asset Class to view the impacted assets highlighted in the
    bubble view. The associated Security and Posture cases if any are
    also available. Both Security and Posture cases are created by
    attack paths and risks that are grouped together. Some risks may not
    be accounted for by a Case, but their totals are listed as shown
    above.

####### Value Metrics

The key metrics bar provides you with a closer look at the value
provided by the Cortex XSIAM platform. Metrics include data points such
as Total Assets, Cloud Data Ingestions, Security Issues Closed, Cloud
Agents, Time Saved, and Analyst Savings.

> **Note**
>
> The **Time Saved** estimate is based on the total amount of savings
> derived from the reduction of issues by grouping and addressing them
> as Posture Cases and Attack Paths. Analyst savings are estimates based
> on an average Security Analyst's wage coupled with the reduction in
> time spent addressing Issues on an individual basis.

##### Cloud Security Operations

###### Cloud Security Operations

> **Note**
>
> Requires the Cortex Cloud Runtime Security add-on or the Cortex Cloud
> Posture Management add-on.

The Cloud Security Operations dashboard helps you rapidly assess your
security posture and resolve issues with the largest impact. As a
security architect or engineer you can leverage the dashboard to assess
the efficiency with which your team responds to security issues on an
ongoing basis, without spending any extra time gathering and grouping
issue details, identifying owners, and kickstarting the remediation
process. Contextual views also link to other areas of the Cortex Cloud
platform for deeper security context. With the Cloud Security Operations
dashboard you can:

- Reduce noise and maximize impact: Use the dashboard's curated views to
  focus on the most important issues prioritized by criticality and
  impact, and tasks that maximize the output of your efforts.

- Improve situational awareness and visibility: The dashboard interface
  helps you learn about your security estate, identify security gaps,
  and track progress against key performance indicators such as Issue
  Burn Down and Mean Time To Remediation (MTTR)

- Customize your view: The dashboard provides a default view for each of
  the widgets while giving you the option to customize views to capture
  the insights you need.

![](media/rId1191.png){width="5.833333333333333in"
height="3.2958333333333334in"}

> **Note**
>
> Command Center data may not match the counts on the Issues page and
> you may observe inconsistencies. This is because dashboard data is a
> snapshot of issues identified, whereas the Issues page provides the
> most up to date view of risks across your cloud assets. In addition,
> the Issues pages does not support all the currently available filters
> on the Command Center dashboard.

####### Dashboard Widgets

The Cloud Security Operations dashboard provides the widgets described
below to help you rapidly remediate the issues that require immediate
attention.

+-----------------------------------+-----------------------------------+
| **Widget**                        | **Description**                   |
+:==================================+:==================================+
| Posture Issues Resolved           | Provides a count of the total     |
|                                   | number of Posture issues you have |
|                                   | resolved over the selected time   |
|                                   | period across all issue           |
|                                   | categories and compares it with   |
|                                   | the number of issues resolved     |
|                                   | over the previous equivalent time |
|                                   | period. By default, the count     |
|                                   | reflects the number of Critical   |
|                                   | and High severity issues you have |
|                                   | resolved over the last 7 day      |
|                                   | period, while the percentage      |
|                                   | change indicates the relative     |
|                                   | change from the previous 7-day    |
|                                   | period.                           |
|                                   |                                   |
|                                   | Issues are based on rule          |
|                                   | violations on a specified scope   |
|                                   | of resources. Select any portion  |
|                                   | of the issues highlighted to see  |
|                                   | a list view of resolved issues.   |
+-----------------------------------+-----------------------------------+
| Open Posture Issues               | Provides a cumulative snapshot    |
|                                   | count of the total number of      |
|                                   | Posture issues that remain        |
|                                   | unresolved in your environment    |
|                                   | and tracks the relative change in |
|                                   | this count over the selected time |
|                                   | frame. By default, the count      |
|                                   | reflects the total number of      |
|                                   | Critical and High severity issues |
|                                   | still unresolved in your          |
|                                   | environment, while the percentage |
|                                   | change indicates the relative     |
|                                   | change in this count over the     |
|                                   | last 7 days.                      |
|                                   |                                   |
|                                   | Select the                        |
|                                   | **Related Posture Cases** donut   |
|                                   | chart to see Critical and High    |
|                                   | issues grouped into remediable    |
|                                   | Posture Cases. The displayed      |
|                                   | count shows you the number of     |
|                                   | Open Issues that can be addressed |
|                                   | by resolving the corresponding    |
|                                   | Posture Case category.            |
|                                   |                                   |
|                                   | Choose from one of the            |
|                                   | time-ranges specified in the      |
|                                   | filter options to narrow your     |
|                                   | search.                           |
+-----------------------------------+-----------------------------------+
| Open Posture Issues by Age        | Provides a total count of         |
|                                   | unresolved Posture issues sorted  |
|                                   | by the time period since they     |
|                                   | first originated in the system.   |
|                                   | Select any time range to view a   |
|                                   | detailed list of Issues defined   |
|                                   | by how long they have remained    |
|                                   | unresolved.                       |
+-----------------------------------+-----------------------------------+
| Posture Issue Burndown            | Provides a trendline of the total |
|                                   | number of open and resolved       |
|                                   | Posture issues over time across   |
|                                   | all issue categories. By default, |
|                                   | the trendlines track the number   |
|                                   | of open and resolved issues over  |
|                                   | the last 7 days.                  |
|                                   |                                   |
|                                   | This daily point in time snapshot |
|                                   | captured can be adjusted by       |
|                                   | severity level. Select the filter |
|                                   | option to narrow issues displayed |
|                                   | by Issue Type (Attack Paths,      |
|                                   | Configuration, Data etc.) or Time |
|                                   | Range.                            |
+-----------------------------------+-----------------------------------+
| Mean Time to Remediation Issues   | Provides a graphical view of the  |
| (MTTR)                            | Mean Time to Remediation (MTTR)   |
|                                   | for issues across all categories, |
|                                   | within the Posture domain, over a |
|                                   | selected time range. By default,  |
|                                   | the chart displays the MTTR       |
|                                   | trends for Critical and High      |
|                                   | severity issues, as well as, the  |
|                                   | combined MTTR across both         |
|                                   | severities over the last 7-day    |
|                                   | period. Switch to the table view  |
|                                   | to compare the 7-day average MTTR |
|                                   | with the average across the       |
|                                   | previous 7-day period.            |
|                                   |                                   |
|                                   | The severity level displayed in   |
|                                   | the list view is set by the       |
|                                   | levels selected in the global     |
|                                   | filter. This can be adjusted on   |
|                                   | the **View MTTR Insights**        |
|                                   | side-panel. The                   |
|                                   | **View MTTR Insights** side-panel |
|                                   | also lists the top ten            |
|                                   | Accounts/Issues with the highest  |
|                                   | MTTR for further analysis. Select |
|                                   | the filter option to narrow down  |
|                                   | issues displayed by Issue Type    |
|                                   | (Attack Paths, Configuration,     |
|                                   | Data etc.) or Severity.           |
+-----------------------------------+-----------------------------------+
| Top 3 Posture Cases               | Top 3 unresolved Posture Cases    |
|                                   | based on the count of Posture     |
|                                   | issues within the cases with      |
|                                   | domain as posture. Click on any   |
|                                   | Posture Case to be redirected to  |
|                                   | a detailed view of the case.      |
|                                   | Select the filter option to       |
|                                   | narrow down issues displayed by   |
|                                   | Posture Cases status or time      |
|                                   | range. Select                     |
|                                   | ** View All Posture Cases** to    |
|                                   | see a comprehensive list of all   |
|                                   | open Posture Cases containing     |
|                                   | Crttical and High severity        |
|                                   | Issues.                           |
+-----------------------------------+-----------------------------------+
| Open Posture Issues by Type       | Provides a breakdown of all open  |
|                                   | Posture issues listed by all      |
|                                   | applicable Issue Type (Attack     |
|                                   | Paths, Configuration, Data, Code, |
|                                   | etc.) and Severity. Click on any  |
|                                   | issue to be redirected to the     |
|                                   | Issues view. Select the filter    |
|                                   | option to narrow down issues by a |
|                                   | specific time range. You can also |
|                                   | toggle between graph and table    |
|                                   | view here.                        |
+-----------------------------------+-----------------------------------+
| Top Impacted Assets               | Displays the top five assets with |
|                                   | the highest number of Posture     |
|                                   | issues. Additional account and    |
|                                   | asset details are also provided.  |
|                                   | Click on any asset to view more   |
|                                   | details in the Assets side panel. |
|                                   | Assets can be filtered by type,   |
|                                   | category, and time range. Graph   |
|                                   | and table toggle is also          |
|                                   | available to customize your view  |
+-----------------------------------+-----------------------------------+
| Top Impacted Accounts             | Lists the account with the        |
|                                   | highest number of unresolved      |
|                                   | Posture issues, sorted by issue   |
|                                   | count and broken down by          |
|                                   | severity. Select a filter to      |
|                                   | narrow your search by time range  |
|                                   | or issue type.                    |
+-----------------------------------+-----------------------------------+

> **Note**
>
> The Last updated time indicated on each widget may differ as widget
> data is gathered at varying intervals.

######## Generate Reports

You can also share Cloud Security Operations dashboard reports with
stakeholders to keep them abreast of the security status of your cloud
assets. Select the **Save as a report template** to create a shareable
template. Next, navigate to **Report Templates** to Edit, Delete, or
**Generate a Report** that can be scheduled for wider distribution.

######## Filter Options

Use one of the multiple filter options provided to further focus on the
most impactful issues. Filter options include:

- **Severity Filter:** Select a severity level from the drop-down to
  apply the filter globally across all widgets. Click **Run** to update
  all existing widgets to the selected severity level. Severity can also
  be adjusted individually at the widget level. Filter settings at the
  widget level are saved, global filters are however not saved.

- **Time Range Filter:** By default the time range is set to 7 days.
  This can be updated to 24 hours, 7 or 30 days, and a Custom time frame
  and applied across all widgets.

#### Predefined dashboards

Cortex XSIAM provides predefined dashboards that display widgets
tailored to the dashboard type. The dashboards can help you monitor
different aspects of your environment. To access your default dashboard,
select Dashboards & Reports \> Dashboard. From the dashboard header, a
drop-down menu lists all available predefined and custom dashboards. The
available dashboards depend on your license type.

To change your default dashboard, go to Dashboards & Reports \>
Dashboard Manager. In the **Dashboard Manager**, you can also create
custom dashboards based on existing dashboards and save dashboards as
report templates.

The following predefined dashboards are available:

+-----------------------+----------------------------------------------------+-----------------------+
| Dashboard name        | Description                                        | Other details         |
+=======================+====================================================+=======================+
| Agent Management      | Provides an overview of the deployed agents in     |                       |
|                       | your organization, their statuses and content      |                       |
|                       | versions, and a breakdown by OS type.              |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| AI Security           | The Cortex Cloud AI Security overview dashboard    |                       |
|                       | serves as the central hub for information on the   |                       |
|                       | AI ecosystem within the organization. It provides  |                       |
|                       | a comprehensive overview of AI security posture    |                       |
|                       | and is designed to help users quickly access       |                       |
|                       | relevant information. The layout and organization  |                       |
|                       | of the dashboard are tailored to guide you in      |                       |
|                       | understanding the AI environment and determining   |                       |
|                       | the next steps to take for effective AI            |                       |
|                       | governance.                                        |                       |
|                       |                                                    |                       |
|                       | For more information, see [What is Cortex Cloud AI |                       |
|                       | Security?](#UUID0074a352a93966b514e099fa518cbaf4). |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| API security          | Provides an overview of your API security          |                       |
| Management            | landscape. You can view all the information and    |                       |
|                       | statistics applicable to threats and               |                       |
|                       | vulnerabilities of APIs across the cloud and       |                       |
|                       | services in your environment. Using this           |                       |
|                       | information, you can manage and implement security |                       |
|                       | measures to safeguard the APIs running in your     |                       |
|                       | environment.                                       |                       |
|                       |                                                    |                       |
|                       | The predefined dashboard for API security          |                       |
|                       | management, you can view data for:                 |                       |
|                       |                                                    |                       |
|                       | - Risky API Funnel                                 |                       |
|                       |                                                    |                       |
|                       | - Attack traffic over time                         |                       |
|                       |                                                    |                       |
|                       | - Attacks by region                                |                       |
|                       |                                                    |                       |
|                       | - Risks by severity over time                      |                       |
|                       |                                                    |                       |
|                       | - Total attacks per type                           |                       |
|                       |                                                    |                       |
|                       | - Asset count by sensitive data type               |                       |
|                       |                                                    |                       |
|                       | - Number of APIs                                   |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Application Security  | Provides an overview of application security       |                       |
|                       | posture with asset and code/pipeline issue         |                       |
|                       | insights.                                          |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Data Ingestion        | Provides an overview of data ingestion by product  | Due to a calculation  |
|                       | and vendor, the daily quota consumption, and your  | change in NGFW log    |
|                       | data ingestion rate.                               | ingestion and         |
|                       |                                                    | improvements to data  |
|                       |                                                    | ingestion metrics,    |
|                       |                                                    | you cannot view data  |
|                       |                                                    | earlier than July     |
|                       |                                                    | 2023 on this          |
|                       |                                                    | dashboard. However,   |
|                       |                                                    | you can still view    |
|                       |                                                    | this data by running  |
|                       |                                                    | Cortex Query Language |
|                       |                                                    | (XQL) queries on the  |
|                       |                                                    | `metrics_center` data |
|                       |                                                    | set.                  |
+-----------------------+----------------------------------------------------+-----------------------+
| Data Security         | Discover and visualize all your data assets across |                       |
|                       | the different cloud services, which will help you  |                       |
|                       | understand where the sensitive data is, how it is  |                       |
|                       | used and how it is moving across the organization. |                       |
|                       |                                                    |                       |
|                       | For more information, see [What is Cortex Cloud    |                       |
|                       | Data                                               |                       |
|                       | Security?](#UUIDd6e165e7d431b94866f8d3535550ac2d). |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Identity Security     | You can use the Identity Security dashboard to     |                       |
|                       | ensure that your identity estate is fully covered  |                       |
|                       | from a security perspective. The Identity Security |                       |
|                       | dashboard helps you perform actions such as        |                       |
|                       | monitoring your identity inventory, detecting the  |                       |
|                       | top critical issues and findings in your           |                       |
|                       | environment, identifying risky identities,         |                       |
|                       | discovering admins and admins at risk, and         |                       |
|                       | analyzing 3rd-party access.                        |                       |
|                       |                                                    |                       |
|                       | For more information, see [What is Cortex Cloud    |                       |
|                       | Identity                                           |                       |
|                       | Security?](#UUID38efb91edf7c9263819e2c84e9d6ff17). |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| IT Metrics            | Provides an overview of IT performance on your     | The Applications      |
|                       | Cortex XDR agent, including CPU and memory         | Crashing widget is    |
|                       | performance data, connectivity data, and data      | supported for Windows |
|                       | about hard reboots and crashed applications.       | agents only.          |
+-----------------------+----------------------------------------------------+-----------------------+
| KSPM                  | Provides insights into your Kubernetes             |                       |
|                       | environment, including clusters, assets, and       |                       |
|                       | resources. Receive critical security information   |                       |
|                       | related to vulnerabilities, malware, secrets, and  |                       |
|                       | other available scanners. Identify areas lacking   |                       |
|                       | protection and take action to secure your          |                       |
|                       | clusters.                                          |                       |
|                       |                                                    |                       |
|                       | For more information on onboarding your Kubernetes |                       |
|                       | environment, see [Onboard the Kubernetes           |                       |
|                       | Connector](#UUID0735a2d92b0f9e3d6c3f994dfe6fdea8). |                       |
|                       |                                                    |                       |
|                       | > **Note**                                         |                       |
|                       | >                                                  |                       |
|                       | > Users can access all information on the          |                       |
|                       | > dashboard when their user access is scoped to    |                       |
|                       | > view **All assets** or assigned to the Instance  |                       |
|                       | > Administrator role. Otherwise, users with        |                       |
|                       | > granular scoping set to **No assets** or         |                       |
|                       | > **Select asset groups** will have limited access |                       |
|                       | > to the dashboard. For more information on        |                       |
|                       | > Scope-Based Access Control (SBAC), see [Manage   |                       |
|                       | > user                                             |                       |
|                       | > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).   |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| MITRE ATT&CK          | Provides a comprehensive overview of the Cortex    |                       |
| Framework Coverage    | XSIAM content and capabilities in context with the |                       |
|                       | MITRE ATT&CK framework.                            |                       |
|                       |                                                    |                       |
|                       | For more information, see [Review MITRE ATT&CK     |                       |
|                       | framework                                          |                       |
|                       | coverage](#UUID698b98f4498cebd527d471e55831a55d).  |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| My Dashboard          | Provides an overview of the cases and MTTR for the |                       |
|                       | logged-in user.                                    |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Network Traffic       | Provides an overview of network traffic analysis,  |                       |
| Analysis (NTA)        | and highlights key pieces of information.          |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| NGFW Ingestion        | Provides an overview of ingestion status for all   |                       |
|                       | log types, the daily quota consumption for NGFW,   |                       |
|                       | and a breakdown by log type.                       |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Playbook Optimization | Provides an overview of Playbook, script and       |                       |
|                       | command metrics for optimization.                  |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Risk Management       | Provides issue and case information to aid in risk | > **Note**            |
|                       | assessment by highlighting information about       | >                     |
|                       | compromised accounts and insider threats.          | > Requires the ITDR   |
|                       |                                                    | > add-on.             |
|                       | The issues displayed in this dashboard are tagged  |                       |
|                       | by the research as Identity Threat issues or       |                       |
|                       | Identity Analytics issues. A case is displayed if  |                       |
|                       | any of its associated issues are tagged as an      |                       |
|                       | Identity threat or an Identity Analytics threat.   |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Security Manager      | Provides general information about Cortex XSIAM    |                       |
|                       | cases and agents.                                  |                       |
+-----------------------+----------------------------------------------------+-----------------------+
| Threat Intel          | Provides information about malicious or suspicious |                       |
| Management            | indicators in cases.                               |                       |
+-----------------------+----------------------------------------------------+-----------------------+

#### Reports

Reports contain statistical data in the form of widgets, which enable
you to analyze data from inside or outside Cortex XSIAM, in different
formats such as graphs, pie charts, or text from information. After
generating a report, it also appears in the Reports tab, so you can use
the report again.

##### Report templates

On the **Report Templates** page, you can view, delete, import, export,
create, and modify report templates. You can also select and generate
multiple reports.

### Build custom dashboards and reports

You can create custom dashboards and reports that are tailored to your
unique workflow and support your day-to-day operations. With custom
dashboards and reports, you have the flexibility to base your dashboard
or report on an existing template, or build a new template from scratch.

Dashboards and reports are built from widgets. You can drag any widgets
from the **Widget Library** on to your dashboard or report and arrange
them. Cortex XSIAM provides predefined widgets for you to use. In
addition, you can create custom widgets that are built on Cortex Query
Language (XQL) queries or custom scripts and provide the flexibility to
query specific data, and select the graphical format you require (such
as table, line graph, or pie chart).

#### Build a custom dashboard

You can base your custom dashboards on predefined dashboard templates,
or you can build a new dashboard from scratch.

1.  Select Dashboards & Reports \> Customize \> Dashboard Manager \> New
    Dashboard, or in the **Dashboard Manager** right-click an existing
    dashboard and select **Save as new**.

2.  In the **Dashboard Builder**, under **Dashboard Name**, enter a
    unique name for the dashboard.

3.  Under **Dashboard Type**, choose a built-in dashboard template or a
    blank template, and click **Next**.

4.  Customize your dashboard.

- To get a feel for how the data will look, Cortex XSIAM provides mock
  data. To see how the dashboard would look with real data in your
  environment, change the toggle to **Real Data**.

5.  Add widgets to the dashboard. From the widget library, drag widgets
    on to the dashboard.

- > **Note**

  - > For agent-related widgets, you can apply an endpoint scope to
    > refine the displayed data to only show results from specific
    > endpoint groups.

  <!-- -->

  - > Select the menu on the top right corner of the widget, select
    > **Groups**, and select one or more endpoint groups.

  <!-- -->

  - > For case-related widgets, you can refine the displayed data to
    > only show results from cases that match a case starring
    > configuration. A purple star indicates that the widget is
    > displaying only starred cases. For more information, see [Case
    > starring](#UUID462fb07d16fd2bddbd6e9e8def6ecadc).

6.  (Optional) Configure fixed filters and inputs.

- What are fixed filters and inputs?
  Add fixed filters to your dashboard to provide dashboard users with
  useful dashboard filters that are based on predefined or dynamic input
  values. Any defined filters are displayed in the dashboard header.

  Fixed filters are based on XQL widgets with dynamic parameters. If a
  dashboard contains these widgets, the **Add Filters & Inputs** option
  is displayed. For more information, see [Configure filters and inputs
  for custom XQL widgets](#UUID6d3f1930adbbaba7a8d6b6671f0b5b15).

7.  (Optional for dashboards with custom XQL widgets) Configure
    dashboard drilldowns.

- What are dashboard drilldowns?
  Add drilldowns to your dashboard to provide interactive data insights
  when clicking on data points, table rows, or other visualization
  elements.

  Dashboard drilldowns are based on XQL widgets. To add a drilldown to
  an XQL widget, click on the widget menu, and select **Add drilldown**.
  For more information, see [Configure dashboard
  drilldowns](#UUIDb201aa9fde70fa799bc23bf476b9998a).

8.  Under **Time Range**, set a time range for your dashboard.

- By default, the widgets use the dashboard time frame. You can change
  the widget time frame from the widget menu.

9.  When you have finished customizing your dashboard, click **Next**.

10. To set the custom dashboard as your default dashboard, select
    **Define as default dashboard**.

11. To keep this dashboard visible only for you, select **Private**.

- Otherwise, the dashboard is public and visible to all Cortex XSIAM
  users with the appropriate roles to view dashboards. Private
  dashboards can only be viewed, edited, and deleted by the dashboard
  creator.

12. Click **Generate** to complete your dashboard.

#### Manage your Widget Library

The **Widget Library** displays predefined widgets, user-created custom
Cortex Query Language (XQL) widgets, and user-created custom script
widgets.

You can include these widgets in your custom dashboards and reports. To
access the **Widget Library**, navigate to Dashboards & Reports \>
Widget Library.

From the **Widget Library** you can take the following actions:

- Create custom widgets based on XQL search queries. For more
  information see [Create custom XQL
  widgets](#UUID61c360eebddd76373c7e500f08dc57a7).

- Create custom widgets based on scripts. For more information, see
  [Create a custom widget using a
  script](#UUIDd584ce579a09c946c0446011ae64a84f).

- Search for custom and predefined widgets. Widgets are grouped by
  category.

- Edit or delete custom widgets.

<!-- -->

- > **Note**

  > Any dashboards or reports that include the widget are affected by
  > the changes.

### Fine-tune dashboards and reports

You can fine-tune your custom dashboards and reports to tailor them to
suit your specific needs. The following dashboard features enhance the
functionality of your dashboards, by refining the data displayed and
enabling dashboard users to filter and manipulate the displayed data.
Click on the tabs to see each feature.

#### Custom script widgets

Build custom widgets based on scripts, to display data from third -part
systems.

These widgets can display pie, column, and line charts, as well as
single value results. A single value result can, optionally, be
presented as a time duration.

#### Custom XQL widgets

Personalize the information that you display on your custom dashboards
and reports by creating custom XQL widgets and adding them to your
dashboard. 

These widgets can query specific information that is unique to your
workflow, and define the graphical format you require (such as table,
line graph, or pie chart). In addition, you can add variables to your
custom XQL widget that provide dynamic input values for dashboard
filters.

#### Fixed filters and inputs

Enable dashboard users to alter the scope of a dashboard by selecting
from predefined or dynamic input values.

#### Dashboard drilldowns

Enable dashboard users to access interactive data insights when clicking
on data points in widgets. Drilldowns can trigger contextual changes on
the dashboard, or they can link to an XQL search, a custom URL, another
dashboard, or a report. Users can hover over a widget to see details
about the drilldown, and click a value to trigger the drilldown.

#### Create a custom widget using a script

You can use scripts in custom widgets to create dynamic widgets for more
complex calculations and to present data from third-party systems.

For examples of creating widgets using scripts, see [Script-based widget
examples](#UUID0c1b69e91d4e1646084ba6761a8c769e).

Before creating a script-based widget in the **Widgets Library**, you
need to create or upload the script to the **Scripts** page. In the
**Widgets Library**, you can change elements of the visual presentation.

Cortex XSIAM supports JavaScript, Python and PowerShell.

1.  Go to Investigation & Response \> Automation \> Scripts page to
    upload a script or create a new script for one of the following
    chart types:

    - Pie

    - Column

    - Line

    - Single Value

2.  In the **Script Settings** , add the **widget** tag to the script.

3.  Go to Dashboards & Reports \> Widget Library and create a script
    widget.

4.  Name the widget and select your script from the **Scripts** menu.

- > **Note**

  > If you have added arguments to the script, these appear when
  > creating a widget.

5.  **Run** the script to view the results.

6.  Use the **Chart Editor** to choose the graph type and the subtype
    and to enable or disable the graph legend.

- > **Note**

  > Available options are **Pie**, **Column**, **Line**, and
  > **Single Value**.

  > To display the result of the script as a time duration, choose the
  > graph type **Single Value** and enable **Show as Time**. You can
  > then select the **Time Unit** (millisecond, second, minute, or hour)
  > and the **Display format**.

7.  Add the script-based widget to a report or a dashboard.

##### Script-based widget examples

You can use script-based widgets to perform calculations on and
visualize third-party data.

> **Note**
>
> Add the **widget** tag in the script settings. to make the script
> available for use in script-based widgets.

The following are sample Python scripts for the graph types
**Single Value**, **Pie**, **Line**, and **Column**.

###### Single value

This example shows how to use a script with an API call to return a
single value in a widget. Use this example to build your own script that
pulls in third-party data to display a single value.

> **Note**
>
> If your script returns a time duration, configure the widget with the
> graph type **Single Value** and enable **Show as Time**..

**Example:**

    import requests

    def main():
        api_key = 'PUTYOURKEYHERE'
        symbol = 'PANW'
        api_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

        response = requests.get(api_url)
        data = response.json()

        price_str = data['Global Quote']['05. price']
        price_int = int(float(price_str))

        return_results(price_int)

    if __name__ in ('__main__', '__builtin__', 'builtins'):
        main()

###### Pie, Line, or Column Chart

**Example 1**

The following example script creates random, mock data to simulate a
stock price fluctuating over a short period of time. Use this example to
build your own script that brings in third-party data and display trends
using a pie, line, or column chart.

    import random
    import json
    from datetime import datetime, timedelta

    def main():
        chart_data = []
        start_time = datetime.strptime("13:00", "%H:%M")

        # Start the price at a realistic value
        current_price = 202.0

        # Simulate 50 data points
        for i in range(50):
            # Generate a time label in 1-minute jumps
            time_label = (start_time + timedelta(minutes=i)).strftime("%H:%M")

            # Create the data point for the chart
            data_point = {
                "name": time_label,
                "data": [int(current_price)],
                "groups": []
            }
            chart_data.append(data_point)

            # Simulate the next price by adding a small change to the current price
            price_change = random.uniform(-1.5, 1.5) # A small drift up or down
            current_price += price_change

        # Return the data formatted exactly as in your working script
        return_results({
            "Type": 1,
            "ContentsFormat": "json",
            "Contents": json.dumps(chart_data)
        })


    if __name__ in ('__main__', '__builtin__', 'builtins'):
        main()

When used in a widget:

![](media/rId1215.png){width="5.833333333333333in"
height="3.376418416447944in"}

**Example 2**

The following example script generates simulated data representing the
count of security incidents (or other events) broken down by severity
level for each day of the week (Monday to Friday). Use this example to
build your own script to create a stacked column chart. Configure the
widget with graph type **Column** subtype **Stacked**.

    import json
    import random

    def main():
        chart_data = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        severities = ["Critical", "High", "Medium", "Low", "Info"]

        for day in days:
            groups_list = []
            daily_total = 0

            for severity in severities:
                count = 0
                if severity == "Critical":
                    count = random.randint(0, 5)
                elif severity == "High":
                    count = random.randint(5, 15)
                elif severity == "Medium":
                    count = random.randint(10, 25)
                elif severity == "Low":
                    count = random.randint(20, 50)
                else:
                    count = random.randint(5, 30)

                daily_total += count
                groups_list.append({"name": severity, "data": [count]})

            chart_data.append({
                "name": day,
                "data": [daily_total],
                "groups": groups_list
            })

        return_results({
            "Type": 1,
            "ContentsFormat": "json",
            "Contents": json.dumps(chart_data)
        })

When used in a widget:

![](media/rId1218.png){width="5.833333333333333in" height="4.06875in"}

#### Create a text widget

You can use a widget to display formatted text in dashboards and
reports.

**Add a text-based widget to a dashboard**

1.  Go to Dashboards & Reports \> Dashboard Manager and create a new
    dashboard or right-click to edit an existing custom dashboard.

2.  If you are creating a new dashboard, enter a dashboard name.

3.  If you are creating a new dashboard, choose a dashboard type or
    create a new dashboard from scratch.

4.  From the **Widgets Library**, drag the **Free Text** widget to your
    dashboard.

5.  Add your custom text to the **Free Text** widget.

6.  (Optional) To enable Markdown, click the vertical menu for the
    widget and select **Use Markdown**.

7.  Click **Next** .

8.  Choose your dashboard options and **Generate** dashboard.

**Add a text-based widget to a report template**

> **Note**
>
> From the dashboard manager, you can right-click an existing dashboard
> and choose **Save as report template**. You can also add text-based
> widgets directly to new or existing report templates, as described
> below.

1.  Go to Dashboards & Reports \> Report Templates and create a new
    template or right-click to edit an existing custom template.

2.  If you are creating a new report template, enter a report template
    name.

3.  If you are creating a new report template, choose a report template
    type or create a new report template from scratch.

4.  From the **Widgets Library**, drag the **Free Text** widget to your
    dashboard.

5.  Add your custom text to the **Free Text** widget.

6.  (Optional) To enable Markdown, click the vertical menu for the
    widget and select **Use Markdown**.

7.  Click **Next** .

8.  Choose your report builder options and **Save Template**.

#### Create custom XQL widgets

With custom XQL widgets you can personalize the information that you
display on your custom dashboards and reports. You can build widgets
that query specific information that is unique to your workflow, and
define the graphical format you require (such as table, line graph, or
pie chart).

All of your predefined and custom XQL widgets are available in the
**Widget Library** under Dashboards & Reports \> Customize \> Widget
Library. From the **Widget Library**, you can browse all widgets by
category, create new XQL widgets, and edit and delete existing XQL
widgets.

**How to create a custom XQL widget**

1.  In the **Widget Library**, select **Create custom XQL widget**.

2.  Enter a widget name and an optional description.

3.  Define an XQL query that searches for the data you require. Select
    **XQL Helper** to view XQL search and schema examples. For more
    information, see [How to build XQL
    queries](#UUID125805d7e53750e71a87cb4c4140fa73).

- > **Tip**

  > You can create a generic dashboard for multiple views of the same
  > dataset by defining the dataset in the XQL widget as
  > `dataset = <dataset_name>*`. The placement of the asterisk (\*) in
  > the dataset name ensures that any view containing this prefix text
  > is displayed in the results.

  > The dataset in a query is defined as:

      dataset = amazon_aws_raw*

  > If there are multiple datasets that begin with `amazon_aws_raw` in
  > their name, such as `amazon_aws_raw_eu_view` and
  > `amazon_aws_raw_us1_view`, these views will be included.

4.  Select **Preview** to review the search results.

- > **Note**

  > Cortex Query Language (XQL) queries generated from the
  > **Widget Library** do not appear in the **Query Center**. The
  > results are used only for creating the custom widget.

5.  *(Optional)* Add parameters to the query.

- You can use parameters to filter widget data on a dashboard or report,
  and create drilldowns on dashboards. Base your filters on fields and
  values in the query results.

  Take the following steps
  1.  In the search results, identify a field by which you want to
      filter.

  2.  Using the `filter` stage, define parameters prefixed with `$`.

  - To specify parameters with a single predefined value, use the `=`
    operator. To specify parameters with multiple values (predefined or
    dynamic), use the `IN` operator.

    Example of a single value parameter
    Single value parameters
    The following query defines the `$domain` parameter for filtering
    dashboard data by domain, based on the `domain` field in the
    `agent_auditing` dataset.

    Single value parameters are based on static predefined values. In
    this example, the dashboard user will be able to select a domain
    from a list of predefined domains.

        dataset = agent_auditing | filter domain = $domain

    Example of a multiple value parameter
    Multiple value parameters
    The following query defines the `$endpointname` parameter for
    filtering dashboard data by one or more endpoint names, based on the
    `endpoint_name` field in the `agent_auditing` dataset.

    You can configure this parameter with static predefined values, or
    dynamic values that are pulled from an XQL query.

        dataset = agent_auditing | filter endpoint_name IN ($endpointname)

  3.  (Optional) Under **Assign Parameters (default values)**, define
      default values for the parameters. When you add the widget to a
      dashboard or report, the data will be automatically populated.
      Alternatively, you can configure all input values when you set up
      a dashboard or report.

6.  *(Optional)* Change the default time period against which to run
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

7.  In the **Query Results** section, to graph the results either:

- Use Chart Editor
  Under Query Results \> Chart Editor
  (![](media/rId1231.png){width="0.2604166666666667in"
  height="0.20833333333333334in"}), manually build and view the graph
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

    - **Show Callouts**: Display numeric values on graph.

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

  - view graph type = column subtype = grouped header = “Test 1” xaxis = _time yaxis = _product,action_total_upload series = _vendor

  <!-- -->

  - Select **ADD TO QUERY** to insert your chart preferences into the
    query itself.

8.  Save the widget.

- The custom widget appears in the list of existing widgets.

##### Configure filters and inputs for custom XQL widgets

Define fixed filters on your dashboards to enable dashboard users to
alter the scope of the dashboard by selecting from predefined or dynamic
values. You can define filters with free text, single select, and
multiple select input values. After configuration, anyone who views your
dashboard can use the fixed filters in the dashboard header.

> **Prerequisite**
>
> Fixed filters are based on parameters that are defined in custom XQL
> widgets. Before you can configure fixed filters, take the following
> steps:

1.  > Create custom XQL widgets with parameters. For more information,
    > see [Create custom XQL
    > widgets](#UUID61c360eebddd76373c7e500f08dc57a7).

2.  > Add the widgets to a Custom dashboard. For more information, see
    > [Build a custom dashboard](#UUID6e8570201468816980eccfe0601e0d14).

**How to configure fixed dashboard filters**

1.  Open a custom dashboard, and select **Edit dashboard**.

2.  Click **Add Filters & Inputs**.

- This option only appears if the dashboard contains custom XQL widgets
  with defined parameters.

3.  Under **Parameter Title** enter a name that identifies the
    parameter.

4.  On the **FILTERS & INPUTS** panel, click **+Add an input** and
    select one of the following options:

    - To specify a single predefined value, select **Single Select**.

    - To specify multiple predefined or dynamic values, select
      **Multi Select**.

    - To specify a single free text value, select **Free text/number**.

- Guidelines
  - Select an option that corresponds with the parameter configured in
    the XQL widget. Parameters with single predefined or free text
    values use the `=` operator, and parameters with multiple values,
    use the `IN` operator.

  - Predefined values are most suitable for filtering fields that have
    static values, such as status fields with a limited number of
    available options.

  - Dynamic values help you to filter with values that change often. You
    can configure an XQL query that extracts all of the values that are
    available for that field. For example, in the `endpoints` dataset,
    the `endpoint_name` field values can change frequently.

5.  Click **Parameter** and select the parameter that you want to
    configure.

- The parameters are extracted from the XQL queries of the widgets on
  the dashboard. You can define up to four parameter filters on a report
  or dashboard.

6.  If you selected **Single Select** or **Multi Select** values, click
    **Dropdown Options** and specify input values. When you generate the
    dashboard, these input values appear in a dropdown list for
    selection.

    - To configure **Predefined** inputs for **Single Select** and
      **Multi Select** values, manually type the list values.

    <!-- -->

    - Guidelines
      - The values must support the parameter type. For example, for
        `$name` specify characters and for `$num` specify numbers.

      - If you uploaded numbers in a string, specify each number in
        quotes, for example \"500\".

    <!-- -->

    - To configure **Dynamic** inputs for **Multi Select** values, click
      **XQL Query to fetch dynamic values**.

    <!-- -->

    - Guidelines
      In the XQL Query Builder, configure a query that includes the
      `field` stage and the name of the column from which to take the
      dropdown values. All values in the specified `field` will be
      available for selection, and the values are dynamically updated.

      Example
      In this example, the **endpoint_name** field is configured. The
      dashboard user will be able to filter by one or more values from
      the `endpoint_name` field.

      `dataset =endpoints | fields endpoint_name`

      > **Note**

      > If you specify more than one field, only the first field value
      > is used.

7.  Under **Default Value**, select a value from the list of defined
    values. Specifying a default value ensures that the widget is
    automatically populated when you open the dashboard.

8.  Click **Save Filters & Inputs** and save your dashboard.

- > **Tip**

  > After the initial setup, when you access your dashboard the filters
  > and inputs might need further refinement. You can make changes to
  > the configured parameters in the XQL widgets, and update the
  > **Filters & Inputs** on your dashboard until you are satisfied with
  > the results.

#### Configure dashboard drilldowns

Dashboard drilldowns can trigger contextual changes on the dashboard, or
they can link to an XQL search, a custom URL, another dashboard, or a
report. You configure drilldowns on individual widgets. After a
drilldown is configured, clicking the widget triggers the drilldown.

> **Prerequisite**
>
> To configure drilldowns your dashboard must contain custom XQL
> widgets. In addition, if you want to configure in-dashboard drilldowns
> your custom XQL widget must contain one or more parameters. For more
> information about configuring parameters in custom XQL widgets, see
> [Create custom XQL widgets](#UUID61c360eebddd76373c7e500f08dc57a7).

**How to configure dashboard drilldowns**

1.  Open a custom dashboard and select **Edit dashboard**.

2.  Identify the widget to which you want to apply a drilldown, click on
    the widget menu, and select **Add drilldown**.

3.  In **Action On Click** select one of the following options:

    - **In-Dashboard Drilldown**­: Interactively filters the dashboard
      data. Filters are based on the parameters defined in the custom
      XQL widgets on the dashboard.

    <!-- -->

    - Define the following values:

+-----------------------------------+-------------------------------------------------------+
| Field                             | Action                                                |
+===================================+=======================================================+
| **Parameters**                    | Select the parameter by which to filter. You can      |
|                                   | choose any parameter that is defined in the XQL query |
|                                   | of the widget.                                        |
|                                   |                                                       |
|                                   | > **Note**                                            |
|                                   | >                                                     |
|                                   | > If the selected parameter is configured in other    |
|                                   | > XQL widgets on the dashboard, these widgets are     |
|                                   | > also affected by the drilldown.                     |
+-----------------------------------+-------------------------------------------------------+
| **Value**                         | When a user clicks the widget, the dashboard is       |
|                                   | filtered by this value.                               |
|                                   |                                                       |
|                                   | - Type your own value.                                |
|                                   |                                                       |
|                                   | - Select a variable from which to capture the clicked |
|                                   |   value, for example, the \$y-axis.value in a chart.  |
|                                   |   For more information, see [Variables in             |
|                                   |   drilldowns](#UUIDfed66e1019725a276491d724d6a1b5e1). |
+-----------------------------------+-------------------------------------------------------+

- **Link to dashboard**: Opens a target dashboard.

<!-- -->

- Define the following values:

+-----------------------------------+-------------------------------------------------------+
| Field                             | Action                                                |
+===================================+=======================================================+
| **Dashboard**                     | Select the target dashboard.                          |
+-----------------------------------+-------------------------------------------------------+
| (Optional) **Parameter**          | Select parameters by which to filter the data on the  |
|                                   | target dashboard. Parameters are only available if    |
|                                   | there are parameters defined in the widgets on the    |
|                                   | *target* dashboard.                                   |
+-----------------------------------+-------------------------------------------------------+
| (Optional) **Value**              | When a user clicks the widget, this value is          |
|                                   | configured as a parameter on the target dashboard.    |
|                                   |                                                       |
|                                   | - Type your own value.                                |
|                                   |                                                       |
|                                   | - Select a variable from which to capture the clicked |
|                                   |   value in the source dashboard, for example, the     |
|                                   |   \$y-axis.value in a chart. For more information,    |
|                                   |   see [Variables in                                   |
|                                   |   drilldowns](#UUIDfed66e1019725a276491d724d6a1b5e1). |
+-----------------------------------+-------------------------------------------------------+

- **Open XQL Search**: Runs an XQL query based on the clicked value.

<!-- -->

- Define the following values:

+-----------------------------------+-----------------------------------------------------+
| Field                             | Action                                              |
+===================================+=====================================================+
| **XQL Query**                     | Define the query that you want to run on drilldown. |
|                                   |                                                     |
|                                   | Type `$` to see autocomplete options for variables  |
|                                   | that are available in the widget drilldown. For     |
|                                   | example, in a table widget **\$first.name** selects |
|                                   | the leftmost column name in the table. For more     |
|                                   | information, see [Variables in                      |
|                                   | drilldowns](#UUIDfed66e1019725a276491d724d6a1b5e1). |
+-----------------------------------+-----------------------------------------------------+

- In the following example two parameters are passed from a table widget
  to an XQL query. The first parameter with the cell value that the user
  clicked on, and a second parameter with the cell value in the
  request_url column in the row that the user clicked.

      dataset=xdr_data
      |filter event_type=$y_axis.value and requestUri=$row.request_url
      |fields action_download, action_remote_ip as remote_ip,
      actor_process_image_name as process_name
      |comp count_distinct(action_download) as total_download by process_name,
      remote_ip, remote_hostname
      |sort desc total_download
      |limit 10
      |view graph type=single subtype=standard xaxis=remote_ip yaxis=total_download

<!-- -->

- **Open custom URL**: Opens an external URL based on a clicked value.

<!-- -->

- Define the following values:

+-----------------------------------+-----------------------------------------------------+
| Field                             | Action                                              |
+===================================+=====================================================+
| **URL Address**                   | Type the URL.                                       |
|                                   |                                                     |
|                                   | To create a dynamic drilldown, you can include      |
|                                   | **Available parameters**. For more information      |
|                                   | about the parameters, see [Variables in             |
|                                   | drilldowns](#UUIDfed66e1019725a276491d724d6a1b5e1). |
+-----------------------------------+-----------------------------------------------------+

- In the following URL, the `$x_axis.value` parameter represents cortex
  products names. On drilldown, the \$x_axis.value is replaced with the
  clicked product name in the pie chart.

  https://www.paloaltonetworks.com/cortex/cortex-\$x_axis.value

  ![](media/rId1246.png){width="3.5in" height="2.820754593175853in"}

<!-- -->

- **Generate Report**: Runs a report from a clicked value.

##### Variables in drilldowns

The following tabs are organized according to widget type and describes
the widget variables that are available in drilldowns. The variable
defines the value to capture in the drilldown, according to the element
that is clicked. The captured value is then configured as a parameter by
which to filter data on drilldown.

###### Chart

(Area, Bubble, Column, Funnel, Line, Map, Pie, Scatter, or Word Cloud)

![](media/rId1250.png){width="4.083333333333333in"
height="2.087603893263342in"}

- `$x_axis.name`: Selects the x-axis name.

- `$x_axis.value`: Selects the x-axis value for the clicked value.

- `$y_axis.name`: Selects the y-axis name.

- `$y_axis.value`: Selects the y-axis value for the clicked value.

###### Single value or gauge

![](media/rId1254.png){width="2.3333333333333335in"
height="1.830064523184602in"}

- `$y_axis.name`: Selects the y-axis name that the single value
  represents.

- `$y_axis.value`: Selects the y-axis value for the clicked value.

###### Table

![](media/rId1258.png){width="4.083333333333333in"
height="1.811978346456693in"}

- `$first.name`: Selects the leftmost column name in the table.

- `$first.value`: Selects the leftmost value in the clicked table row.

- `$clicked.name`: Selects the column name of the clicked value.

- `$clicked.value`: Selects the value in the clicked table cell.

- `$row.<field_name>`: Selects the field (column) from the clicked table
  row.

### Run or schedule reports

You can generate reports using pre-designed dashboard templates, or
create custom reports from scratch with widgets from the
**Widget Library**. You can also schedule your reports to run regularly
or just once. All reports are saved under Dashboards & Reports \>
Reports.

To take actions on existing report templates, go to Dashboards & Reports
\> Customize \> Report Templates. On this page you can also import and
export report templates in a JSON format, which enables you to transfer
your configurations between environments for onboarding, migration,
backup, and sharing. You can bulk export and import multiple report
templates at a time.

> **Note**

- > Report templates that are based on custom infrastructure cannot be
  > exported.

- > If you import a report template that already exists in the system,
  > the imported template will overwrite the existing template. If you
  > do not want to overwrite the existing template, duplicate and rename
  > the existing template before importing the new template.

#### Run a report based on a dashboard

You can generate a report based on an existing dashboard.

1.  Select Dashboards & Reports \> Customize \> Dashboards Manager.

2.  Right-click the dashboard from which you want to generate a report,
    and select **Save as report template**.

3.  Enter a unique name for the report and an optional description, and
    click **Save**.

4.  Select Dashboards & Reports \> Customize \> Report Templates.

5.  Locate your report and take one of the following actions:

    - To run the report without make any modifications, hover over the
      report name, and select **Generate Report**.

    - To modify or schedule the report, hover over the report name, and
      select **Edit**.

6.  After your report completes, you can download it from the Dashboards
    & Reports \> Reports page.

#### Create a new report template

You can base your report on an existing template, or you can start with
a blank template.

1.  Select Dashboards & Reports \> Customize \> Reports Templates \> +
    New Template.

2.  Enter a unique name for the report and an optional description.

- > **Note**

  > The report name and description will be displayed in the report
  > header and are not editable during customization.

3.  Under **Data Timeframe**, select the time frame from which to run
    the report. Custom time frames are limited to one month.

4.  Under **Report Type** select the report template on which to base
    the report, or select a blank template to build the report from
    scratch and click **Next**.

5.  Customize your report.

- Cortex XSIAM offers mock data to help you visualize the data\'s
  appearance. To see how the report would look with real data in your
  environment, switch to **Real Data**. Select **Preview in A4** to see
  how the report is displayed in an A4 format.

6.  Add or remove widgets to the report. From the widget library, drag
    widgets on to the report.

- > **Note**

  - > For agent-related widgets, you can apply an endpoint scope to
    > refine the displayed data to only show results from specific
    > endpoint groups.

  <!-- -->

  - > Select the menu on the top right corner of the widget, select
    > **Groups**, and select one or more endpoint groups.

  <!-- -->

  - > For case-related widgets, you can refine the displayed data to
    > only show results from cases that match a case starring
    > configuration. A purple star indicates that the widget is
    > displaying only starred cases. For more information, see [Case
    > starring](#UUID462fb07d16fd2bddbd6e9e8def6ecadc).

7.  (Optional) Add filters to the report. Adding filters and inputs to
    the report gives you the flexibility to filter report data based on
    default values that you define.

- If you selected a report template with default filters, the filters
  are displayed at the top of the dashboard. To edit the filters, click
  **+ Add Filters & Inputs**.

  You can configure basic filters that provide predefined static values,
  as explained in the following steps. Alternatively you can define
  dynamic filters that are based on predefined parameters in custom XQL
  widgets, as explained in [Configure filters and inputs for custom XQL
  widgets](#UUID6d3f1930adbbaba7a8d6b6671f0b5b15).

  a.  Click **+ Add Filters & Inputs**.

  b.  On the **FILTERS & INPUTS** panel, select a parameter for which to
      configure a filter.

  c.  Under **Value**, select one or more filter values.

  - If no values are selected, the filter name shows an error symbol and
    you cannot save the filter.

  d.  Add more filters as required. You can drag the filters to change
      the priority.

  e.  Click **Save Filters & Inputs**.

8.  When you have finished customizing your report template, click
    **Next**.

9.  If you are ready to run the report select **Generate now**, or
    define options for scheduling the report.

10. (Optional) Under **Email Distribution** and **Slack workspace** add
    the recipients that you want to receive a PDF version of your
    report.

- Select **Add password used to access report sent by email and Slack**
  to set password encryption. Password encryption is only available in
  PDF format.

11. (*Optional*) Select **Attach CSV** to attach CSV files of your XQL
    query widgets to the report.

- From the menu, select one or more of your custom widgets to attach to
  the report. The CSV files of the widgets are attached to the report
  along with the report PDF. Depending on how you selected to send the
  report, the CSV file is attached as follows:

  - Email: Sent as separate attachments for each widget. The total size
    of the attachment in the email cannot exceed 20 MB.

  - Slack: Sent within a ZIP file that includes the PDF file.

12. Click **Save Template**.

13. After your report completes, you can download it from the Dashboards
    & Reports \> Reports page.

- In the **Name** field, icons indicate the number of attached files for
  each report. Reports with multiple PDF and CSV files are marked with a
  zip icon. Reports with a single PDF are marked with a PDF icon.

#### Configure the notification rule for a failed report

You can receive an email alert if a report fails to run due to a timeout
or fails to upload to the GCP bucket.

1.  Under Settings \> Configurations \> General \> Notifications, click
    **+ Add Forwarding Configuration**.

2.  Enter a name and a description for your rule, and under
    **Log Type**, select **Management Audit Logs**.

3.  Use a filter to select the **Type** as `Reporting`, **Subtype** as
    `Run Report`, and **Result** as **Fail**.

4.  Under **Distribution List**, select the email address to send the
    notification to.

5.  Click **Done**.

