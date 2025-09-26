## Serverless function security

### Overview

Securing serverless functions involves addressing both security posture
and runtime behavior.

For posture security, Cortex XSIAM provides comprehensive visibility
into the security configuration of your serverless functions across your
code and CI/CD pipelines. This is achieved through agentless scanning
that automatically detects vulnerabilities early in the development
lifecycle, allowing for proactive risk detection and mitigation before
reaching production.

In addition to posture, runtime security is crucial. Cortex XSIAM
enables runtime monitoring by embedding the Cortex XSIAM agent directly
into the code of the serverless function. This allows for real-time
monitoring of code execution, processes, networking, and filesystem
activity, along with the enforcement of policies to permit or deny these
actions. This in-depth runtime visibility enhances the overall security
of your serverless functions.

### Serverless function posture security

Cortex XSIAM serverless function scanning capabilities offer
comprehensive visibility into the security posture of your serverless
functions throughout your code and CI/CD environments without the need
to install agents or disrupt your workload operations. By integrating
scanning functionality directly into your serverless functions, Cortex
XSIAM automatically detects vulnerabilities early in the development
process, enabling proactive risk detection and mitigation before
production.

The following events trigger Cortex XSIAM serverless function scans:

- Periodic scans

- Settings modifications, including adding new functions for scanning

#### Supported platforms

- Supported architecture: x86_64

