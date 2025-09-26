## Web and API Security (WAAS)

### Overview

> **Note**
>
> Requires the Cortex Cloud Runtime Security add-on.

Cortex Web and API Security (WAAS) capabilities offer comprehensive
protection of APIs across integrated API gateways, web-based
applications, and APIs running on Linux-based workloads.

#### Use cases

- **API Visibility**: APIs are discovered through traffic mirroring and
  API Gateway logs. Cortex scans and collects metadata including
  domains, paths, HTTP methods, authentication types, protocol schemas
  (HTTP/HTTPS), and request/response content types. The source of
  discovery comes from analyzing these key elements.

- **Posture Management and Risk Insights**: WAAS assesses discovered
  APIs for internet exposure, sensitive data transmissions, weak
  authentication, lack of encryption, and specification drift. This
  evaluation provides critical posture management and risk insights to
  ensure the security of the APIs.

- **Threat Detection**: WAAS identifies API-specific threats, including
  SQL injection (SQLi), Cross-site scripting (XSS), CVE exploit
  attempts, authentication bypass, sensitive data leakage, bot and
  scanner activity, and traffic anomalies. This detection capability
  enhances threat identification and response measures for safeguarding
  APIs. Refer to
  [/document/preview/1415560#UUID-13bd923f-f8de-c189-d9a0-7bc721c68c8c](/document/preview/1415560#UUID-13bd923f-f8de-c189-d9a0-7bc721c68c8c)
  for more information on the threats.

#### Deployment options

WAAS is available through the following deployment options:

- **Agentless integration through API gateways** (AWS API Gateway, Azure
  APIM, GCP Apigee, Kong, F5):

<!-- -->

- Cortex XSIAM offers agentless in-depth scans, thorough analysis, and
  timely alerts to detect and mitigate security risks and potential
  vulnerabilities effectively. It enhances the security of your APIs in
  Apigee, Azure, and AWS by integrating with Cortex API Security for
  complete protection against threats.

  Refer to [Secure your API
  landscape](#UUID639c5a747ceafd3beddd97a765cf5758) for more information
  about scanning your API sources of data and addressing issues, cases,
  and findings.

<!-- -->

- **Agent-based protection (Beta)**, through lightweight agents on
  workloads:

<!-- -->

- Web and API Security profiles provide comprehensive real-time
  detection and protection for web-based applications and APIs running
  on Linux-based workloads. These profiles can be applied to policies
  for such workloads. These agent-based capabilities are offered as a
  Beta feature.

  Refer to [Agent-based
  protection](#UUID88b70739c01d406cbbf7ee6b3b1b55a7) for more
  information about setting up profiles and policies.

#### User roles and permissions

Cortex API security includes three main roles that are responsible for
ensuring the security of the API landscape in the organization.

> **Note**
>
> Verify API security configurations for relevant users and roles.

- **SOC analyst**: The Security Operations Center (SOC) team is
  responsible for live threat detection, investigation, and response.
  They continuously monitor, prioritize, and analyze security incidents,
  investigating the scope and context of attacks to determine if they
  are legitimate threats and deciding on appropriate actions such as
  prevention, remediation, or classifying them as normal activity.

- **Security practitioner**: A security team\'s role involves
  understanding the environment, its assets, and its security posture to
  assess and monitor risks. They define and enforce security policies,
  collect items requiring fixes, and collaborate with development and
  operations teams to remediate vulnerabilities and track outstanding
  risks, ensuring timely resolution.

- **Workload owner**: Application owners are responsible for building
  and modifying their applications, and they need to understand what is
  required to align their assets and API endpoints with established
  security standards. Their goal is to apply necessary fixes to achieve
  a consistent and secure posture.

### Personas workflow

The workflow outlines the responsibilities of each persona to detect,
assess, protect, and secure the API assets across the organization,
focusing on the main API security elements:

- Visibility

- Posture Management & Risk Profiling

- Threat Detection & Response

#### SOC analyst

**Responsibility**: Real-time threat detection & response

The SOC analyst is the key to identifying and investigating API
vulnerabilities and attacks within an organization.

**Steps**:

1.  **Visibility**: Reviews the **Cases & Issues** module for new
    attacks.

2.  **Investigate**: Select a case or an issue, analyze involved APIs
    and their context, analyze request/response details, and distinguish
    normal from malicious activity.

3.  **Decide and Act**: Determine if it\'s a true attack. If so,
    initiate an immediate response (often outside the UI) and flag for
    fixes. Close the case in the UI.

#### Security practitioner

**Responsibility**: Proactive posture management & risk reduction

The security practitioner uses the UI for continuous risk assessment and
orchestration of remediation.

**Steps**:

1.  **Overview of API landscape**: In the **API Security Management**
    dashboard, review emerging threats and understand the overall
    security of the API landscape.

2.  **Analyze APIs and Risks**: Navigate to API endpoints to view all
    APIs, their risk factors (e.g., internet exposure, sensitive data,
    authentication/encryption status), and posture issues. Drill down
    for details.

3.  **Manage OpenAPI Specifications**: Access the OpenAPI specification
    files. Review findings on the specification file itself
    (misconfigurations) and verify API traffic conformance to its
    specification.

4.  **Assign Remediation**: Consolidate all findings, group them by
    application owner, and distribute tasks (via email/tickets with
    timelines) for fixes (code, gateway, specification updates).

#### Workload owner

**Responsibility**: Application security accountability

The workload owner acts on security tasks, primarily outside the UI.

**Steps**:

1.  **Receive Tasks**: Get detailed security tasks and timelines from
    the security practitioner.

2.  **Implement Fixes**: Apply necessary fixes to application code, API
    configurations, or OpenAPI specifications.

3.  **Ensure Compliance**: Bring their APIs and assets into alignment
    with security standards.

### Secure your API landscape

Integrate Cortex XSIAM with your API Gateway (AWS, Azure, GCP, Kong, or
F5) to scan traffic and analyze logs. With Cortex XSIAM, use the API
security features to monitor, manage, and enforce security policies
across the integrated API gateways. In addition, the API specification
can validate live traffic against specifications and alert on surface
deviations, undocumented endpoints, or security gaps.

Refer to the relevant section for more information:

- [API visibility and risk
  assessment](#UUID6ca0d29dd0bbe838091e9df0176115f5)

- [Monitor and investigate API
  threats](#UUID980c3537eb02a629eed87284ea892b11)

- [Configure API security from end to
  end](#UUIDcb3b73b776bed8e71207c31cef764378)

- [API specification inventory](#UUIDba0a0cfb866f52895ec84a57076638bd)

#### API visibility and risk assessment

Cortex\'s in-depth analysis of API traffic provides extensive visibility
and control, enabling continuous discovery of all APIs, real-time
detection of threats and anomalies, and proactive identification of
vulnerabilities like shadow APIs or misconfigurations. This
comprehensive monitoring empowers security teams to quickly respond to
attacks, ensure compliance, and strengthen their overall API security
posture across the entire digital landscape.

Cortex XSIAM API endpoints provide an overview of the API assets across
cloud providers and data sources (for example: API Gateway, API
specification), enabling you to analyze, assess, and implement security
measures to safeguard against security risks and potential
vulnerabilities.

At a glance, we see a graphical representation of the APIs per cloud
provider, including on-prem, and APIs per discovery source, including
XDR agent.

You can filter in by provider or by discovery source.

![](media/rId4410.png){width="5.833333333333333in"
height="0.9916666666666667in"}

The following table lists the fields that are available for each API
endpoint.

+-----------------------------------+---------------------------------------------------------+
| Field                             | Description                                             |
+===================================+=========================================================+
| Server                            | Hosting server of the API.                              |
+-----------------------------------+---------------------------------------------------------+
| Path                              | API endpoint path is used by applications to            |
|                                   | communicate with the server, enabling you to access     |
|                                   | data and execute actions.                               |
+-----------------------------------+---------------------------------------------------------+
| API Category                      | Associated category of the API. For example, **Login**, |
|                                   | **Checkout**, and **Add credit card**.                  |
+-----------------------------------+---------------------------------------------------------+
| HTTP method                       | HTTP method used for the API call. For example, GET,    |
|                                   | DELETE, CONNECT.                                        |
+-----------------------------------+---------------------------------------------------------+
| Risk factors                      | Risk type associated with the API. Some examples of     |
|                                   | risk type include:                                      |
|                                   |                                                         |
|                                   | - Internet Exposure                                     |
|                                   |   (![](media/rId4413.png){width="0.21577318460192477in" |
|                                   |   height="0.20833333333333334in"})                      |
|                                   |                                                         |
|                                   | - Sensitive Data                                        |
|                                   |   (![](media/rId4416.png){width="0.23437445319335082in" |
|                                   |   height="0.20833333333333334in"})                      |
|                                   |                                                         |
|                                   | - No Authentication                                     |
|                                   |   (![](media/rId4419.png){width="0.20833333333333334in" |
|                                   |   height="0.20833333333333334in"})                      |
|                                   |                                                         |
|                                   | - No Encryption                                         |
|                                   |   (![](media/rId4422.png){width="0.22569444444444445in" |
|                                   |   height="0.20833333333333334in"})                      |
+-----------------------------------+---------------------------------------------------------+
| API spec name                     | API specification name is obtained from the `title`     |
|                                   | field of the specification imported to Cortex XSIAM.    |
+-----------------------------------+---------------------------------------------------------+
| API spec conformance              | Indicates if the endpoint was found/not found in the    |
|                                   | specification.                                          |
|                                   |                                                         |
|                                   | - **Undefined**: Indicates that the endpoint from the   |
|                                   |   gateway is not found in any known specification       |
|                                   |   document.                                             |
|                                   |                                                         |
|                                   | - **Match**: Indicates there\'s a match between the API |
|                                   |   path of the endpoint and a specification.             |
|                                   |                                                         |
|                                   | - **Mismatch**: Indicates that the API path is the same |
|                                   |   in the endpoint and specification, but there is a     |
|                                   |   missing query parameter in the specification.         |
|                                   |                                                         |
|                                   | - **Conflict**: Indicates when the API endpoint matches |
|                                   |   more than one API specification file.                 |
+-----------------------------------+---------------------------------------------------------+
| Provider                          | Gateway provider of the API.                            |
+-----------------------------------+---------------------------------------------------------+
| Source                            | The source from which the data was obtained.            |
|                                   |                                                         |
|                                   | Configuration                                           |
|                                   | ![](media/rId4425.png){width="0.29017825896762905in"    |
|                                   | height="0.20833333333333334in"}: Indicates that the     |
|                                   | source is from the API specification.                   |
+-----------------------------------+---------------------------------------------------------+
| Inspected                         | Number of requests or connections that have been        |
|                                   | analyzed and verified by Cortex XSIAM.                  |
+-----------------------------------+---------------------------------------------------------+
| Request/Response Sensitive Data   | Shows the sensitive data type in the request/response,  |
|                                   | such as passwords, credit card numbers, SSNs, or bank   |
|                                   | account numbers. Refer to [What is Cortex Cloud Data    |
|                                   | Classification?](#UUID774b12bc81879542ebb9d7bf17a73ec9) |
|                                   | for more information.                                   |
|                                   |                                                         |
|                                   | > **Note**                                              |
|                                   | >                                                       |
|                                   | > Data classification findings are only available for   |
|                                   | > enabled profiles.                                     |
+-----------------------------------+---------------------------------------------------------+
| Request/Response Content Types    | Data format sent/received in the request/response of    |
|                                   | the API calls. For example, application/json;           |
|                                   | application/xml.                                        |
+-----------------------------------+---------------------------------------------------------+
| Schema                            | Protocol used (HTTP/HTTPS) to access the API resource.  |
+-----------------------------------+---------------------------------------------------------+
| Authentication Types              | Authentication method used by the API. The list         |
|                                   | includes:                                               |
|                                   |                                                         |
|                                   | - API key                                               |
|                                   |                                                         |
|                                   | - Basic                                                 |
|                                   |                                                         |
|                                   | - OAuth                                                 |
|                                   |                                                         |
|                                   | - OIDC                                                  |
|                                   |                                                         |
|                                   | - Learning                                              |
|                                   |                                                         |
|                                   | <!-- -->                                                |
|                                   |                                                         |
|                                   | - > **Note**                                            |
|                                   |                                                         |
|                                   |   > Indicates that a JSON Web Token was identified, but |
|                                   |   > it is unknown how to determine its type from the    |
|                                   |   > given string. It could be a non-standard JSON Web   |
|                                   |   > Token creation algorithm.                           |
|                                   |                                                         |
|                                   | <!-- -->                                                |
|                                   |                                                         |
|                                   | - Unknown: Indicates that the authentication method     |
|                                   |   couldn\'t be identified.                              |
|                                   |                                                         |
|                                   | - Authentication not detected: Indicates that the API   |
|                                   |   does not require authentication.                      |
+-----------------------------------+---------------------------------------------------------+
| Discovery Method                  | Based on asset discovery. The list includes:            |
|                                   |                                                         |
|                                   | - HTTP                                                  |
|                                   |                                                         |
|                                   | - Logs                                                  |
|                                   |                                                         |
|                                   | - Traffic mirroring                                     |
|                                   |                                                         |
|                                   | - Configuration                                         |
|                                   |                                                         |
|                                   | - Unknown                                               |
+-----------------------------------+---------------------------------------------------------+
| Asset Status                      | The API\'s status is **Active** only when both an API   |
|                                   | gateway and an API specification are present;           |
|                                   | otherwise, it\'s deleted. An **Inactive** status means  |
|                                   | the endpoint is defined in the specification but isn\'t |
|                                   | receiving traffic via the gateway.                      |
+-----------------------------------+---------------------------------------------------------+
| Cloud                             | Cloud provider where the agent is running. In case of   |
|                                   | on-prem, this field shows **On-Prem**.                  |
+-----------------------------------+---------------------------------------------------------+
| Provider Type                     | Indicates the cloud service provider: CSP or On Prem.   |
+-----------------------------------+---------------------------------------------------------+
| Region                            | Region of the hosting server.                           |
+-----------------------------------+---------------------------------------------------------+

When clicking on a specific API endpoint, a side card opens. Each tab
includes detailed information as described.

##### Overview

Shows the highlights and properties of the API endpoint.

+-----------------------------------+--------------------------------------------------------------------------------+
| Field                             | Description                                                                    |
+===================================+================================================================================+
| Asset ID                          | UAI (Unified Asset Inventory) ID                                               |
+-----------------------------------+--------------------------------------------------------------------------------+
| Asset Category                    | Either **API Endpoint** or **API Specification**.                              |
+-----------------------------------+--------------------------------------------------------------------------------+
| Cloud Region                      | Region of the cloud provider.                                                  |
+-----------------------------------+--------------------------------------------------------------------------------+
| Asset Groups                      | Assigned asset groups to the API endpoint.                                     |
+-----------------------------------+--------------------------------------------------------------------------------+
| Account ID                        | Cloud account ID.                                                              |
+-----------------------------------+--------------------------------------------------------------------------------+
| Cases/Issues/Findings             | The link from the number opens the page where you can review the details.      |
|                                   | Refer to                                                                       |
|                                   | [#UUID78f2bdc35db231bedec98cace6573b65](#UUID78f2bdc35db231bedec98cace6573b65) |
|                                   | for detailed information.                                                      |
|                                   |                                                                                |
|                                   | You can view all API security issues and cases detected by Cortex XSIAM.       |
+-----------------------------------+--------------------------------------------------------------------------------+
| **Related Assets**                |                                                                                |
|                                   |                                                                                |
| Shows the data from the source of |                                                                                |
| the traffic.                      |                                                                                |
|                                   |                                                                                |
| - If the source of the traffic is |                                                                                |
|   from the gateway, the related   |                                                                                |
|   asset data shows AWS API        |                                                                                |
|   Gateway or Azure Gateway, the   |                                                                                |
|   name of the gateway, and the    |                                                                                |
|   stage.                          |                                                                                |
|                                   |                                                                                |
| - If the source of the traffic is |                                                                                |
|   from a specification from the   |                                                                                |
|   gateway, the related asset data |                                                                                |
|   shows the API specification,    |                                                                                |
|   the name of the specification,  |                                                                                |
|   and the gateway provider.       |                                                                                |
|                                   |                                                                                |
| - If the source of the traffic is |                                                                                |
|   from the XDR agent, the related |                                                                                |
|   asset data shows the agent ID.  |                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------+
| Type                              | API specification                                                              |
+-----------------------------------+--------------------------------------------------------------------------------+
| Name                              | Name of the API specification.                                                 |
+-----------------------------------+--------------------------------------------------------------------------------+
| Provider                          | Cloud provider of the API specification.                                       |
+-----------------------------------+--------------------------------------------------------------------------------+

An issue is generated when the following **Detection Method** is
triggered:

+-----------------------+-----------------------+-----------------------+
| Deployment option     | Detection Method and  | Description           |
|                       | Type                  |                       |
+=======================+=======================+=======================+
| Agentless for Posture | **Detection Method**: | If Cortex XSIAM       |
|                       | API Posture Scanner   | detects security      |
|                       |                       | vulnerabilities or    |
|                       |                       | compliance issues in  |
|                       |                       | the posture of an API |
|                       |                       | during scanning, an   |
|                       |                       | issue is generated.   |
+-----------------------+-----------------------+-----------------------+
| Agentless             | **Detection Method**: | If Cortex XSIAM       |
|                       | API Traffic Scanner   | detects anomalies,    |
|                       |                       | suspicious            |
|                       |                       | activities, or        |
|                       |                       | potential security    |
|                       |                       | threats in the        |
|                       |                       | network traffic of    |
|                       |                       | the APIs, an issue is |
|                       |                       | generated.            |
+-----------------------+-----------------------+-----------------------+
| Agent-based           | **Type**: Security    | If Cortex XSIAM       |
|                       |                       | detects threats from  |
|                       | **Detection Method**: | cloud workloads, an   |
|                       | XDR Agent             | issue is generated.   |
+-----------------------+-----------------------+-----------------------+

##### Endpoint Data

Shows the details of the API endpoint, and the components associated
with authentication, such as token type, request/response body schema,
and usage statistics.

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| API Endpoint                      | API endpoint path used by         |
|                                   | applications to communicate with  |
|                                   | the server, enabling you to       |
|                                   | access data and execute actions.  |
+-----------------------------------+-----------------------------------+
| Method                            | HTTP Method.                      |
+-----------------------------------+-----------------------------------+
| Server                            | Hosting server of the API.        |
+-----------------------------------+-----------------------------------+
| Query Parameters                  | Parameters included in the API    |
|                                   | endpoint URL. Only the keys are   |
|                                   | stored to avoid saving personal   |
|                                   | identifiable information (PII)?   |
|                                   | For example, ID.                  |
+-----------------------------------+-----------------------------------+
| Response Content Type             | Specifies the response type       |
|                                   | format transmitted from the       |
|                                   | server to the client, such as     |
|                                   | JSON or XML.                      |
+-----------------------------------+-----------------------------------+
| Inspected Transactions            | Number of requests scanned by     |
|                                   | Cortex XSIAM.                     |
+-----------------------------------+-----------------------------------+
| First Observed/Last Observed      | Timestamp of the first and last   |
|                                   | time the API was accessed.        |
+-----------------------------------+-----------------------------------+
| Last Changed                      | Timestamp of when the API was     |
|                                   | updated.                          |
+-----------------------------------+-----------------------------------+
| Sensitive Data Pattern            | Identifies sensitive data         |
|                                   | exposure risks.                   |
+-----------------------------------+-----------------------------------+
| Authentication                    | Specified the authentication of   |
|                                   | the API endpoint. Refer to        |
|                                   | Authentication Types.             |
+-----------------------------------+-----------------------------------+
| Response Body Schema              | Shows the structure and format of |
|                                   | the data that\'s included in the  |
|                                   | response. It shows expected data  |
|                                   | types, format, and organization   |
|                                   | of the response payload, such as  |
|                                   | the fields, attributes, and valid |
|                                   | values.                           |
|                                   |                                   |
|                                   | The body is not saved (to avoid   |
|                                   | saving PII). The schema is        |
|                                   | created based on the              |
|                                   | request/response.                 |
+-----------------------------------+-----------------------------------+
| Usage Statistics                  | Shows the metrics for             |
|                                   | **Requests size distribution**,   |
|                                   | **Response size distribution**,   |
|                                   | and **Status code distribution**. |
|                                   | Using these statistics can help   |
|                                   | assess usage patterns, identify   |
|                                   | performance issues, and help      |
|                                   | optimize the API to enhance its   |
|                                   | security posture.                 |
|                                   |                                   |
|                                   | You can hover over the metric bar |
|                                   | to view details.                  |
+-----------------------------------+-----------------------------------+

#### Monitor and investigate API threats

Cortex XSIAM provides a comprehensive solution to counter API threats
and attacks. It doesn\'t just address vulnerabilities, but actively
protects against the misuse of legitimate API functions, mitigates risks
from misconfigurations, and secures often-forgotten \"shadow\" or
\"zombie\" APIs. By offering continuous visibility and monitoring,
Cortex XSIAM ensures robust, proactive protection for all your APIs,
safeguarding your organization against evolving and sophisticated
threats.

Cortex XSIAM protects from the following threats:

+-----------------------------------+-----------------------------------+
| Module                            | Threat description                |
+===================================+===================================+
| Advanced Threat Protection        | Advanced Threat Protection (ATP)  |
|                                   | is a comprehensive security       |
|                                   | feature designed to detect,       |
|                                   | prevent, and respond to           |
|                                   | sophisticated Web and API         |
|                                   | threats, ensuring robust          |
|                                   | protection for workloads against  |
|                                   | evolving risks.                   |
+-----------------------------------+-----------------------------------+
| Authentication bypass             | The Cortex XSIAM authentication   |
|                                   | bypass module protects against    |
|                                   | attacks that attempt to           |
|                                   | circumvent authentication         |
|                                   | controls through session          |
|                                   | manipulation, token exploitation, |
|                                   | or credential abuse.              |
+-----------------------------------+-----------------------------------+
| Automation tools                  | Cortex XSIAM detects and protects |
|                                   | against automated tools or        |
|                                   | services that scrape website      |
|                                   | contents such as Scriptable       |
|                                   | headless web browsers, command    |
|                                   | line tools, or HTTP libraries.    |
+-----------------------------------+-----------------------------------+
| Cross-Site Scripting (XSS)        | Cortex XSIAM protects against XSS |
| injection                         | attacks, in which malicious       |
|                                   | JavaScript snippets are injected  |
|                                   | into otherwise benign and trusted |
|                                   | websites. In such attacks,        |
|                                   | attackers try to trick the        |
|                                   | browser into switching to a       |
|                                   | JavaScript context and executing  |
|                                   | arbitrary code.                   |
+-----------------------------------+-----------------------------------+
| CVE exploits                      | Cortex XSIAM protects against     |
|                                   | exploitation attempts of known    |
|                                   | vulnerabilities (Common           |
|                                   | Vulnerabilities and Exposures     |
|                                   | (CVEs)).                          |
+-----------------------------------+-----------------------------------+
| Malformed Traffic                 | Cortex XSIAM identifies and       |
|                                   | protects against HTTP requests    |
|                                   | with anomalies that are not       |
|                                   | expected from common web          |
|                                   | browsers.                         |
+-----------------------------------+-----------------------------------+
| Injection attacks                 | Injection attacks are a form of   |
|                                   | attacks in which attackers        |
|                                   | attempt to insert malicious input |
|                                   | into an application to manipulate |
|                                   | its execution. For example, a     |
|                                   | code injection attack injects     |
|                                   | code which is interpreted by the  |
|                                   | application or other runtimes.    |
|                                   | Command and code payloads can     |
|                                   | either be injected as part of     |
|                                   | HTTP requests, or are included    |
|                                   | from local or remote files (also  |
|                                   | known as File Inclusion attacks). |
+-----------------------------------+-----------------------------------+
| Known bots                        | Cortex XSIAM can identify         |
|                                   | legitimate bots that properly     |
|                                   | declare their identity and        |
|                                   | purpose, such as search engine    |
|                                   | crawlers and authorized web       |
|                                   | indexers. These bots follow       |
|                                   | standard protocols and provide    |
|                                   | verifiable operator information,  |
|                                   | however some of them might cause  |
|                                   | undesirable behaviors, such as    |
|                                   | spam, and you might prefer to     |
|                                   | block such bots.                  |
+-----------------------------------+-----------------------------------+
| Offensive tools                   | Cortex XSIAM identifies offensive |
|                                   | tools that scan web applications  |
|                                   | for known security                |
|                                   | vulnerabilities and               |
|                                   | misconfiguration, and exploit     |
|                                   | them.                             |
+-----------------------------------+-----------------------------------+
| Sensitive data exposure           | Cortex XSIAM protects workloads   |
|                                   | from providing responses that     |
|                                   | could expose sensitive data found |
|                                   | in critical system files,         |
|                                   | including password hashes         |
|                                   | (/etc/shadow), user account       |
|                                   | information (/etc/password), and  |
|                                   | private encryption keys.          |
|                                   |                                   |
|                                   | Such examples would be            |
|                                   | compromised accounts, credential  |
|                                   | stuffing, and ATO attacks.        |
+-----------------------------------+-----------------------------------+
| SQL injection (SQLi)              | Cortex XSIAM protects against     |
|                                   | SQLi attacks, which can occur     |
|                                   | when an attacker successfully     |
|                                   | inserts a malicious SQL query     |
|                                   | into the input fields of a web    |
|                                   | application. A successful attack  |
|                                   | can read sensitive data from the  |
|                                   | database, modify data in the      |
|                                   | database, or run arbitrary        |
|                                   | commands.                         |
+-----------------------------------+-----------------------------------+
| Identity-based attacks            | Cortex XSIAM identifies and       |
|                                   | protects from compromised         |
|                                   | accounts, credential stuffing,    |
|                                   | and ATO attacks. These types of   |
|                                   | attacks involve exploiting stolen |
|                                   | or weak login credentials to      |
|                                   | impersonate legitimate users and  |
|                                   | gain unauthorized access to       |
|                                   | accounts and systems.             |
|                                   |                                   |
|                                   | The API inventory\'s category by  |
|                                   | type (e.g., login, sign-in,       |
|                                   | sign-up, register, create         |
|                                   | account, reset password) and      |
|                                   | sub-type (e.g., add to cart, show |
|                                   | cart, general checkout page, add  |
|                                   | billing address, add credit card, |
|                                   | gift card) is crucial. This       |
|                                   | enables a deeper investigation    |
|                                   | into potential discrepancies      |
|                                   | related to identity-based         |
|                                   | attacks.                          |
+-----------------------------------+-----------------------------------+

##### SOC analyst workflow

The following workflow outlines a step-by-step action plan as a SOC
analyst to monitor, investigate, and respond to API threats.

**SOC analyst role overview**

SOC analysts continuously monitor and analyze security incidents related
to APIs. Their goal is to identify, investigate, and mitigate API
endpoint attacks, ensuring API integrity, confidentiality, and
availability. They prioritize issues based on severity and specific
indicators.

- ISSUE DOMAIN: Security

- DETECTION METHOD: API Traffic Monitor

- SEVERITY: High or Critical

**SOC analyst action plan**

The following outlines the streamlined actions a SOC analyst takes when
detecting an API threat:

**Step 1: Initial Examination (Cases & Issues) **

- **Objective**: Quickly assess the type and severity of the API attack.

- **Actions**: Navigate to **Issues**, filter by key indicators, and
  review the high-level alert summary (timestamp, affected service,
  initial notes).

**Step 2: In-depth analysis (Issue page - Overview tab)**

- **Objective**: Gather detailed attack context, identify affected
  assets, and collect evidence.

- **Actions**:

  - **Affected Assets**: Identify targeted API endpoints; click to
    navigate to their detailed pages for granular review.

  - **Evidence**: Examine findings (request/response logs, payload,
    timestamps, source IP, user agent) to understand the attack vector.

![](media/rId4431.png){width="5.833333333333333in"
height="4.272916666666666in"}

**Step 3: Refer to [API visibility and risk
assessment](#UUID6ca0d29dd0bbe838091e9df0176115f5) for drilled-down details of the API data. **

**Step 4: Post-Investigation Actions & Reporting**

- **Objective**: Mitigate the threat, prevent recurrence, and document
  findings.

- **Actions**:

  - **Reporting**: Create a detailed incident report (detection, attack
    type, assets, evidence, vulnerabilities, actions, lessons learned).
    Communicate findings to stakeholders.

  - **Improvement**: Conduct post-incident review, update
    policies/playbooks, and recommend security enhancements.

#### Configure API security from end to end

Implementing end-to-end API security means establishing comprehensive
protection across the entire API lifecycle. This process begins by
integrating with third-party cloud providers to enable thorough scanning
of your APIs for threats and vulnerabilities. Following this, you\'ll
configure profiles for agent-based protection, which actively safeguards
your APIs in real-time. This ensures that every potential vulnerability,
from authentication and authorization issues to data encryption and
threat monitoring, is addressed across your entire API ecosystem.

For more information on how to configure, refer to:

- [Third-party API security
  integrations](#UUID1a904a674e66e83fb174253099bb9a65)

- [Agent-based protection](#UUID88b70739c01d406cbbf7ee6b3b1b55a7)

##### Third-party API security integrations

Easily configure the settings in both Cortex XSIAM and your cloud
service to retrieve and collect API data for further analysis by
Cortex\'s comprehensive [API
security](#UUID6ca0d29dd0bbe838091e9df0176115f5) capabilities, which
provide a transparent view of API traffic, helping to identify potential
security threats.

###### Ingest AWS API Gateway

Integrate AWS API Gateway with Cortex XSIAM to begin scanning the APIs
for potential threats and vulnerabilities.

Settings in Cortex XSIAM

In Cortex XSIAM, set up the **AWS API Gateway** data source to integrate
with the AWS API Gateway.

1.  From Settings \> Data Sources , click
    ![](media/rId4436.png){width="0.9668799212598426in"
    height="0.20833333333333334in"} and search for **AWS API Gateway**
    and then click **Connect** or **Connect Another Instance**.

2.  In the **AWS API Collector** wizard, enter a relevant name and click
    **Create and Proceed**.

3.  Copy the key and save it for later.

- > **Note**

  > You must generate a new key if you did not save.

4.  Click **Close**.

5.  An instance is created for the data source. Click
    ![](media/rId4439.png){width="0.2646391076115486in"
    height="0.20833333333333334in"} (Copy API URL) to establish a
    connection when setting up AWS API Gateway.

####### Settings in AWS Management Console

Configure the settings in the AWS Management Console to integrate with
Cortex XSIAM:

1.  Log in to the [AWS Management
    Console](https://aws.amazon.com/console/).

2.  In AWS Management Console, navigate to **API Gateway**.

    a.  Expand the left-hand menu of the API project.

    b.  Go to Settings \> Logging and click **Edit**. Verify that the
        **CloudWatch log role ARN** is filled.

    c.  Click **Stages** and from **Stages**, select the relevant stage.

    d.  From **Logs and Tracing**, click **Edit** and configure the
        following:

        - **CloudWatch Logs**: Select **Errors and info logs**

        - Select **Data tracing**

        - Select **Detailed metrics**

    e.  Click **Save**.

    - This creates a unique log group inside CloudWatch.

3.  Open CloudWatch in another window by typing **CloudWatch** in the
    search bar.

    a.  Go to Logs \> Log groups and search for the log group just
        created.

    - The group name follows the following format:
      `“API-Gateway-Execution-Logs_<gw ID>/<stage name>”`

    b.  Click the log group, and from the **Log group details**, copy
        the **ARN**.

4.  Return to **Edit logs and tracing**, go to
    **enable the custom access logging** , and paste the ARN without the
    \* in the **Access log destination ARN** field.

- ARN:
  `arn:aws:logs:us-east-1:123456789012:log-group:API-Gateway-Execution-Logs_153tp249k2/Prod:*`

  Paste in **Access log destination ARN**:
  `arn:aws:logs:us-east-1:123456789012:log-group:API-Gateway-Execution-Logs_153tp249k2/Prod`

5.  In **Log format**, type the following and click **Save**:

- ($context.requestId) accountId: $context.accountId; requestTime: $context.requestTime; path: $context.path

6.  Open Firehose in another window by typing **Firehose** in the search
    bar.

    a.  Configure the following:

        - **Source**: **Direct PUT**

        - **Destination**: **HTTP Endpoint**

        - **Firehose stream name**: Add a relevant name.

    b.  In **Destination settings**, configure the following:

        - **HTTP endpoint URL** : Add the API URL from Cortex XSIAM.

        - **Authentication**: Select **Use access key**.

        - **Access key**: Paste the generated token from
          **AWS API Gateway**.

        - **Content encoding**: Select **GZIP**.

    c.  In **Backup settings**, configure the following:

        - **Source record backup in Amazon S3**: select
          **Failed date only**.

        - **S3 backup bucket**: select a bucket or enter a bucket URI.

    d.  Click **Create**.

    - It takes up to 5 minutes for the stream to be activated.

7.  Refer to [Subscription filters with Amazon Data
    Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#FirehoseExample).
    To create an IAM Role and provide CloudWatch with the appropriate
    permissions for the streaming, refer to steps 8-12.

- aws logs put-subscription-filter \
          --log-group-name "<YOUR_LOG_GROUP_NAME>" \
          --filter-name "<any_filter_name>" \
          --filter-pattern "" \
          --destination-arn "arn:aws:firehose:region:123456789012:deliverystream/<YOUR_DELIVERY_STREAM>" \
          --role-arn "arn:aws:iam::<ACCOUNT_ID>:role/<YOUR_IAM_ROLE>"

  > **Important**

  > Leave `–filter-pattern` empty as displayed above.

  After the Data Firehose delivery stream is active and you have created
  the IAM role, you can create the CloudWatch Logs subscription filter.
  The subscription filter immediately starts the flow of real-time log
  data from the chosen log group to your Amazon Data Firehose delivery
  stream.

  After you create the filter, go back to Data Sources \> AWS API
  Gateway to see the logs starting to come in.

  > **Note**

  > If no logs are showing, send some API requests on Postman or CURL.

###### Ingest Azure APIM

> **Note**
>
> Requires the Data Collection add-on.

Integrate Azure APIM with Cortex XSIAM to start scanning its APIs for
potential threats and vulnerabilities.

You need to set up a policy that enables you to customize the behavior
of managed APIs. You can configure the sending of HTTP request/response
data to Cortex XSIAM. The data is saved and analyzed by API security
modules, which provide information on the security risks associated with
the APIs.

> **Note**
>
> Microsoft Azure APIM service must be running before starting to
> configure the integration.

Settings in Cortex XSIAM

In Cortex XSIAM, set up the **Azure API Management** data source to
integrate with the Azure API Gateway.

1.  From Settings \> Data Sources , click
    ![](media/rId4436.png){width="0.9668799212598426in"
    height="0.20833333333333334in"} and search for
    **Azure API Management** and click **Connect** or
    **Connect Another Instance**.

2.  In the **APIM Collector** wizard, enter a relevant name and then
    click **Create and Proceed**.

3.  Copy the key and paste it somewhere so that you can access it for
    later.

- If you forget to record the key and close the window, you must
  generate a new key and repeat this process.

4.  Click **Close**.

5.  An instance is created for the data source. Click
    ![](media/rId4439.png){width="0.2646391076115486in"
    height="0.20833333333333334in"} (Copy API URL) to establish a
    connection when setting up Azure APIM.

####### Settings in Azure APIM policy

Configure an inbound and outbound policy to send HTTP traffic data of
the APIs to Cortex XSIAM. You can configure a policy for individual
operations (endpoints) or all operations of a single API.

Follow the steps to configure the policy.

1.  Log in to [Microsoft Azure](https://portal.azure.com/).

2.  Go to **API Management services** and select the relevant service.

3.  From the left-hand menu, select APIs \> Named values.

- > **Note**

  > From the URL, save the UUID and the resource group -
  > `/resource/subscriptions/<UUID>/resourceGroups/<ResourceGroup>`.

  > The UUID is the Azure account/subscription ID and the resource
  > group, which is the group where the APIM Service is defined.

4.  Configure the settings in each of the sections. Follow the steps in
    the order they are listed.

- > **Note**

  > Use the search to navigate to the specific section.

  **Named values**: Add the values:

  - cloud-account-id

    - **Type**: Plain

    - **Value**: The UUID you saved from the previous step.

  - cloud-resource-group

    - **Type**: Plain

    - **Value**: The resource group you saved from the previous step.

  - cortex-api-key

    - **Type**: Secret

    - **Value**: The token that you saved from data sources in Cortex.

  - cortex-api-url

    - **Type**: Plain

    - **Value**: The API URL from data sources in Cortex.

  - cortex-http-body-size-limit-bytes

    - **Type**: Plain

    - **Value**: 131072

    <!-- -->

    - > **Note**

      > 131072 bytes = 128 KB. This value determines the size (in bytes)
      > of request and response bodies to send to Cortex. Any bytes
      > beyond this limit are truncated.

  **APIs**: From the left-hand menu, go to APIs \> APIs.

  a.  You can create a policy on a specific API or choose to create a
      policy on all APIs.

  b.  From **Inbound Processing**, click
      ![](media/rId4454.png){width="0.2777777777777778in"
      height="0.20833333333333334in"}.

  - The Policies screen opens. There are three sections:

    - `<inbound>`

    - `<backend>`

    - `<outbound>`

    The `<inbound>` includes the request before it\'s sent to the
    `<outbound>`. The parameters are saved before they\'re sent.

    Add the following inside the `<inbound>`:

         <!-- Save the request body and headers to be sent to Cortex. This should always be placed at the very beginning of the inbound element. -->
                <set-variable name="requestBody" value="@((context.Request?.Body?.As<string>(preserveContent: true)) ?? string.Empty)" />
                <set-variable name="requestHeaders" value="@(JsonConvert.SerializeObject(context.Request.Headers))" />
                <!-- End of setting variables for sending to Cortex --><!-- Save the request body and headers to be sent to Cortex. This should always be placed at the very beginning of the inbound element. -->
                <set-variable name="requestBody" value="@((context.Request?.Body?.As<string>(preserveContent: true)) ?? string.Empty)" />
                <set-variable name="requestHeaders" value="@(JsonConvert.SerializeObject(context.Request.Headers))" />
                <!-- End of setting variables for sending to Cortex -->

    > **Note**

    > If any other inbound policies should be added, they must be added
    > after these elements.

    The `<outbound>` includes the request before it returns a response.

    Add the following inside the \<outbound\> element, at the end, after
    the other child elements:

        <!-- Send data to Cortex. This should always be placed at the very end of the outbound element. -->
                <send-request mode="new" response-variable-name="mirrorMessage">
                    <set-url>{{cortex-api-url}}</set-url>
                    <set-method>POST</set-method>
                    <set-header name="Content-Type" exists-action="override">
                        <value>application/json</value>
                    </set-header>
                    <set-header name="Authorization" exists-action="override">
                        <value>{{cortex-api-key}}</value>
                    </set-header>
                    <set-body>@{
                                string requestBody = context.Variables.GetValueOrDefault<string>("requestBody");
                                string responseBody = context.Response.Body.As<string>(preserveContent: true);
                                int bodySizeLimit = {{cortex-http-body-size-limit-bytes}};
                                bool requestBodySizeExceedsLimit = requestBody.Length > bodySizeLimit;
                                bool responseBodySizeExceedsLimit = responseBody.Length > bodySizeLimit;

                                return JsonConvert.SerializeObject(new {
                                    // Resource information
                                    subscriptionID          = "{{cloud-account-id}}",
                                    resourceGroup           = "{{cloud-resource-group}}",
                                    serviceID               = context.Deployment.ServiceId,
                                    region                  = context.Deployment.Region,
                                    apiID                   = context.Api.Id,
                                    apiRevision             = context.Api.Revision,
                                    // Request information
                                    requestID               = context.RequestId,
                                    url                     = context.Request.OriginalUrl,
                                    httpMethod              = context.Request.Method,
                                    requestBody             = requestBodySizeExceedsLimit ? requestBody.Substring(0, bodySizeLimit) : requestBody,
                                    requestBodyTruncated    = requestBodySizeExceedsLimit,
                                    requestHeaders          = JsonConvert.DeserializeObject(context.Variables.GetValueOrDefault<string>("requestHeaders")),
                                    timestamp               = new DateTimeOffset(context.Timestamp).ToUnixTimeMilliseconds(),
                                    requestIpAddress        = context.Request.IpAddress,
                                    statusCode              = context.Response.StatusCode,
                                    responseBody            = responseBodySizeExceedsLimit ? responseBody.Substring(0, bodySizeLimit) : responseBody,
                                    responseBodyTruncated   = responseBodySizeExceedsLimit,
                                    responseHeaders         = context.Response.Headers,
                                });
                            }
                    </set-body>
                </send-request>
                <!-- End of sending data to Cortex -->

    > **Important**

    > If you want to add additional data to the \<outbound\>, add it at
    > the start of the \<outbound\> code.

  c.  Click **Save**. Your APIM traffic collection is now configured.

  - Request and response data for the configured endpoints are sent to
    Cortex XSIAM for inspection by API security modules.

5.  Go to **Azure API Management** data source to validate that data is
    ingested from Azure APIM.

6.  Do the following to remove the integration of Azure APIM with Cortex
    XSIAM:

    - Remove the snippets you added to the policies.

    - Remove the named values from the API service.

    - Delete the HTTP log collector from Data Sources in Cortex.

###### Ingest Apigee Proxy

> **Note**
>
> Requires the Data Collection add-on.

Integrate Apigee Proxy with Cortex XSIAM to begin scanning the APIs for
potential threats and vulnerabilities.

The integration uses the Apigee's JavaScript (JS) policy, implemented
within a shared flow and deployed as a pre-proxy and post-proxy
flow-hook in selected environments. The JS policy is designed to capture
both request and response data from all traffic entering and exiting the
proxy.

Settings in Cortex XSIAM

In Cortex XSIAM, set up the **Apigee** data source to integrate with the
Apigee Gateway.

1.  From Settings \> Data Sources , click
    ![](media/rId4436.png){width="0.9668799212598426in"
    height="0.20833333333333334in"} and search for **Apigee** and click
    **Connect** or **Connect Another Instance**.

2.  In the **Apigee Collector** wizard, enter a relevant name and then
    click **Create and Proceed**.

3.  Copy the key and paste it somewhere so that you can access it for
    later.

- If you forget to record the key and close the window, you must
  generate a new key and repeat this process.

4.  Click the **Download Configuration Script** link to download the
    plugin, which you can then upload to the Apigee Gateway.

5.  Click **Close**.

6.  An instance is created for the data source. Click
    ![](media/rId4439.png){width="0.2646391076115486in"
    height="0.20833333333333334in"} (Copy API URL) to establish a
    connection when setting up Apigee Gateway.

First, download the resource file and then select the method to set up
the integration with Apigee.

####### Run an automated script to deploy configurations to Apigee

Use the script for full deployment (with or without connecting a flow
hook).

> **Note**
>
> The steps include the prerequisites that run the automated script that
> deploys files and configurations to Apigee. For manual configuration,
> refer to the section [Manual
> deployment](#bridgeheadidm113485995730202).

1.  Check that the GCP user running the script has `IAM` permissions.

- apigee.resourcefiles.list
      apigee.resourcefiles.create
      apigee.resourcefiles.update
      apigee.sharedflows.get
      apigee.sharedflows.create
      apigee.deployments.create
      apigee.sharedflowrevisions.deploy
      apigee.flowhooks.attachSharedFlow
      apigee.keyvaluemaps.create
      apigee.keyvaluemaps.delete
      apigee.keyvaluemapentries.create

2.  Run the `deploy.sh` script:

- chmod +x
      ./deploy.sh

3.  Verify that the JavaScript policies have been added to the shared
    flows:

- Go to Apigee \> Proxy development \> Shared Flows and check that the
  following policies have been added.

  - `sf-api-sec-extension-postflow`

  - `sf-api-sec-extension-preflow`

4.  Validate data ingestion:

- Send a request to the gateway and go to **Apigee** data source to
  validate that the data has been received from Apigee.

5.  (Optional) Exclude unwanted domains from being tracked by APIsec:

    a.  Uncomment: DOMAIN_EXCLUSION_LIST.

    b.  Add the domains to exclude.

    c.  Edit `deploy.sh` and set the following variables:

    - export DOMAIN_EXCLUSION_LIST="domain1,domain2"

6.  Discontinue the integration:

    a.  Edit `undeploy.sh`:

    - export PROJECT_ID=example-project-id
          export ORG=$PROJECT_ID
          export ENVIRONMENT=example-env

    b.  Run the undeploy.sh script:

    - chmod +x
          ./undeploy.sh

      Go to Apigee \> Proxy development \> Shared Flows and check that
      the following policies have been removed.

      - `sf-api-sec-extension-postflow`

      - `sf-api-sec-extension-preflow`

####### Configure Apigee\'s JavaScript for manual deployment

You can customize the shared flow and apply it to an existing flow hook
(pre-proxy, post-proxy).

Set up Apigee\'s JavaScript policy to send Apigee Collector\'s API data
to Cortex XSIAM.

> **Note**
>
> If you have an existing hookand would like to integrate with the
> shared flow, run the `deploy.sh` script, and select `n`\' and exit at
> the prompt to create a new hook. Refer to the section [Connect to
> existing hook](#bridgeheadidm234856423182936).

1.  Edit `panw-api-sec-extension-configuration.properties` file:

    - Enter the `targetUrl` and `projectID`.

    - You can update 127KB of `maxBodyInspectionSizeKB`.

    - For domain exclusion, uncomment the line and add the URL to
      exclude.

    <!-- -->

    - targetUrl=<Cortex collector url>
          projectID=<GCP project id of apigee>
          maxBodyInspectionSizeKB=127 // This is default 
          and can be modified if needed.
          commonBinaryContentType=audio/,video/,image/,
          application/octet-stream,application/ogg,application/
          pdf,application/zip,application/gzip,application/
          vnd.rar,application/x-7z-compressed
          #domainExclusionList=example.com,example2.com/shopping

2.  Upload the edited `property set`:

    a.  Get a token to upload updates via an API request. For more
        information, refer to [property
        sets](https://cloud.google.com/apigee/docs/api-platform/cache/property-sets).

    - Input:

          gcloud config config-helper --force-auth-refresh --format

      Output:

          configuration:
            active_configuration: 
            properties:
              compute:
                region: 
                zone:     
          core:
                account: 
                disable_usage_reporting: 
                project: 
          credential:
            access_token: <Copy this value>
            id_token: 
            token_expiry: 
          sentinels:
            config_sentinel: 

    b.  Copy the `<access_token>` value from the output.

3.  Upload the `property set` to Apigee:

- curl --silent -X GET 
      "https://apigee.googleapis.com/v1/organizations/
      <ORG>/environments/<ENVIRONMENT>/resourcefiles/
      properties" -H 
      "Authorization: Bearer <access_token from above>"

4.  Generate Key Value Map (KVM), which stores the Cortex API key
    that\'s encrypted

- curl --silent -X POST 
      "https://apigee.googleapis.com/v1/organizations/
      <ORG>/environments/<ENVIRONMENT>/keyvaluemaps" -H 
      "Authorization: Bearer <access_token from above>" 
      -H "Content-Type: application/json" --data-raw 
      '{"name": "'"APISec-KVM"'", "encrypted": true}'

  If there\'s an error when creating the KVM because of an existing
  name, delete the KVM and recreate.

      curl --silent -X DELETE 
      "https://apigee.googleapis.com/v1/organizations/
      <ORG>/environments/<ENVIRONMENT>/keyvaluemaps/
      $APISEC_KVM_NAME" -H "Authorization: Bearer 
      <access_token from above>"

  Add the Cortex API key entry to the created KVM.

      curl --silent -X POST "https://apigee.googleapis.com/
      v1/organizations/<ORG>/environments/<ENVIRONMENT>/
      keyvaluemaps/$APISEC_KVM_NAME/entries" -H 
      "Authorization: Bearer <access_token from above>" 
      -H "Content-Type: application/json" --data-raw 
      '{"name": "api-key","value": "'"<Generated key 
      from cortex env>"'"}'

5.  Upload the shared flows:

- **Shared flows**:

  - `sf-api-sec-extension-postflow`

  - `sf-api-sec-extension-preflow`

  **Upload**

  Replace the `<sf>` with the shared flows:

      curl --silent -X POST --data-binary "<sf>.zip" -H 
      "Content-Type: application/octet-stream" -H 
      "Authorization: Bearer <access_token from above>" 
      "https://apigee.googleapis.com/v1/organizations/$ORG/
      sharedflows?action=import&name=<sf>"

  **Deploy**

  Input:

      curl --silent -X GET "https://apigee.googleapis.com/
      v1/organizations/<ORG>/sharedflows/<sf>" -H 
      "Authorization: Bearer <access_token from above>"

  Output:

      {
        "metaData": {
          "createdAt": "1736952161610",
          "lastModifiedAt": "1736952161610",
          "subType": "SharedFlow"
        },
        "name": "sf-api-sec-extension-postflow",
        "revision": [
          "1" // This is the revision number
        ],
        "latestRevisionId": "1"
      }

6.  Deploy `<sf>`:

- curl --silent -X POST -H "Authorization: 
      Bearer <access_token from above>" 
      "https://apigee.googleapis.com/
      v1/organizations/$ORG/environments/<ENVIRONMENT>/
      sharedflows/$sf/revisions/<REVISION>/
      deployments?override=true"

7.  Verify API security shared flows were created:

- Go to Apigee \> Proxy development \> Shared Flows and check that the
  following policies have been added.

  - `sf-api-sec-extension-postflow`

  - `sf-api-sec-extension-preflow`

####### Connect to an existing hook

Follow the steps if you have an existing hook and would like to
integrate with a shared flow.

1.  Check for existing flow hooks.

    a.  Go to Apigee \> Management \> Environments and select the
        environment to hook the shared flow.

    b.  In the **Flow Hooks** tab, select the relevant flow hook.

2.  Configure policy for shared flow to the existing hook.

    a.  Go to Apigee \> Proxy development \> Shared Flows and select the
        flow hook from the relevant environment.

    - > **Note**

      > Start with the hook in pre-proxy.

    b.  From the **Develop** tab, expand **Policies** and select
        **Flow Callout**.

    c.  Enter a meaningful name and select the **Sharedflow**:
        `sf-api-sec-extension-preflow` , and then click **Create**.

    d.  From the **Develop** tab, select **Shared flows** and expand
        **Default**.

    e.  From **Select policy**, select **Select existing policy**, and
        select the policy just created and then click **Add**.

    f.  Repeat the previous steps for the post-proxy hook. Select the
        **Sharedflow**: `sf-api-sec-extension-postflow`.

    g.  Click **Save and Deploy**.

- The steps automatically run without linking to the hooks.

  > **Important**

  > This should only be done when there are already existing hooks, and
  > API security shared flows can\'t be hooked as a standalone. Run the
  > deployment script, but skip step 9 by passing `n`. This step
  > publishes API security shared flows to the desired Apigee
  > environment without setting them to flow hooks.

3.  Limitations:

    - The API security extension deployment scripts currently do not
      support archive-deployment Apigee environments. Refer to [Manage
      archive
      deployment](https://cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments)
      for more information.

    <!-- -->

    - > **Note**

      > Archive deployments are currently in preview and are subject to
      > change.

    <!-- -->

    - The API security extension for Apigee relies on flow-hooks, which
      are available only with Intermediate or Comprehensive Apigee
      Environment types. Refer to
      [Environments](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types)
      for more information.

    - For requests/responses with binary payloads, the binary payload is
      not sent to the collector for analysis; only the metadata (for
      example, HTTP headers, query parameters, etc.) is sent.

###### Ingest Kong

> **Note**
>
> Requires the Data Collection add-on.

Integrate Kong with Cortex XSIAM to start scanning its APIs for
potential threats and vulnerabilities.

You need to integrate a dedicated Kong HTTP log plugin. This plugin
enables seamless traffic ingestion from your Kong API gateway to Cortex
XSIAM, allowing for comprehensive security measures such as OWASP
Top-10, bot detection, access control, and more.

Settings in Cortex XSIAM

In Cortex XSIAM, set up the **Kong** data source to integrate with the
Kong API Gateway.

1.  From Settings \> Data Sources , click
    ![](media/rId4436.png){width="0.9668799212598426in"
    height="0.20833333333333334in"} and search for **Kong** , and then
    click **Connect** or **Connect Another Instance**.

2.  In the **Kong Collector** wizard, enter a relevant name and then
    click **Create and Proceed**.

3.  Copy the key and paste it somewhere so that you can access it later.

- If you forget to record the key and close the window, you must
  generate a new key and repeat this process.

4.  Click the **Download Custom Plugin** link to download the plugin,
    which you can then install on the Kong API Gateway.

5.  Click **Close**.

6.  An instance is created for the data source. Click
    ![](media/rId4439.png){width="0.2646391076115486in"
    height="0.20833333333333334in"} (Copy API URL) to establish a
    connection when setting up Kong API Gateway.

Follow the steps to integrate Kong\'s API gateway with Cortex XSIAM.

####### Provision Kong API gateway with the custom plugin

To deploy the custom plugin, refer to the Kong API documentation online:

- [Kong
  Gateway](https://docs.konghq.com/gateway/latest/plugin-development/distribution/)

- [Kong
  Konnect](https://docs.konghq.com/konnect/gateway-manager/plugins/add-custom-plugin/)

- [Kong Ingress
  Controller](https://docs.konghq.com/kubernetes-ingress-controller/latest/plugins/custom/)

Kong as docker container

In this example, we\'ll use Docker to deploy Kong with the custom
plugin.

1.  Extract the zip archive into some target directory TARGET_DIRECTORY.
    This directory should contain an extracted \"kong\" directory.

2.  Add the following arguments to the \`docker run\` command, replacing
    TARGET_DIRECTORY with the correct path:

- -v "TARGET_DIRECTORY/kong:/tmp/custom_plugins/kong" \
      -e "KONG_LUA_PACKAGE_PATH=/tmp/custom_plugins/?.lua;;" \
      -e "KONG_PLUGINS=bundled,panw-apisec-http-log"

  You may want to adjust the size of the nginx body buffer, which is
  used by Kong internally. This size sets the upper limit on the amount
  of HTTP body bytes that can be mirrored by the plugin. By default,
  this value is 8192 bytes (8 KB). To change it, another argument can be
  passed to the docker: for example, setting it to 128 KB:

      -e "KONG_NGINX_HTTP_CLIENT_BODY_BUFFER_SIZE=128k"

  See <https://nginx.org/en/docs/syntax.html> for information on the
  allowed values of this variable.

  > **Important**

  > The size of the buffer must be equal to or larger than the max body
  > size setting in the plugin configuration, on every data plane node.

3.  To verify that the plugin is installed, query Kong's Admin API using
    the following command:

- curl admin-api-hostname:8001 | jq .configuration.loaded_plugins.'"panw-apisec-http-log"'

  This prints true to the terminal if the plugin is loaded into the Kong
  instance.

####### Add and configure the custom plugin

Add and configure the plugin.

1.  From the Kong Manager menu, go to **Plugins**.

2.  From the **Plugins** page, scroll down to the **Custom Plugins**
    section.

3.  Select **panw-apisec-http-log** and click **Edit** to configure the
    panw-apisec-http-log plugin settings.

  -----------------------------------------------------------------------
  Configuration           Description             Example
  ----------------------- ----------------------- -----------------------
  Protocols               The request protocols   Either http, https, or
                          the plugin will be      both
                          applied to.             

  Cloud Context           Cloud context, such as  987654321000
                          AWS Account ID, GCP     
                          Project ID, Azure       
                          Subscription or an      
                          appropriate value for   
                          on-prem.                

  Cloud Provider          Cloud provider where    AWS.
                          Kong API Gateway is     
                          installed.              

  Cloud Region            Cloud region.           us-east-2

  Cloud API Key           The collector           
                          authorization key       
                          provided by the Cortex  
                          platform.               

  HTTP Endpoint           The Cortex collector\'s 
                          endpoint URL.           
  -----------------------------------------------------------------------

4.  Click the **View Advanced Parameters** to configure optional
    settings.

- > **Note**

  > The queue parameters can be updated to change when the plugin
  > mirrors data to Cortex.

+-----------------------+----------------------------------------+-----------------------+
| Configuration         | Description                            | Example               |
+=======================+========================================+=======================+
| Instance Name         | A custom name for this plugin          | Empty                 |
|                       | instance. This is useful when applying |                       |
|                       | different instances to different       |                       |
|                       | scopes.                                |                       |
+-----------------------+----------------------------------------+-----------------------+
| Tags                  | An optional set of strings for         | Empty                 |
|                       | grouping and filtering,                |                       |
|                       |                                        |                       |
|                       | > **Note**                             |                       |
|                       | >                                      |                       |
|                       | > Use commas to separate tags.         |                       |
+-----------------------+----------------------------------------+-----------------------+
| Keepalive             | An optional value in milliseconds that | 60000 (60 seconds)    |
|                       | defines how long an idle connection    |                       |
|                       | will live before being closed.         |                       |
+-----------------------+----------------------------------------+-----------------------+
| Timeout               | An optional timeout in milliseconds    | 10000 (10 seconds)    |
|                       | when sending data to Cortex.           |                       |
+-----------------------+----------------------------------------+-----------------------+
| Max body size         | The maximum body size to mirror in     | 131072 (128 KB), or   |
|                       | bytes (for example: 1024 is 1KB). Any  | the nginx body buffer |
|                       | bytes beyond this size are omitted     | size if it's smaller. |
|                       | from the request and response bodies.  |                       |
|                       | Must be \<= 4 MB and \<= the value of  |                       |
|                       | Kong\'s                                |                       |
|                       | **nginx_http_client_body_buffer_size** |                       |
|                       | setting.                               |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue Concurrency     | The number of queue delivery timers.   | 1                     |
| Limit                 | -1 indicates unlimited.                |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Initial Retry   | Time in seconds before the initial     | 0.01 (10              |
| Delay                 | retry is made for a failing batch.     | milliseconds)         |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Batch Size  | Maximum number of entries that can be  | 1                     |
|                       | processed at a time.                   |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Bytes       | Maximum number of bytes that can be    | Unlimited             |
|                       | waiting in a queue, requires string    |                       |
|                       | content                                |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Coalescing  | Maximum number of (fractional) seconds | 1                     |
| Delay                 | to elapse after the first entry was    |                       |
|                       | queued before the queue starts calling |                       |
|                       | the handler.                           |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Entries     | Maximum number of entries that can be  | 10000                 |
|                       | waiting in the queue.                  |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Retry Delay | Maximum time in seconds between        | 60                    |
|                       | retries, caps exponential backoff.     |                       |
+-----------------------+----------------------------------------+-----------------------+
| Queue.Max Retry Time  | Time in seconds before the queue gives | 60                    |
|                       | up calling a failed handler for a      |                       |
|                       | batch.                                 |                       |
+-----------------------+----------------------------------------+-----------------------+

5.  Go to **Kong** data source to validate that data is ingested from
    the Kong API Gateway.

####### Limitations

- The plugin supports HTTP and HTTP/S protocols.

- The plugin supports Kong API Gateway version 3.4.x and above.

- The nginx body buffer size on each data plane node must be equal or
  larger than the **max body size** setting.

- Request and response bodies will not be mirrored if their size exceeds
  the nginx body buffer size. When this occurs, it is indicated in the
  metadata that is sent to Cortex along with the HTTP transaction data.

- The mirrored response body is the body returned from the upstream
  service. This means that changes made to the response body by other
  plugins, is not reflected in the mirrored data.

###### Ingest-F5

> **Note**
>
> Requires the Data Collection add-on.

Integrate F5 with Cortex XSIAM to start scanning its APIs for potential
threats and vulnerabilities.

You need to integrate a dedicated F5 log plugin. This plugin enables
seamless traffic ingestion from your F5 Gateway to Cortex XSIAM,
allowing for comprehensive security measures such as OWASP Top-10, bot
detection, access control, and more.

####### Settings in Cortex XSIAM

In Cortex XSIAM, set up the **F5** data source to integrate with the F5
API Gateway.

1.  From Settings \> Data Sources , click
    ![](media/rId4436.png){width="0.9668799212598426in"
    height="0.20833333333333334in"} and search for **F5 BIG-IP LTM** ,
    and then click **Connect** or **Connect Another Instance**.

2.  In the **F5 BIG-IP LTM Collector** wizard, enter a relevant name and
    then click **Create and Proceed**.

3.  Copy the key and paste it somewhere so that you can access it for
    later.

- If you forget to record the key and close the window, you must
  generate a new key and repeat this process.

4.  Click the **Download iRules LX Plugin** link to download the plugin,
    which you can then upload to the F5 API Gateway.

5.  Click **Close**.

6.  An instance is created for the data source. Click
    ![](media/rId4439.png){width="0.2646391076115486in"
    height="0.20833333333333334in"} (Copy API URL) to establish a
    connection when setting up F5 API Gateway.

####### Settings in F5 BIG-IP LTM

1.  Log in to your F5 environment.

2.  Verify that the following is configured:

- Navigate to System \> Resource Provisioning and enable
  **iRules Language Extensions (iRulesLX)** . Check **Provisioning** and
  set to **Nominal**.

3.  Navigate to Local Traffic \> iRules \> LX Workspaces and follow the
    steps under the relevant tab:

- **LX Workspaces**:

  - Click **Import**. In the **General Properties** page, enter a
    **Name** and for **Source**, select **apisec_bigip_plugin_tar.gz** .

  <!-- -->

  - > **Note**

    > Extract the files from the F5 plugin to a folder before selecting
    > to upload to F5.

  <!-- -->

  - In the **General Properties** page, enter:

    - **Name**: Enter the name **panw_apisec_workspace**.

    - **Source**: Select **apisec_bigip_plugin_tar.gz**.

  - Select **Import** to import the plugin.

  **LX Plugins**:

  - Click **Create**.

  - In the **General Properties** page, enter:

    - **Name**: Enter **panw_apisec_plugin**.

    - **From Workspace**: Select **panw_apisec_workspace**.

  - Click **Finished**.

4.  Navigate to Local Traffic \> Virtual Servers \> Virtual Server List
    . The virtual server functions as an API Gateway, handling all
    incoming and outgoing requests and responses, then forwarding that
    data to the Cortex XSIAM collector.

    - From the virtual server that serves as the gateway, click
      **Edit**.

    - In the **Resources** tab, under **iRules**, click **Manage**.

    - From the **Available** list, navigate to
      **/Common/panw_apisec_plugin** and select
      **panw_apisec_data_collection** and **panw_apisec_set_ssl_data** ,
      and then click the left arrow button to move them to
      the **Enabled** list.

    <!-- -->

    - > **Note**

      > Select **panw_apisec_set_ssl_data** only if your client SSL
      > profile is enabled.

    <!-- -->

    - Click **Finished**.

    - Click the **Properties** tab.

5.  Navigate to System \> File Management \> Data Group File List \>
    Import.

    - From **File Name**, select the **panw_apisec_config.txt** file
      that was extracted from the zip that was downloaded from Cortex
      XSIAM.

    - In the **Name** field, select **Create New** and enter
      **panw_apisec_config**.

    - From **File Contents**, select **String**.

    - For **Data Group Name**, enter **panw_apisec_config**.

    - Click **Import**.

6.  Navigate to System \> File Management \> Data Group File List.

    - Click **panw_apisec_config**.

    - In **Definition**, fill in the values for the following:

    <!-- -->

    - "context_account_id" := "",
          "context_provider" := "",
          "context_region" := "",
          "cortex_collector_key" := "",
          "cortex_collector_url" := "",

      - Paste the F5 VIG-IP LTM Collector key you copied from Cortex
        XSIAM in the `"cortex_collector_key"`.

      - From Cortex XSIAM, go to **Data Sources** and from
        **F5 BIG_IP LTM** , copy the API URL and paste it in the
        `"cortex_collector_url"`.

      <!-- -->

      - ![](media/rId4490.png){width="5.833333333333333in"
        height="1.0791666666666666in"}

      <!-- -->

      - The `context_account_id`, `context_provider`, and
        `context_region` depend on the cloud environment. In this
        instance, AWS is the example:

      <!-- -->

      - > **Note**

        - > The provider for `"context_provider"` should always be
          > uppercase.

        - > Supported providers: AWS, GCP, Azure, On-prem.

        <!-- -->

            "context_account_id" := "12345",
            "context_provider" := "AWS",
            "context_region" := "us-east-2",
            "cortex_collector_key" := "collector key",
            "cortex_collector_url" := "API URL",

      <!-- -->

      - Click **Update**.

7.  Test the request/response and verify that the logs are sent to
    Cortex XSIAM. This can be verified by checking that the counter has
    increased. The scanned API endpoint metadata from f5-bigip is ready
    for investigation in the API inventory.

##### Agent-based protection

> **Note**
>
> Web and API Security (WAAS) profiles and policies are currently a Beta
> feature.

Cortex XSIAM can protect your workloads from various types of injection
attacks, exploitation attempts, known vulnerabilities, automated tools,
and more. In addition, your cloud workloads can be protected against
evolving threats aggregated from commercial threat feeds, open-source
threat feeds, and input from the Palo Alto Networks Unit 42 research
team.

Web and API Security profiles provide comprehensive real-time detection
and protection for web-based applications and APIs running on
Linux-based workloads, to prevent cloud attacks. These profiles can be
applied to policies for such workloads.

You can configure Cortex XSIAM to either monitor traffic for threats, or
to actively block them. A fully configurable profile gives you the
flexibility to protect your workloads based on specific needs for each
type of threat.

Follow these steps to configure profiles and policies for cloud
workloads:

1.  Task 1: [Set up Web and API Security
    profiles](#UUIDe21c21d9553b8a8d6ca41326983cdbf9)

2.  Task 2: [Apply Web and API Security profiles to
    workloads](#UUID19c9ba3f6162b0cd83231fd8ced5c458)

3.  (Optional) Task 3: Configure exception rules, such as [legacy
    exception rules](#UUID0579a9bf77f51bedf85935040b6dab05) and [support
    exception rules](#UUIDb579fa6ffeece274b8dcf8b4e613ec6c). [Disable
    prevention rules](#UUID3802af8bbb27f112a18f0654f4aee37a) for
    specific use cases.

Limitations

The following limitations currently exist for WAAS protection features:

- Only Linux kernel version 5.13 and later, and cgroup v2 are supported.

- The Linux kernel must be compiled with BPF support.

- K8s network policy is not enforced.

- Connections that were initiated before the XDR agent was started will
  not be inspected.

- Inspection size is limited to 128 Kb

- In HTTP/2, XFF is only added when there is no existing XFF header.

- The following are not supported:

  - localhost interface

  - K8s pod traffic between containers within the same node

  - Multiple NICs on K8s nodes (only traffic using the default route is
    supported)

  - Direct HTTPS connection (end-to-end encryption)

  - Service-Mesh based communication

  - UDP-based communication, including HTTP/3 and QUIC

  - gRPC

###### Set up Web and API Security profiles

> **Note**
>
> Web and API Security profiles and policies are currently a Beta
> feature.

You can configure Web and API Security profiles to provide comprehensive
real-time detection and protection for web-based applications and APIs
running on Linux-based workloads. These profiles can be applied to
policies for such workloads.

For each setting that you want to override, clear the corresponding
option to **Use Default**, and then select the setting of your choice.

> **Note**
>
> In this profile, the **Report** options configure the workload to
> report the corresponding malicious applications or APIs to Cortex
> XSIAM, without blocking them. The **Disabled** options configure the
> workloads to neither analyze nor report the corresponding malware or
> behavior.

1.  Add a new profile and define basic settings.

    a.  From Cortex XSIAM, select Inventory \> Endpoints \> Policy
        Management \> Prevention \> Profiles. Click **+Add Profile**,
        and select whether to create a new profile, or to import a
        profile from a file.

    b.  Select the **Linux** platform, and **Web & API Security** as the
        profile type.

    c.  Click **Next**.

    d.  Enter a unique **Profile Name** for the profile. The name can
        contain only letters, numbers, or spaces, and must be no more
        than 30 characters. The name will be visible from the list of
        profiles when you configure a policy rule.

    e.  (Optional) Enter a description that describes the intention or
        business purpose of the profile.

2.  Configure **Action Mode** options. If you choose **Enable**, you can
    then configure each item separately.

+-----------------------+-----------------------+-----------------------+
| Item                  | Options               | More details          |
+:======================+=======================+:======================+
| Action Mode           | - Enable              | When set to           |
|                       |                       | **Enable**, Cortex    |
|                       | - Disable             | XSIAM performs the    |
|                       |                       | configured action for |
|                       |                       | each of the options.  |
+-----------------------+-----------------------+-----------------------+
| XSS                   | - Block               | When Cortex XSIAM     |
|                       |                       | detects cross-site    |
|                       | - Report              | scripting (XSS)       |
|                       |                       | injection, it         |
|                       | - Disable             | performs the          |
|                       |                       | configured action.    |
|                       |                       |                       |
|                       |                       | XSS attacks are       |
|                       |                       | attacks in which      |
|                       |                       | malicious JavaScript  |
|                       |                       | snippets are injected |
|                       |                       | into otherwise benign |
|                       |                       | and trusted websites. |
|                       |                       | In such attacks,      |
|                       |                       | attackers try to      |
|                       |                       | trick the browser     |
|                       |                       | into switching to a   |
|                       |                       | JavaScript context    |
|                       |                       | and executing         |
|                       |                       | arbitrary code.       |
+-----------------------+-----------------------+-----------------------+
| SQL Injection         | - Block               | When Cortex XSIAM     |
|                       |                       | detects SQL injection |
|                       | - Report              | (SQLi) attempts, it   |
|                       |                       | performs the          |
|                       | - Disable             | configured action.    |
|                       |                       |                       |
|                       |                       | (SQLi) attacks can    |
|                       |                       | occur when an         |
|                       |                       | attacker successfully |
|                       |                       | inserts a malicious   |
|                       |                       | SQL query into the    |
|                       |                       | input fields of a web |
|                       |                       | application. A        |
|                       |                       | successful attack can |
|                       |                       | read sensitive data   |
|                       |                       | from the database,    |
|                       |                       | modify data in the    |
|                       |                       | database, or run      |
|                       |                       | arbitrary commands.   |
+-----------------------+-----------------------+-----------------------+
| Injection Attacks     | - Block               | When Cortex XSIAM     |
|                       |                       | detects injection     |
|                       | - Report              | attacks, it performs  |
|                       |                       | the configured        |
|                       | - Disable             | action.               |
|                       |                       |                       |
|                       |                       | Injection attacks are |
|                       |                       | a form of attacks in  |
|                       |                       | which attackers       |
|                       |                       | attempt to insert     |
|                       |                       | malicious input into  |
|                       |                       | an application to     |
|                       |                       | manipulate its        |
|                       |                       | execution. Command    |
|                       |                       | and code payloads can |
|                       |                       | either be injected as |
|                       |                       | part of HTTP          |
|                       |                       | requests, or are      |
|                       |                       | included from local   |
|                       |                       | or remote files (also |
|                       |                       | known as File         |
|                       |                       | Inclusion attacks).   |
+-----------------------+-----------------------+-----------------------+
| CVE Exploits          | - Block               | When Cortex XSIAM     |
|                       |                       | detects known         |
|                       | - Report              | vulnerabilities       |
|                       |                       | (Common               |
|                       | - Disable             | Vulnerabilities and   |
|                       |                       | Exposures (CVEs)), it |
|                       |                       | performs the          |
|                       |                       | configured action.    |
+-----------------------+-----------------------+-----------------------+
| Sensitive Data        | - Block               | When Cortex XSIAM     |
| Exposure              |                       | protects workloads    |
|                       | - Report              | from exposing         |
|                       |                       | sensitive data, it    |
|                       | - Disable             | performs the          |
|                       |                       | configured action.    |
|                       |                       |                       |
|                       |                       | This module protects  |
|                       |                       | workloads from        |
|                       |                       | providing responses   |
|                       |                       | that could expose     |
|                       |                       | sensitive data found  |
|                       |                       | in critical system    |
|                       |                       | files, including      |
|                       |                       | password hashes       |
|                       |                       | (/etc/shadow), user   |
|                       |                       | account information   |
|                       |                       | (/etc/passwd), and    |
|                       |                       | private encryption    |
|                       |                       | keys.                 |
+-----------------------+-----------------------+-----------------------+
| Authentication Bypass | - Block               | When Cortex XSIAM     |
|                       |                       | detects attempts to   |
|                       | - Report              | bypass authentication |
|                       |                       | controls, it performs |
|                       | - Disable             | the configured        |
|                       |                       | action.               |
|                       |                       |                       |
|                       |                       | This module protects  |
|                       |                       | against attacks that  |
|                       |                       | attempt to circumvent |
|                       |                       | authentication        |
|                       |                       | controls through      |
|                       |                       | session manipulation, |
|                       |                       | token exploitation,   |
|                       |                       | or credential abuse.  |
+-----------------------+-----------------------+-----------------------+
| Advanced Threat       | - Block               | When Cortex XSIAM     |
| Protection            |                       | detects evolving      |
|                       | - Report              | threats, it performs  |
|                       |                       | the configured        |
|                       | - Disable             | action.               |
|                       |                       |                       |
|                       |                       | Advanced Threat       |
|                       |                       | Protection (ATP) is a |
|                       |                       | comprehensive         |
|                       |                       | security feature      |
|                       |                       | designed to detect,   |
|                       |                       | prevent, and respond  |
|                       |                       | to sophisticated web  |
|                       |                       | and API threats,      |
|                       |                       | ensuring robust       |
|                       |                       | protection for        |
|                       |                       | workloads against     |
|                       |                       | evolving risks.       |
+-----------------------+-----------------------+-----------------------+
| Offensive Tools       | - Block               | Cortex XSIAM can      |
|                       |                       | identify offensive    |
|                       | - Report              | tools that scan web   |
|                       |                       | applications for      |
|                       | - Disable             | known security        |
|                       |                       | vulnerabilities and   |
|                       |                       | misconfiguration, and |
|                       |                       | exploit them. When    |
|                       |                       | such tools are found, |
|                       |                       | this module can block |
|                       |                       | or report them.       |
+-----------------------+-----------------------+-----------------------+
| Malformed Traffic     | - Block               | When Cortex XSIAM     |
|                       |                       | detects HTTP requests |
|                       | - Report              | with anomalies that   |
|                       |                       | are not expected from |
|                       | - Disable             | common web browsers,  |
|                       |                       | it performs the       |
|                       |                       | configured action.    |
+-----------------------+-----------------------+-----------------------+
| Automation Tools      | - Block               | When Cortex XSIAM     |
|                       |                       | detects automated     |
|                       | - Report              | tools, it performs    |
|                       |                       | the configured        |
|                       | - Disable             | action.               |
|                       |                       |                       |
|                       |                       | Malicious automated   |
|                       |                       | tools or services can |
|                       |                       | scrape website        |
|                       |                       | contents such as      |
|                       |                       | Scriptable headless   |
|                       |                       | web browsers, command |
|                       |                       | line tools, or HTTP   |
|                       |                       | libraries.            |
+-----------------------+-----------------------+-----------------------+
| Known Bots            | - Block               | When Cortex XSIAM     |
|                       |                       | detects known bots,   |
|                       | - Report              | it performs the       |
|                       |                       | configured action.    |
|                       | - Disable             |                       |
|                       |                       | Cortex XSIAM can      |
|                       |                       | identify legitimate   |
|                       |                       | bots that properly    |
|                       |                       | declare their         |
|                       |                       | identity and purpose, |
|                       |                       | such as search engine |
|                       |                       | crawlers and          |
|                       |                       | authorized web        |
|                       |                       | indexers. These bots  |
|                       |                       | follow standard       |
|                       |                       | protocols and provide |
|                       |                       | verifiable operator   |
|                       |                       | information, however  |
|                       |                       | some of them might    |
|                       |                       | cause undesirable     |
|                       |                       | behaviors, such as    |
|                       |                       | spam, and you might   |
|                       |                       | prefer to block such  |
|                       |                       | bots.                 |
+-----------------------+-----------------------+-----------------------+

3.  To save the profile, click **Create**.

**What to do next**

If you are ready to apply your new profile to endpoints, you do this by
adding it to a policy rule. If you still need to define other profiles,
you can do this later. During policy rule creation or editing, you
select the endpoints to which to assign the policy. There are different
ways of doing this, such as:

Create a policy rule from the **Prevention Profiles** page

1.  Navigate to Inventory \> Endpoints \> Policy Management \>
    Prevention \> Profiles.

2.  Right-click your new profile, and select
    **Create a new policy rule using this profile**.

3.  Configure the policy rule.

Edit an existing policy rule from the **Policy Rules** page

1.  Navigate to Inventory \> Endpoints \> Policy Management \>
    Prevention \> Policy Rules.

2.  Right click an existing policy and select **Edit**.

3.  Add your new profile to the policy rule.

Create a new policy rule from the **Policy Rules** page

1.  Navigate to Inventory \> Endpoints \> Policy Management \>
    Prevention \> Policy Rules.

2.  Click **Add Policy**.

3.  Configure a new policy that includes your new profile.

###### Apply Web and API Security profiles to workloads

> **Note**
>
> Web and API Security profiles and policies are currently a Beta
> feature.

Cortex XSIAM provides out-of-the-box protection for all registered
workloads with a default security policy. To customize your security
policy, create or edit one or more security profiles, and then attach
the profiles to one or more policies.

Each policy you create must apply to one or more workload or workload
groups. The **Prevention Policy Rules** table lists all the policy rules
per operating system. Rules associated with one or more targets that are
beyond your defined user scope are locked and cannot be edited.

1.  From Cortex XSIAM, create a policy rule.

- Do one of the following:

  - Select Inventory \> Endpoints \> Policy Management \> Prevention \>
    Policy Rules, and select **+ New Policy** or **Import from File**.

  <!-- -->

  - > **Note**

    > When importing a policy, select whether to enable the associated
    > policy targets. Rules within the imported policy are managed as
    > follows:

    - > New rules are added to the top of the list.

    - > Default rules override the default rule in the target tenant.

    - > Rules without a defined target are disabled until the target is
      > specified.

  <!-- -->

  - Select Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, right-click the profile that you want to assign, and click
    **Create a new policy rule using this profile**.

2.  Enter a policy name, and a description (optional) that describes the
    purpose or intent of the policy.

3.  Select the **Platform** for which you want to create a new policy.

4.  Select the desired profiles that you want to apply in this policy.

- If you do not specify a profile, the default profiles are used.

5.  Click **Next**.

6.  Use the filters to assign the policy to one or more workloads or
    workload groups.

- Cortex XSIAM automatically applies the platform filter you selected
  and, if it exists, the **Group Name** according to the groups within
  your defined user scope.

7.  Click **Done**.

8.  In the **Policy Rules** table, change the rule position, if needed,
    to order the policy relative to other policies.

- The Cortex XDR agent evaluates policies from top to bottom. When the
  Cortex XDR agent finds the first match, it applies that policy as the
  active policy. To move the rule, select the arrows and drag the policy
  to the desired location in the policy hierarchy.

  Right-click to display and use one of the following options
  **View Policy Details**, **Edit**, **Save as New**, **Disable**, and
  **Delete**.

9.  If you want to export policies, select one or more policies,
    right-click, and select **Export Policies**. You can include the
    associated **Policy Targets**, **Global Exceptions**, and workload
    groups.

- > **Note**

  > The exported file is encoded in Base64 and cannot be edited.

###### Manage Web and API Security prevention profiles

After you create and customize your Web and API Security prevention
profiles, you can manage them from the **Prevention Profiles** page as
needed.

####### View the prevention policy rules that use a specific prevention profile

Before you modify or delete a profile, you can check which policy rules,
if any, use the profile.

- From Inventory \> Endpoints \> Policy Management \> Prevention \>
  Profiles, right-click the profile and select **View policy Rules**.

<!-- -->

- Cortex XSIAM opens the **Prevention Policy Rules** page on a new tab.
  This page is filtered, and only displays the rules that use the
  profile that you selected.

####### Edit, export, duplicate, or delete a prevention profile

Edit a profile:

1.  From Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, right-click the profile and select **Edit**.

2.  Make your changes, and then click **Save**.

Export a profile:

1.  From Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, right-click the profile and select **Export Profile**.

2.  Click **Export**. The profile is downloaded to your computer.

Duplicate a profile:

1.  From Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, right-click the prevention profile and select
    **Save as New**. A new profile is displayed, containing the values
    from the profile that you selected.

2.  Edit the profile name and description, edit any values that you want
    to change, and then click **Create**.

3.  Populate a new prevention policy rule with your new profile.

Delete a profile:

1.  If necessary, delete or detach any policy rules that use the profile
    before attempting to delete it.

2.  From Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, locate the profile that you want to remove. The profile\'s
    **Usage Count** cell must have a 0 (zero) value.

3.  Right-click the prevention profile and select **Delete**.

4.  To confirm the deletion, click **Yes**.

####### Populate a new prevention policy rule with a prevention profile

1.  From Inventory \> Endpoints \> Policy Management \> Prevention \>
    Profiles, right-click the profile and select
    **Create a new policy rule using this profile**.

- Cortex XSIAM automatically populates the **Platform** selection based
  on your profile configuration, and assigns the profile based on the
  profile type.

2.  For **Policy Name**, enter a meaningful name, and optionally, add a
    description for the policy rule.

3.  Assign any additional profiles that you want to apply to your policy
    rule, and click **Next**.

4.  Select the target workloads for the policy rule, or use the filters
    to define criteria for the policy rule to apply, and then click
    **Next**.

5.  Review the policy rule summary, and then click **Done**.

####### View information about your Web and API Security prevention profiles

The following table displays the fields that are available on the
**Prevention Profiles** page, in alphabetical order. The table includes
both default fields and additional fields that are available in the
column manager. To view this page, go to Inventory \> Endpoints \>
Policy Management \> Prevention \> Profiles.

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  Associated Targets                  The endpoints or endpoint groups to
                                      which the profile is assigned

  Created By                          The administrator who created the
                                      prevention profile

  Created Time                        The date and time at which the
                                      prevention profile was created

  Description                         An optional description entered by
                                      an administrator to describe the
                                      prevention profile

  Modification Time                   The date and time at which the
                                      prevention profile was modified

  Modified By                         The administrator who modified the
                                      prevention profile

  Name                                The prevention profile name

  Profile ID                          The ID assigned to to the profile
                                      by Cortex XSIAM

  Summary                             Summary of prevention profile
                                      configuration

  Type                                The prevention profile type

  Usage Count                         The number of policy rules that use
                                      the profile. If you want to delete
                                      a profile, ensure that this cell
                                      displays \"0\".
  -----------------------------------------------------------------------

###### Add a disable prevention rule for cloud workloads

You can create granular exceptions to prevention actions defined for
your workloads. These exception rules may be useful when you have
processes that are essential to your organization, and must not be
terminated. To cover all your workloads, you can configure different
exception rules per platform. Cortex XSIAM still generates issues from
the disabled rules.

> **Important**

- > All applicable prevention actions are skipped for the files and
  > process that match the properties defined in the rule.

- > Consider the consequences of disabling a prevention rule before you
  > add the exception, and monitor it over time.

1.  Go to Settings \> Exceptions Configuration \> Disable Prevention
    Rules.

2.  Click **Add Rule**, and select **Web and API Security**.

3.  For **Rule Name**, enter a meaningful name for the rule.

4.  (Optional) Enter a description for the business reason or intent for
    the rule.

5.  Click **Next**.

6.  For **Exception Effect**, choose an option:

    - **Disable prevention and report**: Disable the prevention modules
      included in this rule and report on it.

    - **Disable prevention and do not report**: Disable the prevention
      modules included in this rule but do not report on it.

7.  For **Platform**, select the operating system that you require.

8.  Under **Target Properties**, you can configure any combination of
    parameters. If a parameter is not specified, all values are allowed.
    You can use wildcards for matching. Press Enter to add the target
    properties. Repeat this step for additional target properties.

- When you specify two or more values, the exception is applied only if
  the file satisfies all the specified target properties.

  - **Domain**: Specify a domain.

  - **IP**: Specify an IP address.

  - **User Agent**: Specify the application\'s User-Agent ID that is
    used in the headers of an API request.

  <!-- -->

  - For example, if the user agent is `"User-Agent:paypal.com"`, enter
    `paypal.com` here.

  <!-- -->

  - **Path**: Specify the path to the required files or folders.

9.  For **Modules**, select one or more security modules that won\'t
    trigger prevention actions.

- The actions triggered by the other modules are not affected.

10. For **Scope**, select the scope for the rule:

    - If you want to apply the rule to all workloads, select **Global**.

    - If you want to apply the rule to only specific exception profiles,
      click **Exception Profiles**, and then select them from the list.

11. Click **Next**.

12. Review the configurations for the exception, and if the risks are
    acceptable to you, select **I understand the risk**, and then click
    **Create**.

###### Add a support exception rule for cloud workloads

You can define and manage exceptions based on files received from the
customer support team. You can apply the rule across all of your
workloads or to specific profiles.

1.  From Settings \> Exceptions Configuration \> Support Exception
    Rules, click **+ Import from file**.

2.  Locate the JSON file that you received from the customer support
    team, and either drag and drop the file to this dialog box, or click
    **Browse** to locate the file.

3.  Select **Profile/s** to apply the rule to one or more specific
    profiles, or select **Global** to apply to all workloads.

    - If you want to apply the rule to existing profiles, select them
      from the list.

    - If you want to apply the rule to a new profile, click
      **New Profile**, and enter the name of the new profile.

4.  Click **Import**.

###### Add a legacy exception rule for cloud workloads

Legacy Exception rules enable you to configure an exception to
prevention and protection modules on workloads for selected profiles.

Items included in allow lists may continue to generate Cortex XSIAM
security events. If you want to exclude event reporting, configure this
on the **Issue Exclusions** page (Settings \> Exception Configurations
\> Issue Exclusions).

1.  Select Cases & Issues \> Issues.

2.  Locate an issue from which you can create an exception rule, and
    right-click it.

3.  Select Manage Issue \> Create Issue Exception.

4.  Select the items that you want to be included in the exception rule:

    - **Domain**: The domain to be excluded by the rule. For example,
      google.com

    - **Path**: The path to files or folders to be excluded by the rule.

    - **User-Agent**: The application\'s User-Agent ID to be excluded by
      the rule. For example, a User-Agent ID for the curl application
      could be `curl/7.68.0`

    - **IP address**: The IP address to be excluded by the rule.

5.  Select an option for **Exception Scope**:

    - **Global**: Apply the exception rule globally for all workloads.

    - **Profile**: Apply the rule only to workloads mapped to the
      profile selected in the next step.

6.  If you selected **Profile**, select a profile from the
    **Exception Profile Name** list.

7.  Click **Create**.

- Your rule is created, and can be viewed at the following location:
  Settings \> Exceptions Configuration \> Legacy Agent Exceptions.

###### Additional workload management tasks

Several management activities that can be performed on workloads are
accessible from Inventory \> Endpoints \> All Endpoints and from
Inventory \> Endpoints \> Groups. On these pages, select one or more
workloads, and right-click to access the available actions and
configuration options.

#### API specification inventory

Cortex XSIAM offers the option to import API specifications that comply
with the [OpenAPI](https://www.openapis.org/) format, including format,
file structure, and data types.

Cortex Cloud automatically identifies and extracts API specifications
from your AWS and Azure API gateways, proactively scanning them for
misconfigurations and vulnerabilities, providing a comprehensive and
secure inventory of all your API endpoints, going beyond the visibility
of just traffic. Cortex generates API endpoints directly from
specifications, to pinpoint shadow APIs that are otherwise hidden.

Use Cortex XSIAM to validate live traffic against specifications and
alert on surface deviations, undocumented endpoints, or security gaps.

The following table describes the fields that are available for each API
specification.

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Sources                           | Source of the API specification:  |
|                                   |                                   |
|                                   | - User                            |
|                                   |                                   |
|                                   | - API Gateway Configuration       |
+-----------------------------------+-----------------------------------+
| Asset Name                        | Asset name is obtained from the   |
|                                   | `title` field in the              |
|                                   | specification.                    |
+-----------------------------------+-----------------------------------+
| Servers List                      | This field is automatically       |
|                                   | filled if the specification       |
|                                   | contains the server URL or host.  |
|                                   | You must manually add the URL or  |
|                                   | host address if no URL or host is |
|                                   | specified.                        |
|                                   |                                   |
|                                   | > **Note**                        |
|                                   | >                                 |
|                                   | > Even if you have already        |
|                                   | > imported the specification, you |
|                                   | > can edit the API specification  |
|                                   | > in Cortex XSIAM and add or      |
|                                   | > update the server list.         |
+-----------------------------------+-----------------------------------+
| API Versions                      | API version obtained from the API |
|                                   | specification.                    |
+-----------------------------------+-----------------------------------+
| Associated Endpoints              | Shows the number of endpoints     |
|                                   | that match the specification.     |
|                                   |                                   |
|                                   | You can right-click and select    |
|                                   | **View Associated Endpoints** to  |
|                                   | see the matched paths in the      |
|                                   | **API Endpoints** table.          |
+-----------------------------------+-----------------------------------+
| Format & Version                  | OpenAPI or Swagger and the        |
|                                   | relative version.                 |
+-----------------------------------+-----------------------------------+
| Spec File Name                    | Specification file name that was  |
|                                   | imported to Cortex XSIAM.         |
+-----------------------------------+-----------------------------------+
| Findings                          | The total number of findings is   |
|                                   | broken down by severity, and      |
|                                   | findings with a severity of high  |
|                                   | trigger an issue.                 |
+-----------------------------------+-----------------------------------+
| Status                            | Indicates if the specification    |
|                                   | is:                               |
|                                   |                                   |
|                                   | - Unknown                         |
|                                   |                                   |
|                                   | - Active                          |
|                                   |                                   |
|                                   | - Recently Active                 |
|                                   |                                   |
|                                   | - Inactive                        |
|                                   |                                   |
|                                   | - Deleted                         |
+-----------------------------------+-----------------------------------+

Click the API asset to open the side card. Each tab includes detailed
information from the parsed data of the API.

You can add **Comments**
(![](media/rId4515.png){width="0.20833333333333334in"
height="0.20833333333333334in"}) to the specification, providing
additional context about the API endpoints or other relevant
information.

##### Overview

Shows the highlights and properties of the API endpoint asset.

+-----------------------------------+--------------------------------------------------------------------------------+
| Field                             | Description                                                                    |
+===================================+================================================================================+
| Asset ID                          | API asset ID.                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------+
| Provider                          | Gateway provider:                                                              |
|                                   |                                                                                |
|                                   | - GCP                                                                          |
|                                   |                                                                                |
|                                   | - AWS                                                                          |
|                                   |                                                                                |
|                                   | - Azure                                                                        |
|                                   |                                                                                |
|                                   | - On Prem                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Asset Category                    | API Endpoint or API Specification                                              |
+-----------------------------------+--------------------------------------------------------------------------------+
| Account ID                        | Account ID of the API specification.                                           |
+-----------------------------------+--------------------------------------------------------------------------------+
| Asset Groups                      | Indicates the asset group to which the API is associated. For more             |
|                                   | information, go to [Asset Groups](#UUIDa299007a63312a26ae182d415c512454).      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Cases/Issues/Findings             | The page shows issues and cases.                                               |
|                                   |                                                                                |
|                                   | The link from the number opens the page where you can review the details.      |
|                                   | Refer to                                                                       |
|                                   | [#UUID78f2bdc35db231bedec98cace6573b65](#UUID78f2bdc35db231bedec98cace6573b65) |
|                                   | for detailed information.                                                      |
|                                   |                                                                                |
|                                   | You can view all API security issues and cases detected by Cortex XSIAM.       |
+-----------------------------------+--------------------------------------------------------------------------------+
| Evidence                          | Shows findings that provide visibility into the risks and vulnerabilities of   |
|                                   | your API landscape. By continuously analyzing findings, you can maintain an    |
|                                   | up-to-date view of the API asset's security posture and support more informed  |
|                                   | decision-making for detection, prioritization, and remediation efforts.        |
+-----------------------------------+--------------------------------------------------------------------------------+

An issue is generated when the following **Detection Method** is
triggered.

+-----------------------+-----------------------+-----------------------+
| Deployment option     | Detection Method and  | Description           |
|                       | Type                  |                       |
+=======================+=======================+=======================+
| Agentless for Posture | **Detection Method**: | If Cortex XSIAM       |
|                       | API Posture Scanner   | detects security      |
|                       |                       | vulnerabilities or    |
|                       |                       | compliance issues in  |
|                       |                       | the posture of an API |
|                       |                       | during scanning, an   |
|                       |                       | issue is generated.   |
|                       |                       |                       |
|                       |                       | The issue includes    |
|                       |                       | specification static  |
|                       |                       | scan findings         |
|                       |                       | relevant to the       |
|                       |                       | issue.                |
+-----------------------+-----------------------+-----------------------+

##### Code

The schema shows the actual API specification that includes the basic
information of the API, the API path, method, and parameters.

##### Insights

At a glance, we see a graphical representation of the specification scan
results by severity and by category.

You can filter in by severity or by category. Drill down to view details
of the selected scan result.

The specification scan results by severity table include the following
information:

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Severity                          | Indicates the severity of the     |
|                                   | scan result issue.                |
+-----------------------------------+-----------------------------------+
| Category                          | API category. The options are:    |
|                                   |                                   |
|                                   | - Access Control                  |
|                                   |                                   |
|                                   | - Networking and Firewall         |
|                                   |                                   |
|                                   | - Insecure Configurations         |
|                                   |                                   |
|                                   | - Data                            |
|                                   |                                   |
|                                   | - Encryption                      |
|                                   |                                   |
|                                   | - Structure and Semantics         |
+-----------------------------------+-----------------------------------+
| Name                              | Name of API specification.        |
+-----------------------------------+-----------------------------------+
| Description                       | Details of the scan results.      |
+-----------------------------------+-----------------------------------+
| Modification Time                 | Time stamp of when the API        |
|                                   | specification was modified        |
+-----------------------------------+-----------------------------------+
| Finding ID                        | For every vulnerability, a        |
|                                   | finding is created.               |
+-----------------------------------+-----------------------------------+

You can drill down by clicking a severity to view the
details/information of the findings (vulnerabilities).

+-----------------------------------+--------------------------------------+
| Field                             | Description                          |
+===================================+======================================+
| Severity                          | - Critical/High/Medium/Low           |
|                                   |                                      |
|                                   | - Info                               |
+-----------------------------------+--------------------------------------+
| Category                          | API category.                        |
+-----------------------------------+--------------------------------------+
| Link to OpenAPI checks            | The                                  |
|                                   | [OpenAPI](https://www.openapis.org/) |
|                                   | page of the scan results item        |
|                                   | includes a description of the issue  |
|                                   | and a link to the **Details**.       |
+-----------------------------------+--------------------------------------+
| Description                       | Details of the scan results.         |
+-----------------------------------+--------------------------------------+
| Scan Result Issue                 | Refers to the number of findings.    |
+-----------------------------------+--------------------------------------+
| Scan Results                      | Shows the findings in the API        |
|                                   | request. The issue is highlighted.   |
+-----------------------------------+--------------------------------------+

##### Import API specification

Cortex XSIAM enables you to import YAML or JSON files. After importing
the file, Cortex XSIAM analyzes the data to identify vulnerabilities to
help you effectively manage and enforce security measures.

**How to import an API Specification**

1.  Go to Inventory \> All Assets \> APIs \> Specification.

2.  Click **Import API Specification**.

3.  Drop or browse for the API specification file and add the server of
    where the file is hosted. This field is automatically filled if the
    file contains the server URL or host. If there is no URL or host in
    the file, you must manually add the URL or host address.

- > **Note**

  > Even if you already imported the file, you can edit the API asset
  > and add or update the server list.

4.  Click **Import**.

- It can take up to 30 minutes to import the file.

