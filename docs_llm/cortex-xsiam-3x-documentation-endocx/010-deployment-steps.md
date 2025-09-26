## Deployment steps

Review the plan and prepare considerations, and then use the onboarding
checklist to successfully deploy and onboard Cortex XSIAM.

### Plan and prepare

#### Prepare for deployment

Before you get started with Cortex XSIAM, consider the following:

- Determine the amount of log storage you need for your Cortex XSIAM
  deployment. Talk to your partner or sales representative to determine
  whether you must purchase additional storage within the Cortex XSIAM
  tenant.

- Determine the region in which you want to host Cortex XSIAM and any
  associated services, such as Directory Sync Service. If you plan to
  stream data from a Strata Logging Service instance, it must be in the
  same region as Cortex XSIAM. For more information, see [Cortex XSIAM
  supported regions](#UUID61479dc6978fbf5dda884f934ff79ef1).

- Determine the necessary bandwidth required to support the number of
  agents you plan to deploy. Allocate 1.2Mbps of bandwidth for every
  1,000 agents. This requirement scales proportionally. For example, if
  you plan to have 100,000 agents, you will need to allocate 120Mbps of
  bandwidth.

### Cortex XSIAM onboarding checklist

![](media/rId199.png){width="5.833333333333333in"
height="0.8677077865266841in"}

We recommend reviewing the following steps to successfully deploy and
onboard Cortex XSIAM:

+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Step               | Action                                        | Details                                                                                                                                | See more                                                                   |
+====================+===============================================+========================================================================================================================================+============================================================================+
| Step 1: Activate   | Activate and log in to Cortex Gateway         | 1.  Follow the instructions in the activation email and sign in to Cortex Gateway.                                                     | [See                                                                       |
| Cortex XSIAM       |                                               |                                                                                                                                        | topic](/document/preview/870141#UUID-13a2d2d5-ca89-5ea5-61c8-d2ca496397c2) |
|                    |                                               | 2.  Confirm license type.                                                                                                              |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| 1.  Enable access  | [See                                          |                                                                                                                                        |                                                                            |
|     to Cortex      | topic](#UUID24cb15454f44c259b484435238bb6a33) |                                                                                                                                        |                                                                            |
|     XSIAM          |                                               |                                                                                                                                        |                                                                            |
|     communication  |                                               |                                                                                                                                        |                                                                            |
|     servers,       |                                               |                                                                                                                                        |                                                                            |
|     storage        |                                               |                                                                                                                                        |                                                                            |
|     buckets, and   |                                               |                                                                                                                                        |                                                                            |
|     resources.     |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Step 2:            | Assign user roles                             | Start assigning roles directly to users or create user groups and assign roles to those groups.                                        | [See topic](#UUIDc0966cb32b3c88e214d33131de93fa8a)                         |
| Pre-installation   |                                               |                                                                                                                                        |                                                                            |
| steps for Cortex   |                                               |                                                                                                                                        |                                                                            |
| XDR agents         |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure how      | [See                                          |                                                                                                                                        |                                                                            |
| users access       | topic](#UUID9191b3fc18aa6b12fd020a24f8ed79a6) |                                                                                                                                        |                                                                            |
| Cortex XSIAM. You  |                                               |                                                                                                                                        |                                                                            |
| can authenticate   |                                               |                                                                                                                                        |                                                                            |
| users by doing one |                                               |                                                                                                                                        |                                                                            |
| or both of the     |                                               |                                                                                                                                        |                                                                            |
| following:         |                                               |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
| - User             |                                               |                                                                                                                                        |                                                                            |
|   authentication   |                                               |                                                                                                                                        |                                                                            |
|   through the      |                                               |                                                                                                                                        |                                                                            |
|   Customer Support |                                               |                                                                                                                                        |                                                                            |
|   Portal           |                                               |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
| - SAML single      |                                               |                                                                                                                                        |                                                                            |
|   sign-on in       |                                               |                                                                                                                                        |                                                                            |
|   the Cortex       |                                               |                                                                                                                                        |                                                                            |
|   XSIAM tenant     |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Verify endpoint    | Validate endpoint operating systems to ensure | [See                                                                                                                                   |                                                                            |
| operating systems  | they are compatible with Cortex XSIAM.        | topic](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Compatibility-Matrix/Endpoint-operating-systems-supported)     |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Define endpoint    | (Optional, can be performed post-deployment)  | [See topic](#UUIDf5ef98eec653f71f7752af7c075d9bb4)                                                                                     |                                                                            |
| groups             | Define an endpoint group to apply policy      |                                                                                                                                        |                                                                            |
|                    | rules and manage specific endpoints. If you   |                                                                                                                                        |                                                                            |
|                    | set up Cloud Identity Engine, you can also    |                                                                                                                                        |                                                                            |
|                    | leverage your Active Directory user, group,   |                                                                                                                                        |                                                                            |
|                    | and computer details in endpoint groups.      |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Customize endpoint | Customize your Endpoint Security Profiles and | [See topic](#UUID8e42879c93b8fb0cbaff1fe6544db66d)                                                                                     |                                                                            |
| security profiles  | assign them to your endpoints.                |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | Cortex XSIAM provides default security        |                                                                                                                                        |                                                                            |
|                    | profiles that you can use out-of-the-box to   |                                                                                                                                        |                                                                            |
|                    | immediately begin protecting your endpoints   |                                                                                                                                        |                                                                            |
|                    | from threats. Defaults include profiles for   |                                                                                                                                        |                                                                            |
|                    | exploits, malware, restrictions, agent        |                                                                                                                                        |                                                                            |
|                    | settings, and exceptions.                     |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | Review your policy rules and the security     |                                                                                                                                        |                                                                            |
|                    | profiles assigned to these rules and make any |                                                                                                                                        |                                                                            |
|                    | necessary adjustments.                        |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Enable enhanced    | Cortex XSIAM provides out-of-the-box exploit  | [See topic](/document/preview/868498#UUID-416260cf-dda6-2267-9eaa-b66a68471cb6)                                                        |                                                                            |
| data collection    | and malware protection. However, at minimum,  |                                                                                                                                        |                                                                            |
| from endpoints     | you must enable Data Collection in an Agent   | [See topic](#UUIDaaddafa52d3314d990ef6902ff3035ad)                                                                                     |                                                                            |
|                    | Settings profile to leverage endpoint data    |                                                                                                                                        |                                                                            |
|                    | in Cortex XSIAM.                              | [See topic](#UUID1075f7b0ff98ab957c3af79b79dc4d4e)                                                                                     |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | > **Note**                                    |                                                                                                                                        |                                                                            |
|                    | >                                             |                                                                                                                                        |                                                                            |
|                    | > Data collection for Windows endpoints is    |                                                                                                                                        |                                                                            |
|                    | > available with Traps 6.0 and later releases |                                                                                                                                        |                                                                            |
|                    | > and on endpoints running Windows 7 SP1 and  |                                                                                                                                        |                                                                            |
|                    | > later releases. Data collection on macOS    |                                                                                                                                        |                                                                            |
|                    | > and Linux endpoints are available with      |                                                                                                                                        |                                                                            |
|                    | > Traps 6.1 and later releases.               |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | 1.  Enable data collection in an Agent        |                                                                                                                                        |                                                                            |
|                    |     Settings profile to leverage endpoint     |                                                                                                                                        |                                                                            |
|                    |     data in Cortex XSIAM and use features     |                                                                                                                                        |                                                                            |
|                    |     such as Analytics or Host Insights.       |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | 2.  Attach the Agent Settings profile to a    |                                                                                                                                        |                                                                            |
|                    |     policy rule in order to apply it to       |                                                                                                                                        |                                                                            |
|                    |     selected endpoints.                       |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | 3.  Set global agent configurations that      |                                                                                                                                        |                                                                            |
|                    |     apply to all the endpoints in your        |                                                                                                                                        |                                                                            |
|                    |     network.                                  |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Step 3: Install    | Plan agent deployment                         | Plan your agent deployment.                                                                                                            | [See topic](#UUID92857c1f92746971d66e6a64fc15e8d1)                         |
| Cortex XDR agents  |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Keep Cortex XDR    | Recommended strategy and best practices for   | [See topic](#UUID5745e5298a488ded9008d9e01c219c1b)                                                                                     |                                                                            |
| agents and content | managing agent and content updates to help    |                                                                                                                                        |                                                                            |
| updated            | reduce the risk of downtime in a production   |                                                                                                                                        |                                                                            |
|                    | environment, while helping ensure timely      |                                                                                                                                        |                                                                            |
|                    | delivery of security content and              |                                                                                                                                        |                                                                            |
|                    | capabilities.                                 |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Create             | To reduce the network load and time typically | [See topic](#UUIDde47a28d94790584e7b55ebd6f68fdce)                                                                                     |                                                                            |
| installation       | required for the initial roll-out or major    |                                                                                                                                        |                                                                            |
| packages           | upgrades of the Cortex XDR agent, Cortex      |                                                                                                                                        |                                                                            |
|                    | XSIAM offers an agent installation and        |                                                                                                                                        |                                                                            |
|                    | content update distribution package.          |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Review the Cortex  | Until a Cortex XDR agent release reaches its  | [See                                                                                                                                   |                                                                            |
| XDR compatibility  | end-of-life (EoL) status, Palo Alto Networks  | topic](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Compatibility-Matrix/Agent-Versions-Supported-with-Cortex-XDR) |                                                                            |
| matrix             | provides the following support:               |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | - Microsoft operating systems are supported   |                                                                                                                                        |                                                                            |
|                    |   for three years beyond the end of Microsoft |                                                                                                                                        |                                                                            |
|                    |   support                                     |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | - Other operating system vendors are          |                                                                                                                                        |                                                                            |
|                    |   supported until they reach end-of-life.     |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
|                    | - Cortex XDR agents for macOS and 32-bit      |                                                                                                                                        |                                                                            |
|                    |   Windows are not FedRamp compliant.          |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Review Cortex XDR  | Check the list of agent versions that Cortex  | [See topic](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Compatibility-Matrix)                                     |                                                                            |
| agent              | XSIAM is compatible with. Contact Cortex      |                                                                                                                                        |                                                                            |
| compatibility with | XSIAM teams for insights on agent versions    |                                                                                                                                        |                                                                            |
| third-party        | that aren\'t listed.                          |                                                                                                                                        |                                                                            |
| security products  |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Deploy agent       | Deploy agent installation packages using a    | [See topic](#UUIDc7dd5578166668a2f571b6b7eeff300d)                                                                                     |                                                                            |
| installation       | third-party tool such as an SCCM, or manually |                                                                                                                                        |                                                                            |
| packages           | on the endpoint.                              |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Step 4: Configure  | Enable Cortex XSIAM analytics                 | Set up monitoring for internal networks.                                                                                               | [See topic](#UUID79661fb4f0136c198d25dbc9c7d9642e)                         |
| and deploy Cortex  |                                               |                                                                                                                                        |                                                                            |
| XSIAM              |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Activate Cortex    | [See                                          |                                                                                                                                        |                                                                            |
| XSIAM Analytics to | topic](#UUIDefaf1a2cc1ea98a077d09b52d3ed5cc4) |                                                                                                                                        |                                                                            |
| enable the         |                                               |                                                                                                                                        |                                                                            |
| analytics engine   |                                               |                                                                                                                                        |                                                                            |
| to analyze your    |                                               |                                                                                                                                        |                                                                            |
| endpoint data to   |                                               |                                                                                                                                        |                                                                            |
| develop a baseline |                                               |                                                                                                                                        |                                                                            |
| and generate       |                                               |                                                                                                                                        |                                                                            |
| analytics and      |                                               |                                                                                                                                        |                                                                            |
| analytics BIOC     |                                               |                                                                                                                                        |                                                                            |
| issues when        |                                               |                                                                                                                                        |                                                                            |
| anomalies and      |                                               |                                                                                                                                        |                                                                            |
| malicious          |                                               |                                                                                                                                        |                                                                            |
| behaviors are      |                                               |                                                                                                                                        |                                                                            |
| detected.          |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| (Optional but      |                                               |                                                                                                                                        |                                                                            |
| highly             |                                               |                                                                                                                                        |                                                                            |
| recommended)       |                                               |                                                                                                                                        |                                                                            |
| Enable Identity    |                                               |                                                                                                                                        |                                                                            |
| Analytics to       |                                               |                                                                                                                                        |                                                                            |
| aggregate and      |                                               |                                                                                                                                        |                                                                            |
| display user       |                                               |                                                                                                                                        |                                                                            |
| profile details,   |                                               |                                                                                                                                        |                                                                            |
| activities, and    |                                               |                                                                                                                                        |                                                                            |
| issues related to  |                                               |                                                                                                                                        |                                                                            |
| a user-based       |                                               |                                                                                                                                        |                                                                            |
| analytics type     |                                               |                                                                                                                                        |                                                                            |
| issue and          |                                               |                                                                                                                                        |                                                                            |
| Analytics BIOC     |                                               |                                                                                                                                        |                                                                            |
| rule during an     |                                               |                                                                                                                                        |                                                                            |
| investigation.     |                                               |                                                                                                                                        |                                                                            |
|                    |                                               |                                                                                                                                        |                                                                            |
| > **Prerequisite** |                                               |                                                                                                                                        |                                                                            |
| >                  |                                               |                                                                                                                                        |                                                                            |
| > Cloud Identity   |                                               |                                                                                                                                        |                                                                            |
| > Engine must be   |                                               |                                                                                                                                        |                                                                            |
| > set up.          |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| (Optional but      | Broker VM is used to proxy all Cortex         | [See topic](#UUIDa2b1b832d74850d81f427e175514c501)                                                                                     |                                                                            |
| highly             | XDR/Traps agent communication to provide a    |                                                                                                                                        |                                                                            |
| recommended) Set   | more predictable flow of traffic to and from  |                                                                                                                                        |                                                                            |
| up and configure   | the cloud for heartbeats, agent updates,      |                                                                                                                                        |                                                                            |
| Broker VM          | content updates, and more. It is also used to |                                                                                                                                        |                                                                            |
|                    | serve as a Syslog collection point for all    |                                                                                                                                        |                                                                            |
|                    | third-party log ingestion.                    |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| (Optional but      | Pathfinder is used to examine network hosts,  | [See topic](#UUIDedfbabf66d30717d0d0ef54801b8cf35)                                                                                     |                                                                            |
| highly             | servers, and workstations for malicious or    |                                                                                                                                        |                                                                            |
| recommended)       | risky software.                               |                                                                                                                                        |                                                                            |
| Activate           |                                               |                                                                                                                                        |                                                                            |
| Pathfinder         |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| (Optional but      | Cloud Identity Engine is a complimentary      | [See topic](#UUID586f81e7ddbd6968328cbd7809bd7eaa)                                                                                     |                                                                            |
| highly             | service that enables you to leverage Active   |                                                                                                                                        |                                                                            |
| recommended)       | Directory user, group, and computer details   |                                                                                                                                        |                                                                            |
| Install Cloud      | in Cortex XSIAM to provide context when you   |                                                                                                                                        |                                                                            |
| Identity Engine    | investigate alerts. You can also use Active   |                                                                                                                                        |                                                                            |
|                    | Directory information in policy configuration |                                                                                                                                        |                                                                            |
|                    | and endpoint management of Traps agents.      |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Install engines    | Install an engine on a remote machine to      | [See topic](#UUID252e9afbac843ebaf0c43a2d8bd0be22)                                                                                     |                                                                            |
|                    | allow communication between the remote        |                                                                                                                                        |                                                                            |
|                    | machine and Cortex XSIAM.                     |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Step 5: Define     | Configure data ingestion                      | To provide you with a more complete and detailed picture of the activity involved in an incident, Cortex XSIAM can ingest data from a  | [See topic](#UUID00d964f3e91bf4f6d19a763269659fad)                         |
| data sources and   |                                               | variety of Palo Alto Networks, cloud, and third-party sources.                                                                         |                                                                            |
| integrations       |                                               |                                                                                                                                        |                                                                            |
+--------------------+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

### Activate Cortex XSIAM

To activate a tenant, you need to log in to Cortex Gateway, a
centralized portal for activating and managing tenants, users, roles,
and user groups. After activating the tenant, you can then access the
tenant. You must repeat this task for each tenant if you have multiple
tenants. The activation process involves accessing Cortex Gateway,
activating the tenant, and then accessing the tenant\'s resources.

> **Prerequisite**

- > The Cortex XSIAM activation email.

- > A Customer Support Portal (CSP) account.

<!-- -->

- > You need to set up your CSP account. For more information, see [How
  > to Create Your CSP User
  > Account](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNVCA0).

  > When you create a CSP account, you can set up two-factor
  > authentication (2FA) to log into the CSP by using an Email, Okta
  > Verify, or Google Authenticator (non-FedRAMP accounts). For more
  > information, see [How to Enable a Third Party
  > IdP](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA14u000000sZ8mCAE).

<!-- -->

- > You have one of the following roles assigned:

+-----------------------------------+-----------------------------------+
| > Role                            | > Description                     |
+===================================+===================================+
| > CSP role                        | > The Super User role is assigned |
|                                   | > to your CSP account. The user   |
|                                   | > who creates the CSP account is  |
|                                   | > granted the Super User role.    |
+-----------------------------------+-----------------------------------+
| > Cortex role                     | > You must have the Account Admin |
|                                   | > role.                           |
|                                   | >                                 |
|                                   | > If you are the first user to    |
|                                   | > access Cortex Gateway with the  |
|                                   | > CSP Super User role, you are    |
|                                   | > automatically granted Account   |
|                                   | > Admin permissions for the       |
|                                   | > Cortex Gateway. You can also    |
|                                   | > add Account Admin users as      |
|                                   | > required.                       |
|                                   | >                                 |
|                                   | > In the Cortex Gateway, you can  |
|                                   | > activate new tenants, access    |
|                                   | > existing tenants, and create    |
|                                   | > and manage role-based access    |
|                                   | > control (RBAC) for all of your  |
|                                   | > tenants.                        |
+-----------------------------------+-----------------------------------+

**How to activate Cortex XSIAM**

1.  Log in to [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/signin/).

- You can also access the link from the activation email.

2.  Enter your username and password or multi-factor authentication (if
    set up) by using your Customer Support Portal account credentials to
    sign in.

- After you sign in, you can view the following:

  - If you are a CSP Account Admin, you can see tenants allocated to
    your CSP account and ready for activation. After activation, you
    cannot move your tenant to a different CSP account.

  - Tenant details such as license type, number of endpoints, and
    purchase date.

  - Tenants that were activated and are now available. If you have more
    than one Customer Support Portal account, the tenants are displayed
    according to the Customer Support Portal account name.

3.  In the **Available for Activation** section, use the serial number
    to locate the tenant that needs activation, and then click
    **Activate**.

- > **Note**

  > When you activate, a production tenant is first activated. After
  > activation, you can set up a development tenant (subject to your
  > license).

4.  On the **Tenant Activation** page, define the following:

+-----------------------------------+--------------------------------------------------------+
| Parameter                         | Description                                            |
+===================================+========================================================+
| Tenant Name                       | Enter the name of the tenant. Use a unique name across |
|                                   | your company account up to 59 characters long.         |
+-----------------------------------+--------------------------------------------------------+
| Region                            | Geographic location where your tenant will be hosted.  |
|                                   | For more information about supported regions, see      |
|                                   | [Cortex XSIAM supported                                |
|                                   | regions](#UUID61479dc6978fbf5dda884f934ff79ef1).       |
+-----------------------------------+--------------------------------------------------------+
| Tenant Subdomain                  | DNS record associated with your tenant. Enter a name   |
|                                   | that will be used to access the tenant directly using  |
|                                   | the full URL:                                          |
|                                   |                                                        |
|                                   | `https://<subdomain>xdr.<region>.paloaltonetworks.com` |
+-----------------------------------+--------------------------------------------------------+
| Encryption Method                 | (Optional) If you want to bring your own keys for      |
|                                   | encrypting your data, under **Advanced**, select       |
|                                   | **BYOK** and follow the instructions of the wizard as  |
|                                   | detailed in **Encryption Method**.                     |
|                                   |                                                        |
|                                   | - Default encryption (recommended)                     |
|                                   |                                                        |
|                                   | <!-- -->                                               |
|                                   |                                                        |
|                                   | - All data stored by Cortex XSIAM is encrypted at rest |
|                                   |   using a dedicated key management system. Cortex      |
|                                   |   XSIAM provides strict key access controls and        |
|                                   |   auditing, and encrypts user data at rest according   |
|                                   |   to AES-256 encryption standards. We recommend all    |
|                                   |   our customers use this default system.               |
|                                   |                                                        |
|                                   | <!-- -->                                               |
|                                   |                                                        |
|                                   | - BYOK (Bring your own keys)                           |
|                                   |                                                        |
|                                   | <!-- -->                                               |
|                                   |                                                        |
|                                   | - BYOK (Bring Your Own Keys) enables you to generate   |
|                                   |   your own encryption keys and securely import and     |
|                                   |   manage them via Cortex Gateway to retain greater     |
|                                   |   control over your tenant data and encryption. This   |
|                                   |   requires [further                                    |
|                                   |   setup](#UUIDb6b90a5112c8fc508777a930771fdbb9).       |
+-----------------------------------+--------------------------------------------------------+

5.  Review and
    **agree to the terms and conditions of the Privacy policy, Terms of Use, and EULA**
    , and then **Activate** your tenant.

- > **Note**

  > Activation can take about an hour and does not require you to remain
  > on the activation page. Cortex XSIAM sends a notification to your
  > email when the process is complete.

6.  After activation, from Cortex Gateway, in the **Available Tenants**,
    when hovering over the activated tenant, do the following:

    - Ensure that you can successfully access the tenant by clicking the
      Cortex XSIAM tenant name (when the tenant is active).

    - In the dialog box, view the tenant status, region, serial number,
      and license details.

    <!-- -->

    - > **Note**

      > If you want to change your tenant\'s name, the subdomain, or
      > activate a development tenant (subject to license), on the
      > right-hand side, click the ellipsis.

      > You can only change the subdomain once, and it cannot be undone.

      > After deleting the subdomain, you can reuse it after 7 days.

7.  Enable and verify access to  Cortex XSIAM communication servers,
    storage buckets, and various resources in your firewall
    configuration. For more information, see [Enable access to required
    PANW resources](#UUID24cb15454f44c259b484435238bb6a33).

#### Bring your own keys

> **Prerequisite**
>
> Access to BYOK (Bring Your Own Keys) functionality is restricted to
> tenants that were initially activated with BYOK.

##### What is Cortex BYOK?

Cortex self-managed BYOK (bring your own keys) offers a comprehensive
data encryption solution, empowering enterprises to assert complete
authority over their encryption key management, while ensuring platform
reliability, availability, and responsiveness. It enables you to
securely import and manage your own encryption keys via Cortex Gateway.
This provides you with enhanced control over your tenant data encryption
and accessibility, eliminates reliance on default CSP encryption or
third-party key management, and enables you to comply with stringent
regulatory requirements.

Unlike self-hosted solutions, Cortex BYOK minimizes exposure to external
risks, such as downtime, breaches, or operational disruptions, by
reducing dependency on external environments, ensuring availability and
responsiveness of your Cortex products.

By default, Google Cloud encrypts customer data at rest using envelope
encryption, where randomly generated Data Encryption Keys (DEKs) encrypt
the data, and Google-managed Key Encryption Keys (KEKs) wrap the DEKs,
all protected within Google\'s multi-layered key hierarchy. Cortex BYOK
enhances this model by allowing customers to generate and supply their
own KEK, which is securely imported into PANW\'s tenant-specific Key
Management Service (KMS) environment on Google Cloud. The
customer-provided KEK is used to encrypt the DEKs that protect tenant
data, giving customers control over key management through the Cortex
Gateway. While PANW securely manages encryption operations within its
cloud environment, customers retain authority over the KEK, achieving
greater control and auditability.

**Cortex BYOK architecture**

Cortex BYOK leverages a dedicated Key Management Service (KMS) deployed
per tenant within PANW\'s GCP-based infrastructure. Each tenant has its
own isolated KMS instance, ensuring complete separation of key material.

In multitenant environments, each tenant has its own isolated KMS
instance and keys, and each one is managed independently.

Two separate keys are used for encrypting tenant data: one for BigQuery
and another for other services.

**Security measures**

Cortex BYOK ensures key material is wrapped for protection in transit,
and access to the wrapping key is limited solely to the scope of the
import job.

The key material is unwrapped solely within the tenant's KMS using the
import job\'s private key and is inserted as a new version of the target
key on the target key ring through an atomic operation. This ensures
that no key material is left exposed or in an untrusted state, keeping
it secure and preventing potential vulnerabilities, while maintaining
its integrity and consistency.

Cortex also provides detailed audit logs within the tenant on all key
management operations.

Email notifications are sent for any key management operations, allowing
tenant administrators to monitor and review all activities and detect
and mitigate any unauthorized access attempts.

##### BYOK key management operations

BYOK supports the following key management operations. Cortex XSIAM
provides detailed audit logs and email notifications on all key
management operations.

To import a new encryption key, whether for initial tenant setup or key
rotation, use the Bring your own keys (BYOK) setup.

Set up new tenant with BYOK

Generate your own encryption keys and import them via Cortex Gateway to
retain greater control over your tenant data and encryption. This
control enables you to implement customized security measures tailored
to your organization's needs and compliance requirements for encrypting
your tenant data at rest.

Cortex BYOK uses two keys for encrypting your tenant data at rest: one
for BigQuery and another for all other tenant services. You can generate
a single key for both or create two separate keys.

- If you\'re doing the activation for the first time, in the Cortex
  Gateway, follow the [Tenant Activation
  wizard](/document/preview/870141#UUID-13a2d2d5-ca89-5ea5-61c8-d2ca496397c2).
  In Tenant Activation \> Define Tenant Settings, under **Advanced**,
  select **BYOK (Bring Your Own Keys)** and click
  **Create Tenant and Set Up Keys**.

<!-- -->

- The tenant is now initialized, which may take a few minutes. You can
  [set up your keys](#sidebaridm234412014574743) now, or return at a
  later stage and click **Set Up Encryption Keys** next to the tenant in
  the gateway to continue the process.

<!-- -->

- If you\'ve already started the activation process and paused, locate
  your tenant in the Available Tenants list in the Cortex gateway, click
  **Set Up Encryption Keys** next to your tenant and [set up your
  keys](#sidebaridm234412014574743).

Rotate encryption keys

To rotate your encryption keys, in the Cortex gateway, open the more
options menu next to the tenant, select **Rotate Encryption Key**, and
follow the [Bring your own keys (BYOK)
setup](#sidebaridm234412014574743).

To resume the process, in the main gateway, open the moremenu next to
the tenant, select **Continue Rotation**, and follow the [Bring your own
keys (BYOK) setup](#sidebaridm234412014574743).

As long as the rotation hasn\'t been completed, you can cancel the
rotation process from the three dot menu next to the tenant.

> **Note**
>
> The new keys you import will serve as primary encryption keys for
> newly generated data.

Disable encryption keys

To disable your encryption keys, in the main gateway, open the three dot
menu next to the tenant, select
**Disable All Keys & Deactivate Tenant**.

> **Warning**
>
> To disable your encryption keys and deactivate a tenant, you must have
> an Account Admin role.
>
> **Caution**
>
> Disabling all encryption keys and deactivating the tenant renders the
> tenant inaccessible and non-operational.
>
> Disabling the keys affects the communication with the agents, may
> prevent the agents from receiving updates to policies, configurations,
> and crucial information, and may result in loss of data.
>
> To secure your tenant data and to prevent unauthorized access,
> re-enabling the keys and re-activating the tenant are strictly
> controlled and require manual intervention by the Cortex XSIAM
> Customer Success team.

##### Bring your own keys (BYOK) setup

Cortex BYOK uses two keys for encrypting your data at rest. One key is
for BigQuery and the other is for all the other services within the
tenant. You can generate a single key for both or create two separate
keys for each service.

After completing the process, the imported keys become the primary keys
used for encrypting any newly generated data stored within the tenant.

> **Note**
>
> At any stage, you can select **Continue Later** to pause the process.
> To resume the process, in the Cortex gateway, select
> **Continue Setup** next to the tenant, and follow the wizard
> instructions from the point you left off, as detailed below. If you
> don\'t use either of your wrapping keys within three days, they expire
> and you\'ll have to restart the process.

Import new keys for encrypting your tenant data at rest:

1.  The **Generate Key** screen helps you generate an encryption key.

- > **Note**

  > BYOK requires a 32-byte, symmetric, unencoded key in binary format.

  Generate a key that meets these requirements using your preferred
  method or use the provided OpenSSL command:

      openssl rand 32 <FILENAME>

  When your encryption key is ready, select
  **I have a 32-byte symmetric encryption key ready** and click
  **Next**.

2.  In the **Wrap & Upload** screen, repeat the following procedure for
    both **Data lake wrapping key** and **Services wrapping key**.

    a.  Download the wrapping key.

    - The wrapping key is valid for up to three days. After three days,
      you need to download a new wrapping key.

    b.  Use an OpenSSL editor to wrap your encryption key using the
        following code:

    - openssl pkeyutl \  
          -encrypt \  
          -pubin \  
          -inkey <WRAPPING_KEY_FULL_PATH> \  
          -in <YOUR_32_BYTE_KEY_FULL_PATH> \ 
          -out <TARGET_WRAPPED_KEY_FULL_PATH> \  
          -pkeyopt rsa_padding_mode:oaep \  
          -pkeyopt rsa_oaep_md:sha256 \  
          -pkeyopt rsa_mgf1_md:sha256

    c.  Upload the wrapping key and click **Complete Activation**.

#### Cortex XSIAM supported regions

The following table lists the regions available to host Cortex XSIAM and
any associated Cortex services:

+-----------------------------------+-----------------------------------+
| Country                           | Description                       |
+===================================+===================================+
| Australia (AU)                    | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of          |
|                                   | Australia.                        |
+-----------------------------------+-----------------------------------+
| Canada (CA)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Canada.  |
|                                   | However, if you have a WildFire   |
|                                   | Canada cloud subscription,        |
|                                   | consider the following:           |
|                                   |                                   |
|                                   | - You cannot send file            |
|                                   |   submissions for bare-metal      |
|                                   |   analysis.                       |
|                                   |                                   |
|                                   | - You will not be protected       |
|                                   |   against macOS-borne zero-day    |
|                                   |   threats. However, you will      |
|                                   |   receive protection against      |
|                                   |   other macOS malware in regular  |
|                                   |   WildFire updates.               |
|                                   |                                   |
|                                   | - You will not be able to view    |
|                                   |   file submissions in AutoFocus.  |
+-----------------------------------+-----------------------------------+
| Europe (EU)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Europe.  |
+-----------------------------------+-----------------------------------+
| France (FR)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of France.  |
+-----------------------------------+-----------------------------------+
| Germany (DE)                      | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Germany. |
+-----------------------------------+-----------------------------------+
| India (IN)                        | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of India.   |
+-----------------------------------+-----------------------------------+
| Indonesia (ID)                    | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of          |
|                                   | Indonesia.                        |
+-----------------------------------+-----------------------------------+
| Israel (IL)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Israel.  |
+-----------------------------------+-----------------------------------+
| Italy (IT)                        | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Italy.   |
+-----------------------------------+-----------------------------------+
| Japan (JP)                        | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Japan.   |
+-----------------------------------+-----------------------------------+
| Poland (PL)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Poland.  |
+-----------------------------------+-----------------------------------+
| Qatar (QT)                        | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Qatar.   |
+-----------------------------------+-----------------------------------+
| Saudi Arabia (SA)                 | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Saudi    |
|                                   | Arabia.                           |
+-----------------------------------+-----------------------------------+
| Singapore (SG)                    | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of          |
|                                   | Singapore.                        |
+-----------------------------------+-----------------------------------+
| South Africa (ZA)                 | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of South    |
|                                   | Africa.                           |
+-----------------------------------+-----------------------------------+
| South Korea (KR)                  | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of South    |
|                                   | Korea.                            |
+-----------------------------------+-----------------------------------+
| Spain (ES)                        | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Spain.   |
+-----------------------------------+-----------------------------------+
| Switzerland (CH)                  | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of          |
|                                   | Switzerland.                      |
+-----------------------------------+-----------------------------------+
| Taiwan (TW)                       | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of Taiwan.  |
+-----------------------------------+-----------------------------------+
| United Kingdom (UK)               | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of the      |
|                                   | United Kingdom.                   |
+-----------------------------------+-----------------------------------+
| United States (US)                | All Cortex XSIAM logs and         |
|                                   | ingested data remain hosted       |
|                                   | within the boundaries of the      |
|                                   | United States.                    |
+-----------------------------------+-----------------------------------+

#### Enable access to required PANW resources

After you receive your account details, enable and verify access to
 Cortex XSIAM communication servers, storage buckets, and various
resources in your firewall configuration.

Some of the IP addresses required for access are registered in the
United States. As a result, some GeoIP databases do not correctly
pinpoint the location in which IP addresses are used. All customer data
is stored in your deployment region, regardless of the IP address
registration, and restricts data transmission through any infrastructure
to that region.

Keep in mind the following guidelines:

- If you use the specific Palo Alto Networks App-IDs indicated in the
  tables, you do not need to allow access to the resource.

- A dash (---) indicates there is no App-ID coverage for a resource.
  Enable access from the agent to the console; this does not need to be
  bidirectional.

- For IP address ranges in Google Cloud Platform (GCP), refer to these
  lists for IP address coverage for your deployment:

  - <https://www.gstatic.com/ipranges/goog.json>: IP address subnet
    ranges

  - <https://www.gstatic.com/ipranges/cloud.json>: IP address ranges
    associated with your region

- If you use SSL decryption and experience difficulty in connecting the
  Cortex XDR agent to the server, we recommend that you add the FQDNs
  required for access to your SSL Decryption Exclusion list.

<!-- -->

- In PAN-OS 8.0 and later releases, you can configure the list in Device
  \> Certificate Management \> SSL Decryption Exclusion.

> **Note**
>
> `<tenant-name>` refers to the selected subdomain of your Cortex XSIAM
> tenant, and `<region>` is the region in which your tenant is deployed.
> For more information, see [Cortex XSIAM supported
> regions](#UUID61479dc6978fbf5dda884f934ff79ef1).

The following table lists the required resources by region, including
FQDNs, IP addresses, ports, and App-ID coverage for your deployment:

+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| FQDN                                                                                                          | IP Addresses and Port | App-ID Coverage            |
+===============================================================================================================+=======================+============================+
| `<tenant-name>.xdr.<region>.paloaltonetworks.com`                                                             | IP address by region: | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to connect to the Cortex XSIAM tenant.                                                                   | - US (United States): |                            |
|                                                                                                               |   35.244.250.18       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   35.227.237.180      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   34.120.31.199       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   34.120.87.77        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   35.241.28.254       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.117.211.129      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   34.120.229.65       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   34.98.68.183        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   35.186.207.80       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.111.6.153        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   34.117.240.208      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   34.160.28.41        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   35.190.0.180        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.111.134.57       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.111.129.144      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   35.244.157.127      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.111.58.152       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.111.188.248      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.8.224.70         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.54.5.247         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   34.149.165.12       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `distributions.traps.paloaltonetworks.com`                                                                    | - IP address:         | `traps-management-service` |
|                                                                                                               |   35.223.6.69         |                            |
| Used for the first request in registration flow where the agent passes the distribution id and obtains the    |                       |                            |
| `ch-<tenant-name>.traps.paloaltonetworks.com` of its tenant.                                                  | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `wss://lrc-<region>.paloaltonetworks.com`                                                                     | IP address by region: | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used in live terminal flow.                                                                                   | - US (United States): |                            |
|                                                                                                               |   35.190.88.43        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   35.244.251.25       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   35.203.99.74        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   35.242.159.176      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   34.84.201.32        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.87.61.186        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   35.244.66.177       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   34.107.61.141       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   35.200.146.253      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.65.213.226       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   34.118.62.80        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   34.80.34.30         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.18.34.73         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.163.57.57        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.165.43.106       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.166.54.6         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.101.214.157      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.175.18.78        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.154.154.5        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.22.66.91         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   34.35.56.170        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-installers-prod-us.storage.googleapis.com`                                                          | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to download installers for upgrade actions from the server.                                              | - Port: 443           |                            |
|                                                                                                               |                       |                            |
| This storage bucket is used for all regions.                                                                  |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-payloads-prod-us.storage.googleapis.com`                                                            | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to download the executable for live terminal for XDR agents earlier than version 7.1.0.                  | - Port: 443           |                            |
|                                                                                                               |                       |                            |
| This storage bucket is used for all regions.                                                                  |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `global-content-profiles-policy.storage.googleapis.com`                                                       | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to download content updates.                                                                             | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-evr-prod-<region>.storage.googleapis.com`                                                           | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to download extended verdict request results in scanning.                                                | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `https://<region>-docker.pkg.dev`                                                                             | - IP ranges in GCP    |                            |
|                                                                                                               |                       |                            |
| Used to download the Kubernetes image from the registry for Kubernetes agents installation.                   | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `dc-<tenant-name>.traps.paloaltonetworks.com`                                                                 | IP address by region: | `traps-management-service` |
|                                                                                                               |                       |                            |
| Used for EDR data upload.                                                                                     | - US (United States): |                            |
|                                                                                                               |   34.98.77.231        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   34.102.140.103      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   34.96.120.25        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   35.244.133.254      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   34.95.66.187        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.120.142.18       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   34.102.237.151      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   34.107.161.143      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   34.120.213.187      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.149.180.250      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   35.190.13.237       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   34.149.248.76       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.107.129.254      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.36.155.211       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.128.157.130      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.107.213.85       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.128.156.84       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.120.102.147      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.8.234.58         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.54.155.245       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   35.190.79.68        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `ch-<tenant-name>.traps.paloaltonetworks.com`                                                                 | IP address by region: | `traps-management-service` |
|                                                                                                               |                       |                            |
| Used for all other requests between the agent and its tenant server including heartbeat, uploads, action      | - US (United States): |                            |
| results, and scan reports.                                                                                    |   34.98.77.231        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   34.102.140.103      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   34.96.120.25        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   35.244.133.254      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   34.95.66.187        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.120.142.18       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   34.102.237.151      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   34.107.161.143      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   34.120.213.188      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.149.180.250      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   35.190.13.237       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   34.149.248.76       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.107.129.254      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.36.155.211       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.128.157.130      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.107.213.85       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.128.156.84       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.120.102.147      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.8.234.58         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.54.155.245       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   35.190.79.68        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `api-<tenant-name>.xdr.<region>.paloaltonetworks.com`                                                         | IP address by region: | ---                        |
|                                                                                                               |                       |                            |
| Used for API requests and responses and to connect to an engine.                                              | - US (United States): |                            |
|                                                                                                               |   35.222.81.194       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   34.90.67.58         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   35.203.82.121       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   34.89.56.78         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   34.84.125.129       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.87.83.144        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   35.189.18.208       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   34.107.57.23        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   35.200.158.164      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.65.248.119       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   34.116.216.55       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   35.234.8.249        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.18.46.240        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.155.222.152      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.165.156.139      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.166.58.79        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.128.115.238      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.175.30.176       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.154.195.120      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.64.54.175        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   34.35.64.191        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `cc-<tenant-name>.traps.paloaltonetworks.com`                                                                 | IP address by region: | `traps-management-service` |
|                                                                                                               |                       |                            |
| Used for get-verdict requests.                                                                                | - US (United States): |                            |
|                                                                                                               |   35.224.140.142      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   34.90.71.103        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   35.203.35.23        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   34.89.42.214        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan):         |                            |
|                                                                                                               |   34.84.225.105       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   35.247.161.94       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   35.201.23.188       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   35.242.201.199      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   35.244.57.196       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.65.137.215       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   34.116.213.71       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   35.229.186.216      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.18.53.229        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.155.110.169      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.165.2.110        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.166.53.160       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.101.155.198      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.175.205.166      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.154.230.76       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.64.228.117       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   34.35.13.198        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **Broker VM Resources**                                                                                       |                       |                            |
|                                                                                                               |                       |                            |
| Required for deployments that use Broker VM features                                                          |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| [xdr-ova-installers-prod-us.storage.googleapis.com](http://xdr-ova-installers-prod-us.storage.googleapis.com) | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                                                               |                       |                            |
| Used to download Broker VM images from the server.                                                            | - Port: 443           |                            |
|                                                                                                               |                       |                            |
| This storage bucket is used for all regions.                                                                  |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `br-<tenant-name>.xdr.<region>.paloaltonetworks.com`                                                          | IP address by region: | ---                        |
|                                                                                                               |                       |                            |
|                                                                                                               | - US (United States): |                            |
|                                                                                                               |   104.155.131.72      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe):        |                            |
|                                                                                                               |   34.91.128.226       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada):        |                            |
|                                                                                                               |   34.95.8.232         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United          |                            |
|                                                                                                               |   Kingdom):           |                            |
|                                                                                                               |   35.197.219.110      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP                  |                            |
|                                                                                                               |   (Japan):34.85.74.43 |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore):     |                            |
|                                                                                                               |   34.87.167.125       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia):     |                            |
|                                                                                                               |   35.244.93.0         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany):       |                            |
|                                                                                                               |   35.198.112.13       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India):         |                            |
|                                                                                                               |   35.200.234.99       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland):   |                            |
|                                                                                                               |   34.65.51.103        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland):        |                            |
|                                                                                                               |   34.116.176.97       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan):        |                            |
|                                                                                                               |   34.80.230.166       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar):         |                            |
|                                                                                                               |   34.18.37.73         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France):        |                            |
|                                                                                                               |   34.155.90.61        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel):        |                            |
|                                                                                                               |   34.165.24.222       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia):  |                            |
|                                                                                                               |   34.166.55.153       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia):     |                            |
|                                                                                                               |   34.101.101.170      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain):         |                            |
|                                                                                                               |   34.175.182.55       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy):         |                            |
|                                                                                                               |   34.154.168.139      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea):   |                            |
|                                                                                                               |   34.64.46.249        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |   34.35.45.251        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | Port: 443             |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| `distributions.traps.paloaltonetworks.com`                                                                    | - IP address:         | `traps-management-service` |
|                                                                                                               |   35.223.6.69         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| - `time.google.com`                                                                                           | UDP port: 123         | ---                        |
|                                                                                                               |                       |                            |
| - `pool.ntp.org`                                                                                              |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **App Login and Authentication**                                                                              |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| identity.paloaltonetworks.com                                                                                 | - IP address:         | ---                        |
|                                                                                                               |   34.120.119.85       |                            |
| (SSO)                                                                                                         |                       |                            |
|                                                                                                               | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| login.paloaltonetworks.com                                                                                    | - IP address:         | ---                        |
|                                                                                                               |   34.102.139.110      |                            |
| (SSO)                                                                                                         |                       |                            |
|                                                                                                               | - Port: 443           |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **In-App Help Center and Notifications**                                                                      |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| data.pendo.io                                                                                                 | Port: 443             | ---                        |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| pendo-static-5664029141630976.storage.googleapis.com                                                          | Port: 443             | ---                        |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **Email Notifications**                                                                                       |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| ---                                                                                                           | IP address for all    | ---                        |
|                                                                                                               | regions:              |                            |
|                                                                                                               | 159.183.150.248       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **Egress**                                                                                                    |                       |                            |
|                                                                                                               |                       |                            |
| Used for communication between Cortex XSIAM and customer resources.                                           |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
|                                                                                                               | - US (United States)  | `cortex-xdr`               |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.225.156.101    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.69.88.119      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.147.67.188     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.90.16.31       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.203.57.162     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.203.90.79      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United Kingdom) |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.142.3.42       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.142.44.136     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.146.60.215     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.84.93.160      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.240.144.192    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.240.255.15     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.244.73.76      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.201.22.63      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany)        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.107.83.197     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.159.53.97      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.93.118.113     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.244.5.205      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland)    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.65.233.60      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.65.222.25      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.116.223.119    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.118.92.214     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 104.199.223.229   |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.81.38.132      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.18.39.0        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.18.32.96       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.155.197.131    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.155.5.100      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.165.46.47      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.165.17.246     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia)   |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.166.58.243     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.166.54.238     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.101.125.66     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.101.218.184    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.175.255.99     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.175.230.35     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.154.229.60     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.154.173.134    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea)    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.64.189.205     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.64.45.118      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.35.70.193      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.35.80.189      |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **To Collect 3rd Party Data from Customer\'s SaaS and Cloud resources**                                       |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| ---                                                                                                           | IP address by region. | `cortex-xdr`               |
|                                                                                                               |                       |                            |
|                                                                                                               | - US (United States)  |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.66.69.154      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.202.21.123     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - AU (Australia)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.197.181.108    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.197.175.44     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CA (Canada)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.95.33.72       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.95.62.136      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SG (Singapore)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.247.148.38     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.247.173.40     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - JP (Japan)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.85.68.167      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.84.99.239      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IN (India)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.93.3.196       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.93.175.218     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - DE (Germany)        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.89.197.46      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.107.3.224      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - UK (United Kingdom) |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.105.227.146    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.105.137.22     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - EU (Europe)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.90.70.107      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.204.129.196    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - CH (Switzerland)    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.65.225.124     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.65.89.6        |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - PL (Poland)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.118.71.237     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.118.124.130    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - TW (Taiwan)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.201.142.86     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 35.189.176.163    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - QT (Qatar)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.18.44.71       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.18.30.132      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - FA (France)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.163.125.167    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.163.155.105    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IL (Israel)         |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.165.131.171    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.165.120.206    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - SA (Saudi Arabia)   |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.166.59.20      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.166.53.242     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ID (Indonesia)      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.101.158.32     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.101.79.159     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ES (Spain)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.175.27.251     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.175.198.50     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - IT (Italy)          |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.154.208.247    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.154.243.11     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - KR (South Korea)    |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.64.107.163     |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.64.84.25       |                            |
|                                                                                                               |                       |                            |
|                                                                                                               | - ZA (South Africa):  |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.35.69.156      |                            |
|                                                                                                               |                       |                            |
|                                                                                                               |   - 34.35.60.86       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| **Log Forwarding to a Syslog Receiver**                                                                       |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| See [Integrate a syslog receiver](#UUID218d87cf0fa5bccd27b3bb119b0567ea).                                     |                       |                            |
+---------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

The following table lists the required resources for the federal
government of the United States, including FQDNs, IP addresses, ports,
and App-ID coverage for your deployment:

+-------------------------------------------------------------------------+-----------------------+----------------------------+
| FQDN                                                                    | IP Addresses and Port | App-ID Coverage            |
+=========================================================================+=======================+============================+
| `distributions-prod-fed.traps.paloaltonetworks.com`                     | - IP address:         | `traps-management-service` |
|                                                                         |   104.198.132.24      |                            |
| Used for the first request in registration flow where the agent passes  |                       |                            |
| the distribution ID and obtains the                                     | - Port: 443           |                            |
| `ch-<tenant-name>.traps.paloaltonetworks.com` of its tenant             |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `wss://lrc-fed.paloaltonetworks.com`                                    | - IP address:         | `cortex-xdr`               |
|                                                                         |   35.188.188.91       |                            |
| Used in live terminal flow.                                             |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-installers-prod-fr.storage.googleapis.com`                    | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                         |                       |                            |
| Used to download installers for upgrade actions from the server.        | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-payloads-prod-fr.storage.googleapis.com`                      | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                         |                       |                            |
| Used to download the executable for live terminal for Cortex XDR agents | - Port: 443           |                            |
| earlier than version 7.1.0.                                             |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `global-content-profiles-policy-prod-fr.storage.googleapis.com`         | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                         |                       |                            |
| Used to download content updates.                                       | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `panw-xdr-evr-prod-fr.storage.googleapis.com`                           | - IP ranges in GCP    | `cortex-xdr`               |
|                                                                         |                       |                            |
| Used to download extended verdict request results in scanning.          | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `app-proxy.federal.paloaltonetworks.com`                                | - IP address:         | ---                        |
|                                                                         |   35.186.217.42       |                            |
|                                                                         |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `dc-<tenant-name>.traps.paloaltonetworks.com`                           | - IP address:         | `traps-management-service` |
|                                                                         |   130.211.195.231     |                            |
| Used for EDR data upload.                                               |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `ch-<tenant-name>.traps.paloaltonetworks.com`                           | - IP address:         | `traps-management-service` |
|                                                                         |   130.211.195.231     |                            |
| Used for all other requests between the agent and its tenant server     |                       |                            |
| including heartbeat, uploads, action results, and scan reports.         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `api-<tenant-name>.xdr.federal.paloaltonetworks.com`                    | - IP address:         | ---                        |
|                                                                         |   130.211.195.231     |                            |
| Used for API requests and responses.                                    |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `cc-<tenant-name>.traps.paloaltonetworks.com`                           | - IP address:         | `traps-management-service` |
|                                                                         |   35.222.50.74        |                            |
| Used for get-verdict requests.                                          |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| **Broker VM Resources**                                                 |                       |                            |
|                                                                         |                       |                            |
| Required for deployments that use Broker VM features                    |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `br-<tenant-name>.xdr.federal.paloaltonetworks.com:443`                 | - IP address:         | ---                        |
|                                                                         |   34.71.185.11        |                            |
|                                                                         |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `xsiam-gateway (Broker VM 3.0 only)`                                    | - Port: 443           | ---                        |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| `distributions-prod-fed.traps.paloaltonetworks.com`                     | - IP address:         | `traps-management-service` |
|                                                                         |   104.198.132.24      |                            |
|                                                                         |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
|                                                                         | UDP port: 123         | ---                        |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| **App Login and Authentication**                                        |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| identity.paloaltonetworks.com                                           | - IP address:         | ---                        |
|                                                                         |   34.107.215.35       |                            |
| (SSO)                                                                   |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| login.paloaltonetworks.com                                              | - IP address:         | ---                        |
|                                                                         |   34.107.190.184      |                            |
| (SSO)                                                                   |                       |                            |
|                                                                         | - Port: 443           |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| **To Collect 3rd Party Data from Customer\'s SaaS and Cloud resources** |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| ---                                                                     | IP addresses          | `cortex-xdr`               |
|                                                                         |                       |                            |
|                                                                         | - 34.68.217.16        |                            |
|                                                                         |                       |                            |
|                                                                         | - 34.69.175.202       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| **Log Forwarding to a Syslog Receiver**                                 |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+
| See [Integrate a syslog                                                 |                       |                            |
| receiver](#UUID218d87cf0fa5bccd27b3bb119b0567ea).                       |                       |                            |
+-------------------------------------------------------------------------+-----------------------+----------------------------+

### Set up users and roles

Cortex XSIAM uses both Role-Based Access Control (RBAC) and Scope-Based
Access Control (SBAC) to manage roles with specific permissions for
controlling user access.

RBAC helps manage access to Cortex XSIAM components and Cortex Query
Language (XQL) datasets, so that users, based on their roles, are
granted minimal access required to accomplish their tasks.

SBAC refines the RBAC permissions by granting access only to the
relevant data that the user requires for their designated role. You
canUsers with **Access Management** permission can apply scopes to limit
the data and content that users can be granted access to in Cortex
XSIAM, which are divided into different scoping areas. The scoping areas
include Assets, Cases and Issues, and Endpoints, which can be applied as
relevant to the enforcement area or entity. For more information on user
scopes, see [Manage user scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

Cortex Gateway and the tenant have different options and requirements.

+-----------------------------------+-----------------------------------------------------------------------------------------------+
| Location                          | Details                                                                                       |
+===================================+===============================================================================================+
| Cortex Gateway                    | A centralized portal for managing roles, user groups, and users for all tenants. Any roles    |
|                                   | and user groups created in Cortex Gateway are available for all tenants.                      |
|                                   |                                                                                               |
|                                   | In **Cortex Gateway**, on the **Permissions** page, you can manage users that have been added |
|                                   | to your Customer Support Portal account or view users that have been created in the tenant    |
|                                   | using SSO (you cannot edit SSO users in Cortex Gateway). All users must have at least one     |
|                                   | role or belong to at least one user group to be saved in the Cortex Gateway. You can exclude  |
|                                   | different tenants or different Cortex products. For more information, see [Cortex Gateway     |
|                                   | Administrator                                                                                 |
|                                   | Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex/Cortex-Gateway-Administrator-Guide). |
|                                   |                                                                                               |
|                                   | Only users with the Account Admin role can manage roles, tenants, and user groups in Cortex   |
|                                   | Gateway.                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------+
| Cortex XSIAM tenant               | (Recommended) All permissions and roles are specific to the tenant and exist only at the      |
|                                   | tenant level. Advanced settings, such as SBAC and Dataset access management, can be defined   |
|                                   | at the tenant level.                                                                          |
|                                   |                                                                                               |
|                                   | Managing users, roles, scopes, user groups, and authentication settings in Cortex XSIAM       |
|                                   | requires **View/Edit** RBAC permissions for **Access Management** (under **Configurations**). |
|                                   | Account Admin and Instance Administrator roles are granted this permission by default.        |
|                                   |                                                                                               |
|                                   | For more information, see [Manage user roles](#UUID751d26ed9390ddddd4f6bb1f20db3a1d).         |
+-----------------------------------+-----------------------------------------------------------------------------------------------+

Predefined user roles

Role-based access control (RBAC) enables you to use predefined Palo Alto
Networks roles to assign access rights to Cortex XSIAM users. You can
manage roles for all Cortex XSIAM tenants and services in the Gateway or
in the Cortex XSIAM tenant. By assigning roles, you enforce the
separation of access among functional or regional areas of your
organization.

Each role extends specific privileges to users. The way you configure
administrative access depends on the security requirements of your
organization. Use roles to assign specific access privileges to
administrative user accounts.

You can manage role permissions in Cortex XSIAM , which are listed by
the various components according to the sidebar navigation in Cortex
XSIAM. Some components include additional action permissions, such as
pivot (right-click) options, to which you can also assign access, but
only when you've given the user **View/Edit** permissions to the
applicable component.

The default Palo Alto Networks roles provide a specific set of access
rights to each role. You cannot edit the default roles directly, but you
can save them as new roles and edit the permissions of the new roles. To
view the predefined permissions for each default role, go to Settings \>
Configurations \> Access Management \> Roles.

> **Note**
>
> Some features are license-dependent. Accordingly, users may not see a
> specific feature if the feature is not supported by the license type
> or if they do not have access based on their assigned role or scope.

+-----------------------------------+-----------------------------------+
| Default Role                      | Description                       |
+===================================+===================================+
| Account Admin                     | A Super User role that is         |
|                                   | assigned directly to the user in  |
|                                   | Cortex Gateway and has full       |
|                                   | access to all Cortex products in  |
|                                   | your account, including all       |
|                                   | tenants added in the future. The  |
|                                   | Account Admin can assign roles    |
|                                   | with scopes for Cortex instances  |
|                                   | and activate Cortex tenants       |
|                                   | specific to the product.          |
|                                   |                                   |
|                                   | > **Note**                        |
|                                   | >                                 |
|                                   | > The user who activated the      |
|                                   | > Cortex product is assigned the  |
|                                   | > Account Admin role. You cannot  |
|                                   | > create additional Account Admin |
|                                   | > roles in the Cortex XSIAM       |
|                                   | > tenant. If you do not want the  |
|                                   | > user to have Account Admin      |
|                                   | > permission, you must remove the |
|                                   | > Account Admin role in Cortex    |
|                                   | > Gateway.                        |
+-----------------------------------+-----------------------------------+
| Instance Administrator            | View and edit permissions for all |
|                                   | components and access all pages   |
|                                   | in the Cortex XSIAM tenant. The   |
|                                   | Instance Administrator can also   |
|                                   | make other users an Instance      |
|                                   | Administrator for the tenant. If  |
|                                   | the tenant has predefined or      |
|                                   | custom roles, the Instance        |
|                                   | Administrator can assign those    |
|                                   | roles with scopes to other users. |
+-----------------------------------+-----------------------------------+
| Deployment Admin                  | Manage and control endpoints and  |
|                                   | installations, and configure      |
|                                   | Broker VMs.                       |
+-----------------------------------+-----------------------------------+
| Investigator                      | View and triage issues and cases. |
+-----------------------------------+-----------------------------------+
| Investigation Admin               | View and triage issues and cases, |
|                                   | configure rules, view endpoint    |
|                                   | profiles and policies, and        |
|                                   | analytics management screens.     |
+-----------------------------------+-----------------------------------+
| Responder                         | View and triage issues, and       |
|                                   | access all response capabilities  |
|                                   | excluding Live Terminal.          |
+-----------------------------------+-----------------------------------+
| Privileged Investigator           | View and triage issues, cases,    |
|                                   | and rules, view endpoint profiles |
|                                   | and policies, and analytics       |
|                                   | management screens.               |
+-----------------------------------+-----------------------------------+
| Privileged Responder              | View and triage issues and cases, |
|                                   | access all response capabilities, |
|                                   | and configure rules, policies,    |
|                                   | and profiles.                     |
+-----------------------------------+-----------------------------------+
| IT Admin                          | Manage and control endpoints and  |
|                                   | installations, configure Broker   |
|                                   | VMs, view endpoint profiles and   |
|                                   | policies, and view issues.        |
+-----------------------------------+-----------------------------------+
| Privileged IT Admin               | Manage and control endpoints and  |
|                                   | installations, configure Broker   |
|                                   | VMs, create profiles and          |
|                                   | policies, view issues, and        |
|                                   | initiate Live Terminal.           |
+-----------------------------------+-----------------------------------+
| Privileged Security Admin         | Triage and investigate issues and |
|                                   | cases, and respond to and edit    |
|                                   | profiles and policies.            |
+-----------------------------------+-----------------------------------+
| Viewer                            | View the majority of the features |
|                                   | for this instance, and can edit   |
|                                   | reports.                          |
+-----------------------------------+-----------------------------------+
| Compliance Administrator          |                                   |
+-----------------------------------+-----------------------------------+
| Developer                         | Have limited permissions          |
|                                   | primarily focused on viewing and  |
|                                   | monitoring security information.  |
|                                   | Access and analyze scan results,  |
|                                   | track progress, and collaborate   |
|                                   | with security teams. Does not     |
|                                   | include ability to modify         |
|                                   | detection rules, enforcements, or |
|                                   | directly address security issues. |
+-----------------------------------+-----------------------------------+
| CLI Read Only Role                | View scripts, playbooks,          |
|                                   | credentials, and CLI tool.        |
+-----------------------------------+-----------------------------------+
| CLI Role                          | View scripts, playbooks, and      |
|                                   | credentials. View and edit        |
|                                   | permission for CLI tool.          |
+-----------------------------------+-----------------------------------+
| Scoped Agent Admin                | Can only access product areas     |
|                                   | that support endpoint             |
|                                   | Scoped-Based Access Control       |
|                                   | (SBAC) - Agent Administration,    |
|                                   | Action Center, Response,          |
|                                   | Dashboards and Reports.           |
+-----------------------------------+-----------------------------------+
| AppSec Admin                      | Full permissions for all Cloud    |
|                                   | Application Security related      |
|                                   | activities. Create and modify     |
|                                   | detection rules within the        |
|                                   | Code/Build domain, track          |
|                                   | progress, and adjust enforcements |
|                                   | as needed. Additionally, triage   |
|                                   | and investigate findings, issues, |
|                                   | and cases spanning from code to   |
|                                   | cloud. The role also includes     |
|                                   | complete visibility into all      |
|                                   | cloud assets.                     |
+-----------------------------------+-----------------------------------+
| Security Admin                    | Can triage and investigate issues |
|                                   | and cases, respond (excluding     |
|                                   | Live Terminal), and edit profiles |
|                                   | and policies.                     |
+-----------------------------------+-----------------------------------+
| App Service Account               | View and triage issues, cases,    |
|                                   | and rules, and support public     |
|                                   | APIs relevant for apps.           |
+-----------------------------------+-----------------------------------+
| AI Security Administrator         | Manage all aspects of AI Security |
|                                   | in the organization.              |
+-----------------------------------+-----------------------------------+
| AI Security Viewer                | Views and investigates all issues |
|                                   | and findings on AI Security.      |
+-----------------------------------+-----------------------------------+
| Data Security Administrator       | View and manage all data security |
|                                   | information, including objects    |
|                                   | and data patterns.                |
+-----------------------------------+-----------------------------------+
| Data Security Viewer              | View all data security            |
|                                   | information, including objects    |
|                                   | and data patterns.                |
+-----------------------------------+-----------------------------------+
| Identity Security Administrator   | The Identity Security             |
|                                   | Administrator has full access to  |
|                                   | all general Admin and Identity    |
|                                   | Security capabilities.            |
+-----------------------------------+-----------------------------------+
| Identity Security Viewer          | The Identity Security Viewer can  |
|                                   | view the majority of the features |
|                                   | for this Identity Security and    |
|                                   | can edit reports.                 |
+-----------------------------------+-----------------------------------+

#### User group management

Users are assigned roles and permissions either by being assigned a role
directly or by being assigned membership in one or more user groups.  A
user group can only be assigned to a single role, but users can be added
to multiple groups if they require multiple roles. You can also nest
groups to achieve the same effect.  Users who have multiple roles
through either method will receive the highest level of access based on
the combination of their roles. The same principle for users with
multiple roles is followed for both the Role-Based Access Control (RBAC)
access permissions and the Scope-Based Access Control (SBAC) granular
scoping, so that users receive the highest level of access by combining
their roles.

- Joe has an Analyst role and is a member of the Tier-1 Analyst user
  group, which is assigned the Triage role.  Joe has the permissions of
  the Analyst role and the Triage role. Joe is assigned 2 roles, and has
  the highest permission based on the combination of both roles.

- John is a member of two user groups - Tier-1 Analyst and Tier-2
  Analyst. One group is configured to use the Triage role and the other
  group is configured to use the Incident Response role.  John is
  assigned both roles and has the highest permissions based on the
  combination of all roles.

- Jack is a member of the Tier-2 user group, which has an Incident
  response role.  This user group is included in a Tier-3 user group
  (Threat Hunter role), added as a nested group.  Jack is assigned both
  roles and has the highest permissions based on the combination of all
  roles.

On the **User Groups** page, you can create a new user group for several
different system users or groups. You can see information including the
details of all user groups, the roles, nested groups, IdP groups (SAML),
and when the group was created/updated.

You can also right-click in the table to edit, save as a new group,
remove (delete) a group, and copy text to the clipboard.

> **Note**
>
> You can create user groups in the tenant or Cortex Gateway. User
> groups created in Cortex Gateway cannot be mapped to SAML groups. Only
> user groups created in the tenant support SAML group mapping and
> scoring. We recommend creating user groups in the Cortex tenant
> because:

- > User groups are available for all tenants, and you may want
  > different user groups in different tenants, such as dev/prod.

- > You can apply granular scoping for a user role by granting access
  > only to the relevant data that the user requires for their
  > designated role in the tenant. You also need to enable scope-based
  > access control in the **Server Settings** page. For more
  > information, see [Manage user
  > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

<!-- -->

- > Before configuring SBAC, ensure that you review
  > **Understand scoping** in the [Manage user
  > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8) section.

**How to create a user group**

1.  Go to Settings \> Configurations \> Access Management \> User
    Groups.

- If creating in Cortex Gateway, go to Permission Management \> User
  Groups.

2.  To create a new user group for several different system users or
    groups, click **New Group**, and add the following parameters:

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                         | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| Name                              | Name of the user group.                                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description                       | Description of the user group.                                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Group for product                 | (Cortex Gateway only) If you have multiple products, select the relevant Cortex product.                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Role                              | Select the group role associated with this user group. You can only have a single role designated per group.                                         |
|                                   |                                                                                                                                                      |
|                                   | In Cortex Gateway, you can only select either Instance Administrator or a custom role created in the Gateway.                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Users                             | Select the users you want to belong to this user group.                                                                                              |
|                                   |                                                                                                                                                      |
|                                   | > **Note**                                                                                                                                           |
|                                   | >                                                                                                                                                    |
|                                   | > If users have been created in the CSP, but you want them to access the tenant through SSO only, skip this field and add only SAML group mapping    |
|                                   | > after SSO is set up, otherwise, users can access the tenant through both the CSP and SSO.                                                          |
|                                   | >                                                                                                                                                    |
|                                   | > If you have not yet created any users, skip this field and add them later. See [Set up                                                             |
|                                   | > authentication](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Cloud-Documentation/Set-up-authentication) .                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nested Groups                     | Lists any nested groups associated with this user group. If you have an existing group, you can add a nested group.                                  |
|                                   |                                                                                                                                                      |
|                                   | User groups can include multiple users and nested groups, which inherit the permissions of parent user groups. The user group will have the highest  |
|                                   | level of permission.                                                                                                                                 |
|                                   |                                                                                                                                                      |
|                                   | For example:                                                                                                                                         |
|                                   |                                                                                                                                                      |
|                                   | - Group A has Tier-1 Analyst permissions                                                                                                             |
|                                   |                                                                                                                                                      |
|                                   | - Group B has Tier-2 Analyst permissions                                                                                                             |
|                                   |                                                                                                                                                      |
|                                   | If you add Group A as a nested group in Group B, Group A inherits Group B\'s permissions (Tier-1 and Tier-2 permissions).                            |
|                                   |                                                                                                                                                      |
|                                   | In Cortex Gateway, you can only add user groups that are created in Cortex Gateway.                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| SAML Group Mapping                | (Relevant when creating a user group in the Cortex tenant only.)                                                                                     |
|                                   |                                                                                                                                                      |
|                                   | Maps the SAML group membership to this user group. For example, you have defined a `Cortex Admins` group. You need to name this group exactly how it |
|                                   | appears in Okta.                                                                                                                                     |
|                                   |                                                                                                                                                      |
|                                   | You can add multiple groups by separating them with a comma.                                                                                         |
|                                   |                                                                                                                                                      |
|                                   | > **Note**                                                                                                                                           |
|                                   | >                                                                                                                                                    |
|                                   | > When using Azure AD for SSO, the SAML group mapping needs to be provided using the group object ID (GUID) and not the group name.                  |
|                                   |                                                                                                                                                      |
|                                   | If you have not set up SSO in your tenant, skip this field and add it later. After you have added it, follow the procedure relevant to your IdP. For |
|                                   | example, see [Set up Okta as the identity using SAML                                                                                                 |
|                                   | 2.0](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Cloud-Documentation/Set-up-Okta-as-the-Identity-Provider-Using-SAML-2.0) |
|                                   | .                                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

3.  (Optional) When creating the user group in the tenant, configure
    granular scoping for the user group.

- If creating the user group in the Cortex Gateway, you can skip this
  step, as scoping is only supported in the tenant.

  a.  Click the **Scope** tab.

  b.  Expand the scoping areas that you want to grant the user role
      access to in the tenant by clicking the chevron icon (**\>**)
      beside the scoping area title, and make any changes required. The
      following table explains the options available to configure:

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

  > By default, **Enable Scope Based Access Control** is disabled
  > in Settings \> Configurations \> General \> Server Settings, and
  > granular scoping is not enforced. Before enabling SBAC, we recommend
  > that an administrator or a user
  > with **Access Management** permissions first ensures that the users,
  > user groups, and API Keys defined in Cortex XSIAM are granted the
  > required access by assigning the relevant scopes. For more
  > information, see [Manage user
  > scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

4.  Click **Create** to create the user group.

#### Assign user roles and groups

Assign roles directly to users or create user groups and assign roles to
those groups. We recommend creating user groups (with a user role), and
assigning users to those user groups rather than creating direct roles
for each user.

> **Note**
>
> If an existing user in the Cortex Gateway no longer has a role or a
> user group assigned, the user is revoked. Any roles, user groups, or
> egress configurations created by that user are shown as created by
> **Revoked user** instead of the user's email address.

Assign a user/user group to a role

Cortex XSIAM provides predefined built-in user roles that provide
specific access rights that cannot be modified. You can also create
custom, editable user roles. If a user does not have any Cortex XSIAM
access permissions that are assigned specifically to them, the field
displays **No-Role**.

1.  Select Settings \> Configurations \> Access Management \> Users.

2.  Right-click the relevant user, and select **Edit User Permissions**.

- > **Tip**

  > To apply the same settings to multiple users, select them, and then
  > right-click and select **Edit Users Permissions**.

3.  Ensure the **Role** tab is selected.

4.  Under **Role**, select the default or custom role.

5.  (Optional) Under **User Groups**, add the user to a group.

6.  (Optional) Under **Show Accumulated Permissions**:

    a.  Do one of the following:

        - Select all to view the combined permissions for every role and
          user group assigned to the user.

        - Select a specific role assigned to the user to view the
          available permissions for that role.

    b.  Under **Components**, expand each list to view the permissions.

- > **Important**

  > Setting Cortex Query Language (XQL) dataset access permissions for a
  > user role can only be performed from **Cortex
  > XSIAM Access Management**. For more information, see [Manage user
  > roles](#UUID751d26ed9390ddddd4f6bb1f20db3a1d).

7.  (Optional) You can configure and manage granular scoping:

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

8.  Click Save.

**Perform additional tasks**

For more information about additional tasks such as creating a custom
role, modifying a user\'s role, or removing a user\'s role, see [Manage
user access](#UUIDa112c99e112fab8ae5ede31445dee8fe) or [Cortex Gateway
Administrator
Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex/Cortex-Gateway-Administrator-Guide).

### Set up authentication

You can create users in the Customer Support Portal or by using SAML
Single Sign-On (SSO) in the tenant. Users authenticate by doing the
following:

- Authenticate through the Customer Support Portal

<!-- -->

- When users log into Cortex Gateway or the tenant (provided they are
  assigned a role) they are prompted to sign into the Customer Support
  Portal using their username and password or 2FA (if set up). This is
  the default method of authentication.

  After you have created users, add them to user groups or assign roles
  directly.

<!-- -->

- Authenticate using SAML single sign-on in the Cortex XSIAM tenant

<!-- -->

- Users can be authenticated using your IdP provider such as Okta, Ping,
  or Azure AD. You can use any IdP that supports SAML 2.0. After you
  configure the SSO integration you need to map group SAML group
  membership to user groups in Cortex XSIAM.

SSO authentication has the following advantages:

- Removes the administrative burden of requiring separate accounts to be
  configured through the Customer Support Portal.

- Enforces multi-factor authentication (MFA) and any conditional access
  policies on the user login at the IdP before granting a user access to
  Cortex XSIAM.

- Maps SAML group memberships to user groups and roles, allowing you to
  manage role-based access control.

- Removes access to Cortex XSIAM when a user is removed or disabled in
  the IdP.

Customer Support Portal authentication, by contrast, is useful if you
have users who need the same permissions across multiple tenants. If you
use SSO for multiple tenants, you must set up the SSO configuration
separately for each tenant, both in the IdP and in Cortex XSIAM.

If you want to restrict the user login through SSO only, remove any
direct role and user group mapping for the user on Cortex Gateway or the
Cortex XSIAM tenant. This removes Customer Support Portal access for the
user. You then need to ensure that you add the SAML group mapping. The
user can access and acquire the user group and roles based on SAML group
mapping. Once completed, the user is able to access Cortex XSIAM using
SSO only and will not be able to use Customer Support Portal login
method.

For more information, see [Assign user roles and
groups](#UUIDc0966cb32b3c88e214d33131de93fa8a).

> **Tip**
>
> You should have at least one user in the Customer Support Portal for
> backup, in case of any authentication issues with your IdP provider.

#### Authenticate users through the Customer Support Portal

When you add users to your Customer Support Portal account, users are
sent an invitation to join. After they accept, users can access Cortex
Gateway and tenants, but they cannot view any tenants in the Gateway and
cannot view any data in the tenant unless they are assigned a direct
role or user group role. Only Account Admins can make any changes in
Cortex Gateway.

> **Note**
>
> You must be assigned the Super User role in the Customer Support
> Portal to add users in the Customer Support Portal.
>
> The first Super User who logs into Cortex Gateway is automatically
> assigned the Account Admin role and has access to the tenant. The user
> who activates the Cortex XSIAM tenant will also be assigned the
> Account Admin role (if there is no current Account Admin role) or
> Instance Admin (if there is an existing Account Admin role) and will
> have access to the tenant. Any additional users including Super Users
> need to be assigned access to the tenant.

When users log into Cortex Gateway or the tenant they are prompted to
sign into the Customer Support Portal using their username and password.
This is the default method of authentication.

> **Note**
>
> After users are added to the Customer Support Portal and they accept
> the invitation, you can manage them in Cortex Gateway or the Cortex
> XSIAM tenant.

**How to authenticate users through the Customer Support Portal**

1.  Add users to your Customer Support Portal account, by logging into
    <https://support.paloaltonetworks.com/> and doing one of the
    following:

    - In your Customer Support User Account, create users.

      1.  On the left-hand side menu, select Members \> Create New User
          .

      2.  Add the member details and click Submit.

      - An email is sent to the user which must be accepted within seven
        days.

        For more detailed information including how to reset the
        invitation, see [How a Super User Creates a New Customer Support
        Portal User
        Account](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNPCA0).

    - Send an Account Registration Link.

    <!-- -->

    - A registration link is generated by a Customer Support Portal
      account Super User and shared with users who need to create a
      login for access to the account.

      1.  On the left-hand side menu, select Account Management \>
          Account Details, and click **User Access**.

      2.  In the **Account Registration** link, click **Create**.

      3.  Copy and send the link to the users you want to add.

      - When clicking the link, users are required to enter their
        registration details and submit them to the Customer Support
        Portal.

        After users have submitted their details, the Super User
        receives a notification that a user has been created.

      For more information about how to generate, regenerate, or disable
      a link, see [How to Use the Account Registration
      Link](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNXCA0).

2.  Log in to [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/accounts) .

- After the user accepts the invitation, you see the added users. You
  must assign a role to the user directly or add them to user groups in
  Cortex Gateway or in the Cortex XSIAM tenant.

#### Authenticate users using SSO

Cortex XSIAM enables you to authenticate system users securely across
enterprise-wide applications and websites with one set of credentials
using single sign-on (SSO) with SAML 2.0. System users can authenticate
using your organization\'s Identity Provider (IdP), such as Okta or
PingOne. You can integrate with any IdP that is supported by SAML 2.0.

Configuring SSO with SAML 2.0 is dependent on your organization's IdP.
Some of the parameter values need to be supplied from your
organization's IdP and some need to be added to your organization's IdP.
You must have sufficient knowledge about IdPs, how to access your
organization's IdP, which values to add to Cortex XSIAM, and which
values to add to your IdP fields.

> **Note**

- > To set up SSO authentication in the tenant, you must be assigned an
  > Instance Administrator or Account Admin role.

- > SAML 2.0 users must log in to Cortex XSIAM using the FQDN (full URL)
  > of the tenant. To allow login directly from the IdP to , you must
  > set the relay state on the IdP to the FQDN of the tenant.

- > If you have multiple tenants, you must set up the SSO configuration
  > separately for each tenant, both in the IdP and in Cortex XSIAM.

- > Create groups in Cortex XSIAM that correspond to the groups in your
  > IDP, and assign users to those groups in your IdP.  Add the
  > appropriate SAML group mapping from your IdP to each of the user
  > groups in Cortex XSIAM.

- > When you log in for the first time, your user account is
  > automatically created, provided you have a mapped role or group.
  > This process requires either using the default role option or
  > ensuring that your SSO groups are properly mapped to Cortex XSIAM
  > groups. If you belong to a group that has a mapping, you will be
  > granted access automatically upon login.

- > If you are using AWS SSO, the `Application ACS URL` refers to
  > the `Single Sign-On URL` and the `Application SAML Audience` refers
  > to the `Audience URL (SP Entity ID)`. Both values can be copied from
  > the **Authentication Settings** in Cortex XSIAM.

If you are configuring Okta or Azure, follow the procedure in
[Okta](#UUIDbbdf85345cae5bf8c8170d94c7152bf5) or [Azure
AD](#UUID1192642ac44e58e54af1b3654ab2e41a). You can also adapt these
instructions for use with any similar SAML 2.0 IdP.

1.  In Cortex XSIAM, go to Settings \> Configurations \> Access
    Management \> Authentication Settings.

2.  In the **Login Options** tab, toggle **SSO Disabled** to on.

- You can see the SSO settings, so you can configure them according to
  your organization's IdP.

3.  If you want to add another SSO connection to enable managing user
    groups with different roles and different IdPs, click
    **Add SSO Connection**.

- Different SSO parameters for an SSO are displayed to configure
  according to your organization's additional IdP.

  > **Note**

  - > The first SSO cannot be deleted, it can only be deactivated by
    > toggling **SSO Enabled** to off.

  - > The **Domain** parameter is predefined for the first SSO.

  <!-- -->

  - > If you add additional SSO providers, you must provide the
    > email Domain in the SSO Integration settings for all providers
    > except the first. Cortex XSIAM uses this domain to determine to
    > which identity provider to send the user for authentication.

  <!-- -->

  - > When mapping IdP user groups to Cortex XSIAM user groups, you must
    > include the group attribute for each IdP you want to use. For
    > example, if you are using Microsoft Azure and Okta, your Cortex
    > XSIAM user group SAML Group Mapping field must include the IdP
    > groups for each provider. Each group name is separated by a comma.

4.  Set the following parameters using your organization's IdP.

    - **General parameters**

    - **IdP Attribute Mapping**

    - **Advanced Settings** (optional)

5.  **Save** your changes.

- Whenever an SSO user logs in to Cortex XSIAM, the following login
  options are available.

  - **Sign-in with SSO**

  <!-- -->

  - If you have enabled more than one SSO provider, an optional email
    field appears. If the user does not enter an email address or if the
    email address does not match an existing domain, the user is
    automatically directed to the default IdP provider (the first in the
    list of SSO providers in the Authentication Settings). If the user
    enters an email address and it matches a domain listed in the
    **Domain** field in the SSO Integration settings for one of your
    IdPs, **Sign-In with SSO** sends the user to the IdP associated with
    that email domain.

##### General parameters

+-----------------------------------+----------------------------------------------------------------+
| Parameter                         | Description                                                    |
+===================================+================================================================+
| IdP SSO or Metadata URL           | Select the option that meets your organization\'s              |
|                                   | requirements.                                                  |
|                                   |                                                                |
|                                   | Indicates your SSO URL, which is a fixed, read-only value      |
|                                   | based on your tenant\'s URL using the format                   |
|                                   | `https://<name of tenant>.crtx.paloaltonetworks.com/idp/saml`. |
|                                   | For example,                                                   |
|                                   | `https://tenant1.crtx.paloaltonetworks.com/idp/saml`           |
|                                   |                                                                |
|                                   | You need this value when configuring your IdP.                 |
+-----------------------------------+----------------------------------------------------------------+
| IdP SSO URL                       | Specify your organization's SSO URL, which is copied from your |
|                                   | organization's IdP.                                            |
+-----------------------------------+----------------------------------------------------------------+
| Metadata URL                      |                                                                |
+-----------------------------------+----------------------------------------------------------------+
| Audience URI (SP Entity ID)       | Indicates your Service Provider Entity ID, also known as the   |
|                                   | ACS URL. It is a fixed, read-only value using the format,      |
|                                   | `https://<name of tenant>.paloaltonetworks.com`. For example   |
|                                   | `https://tenant1.crtx.paloaltonetworks.com`.                   |
|                                   |                                                                |
|                                   | You need this value when configuring your organization's IdP.  |
+-----------------------------------+----------------------------------------------------------------+
| Default Role                      | (*Optional*) Select the default role that you want any user to |
|                                   | automatically receive when they are granted access to Cortex   |
|                                   | XSIAM through SSO. This is an inherited role and is not the    |
|                                   | same as a direct role assigned to the user.                    |
+-----------------------------------+----------------------------------------------------------------+
| IdP Issuer ID                     | Specify your organization's IdP Issuer ID, which is copied     |
|                                   | from your organization's IdP.                                  |
+-----------------------------------+----------------------------------------------------------------+
| X.509 Certificate                 | Specify your X.509 digital certificate, which is copied from   |
|                                   | your organization's IdP.                                       |
+-----------------------------------+----------------------------------------------------------------+
| Domain                            | Relevant only for multiple SSOs. For one SSO, this is a fixed, |
|                                   | read-only value. Associate this IdP with a specific email      |
|                                   | domain (user@\<domain\>). When logging in, users are           |
|                                   | redirected to the IdP associated with their email domain or to |
|                                   | the default IdP if no association exists.                      |
+-----------------------------------+----------------------------------------------------------------+

##### IdP attribute mapping

These IdP attribute mappings are dependent on your organization's IdP.

+-----------------------------------+-----------------------------------+
| Parameter                         | Description                       |
+===================================+===================================+
| Email                             | Specify the email mapping         |
|                                   | according to your organization's  |
|                                   | IdP.                              |
+-----------------------------------+-----------------------------------+
| Group Membership                  | Specify the group membership      |
|                                   | mapping according to your         |
|                                   | organization's IdP.               |
|                                   |                                   |
|                                   | > **Note**                        |
|                                   | >                                 |
|                                   | > Cortex XSIAM requires the IdP   |
|                                   | > to send the group membership as |
|                                   | > part of the SAML token. Some    |
|                                   | > IdPs send values in a format    |
|                                   | > that include a comma, which is  |
|                                   | > not compatible with Cortex      |
|                                   | > XSIAM. In that case, you must   |
|                                   | > configure your IdP to send a    |
|                                   | > single value without a comma    |
|                                   | > for each group membership. For  |
|                                   | > example, if your IdP sends the  |
|                                   | > Group DN (a comma-separated     |
|                                   | > list), by default, you must     |
|                                   | > configure IdP to send the Group |
|                                   | > CN (Common Name) instead.       |
+-----------------------------------+-----------------------------------+
| First Name                        | Specify the first name mapping    |
|                                   | according to your organization's  |
|                                   | IdP.                              |
+-----------------------------------+-----------------------------------+
| Last Name                         | Specify the last name mapping     |
|                                   | according to your organization's  |
|                                   | IdP.                              |
+-----------------------------------+-----------------------------------+

##### Advanced settings

The following advanced settings are optional to configure and some are
specific for a particular IdP.

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Parameter                         | Description                                                                                                               |
+===================================+===========================================================================================================================+
| Relay State                       | (*Optional*) Specify the URL for a specific page that you want users to be directed to after they've been authenticated   |
|                                   | by your organization's IdP and log in to Cortex XSIAM.                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| IdP Single logout URL             | (*Optional*) Specify your IdP single logout URL provided by your organization's IdP to ensure that when a user initiates  |
|                                   | a logout from Cortex XSIAM, the identity provider logs the user out of all applications in the current identity provider  |
|                                   | login session.                                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| SP Logout URL                     | (*Optional*) Indicates the Service Provider logout URL that you need to provide when configuring a single logout from     |
|                                   | your organization's IdP to ensure that when a user initiates a logout from Cortex XSIAM, the identity provider logs the   |
|                                   | user out of all applications in the current identity provider login session. This field is read-only and uses the         |
|                                   | following format `https://<name of tenant>.crtx.paloaltonetworks.com/idp/logout`, such as                                 |
|                                   | `https://tenant1.crtx.paloaltonetworks.com/idp/logout`.                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Service Provider Public           | (*Optional*) Specify your organization's IdP service provider public certificate.                                         |
| Certificate                       |                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Service Provider Private Key (Pem | (*Optional*) Specify your organization's IdP service provider private key in Pem Format.                                  |
| Format)                           |                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Remove SAML RequestedAuthnContext | (*Optional*) Requires users to log in to Cortex XSIAM using additional authentication methods, such as biometric          |
|                                   | authentication.                                                                                                           |
|                                   |                                                                                                                           |
|                                   | Selecting this removes the error generated when the authentication method used for previous authentication is different   |
|                                   | from the one currently being requested. See                                                                               |
|                                   | [here](https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/error-code-aadsts75011-auth-method-mismatch) |
|                                   | for more details about the `RequestedAuthnContext` authentication mismatch error.                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Force Authentication              | (*Optional*) Requires users to reauthenticate to access the Cortex XSIAM tenant if requested by the idP, even if they     |
|                                   | already authenticated to access other applications.                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

##### Troubleshoot SSO issues

The following list describes the common errors and issues when using
SAML 2.0 authentication.

- Errors in your IdP could mean the Service Provider Entity ID and/or
  Service Identifier are not properly configured in the IdP or in the
  Cortex XSIAM settings.

- SAML attributes from the IdP are not properly mapped in Cortex XSIAM.
  The attributes are case sensitive and must exactly match in your IdP
  and in the Cortex XSIAM **IdP Attributes Mapping**.

- Group memberships from the IdP have not been properly mapped to Cortex
  XSIAM user groups. Verify the values your identity provider is
  sending, to properly map the groups in Cortex XSIAM.

- The identity provider is not configured to sign both the SAML response
  and the assertion on the login token. Your IdP must be configured to
  sign both to ensure a secure login.

- If you require further troubleshooting, we recommend using your
  browser\'s built-in developer tools or additional browser plugins to
  capture the login request and SAML token.

#### Set up Okta as the Identity Provider Using SAML 2.0

This topic provides specific instructions for using Okta to authenticate
your Cortex XSIAM users. As Okta is a third-party software, specific
procedures, and screenshots may change without notice. We encourage you
to also review the [Okta documentation for app
integrations](https://help.okta.com/oie/en-us/content/topics/apps/apps_apps.htm).

To configure SAML SSO in Cortex XSIAM, you must be a user who can access
the Cortex XSIAM tenant and have either the Account Admin or Instance
Administrator role assigned.

##### Task 1. Configure Okta Groups

Within Okta, assign users to
[groups](https://help.okta.com/asa/en-us/content/topics/adv_server_access/docs/setup/create-a-group.htm)
that match the user groups they will belong to in Cortex XSIAM. Users
can be assigned to multiple Okta groups and receive permissions
associated with multiple user groups in Cortex XSIAM. Use an identifying
word or phrase, such as Cortex XSIAM, within the group names. For
example, Cortex XSIAM Analysts. This allows you to send only relevant
group information to Cortex XSIAM, based on a filter you will set in the
group attribute statement.

Create a list of the Okta groups and their corresponding Cortex XSIAM
user groups (or the Cortex XSIAM user groups you intend to create) and
save this list for later use when configuring user groups in Cortex
XSIAM.

##### Task 2. Copy Single SSO and Audience URI Values from Cortex XSIAM

1.  In Cortex XSIAM, go to Settings \> Configurations \> Access
    Management \> Authentication Settings.

2.  In the **Login Options** tab, toggle **SSO Disabled** to on.

3.  Expand the **SSO Integration** settings.

4.  Copy and save the values for **Single Sign-On URL** and
    **Audience URI (SP Entity ID)**.

- Both values are needed to configure your IdP settings.

  You cannot save the enabled SSO Integration at this time, as it
  requires values from your IdP.

##### Task 3. Configure Cortex XSIAM Application in Okta

1.  In Okta, create a Cortex XSIAM application and **Edit** the
    **SAML Settings**.

2.  Paste the **Single sign-on URL** and the
    **Audience URI (SP Entity ID)** that you copied from the Cortex
    XSIAM SSO settings. The Audience URI should also be pasted in the
    **Default RelayState** field, which allows users to log in to Cortex
    XSIAM directly from the Okta dashboard.

3.  Click **Show Advanced Settings**, verify that Okta is configured to
    sign both the response and the assertion signature for the SAML
    token, and then click **Hide Advanced Settings**.

4.  Cortex XSIAM requires the IdP to send four attributes in the SAML
    token for the authenticating user.

    - Email address

    - Group membership

    - First Name

    - Last Name

- Configure Okta to send group memberships of the users using the
  `memberOf` attribute. Use the word or phrase you selected when
  configuring Okta groups (such as Cortex XSIAM) to create a filter for
  the relevant groups.

5.  Copy the exact names of the attribute statements from Okta and save
    them, as they are required to configure the Cortex XSIAM SSO
    integration. In the example above, the names are FirstName,
    LastName, Email, and memberOf. The attribute names are
    case-sensitive.

##### Task 4. Copy IdP SSO URL, Identity Provider Issuer, and X.509 Certificate Values

1.  In Okta, from your Cortex XSIAM application page, click
    **View SAML setup instructions**. If you do not see this button,
    verify you are on the **Sign On** tab of the application.

2.  Copy and save the values for
    **Identity Provider Single Sign-On URL**,
    **Identity Provider Insurer**, and the **X.509 Certificate**. These
    values are needed to configure your Cortex XSIAM SSO Integration.

##### Task 5. Configure the Cortex XSIAM SSO Integration

1.  In Cortex XSIAM go to Settings \> Configurations \> Access
    Management \> Authentication Settings.

2.  In the **Login Options** tab, toggle **SSO Disabled** to on.

3.  Expand the **SSO Integration** settings.

4.  Use the following table to complete the SSO Integration settings,
    based on the values you saved from Okta.

  -----------------------------------------------------------------------
  Okta                                Cortex XSIAM Field
  ----------------------------------- -----------------------------------
  Identity Provider Single Sign-On    IdP SSO URL
  URL                                 

  Identity Provider Issuer            IdP Issuer ID

  X.509 Certificate                   X.509 Certificate
  -----------------------------------------------------------------------

5.  In the **IdP Attributes Mapping** section, enter the attribute names
    from Okta. The names are case-sensitive and must match exactly.

6.  **Save** your settings.

##### Task 6. Map SAML Group Memberships to Cortex XSIAM User Groups

1.  Select Settings \> Configurations \> Access Management \> User
    Groups.

2.  Right-click a user group and select **Edit Group**.

3.  In the **SAML Group Mapping** field add the Okta group(s) that
    should be associated with this user group. Multiple groups should be
    separated with a comma. The Okta group name must match the exact
    value sent in the token.

4.  **Save** your settings.

5.  Repeat for each user group.

##### Task 7. Test SSO Login

1.  Go to the Cortex XSIAM tenant URL and **Sign-In with SSO**.

- > **Note**

  > When using SAML 2.0, users are required to authenticate by logging
  > in directly at the tenant URL. They cannot log in via Cortex
  > Gateway.

2.  After authentication to Okta, you are redirected again to the Cortex
    XSIAM tenant.

3.  When logged in, validate that you have been assigned the proper
    roles.

- To view your role and any role assigned to a user group you are a
  member of, click your name in the bottom left-hand corner, and click
  **About**.

#### Set up Azure AD as the Identity Provider Using SAML 2.0

This topic provides specific instructions for using Azure AD to
authenticate your Cortex XSIAM users. As Azure AD is a third-party
software, specific procedures, and screenshots may change without
notice. We encourage you to also review the [Azure AD
documentation](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-setup-sso).

To configure SAML SSO in Cortex XSIAM, you must be a user who can access
the Cortex XSIAM tenant and have either the Account Admin or Instance
Administrator role assigned.

##### Task 1. Configure Azure AD Security Groups

Within Azure AD, assign users to [security
groups](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-manage-groups)
that match the user groups they will belong to in Cortex XSIAM. Users
can be assigned to multiple Azure AD groups and receive permissions
associated with multiple user groups in Cortex XSIAM. Use an identifying
word or phrase, such as Cortex XSIAM, within the group names. For
example, Cortex XSIAM Analysts. This allows you to send only relevant
group information to Cortex XSIAM, based on a filter you will set in the
group attribute statement.

##### Task 2. Copy Single SSO and Audience URI Values from Cortex XSIAM

1.  In Cortex XSIAM go to Settings \> Configurations \> Access
    Management \> Authentication Settings.

2.  In the **Login Options** tab, toggle **SSO Disabled** to on.

- By default, SSO is disabled in Cortex XSIAM.

3.  Expand the **SSO Integration** settings.

4.  Copy and save the values for **Single Sign-On URL** and
    **Audience URI (SP Entity ID)**.

- Both values are needed to configure your IdP settings.

  > **Important**

  > When copying the **Single Sign-On URL** value, remove `idp/saml` and
  > leave the trailing `/`.

  > For example, if the **Single Sign-On URL** is
  > `https://clientname.panproduct.region.paloaltonetworks.com/idp/saml`,
  > just copy
  > `https://clientname.panproduct.region.paloaltonetworks.com/`.

5.  You cannot save the enabled SSO Integration at this time, as it
    requires values from your IdP.

##### Task 3. Configure Cortex XSIAM Application in Azure AD

1.  From within Azure AD, create a Cortex XSIAM application and **Edit**
    the **Basic SAML Configuration**.

- ![](media/rId262.png){width="5.833333333333333in"
  height="4.141666666666667in"}

2.  Paste the **Single sign-on URL** and the
    **Audience URI (SP Entity ID)** that you copied from the Cortex
    XSIAM SSO settings. The **Single sign-on URL** from Cortex XSIAM
    should be pasted in the **Reply URL** and the **Sign on URL**
    fields. The **Audience URI (SP Entity ID)** value from Cortex XSIAM
    should be pasted in the **Identifier (Entity ID)** and
    **Relay State** fields. This allows users to log in to Cortex XSIAM
    directly from Azure AD.

- ![](media/rId265.png){width="5.833333333333333in"
  height="6.028819991251094in"}

3.  In the **SAML Certificates** section, click **Edit** and verify that
    Azure is configured to sign both the response and the assertion.

- ![](media/rId268.png){width="5.833333333333333in"
  height="1.9979166666666666in"}

4.  To have Azure AD send group membership for the user in the SAML
    token, you must **+ Add a group claim** in the
    **Attributes & Claims** section. Send the **Security groups**, using
    the source attribute **Group ID**. Use the word or phrase you
    selected when configuring Azure AD security groups (such as Cortex
    XSIAM) to create a filter. Customize the name of the group claim as
    **memberOf**.

- ![](media/rId271.png){width="5.833333333333333in"
  height="9.446692913385826in"}

5.  In addition to group membership, verify that there are also claims
    for:

    - Email address

    - First Name

    - Last Name

##### Task 4. Copy Login URL, Azure ID Identifier, and Attribute Claims

1.  In Azure, from the **Single sign-on** page, in the **Set up Cortex
    XSIAM Production** section, copy the values for the **Login URL**
    and **Azure AD Identifier**. You need these values to configure the
    SSO Integration in Cortex XSIAM.

- ![](media/rId275.png){width="5.833333333333333in"
  height="1.401933508311461in"}

2.  **Edit** **Attributes & Claims** and copy the values in the
    **Claim name** column. The claim name is case sensitive. You need
    these values to configure the SSO Integration in Cortex XSIAM.

- > **Note**

  > The default attributes shown on the main single sign-on page in
  > Azure AD are not the values you need. You must click **Edit** next
  > to **Attributes and Claims** to view and copy the actual values.

  ![](media/rId278.png){width="5.833333333333333in" height="2.58125in"}

##### Task 5. Download the Certificate

From the SAML Certificates section in Azure AD, **Download** the
**Certificate (Base64)**. You need the contents of this file to
configure the Cortex XSIAM SSO Integration.

![](media/rId282.png){width="5.833333333333333in" height="2.1in"}

##### Task 6. Copy the Source IDs for Azure AD Security Groups

The claim for the [membership
attribute](#X97cc8a263ad75b5f8aafdf7780c871d59a70597) that is sent to
Cortex XSIAM uses the **Object Id** of the group. The **Object Id** is
different from the Azure AD security group name. You can find the
**Object Id** for each of your Azure AD security groups by navigating to
**Users and groups** in Azure AD, clicking on the group name, and
viewing the **Object id**. Create a list of the group names and
corresponding **Object Ids** for every Azure AD security group you want
to map to a Cortex XSIAM user group.

##### Task 7. Configure the Cortex XSIAM SSO Integration

1.  In Cortex XSIAM go to Settings \> Configurations \> Access
    Management \> Authentication Settings.

2.  In the **Login Options** tab, toggle **SSO Disabled** to on.

- By default, SSO is disabled in Cortex XSIAM.

3.  Expand the **SSO Integration** settings.

4.  Use the following table to complete the SSO Integration settings,
    based on the values you saved from Azure AD.

  -----------------------------------------------------------------------
  Azure AD                            Cortex XSIAM Field
  ----------------------------------- -----------------------------------
  Login URL                           IdP SSO URL

  Azure AD Identifier                 IdP Issuer ID

  Contents of the downloaded          X.509 Certificate
  certificate file.                   
  -----------------------------------------------------------------------

5.  In the **IdP Attributes Mapping** section, enter the attribute claim
    names from Azure AD. The names are case sensitive and must match
    exactly.

- > **Note**

  > The attribute claim name must exactly match the value sent by your
  > IdP. In some cases, this may be the full attribute name/namespace,
  > depending on the configuration of our IdP

  ![](media/rId287.png){width="5.833333333333333in"
  height="3.1128947944006997in"}

6.  (Optional) Under **Advanced Settings**, select the checkboxes for
    **ADFS** and **Compress encode URL (ADFS)**. In some circumstances,
    these fields may be required by your Azure AD configuration.

7.  Save your settings.

##### Task 8. Map SAML Group Memberships to Cortex XSIAM User Groups

1.  Select Settings \> Configurations \> Access Management \> User
    Groups.

2.  Right-click a user group and select **Edit Group**.

3.  In the **SAML Group Mapping** field add the Azure AD group(s) Object
    Ids that should be associated with this user group. Multiple Object
    Ids should be separated with a comma. The Azure AD group Object Id
    must match the exact value sent in the token.

4.  Save your settings.

5.  Repeat for each user group.

##### Task 9. Test SSO Login

1.  Go to the Cortex XSIAM tenant URL and **Sign-In with SSO**.

- > **Note**

  > When using SAML 2.0, users are required to authenticate by logging
  > in directly at the tenant URL. They cannot log in via Cortex
  > Gateway.

2.  After authentication to Azure AD, you are redirected again to the
    Cortex XSIAM tenant.

3.  When logged in, validate that you have been assigned the proper
    roles.

- To view your role and any role assigned to a user group you are a
  member of, click your name in the bottom left-hand corner, and
  click **About**.

### Pre-installation steps for Cortex XDR agents

#### Define endpoint groups

You can define an endpoint group and then apply policy rules and manage
specific endpoints. If you set up Cloud Identity Engine, you can also
leverage your Active Directory user, group, and computer details to
define endpoint groups.

Do one of the following:

- Create a dynamic group by enabling Cortex XSIAM to populate your
  endpoint group dynamically using endpoint characteristics, such as an
  endpoint tag, partial hostname or alias, full or partial domain or
  workgroup name, IP address, range or subnets, installation type (VDI,
  temporary session or standard endpoint), agent version, endpoint type
  (workstation, server, mobile), or operating system version.

- Create a static group by selecting a list of specific endpoints.

After you define an endpoint group, you can then use it to target policy
and actions to specific recipients. The **Endpoint Groups** page
displays all endpoint groups along with the number of endpoints and
policy rules linked to the endpoint group.

**How to define an endpoint group**

1.  Select Inventory \> Endpoints \> Groups \> +Add Group.

2.  Select one of the following:

    - **Create New** to create an endpoint group from scratch

    - **Upload From File** using plain text files with a new line
      separator, to populate a static endpoint group from a file
      containing IP addresses, hostnames, or aliases.

3.  Enter a **Group Name** and optional description to identify the
    endpoint group. The name you assign to the group will be visible
    when you assign endpoint security profiles to endpoints.

4.  Determine the endpoint properties for creating an endpoint group:

    - **Dynamic:** Use the filters to define the criteria you want to
      use to dynamically populate an endpoint group. Dynamic groups
      support multiple criteria selections and can use **AND** or **OR**
      operators. For endpoint names and aliases, and domains and
      workgroups, you can use `*` to match any string of characters. As
      you apply filters, Cortex XSIAM displays any registered endpoint
      matches to help you validate your filter criteria.

    - **Static:** Select specific registered endpoints that you want to
      include in the endpoint group. Use the filters, as needed, to
      reduce the number of results.

    <!-- -->

    - When you create a static endpoint group from a file, the IP
      address, hostname, or alias of the endpoint must match an existing
      agent that has registered with Cortex XSIAM. You can select up to
      250 endpoints.

- > **Note**

  > Disconnecting Cloud Identity Engine in your Cortex XSIAM deployment
  > can affect existing endpoint groups and policy rules based on Active
  > Directory properties.

5.  Create the endpoint group.

- After you save your endpoint group, it is ready for use to assign
  security profiles to endpoints and in other places where you can use
  endpoint groups.

At any time, you can return to the **Groups** page to view and manage
your endpoint groups. To manage a group, right-click the group and
select the desired action:

- **Edit:** View the endpoints that match the group definition, and
  optionally refine the membership criteria using filters.

- **Delete:** Remove the endpoint group.

- **Save as new:** Duplicate the endpoint group and save it as a new
  group.

- **Export group:** Export the list of endpoints that match the endpoint
  group criteria to a tab separated values (TSV) file.

- **View endpoints:** Pivot from an endpoint group to a filtered list of
  endpoints on the **All Endpoints** page where you can quickly view and
  initiate actions on the endpoints within the group.

#### Manage endpoint profiles

 Cortex XSIAM provides default security profiles that you can use out of
the box to immediately begin protecting your endpoints from threats.
These profiles are applied to endpoints by mapping them to policies and
then mapping the policies to endpoints.

While security rules enable you to block or allow files to run on your
endpoints, security profiles help you customize and reuse settings
across different groups of endpoints. When the Cortex XDR agent detects
behavior that matches a rule defined in your security policy, it applies
the security profile that is attached to the rule for further
inspection.

**Related information**

- [/document/preview/953906#UUID-96637ab0-4b96-ac8c-66cc-61dc18f3aa5e](/document/preview/953906#UUID-96637ab0-4b96-ac8c-66cc-61dc18f3aa5e)

- [Set up exploit prevention
  profiles](#UUID6386af9aca64a1798ab833489f5c488c)

- [/document/preview/868498#UUID-416260cf-dda6-2267-9eaa-b66a68471cb6](/document/preview/868498#UUID-416260cf-dda6-2267-9eaa-b66a68471cb6)

- [Set up restrictions prevention
  profiles](#UUID782ed1ba266abada97ca57d2dbd475e3)

- [Set up exception profiles and
  rules](#UUIDd966bf691d536e2a8ab7cea3141baa13)

#### Endpoint data collection

When the Cortex XDR agent generates an issue on endpoint activity, a
minimum set of metadata about the endpoint is sent to the server.

When you enable behavioral threat protection or EDR data collection in
your endpoint security policy, the Cortex XDR agent can also
continuously monitor endpoint activity for malicious event chains
identified by Palo Alto Networks. The endpoint data that the Cortex XDR
agent collects when you enable these capabilities varies by platform
type.

##### Metadata collected for Cortex XDR agent issues

When the Cortex XDR agent generates an issue on endpoint activity, the
following metadata is sent to the server:

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  Absolute timestamp                  Kernel system time

  Relative timestamp                  Uptime since the computer started

  Thread ID                           ID of the originating thread

  Process ID                          ID of the originating process

  Process creation time               Part of the process unique ID per
                                      boot session (PID + creation time)

  Sequence ID                         Unique integer per boot session

  Primary user SID                    Unique identifier of the user

  Impersonating user SID              Unique identifier of the
                                      impersonating user, if applicable
  -----------------------------------------------------------------------

##### EDR data collected for Windows endpoints

+-------------------------+--------------------------------------------------+--------------------------------------+
| Category                | Events                                           | Attributes                           |
+=========================+==================================================+======================================+
| Mount a device (volume  | - Mount                                          | - Storage device name                |
| and hardware)           |                                                  |                                      |
|                         | - Unmount                                        | - Storage device class GUID          |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device class name          |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device bus type            |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device volume GUID         |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device mount point         |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device drive type          |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device vendor ID           |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device product ID          |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device serial number       |
|                         |                                                  |                                      |
|                         |                                                  | - Storage device virtual volume      |
|                         |                                                  |   image                              |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Executable metadata     | Process start                                    | - File size                          |
| (*Traps 6.1 and later*) |                                                  |                                      |
|                         |                                                  | - File access time                   |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Files                   | - Create                                         | - Full path of the modified file     |
|                         |                                                  |   before and after modification      |
|                         | - Write                                          |                                      |
|                         |                                                  | - SHA256 and MD5 hash for the file   |
|                         | - Delete                                         |   after modification                 |
|                         |                                                  |                                      |
|                         | - Rename                                         | - SetInformationFile for timestamps  |
|                         |                                                  |   (*Traps 6.1 and later*)            |
|                         | - Move                                           |                                      |
|                         |                                                  | - File set security (DACL)           |
|                         | - Modification (*Traps 6.1 and later*)           |   information                        |
|                         |                                                  |   (*Traps 6.1 and later*)            |
|                         | - Symbolic links (*Traps 6.1 and later*)         |                                      |
|                         |                                                  | - Resolve hostnames on local network |
|                         |                                                  |   (*Traps 6.1 and later*)            |
|                         |                                                  |                                      |
|                         |                                                  | - Symbolic-link/hard-link and        |
|                         |                                                  |   reparse point creation             |
|                         |                                                  |   (*Traps 6.1 and later*)            |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Image (DLL)             | Load                                             | - Full path                          |
|                         |                                                  |                                      |
|                         |                                                  | - Base address                       |
|                         |                                                  |                                      |
|                         |                                                  | - Target process-id/thread-id        |
|                         |                                                  |                                      |
|                         |                                                  | - Image size                         |
|                         |                                                  |                                      |
|                         |                                                  | - Signature (*Traps 6.1 and later*)  |
|                         |                                                  |                                      |
|                         |                                                  | - SHA256 and MD5 hash for the DLL    |
|                         |                                                  |   (*Traps 6.1 and later*)            |
|                         |                                                  |                                      |
|                         |                                                  | - File size (*Traps 6.1 and later*)  |
|                         |                                                  |                                      |
|                         |                                                  | - File access time                   |
|                         |                                                  |   (*Traps 6.1 and later*)            |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Process                 | - Create                                         | - Process ID (PID) of the parent     |
|                         |                                                  |   process                            |
|                         | - Terminate                                      |                                      |
|                         |                                                  | - PID of the process                 |
|                         |                                                  |                                      |
|                         |                                                  | - Full path                          |
|                         |                                                  |                                      |
|                         |                                                  | - Command line arguments             |
|                         |                                                  |                                      |
|                         |                                                  | - Integrity level to determine if    |
|                         |                                                  |   the process is running with        |
|                         |                                                  |   elevated privileges                |
|                         |                                                  |                                      |
|                         |                                                  | - Hash (SHA256 and MD5)              |
|                         |                                                  |                                      |
|                         |                                                  | - Signature or signing certificate   |
|                         |                                                  |   details                            |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Thread                  | Injection                                        | - Thread ID of the parent thread     |
|                         |                                                  |                                      |
|                         |                                                  | - Thread ID of the new or            |
|                         |                                                  |   terminating thread                 |
|                         |                                                  |                                      |
|                         |                                                  | - Process that initiated the thread  |
|                         |                                                  |   if from another process            |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Network                 | - Accept                                         | - Source IP address and port         |
|                         |                                                  |                                      |
|                         | - Connect                                        | - Destination IP address and port    |
|                         |                                                  |                                      |
|                         | - Create                                         | - Failed connection                  |
|                         |                                                  |                                      |
|                         | - Listen                                         | - Protocol (TCP/UDP)                 |
|                         |                                                  |                                      |
|                         | - Close                                          | - Resolve hostnames on local network |
|                         |                                                  |                                      |
|                         | - Bind                                           |                                      |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Network protocols       | - DNS request and UDP response                   | - Origin country                     |
|                         |                                                  |                                      |
|                         | - HTTP connect                                   | - Remote IP address and port         |
|                         |                                                  |                                      |
|                         | - HTTP disconnect                                | - Local IP address and port          |
|                         |                                                  |                                      |
|                         | - HTTP proxy parsing                             | - Destination IP address and port if |
|                         |                                                  |   proxy connection                   |
|                         |                                                  |                                      |
|                         |                                                  | - Network connection ID              |
|                         |                                                  |                                      |
|                         |                                                  | - IPv6 connection status             |
|                         |                                                  |   (true/false)                       |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Network statistics      | - On-close statistics                            | - Upload volume on TCP link          |
|                         |                                                  |                                      |
|                         | - Periodic statistics                            | - Download volume on TCP link        |
|                         |                                                  |                                      |
|                         |                                                  | Traps sends statistics both when a   |
|                         |                                                  | connection is closed, and at         |
|                         |                                                  | periodic intervals while the         |
|                         |                                                  | connection remains open.             |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Registry                | - Registry value:                                | - Registry path of the modified      |
|                         |                                                  |   value or key                       |
|                         |   - Deletion                                     |                                      |
|                         |                                                  | - Name of the modified value or key  |
|                         |   - Set                                          |                                      |
|                         |                                                  | - Data of the modified value         |
|                         | - Registry key:                                  |                                      |
|                         |                                                  |                                      |
|                         |   - Creation                                     |                                      |
|                         |                                                  |                                      |
|                         |   - Deletion                                     |                                      |
|                         |                                                  |                                      |
|                         |   - Rename                                       |                                      |
|                         |                                                  |                                      |
|                         |   - Addition                                     |                                      |
|                         |                                                  |                                      |
|                         |   - Modification (set information)               |                                      |
|                         |                                                  |                                      |
|                         |   - Restore                                      |                                      |
|                         |                                                  |                                      |
|                         |   - Save                                         |                                      |
|                         |                                                  |                                      |
|                         | > **Important**                                  |                                      |
|                         | >                                                |                                      |
|                         | > Registry key is collected as a real key name,  |                                      |
|                         | > and not as a symbolic link.                    |                                      |
|                         | >                                                |                                      |
|                         | > Instead of                                     |                                      |
|                         | > `HKEY_LOCAL_MACHINE\System\CurrentControlSet`, |                                      |
|                         | > which is a symbolic                            |                                      |
|                         | > link`, KEY_LOCAL_MACHINE\System\ControlSet001` |                                      |
|                         | > will be collected.                             |                                      |
|                         | >                                                |                                      |
|                         | > Instead of `HKEY_CURRENT_USER`,                |                                      |
|                         | > `HKEY_USERS\<SID>` will be collected, where    |                                      |
|                         | > SID is a SID of the current user.              |                                      |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Session                 | - Log on                                         | - Interactive log-on (log-on at a    |
|                         |                                                  |   computer console using credentials |
|                         | - Log off                                        |   such as a username and password)   |
|                         |                                                  |                                      |
|                         | - Connect                                        | - Session ID                         |
|                         |                                                  |                                      |
|                         | - Disconnect                                     | - Session State (equivalent to the   |
|                         |                                                  |   event type)                        |
|                         |                                                  |                                      |
|                         |                                                  | - Local (physically on the computer) |
|                         |                                                  |   or remote (connected using a       |
|                         |                                                  |   terminal services session)         |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Host status             | - Boot                                           | - Host name                          |
|                         |                                                  |                                      |
|                         | - Suspend                                        | - OS Version                         |
|                         |                                                  |                                      |
|                         | - Resume                                         | - Domain                             |
|                         |                                                  |                                      |
|                         |                                                  | - Previous and current state         |
+-------------------------+--------------------------------------------------+--------------------------------------+
| User presence           | User Detection                                   | Detection when a user is present or  |
| (*Traps 6.1 and later*) |                                                  | idle per active user session on the  |
|                         |                                                  | computer.                            |
+-------------------------+--------------------------------------------------+--------------------------------------+
| RPC calls               | - RpcCall                                        | - action_rpc_interface_uuid          |
|                         |                                                  |                                      |
|                         | - RpcPreCall                                     | - action_rpc_interface_version_major |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_interface_version_minor |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_func_opnum              |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_func_str_call_fields    |
|                         |                                                  |   (optional)                         |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_func_int_call_fields    |
|                         |                                                  |   (optional)                         |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_interface_name          |
|                         |                                                  |                                      |
|                         |                                                  | - action_rpc_func_name               |
+-------------------------+--------------------------------------------------+--------------------------------------+
| System calls            | Syscall types change frequently, and can be      | - action_syscall_string_params       |
|                         | observed in each event\'s data.                  |                                      |
|                         |                                                  | - action_syscall_int_params          |
|                         |                                                  |                                      |
|                         |                                                  | - action_syscall_target_instance_id  |
|                         |                                                  |                                      |
|                         |                                                  | - action_syscall_target_image_path   |
|                         |                                                  |                                      |
|                         |                                                  | - action_syscall_target_image_name   |
|                         |                                                  |                                      |
|                         |                                                  | - action_syscall_target_os_pid       |
|                         |                                                  |                                      |
|                         |                                                  | - action_syscall_target_thread_id    |
|                         |                                                  |                                      |
|                         |                                                  | - address_mapping                    |
+-------------------------+--------------------------------------------------+--------------------------------------+
| Event log               | See the table below for the list of Windows      |                                      |
|                         | Event Logs that can be sent to the server.       |                                      |
+-------------------------+--------------------------------------------------+--------------------------------------+

##### Windows event logs collected for Windows endpoints

Cortex XDR agents can send the following Windows Event Logs to the
tenant.

Cortex XSIAM saves the Windows event logs both in xdr_data and in the
microsoft_windows_raw datasets.

For more information on how to set up Windows event logs collection, see
[Microsoft Windows security auditing
setup](#UUID5ff1171c1dfde73dccf7c00dd6948e1f).

+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Path                                                     | Provider                            | Event IDs and Description         |
+==========================================================+=====================================+===================================+
| Application                                              | EMET                                |                                   |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Application                                              | Windows Error Reporting             | Only for Windows Error Reporting  |
|                                                          |                                     | (WER) events when an application  |
|                                                          |                                     | stops unexpectedly                |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Application                                              | Microsoft-Windows-User Profiles     | - **1511**: A user logged on with |
|                                                          | Service                             |   a temporary profile because     |
|                                                          |                                     |   Windows could not find the      |
|                                                          |                                     |   user\'s local profile.          |
|                                                          |                                     |                                   |
|                                                          |                                     | - **1518**: A profile could not   |
|                                                          |                                     |   be created using a temporary    |
|                                                          |                                     |   profile                         |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Application                                              | Application Error                   | **1000**: Application unexpected  |
|                                                          |                                     | stop/hang events, similar to      |
|                                                          |                                     | WER/1001. These events include    |
|                                                          |                                     | the full path to the EXE file, or |
|                                                          |                                     | to the module with the fault.     |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Application                                              | Application Hang                    | **1002**: Application unexpected  |
|                                                          |                                     | stop/hang events, similar to      |
|                                                          |                                     | WER/1001. These events include    |
|                                                          |                                     | the full path to the EXE file, or |
|                                                          |                                     | to the module with the fault.     |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-LDAP-client                            |                                     | **30**: Windows Event Collector   |
|                                                          |                                     | (WEC) recommended event           |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-CAPI2/Operational                      |                                     | Windows CAPI2 logging events:     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **11**: Build Chain             |
|                                                          |                                     |                                   |
|                                                          |                                     | - **70**: A Private Key was       |
|                                                          |                                     |   accessed                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **90**: X509 object             |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-DNS-Client/Operational                 |                                     | **3008**: A DNS query was         |
|                                                          |                                     | completed without local machine   |
|                                                          |                                     | name resolution events, and       |
|                                                          |                                     | without empty name resolution     |
|                                                          |                                     | events.                           |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-DriverFrameworks-UserMode/Operational  |                                     | **2004**: Detection of User-Mode  |
|                                                          |                                     | drivers loading, for potential    |
|                                                          |                                     | BadUSB detection                  |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-PowerShell/Operational                 |                                     | - **4103**: Block an activity     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4104**: Remote command        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4105**: Start command         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4106**: Stop command          |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-PrintService                           | Microsoft-Windows-PrintService      |                                   |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-TaskScheduler/Operational              | Microsoft-Windows-TaskScheduler     | **106, 129, 141, 142, 200, 201**  |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-TerminalServices-RDPClient/Operational |                                     | **1024**: A terminal service (TS) |
|                                                          |                                     | attempted to connect to a remote  |
|                                                          |                                     | server                            |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-Windows Defender/Operational           |                                     | - **1006**: Microsoft Defender    |
|                                                          |                                     |   Antivirus detected suspicious   |
|                                                          |                                     |   behavior                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **1009**: Microsoft Defender    |
|                                                          |                                     |   Antivirus restored an item from |
|                                                          |                                     |   quarantine                      |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Antimalware-Scan-Interface                     |                                     | **1101**: Anti-Malware Scan       |
|                                                          |                                     | Interface (AMSI) content scan     |
|                                                          |                                     | event                             |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-Windows Defender/Operational           |                                     | - **1116**: Microsoft Defender    |
|                                                          |                                     |   Antivirus detected malware or   |
|                                                          |                                     |   other potentially unwanted      |
|                                                          |                                     |   software                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **1119**: Microsoft Defender    |
|                                                          |                                     |   Antivirus encountered a         |
|                                                          |                                     |   critical error when taking      |
|                                                          |                                     |   action on malware or other      |
|                                                          |                                     |   potentially unwanted software   |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Microsoft-Windows-Windows Firewall With Advanced         | Microsoft-Windows-Windows Firewall  | **2004, 2005, 2006, 2009, 2033**: |
| Security/Firewall                                        | With Advanced Security              | Windows Firewall With Advanced    |
|                                                          |                                     | Security Local Modifications      |
|                                                          |                                     | (Levels 0, 2, 4)                  |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 |                                     | **1102**: The Security log        |
|                                                          |                                     | cleared events                    |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Eventlog          | Event log service events specific |
|                                                          |                                     | to the Security channel           |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 |                                     | - **4880**: Certificate Authority |
|                                                          |                                     |   Service stopped                 |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4881**: Certificate Authority |
|                                                          |                                     |   Service started                 |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4896**: Certificate Authority |
|                                                          |                                     |   database rows were deleted      |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4898**: A Certificate         |
|                                                          |                                     |   Authority template was loaded   |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 |                                     | Routing and Remote Access Service |
|                                                          |                                     | (RRAS) events (these are only     |
|                                                          |                                     | generated on Microsoft IAS        |
|                                                          |                                     | server)                           |
|                                                          |                                     |                                   |
|                                                          |                                     | - **6272**: User access was       |
|                                                          |                                     |   granted.                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **6280**: User account unlocked |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | - **4624**: Successful logon      |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4625**: Failed logon          |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4634**: Logoff                |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4647**: User initiated logoff |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4648**: Logon attempted,      |
|                                                          |                                     |   explicit credentials            |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4649**: Replay attack         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4672**: Special privileges    |
|                                                          |                                     |   attempted login                 |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4768**: Kerberos TGT request  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4769**: Kerberos service      |
|                                                          |                                     |   ticket requested                |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4770**: Kerberos service      |
|                                                          |                                     |   ticket renewal                  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4771**: Kerberos              |
|                                                          |                                     |   pre-authentication failed       |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4776**: Domain controller     |
|                                                          |                                     |   validation attempt              |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4778**: Session was           |
|                                                          |                                     |   reconnected to a Windows        |
|                                                          |                                     |   station                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4800**: Workstation locked    |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4801**: Workstation unlocked  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4802**: Screensaver was       |
|                                                          |                                     |   invoked                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4803**: Screensaver was       |
|                                                          |                                     |   dismissed                       |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | - **4720**: A user account was    |
|                                                          |                                     |   created                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4722**: A user account was    |
|                                                          |                                     |   enabled                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4723**: An attempt was made   |
|                                                          |                                     |   to change an account\'s         |
|                                                          |                                     |   password                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4724**: An attempt was made   |
|                                                          |                                     |   to reset an account's password  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4725**: A user account was    |
|                                                          |                                     |   disabled                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4726**: A user account was    |
|                                                          |                                     |   deleted                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4727, 4731, 4754**: Creation  |
|                                                          |                                     |   of Groups                       |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4728, 4732, 4756**: Group     |
|                                                          |                                     |   member additions                |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4729, 4733, 4757**: Group     |
|                                                          |                                     |   member removals                 |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4735, 4737, 4755, 4764**:     |
|                                                          |                                     |   Group changes                   |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4738**: A user account was    |
|                                                          |                                     |   changed                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4740**: A user account was    |
|                                                          |                                     |   locked out                      |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4741**: A computer account    |
|                                                          |                                     |   was created                     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4742**: A computer account    |
|                                                          |                                     |   was changed                     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4743**: A computer account    |
|                                                          |                                     |   was deleted                     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4765, 4766**: SID history     |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4767**: A user account was    |
|                                                          |                                     |   unlocked                        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4780**: ACL set on accounts   |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4781**: The name of an        |
|                                                          |                                     |   account was changed             |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4799**: Group membership      |
|                                                          |                                     |   enumeration                     |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | - **4616**: System time was       |
|                                                          |                                     |   changed                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4821**: Kerberos service      |
|                                                          |                                     |   ticket was denied               |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4822, 4823**: New Technology  |
|                                                          |                                     |   LAN Manager (NTLM)              |
|                                                          |                                     |   authentication failed           |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4824**: Kerberos              |
|                                                          |                                     |   pre-authentication failed       |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4825**: A user was denied     |
|                                                          |                                     |   access to Remote Desktop        |
|                                                          |                                     |                                   |
|                                                          |                                     | - **5058**: Key file operation    |
|                                                          |                                     |                                   |
|                                                          |                                     | - **5059**: Key migration         |
|                                                          |                                     |   operation                       |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | - **4698**: A scheduled task was  |
|                                                          |                                     |   created                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4702**: A scheduled task was  |
|                                                          |                                     |   updated                         |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4886**: Certificate Services  |
|                                                          |                                     |   received a certificate request  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4887**: Certificate Services  |
|                                                          |                                     |   approved a certificate request  |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4899**: A Certificate         |
|                                                          |                                     |   Services template was updated   |
|                                                          |                                     |                                   |
|                                                          |                                     | - **4900**: Certificate Services  |
|                                                          |                                     |   template security was updated   |
|                                                          |                                     |                                   |
|                                                          |                                     | - **5140**: A network share       |
|                                                          |                                     |   object was accessed             |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | **4713**: Kerberos policy was     |
|                                                          |                                     | changed on a domain controller    |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+
| Security                                                 | Microsoft-Windows-Security-Auditing | **4662**: An operation was        |
|                                                          |                                     | performed on an Active Directory  |
|                                                          |                                     | object                            |
+----------------------------------------------------------+-------------------------------------+-----------------------------------+

##### EDR data collected for Mac endpoints

+-----------------------+-----------------------+-----------------------+
| Category              | Events                | Attributes            |
+=======================+=======================+=======================+
| Files                 | - Create              | - Full path of the    |
|                       |                       |   modified file       |
|                       | - Write               |   before and after    |
|                       |                       |   modification        |
|                       | - Delete              |                       |
|                       |                       | - SHA256 and MD5 hash |
|                       | - Rename              |   for the file after  |
|                       |                       |   modification        |
|                       | - Move                |                       |
|                       |                       |                       |
|                       | - Open                |                       |
+-----------------------+-----------------------+-----------------------+
| Process               | - Start               | - Process ID (PID) of |
|                       |                       |   the parent process  |
|                       | - Stop                |                       |
|                       |                       | - PID of the process  |
|                       |                       |                       |
|                       |                       | - Full path           |
|                       |                       |                       |
|                       |                       | - Command line        |
|                       |                       |   arguments           |
|                       |                       |                       |
|                       |                       | - Integrity level to  |
|                       |                       |   determine if the    |
|                       |                       |   process is running  |
|                       |                       |   with elevated       |
|                       |                       |   privileges          |
|                       |                       |                       |
|                       |                       | - Hash (SHA256 and    |
|                       |                       |   MD5)                |
|                       |                       |                       |
|                       |                       | - Signature or        |
|                       |                       |   signing certificate |
|                       |                       |   details             |
+-----------------------+-----------------------+-----------------------+
| Network               | - Accept              | - Source IP address   |
|                       |                       |   and port            |
|                       | - Connect             |                       |
|                       |                       | - Destination IP      |
|                       | - Connect Failure     |   address and port    |
|                       |                       |                       |
|                       | - Disconnect          | - Failed connection   |
|                       |                       |                       |
|                       | - Listen              | - Protocol (TCP/UDP)  |
|                       |                       |                       |
|                       | - Statistics          | - Aggregated          |
|                       |                       |   send/receive        |
|                       |                       |   statistics for the  |
|                       |                       |   connection          |
+-----------------------+-----------------------+-----------------------+
| Event log             | - Authentication      | - Provider Name       |
|                       |                       |                       |
|                       |                       | - Data fields         |
|                       |                       |                       |
|                       |                       | - Message             |
+-----------------------+-----------------------+-----------------------+

##### EDR data collected for Linux endpoints

+-----------------------+-----------------------+-----------------------+
| Category              | Events                | Attributes            |
+=======================+=======================+=======================+
| Files                 | - Create              | - Full path of the    |
|                       |                       |   file                |
|                       | - Open                |                       |
|                       |                       | - Hash of the file    |
|                       | - Write               |                       |
|                       |                       | > **Note**            |
|                       | - Delete              | >                     |
|                       |                       | > For specific files  |
|                       |                       | > only and only if    |
|                       |                       | > the file was        |
|                       |                       | > written.            |
+-----------------------+-----------------------+-----------------------+
| - Copy                | - Full paths of both  |                       |
|                       |   the original and    |                       |
| - Move (rename)       |   the modified files  |                       |
+-----------------------+-----------------------+-----------------------+
| - Change owner        | - Full path of the    |                       |
|   (chown)             |   file                |                       |
|                       |                       |                       |
| - Change mode (chmod) | - Newly set           |                       |
|                       |   owner/attributes    |                       |
+-----------------------+-----------------------+-----------------------+
| Network               | - Listen              | - Source IP address   |
|                       |                       |   and port for        |
|                       | - Accept              |   explicit binds      |
|                       |                       |                       |
|                       | - Connect             | - Destination IP      |
|                       |                       |   address and port    |
|                       | - Connect failure     |                       |
|                       |                       | - Failed TCP          |
|                       | - Disconnect          |   connections         |
|                       |                       |                       |
|                       |                       | - Protocol (TCP/UDP)  |
+-----------------------+-----------------------+-----------------------+
| Process               | - Start               | - PID of the child    |
|                       |                       |   process             |
|                       |                       |                       |
|                       |                       | - PID of the parent   |
|                       |                       |   process             |
|                       |                       |                       |
|                       |                       | - Full image path of  |
|                       |                       |   the process         |
|                       |                       |                       |
|                       |                       | - Command line of the |
|                       |                       |   process             |
|                       |                       |                       |
|                       |                       | - Hash of the image   |
|                       |                       |   (SHA256 & MD5)      |
+-----------------------+-----------------------+-----------------------+
| - Stop                | - PID of the stopped  |                       |
|                       |   process             |                       |
+-----------------------+-----------------------+-----------------------+
| Event log             | - Authentication      | - Provider Name       |
|                       |                       |                       |
|                       |                       | - Data fields         |
|                       |                       |                       |
|                       |                       | - Message             |
+-----------------------+-----------------------+-----------------------+

##### IT performance metrics

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Time                              | - Generated time                  |
|                                   |                                   |
|                                   | - Timestamp                       |
+-----------------------------------+-----------------------------------+
| Agent information                 | - Agent ID                        |
|                                   |                                   |
|                                   | - Agent hostname                  |
|                                   |                                   |
|                                   | - Agent OS type                   |
|                                   |                                   |
|                                   | - Agent host boot time            |
|                                   |                                   |
|                                   | - Agent session start time        |
|                                   |                                   |
|                                   | - Agent request time              |
+-----------------------------------+-----------------------------------+
| Event information                 | - Event ID                        |
|                                   |                                   |
|                                   | - Event type                      |
|                                   |                                   |
|                                   | - Event subtype                   |
|                                   |                                   |
|                                   | - Event version                   |
|                                   |                                   |
|                                   | - Event timestamp                 |
+-----------------------------------+-----------------------------------+
| Actor information                 | Actor process instance ID         |
+-----------------------------------+-----------------------------------+
| OS actor information              | - OS actor process instance ID    |
|                                   |                                   |
|                                   | - OS actor process OS PID         |
|                                   |                                   |
|                                   | - OS actor process OS name        |
+-----------------------------------+-----------------------------------+
| Sample information                | - Sample start                    |
|                                   |                                   |
|                                   | - Sample end                      |
+-----------------------------------+-----------------------------------+
| CPU usage information             | - CPU max                         |
|                                   |                                   |
|                                   | - CPU average                     |
|                                   |                                   |
|                                   | - CPU 90th percentile             |
+-----------------------------------+-----------------------------------+
| Memory usage information          | - Memory max                      |
|                                   |                                   |
|                                   | - Memory average                  |
|                                   |                                   |
|                                   | - Memory 90th percentile          |
+-----------------------------------+-----------------------------------+
| Vendor                            | Vendor name                       |
+-----------------------------------+-----------------------------------+
| Product                           | Product name                      |
+-----------------------------------+-----------------------------------+
| ZIP                               | ZIP ID                            |
+-----------------------------------+-----------------------------------+
| Server information                | Server request time               |
+-----------------------------------+-----------------------------------+

#### Configure global agent settings

In addition to the customizable Agent Settings Profiles for each
Operating System and different endpoint targets, you can configure
global Agent Configurations that apply to all the endpoints in your
network.

1.  From Cortex XSIAM, select Settings \> Configurations \> General \>
    Agent Configurations.

2.  Set global uninstall password.

- The uninstall password is required to remove a Cortex XDR agent and to
  grant access to the agent security component on the endpoint. You can
  use the default uninstall `Password1` defined in Cortex XSIAM or set a
  new one and **Save**. This global uninstall password applies to all
  the endpoints (excluding mobile) in your network. If you change the
  password later on, the new default password applies to all new and
  existing profiles to which it applied before. If you want to use a
  different password to uninstall specific agents, you can override the
  default global uninstall password by setting a different password for
  those agents in the Agent Settings profile. The selected password must
  satisfy the requirements enforced by **Password Strength** indicator.

  A new password must satisfy the following **Password Strength**
  indicator requirements:

  - It must be 8 to 32 characters.

  - It must contain at least one upper-case, at least one lower-case
    letter, at least one number, and at least one of the following
    characters: `!@#%`.

3.  Manage the content updates bandwidth and frequency in your network.

    - **Enable bandwidth control:** Palo Alto Networks enables you to
      control your Cortex XDR agent network consumption by adjusting the
      bandwidth it is allocated. Based on the number of agents you want
      to update with content and upgrade packages, active or future
      agents, the Cortex XSIAM calculator configures the recommended
      amount of Mbps (Megabits per second) required for a connected
      agent to retrieve a content update over a 24 hour period or a
      week. Cortex XSIAM supports between 20 - 10000 Mbps, you can enter
      one of the recommended values or enter one of your own. For
      optimized performance and reduced bandwidth consumption, we
      recommend that you install and update new agents with the latest
      version, and include the content package built in using SCCM.

    - **Enable minor content version updates:** The Cortex XSIAM
      research team releases more frequent content updates in-between
      major content versions to ensure your network is constantly
      protected against the latest and newest threats in the wild.
      Enabled by default, the Cortex XDR agent receives minor content
      updates, starting with the next content releases. To learn more
      about the minor content numbering format, refer to the [About
      content updates](#UUIDbd20da96d2c78f88051188c056c820c0) topic.

4.  Configure content bandwidth allocated for all endpoints.

- To control the amount of bandwidth allocated in your network to Cortex
  XSIAM content updates, assign a **Content bandwidth management** value
  between 20-10,000 Mbps. To help you with this calculation, Cortex
  XSIAM recommends the optimal value of Mbps based on the number of
  active agents in your network, and including overhead considerations
  for large content updates. Cortex XSIAM verifies that agents
  attempting to download the content update are within the allocated
  bandwidth before beginning the distribution. If the bandwidth has
  reached its cap, the download will be refused and the agents will
  attempt again at a later time. After you set the bandwidth, **Save**
  the configuration.

5.  Configure the Cortex XDR agent auto upgrade scheduler and number of
    parallel upgrades.

- If Agent auto upgrades are enabled for your Cortex XDR agents, you can
  control the automatic upgrade process in your network. To better
  control the rollout of a new Cortex XDR agent release in your
  organization, during the first week only a single batch of agents is
  upgraded. After that, auto-upgrades continue to be deployed across
  your network with number of parallel upgrades as configured.

  - **Amount of Parallel Upgrades:** Set the number of parallel agent
    upgrades, where the maximum is 2000 agents. When you configure this,
    keep in mind your organization\'s bandwidth usage and resource
    consumption.

  - **Days in week:** You can schedule the upgrade task for specific
    days of the week and a specific time range. The minimum range is
    four hours.

6.  Configure automated Advanced Analysis of Cortex XDR Agent alerts
    raised by exploit protection modules.

- Advanced Analysis is an additional verification method you can use to
  validate the verdict issued by the Cortex XDR agent. In addition,
  Advanced Analysis also helps Palo Alto Networks researchers tune
  exploit protection modules for accuracy.

  To initiate additional analysis you must retrieve data about the alert
  from the endpoint. You can do this manually on an alert-by-alert basis
  or you can enable Cortex XSIAM to automatically retrieve the files.

  After Cortex XSIAM receives the data, it automatically analyzes the
  memory contents and renders a verdict. When the analysis is complete,
  Cortex XSIAM displays the results in the **Advanced Analysis** field
  of the Additional data view for the data retrieval action on the
  **Action Center**. If the Advanced Analysis verdict is benign, you can
  avoid subsequent blocked files for users that encounter the same
  behavior by enabling Cortex XSIAM to automatically create and
  distribute exceptions based on the Advanced Analysis results.

  a.  Configure the desired options:

      - Enable Cortex XSIAM to automatically upload defined alert data
        files for advanced analysis. Advanced Analysis increases the
        Cortex XSIAM exploit protection module accuracy.

      - Automatically apply Advanced Analysis exceptions to your Global
        Exceptions list. This will apply all Advanced Analysis
        exceptions suggested by Cortex XSIAM, regardless of the alert
        data file source.

  b.  **Save** the Advanced Analysis configuration.

7.  Configure the Cortex XDR Agent license revocation and deletion
    period.

- This configuration applies to standard endpoints only and does not
  impact the license status of agents for VDIs or Temporary Sessions.

  a.  Configure the desired options:

      - **Connection Lost (Days):** Configure the number of days after
        which the license should be returned when an agent loses the
        connection to Cortex XSIAM. Default is 30 days; Range is 2 to 60
        days. Day one is counted as the first 24 hours with no
        connection.

      - **Agent Deletion (Days):** Configure the number of days after
        which the agent and related data is removed from the Cortex
        XSIAM management console and database. Default is 180 days;
        Range is 3 to 360 days and must exceed the **Connection Lost**
        value. Day one is the first 24 hours of lost connection.

  b.  Click **Save** to save the Agent Status configuration.

8.  Enable WildFire analysis scoring for files with Benign verdicts.

- The WildFire analysis score for files with a Benign verdict is used to
  indicate the level of confidence WildFire has in the Benign verdict.
  For example, a file by a trusted signer or a file that was tested
  manually gets a high confidence Benign score, whereas a file that did
  not display any suspicious behavior at the time of testing gets a
  lower confidence Benign score. To add an additional verification
  method to such files, enable this setting. After this, when Cortex
  XSIAM receives a Benign Low Confidence verdict, the agent enforces the
  Malware Security profile settings you currently have in place
  (**Run local analysis** to determine the file verdict, **Allow**, or
  **Block**).

  > **Note**

  > Disabling this capability takes immediate effect on new hashes,
  > fresh agent installations, and existing security policies. It could
  > take up to a week to take effect on existing agents in your
  > environment pending agent caching.

9.  Enable Informative BTP Alerts.

- Behavioral threat protection (BTP) alerts have been given unique and
  informative names and descriptions, to provide immediate clarity into
  the events without having to drill down into each alert. Enable to
  display of the informative BTP rule alert names and descriptions.
  After you update the settings, new alerts include the changes while
  already existing alerts remain unaffected.

  > **Note**

  > If you have any Cortex XSIAM filters, starring policies, exclusion
  > policies, scoring rules, log forwarding queries, or automation rules
  > configured for XSOAR/3rd party SIEM, we advise you to update those
  > to support the changes before activating the feature. For example,
  > change the query to include the previous description that is still
  > available in the new description, instead of searching for an exact
  > match.

10. Configure settings for periodic cleanup of duplicate entities in the
    endpoint administration table.

- When enabled, **Periodic duplicate cleanup** removes all duplicate
  entries of an endpoint from the endpoint table based on the defined
  parameters, leaving only the last occurrence of the endpoint reporting
  to the server. This enables you to streamline and improve the
  management of your endpoints. For example, when an endpoint reconnects
  after a hardware change, it may be re-registered, leading to confusion
  in the endpoint administration table regarding the real status of the
  endpoint. The cleanup leaves only the latest record of the endpoint in
  the table.

  - Define whether to clean up according to **Host Name**,
    **Host IP Address**, **MAC Address**, or any combination of them. If
    not selected, the default is Host Name. When you select more than
    one parameter, duplicate entries are removed only if they include
    all the selected parameters.

  - Configure the frequency of the cleanup: every 6 hours, 12 hours, 1
    day, or 7 days. You can also select to perform an immediate
    **One-time cleanup**.

  Data for a deleted endpoint is retained for 90 days since the
  endpoint's last connection to the system. If a deleted endpoint
  reconnects, Cortex XSIAM recovers its existing data.

### Install Cortex XDR agents

The Cortex XDR agent monitors endpoint activity and collects endpoint
data that Cortex XSIAM uses to generate issues. Before you can begin
collecting endpoint data, you must create an agent installation package
and then install the Cortex XDR agent.

#### Plan your agent deployment

You typically deploy Cortex XDR agent software to endpoints across a
network after an initial proof of concept (POC), which simulates your
corporate production environment. During the POC or deployment stage,
you analyze security events to determine which are triggered by
malicious activity and which are due to legitimate processes behaving in
a risky or incorrect manner. You also simulate the number and types of
endpoints, the user profiles, and the types of applications that run on
the endpoints in your organization, and, according to these factors, you
define, test, and adjust the security policy for your organization.

The goal of this multi-step process is to provide maximum protection to
the organization without interfering with legitimate workflows.

After the successful completion of the initial POC, we recommend a
multi-step implementation in the corporate production environment for
the following reasons:

- The POC doesn\'t always reflect all the variables that exist in your
  production environment.

- There is a rare chance that the XDR agent will affect business
  applications, which can reveal vulnerabilities in the software as a
  prevented attack.

- During the POC, it is much easier to isolate issues that appear and
  provide a solution before full implementation in a large environment
  where issues could affect a large number of users.

A multi-step deployment approach ensures a smooth implementation and
deployment of the Cortex XSIAM

Cortex XSIAM solution throughout your network. Use the following steps
for better support and control over the added protection.

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| Step                  | Duration              | Plan                                                                                          |
+=======================+=======================+===============================================================================================+
| Prerequisite. Set up  | 1 week                | Set up the following:                                                                         |
| Cortex XSIAM access   |                       |                                                                                               |
| services              |                       | - **Firewall configuration:** Enable access to Cortex XSIAM communication servers, storage    |
|                       |                       |   buckets, and resources.                                                                     |
|                       |                       |                                                                                               |
|                       |                       | - Required certificates to establish secure communication                                     |
|                       |                       |                                                                                               |
|                       |                       | - Enable access for Windows CRL checks (Windows only)                                         |
|                       |                       |                                                                                               |
|                       |                       | - Enable peer-to-peer content updates                                                         |
|                       |                       |                                                                                               |
|                       |                       | - Validate compatibility with third-party security products                                   |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 1\. Calculate the     | As needed             | For every 100,000 agents, you will need to allocate 120 Mbps of bandwidth. The bandwidth      |
| bandwidth required to |                       | requirement scales linearly. For example, to support 300,000 agents, plan to allocate 360     |
| support the number of |                       | Mbps of bandwidth (three times the amount required for 100,000 agents).                       |
| agents you plan to    |                       |                                                                                               |
| deploy.               |                       |                                                                                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 2\. Install Cortex    | 1 week                | Install the Cortex XDR agent on a small number of endpoints (3 to 10).                        |
| XDR agent on a pilot  |                       |                                                                                               |
| group of endpoints.   |                       | Test the expected behavior of the Cortex XDR agents (injection and policy) and confirm that   |
|                       |                       | there is no change in the user experience.                                                    |
|                       |                       |                                                                                               |
|                       |                       | Review [Where can I install the cortex XDR                                                    |
|                       |                       | Agent](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Compatibility-Matrix) |
|                       |                       | for supported versions and operating systems.                                                 |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 3\. Expand the Cortex | 2 weeks               | Gradually expand agent distribution to larger groups that have similar attributes (hardware,  |
| XSIAM deployment.     |                       | software, and users). At the end of two weeks, you can have Cortex XSIAM deployed on up to    |
|                       |                       | 100 endpoints.                                                                                |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 4\. Complete the      | 2 or more weeks       | Broadly distribute the Cortex XDR agent throughout the organization until all endpoints are   |
| Cortex XSIAM          |                       | protected.                                                                                    |
| installation.         |                       |                                                                                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 5\. Define corporate  | Up to 1 week          | Add protection rules for third-party or in-house applications and then test them.             |
| policy and protected  |                       |                                                                                               |
| processes.            |                       |                                                                                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 6\. Refine corporate  | Up to 1 week          | Deploy security policy rules to a small number of endpoints that use the applications         |
| policy and protected  |                       | frequently. Fine-tune the policy as needed.                                                   |
| processes.            |                       |                                                                                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| 7\. Finalize          | A few minutes         | Deploy protection rules globally.                                                             |
| corporate policy and  |                       |                                                                                               |
| protected processes.  |                       |                                                                                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+

#### Guidelines for keeping Cortex XDR agents and content updated

This document covers a recommended strategy and best practices for
managing agent and content updates to help reduce the risk of downtime
in a production environment, while helping ensure timely delivery of
security content and capabilities.

Keeping Cortex XDR agents up-to-date is essential for protecting against
evolving threats and vulnerabilities. Regular updates ensure the latest
security features for malware and exploit prevention, and compatibility
with the latest software environments, which helps reduce the risk of
attacks. This can also help organizations meet regulatory standards
while maintaining strong overall protection.

Content updates, such as new threat intelligence or detection logic, are
critical for defending against newly discovered cyber threats and
malware and are designed to ensure that systems remain protected against
the latest attacks. Content updates, released on a weekly basis, address
compatibility issues as well, helping to achieve smooth operations
alongside the Cortex XDR agent. Without regular content updates,
security solutions may fail to detect new or evolving threats, leaving
systems vulnerable to attacks.

The Cortex XDR agent can retrieve content updates immediately as they
become available, or after a pre-configured delay period of up to 30
days. Alternatively, you can choose to select a specific version. In
addition, to expedite testing and evaluation, the staging content
provides a preview of the content update a week before its published GA.

> **Important**
>
> When planning Cortex XDR agent upgrades and content updates, consult
> with the appropriate stakeholders and teams and follow the change
> management strategy in your organization.

Cortex XSIAM can be configured to manage the deployment of agent and
content updates by adjusting the following settings:

AGENT UPGRADE SETTINGS

**Agent settings per endpoint: **

- **Agent Auto-Upgrade** is disabled by default. Before enabling agent
  auto-upgrade for Cortex XDR agents, make sure to consult with all
  relevant stakeholders in your organization. Enabling this option
  allows you to define the scope of the automatic updates, such as
  upgrading to the latest agent release, one release prior, only
  maintenance releases, or maintenance releases within a specific
  version.

- **Upgrade Rollout** includes two options: Immediate, where the Cortex
  XDR agent automatically receives new releases, including maintenance
  updates and features, and Delayed, which lets you set a delay of 7 to
  45 days after a version is released before upgrading endpoints.

**Global agent settings:** Configure the Cortex XDR agent upgrade
scheduler and the number of parallel upgrades to apply to all endpoints
in your organization. You can also schedule the upgrade task for
specific days of the week and set a specific time range for the
upgrades.

CONTENT UPDATE SETTINGS

**Content updates per endpoint: **

- **Content Auto-Update** is enabled by default and automatically
  retrieves the latest content before deploying it on the endpoint. If
  you disable content updates, the agent will stop fetching updates from
  the Cortex XSIAM tenant and will continue to operate with the existing
  content on the endpoint.

- **Content Rollout:** The Cortex XDR agent can retrieve content updates
  immediately as they become available, after a pre-configured delay
  period of up to 30 days. Alternatively, you can choose to select a
  specific version. Utilize the staging content for early evaluation on
  test environments before the content is released to production.

**Global content updates:** Configure the content update cadence and
bandwidth allocation within your organization. To enforce immediate
protection against the latest threats, enable minor content updates.
Otherwise, the content updates in your network occur only on major
releases.

**Guidelines for planning Cortex XDR agent upgrades**

Use a phased rollout plan by creating batches for deploying updates. The
specifics may vary based on your organization and its structure. Start
with a control group, then deploy to 10% of your organization.
Subsequently, allocate the remaining upgrades in batches that best suit
your organization until achieving a full 100% rollout.

The following is an example of a rollout plan for deploying a Cortex XDR
agent upgrade:

**Phase 1: Control group rollout:** Start by selecting a control group
of endpoints as early adopters. This group should consist of a diverse
range of operating systems, devices, applications, and servers, with a
focus on low-risk endpoints. After a defined testing period, such as one
week, assess for any issues. If no problems are found, move to the next
phase.

**Phase 2: 10% rollout:** Expand the rollout to 10% of the
organization's endpoints. This group should maintain the same variety as
the control group but include low- to medium-risk endpoints. Monitor
performance during the set period. If the rollout is successful with no
issues, proceed to the next phase.

**Phase 3: 40% rollout: ** After confirming the success of the 10%
rollout, extend the deployment to 40% of the organization. Continue
including a variety of endpoints while gradually incorporating some
medium-risk endpoints. Ensure thorough testing during this phase before
moving forward.

**Phase 4: 80% rollout:** Extend the deployment to 80% of the
organization\'s endpoints. This batch should include a wide variety of
endpoints, incorporating both medium and high-risk systems. After a
careful monitoring period and confirmation that everything is stable,
move to the final phase.

**Phase 5: Full rollout:** Complete the rollout by updating the
remaining 20% of the organization's endpoints. By this point, the
majority of systems should have been thoroughly tested, reducing the
risk of issues in the final stage. Once complete, 100% of the
organization will be updated.

![](media/rId310.gif){width="3.5in" height="0.6125in"}

**Guidelines for planning content updates**

Content updates consist of detection rules and operational logic, and
are typically released on a weekly basis. Staging content provides a
preview of the content update a week before thepublished GA.

Use a phased rollout plan by creating batches for deploying updates.
Start with a control group, then deploy to 10% of your organization.
Subsequently, allocate the remaining upgrades in batches that best suit
your organization until achieving a full 100% rollout.

For early evaluation, select a small test group or a lab environment for
enabling the staging content preview.

The following is an example of a rollout plan over a period of one week
for deploying content updates:

**Phase 1: Control group rollout:** Keep the default configuration set
to deploy content updates immediately.

**Phase 2: 10% rollout:** Content is automatically deployed on day 2
following a delay period defined in the profile.

**Phase 3: 60% rollout:** Content is automatically deployed on day 3
following a delay period defined in the profile.

**Phase 4: Full rollout:** Increase the deployment to include medium and
high-risk systems, until the entire organization is updated.

![](media/rId314.gif){width="3.5in" height="0.76125in"}

##### How to configure agent and content update settings

The following information will help you select and configure the update
settings.

**Cortex XDR agent upgrades**

Configure one or more of the settings described in this section to keep
your Cortex XDR agents up-to-date.

Distribute agent upgrades to selected endpoints

1.  Create an agent installation package for each operating system
    version for which you want to upgrade the Cortex XDR agent.

- Note the installation package names.

2.  Select Inventory \> Endpoints \> All Endpoints.

- If needed, filter the list of endpoints. To reduce the number of
  results, use the endpoint name search and filters at the top of the
  page.

3.  Select the endpoints you want to upgrade.

- You can also select endpoints running different operating systems to
  upgrade the agents at the same time.

4.  Right-click your selection and select Endpoint Control \> Upgrade
    Agent Version.

- For each platform, select the name of the installation package you
  want to push to the selected endpoints.

  You can install the Cortex XDR agent on Linux endpoints using a
  package manager. If you do not want to use the package manager, clear
  the option **Upgrade to installation by package manager**.

  When you upgrade an agent on a Linux endpoint that is not using a
  package manager, Cortex XSIAM upgrades the installation process by
  default according to the endpoint Linux distribution.

  > **Note**

  > The Cortex XDR agent keeps the name of the original installation
  > package after every upgrade.

5.  **Upgrade**.

- Cortex XSIAM distributes the installation package to the selected
  endpoints at the next heartbeat communication with the agent. To
  monitor the status of the upgrades, go to Investigation and Response
  \> Response \> Action Center.

  From the **Action Center** you can also view additional information
  about the upgrade (right-click the action and select
  **Additional data**) or cancel the upgrade (right-click the action and
  select **Cancel Agent Upgrade**).

  > **Note**

  - > Custom dashboards that include upgrade status widgets, and the
    > **All Endpoints** page display upgrade status.

  - > During the upgrade process, the endpoint operating system might
    > request a reboot. However, you do not have to perform the reboot
    > for the Cortex XDR agent upgrade process to complete it
    > successfully.

  - > After you upgrade on an endpoint with Cortex XSIAM Device Control
    > rules, you need to reboot the endpoint for the rules to take
    > effect.

Agent settings per endpoint

> **Note**
>
> These profiles can be configured on one or more endpoints,
> static/dynamic groups, tags, IP ranges, endpoint names, or other
> parameters that allow the creation of logical endpoint groups. See
> [how to define endpoint
> group](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Documentation/Define-endpoint-groups?tocId=3C79USa8cHopVLq9dxCMag).

1.  Go to Inventory \> Endpoints \> Policy Management \> Profiles, and
    then edit an existing profile, add a new profile, or import from a
    file.

2.  If you\'re adding a new profile, select the operating system and
    **Agent Settings**. Then click **Next**.

- If you want to edit an existing profile, hover over **Agent Settings**
  for the operating system and click **View Profile**.

3.  Select **Agent Upgrade**. By default, this option is disabled.

- > **Caution**

  > Before enabling Auto-Update for Cortex XDR agents, make sure to
  > consult with all relevant stakeholders in your organization.

The following table describes the available **Agent Auto-Upgrade**
options:

+-----------------------+-----------------------+------------------------------------------------------+
| Item                  | Options               | Description                                          |
+:======================+=======================+:=====================================================+
| Automatic Upgrade     | - Latest agent        | For **One release before the latest one**, Cortex    |
| Scope                 |   release (Default)   | XSIAM upgrades the agent to the previous release     |
|                       |                       | before the latest, including maintenance releases.   |
|                       | - One release before  | Major releases are numbered X.X, such as release     |
|                       |   the latest one      | 8.0, or 8.2. Maintenance releases are numbered       |
|                       |                       | X.X.X, such as release 8.2.2.                        |
|                       | - Only maintenance    |                                                      |
|                       |   releases            | For                                                  |
|                       |                       | **Only maintenance releases in a specific version**, |
|                       | - Only maintenance    | select the required release version.                 |
|                       |   releases in a       |                                                      |
|                       |   specific version    |                                                      |
+-----------------------+-----------------------+------------------------------------------------------+
| Upgrade Rollout       | - Immediate (Default) | The Cortex XDR agent automatically fetches any new   |
|                       |                       | agent release, maintenance and new features.         |
|                       | - Delayed             |                                                      |
|                       |                       | For **Delayed**, set the delay period (number of     |
|                       |                       | days) to wait after the version release before       |
|                       |                       | upgrading endpoints. Choose a value between 7 and    |
|                       |                       | 45.                                                  |
+-----------------------+-----------------------+------------------------------------------------------+

Global agent settings

Configure the Cortex XDR agent upgrade scheduler and the number of
parallel upgrades to apply to all endpoints in your organization.

1.  Go to Settings \> Configurations \> Agent Configurations, and scroll
    to **Agent upgrade**.

2.  Configure the Cortex XDR agent upgrade scheduler and the number of
    parallel upgrades.

+-----------------------------------+-----------------------------------+
| Item                              | Description                       |
+:==================================+:==================================+
| Amount of parallel upgrades       | During the first week of a new    |
|                                   | Cortex XDR agent release rollout, |
|                                   | only a single batch of agents is  |
|                                   | upgraded. After that,             |
|                                   | auto-upgrades continue to be      |
|                                   | deployed across your network with |
|                                   | the number of parallel upgrades   |
|                                   | as configured.                    |
|                                   |                                   |
|                                   | Set the number of parallel agent  |
|                                   | upgrades, where the maximum is    |
|                                   | 500 agents.                       |
+-----------------------------------+-----------------------------------+
| Days in week                      | Schedule the upgrade task for     |
|                                   | specific days of the week.        |
+-----------------------------------+-----------------------------------+
| Schedule                          | Schedule a specific time range.   |
|                                   | The minimum range is four hours.  |
+-----------------------------------+-----------------------------------+

**Content updates**

When a new content update is available, Cortex XSIAM notifies the Cortex
XDR agent. The Cortex XDR agent then randomly chooses a time within a
six-hour window during which it will retrieve the content update from
Cortex XSIAM. By staggering the distribution of content updates, Cortex
XSIAM reduces the bandwidth load and prevents bandwidth saturation due
to the high volume and size of the content updates across many
endpoints. You can view the distribution of endpoints by content update
version from the dashboard.

You can configure whether to update content per endpoint or use the
global settings.

![](media/rId322.png){width="3.5in" height="1.9556244531933509in"}

Content update settings per endpoint

Configure content update options for agents within the organization to
ensure it is always protected with the latest security measures.

> **Note**
>
> These profiles can be configured on one or more endpoints,
> static/dynamic groups, tags, IP ranges, endpoint names, or other
> parameters that allow the creation of logical endpoint groups.

The following table describes the available **Content Configuration**
options:

1.  Go to Inventory \> Endpoints \> Policy Management \> Profiles, and
    then edit an existing profile, add a new profile, or import from a
    file.

2.  If you\'re adding a new profile, select the operating system and
    **Agent Settings**. Then click **Next**.

- If you want to edit an existing profile, hover over **Agent Settings**
  for the operating system and click **View Profile**.

3.  Select **Content Configuration**. By default, this option is
    Enabled.

+-----------------------+-----------------------+-----------------------+
| Item                  | Options               | More details          |
+:======================+=======================+:======================+
| Content Auto-Update   | - Enabled (Default)   | When Content          |
|                       |                       | Auto-Update is        |
|                       | - Disabled            | enabled, the Cortex   |
|                       |                       | XDR agent retrieves   |
|                       |                       | the most updated      |
|                       |                       | content and deploys   |
|                       |                       | it on the endpoint.   |
|                       |                       |                       |
|                       |                       | If you disable        |
|                       |                       | content updates, the  |
|                       |                       | agent stops           |
|                       |                       | retrieving them from  |
|                       |                       | the Cortex XSIAM      |
|                       |                       | tenant, and keeps     |
|                       |                       | working with the      |
|                       |                       | current content on    |
|                       |                       | the endpoint.         |
+-----------------------+-----------------------+-----------------------+
| Staging Content       | - Enabled             | Enable users to       |
|                       |                       | deploy agent staging  |
|                       | - Disabled (Default)  | content on selected   |
|                       |                       | test environments.    |
|                       |                       | Staging content is    |
|                       |                       | released before       |
|                       |                       | production content,   |
|                       |                       | allowing for early    |
|                       |                       | evaluation of the     |
|                       |                       | latest content        |
|                       |                       | update.               |
+-----------------------+-----------------------+-----------------------+
| Content Rollout       | - Immediate (Default) | The Cortex XDR agent  |
|                       |                       | can retrieve content  |
|                       | - Delayed             | updates immediately   |
|                       |                       | as they are           |
|                       | - Specific            | available, after a    |
|                       |                       | pre-configured delay  |
|                       |                       | period of up to 30    |
|                       |                       | days, or you can      |
|                       |                       | select a specific     |
|                       |                       | version.              |
|                       |                       |                       |
|                       |                       | When you delay        |
|                       |                       | content updates, the  |
|                       |                       | Cortex XDR agent will |
|                       |                       | retrieve the content  |
|                       |                       | according to the      |
|                       |                       | configured delay. For |
|                       |                       | example, if you       |
|                       |                       | configure a delay     |
|                       |                       | period of two days,   |
|                       |                       | the agent will not    |
|                       |                       | use any content       |
|                       |                       | released in the last  |
|                       |                       | 48 hours.             |
+-----------------------+-----------------------+-----------------------+

Global content update settings

1.  Go to Settings \> Configurations \> Agent Configurations, and scroll
    to **Content Management**.

2.  Configure the content update cadence and bandwidth allocation within
    your organization.

+-----------------------------------+-----------------------------------+
| Item                              | Description                       |
+:==================================+:==================================+
| Enable bandwidth control          | Based on the number of agents you |
|                                   | want to update with content and   |
|                                   | upgrade packages, active or       |
|                                   | future agents, the Cortex XSIAM   |
|                                   | calculator configures the         |
|                                   | recommended amount of Mbps        |
|                                   | (Megabits per second) required    |
|                                   | for a connected agent to retrieve |
|                                   | a content update over a 24 hour   |
|                                   | period or a week. Cortex XSIAM    |
|                                   | supports between 20 - 10000 Mbps, |
|                                   | you can enter one of the          |
|                                   | recommended values or enter one   |
|                                   | of your own. For optimized        |
|                                   | performance and reduced bandwidth |
|                                   | consumption, it is recommended    |
|                                   | that you install and update new   |
|                                   | agents with Cortex XDR agents 7.3 |
|                                   | and later include the content     |
|                                   | package built in using SCCM.      |
+-----------------------------------+-----------------------------------+
| XDR Calculator for Recommended    | Based on the number of agents you |
| Bandwidth                         | want to update with content and   |
|                                   | upgrade packages, active or       |
|                                   | future agents, the Cortex XSIAM   |
|                                   | calculator configures the         |
|                                   | recommended amount of Mbps        |
|                                   | (Megabits per second) required    |
|                                   | for a connected agent to retrieve |
|                                   | a content update over 24 hours or |
|                                   | a week. This calculation is based |
|                                   | on connected agents and includes  |
|                                   | an overhead for large content     |
|                                   | update.                           |
|                                   |                                   |
|                                   | Cortex XSIAM supports between     |
|                                   | 20 - 10000 Mbps.                  |
|                                   |                                   |
|                                   | It is recommended to allocate a   |
|                                   | minimum of 20 Mbps, or you can    |
|                                   | enter a value.                    |
+-----------------------------------+-----------------------------------+
| Enable minor content version      | To enforce immediate protection   |
| updates                           | against the latest threats,       |
|                                   | enable minor content updates.     |
|                                   | Otherwise, the content updates in |
|                                   | your network occur only on major  |
|                                   | releases.                         |
+-----------------------------------+-----------------------------------+

#### Create an agent installation package

To install the Cortex XDR agent on the endpoint for the first time,
create an agent installation package. Review [Where can I install the
Cortex XDR
agent](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Compatibility-Matrix/Where-can-I-install-the-Cortex-XDR-agent)
for supported versions and operating systems.

To install the Cortex XDR agent software, you must use a valid
installation package that exists in your Cortex XSIAM management
console. If you delete an installation package, new agents installed
from this package are not able to register to Cortex XSIAM, however,
existing agents may re-register using the Agent ID generated by the
installation package.

1.  From Cortex XSIAM, select Inventory \> Endpoints \> Agent
    Installations.

2.  Click **Create** to create a new installer.

3.  Enter a unique name and an optional description to identify the
    installation package.

- The package name can contain letters, numbers, hyphens, underscores,
  commas, and spaces, and should not exceed 100 characters.

4.  Select the **Package Type**:

    - **Standalone Installer**: Use for fresh installations and to
      upgrade agents on a registered endpoint that is connected to
      Cortex XSIAM.

    - **Upgrade from ESM**: Use this package to upgrade Traps agents
      which connect to the on-premises Traps Endpoint Security Manager
      to Cortex XSIAM. For more information, see [Migrate from Traps
      Endpoint Security
      Manager](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Migrate-from-Traps/Migrate-from-Traps-Endpoint-Security-Manager).

    - (*Linux only*) **Kubernetes Installer**: Use for fresh
      installations and upgrades of Cortex XDR agents running on
      Kubernetes clusters.

    <!-- -->

    - Guidelines for Kubernetes installer
      - Settings for the Kubernetes installer cannot be changed after
        you create the installation package.

      - For **Version**, select the desired Cortex XDR agent version.

      <!-- -->

      - If the option **Always deploy the latest agent version** is
        displayed, do not select it.

      <!-- -->

      - For the **Agent Daemonset Namespace**, it is recommended to use
        the default **cortex-xdr** namespace.

      - For a more granular deployment, enter any labels or selectors in
        the **Node Selector**. The Cortex XDR agent will be deployed
        only on these nodes.

      - To configure the Cortex XDR agent to communicate through a
        proxy, enter either the IP address and port number or enter the
        FQDN and port number. When you enter the FQDN, you can use both
        lowercase and uppercase letters. Avoid using special characters
        or spaces. Use commas to separate multiple addresses.

    <!-- -->

    - **Helm Installer**: Use this package for fresh installations and
      upgrades of Cortex XDR agents running on Kubernetes clusters.

    - **Serverless Installer**: Create an installation package for
      serverless function to deploy to your runtime platform.

    <!-- -->

    - Guidelines for serverless installer
      **How to create an agent package for serverless function:**

      1.  From Cortex XSIAM, go to Inventory \> Endpoints \>
          Installations and click **Create**.

      2.  Add name, description and add any endpoint tags that will be
          added to the agent as part of the installation process.

      3.  For **Package Type**, select **Serverless Function**.

      4.  Configure the following settings for Serverless Function:

          1.  For **Version**, select the required Cortex agent version.

          2.  For **Cloud Provider**, AWS is configured for this
              release.

          3.  For **Runtime**, select one of the environments:

              - node.js

              - python

          4.  For **Deployment Type**, select the type:

              - Embedded

              - AWS Layers

          5.  If node.js and the deployment type, AWS Layers are
              selected, select one of the **Modules**:

              - ECMAScript

              - CommonJS

          6.  For **Embed Default Profile From**, select from the
              profile rules configured for serverless functions.

      - > **Note**

        > The profile will be applied if the security policy cannot be
        > retrieved in real-time.

      The package is created and ready to be deployed.

      **How to deploy the package to your runtime environment:**

      1.  From Cortex XSIAM, go to Inventory \> Endpoints \>
          Installations and from the **Agent Installations** page, right
          click and select **View Installation Instructions**.

      2.  Depending on the runtime environment, the instructions are
          slightly different.

          - Agent installation package for embedded python:

            1.  Download the serverless agent bundle.

            2.  Log in to your AWS Management Console.

            3.  Navigate to the AWS Lambda service, and unzip the
                serverless agent bundle in the main folder.

            4.  Add the serverless agent to the function by importing
                the Cortex library and wrapping the function's handler.

            - > **Note**

              > The Cortex serverless library must be imported after
              > other libraries to activate the hooks that enable
              > auditing.

          - Agent installation package for embedded node.js:

            1.  Download the serverless agent bundle.

            2.  Log in to your AWS Management Console.

            3.  Navigate to the AWS Lambda service, and unzip the
                serverless agent bundle in the main folder.

            4.  Add the serverless agent to the function by importing
                the Cortex library and wrapping the function's handler.

          - Agent installation package for node.js using AWS Layers in
            ECMAScript (JavaScript) runtime/Agent installation package
            for node.js in AWS Lambda using AWS Layers with CommonJS
            module format:

            1.  Download the serverless agent bundle.

            2.  Log in to your AWS Management Console.

            3.  Navigate to the AWS Lambda service, and upload the layer
                and add it to the function's configuration.

            4.  Save the current Lamba handler setting in the
                ORIGINAL_HANDLER environment variable.

            5.  Change the Lambda handler setting to cortex.handler.

5.  Select the platform and relevant settings, and then click
    **Create**.

- Cortex XSIAM prepares your installation package and displays it on the
  **Agent Installations** page.

6.  Download your installation package.

- When the status of the package shows `Completed`, right-click the
  package, and click **Download**.

#### Deploy agent installation packages

After you create and download an installation package, you can then
install it directly on an endpoint or you can use a software deployment
tool, such as JAMF or GPO, to distribute the software to multiple
endpoints.

- For Windows endpoints, select the architecture type. You can download
  the installer msi file only or a distribution package that includes
  both the installer msi file and the latest content zip. The
  distribution package is recommended to reduce the network load and
  time typically required for the initial roll-out or major upgrades of
  the Cortex XDR agent. To understand the benefits, workflow, and
  requirements to support this type of deployment, refer to the Cortex
  XDR Agent Administrator Guide.

- For macOS endpoints, download the ZIP installation folder and upload
  it to the endpoint. To deploy the Cortex XDR agent using JAMF, upload
  the ZIP folder to JAMF. Alternatively, to install the agent manually
  on the endpoint, unzip the ZIP folder and double-click the pkg file.

- For Linux endpoints, you can download .rpm or .deb installers
  (according to the endpoint Linux distribution), and deploy the
  installers on the endpoints using the Linux package manager.
  Alternatively, you can download a Shell installer and deploy it
  manually on the endpoint.

- For Kubernetes clusters on Linux endpoints, download the YAML
  file. We strongly recommend that you do not edit this file.

- For Android endpoints, Cortex XDR creates a tenant-specific download
  link that you can distribute to Android endpoints. When a newer agent
  version is available, Cortex XDR identifies older package versions
  as \[Outdated\].

**Related information**

- Cortex XDR Agent Administrator Guide

- Agent iOS Guide

- Agent Android Guide

### Configure and deploy Cortex XSIAM

#### Cortex XSIAM - Analytics

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

##### Configure Cortex XSIAM network parameters

Define your internal IP address ranges and domain names to enable Cortex
XSIAM to identify, track, and analyze network assets.

###### Define internal IP address ranges

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

###### Define internal domain names

1.  Select Inventory \> Assets \> Network Configuration \> Internal
    Domain Suffixes.

2.  Type the domain suffix you want to include as part of your internal
    network, for example, `acme.com`.

3.  Select ![](media/rId340.png){width="0.14583333333333334in"
    height="0.20833333333333334in"} to add the suffix to the
    **Domains List**.

##### Enable the Analytics Engine and Identity Analytics

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

#### Cortex XSIAM engines

Engines are installed in a remote network and allow communication
between the remote network and Cortex XSIAM. You can run integration
commands on an engine. It is possible to install a single engine or
multiple engines.

You can install multiple engines on the same machine (Shell installation
only) which is useful in a dev-prod environment where you do not want to
have numerous engines in different environments, and to manage those
machines.

##### Engine requirements

You can install engines on all Linux environments. Docker/Podman needs
to be installed before installing an engine. If you are using the shell
installer for an engine, Docker/Podman is installed automatically.

> **Note**
>
> The Cron package is required to install engines on a Linux machine.

**Engine hardware requirements**

If your hard drive is partitioned, we recommend a minimum of 50 GB for
the `/var` partition.

  -----------------------------------------------------------------------
  Component               Dev Environment Minimum Production Minimum
  ----------------------- ----------------------- -----------------------
  CPU                     8 CPU cores             16 CPU cores

  Memory                  16 GB RAM               32 GB RAM

  Storage                 100 GB                  100 GB
  -----------------------------------------------------------------------

**Operating system requirements**

You can deploy a Cortex XSIAM engine on the following operating systems:

+-----------------------------------+-----------------------------------+
| Operating System                  | Supported Versions                |
+===================================+===================================+
| Ubuntu                            | 18.04, 20.04, 22.04               |
+-----------------------------------+-----------------------------------+
| RHEL                              | 8.x, 9.x                          |
|                                   |                                   |
|                                   | Includes all minor versions.      |
+-----------------------------------+-----------------------------------+
| Oracle Linux                      | 7.x, 8.9, 9.3, 9.4                |
+-----------------------------------+-----------------------------------+
| Amazon Linux                      | 2, Amazon Linux 2023              |
+-----------------------------------+-----------------------------------+
| Rocky Linux                       | 9.5                               |
+-----------------------------------+-----------------------------------+

> **Note**
>
> CentOS 8.x reached End of Life (EOL) on December 31, 2021, and is no
> longer supported as an operating system.
>
> CentOS 7.x reached End of Life (EOL) on June 30, 2024, and is no
> longer supported as an operating system.

**Engine required URLs**

You need to allow the following in the URLs for Cortex XSIAM engines to
operate properly. The URLs are needed to pull container images from
public Docker registries.

The endpoint URL
is: `wss://api-<tenant domain>.xdr.<region>.paloaltonetworks.com/xsoar/d1ws`.
For example,
`wss://api-my-tenant.xdr.us.paloaltonetworks.com/xsoar/d1ws`

+-----------------+--------------------------------------------+----------------------+-----------------+
| FUNCTION        | SERVICE                                    | PORT                 | DIRECTION       |
+=================+============================================+======================+=================+
| Integrations    |                                            | Integration-specific | Outbound        |
|                 |                                            | ports                |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+
| Engine          | HTTPS                                      | 443 (configurable)   | Outbound        |
| connectivity    |                                            |                      |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+
| Docker          | - https://registry-1.docker.io             | 443                  | Outbound        |
|                 |                                            |                      |                 |
|                 | - https://registry.fedoraproject.org       |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://registry.access.redhat.com       |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://docker.io                        |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://registry.docker.io               |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://auth.docker.io                   |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - This URL may change at Docker's          |                      |                 |
|                 |   discretion.                              |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://production.cloudflare.docker.com |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - This URL may change at Docker's          |                      |                 |
|                 |   discretion.                              |                      |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+

##### Install an engine

When you install the engine, the `d1.conf` is installed on the engine
machine, which contains engine properties such as proxy, log level, and
log files. If Docker/Podman is already installed, the
`python.engine.docker` and `powershell.engine.docker` keys are set to
`true`. If Docker or Podman is not available when the engine is
installed, the key is set to `false`. If so, you need to set the key to
`true` after installing Docker and Podman. Verify that
`python.engine.docker` and `powershell.engine.docker` configuration keys
are present in the `d1.conf` file.

> **Note**
>
> If you are using DEB, RPM, or Zip installation, install Docker or
> Podman.
>
> Natively running Python or PowerShell integrations/scripts on Windows
> or Linux is not supported on Cortex XSIAM engines.

###### Installation types

Cortex XSIAM supports the following file types for installation on the
engine machine:

- **Shell:** For all Linux deployments, including Ubuntu and SUSE.
  Automatically installs Docker/Podman, downloads Docker/Podman images,
  enables remote engine upgrade, and allows installation of multiple
  engines on the same machine.

<!-- -->

- The installation file is selected for you. Shell installation supports
  the purge flag, which by default is false. To uninstall an engine, run
  the installer with the purge flag enabled.

  > **Note**

  > When upgrading an engine that was installed using the Shell
  > installation, you can use the **Upgrade Engine** feature in the
  > **Engines** page. For Amazon Linux 2 type engines, you need to
  > upgrade these engine types using a zip-type engine and not use the
  > **Upgrade Engine** feature.

  > If you use the shell installer, Docker/Podman is automatically
  > installed. We recommend using Linux and not Windows to be able to
  > use the shell installer, which installs all dependencies.

<!-- -->

- **DEB:** For Ubuntu operating systems.

- **RPM:** RHEL operating systems.

<!-- -->

- > **Note**

  > Use DEB and RPM installation when the shell installation is not
  > available. You need to manually install
  > [Docker](#UUIDc2a4633cc8904adf2a1322b040573124) or
  > [Podman](#UUIDe52020e8425c72ad475a16b5073ca96c) and any
  > dependencies.

<!-- -->

- **Zip:** Used for Amazon Linux 2 machines.

- **Configuration:** Configuration file for download. When you install
  one of the other options, this configuration file (`d1.conf` ) is
  installed on the engine machine.

> **Important**
>
> For DEB/RPM engines, Python (including 3.x) and the containerization
> platform (Docker/Podman) must be installed and configured. For Docker
> or Podman to work correctly on an engine, [IPv4
> forwarding](https://docs.docker.com/network/bridge/#enable-forwarding-from-docker-containers-to-the-outside-world)
> must be enabled.

###### How to install an engine

1.  Create an engine.

    a.  Select Settings \> Configurations \> Data Broker \> Engines \>
        Create New Engine.

    b.  In the **Engine Name** field, add a meaningful name for the
        engine.

    c.  Select one of the installer types from the list.

    d.  (*Optional*) (*Shell only*) Select the checkbox to enable
        multiple engines to run on the same machine.

    - If you have an existing engine, and you did not select the
      checkbox, and now you want to install another engine on the same
      machine, you need to delete the existing engine.

    e.  (*Optional*) Add any required configuration in JSON format.

    f.  Click **OK** to create the engine.

2.  For shell installation, do the following:

- > **Tip**

  > For Linux systems, we recommend using the shell installer. If using
  > Amazon Linux 2, use the zip installer (see step
  > [4](#N1716185281356)).

  a.  Move the `.sh` file to the engine machine using a tool such as SSH
      or PuTTY.

  b.  On the engine machine, grant execution permission by running the
      following command:

  - `chmod +x /<engine-file-path>`

  c.  Install the engine by typing one of the following commands:

  - With tools: `sudo <engine-file-path>`

    Without tools: `sudo <engine-file-path> -- -tools=false`

    > **Note**

    > If you receive a `permissions denied` error, it is likely that you
    > do not have permission to access the `/tmp` directory.

    > If the installer fails to start due to a permissions issue, even
    > if running as root, add one of the following two arguments when
    > running the installer:

    - > `--target <path>` - Extracts the installer files into the
      > specified custom path.

    - > `--keep` - Extracts the installer files into the current working
      > directory (without cleaning at the end).

    > If using installer options such as `-- -tools=false`, the option
    > should come after the `--target` or `--keep` arguments. For
    > example:

    > `sudo ./d1-installer.sh --target /some/temp/dir -- -tools=false`

    > If you set a custom path when you run the installer, you must also
    > set a custom path for upgrading your engine or the upgrade will
    > fail. For more information, see
    > [/document/preview/1199417#UUID-3a9e655c-6f7e-2566-d416-29991d7d1d3b](/document/preview/1199417#UUID-3a9e655c-6f7e-2566-d416-29991d7d1d3b).

3.  For RPM/DEB installation, do the following:

    a.  Move the file to the required machine using a tool such as SSH
        or PuTTY.

    b.  Type one of the following installation commands:

  -------------------------------------------------------------------------------
  Machine Type                        Install Command
  ----------------------------------- -------------------------------------------
  RHEL (RPM)                          `sudo rpm -Uvh d1-2.5_15418-1.x86_64.rpm`

  Ubuntu (DEB)                        `sudo dpkg --install d1_xxx_amd64.deb`
  -------------------------------------------------------------------------------

c.  Start the engine by running one of the following commands:

  -----------------------------------------------------------------------
  Machine Type                        Start Command
  ----------------------------------- -----------------------------------
  RHEL (RPM)                          `sudo systemctl start d1`

  Ubuntu (DEB)                        `sudo service d1 restart`
  -----------------------------------------------------------------------

4.  For Zip installation on Amazon Linux 2, run the following commands:

    a.  Create the engine folder.

    - `mkdir /usr/local/demisto`

    b.  Unzip the engine files to the folder created in the previous
        step.

    - `unzip ./d1.zip -d /usr/local/demisto`

    c.  Allow the process to bind to low-numbered ports.

    - `setcap CAP_NET_BIND_SERVICE=+eip /usr/local/demisto/d1_linux_amd64`

    d.  Change the owner of `/usr/local/demisto` to the demisto user.

    - `chown -R demisto:demisto /usr/local/demisto`

    e.  In `/etc/systemd/system` edit the `d1.service` file as follows
        (adjust the directory and the name of the binary file if
        needed).

    -  [Unit]
          Description=Demisto Engine Service
          After=network.target
          [Service]
          Type=simple
          User=demisto
          WorkingDirectory=/usr/local/demisto
          ExecStart=/usr/local/demisto/d1_linux_amd64
          EnvironmentFile=/etc/environment
          Restart=always
          [Install]
          WantedBy=multi-user.target

    f.  Run the following commands:

    - `chown root:root /etc/systemd/system/d1.service`

      `chmod 644 /etc/systemd/system/d1.service`

    g.  Run the engine process.

    - `systemctl start d1`

    h.  Verify that the engine is running.

    - `systemctl status d1`

5.  Verify that the engine you created is connected.

    a.  Select Settings \> Configurations \> Data Broker \> Engines.

    b.  Locate your engine on the **Engines** page and check that it is
        connected.

6.  When the engine is connected, you can add the engine to a
    load-balancing group by clicking **Load-Balancing Group** on the
    Engines page.

- If you want to add the engine to a new group, click
  **Add to new group** from the list.

  When the engine is in the load-balancing group, it cannot be used as
  an individual engine and does not appear when configuring an engine
  from the list.

7.  (Optional) After installing the engine, you may want to set up a
    proxy, set up Docker hardening, configure the number of workers for
    the engine, or perform other related engine configurations. For more
    information, see [Configure
    Engines](#UUIDea7bc684741f4281cb5dab7fed8d5acb). You can also
    configure an integration instance to run on the engine you created.

#### Set up Cloud Identity Engine

The Cloud Identity Engine provides both user identification and user
authentication for a centralized cloud-based solution in on-premise,
cloud-based, or hybrid network environments. The Cloud Identity Engine
allows you to write security policy based on users and groups, not IP
addresses, and helps secure your assets by enforcing behavior-based
security actions. It also provides the flexibility to adapt to changing
security needs and users by making it simpler to configure an identity
source or provider in a single unified source of user identity, allowing
scalability as needs change. By continually syncing the information from
your directories, whether they are on-premise, cloud-based, or hybrid,
ensures that your user information is accurate and up to date and policy
enforcement continues based on the mappings even if the cloud identity
provider is temporarily unavailable.

To provide user, group, and computer information for policy or event
context, Palo Alto Networks cloud-based applications and services need
access to your directory information. The Cloud Identity Engine, a
secure cloud-based infrastructure, provides Palo Alto Networks apps and
services with read-only access to your directory information for user
visibility and policy enforcement. The components of the Cloud Identity
Engine deployment vary based on whether the Cloud Identity Engine is
accessing an on-premises directory (such as Active Directory) or a
cloud-based directory (such as Azure Active Directory).

The authentication component of the Cloud Identity Engine allows you to
configure a profile for a SAML 2.0-based identity provider (IdP) that
authenticates users by redirecting their access requests through the IdP
before granting access. You can also configure a client certificate for
user authentication. When you configure an Authentication policy and the
Authentication Portal on the Palo Alto Networks firewall, users must log
in with their credentials before they can access the resource.

##### Guidelines for using Cloud Identity Engine with Cortex XSIAM

Keep in mind the following guidelines:

- Cloud Identity Engine is an optional service.

- Cloud Identity Engine must be activated in the same region as Cortex
  XSIAM.

- You can use Active Directory information in policy configuration and
  endpoint management.

- Cortex XSIAM supports on-premises Active Directory and Microsoft
  Entra.

- You can use XQL Query to query the data using
  the `pan_dss_raw` dataset.

##### Activate Cloud Identity Engine

Activating a Cloud Identity Engine instance on your  Cortex
XSIAM account will allow you to pair your Cortex XSIAM tenant with the
Active Directory information collected by the Cloud Identity Engine
instance. Follow the instructions
[here](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine).

##### Configure Cortex XSIAM with Cloud Identity Engine

After you complete the activation steps, wait about ten minutes and do
the following:

1.  Log in to Cortex XSIAM.

2.  Select Settings \> Configuration \> Integrations \> Cloud Identity
    Engine.

3.  In the **Add Cloud Identity Engine** dialog box, select the instance
    name and click **Save**.

##### Risk sharing between Cortex XSIAM and the Cloud Identity Engine

Integrate Cortex XSIAM with the Cloud Identity Engine (CIE) to enable
dynamic user grouping and access control based on real-time risk
assessments. This integration leverages historical events and alerts
from Cortex XSIAM to continuously evaluate user and host risk,
synchronizing the insights with CIE to support adaptive policy
enforcement. When an Okta tenant with an Identity Threat Protection
(ITP) license is available, CIE can be connected to Okta to create and
apply adaptive policies directly within the Okta environment, based on
Cortex Risky users sharing, ensuring responsive and risk-based identity
management.

Before you activate the integration, you must complete the onboarding in
the Cloud Identity Engine.

1.  Configure Cortex XSIAM with Cloud Identity Engine. For more
    information, see [Configure Cortex XSIAM with Cloud Identity
    Engine.](#X0494657482bfa15f244d96bf24566d8499a5693)

2.  In the Cloud Identity Engine, onboard the relevant directories,
    Active Directory, Entra ID, or Okta. For more information, see
    [Choose Your Directory
    Type](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/choose-directory-type).

3.  In Cortex XSIAM, go to Settings \> Configuration \> Integrations \>
    Cloud Identity Engine and select
    **Activate risk signal sharing to CIE**.

- > **Note**

  > The **Activate risk signal sharing to CIE** checkbox is available
  > only after the second step is completed.

### Define data sources

Onboard cloud and on-prem data sources and integrations. To get you up
and running in Cortex XSIAM, you can start ingesting data and logs from
multiple products to assist your investigation and to secure your cloud
and on-prem infrastructure. On the **Data Sources** page (Settings \>
Data Sources) you can view and add data sources to suit your security
use cases. For more information about how to add data sources, see [Add
a new data source or instance](#UUID4f226047ebe62516a23316de720884c4).

On the **Data Sources** page, you can ingest the following data and
logs:

+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Data Source           | Description                                          | See More                                             |
+=======================+======================================================+======================================================+
| Ingest data from      | In Cortex XSIAM content includes many items such as  | [Cortex XSIAM                                        |
| third-party products  | playbooks, scripts, integrations, correlation rules, | content](#UUID2961ef824f3d0cfcc4bf3ccd4f7e7242)      |
|                       | and data model rules. Content is organized into      |                                                      |
|                       | content packs to support specific security           |                                                      |
|                       | orchestration use cases. In **Marketplace**, you can |                                                      |
|                       | download, install, manage, and contribute content    |                                                      |
|                       | packs. For example, the Microsoft Exchange Online    |                                                      |
|                       | content pack includes scripts, integrations, and     |                                                      |
|                       | playbooks. After downloading the content pack you    |                                                      |
|                       | need to configure the integration on the             |                                                      |
|                       | **Automation & Feed Integrations** page to enable    |                                                      |
|                       | Cortex XSIAM to communicate with the Exchange        |                                                      |
|                       | server.                                              |                                                      |
|                       |                                                      |                                                      |
|                       | However, to simplify the onboarding process, on the  |                                                      |
|                       | **Data Sources** page, you can add a data source.    |                                                      |
|                       | The Data Onboarder wizard guides you through the     |                                                      |
|                       | steps for installing the integration instance and    |                                                      |
|                       | enables you to configure your integration. Cortex    |                                                      |
|                       | XSIAM automatically downloads and installs the       |                                                      |
|                       | required Marketplace content packs for the           |                                                      |
|                       | integration, and recommends additional beneficial    |                                                      |
|                       | content such as playbooks and dashboards that are    |                                                      |
|                       | relevant for the specific data source.               |                                                      |
|                       |                                                      |                                                      |
|                       | > **Note**                                           |                                                      |
|                       | >                                                    |                                                      |
|                       | > Not all content packs are available to download on |                                                      |
|                       | > the **Data Sources** page. If you require content  |                                                      |
|                       | > packs such as Phishing, and Malware, you need to   |                                                      |
|                       | > download the pack from Marketplace and configure   |                                                      |
|                       | > the integration. The Data Sources page is designed |                                                      |
|                       | > for third-party integrations to help you onboard.  |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest data from PANW | Cortex XSIAM supports streaming data directly from   | [Palo Alto Network                                   |
| products              | Prisma Access accounts, Next-Generation Firewalls    | integrations](#UUIDe6caf56b093b361f19a4fd274c6c66c2) |
|                       | (NGFW), and Panorama devices to your tenants using   |                                                      |
|                       | the Strata Logging Service.                          |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest network        | Ingest network connection logs from different        | [Ingest network connection                           |
| connection logs       | third-party sources, such as Amazon S3.              | logs](#UUID58b3a39027d805fe448438e253ea5cdd)         |
|                       |                                                      |                                                      |
|                       | > **Note**                                           |                                                      |
|                       | >                                                    |                                                      |
|                       | > For some vendors, to receive data from an external |                                                      |
|                       | > source, you must first set up the Syslog Collector |                                                      |
|                       | > applet on a Broker VM within your network. For     |                                                      |
|                       | > more information, see [Activate Syslog             |                                                      |
|                       | > Collector](#UUIDd7d85d4a97df7ec2a052d22376f5a52e). |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest authentication | Ingest authentication logs and data from an external | [Ingest authentication logs and                      |
| logs and data         | source, such as AWS Cloud Trail.  Cortex XSIAM can   | data](#UUID7853a2834a958ab66d72ea4b251ead68)         |
|                       | place that information into authentication stories.  |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest cloud assets   | Ingest cloud assets from third-party sources. In     | [Ingest cloud                                        |
|                       | addition to automation and core analytics, activate  | assets](#UUIDd0ef91c2f98d2b5fbd7108a453bb69fb)       |
|                       | cloud posture security and cloud runtime security.   |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest operation and  | Ingest operation and system logs from supported      | [Ingest operation and system logs from cloud         |
| system logs from      | cloud providers, such as Amazon Cloud Watch.         | providers](#UUIDabaa5d3af4f5461b091c010a03df4a7a)    |
| cloud providers       |                                                      |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+
| Ingest custom log     | Cortex XSIAM supports several custom log ingestion   | [Additional log ingestion                            |
| methods               | methods, such as ingesting Apache Kafka events as    | methods](#UUID9525ed82d2e059ac6a4bcf055532def4)      |
|                       | datasets. You need to activate the Syslog collect    |                                                      |
|                       | applet on a Broker VM within your network to receive |                                                      |
|                       | logs.                                                |                                                      |
+-----------------------+------------------------------------------------------+------------------------------------------------------+

#### Cortex XSIAM content

In Cortex XSIAM, content includes individual content entities that you
create such as individual playbooks and issue fields, preinstalled
content packs, and content packs that you download from Marketplace.

Content in Marketplace is organized into content packs to support
specific security orchestration use cases. Content packs are created by
Palo Alto Networks, technology partners, contributors, and customers.

You can view Marketplace content packs from within Cortex XSIAM or at
<https://cortex.marketplace.pan.dev/marketplace/>.

In Cortex XSIAM, content includes the following:

+-----------------------------------+-----------------------------------+
| Content                           | Description                       |
+===================================+===================================+
| Issue types and fields            | All issues that are ingested into |
|                                   | Cortex XSIAM are assigned an      |
|                                   | issue type when they are          |
|                                   | classified. After you classify    |
|                                   | the issue, you can then map the   |
|                                   | relevant fields to the issue.     |
|                                   |                                   |
|                                   | Issue types contain fields that   |
|                                   | are relevant to the issue type.   |
+-----------------------------------+-----------------------------------+
| Classifiers                       | Classification determines the     |
|                                   | type of issue/indicator that is   |
|                                   | created for events ingested from  |
|                                   | a specific integration. You       |
|                                   | create a classifier and define    |
|                                   | that classifier in an             |
|                                   | integration. Mappers map the      |
|                                   | fields from your third-party      |
|                                   | integration to the fields in your |
|                                   | issue/indicator layouts.          |
+-----------------------------------+-----------------------------------+
| Correlation Rules                 | Analyzes correlation of           |
|                                   | multi-event from multiple sources |
|                                   | by using the Cortex XSIAM         |
|                                   | XQL-based engine for creating     |
|                                   | these correlations (scheduled)    |
|                                   | rules. Issues can then be         |
|                                   | triggered based on these rules    |
|                                   | with a defined time frame and     |
|                                   | schedule.                         |
+-----------------------------------+-----------------------------------+
| Dashboards                        | Dashboards consist of visualized  |
|                                   | data powered by fully             |
|                                   | customizable widgets, which       |
|                                   | enables you to analyze data from  |
|                                   | inside or outside Cortex XSIAM,   |
|                                   | in different formats such as line |
|                                   | charts, tables, text, etc.        |
+-----------------------------------+-----------------------------------+
| Data Model Rules                  | Data Model rules enable you to    |
|                                   | normalize logs for out-of-the-box |
|                                   | analytics and data enrichment.    |
|                                   | This allows you to do the         |
|                                   | following:                        |
|                                   |                                   |
|                                   | - Map 3rd party data to a         |
|                                   |   consolidated schema with        |
|                                   |   predefined data types.          |
|                                   |                                   |
|                                   | - Enjoy auto-complete and mapping |
|                                   |   suggestions.                    |
|                                   |                                   |
|                                   | - Map multiple datasets to one    |
|                                   |   Data Model.                     |
|                                   |                                   |
|                                   | Some content packs contain        |
|                                   | out-of-the-box default Data Model |
|                                   | Rules.                            |
+-----------------------------------+-----------------------------------+
| Indicator types and fields        | Indicators are categorized by     |
|                                   | indicator type, which determines  |
|                                   | the indicator layout and fields   |
|                                   | that are displayed and which      |
|                                   | scripts are run on indicators of  |
|                                   | that type.                        |
+-----------------------------------+-----------------------------------+
| Integrations                      | You can define the following      |
|                                   | integrations:                     |
|                                   |                                   |
|                                   | - (SOAR) Automation: Add your     |
|                                   |   3rd-party security and alert    |
|                                   |   management vendors, which can   |
|                                   |   then trigger events from these  |
|                                   |   integrations that become issues |
|                                   |   in Cortex XSIAM. Once the       |
|                                   |   issues are created, you can run |
|                                   |   playbooks on these issues to    |
|                                   |   enrich them with information    |
|                                   |   from other products in your     |
|                                   |   system, which helps you         |
|                                   |   complete the picture.           |
|                                   |                                   |
|                                   | - Collection (SIEM): Add          |
|                                   |   integrations that collect raw   |
|                                   |   events, such as logs. These     |
|                                   |   integrations are separate from  |
|                                   |   automation integrations so that |
|                                   |   you can add a collection        |
|                                   |   integration that requires read  |
|                                   |   permissions without having to   |
|                                   |   add automation (read and write  |
|                                   |   permissions).                   |
+-----------------------------------+-----------------------------------+
| Layouts and layout rules          | Enables you to add rules, which   |
|                                   | define the layout of issues and   |
|                                   | notifications,                    |
|                                   |                                   |
|                                   | When installed, the layout rules  |
|                                   | are enabled and added as Default  |
|                                   | Rules. When deleted, all related  |
|                                   | layout rules (including all Rule  |
|                                   | sections) are removed from the    |
|                                   | Default Rules tab.                |
+-----------------------------------+-----------------------------------+
| Parsing rules                     | Enables you to add rules, which   |
|                                   | remove non-required data for      |
|                                   | analytics, hunting, or            |
|                                   | regulation, reduce data storage   |
|                                   | costs, pre-process all incoming   |
|                                   | data, etc.                        |
|                                   |                                   |
|                                   | When installed, the parsing rules |
|                                   | are enabled and added as Default  |
|                                   | Rules. When deleted, all related  |
|                                   | parsing rules (including all Rule |
|                                   | sections) are removed from the    |
|                                   | Default Rules tab.                |
+-----------------------------------+-----------------------------------+
| Playbooks                         | You can automate many security    |
|                                   | processes, including handling     |
|                                   | investigations and managing       |
|                                   | tickets and security responses    |
|                                   | that were previously handled      |
|                                   | manually. When an issue is        |
|                                   | ingested, the playbook runs and   |
|                                   | an issue is created.              |
+-----------------------------------+-----------------------------------+
| Reports                           | Reports contain statistical data  |
|                                   | in the form of widgets (from a    |
|                                   | dashboard), which enable you to   |
|                                   | analyze data from inside or       |
|                                   | outside Cortex XSIAM, in          |
|                                   | different formats such as line    |
|                                   | charts, tables, text from         |
|                                   | information, etc.                 |
+-----------------------------------+-----------------------------------+
| Scripts                           | Perform specific actions and are  |
|                                   | comprised of commands, which are  |
|                                   | used in playbook tasks and when   |
|                                   | running commands in the issue War |
|                                   | Room.                             |
+-----------------------------------+-----------------------------------+

##### Cortex Marketplace

Marketplace enables you to:

- **Leverage content from the largest SOAR community:** Continuously
  extend Cortex XSIAM with proven use cases contributed by SecOps users
  and SOAR partners.

- **Discover top-rated, validated content:** Identify the content
  offerings recommended by your peers and validated by the world's
  leading cybersecurity company. Discover how to increase automation
  with the tools that you already have.

- **Solve your toughest security use cases:** Deploy turnkey security
  workflows that span integrations, playbooks, dashboard layouts, and
  reports with a single click.

Marketplace enables you to build a strong community with other security
professionals by exchanging content. You can explore the latest trends
from Cortex XSIAM and other contributors and test drive use cases all
within your Cortex XSIAM platform.

Cortex XSIAM supports free content packs, which are either Cortex XSIAM
or partner-supported content packs. You can restrict a user role from
managing content packs in Marketplace when defining/editing user roles.

In Marketplace, you can browse all content packs (including installed
content) or view only installed content packs.

You can search for content packs by entering text in the search bar and
selecting the relevant content pack from the search results.

You can sort content packs by latest update, best match, recommended,
number of downloads, and filter according to the following criteria:

- **Use cases:** Filter according to high-level use cases, such as
  Phishing, Malware, Ransomware, and Access.

- **Integrations:** Filter according to the integration included in the
  content pack.

- **Categories:** Filter according to content pack categories, such as
  Messaging, and Forensics & Malware Analysis

- **Published:** Filter according to whether published by Cortex XSIAM
  or by Cortex XSIAM technology partners.

- **Content Pack Includes:** Filter according to the content of the
  content pack, such as scripts, Integrations, and Playbooks.

- **Tags:** Filter according to tags, such as Issues, Network, and
  Security.

- **Types:** Filter according to Collection or TIM.

When clicking a content pack you can view detailed information including
content that it installs (such as scripts and playbooks, and indicator
fields), dependencies (what content packs are required or optional) and
version history (including whether you want to roll back to earlier
versions).

You can view Marketplace content packs from within Cortex XSIAM or at
<https://cortex.marketplace.pan.dev/marketplace/>.

##### Content packs

Cortex XSIAM content in Marketplace is organized in packs. Content packs
are created by Palo Alto Networks, technology partners, consulting
companies, MSSPs, customers, and individual contributors. Content packs
may include a variety of different components, such as integrations,
scripts, playbooks, and widgets, grouped together to address a specific
use case. Content packs are free and can be used by all customers.

You can view Marketplace content packs from within Cortex XSIAM or at
<https://cortex.marketplace.pan.dev/marketplace/>.

**Pre-installed content packs**

Cortex XSIAM comes with a number of pre-installed content packs that
cover many common uses cases. Pre-installed content packs include, but
are not limited to:

- [Common
  Scripts](https://cortex.marketplace.pan.dev/marketplace/details/CommonScripts/),
  [Common
  Widgets](https://cortex.marketplace.pan.dev/marketplace/details/CommonWidgets/),
  [Common
  Playbooks](https://cortex.marketplace.pan.dev/marketplace/details/CommonPlaybooks/),
  [Common
  Types](https://cortex.marketplace.pan.dev/marketplace/details/CommonTypes/),
  [Common
  Reports](https://cortex.marketplace.pan.dev/marketplace/details/CommonReports/),
  [Common
  Dashboards](https://cortex.marketplace.pan.dev/marketplace/details/CommonDashboards/)

<!-- -->

- These content packs provide important tools and building blocks you
  can use to customize your playbooks and workflows in Cortex XSIAM. The
  Common Scripts content pack, for example, includes scripts that
  convert file formats, fetch indicators from a file, export context
  data, send emails, and more.

<!-- -->

- [VirusTotal](https://cortex.marketplace.pan.dev/marketplace/details/VirusTotal/)

<!-- -->

- Provides integration with the popular Virus Total service to analyze
  suspicious files, domains, IPs and URLs to detect malware and other
  security breaches.

**Recommended content packs**

In addition, we recommend reviewing if you require the following popular
content packs:

![](media/rId371.png){width="5.833333333333333in"
height="2.9458333333333333in"}

- [Phishing](https://cortex.marketplace.pan.dev/marketplace/details/Phishing/)

<!-- -->

- Create and respond to phishing issues based on user reports.

<!-- -->

- [Cortex XDR by Palo Alto
  Networks](https://cortex.marketplace.pan.dev/marketplace/details/CortexXDR/)

<!-- -->

- Automate Cortex XDR incident response. Includes custom Cortex XDR
  incident views and layouts to aid analyst investigations.

<!-- -->

- [Atlassian
  Jira](https://cortex.marketplace.pan.dev/marketplace/details/Jira/)

<!-- -->

- Manage Jira tickets directly from Cortex XSIAM, enrich them with
  Cortex XSIAM data, and mirror information between Jira tickets and
  Cortex issues.

<!-- -->

- [ServiceNow](https://cortex.marketplace.pan.dev/marketplace/details/ServiceNow/)

<!-- -->

- Manage ServiceNow tickets directly from the Cortex XSIAM and enrich
  them with Cortex XSIAM data, and mirror information between ServiceNow
  tickets and Cortex issues.

<!-- -->

- [PAN-OS by Palo Alto
  Networks](https://cortex.marketplace.pan.dev/marketplace/details/PANOS/)

<!-- -->

- Manage Palo Alto Networks Firewall and Panorama, from Cortex XSIAM.

<!-- -->

- A collaboration integration, such as [Microsoft
  Teams](https://cortex.marketplace.pan.dev/marketplace/details/MicrosoftTeams/)
  or
  [Slack](https://cortex.marketplace.pan.dev/marketplace/details/Slack/)
  to send messages and notifications to your team.

> **Note**
>
> Cortex XSIAM includes a built-in default mail sender. You also have
> the option of installing a different mail sender content pack, such as
> [Microsoft Exchange
> Online](https://cortex.marketplace.pan.dev/marketplace/details/MicrosoftExchangeOnline/).

##### Install content packs

You can only install one content pack at a time. Cortex
XSIAM automatically adds any content that is required to install the
content pack. You can also add any optional content packs that use the
content pack you want to install.

If you receive an error message when you try to install a content pack,
you need to fix the error before installing. If a warning message is
issued, you can still download the content pack, but you should fix the
problem; otherwise, the content may not work correctly.

Before you install a content pack you should review the content pack to
see what it includes and what are the various dependencies. Following is
the information you can view:

- **Details:** General information about the content pack such as
  installation, content, version, author, and status.

- **Content:** The content to be installed, such as scripts or
  integrations.

- **Dependencies:** Details of any required content packs and optional
  content packs that may need to be installed with your content pack.

- **Version History:** View the currently installed version, earlier
  versions, available updates, and revert if required.

If you want to install data sources you can do one the following:

- Go to the Data Sources page and add a data source by configuring an
  integration in the Data Sources page. Once configured, it
  automatically installs the required content packs, and recommends
  additional beneficial content such as playbooks and dashboards that
  are relevant for this specific data source.

- In Marketplace, select either Data Onboarder (which takes you to the
  integration configuration in the Data Sources page) or install the
  content pack directly from Marketplace. If installing the content pack
  from Marketplace, you will then have to configure the integration in
  the Automation &amp; Feed Integrations page.

> **Note**
>
> Currently, not all content packs are supported in the Data Sources
> page. For example, content packs with several integrations are not yet
> supported.

**How to install a content pack in Marketplace**

1.  Go to Marketplace \> Browse and locate the content pack you want to
    install.

2.  Click the required content pack and review the contents.

3.  Click **Install** to add the content pack to the **Cart**.

4.  (*Optional*) If the content pack includes optional content, select
    the content packs you want to add.

- The **Cart** displays the number of items you are installing,
  including any required content packs. You can log in and out, but the
  content packs remain in the **Cart** until you click either
  **Empty cart** or **Install**.

5.  Click **Install**.

6.  After installation, click **Refresh content**.

- You can now start configuring your content. If you have installed an
  integration, configure the integration including setting up an
  integration instance. For more information, see
  [/document/preview/910079#UUID-1026535e-8863-159e-1fd9-d0eb5f5fec42](/document/preview/910079#UUID-1026535e-8863-159e-1fd9-d0eb5f5fec42).

> **Note**
>
> Content packs are also automatically installed when you adopt
> playbooks and configure tasks.

##### Automation and feed integrations

Integrations are mechanisms through which Cortex XSIAM connects and
communicates with other products. These integrations can be executed
through REST APIs, webhooks, and other techniques. Integrations enable
you to orchestrate and automate SOC operations.

**Integrations installed from a content pack**

Integrations are included in content packs, which you download and
install from Marketplace. After you download and install a content pack
that includes an integration, you need to configure the integration by
adding an instance. You can have multiple instances of an integration,
for example, to connect to different environments. Additionally, if you
are an MSSP and have multiple tenants, you could configure a separate
instance for each tenant.

> **Note**

- > Some integrations can be downloaded directly without having to
  > initially download a content pack from Marketplace. For more
  > information, see [Define data
  > sources](#UUID00d964f3e91bf4f6d19a763269659fad).

- > In addition to content packs that you install from Marketplace,
  > related content packs are automatically downloaded when you adopt
  > playbooks or edit tasks that require content items such as scripts
  > or integrations.

Cortex XSIAM comes out-of-the-box with integrations to help you onboard,
such as:

- Mail Sender

<!-- -->

- Sends email notifications to users.

<!-- -->

- Generic Export Indicators Service

<!-- -->

- Provides an endpoint with a list of indicators as a service for the
  system indicators. For more information about how to set up the
  integration, see [Export indicators using the Generic Export
  Indicators Integration](#X1ed0d74913567e4ac43b9680ff39f339651f584).

<!-- -->

- Palo Alto Networks WildFire Reports

<!-- -->

- Generates a Palo Alto Networks WildFire PDF report. For more
  information, see [Palo Alto Networks WildFire
  Reports](https://xsoar.pan.dev/docs/reference/integrations/wild-fire-reports).

<!-- -->

- Rasterize

<!-- -->

- Converts URLs, PDF files, and emails to an image file or PDF file. For
  more information, see
  [Rasterize](https://xsoar.pan.dev/docs/reference/integrations/rasterize).

**Create an integration**

You can create an integration, by adding parameters, commands,
arguments, and outputs as well as writing the necessary integration
code. You should have a working Cortex XSIAM tenant and programming
experience with Python.

To create an integration, on the **Automation and feed integrations**
page, click **BYOI**.

![](media/rId387.png){width="5.833333333333333in"
height="0.5614577865266842in"}

The Cortex XSIAM IDE and the **HelloWorld** integration template are
loaded by default. For more information about how to create an
integration, including an example, see [Create an
Integration](https://xsoar.pan.dev/docs/tutorials/tut-integration-ui).

**Configure an integration**

On the **Automation and feed integrations** page, after you have either
downloaded the integration or created an integration, you can do the
following:

+-----------------------------------+------------------------------------------------------------------------+
| Option                            | Description                                                            |
+===================================+========================================================================+
| Add instance                      | Configure an integration instance to connect and communicate with      |
|                                   | other products. For more information, see [Add an integration          |
|                                   | instance](#UUIDd5353dd15235a4a7cf7a40eb66cc900e).                      |
|                                   |                                                                        |
|                                   | After configuring the instance, you can also enable/disable the        |
|                                   | integration instance, copy the instance, and view the integration      |
|                                   | fetch history.                                                         |
+-----------------------------------+------------------------------------------------------------------------+
| View integration\'s source        | View the integration settings and source code.                         |
+-----------------------------------+------------------------------------------------------------------------+
| Edit integration\'s source        | Edit the integration settings and source code. For more information    |
|                                   | about editing the integration\'s source code, see [Create an           |
|                                   | Integration](https://xsoar.pan.dev/docs/tutorials/tut-integration-ui). |
|                                   |                                                                        |
|                                   | > **Note**                                                             |
|                                   | >                                                                      |
|                                   | > If the integration was installed from a content pack, you need to    |
|                                   | > duplicate the integration before editing.                            |
+-----------------------------------+------------------------------------------------------------------------+
| Duplicate integration             | If you want to change the source code, and settings, or download the   |
|                                   | integration, you need to duplicate the integration.                    |
+-----------------------------------+------------------------------------------------------------------------+
| Delete                            | Although you can\'t delete an integration installed from a content     |
|                                   | pack (unless a duplicate), you can delete an integration instance.     |
+-----------------------------------+------------------------------------------------------------------------+
| Always / On Demand                | For each integration instance, you have the option of setting the      |
|                                   | instance to be used only **On Demand**, when it is specified with the  |
|                                   | `using` argument in a playbook or the CLI. By default, the settings is |
|                                   | **Always** and the integration instance is used whenever the           |
|                                   | integration is called.                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| Download the integration          | Download the integration in YAML format. You can also upload an        |
|                                   | integration.                                                           |
|                                   |                                                                        |
|                                   | > **Note**                                                             |
|                                   | >                                                                      |
|                                   | > If the integration was installed from a content pack, you need to    |
|                                   | > duplicate the integration before downloading.                        |
+-----------------------------------+------------------------------------------------------------------------+
| Version History                   | If the integration is a duplicate or you create your own integration,  |
|                                   | you can see the changes in the integration.                            |
+-----------------------------------+------------------------------------------------------------------------+

You can view all the integration changes (the last 100 changes) by
clicking the **Version History** button.

###### Using integration commands

The command line interface (CLI) enables you to run system commands,
integration commands, scripts, etc from the Cases War Room, Issues War
Room, or Playground CLI. The CLI auto-complete feature allows you to
find relevant commands, scripts, and arguments.

Cortex XSIAM uses the \"`!`\" such as
`!ad-create-user username=[name of user]`

Under each integration, you can view a list of commands.

> **Note**
>
> Integration commands are only available when the integration instance
> is enabled. Some commands depend on a successful connection
> between Cortex XSIAM and third-party integrations.

You can run the CLI commands in the Playground or in a case/issue War
Room. The Playground is a non-production environment where you can
safely develop and test automation scripts, APIs, commands, etc. It is
an investigation area that is not connected to a live (active)
investigation.

When running the command, the results are returned in the War Room or
Playground and also in a JSON format in Context Data.

> **Tip**
>
> In the Playground, you can clear the context data, if needed, which
> deletes everything in the Playground context data, but does not affect
> the actual issue or case. To clear the context, run
> `!DeleteContext all=yes'` from the CLI or
> click **Clear Context Data** while viewing the context data.

###### Manage API keys

API keys are used to manage and secure API interactions. An API key is
essentially a unique string of alphanumeric characters that acts as a
credential, allowing a specific user or application to access and
interact with a particular API. When you request data or perform an
action through an API call, you must include this API key in the header.
Cortex XSIAM then verifies the key\'s authenticity and, if valid, grants
the requested access.

####### How to create an API key

1.  Select Settings \> Configurations \> Integrations \> API Keys \> New
    Key.

2.  In the **Role** tab, perform for the following:

    a.  Under **Security Level**, select the type of API Key you want to
        generate: **Advanced** or **Standard**. The Advanced API key
        hashes the key using a nonce, a random string, and a timestamp
        to prevent replay attacks. cURL does not support this but it is
        suitable with scripts.

    b.  Under **Role**, select the desired level of access for this key.
        You can select from predefined roles or custom roles. Roles are
        available according to what was defined in either the Cortex
        Gateway or Cortex XSIAM Access Management. You can view the
        configuration of the role selected by expanding the sections
        under **Components**. For more information, see [Assign user
        roles and groups](#UUIDc0966cb32b3c88e214d33131de93fa8a).

    c.  (Optional) Under **Comment**, provide a comment that describes
        the purpose of the API key.

    d.  (Optional) If you want to define a time limit on the API key
        authentication, select **Enable Expiration Date**, and select
        the expiration date and time. You can track the expiration date
        of each API key in the **API Keys** page. In addition, Cortex
        XSIAM displays a API Key Expiration notification in the
        Notification Center one week and one day prior to the defined
        expiration date.

3.  (Optional) To configure and manage granular scoping for Scope-Based
    Access Control (SBAC), click the **Scope** tab, and under
    **Scope Definition**, expand the scoping areas that you want to
    grant the user role access to for this API by clicking the chevron
    icon (**\>**) beside the scoping area title. The following table
    explains the options available to configure:

- > **Important**

  > Before configuring, ensure that you review **Understand scoping** in
  > the [Manage user scope](#UUID071cdbb66c6a6afe3a671fa79991a0a8)
  > section.

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

4.  Click **Generate** to generate the API key.

5.  Copy the generated API key and click **Done**.

- > **Important**

  > You will not be able to view the API key again after you complete
  > this step. Ensure that you copy the API key before closing the
  > notification.

####### Actions available on API Keys

Below are some of the main pivot (right-click) options for actions
available on each API key listed in the API Keys table. Only tasks that
need further explanation are explained below.

  -------------------------------------------------------------------------
  Action                              Description
  ----------------------------------- -------------------------------------
  View Examples                       Copies the Python 3 example, so you
                                      can edit it to set up your own API
                                      calls.

  Copy text to clipboard / Copy       Copies the value of an API setting,
  entire row                          such as the ID, to the clipboard by
                                      right-clicking the setting and
                                      selecting **Copy text to clipboard**.
                                      You can copy all the settings of an
                                      API key by right-clicking and
                                      selecting **Copy entire row**.

  Filter API keys                     Filters the API keys by selecting one
                                      of the filter options, such as
                                      **Show rows 30 days prior to\...**.
                                      You can then adjust the filter
                                      options to filter the API keys
                                      according to all the available
                                      fields.
  -------------------------------------------------------------------------

###### Fetch issues from an integration instance

You can poll third-party integration instances for events and turn them
into Cortex XSIAM issues (fetching). Many integrations support fetching,
but not all support this feature. You can view each integration in the
[Developer Hub](https://xsoar.pan.dev/docs/reference/index).

When setting up an instance, you can configure the integration instance
to fetch events. You can also set the interval for which to fetch new
issues by configuring the **Issue Fetch Interval** field. The fetch
interval default is 1 minute. This enables you to control the interval
in which an integration instance reaches out to third-party platforms to
fetch issues into Cortex XSIAM.

> **Note**

- > In some integrations, the **Issue Fetch interval** is called
  > **Feed Fetch Interval**.

- > If the integration instance does not have the
  > **Issue Fetch Interval** field, you need to add this field by
  > editing the integration settings. If the integration is from a
  > content pack, you need to create a copy of the integration. Any
  > future updates to this integration will not be applied to the copy
  > integration.

- > If you turn off fetching for a while and then turn it on or disable
  > the instance and enable it, the instance remembers the last run and
  > pulls all events that occurred while it was off. If you don\'t want
  > this to happen, verify that the instance is enabled and
  > click **Reset the "last run" timestamp** when editing the instance.
  > Also, note that \"last run\" is retained when an instance is
  > renamed.

After configuring the instance, you may need to set up a correlation
rule to generate issues in Cortex XSIAM.

Correlation rules are predefined logic or patterns that Cortex XSIAM
uses to identify relationships between disparate events occurring across
an organization\'s IT environment. If the conditions specified in the
rule are met, Cortex XSIAM generates an issue.

**How to fetch issues**

1.  Go to Settings \> Configuration \> Data Collection \> Automation and
    Feed Integrations, find the integration, and click
    **+ Add instance**.

2.  In the integration\'s dialog box, select **Fetch issues**.

- After this setting is enabled, Cortex XSIAM searches for events that
  occurred within the time frame set for the integration, which is based
  on the specific integration. The default is 10 minutes, but it can be
  changed in the integration script.

3.  (*Optional*) In the **Issue Fetch Interval** field, set the interval
    of hours and minutes to fetch alerts (default 1 minute).

4.  (*Optional*) If the **Issue Fetch Interval** field does not appear,
    add it to the integration.

- Relevant for any issue fetching integration:

  a.  For integrations installed from a content pack, select the
      duplicate integration button.

  - If you have already duplicated the integration, click the Edit
    integration's source button.

  b.  In the **Basic** section, select the **Fetch issues** checkbox.

  - In the **Parameters** section, you can see that the
    `IssueFetchInterval` parameter is added. Change the default value if
    necessary.

  c.  Click **Save** to save the changes.

5.  To generate issues in Cortex XSIAM, add a correlation rule, as
    required.

- > **Note**

  > Some content packs include preconfigured correlation rules, but you
  > should review them to see if they suit your use case and duplicate
  > them if required. Go to Threat Management \> Detection Rules \>
  > Correlations, search for the relevant rule, right-click, and select
  > **Preview Rule**. For example, the
  > **ServiceNow v2 Alerts (automatically generated)** correlation rule
  > uses the following XQL Query:

      dataset = servicenow_v2_generic_alert_raw
      | filter _alert_data != null
      | alter alert_severity = json_extract_scalar(_alert_data, "$.severity")
      | alter alert_category = json_extract_scalar(_alert_data, "$.alert_category")
      | alter alert_name = json_extract_scalar(_alert_data, "$.alert_name")
      | alter alert_description = json_extract_scalar(_alert_data, "$.alert_description")

  > You may want to update the query by defining complex, multi-source
  > detection logic or add filters, such as alert severity or assignee.

###### Forward Requests to Long-Running Integrations

Some long-running integrations provide internal data via API calls to
your third-party software, such as a firewall. You can set up Cortex
XSIAM to allow third-party software to access long-running integrations
installed either on the Cortex XSIAM tenant or on an engine.

Long-running integrations provide internal data via API calls such as:

+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Integration           | Description                                      | See More                                                                                          |
+=======================+==================================================+===================================================================================================+
| O365 Teams (Using     | Get authorized access to a user\'s Teams app in  | [O365 Teams (Using Graph                                                                          |
| Graph API)            | a personal or organizational account.            | API)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-teams)                    |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Generic Webhook       | Creates cases on event triggers. The trigger can | [Generic Webhook](https://xsoar.pan.dev/docs/reference/integrations/generic-webhook)              |
|                       | be any query posted to the integration.          |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Generic Export        | Use the Generic Export Indicators Service        | [Generic Export Indicators](#UUID20234eeb7afffdf4985fa70052c0a876)                                |
| Indicators Service    | integration to provide an endpoint with a list   |                                                                                                   |
|                       | of indicators as a service for the system        |                                                                                                   |
|                       | indicators.                                      |                                                                                                   |
|                       |                                                  |                                                                                                   |
|                       | You can set up the tenant to export internal     |                                                                                                   |
|                       | data to an endpoint.                             |                                                                                                   |
|                       |                                                  |                                                                                                   |
|                       | > **Note**                                       |                                                                                                   |
|                       | >                                                |                                                                                                   |
|                       | > This integration replaces the External Dynamic |                                                                                                   |
|                       | > list integration, which is deprecated. For     |                                                                                                   |
|                       | > more information about how to set up the       |                                                                                                   |
|                       | > integration, see [Manage external dynamic      |                                                                                                   |
|                       | > lists](#UUID35fa653f80ceb4d7218a0b086bf8a454). |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Microsoft Teams       | Send messages and notifications to team members. | [Microsoft Teams](https://xsoar.pan.dev/docs/reference/integrations/microsoft-teams)              |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| TAXII Server          | Provides TAXII Services for system indicators    | [TAXII Server](https://xsoar.pan.dev/docs/reference/integrations/taxii-server)                    |
|                       | (Outbound feed).                                 |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| TAXII2 Server         | Provides TAXII2 Services for system indicators   | [TAXII2 Server](https://xsoar.pan.dev/docs/reference/integrations/taxii2-server)                  |
|                       | (outbound feed). You can choose to use TAXII     |                                                                                                   |
|                       | v2.0 or TAXII v2.1.                              |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| PingCastle            | Listens for PingCastle XML reports.              | [PingCastle](https://xsoar.pan.dev/docs/reference/integrations/ping-castle)                       |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Publish List          | Publishes Cortex XSIAM lists for external        | [Publish List](https://cortex.marketplace.pan.dev/marketplace/details/PublishList/)               |
|                       | consumption.                                     |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Simple API Proxy      | Provides a simple API proxy to restrict          | [Simple API Proxy](https://cortex.marketplace.pan.dev/marketplace/details/SimpleAPIProxy/)        |
|                       | privileges or minimize the number of credentials |                                                                                                   |
|                       | issued at the API.                               |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Syslog v2             | Opens cases automatically from Syslog clients.   | [Syslog v2](https://xsoar.pan.dev/docs/reference/integrations/syslog-v2)                          |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Web File Repository   | Make your environment ready for testing purposes | [Web File                                                                                         |
|                       | for your playbooks or automations to download    | Repository](https://xsoar.pan.dev/docs/reference/integrations/web-file-repository#context-output) |
|                       | files from a web server.                         |                                                                                                   |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------+

> **Note**

- > When running on the tenant, you can only use long-running
  > integrations provided by Cortex XSIAM, you cannot create custom
  > ones. Custom long-running integrations are supported only on engines
  > at this time.

- > Configuring custom certificates or private API Keys in the
  > long-running integration instance is supported only on engines, not
  > on the Cortex XSIAM tenant.

####### Credentials

For long-running integrations running on a tenant, you must set a
username and password. For long-running integrations running on an
engine, we strongly recommend setting a username and password, but it is
not required.

Users with sufficient permissions can set the username and password for
specific integration instances on the **Automation & Feed Integrations**
page.

####### Test the long-running integration connection

- **Integration instance running on a tenant**

<!-- -->

- You can use CURL commands from any terminal to access and test the
  long-running integration. The string `xdr` in the URL must be replaced
  by `crtx` and the data URL must always be prefixed by `ext-`.

  > **Note**

  > For the TAXII Server and TAXII2 Server integrations, the `xdr`
  > string is automatically replaced by `crtx`. For the Microsoft Teams
  > integration, you can use the
  > `microsoft-teams-create-messaging-endpoint` command to get the
  > correct messaging endpoint based on the server URL, the server
  > version, and the instance configurations. For more information, see
  > [Microsoft
  > Teams](https://xsoar.pan.dev/docs/reference/integrations/microsoft-teams).

  Example:

  **Tenant URL**: https://crtx-cnt-onr-xsiam-dran-9c0.xdr-qa2-uat.us.com

  **Request URL**:
  https://ext-crtx-cnt-onr-xsiam-dran-9c0.crtx-qa2-uat.us.com/xsoar/instance/execute/edl_instance_01\\?q\\=type:ip

  **CURL**: curl -v -u user:pass
  https://ext-crtx-cnt-onr-xsiam-dran-9c0.crtx-qa2-uat.us.com/xsoar/instance/execute/edl_instance_01\\?q\\=type:ip

<!-- -->

- **Integration instance running on an engine**

<!-- -->

- You can use CURL commands from any terminal to access and test the
  long-running integration at the engine URL:

  `http://<engine-address>:<integration listen port>/`

  For example,
  `curl -v -u user:pass http://<engine_address>:<listen_port>/?n=50`

**Curl request parameters**

When sending a curl request to the URL, use the following parameters:

+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Argument              | Description                                            | Example                                                                                                                     |
+=======================+========================================================+=============================================================================================================================+
| `n`                   | The maximum number of entries in the output. If no     | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?n=50`                                       |
|                       | value is provided, will use the value specified in     |                                                                                                                             |
|                       | the **List Size** parameter in the integration         |                                                                                                                             |
|                       | instance settings.                                     |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `s`                   | The starting entry index from which to export the      | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?s=10&n=50`                                  |
|                       | indicators.                                            |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `v`                   | The output format. Supports PAN-OS                     | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=json`                                     |
|                       | (text), CSV, JSON, mwg, and proxysg (alias: bluecoat). |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `q`                   | The query is used to retrieve indicators from the      | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?q="type:ip and sourceBrand:my_source"`      |
|                       | system.                                                |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `t`                   | Only with mwg format. The type is indicated at the top | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=mwg&t=ip`                                 |
|                       | of the exported list. Supports: string, applcontrol,   |                                                                                                                             |
|                       | dimension, category, ip, mediatype, number, and regex. |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `sp`                  | If set, will strip ports off URLs; otherwise, will     | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=text&sp`                                  |
|                       | ignore URLs with ports.                                |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `di`                  | Only with PAN-OS (text) format. If set, will ignore    | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=text&di`                                  |
|                       | URLs that are not compliant with PAN-OS URL format     |                                                                                                                             |
|                       | instead of being rewritten.                            |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `cr`                  | If set, will strip protocols off URLs.                 | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=text&pr`                                  |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `cd`                  | Only with proxysg format. The default category for the | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=proxysg&cd=default_category`              |
|                       | exported indicators.                                   |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `ca`                  | Only with proxysg format. The categories that will be  | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=proxysg&ca=category1,category2`           |
|                       | exported. Indicators not in these categories will be   |                                                                                                                             |
|                       | classified as the default category.                    |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `tr`                  | Only with PAN-OS (text) format. Whether to collapse    | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?q="type:ip and sourceBrand:my_source"&tr=1` |
|                       | IPs.                                                   |                                                                                                                             |
|                       |                                                        |                                                                                                                             |
|                       | - 0 - Do not collapse.                                 |                                                                                                                             |
|                       |                                                        |                                                                                                                             |
|                       | - 1 - Collapse to ranges.                              |                                                                                                                             |
|                       |                                                        |                                                                                                                             |
|                       | - 2 - Collapse to CIDRs                                |                                                                                                                             |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| `tx`                  | Whether to output CSV formats as textual web pages.    | `https://ext-<tenant-address>/instance/execute/<ExportIndicators_instance_name>?v=csv&tx`                                   |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

####### Define a listening port for long-running integrations

When configuring a long-running integration instance, you may need to
define a listening port.

- **Integration Instance Running on a Tenant**

<!-- -->

- If the long-running integration runs on the Cortex XSIAM tenant, you
  do not need to enter a **Listen Port** in the instance settings. The
  system auto-selects an unused port for the long-running integration
  when the instance is saved.

<!-- -->

- **Integration Instance Running on an Engine**

<!-- -->

- You must set the **Listen Port** for access when configuring a
  long-running integration instance on an engine. Use a unique port for
  each long-running integration instance. Do not use the same port for
  multiple instances.

###### Manage credentials

Credentials simplify and compartmentalize administrative tasks, and
enable you to save login information without exposing usernames,
passwords, certificates, and SSH keys. You can reuse credentials across
multiple systems, for example, when using the same administrator
password across multiple endpoints.

After you set up a credential, you can configure integration instances
to use it instead of entering the name and password manually.

**How to add credentials to an integration instance**

1.  Create the credential.

    a.  Select Settings \> Configurations \> Integrations \> Credentials
        \> New Credential.

    b.  Add the following parameters:

  -----------------------------------------------------------------------
  Parameters                          Description
  ----------------------------------- -----------------------------------
  Credential Name                     The name of the credential. You
                                      select this name when adding the
                                      credential to the integration
                                      instance.

  Username                            The username for the credential.

  Workgroup                           The workgroup to associate this
                                      credential with. Relevant for
                                      third-party services, such as
                                      Active Directory, CyberArk, and
                                      HashiCorps.

  Password                            The password for the credential.
                                      For example, add the API Key when
                                      defining the API credential.

  Certificate                         Certificate or SSH to use for the
                                      credential.
  -----------------------------------------------------------------------

c.  Save the credential.

<!-- -->

2.  Add the credential to the integration instance.

    a.  Go to Settings \> Configurations \> Data Collection \>
        Automation & Feed Integrations and select the integration
        instance.

    b.  Click **Add instance**.

    c.  Locate the relevant section and click **Switch to credentials**.

    - If there is more than one credential, select the relevant
      credential.

    d.  **Test** and **Save & Exit** the integration.

####### Configure an external credentials vault

Cortex XSIAM integrates with external credential vaults, which enables
you to use them without hard coding or exposing the credentials. The
credentials are not stored in Cortex XSIAM, but the integration fetches
the credentials from the external vault when called. The credentials are
passed to the relevant executed integrations as part of
the integration parameters.

Sample credentials provider integrations:

- [CyberArk AIM
  v2](https://xsoar.pan.dev/docs/reference/integrations/cyber-ark-aim-v2)

- [HashiCorp
  Vault](https://xsoar.pan.dev/docs/reference/integrations/hashi-corp-vault)

After the integration is configured to fetch credentials, you can also
use them in scripts and playbooks. To use these credentials in an
integration, click **Switch to credentials** in an integration instance,
and select the necessary credential from the drop-down menu.

###### Integration use cases

The following categories are common use cases for Cortex XSIAM
integrations. While this list is not meant to be exhaustive, it\'s a
starting point to understand what use cases are supported by Cortex
XSIAM and third-party integrations.

####### Analytics and SIEM

Top use cases:

- Fetch issues with relevant filters.

- Create, close, and delete issues/events/cases.

- Update issues - update status, assignees, severity, SLA, and more.

- Get events related to an issue/case for enrichment/investigation
  purposes.

- Query SIEM (consider aggregating logs).

These integrations usually include the Fetch Issues or Fetch Alerts
option for an integration instance configuration. The integration may
also include integration commands enabling you to list or retrieve
issues or related information.

Analytics & SIEM integration Example: ArcSight ESM

####### Authentication and Identity Management

Top use cases:

- Use credentials from the authentication vault to configure instances
  in Cortex XSIAM. (Save credentials in: Settings \> Configurations \>
  Integrations \> Credentials.) Integrations that use credentials from
  the vault should have the **Switch to credentials** option.

- Lock/Delete Account -- Use an integration to lock/unlock a third-party
  account.

- Reset Account - Perform a reset password command for a third-party
  account.

- Lock an external credentials vault - in case of an emergency (if the
  vault has been compromised), allow the option to lock/unlock the
  entire vault via an integration.

- Step-Up authentication - Enforce Multi-Factor Authentication for an
  account.

- Create, update, and delete users.

- Manage user groups.

- Block users, force a change of passwords.

- Manage access to resources and applications.

- Create, update, and delete roles.

Authentication integration example: CyberArk AIM v2 (Partner
Contribution)

####### Case Management

Top use cases:

- Create, get, edit, close a ticket or issue, and add and view comments.

- Assign a ticket/issue to a specified user.

- List all tickets, and filter by name, date, and assignee.

- Get details about a managed object, update, create, or delete.

- Add and manage users.

Case Management/Ticketing integration example: ServiceNow V2

####### Data Management and Threat Intelligence

Top use cases:

- Enrich information about different IOC types: Upload object for scan
  and get the scan results. (If there's an option to upload
  private/public, the default should be set to private.) Search for
  former scan results about an object to get information about a sample
  without uploading it yourself. Enrich information and scoring for the
  object.

- Add indicators to the system and search for existing indicators.

- Add indicators to the exclusion list.

- Calculate DBot Score for indicators.

- Enrich asset -- get vulnerability information for an asset (or a group
  of assets) in the organization.

- Generate/trigger a scan on specified assets.

- Get a scan report including vulnerability information for a specified
  scan and export it.

- Get details for a specified vulnerability.

- Scan assets for a specific vulnerability.

Data Enrichment & Threat Intelligence integration example: Unit 42
Objects Feed.

####### Email

Top use cases:

- Get message -- download the email itself, retrieve metadata, and body.

- Download attachments for a given message.

- Manage senders -- block/allow specified mail senders.

- Manage URLs -- block/allow the sending of specified URLs.

- Encode/decode URLs in messages

- Release a held message when a gateway has placed a suspicious message
  on hold.

Email Gateway integration example: MimeCast v2

####### Endpoint

Top use cases:

- Fetch issues and events

- Get event details (from a specified alert)

- Quarantine a file

- Isolate and contain endpoints

- Update indicators (for example, network and hashes) by policy (can be
  block, monitor) -- deny list

- Add indicators to the exclusion list

- Search for indicators in the system (see indicators and related
  issues/events)

- Download a file based on the hash and the path

- Trigger scans on specified hosts

- Update .DAT files for signatures and compare existing .DAT files to
  the newest one on the Cortex XSIAM tenant

- Get information for a specified host (OS, users, addresses, hostname)

- Get policy information and assign policies to endpoints

Endpoint integration example: Tanium V2

####### Forensics and Malware Analysis

Top use cases:

- Submit a file and get a report (detonation)

- Submit a URL and get a report (detonation)

- Search for past analysis (input being a hash/URL)

- Retrieve a PCAP file

- Retrieve screenshots taken during analysis

Forensic and Malware Analysis example: Cuckoo Sandbox

####### Network Security

Top use cases:

- Create block/accept policies (source, destination, port), for IP
  addresses and domains

- Add addresses and ports (services) to predefined groups, create
  groups, and more

- Support custom URL categories

- Fetch network logs for a specific address for a configurable time
  frame

- URL filtering categorization change request

- Built-in blocked rule command for fast blocking

- If there is a Management Firewall, allow the option to manage policy
  rules through it

- Get/fetch issues

- Get PCAP file, packet

- Get network logs filtered by time range, IP addresses, ports, and more

- Create/manage/delete policies and rules

- Update signatures from an online source/upload + get the last
  signature update information

- Install policy (if existing)

Network Security Firewall integration examples: Tufin (Partner
Contribution), Protectwise

####### Vulnerability Management

Top use cases:

- Enrich asset -- get vulnerability information for an asset (or a group
  of assets) in the organization.

- Generate/trigger a scan on specified assets

- Get a scan report including vulnerability information for a specified
  scan and export it

- Get details for a specified vulnerability

- Scan assets for a specific vulnerability

Vulnerability Management integration example: Tenable.sc

###### Troubleshoot Integrations

When troubleshooting integrations, do the following:

- Use the **Test** button in the integration instance.

- Verify the integration settings. Check settings such as usernames,
  URLs, and passwords.

- Download the debug log file and review its contents.

<!-- -->

- In the following example, you receive a 401 unauthorized error code
  after testing the integration.

  ![](media/rId426.png){width="5.833333333333333in" height="3.92in"}

  Click **Run Test & Download Debug Log**, to download the debug file
  locally. You can verify what server the URL request is being forwarded
  to and any other reasons as to why you received this error code. The
  401 unauthorized error code usually relates to invalid error
  credentials, expired tokens, or incorrect API settings.

<!-- -->

- Enable verbose or debug-level logging on the integration.

If you are unable to fix the integration, contact Customer Support for
further assistance.