- Supported cloud providers: Amazon Web Services (AWS, Google Cloud
  Platform (GCP Generation 1), Microsoft Azure

  - Amazon Web Services (AWS): Lambda functions

  - Google Cloud Platform (GCP): Google functions. Support for Gen1 only

  - Microsoft Azure: Azure functions

#### Use cases

- **Scan Serverless Functions**: You can set up automated security scans
  for all your serverless functions to regularly check for potential
  vulnerabilities. You can schedule these scans to run periodically or
  automatically (event-driven) whenever changes are made to your
  functions. The scan results allow you to assess the security risks
  associated with your serverless applications

- **Visibility**: Get a single view of all vulnerabilities affecting
  your organization\'s serverless functions. This allows you to easily
  understand the overall security posture of these assets

- **Analyze and mitigate scan results**: Gain insights about the
  vulnerabilities detected by serverless function security scans. This
  enables you to understand and mitigate potential risks to improve the
  security of your serverless applications

- **Monitor scan health**: Gain detailed insights into serverless
  function scan health and status, allowing you to track scan data,
  troubleshoot errors and mitigate detected vulnerabilities, ensuring
  the overall health of your serverless functions

#### Onboard cloud providers for serverless functions

Integrate Cortex XSIAM with your cloud provider accounts to enable
security vulnerability scans of your serverless functions. This enables
you to efficiently analyze, prioritize, and resolve security findings
specific to your serverless deployments.

Supported cloud providers include:

- Amazon Web Services (AWS): Refer to [Onboarding
  AWS](/document/preview/1331929#UUID-5c1ddfb3-552a-7bea-2e00-168a2d859fa8)
  for more information about integrating Cortex XSIAM with AWS Lambda
  functions

- Google Cloud Platform (GCP): Refer to [Onboarding
  GCP](#UUID6ca58a018ee91fe08e96d50a2047795e) for more information about
  integrating Cortex XSIAM with GCP functions

<!-- -->

- > **Important**

  > Only GCP Gen1 functions support Cortex XSIAM serverless function
  > scans.

<!-- -->

- Microsoft Azure: Refer to [Onboarding
  Azure](#UUID54de27b4d4a6fb323a04f77b412de740) for more information
  about integrating Cortex XSIAM with Azure functions

> **Note**
>
> Only functions containing zip files are supported.

#### Serverless function posture policies

##### Manage serverless function policies

Serverless function policies define how a system should respond to
serverless function threats. They include conditions that trigger the
policy, the scope of its application, and the actions to be taken when
these conditions are met. When policies detect a threat, they generates
issues for remediation.

###### How to access serverless function policies

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Policies).

2.  Select the **Show filter panel** icon.

3.  Filter the table by the **Asset Types** category and select your
    cloud provider serverless function type from the **Select values**
    menu. Options:

    - **Azure Cloud Function**

    - **Google Cloud Function** (Gen 1 only)

    - **Lambda Function (AWS)**

- > **Note**

  > You can select multiple types to view all your serverless function
  > rules across your cloud providers.

  A list of serverless function rules filtered by asset type is
  displayed.

###### Manage serverless function policies

You can delete, edit or clone serverless function policies.

- Delete a policy when no longer relevant, to avoid overhead

- Edit a policy to fine-tune existing policies

- Clone a policy to saves time by reusing settings and applying policies
  uniformly across similar assets, ensuring standardized policies and
  predictable behavior

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Policies).

2.  Filter for the list of serverless function policies. Refer to [How
    to access serverless function
    policies](#Xa4f6e37fd7ee762394d3fd56eea3444a84fffea) above for more
    information.

3.  Right-click on a policy.

    - To delete a policy, click **Delete**, and confirm the deletion in
      the popup

    - To edit a policy, click **Edit**.

    <!-- -->

    - You are redirected to the **Details** step of the **Edit Policy**
      wizard.

    <!-- -->

    - To clone a policy, select **Save as new**.

    <!-- -->

    - You are redirected to the **Details** step of the new policy
      wizard.

- > **Note**

  > Refer to [Create serverless function
  > policies](#UUID3ecaad442c162c92ef11facea4232169) for more
  > information on how to define the steps of a policy in the wizard.

##### Create serverless function policies

The following procedure describes how to create policies for serverless
functions.

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Policies) \> click Create Policy.

2.  On the **Details ** step of the wizard:

    a.  Fill in these fields:

        - **Policy Name** (required): An alias you provide to identify
          the policy

        - **Description** (required): A description of the policy

        - **Labels** (optional): Assign labels to categorize and
          organize the policy based on specific criteria or attributes.
          Labels help in easily identifying and filtering policies

    b.  Click Next.

3.  On the **Rules** step of the wizard.

    a.  Select rules that check for violations when scanning serverless
        functions: Options:

        - **All Matching Filter Criteria**: Allows you to filter for
          rules according to criteria

        - **From Rules List**. Filter the rues list by the type of
          serverless function.

          i.  Select From Rules List

          ii. Select **Asset Type** from the **Select Field** menu of
              the query.

          iii. Filter for the following serverless functions, depending
               on the target cloud provider for the rule. Options:

               - Azure Cloud Function

               - Google Cloud Function

               - Lambda Function

               <!-- -->

               - > **Note**

                 > You can select multiple options.

          iv. Select a rule or multiple rules from the resulting list.

        - **All Rules**: This option is not recommended as it will
          probably create a large number of issues/

    - > **Note**

      > For more information about rules, refer to [Manage serverless
      > function rules](#UUID8868b0b116a61efb207bb8caeba7653f).

    b.  Click Next.

4.  On the **Scope** step of the of the wizard:

    a.  Define the scope of the policy by selecting the assets it will
        apply to. Options:

        - **From Cloud Accounts** (recommended): Select one or more
          accounts to which this policy applies

        - **All Cloud Accounts** (not recommended): Selecting this
          option will likely result in a large volume of issues. For
          more relevant and higher fidelity results, select the
          **From Cloud Accounts** option

    b.  Click Done.

#### Serverless function posture rules

##### Manage serverless function rules

Serverless function rules are designed to detect security threats within
your serverless function environment that can potentially introduce
vulnerabilities to its security. Serverless function rules identify and
flag issues based on predefined criteria, ensuring that potential
threats are proactively detected and addressed to enhance the overall
security posture of your serverless functions. There are three
categories or types of serverless function rules:

- **Attack Path**: These rules identify combined risks in your
  serverless function configurations, like overly permissive roles and
  network exposure, that could be exploited to breach your serverless
  applications

- **Config**: These rules detect security resource misconfigurations in
  your serverless function configurations and their related code and
  pipeline infrastructure

- **Network Exposure**: These rules detect internet-exposed serverless
  functions by leveraging network configurations monitored across your
  cloud environment

###### How to access serverless function rules

To access serverless function rules:

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Rules).

2.  Select the **Show filter panel** icon.

3.  Under the **Select field** menu, select the **Asset Types** category
    and select your cloud provider serverless function type from the
    **Select values** menu. Options:

    - **Azure Cloud Function**

    - **Google Cloud Function** (Gen 1 only)

    - **Lambda Function (AWS)**

- > **Note**

  > You can select multiple types to view all your serverless function
  > policies across your cloud providers.

  A table of serverless function rules filtered by asset type is
  displayed. Serverless functions properties unique or important enough
  to mention to serverless functions include:

  - **Provider**: The cloud provider (such as WAS) associated with the
    serverless function

  - **Severity**: The severity level of findings associated with the
    rule

  - **Asset Types**: The type of serverless function. Options: Lambda
    Function, Google Cloud Function, Azure Cloud Function

  - **Type**: The type of serverless function rule. Options: Attack
    Path, Config, Network Exposure

###### Manage serverless function rules

You can edit or clone serverless function rules.

- Edit a rule to fine-tune existing rules

- Clone a rule to saves time by reusing settings and applying policies
  uniformly across similar assets, ensuring standardized policies and
  predictable behavior

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Rules).

2.  Filter for the list of serverless function rules. Refer to [How to
    access serverless function
    rules](#Xebd85ecff894b4fbe63d82a6df588d016918bef) above for more
    information.

3.  Right-click on a rule.

    - To edit a rule, click **Edit**.

    <!-- -->

    - You are redirected to the **Overview** step of the **Edit Rule**
      wizard.

    <!-- -->

    - To clone a rule, select **Save as new**.

    <!-- -->

    - You are redirected to the **Overview** step of the new rules
      wizard.

- > **Note**

  > Refer to [Create serverless function
  > rules](#UUIDeaf3dd0d003040ba03c5e6234d7c46b4) for more information
  > on how to define the steps of a rule in the wizard.

##### Create serverless function rules

You can create custom rules for serverless functions to suit your
requirements. The following types of rules are supported:

- **Attack Path**: These rules monitor the high risk attack paths for
  potential breaches. Refer to [Create an attack path rule for
  serverless functions](#UUID220af99b0e301669679621abd1149575) for more
  information

- **Config**: These rules monitor resource configurations for potential
  breaches. Refer to [Create a configuration rule for serverless
  functions](#UUIDe2f0a0e1105ce2dca9657fa20a6f3469) for more information

- **Network Exposure**: These rules detect assets exposed to the
  internet. Refer to [Create a network exposure rule for serverless
  functions](#UUID6cdc6caf83d3b82dde546700349eeda5) for more information

##### Create an attack path rule for serverless functions

Attack Path policies for serverless functions identify critical risks
arising from interconnected weaknesses across your serverless
architecture (such as correlating findings across functions, triggers,
and permissions), to expose complex attack paths revealing complex
attack paths beyond individual findings.

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Rules) \> click Create Rule.

2.  Select **Attack Path**.

3.  On the **Overview** step of the **Create Attack Path Rule** wizard.

    a.  Fill in these fields.

        - **Rule Name**: (Required): A user-provided to identify the
          rule

        - **Rule Name**: (Required): A user-provided to identify the
          rule

        - **Description** (Required): A description of the policy

        - **Severity** (Required): Select the severity level. Only
          findings with this exact severity level will trigger this
          rule. Findings with different severity levels will be ignored

        - **Labels**: (Optional): Assign labels to categorize and
          organize the rule based on specific criteria or attributes.
          Labels help in easily identifying and filtering rules

        - **Enable How to Fix** (Optional. Default: **ON**): Enable to
          take action when the rule is violated

    b.  Click Next.

4.  Define the logic for the rule on the **Rule Logic** step of the
    wizard in the query editor.

    a.  Under the value menu in the **Find** field:

        i.  Select **Compute**.

        ii. In the corresponding table, search for a serverless
            function. Options: **Lambda Function**,
            **Google Cloud Function**, **Azure Cloud Function**.

    b.  Select the `+` icon in the editor.

    c.  Select an option: **Finding**, **Vulnerability**.

        - **Findings**: Define the logic for findings.

          i.  Provide the finding name. The name must match the name of
              the policy that will generate the security finding.

          ii. Click on the **Finding Name** card that is displayed In
              the **WHERE** field.

          iii. Select the value `in` under the **Operator** field.

          iv. Select the required finding or findings from the list that
              is displayed.

          v.  Click **Search**.

          - All assets matching the search criteria are displayed. This
            allows you to validate the rule\'s effectiveness on existing
            functions and provides valuable context for refining the
            rule\'s logic to accurately identify future functions.

          vi. Select Next.

          vii. Provide suggested mitigation in the **How to Fix** step
               and click **Done**.

        - **Vulnerability**: define the logic rule for types of
          vulnerabilities. Options: **CVE ID**,
          **Vulnerability Severity**, **CVSS Score**

          i.  **CVE ID**: Select in as the operator \> enter the CVE ID
              \> Search

    d.  Click **Next** if you have enabled a fix in step 1a above, or
        **Done** if fix is disabled.

5.  Define the fix in the **How to Fix** step (when enabled in step 1a
    above), and click Done.

##### Create a configuration rule for serverless functions

Config rules for serverless functions identify security
misconfigurations within the settings and deployment infrastructure of
your individual serverless resources.

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Rules) \> click Create Rule.

2.  Select **Config**.

3.  On the **Overview** step of the **Create Config Rule** wizard.

    a.  Fill in these fields:

        - **Rule Name**: (required): A user-provided to identify the
          rule

        - **Description** (required): A description of the rule

        - **Severity** (required): Select the severity level. Only
          findings with this exact severity level will trigger this
          rule. Findings with different severity levels will be ignored

        - **Labels**: (optional): Assign labels to categorize and
          organize the rule based on specific criteria or attributes.
          Labels help in easily identifying and filtering rules

        - **Enable How to Fix**: (Default: ON): Enable to take action
          when the rule is violated

    b.  Click Next.

4.  Define the logic for the configuration rule on the **Rule Logic**
    step of the wizard in the query editor.

    a.  Under the **Value** menu in the **Find** field:

        i.  Select **Compute**.

        ii. Select the relevant serverless function from the list that
            is displayed. Options: **Lambda Function**,
            **Google Cloud Function**, **Azure Cloud Function**.

        - The JSON configuration file for the selected serverless
          function is displayed. Note that each type of serverless
          function has a unique configuration file and unique
          properties.

    b.  Select a property or multiple properties of the serverless
        function configuration file and provide a value.

    c.  Click Search.

    - All assets matching the search criteria are displayed. This allows
      you to validate the rule\'s effectiveness on existing functions
      and provides valuable context for refining the rule\'s logic to
      accurately identify future functions.

    d.  Click **Next** if you have enabled a fix in step 1a above, or
        **Done** if fix is disabled.

5.  Define the fix in the **How to Fix** step (when enabled in step 1a
    above), and click Done.

##### Create a network exposure rule for serverless functions

Network Exposure rules allow you to monitor and control the network
accessibility of your serverless functions, identifying configurations
that might expose them to unwanted external traffic.

1.  Under **Posture Management**, select Rules & Policies \> Cloud
    Security (under Rules) \> click Create Rule.

2.  Select **Network Exposure**.

3.  On the **Overview** step of the **Create Network Exposure Rule**
    wizard.

    a.  Fill in these fields:

        - **Rule Name**: (required): A user-provided to identify the
          rule

        - **Description** (required): A description of the rule

        - **Severity** (required): Select the severity level. Only
          findings with this exact severity level will trigger this
          rule. Findings with different severity levels will be ignored

        - **Labels**: (optional): Assign labels to categorize and
          organize the rule based on specific criteria or attributes.
          Labels help in easily identifying and filtering rules

    b.  Click Next.

4.  Define the logic for the rule on the **Rule Logic** step of the
    wizard.

    a.  Fill in these fields:

        - **Source Network**: Select the source network to be evaluated
          by this rule. Options:

          - **Untrusted** (default): all internet IPs

          - A specific IP or CIDR range: Select
            **Show Advanced Settings** and fill in the following fields:

            - **Protocol/Port**: Specify the protocols and ports that
              will generate findings if exposed. For example: tcp/80,
              tcp/20-23, tcp/80, tcp/443

            - **Host State**: Configure the rule to alert on either
              active (running) or potentially exposed (stopped)
              workloads

            - **Use External Probe Validation**: When enabled, network
              scanning verifies internet exposure and provides
              additional context (protocols, ports, services). Disabling
              it relies on configuration alone, which may increase
              inaccurate findings

        - **Destination Asset Type**: Select **Serverless Function** as
          the asset type to be evaluated in the rule

        - **Cloud Service Provider**: Select the target cloud provider
          in which the rule will be evaluated (AWS, GCP, Azure)

    b.  Click Done.

#### Serverless function usage

Serverless functions is integrated as a feature across various sections
of your tenant. Refer to the following sections for specific usage
instructions within each context:

##### Serverless function assets

The **Serverless Functions** asset inventory provides a centralized view
of all serverless functions in your environment.

To access serverless function assets, under **Inventory**, select All
Assets \> Compute \> Serverless Functions.

For more information on serverless function assets, refer to [Manage
serverless function
assets](/document/preview/1330356#UUID-1b05c79b-a087-e32e-8fb6-bd6b4042f18c)

##### Serverless function issues

Currently, only vulnerability issues are supported for serverless
functions.

- To manage serverless function vulnerability issues through
  **Vulnerability Management**:

  1.  Navigate to Posture Management \> Vulnerability Management) \>
      Vulnerability Issues.

  2.  Select Add Filters \> Asset Category \> Serverless Function.

- To manage serverless function vulnerability issues through
  **Vulnerability Assets**:

  1.  Navigate to Posture Management \> Vulnerability Management) \>
      Vulnerable Assets.

  2.  Select Add Filters \> Asset Category \> Serverless Functions.

  3.  Select an asset in the inventory table.

  - The Overview tab is displayed.

  4.  Click on **Issues**.

  - You are redirected to the Issues page, displaying a list of
    serverless function vulnerabilities.

The serverless function vulnerabilities issues inventory includes these
unique properties:

- **Asset Type**: The type of serverless function: **Lamda Function**
  for AWS, **Google Cloud Function** for GCP and
  **Azure App Service Web App Function** for Azure

- **Asset Category**: Serverless Functions

Selecting an issue opens the expanded card with additional details about
the issue including a description of the issue, when fist and last
detected, affected assets, linked cases and evidence (such as the
vulnerability ID, CVSS severity, score and version, and the policy that
detected the issue).

For more information on vulnerability issues, refer to [Investigate and
remediate vulnerabilities](#UUID8ac80e5bbfbd3e830f52bd37b0c520e2).

##### Serverless function findings

1.  To manage serverless function findings, navigate to Posture
    Management \> Vulnerability Management) \> Vulnerability Issues.

2.  Select All Vulnerabilities Findings.

3.  Select Add Filters \> Asset Category \> Serverless Function.

4.  Select an asset in the inventory table.

For more information on vulnerability findings, refer to [View All
Vulnerability Findings](#UUID4083600dfe7d99bedd8e82ac8f21c712).

##### Monitor serverless function scan health

You can monitor and manage the health and status of your integrated
serverless function scans, troubleshoot errors and mitigate detected
vulnerabilities

For more information, refer to [Monitor serverless function scan
health](/document/preview/1338813#UUID-92106126-f00e-1ad1-0460-ac8e71cd514b).

### Serverless function runtime security

#### Overview

Cortex XSIAM enables runtime monitoring within a cloud environment by
embedding Cortex XDR agent directly into the code of the serverless
function. This allows for real-time monitoring of code execution,
processes, networking, and filesystem activity, along with the
enforcement of policies to permit or deny these actions. This in-depth
runtime visibility enhances the overall security of your serverless
functions.

Policy violations are detected and logged in Cortex Issues to allow for
effective scoping and analysis in order to thoroughly assess the issues.

##### Use cases

- **Visibility of policy violations in issues**: Use the Issues entity
  to view the policy violations of serverless functions that have
  occurred.  You can drill down and view information such as region,
  cloud function runtime, the specific serverless function name which
  indicates the issue that's occurred, cloud function request id which
  is the instance id from the cloud provider.

- **Monitor serverless functions in your cloud environment**: After
  embedding the agent in the function, the agent monitors for policy
  violations as defined in the profile you have configured.

##### Supported platforms

Runtime protection for serverless functions is available for Cortex
Cloud Runtime Security, Cortex XSIAM Premium, Cortex XSIAM Enterprise,
and Cortex XSIAM NG Siem licenses.

- Supported runtime environments: Python, Node.js. Refer to supported
  runtime versions for supported versions of Python and Node.js.

- Supported architecture: x86_64

- Supported cloud providers: Amazon Web Services (AWS): Amazon Lambda
  functions, Google Cloud Platform (GCP).

<!-- -->

- > **Note**

  - > For GCP Functions, Cortex supports: Cloud Functions (1st gen) and
    > Cloud Run functions (2nd gen) deployed by Cloud Functions API.
    > Refer to [Cloud Functions
    > API](https://cloud.google.com/functions/docs/reference/rest) for
    > more information.

  - > Google Cloud Run functions automatically creates and stores
    > container images in Google Artifact Registry (GAR) when uploading
    > code. For Cortex to scan images from Cloud Run functions, ensure
    > that Cortex is configured to scan all the registries in your GCP
    > account or at least the specific GAR where these images reside.

##### User roles and permissions

Granting access and configuration permissions to serverless function
capabilities in the Cortex tenant, you must verify that the user has the
correct settings in the linked role.

1.  Go to  Settings \> Configuration \> Access Management \> Roles.

2.  Go to the relevant role, right-click and select **Edit Role** and in
    the **Components** tab, verify under **Inventory**, that
    **Agent Profiles**, **Agent Installations** and
    **Agent Extension Policies** are configured to **View/Edit**.

#### Set up serverless function protection

Setting up serverless function protection includes:

1.  [Configure restriction profile for serverless
    functions](#UUID782ed1ba266abada97ca57d2dbd475e3)

2.  [Create a new policy rule for serverless
    functions](#UUIDf9602ef5969219a25fc6f9eef35849e5)

3.  [Create a serverless function agent
    package](#UUIDde47a28d94790584e7b55ebd6f68fdce)

#### Serverless runtime issues

You can view all serverless function issues detected by an agent and
generated from policy violations under **Issues** (under Cases & Issues)
inventories.

Every policy violation creates an issue per type:

- Process activity - enables specifying specific allowed list processes,
  blocking all processes except the main process and detecting crypto
  mining attempts.

- Network activity - enables monitoring and enforcement of DNS
  resolutions, inbound and outbound network connections.

- Filesystem activity - enables defining specific paths in an allowed or
  denied list.

Additional issues from specific policy violation are raised, which
include the same cloud provider, region, runtime, function name,
function version, issue name and issue description, will be suppressed.

The **Issues** page includes the following information indicating unique
serverless function issues raised by agents:

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Domain                            | For serverless, this is set to    |
|                                   | **Security**.                     |
+-----------------------------------+-----------------------------------+
| Category                          | For serverless, this is set to    |
|                                   | **Cloud**.                        |
+-----------------------------------+-----------------------------------+
| Name                              | For serverless, the relevant      |
|                                   | issue name appears:               |
|                                   |                                   |
|                                   | - Serverless function Network     |
|                                   |   Policy violation for outbound   |
|                                   |   ports                           |
|                                   |                                   |
|                                   | - Serverless function Network     |
|                                   |   Policy violation for listening  |
|                                   |   ports                           |
|                                   |                                   |
|                                   | - Serverless function Network     |
|                                   |   Policy violation for DNS        |
|                                   |                                   |
|                                   | - Serverless function Network     |
|                                   |   Policy violation for IPs        |
|                                   |                                   |
|                                   | - Serverless function File system |
|                                   |   Policy violation                |
|                                   |                                   |
|                                   | - Serverless function Process     |
|                                   |   Policy violation                |
+-----------------------------------+-----------------------------------+
| Detection method                  | For serverless, this is set to    |
|                                   | **XDR agent**.                    |
+-----------------------------------+-----------------------------------+
| Severity                          | For serverless, this is always    |
|                                   | set to **High**.                  |
+-----------------------------------+-----------------------------------+
| Cloud Function Runtime            | - Python                          |
|                                   |                                   |
|                                   | - Node.JS                         |
+-----------------------------------+-----------------------------------+
| Cloud Function Request ID         | Instance id from the cloud        |
|                                   | provider.                         |
+-----------------------------------+-----------------------------------+

> **Note**
>
> Issues triggered within 24 hours, sharing the same name and
> description, will be aggregated into cases along with issues from the
> same function per execution.

