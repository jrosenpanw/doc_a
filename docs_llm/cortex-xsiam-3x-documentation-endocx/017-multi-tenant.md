## Multi-Tenant

### What is Cortex XSIAM multi-tenant?

Cortex XSIAM multi-tenant is designed for managed security service
providers (MSSPs) and enterprises that require strict data segregation,
but also need the flexibility to share and manage critical security
practices across tenants. In Cortex XSIAM, MSSPs and enterprises can
benefit from central licensing management and have access to a variety
of configuration options for their child tenants. These options include
defining which Cortex add-ons to include and configuring the number of
endpoints and gigabytes per tenant. This flexibility allows
multi-tenants to tailor security operations to meet the specific needs
of each child tenant.

Multi-tenancy enables you to manage multiple tenants from a single
console. For a multi-tenant deployment, you create and manage the main
account and child tenants from the Cortex Gateway.

In the main account, you can see all alerts across all child tenants.

#### Multi-tenant architecture

Multi-tenancy architecture is based on the platform\'s ability to run
separate instances (process and data) of Cortex XSIAM, linking each
child tenant to a main tenant. Each deployment consists of a main
account and child tenants. All child tenants are associated with the
main tenant. While tenant alerts can be searched from the main tenant,
no data is stored on the main tenant.

  -----------------------------------------------------------------------
  Component                           Description
  ----------------------------------- -----------------------------------
  Main tenant                         The main tenant, also referred to
                                      as the parent tenant, is used to
                                      access and administer your
                                      environment.

  Child tenant                        A child tenant is an instance of
                                      Cortex XSIAM that serves an end
                                      customer, such as the customer of
                                      an MSSP, and is associated with the
                                      main tenant. Each tenant has
                                      customer-specific data, which are
                                      stored separately.
  -----------------------------------------------------------------------

> **Note**
>
> By default, multi-tenant licenses include one child tenant.

#### MSSP multi-tenant

Cortex XSIAM supports pairing multiple Cortex XSIAM environments with a
single main account enabling MSSPs to easily manage security on behalf
of their clients.

The following license options are available for MSSP multi-tenants:

  -----------------------------------------------------------------------
  Option                              Description
  ----------------------------------- -----------------------------------
  Central licensing management        The MSSP acquires a license for the
                                      main tenant (parent account) with
                                      resource allocations of total
                                      endpoints and/or GB for child
                                      tenants. From the main tenant, the
                                      administrator can then dynamically
                                      create child tenants and allocate
                                      the resources among its child
                                      tenants. All child tenants are
                                      automatically paired to the main
                                      tenant and the licenses are all
                                      owned by the main tenant.

  Customer-owned license              The MSSP acquires a license for its
                                      parent tenant. All end customers
                                      must acquire their own licenses in
                                      a separate contract. The child
                                      tenants must be manually paired to
                                      the main tenant.
  -----------------------------------------------------------------------

#### Enterprise multi-tenant

In addition to multi-tenant for MSSPs, enterprises can use multi-tenancy
to segregate data across subdivisions while allowing for co-management
of environments with potentially diverse security stacks. With
enterprise multi-tenant, there is central visibility of threats from the
main account while providing varying levels of independence to the child
tenants. Central licensing management and dynamic allocation of
resources from the main account allow for flexibility according to
changing needs.

### Multi-tenant central licensing management

The new central licensing management for MSSP and enterprise
multi-tenant allows the MSSP or enterprise to own and manage their child
tenants dynamically from the Cortex Gateway. The Cortex Gateway displays
the main account with its child tenants and the number of endpoints ,
employees, and GBs available to allocate to child tenants. The Admin
user of the main account can add and delete child tenants, edit
allocation of resources to child tenants, and change the child tenant
subdomain.

The following are the minimum license requirements for central licensing
management:

  -----------------------------------------------------------------------
  Option                              Description
  ----------------------------------- -----------------------------------
  MSSP multi-tenant                   A multi-tenant deployment enables
                                      MSSPs to centrally manage multiple
                                      tenants and their resources from
                                      the Cortex Gateway.

  Enterprise multi-tenant             Large enterprises can have many
                                      subdivisions and want to manage
                                      their tenant allocation and
                                      resources centrally from a main
                                      tenant while maintaining complete
                                      data separation.
  -----------------------------------------------------------------------

> **Note**
>
> In MSSP or enterprise multi-tenant, the license specifies the maximum
> number of child tenants that can be created. Once this limit is
> reached, no additional tenants can be created, even if there remains
> allocation for endpoints or GBs.

### Onboard Cortex multi-tenant

This section describes how to get up and running with Cortex XSIAM
multi-tenant, including how to activate parent and child tenants, and
manage child tenants.

#### Onboarding checklist for multi-tenant central licensing deployments

We recommend that you review the following steps to successfully deploy
and onboard Cortex XSIAM with central licensing management. For MSSP
multi-tenant environments with customer-owned licenses, see [Onboarding
checklist for multi-tenant customer-owned license
deployments](#UUIDfd6a6c292697613a9af1779d0dd94a66).

This checklist enables you to set up a multi-tenant deployment. After
onboarding, you should configure Cortex XSIAM to suit your needs. For
more information, see [Configure Cortex
XSIAM](#UUID6db2b8d75b086f6234912a86a2eb8a04).

+-----------------------+-----------------------+-----------------------------------------------+
| Step                  | Details               | See More                                      |
+=======================+=======================+===============================================+
| Step 1. Activate the  | - Activate Cortex     | [See                                          |
| parent tenant         |   XSIAM in Cortex     | topic](#UUID34401c618f6e5539b83a88b80d721907) |
|                       |   Gateway for the     |                                               |
|                       |   parent tenant       |                                               |
|                       |                       |                                               |
|                       | - Enable access to    |                                               |
|                       |   Palo Alto Network   |                                               |
|                       |   resources           |                                               |
+-----------------------+-----------------------+-----------------------------------------------+
| Step 2. Create a      | Create and activate a | [See                                          |
| child tenant          | child tenant in       | topic](#UUIDf8450665a7107ec2d40a7f15349ac119) |
|                       | Cortex Gateway.       |                                               |
+-----------------------+-----------------------+-----------------------------------------------+
| Step 3. Set up users  | Set up users, roles,  | [See                                          |
| and roles             | user groups, and user | topic](#UUIDc0966cb32b3c88e214d33131de93fa8a) |
|                       | authentication.       |                                               |
+-----------------------+-----------------------+-----------------------------------------------+

##### Step 1. Activate Cortex XSIAM (main account)

To set up Cortex XSIAM multi-tenant, you need to activate the main
account in Cortex Gateway. Cortex Gateway is a centralized portal for
activating and managing tenants, users, roles, and user groups. After
activating the tenant you can then access the tenant. You will need to
repeat this task for each tenant if you have multiple tenants. The
activation process includes accessing Cortex Gateway, activating the
tenant, and then accessing the tenant.

> **Prerequisite**
>
> Before you begin, make sure you have the following:

- > Cortex XSIAM activation email.

- > Customer Support Portal Super User role is assigned to your account.

<!-- -->

- > Before activating your Cortex XSIAM tenant, you need to set up your
  > Customer Support Portal account. See [How to Create Your Customer
  > Support Portal User
  > Account](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNVCA0).
  > When you create a Customer Support Portal account you can set up
  > two-factor authentication (2FA) to log into the Customer Support
  > Portal, by using one of the following:

  - > Email

  - > Okta Verify

  - > Google Authenticator (non-FedRAMP accounts)

  > Users who create the Customer Support Portal account are granted the
  > Super User role. If you are the first user to access Cortex Gateway
  > with the Customer Support Portal Super User role, you are
  > automatically granted Account Admin permissions for the gateway.

  > You can activate Cortex XSIAM new tenants, access existing tenants,
  > and create and manage role-based access control (RBAC) for all of
  > your tenants.

**How to activate Cortex XSIAM**

1.  Enable and verify access to  Cortex XSIAM communication servers,
    storage buckets, and various resources in your firewall
    configuration. For more information, see [Enable access to required
    PANW resources](#UUID24cb15454f44c259b484435238bb6a33).

2.  Go to [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/signin/) .

- You can also access the link from the activation email.

3.  Enter your username and password or multi-factor authentication (if
    set up) by using your Customer Support Portal account credentials to
    sign in.

- Once signed in, you can view the following:

  - Tenants that are allocated to your Customer Support Portal account
    and ready for activation. After activation, you cannot move your
    tenant to a different Customer Support Portal account.

  - Tenant details such as license type, number of endpoints, and
    purchase date.

  - Tenants that were activated and are now available. If you have more
    than one Customer Support Portal account, the tenants are displayed
    according to the Customer Support Portal account name.

4.  In the **Available for Activation** section, use the serial number
    to locate the tenant that needs activation, and then click
    **Activate**.

5.  On the **Tenant Activation** page, define the following:

    - **Tenant Name:** Enter a name for the tenant. Use a name that is
      unique across your company account and up to 59 characters long.

    - **Region:** Geographic location where your tenant will be hosted.
      For more information, see [Cortex XSIAM supported
      regions](#UUID61479dc6978fbf5dda884f934ff79ef1).

    - **Tenant Subdomain:** DNS record associated with your tenant.
      Enter a name that will be used to access the tenant directly using
      the full URL:

    <!-- -->

    - `https://<xsiam-tenant>.xdr.<region>.paloaltonetworks.com`

    <!-- -->

    - (Optional) If you want to bring your own keys for encrypting your
      data, under **Advanced**, select **BYOK** and follow the
      instructions of the wizard as detailed in **Encryption Method**.

    <!-- -->

    - Encryption Method
      Cortex XSIAM enables you to select the method used to encrypt your
      tenant data at rest. You can select the encryption method of your
      tenant only when creating new tenants. Select the encryption
      method in Advanced \> Encryption Method.

      Default encryption (recommended)
      All data stored by Cortex XSIAM is encrypted at rest using a
      dedicated key management system. Cortex XSIAM provides strict key
      access controls and auditing, and encrypts user data at rest
      according to AES-256 encryption standards. We recommend all our
      customers use this default system.

      BYOK (Bring your own keys)
      BYOK (Bring Your Own Keys) enables you to generate your own
      encryption keys and securely import and manage them via Cortex
      Gateway to retain greater control over your tenant data and
      encryption. This requires [further
      setup](/document/preview/1054855#UUID-f87e1680-f4d1-fa01-c156-b1e48cf23398).

6.  Select
    **I agree to the terms and conditions of the Privacy policy**.

7.  Click **Activate**.

- The activation process can take about an hour and does not require
  that you remain on the activation page. Cortex XSIAM sends a
  notification to your email when the process is complete.

8.  After activation, from Cortex Gateway, in the
    **Available Tenants** when hovering over the activated tenant, do
    the following:

    - Ensure that you can successfully access the tenant by clicking the
      Cortex XSIAM tenant name (when the tenant is active).

    - In the dialog box, view the tenant status, region, serial number,
      and license details.

##### Step 2. Create a child tenant

After setting up the main account, you can create child tenants in
Cortex Gateway. You can create as many child tenants as you require,
subject to your license.

> **Note**

- > The main account is labeled in Cortex Gateway, but child tenants are
  > not labeled.

- > Cortex enables parent-child pairing between tenants located in
  > different geographical regions.

- > To create a child tenant, ensure that you have Account Admin
  > permissions.

In Cortex Gateway, you can view all the available tenants. If you want
to create more child tenants than your license permits, contact Customer
Support.

1.  In the Cortex Gateway, hover over the main account you activated
    previously until the three-dot menu appears and click
    **Add Child Tenant**.

2.  Add the following details:

+-----------------------------------+------------------------------------------------------------+
| Parameter                         | Description                                                |
+===================================+============================================================+
| Child Tenant Name                 | Give the Cortex XSIAM tenant an easily recognizable name.  |
|                                   |                                                            |
|                                   | Choose a name that is 59 or fewer characters and is unique |
|                                   | across your company account.                               |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > After activating a child tenant, you can\'t change the   |
|                                   | > child tenant\'s name.                                    |
+-----------------------------------+------------------------------------------------------------+
| Region                            | View the region for the child tenant.                      |
+-----------------------------------+------------------------------------------------------------+
| Child Tenant Subdomain            | Give your Cortex XSIAM instance an easy-to-recognize name  |
|                                   | that is used to access the tenant directly using the full  |
|                                   | URL.                                                       |
|                                   |                                                            |
|                                   | https://\<subdomain\>.crtx.\<region\>.paloaltonetworks.com |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > This is a public FQDN, so be careful with sensitive      |
|                                   | > information such as the company name.                    |
|                                   | >                                                          |
|                                   | > After activating a child tenant, you can only change the |
|                                   | > child tenant subdomain once.                             |
+-----------------------------------+------------------------------------------------------------+
| Child Units Allocation            | Assign the number of employees and Gigabytes you want to   |
|                                   | allocate to this child tenant. The amount used and the     |
|                                   | total amount available to this multi-tenant environment    |
|                                   | are displayed.                                             |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > Ensure that you meet the [minimum                        |
|                                   | > requirements](#X32b9747b8808cf0fd2da086cb097292d9facf30) |
|                                   | > for child tenant allocation.                             |
+-----------------------------------+------------------------------------------------------------+
| Add Ons                           | If any license add-ons were purchased with your            |
|                                   | multi-tenant license, they are listed here. If you         |
|                                   | acquired compute units (CU) or forensics, you can allocate |
|                                   | how many units to allocate to this child tenant.           |
+-----------------------------------+------------------------------------------------------------+

3.  Confirm approval of the terms and conditions of the privacy policy
    and click **Activate**.

- Activation can take up to an hour. You should receive notification by
  email that the child tenant has completed the activation process.

4.  (Optional) Add another child tenant by repeating steps 1 and 2 or
    access your newly created tenant.

- In the Cortex Gateway, under your main account, you can see the total
  number of tenants you are licensed for and how many you have created.

  > **Note**

  > If you reach your limit for child tenants, depending on your
  > license, you may be able to create more tenants. You may be charged
  > for additional tenants. Contact Customer Support if you are
  > approaching your authorized limit.

###### Child tenant minimum allocations

The following are the minimum number of endpoints , employees and
Gigabytes needed in a child tenant. You will not be able to create a
child tenant with less than these minimum allocations, nor will you be
able to edit your child tenant allocations to have less than these
minimum allocations.

  -----------------------------------------------------------------------
  Multi-tenant environment            Child tenant minimum allocation
  ----------------------------------- -----------------------------------
  MSSP multi-tenant                   100 employees AND 50 Gigabytes.

  Enterprise multi-tenant             100 employees AND 50 Gigabytes.
  -----------------------------------------------------------------------

#### Onboarding checklist for multi-tenant customer-owned license deployments

We recommend that you review the following steps to successfully deploy
and onboard Cortex XSIAM with customer-owned licenses. For MSSP
multi-tenant environments with central licensing management, see
[Onboarding checklist for multi-tenant central licensing
deployments](#UUID938978e60c714dd5ea0ec4ae127d32e6).

This checklist enables you to set up a multi-tenant deployment. After
onboarding, you should configure Cortex XSIAM to suit your needs. For
more information, see [Configure Cortex
XSIAM](#UUID6db2b8d75b086f6234912a86a2eb8a04).

  -----------------------------------------------------------------------------------------------
  Step                    Details                 See More
  ----------------------- ----------------------- -----------------------------------------------
  Step 1. Activate Cortex Activate parent and     [See
  XSIAM parent and child  child tenants in Cortex topic](#UUID506c648b944995270e4259e111547e23)
  tenants                 Gateway.                

  Step 2. Define access   Ensure the users have   [See
  configurations and role the appropriate role    topic](#UUIDc54097060b0a479fcc7b4fd261bfe449)
  permissions             permissions in the CSP  
                          and the correct access  
                          configurations in       
                          Cortex Gateway.         

  Step 3. Pair parent     Use Cortex XSIAM Tenant [See
  tenant with child       Management in the       topic](#UUIDc4e2a73ac6f270542273e416375522e1)
  tenant                  parent tenant to pair   
                          the child tenant.       
  -----------------------------------------------------------------------------------------------

##### Step 1. Activate Cortex Cortex XSIAM (parent and child tenants)

To set up Cortex XSIAM multi-tenant in a customer-owned license
deployment, you need to activate the parent and child tenants in Cortex
Gateway. Cortex Gateway is a centralized portal for activating and
managing tenants, users, roles, and user groups. After activating the
tenants you can then access the tenant. You will need to repeat this
task for each tenant if you have multiple tenants. The activation
process includes accessing Cortex Gateway, activating the tenant, and
then accessing the tenant.

> **Prerequisite**
>
> Before you begin, make sure you have the following:

- > Cortex XSIAM activation email.

- > Customer Support Portal Super User role is assigned to your account.

<!-- -->

- > Before activating your Cortex XSIAM tenant, you need to set up your
  > Customer Support Portal account. See [How to Create Your Customer
  > Support Portal User
  > Account](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNVCA0).
  > When you create a Customer Support Portal account you can set up
  > two-factor authentication (2FA) to log into the Customer Support
  > Portal, by using one of the following:

  - > Email

  - > Okta Verify

  - > Google Authenticator (non-FedRAMP accounts)

  > Users who create the Customer Support Portal account are granted the
  > Super User role. If you are the first user to access Cortex Gateway
  > with the Customer Support Portal Super User role, you are
  > automatically granted Account Admin permissions for the gateway.

  > You can activate Cortex XSIAM new tenants, access existing tenants,
  > and create and manage role-based access control (RBAC) for all of
  > your tenants.

**How to activate Cortex XSIAM**

1.  Enable and verify access to  Cortex XSIAM communication servers,
    storage buckets, and various resources in your firewall
    configuration. For more information, see [Enable access to required
    PANW resources](#UUID24cb15454f44c259b484435238bb6a33).

2.  Go to [Cortex
    Gateway](https://cortex-gateway.paloaltonetworks.com/signin/) .

- You can also access the link from the activation email.

3.  Enter your username and password or multi-factor authentication (if
    set up) by using your Customer Support Portal account credentials to
    sign in.

- Once signed in, you can view the following:

  - Tenants that are allocated to your Customer Support Portal account
    and ready for activation. After activation, you cannot move your
    tenant to a different Customer Support Portal account.

  - Tenant details such as license type, number of endpoints, and
    purchase date.

  - Tenants that were activated and are now available. If you have more
    than one Customer Support Portal account, the tenants are displayed
    according to the Customer Support Portal account name.

4.  In the **Available for Activation** section, use the serial number
    to locate the tenant that needs activation, and then click
    **Activate**.

5.  On the **Tenant Activation** page, define the following:

    - **Tenant Name:** Enter a name for the tenant. Use a name that is
      unique across your company account and up to 59 characters long.

    - **Region:** Geographic location where your tenant will be hosted.
      For more information, see [Cortex XSIAM supported
      regions](#UUID61479dc6978fbf5dda884f934ff79ef1).

    - **Tenant Subdomain:** DNS record associated with your tenant.
      Enter a name that will be used to access the tenant directly using
      the full URL:

    <!-- -->

    - `https://<xsiam-tenant>.xdr.<region>.paloaltonetworks.com`

    <!-- -->

    - (Optional) If you want to bring your own keys for encrypting your
      data, under **Advanced**, select **BYOK** and follow the
      instructions of the wizard as detailed in **Encryption Method**.

    <!-- -->

    - Encryption Method
      Cortex XSIAM enables you to select the method used to encrypt your
      tenant data at rest. You can select the encryption method of your
      tenant only when creating new tenants. Select the encryption
      method in Advanced \> Encryption Method.

      Default encryption (recommended)
      All data stored by Cortex XSIAM is encrypted at rest using a
      dedicated key management system. Cortex XSIAM provides strict key
      access controls and auditing, and encrypts user data at rest
      according to AES-256 encryption standards. We recommend all our
      customers use this default system.

      BYOK (Bring your own keys)
      BYOK (Bring Your Own Keys) enables you to generate your own
      encryption keys and securely import and manage them via Cortex
      Gateway to retain greater control over your tenant data and
      encryption. This requires [further
      setup](/document/preview/1054855#UUID-f87e1680-f4d1-fa01-c156-b1e48cf23398).

6.  Select
    **I agree to the terms and conditions of the Privacy policy**.

7.  Click **Activate**.

- The activation process can take about an hour and does not require
  that you remain on the activation page. Cortex XSIAM sends a
  notification to your email when the process is complete.

8.  After activation, from Cortex Gateway, in the
    **Available Tenants** when hovering over the activated tenant, do
    the following:

    - Ensure that you can successfully access the tenant by clicking the
      Cortex XSIAM tenant name (when the tenant is active).

    - In the dialog box, view the tenant status, region, serial number,
      and license details.

##### Step 2. Define access configurations and role permissions

To set up manual pairing in a customer-owned license multi-tenant
deployment, after the parent and child Cortex XSIAM tenants are
activated, you must define correct access configuration in the Customer
Support Portal (CSP) and role permissions in Cortex Gateway.

The following table describes the access configurations and role
permissions needed:

  -----------------------------------------------------------------------
  Tenant                  Application             Action
  ----------------------- ----------------------- -----------------------
  Parent                  Customer Support Portal Ensure the parent user
                          (CSP) Account           name has *Super User*
                                                  role permissions.

  Cortex Gateway          Ensure the user name    
                          added to the child      
                          tenant's CSP account    
                          has *Admin* role        
                          permissions on the      
                          parent Cortex XSIAM     
                          instance.               

  Child                   Customer Support Portal Add the user name from
                          (CSP) Account           the parent tenant who
                                                  is initiating the
                                                  parent-child pairing
                                                  and ensure the user
                                                  name has *Super User*
                                                  role permissions.

  Gateway                 Provide the user name   
                          added in CSP with       
                          *Admin* role            
                          permissions to access   
                          the child Cortex XSIAM  
                          instance.               
  -----------------------------------------------------------------------

##### Step 3. Pair a parent tenant with child tenant

After you set up the correct access configurations and role permissions,
you should pair the parent tenant to the child tenants.

Cortex provides the capability of parent-child pairing between tenants
located in different geographical regions. To enable this capability,
contact your support team.

###### Pairing a Parent and Child Tenant

1.  Log in to the Cortex XSIAM tenant that has been assigned as the
    parent tenant and select Settings \> Configurations \> Tenant
    Management.

- The Tenant Management table displays:

  - **Tenant Name**: Name of the child tenant.

  - **Pairing Status**: State of a pairing request: **Paired**,
    **Pending**, **Failed**, **Rejected**.

  - **Account Name**: CSP account to which the child tenant is
    associated.

  - **Last Sync**: Timestamp of when the parent tenant last made contact
    with child tenant.

  - **Managed Security Actions**: A column for each security action with
    a status: **Configuration name** or **Unmanaged**. **Unmanaged**
    status means that a configuration for the security action has not
    yet been selected.

  - **Region**: Shows the region of the child tenant.

  <!-- -->

  - > **Note**

    > This field is not enabled by default. To enable contact your
    > account administrator.

2.  Click **+ Pair Tenant**.

- You can pair tenants across different regions.

3.  In the **Pair Tenant** window, select the child tenant you want to
    pair.

- Child tenants are grouped according to:

  - **Unpaired**: Children that have not yet been paired and are
    available. If another parent has requested to pair with the child
    but the child has not yet agreed, the tenant will appear.

  - **Paired**: Children that have already been paired to this parent.

  - **Paired with others**: Children that have been paired with other
    parents.

  - **Pending**: Children with a pending pairing request.

4.  **Pair the tenant.**

- Cortex XSIAM then sends a **Request for Pairing** to the specified
  child tenant.

5.  In the child tenant Cortex XSIAM console, a child tenant user with
    Admin role permissions needs to approve the pairing by navigating to
    **Notifications**
    ![](media/rId578.png){width="0.14583333333333334in"
    height="0.20833333333333334in"}, locate the **Request for Pairing**
    notification and select **Approve**.

6.  Verify the parent-child pairing.

- After pairing has been approved, in the child tenant's Cortex XSIAM
  app, when navigating to a page managed by a parent configuration, the
  child user is notified by a flag who is managing their security.

  In the child tenant's, pages that you manage, appear with a read-only
  banner. Child tenant users cannot perform any actions from these
  pages, but can view the configurations you create on their behalf.

  ![](media/rId581.png){width="3.125in" height="0.8854166666666666in"}

### Dynamic license allocation

In a multi-tenant environment with central licensing management, in
Cortex Gateway you can edit child tenant allocations, add child tenants,
and delete child tenants. When you delete a child tenant, the tenant\'s
allocations of endpoints, employees, and GBs are returned to the main
account\'s pool and can immediately be used for existing child tenants
or for creating new child tenants.

#### Edit tenant allocations

You can edit the child tenant allocations by increasing or decreasing
the amount of endpoints, employees, and GBs allocated to the tenant. The
total available count for the multi-tenant environment is updated
accordingly.

> **Note**
>
> Changing the tenant\'s allocations might result in a short downtime of
> your tenant.

1.  In Cortex Gateway, locate the main account and then hover over the
    child tenant until the three-dot menu appears and click
    **Edit Tenant Allocations**.

2.  In the **Edit Tenant Allocations** window, assign the number of
    Gigabytes and endpoints you want to allocate to this child tenant.
    The amount used and the total amount available to this multi-tenant
    environment are displayed. Ensure you meet the [minimum allocation
    requirements](#X32b9747b8808cf0fd2da086cb097292d9facf30). Click
    **Done**.

#### Add a child tenant

When you have enough license allocations available in your multi-tenant
central licensing environment, you can add a child tenant to the main
account in Cortex Gateway.

1.  In the Cortex Gateway, hover over the main account you activated
    previously until the three-dot menu appears and click
    **Add Child Tenant**.

2.  Add the following details:

+-----------------------------------+------------------------------------------------------------+
| Parameter                         | Description                                                |
+===================================+============================================================+
| Child Tenant Name                 | Give the Cortex XSIAM tenant an easily recognizable name.  |
|                                   |                                                            |
|                                   | Choose a name that is 59 or fewer characters and is unique |
|                                   | across your company account.                               |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > After activating a child tenant, you can\'t change the   |
|                                   | > child tenant\'s name.                                    |
+-----------------------------------+------------------------------------------------------------+
| Region                            | View the region for the child tenant.                      |
+-----------------------------------+------------------------------------------------------------+
| Child Tenant Subdomain            | Give your Cortex XSIAM instance an easy-to-recognize name  |
|                                   | that is used to access the tenant directly using the full  |
|                                   | URL.                                                       |
|                                   |                                                            |
|                                   | https://\<subdomain\>.crtx.\<region\>.paloaltonetworks.com |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > This is a public FQDN, so be careful with sensitive      |
|                                   | > information such as the company name.                    |
|                                   | >                                                          |
|                                   | > After activating a child tenant, you can only change the |
|                                   | > child tenant subdomain once.                             |
+-----------------------------------+------------------------------------------------------------+
| Child Units Allocation            | Assign the number of employees and Gigabytes you want to   |
|                                   | allocate to this child tenant. The amount used and the     |
|                                   | total amount available to this multi-tenant environment    |
|                                   | are displayed.                                             |
|                                   |                                                            |
|                                   | > **Note**                                                 |
|                                   | >                                                          |
|                                   | > Ensure that you meet the [minimum                        |
|                                   | > requirements](#sectionidm234529819989674) for child      |
|                                   | > tenant allocation.                                       |
+-----------------------------------+------------------------------------------------------------+
| Add Ons                           | If any license add-ons were purchased with your            |
|                                   | multi-tenant license, they are listed here. If you         |
|                                   | acquired compute units (CU) or forensics, you can allocate |
|                                   | how many units to allocate to this child tenant.           |
+-----------------------------------+------------------------------------------------------------+

3.  Confirm approval of the terms and conditions of the privacy policy
    and click **Activate**.

- Activation can take up to an hour. You should receive notification by
  email that the child tenant has completed the activation process.

4.  (Optional) Add another child tenant by repeating steps 1 and 2 or
    access your newly created tenant.

- In the Cortex Gateway, under your main account, you can see the total
  number of tenants you are licensed for and how many you have created.

  > **Note**

  > If you reach your limit for child tenants, depending on your
  > license, you may be able to create more tenants. You may be charged
  > for additional tenants. Contact Customer Support if you are
  > approaching your authorized limit.

#### Delete a child tenant

Deleting a child tenant deletes all of its data and content permanently.
The child tenant\'s license allocations are returned to the total
available in the multi-tenant environment and can be allocated to other
child tenants.

> **Note**
>
> In a multi-tenant central licensing management environment, you cannot
> unpair a child tenant from the main account. The only way to remove
> the connection to the main account is to delete the tenant.

1.  In Cortex Gateway, locate the main account and then hover over the
    child tenant until the three-dot menu appears and click
    **Delete Tenant**.

2.  In the **Delete Tenant** window, confirm that you want to delete the
    child tenant by typing \'Delete\' and click **Confirm Deletion**.

### Child tenant management

You can manage, track, and investigate child tenant data from the parent
tenant.

#### Manage a child tenant

Multi-tenancy enables you to view and investigate Cortex XSIAM data of a
child tenant, and initiate security actions on their behalf.

In your Cortex XSIAM management console, you have access to view the
following pages:

- Incidents

- Alerts

- Query Builder

- Query Center and Results

- Causality View

- Timeline View

To initiate security actions on your child tenant, you need to create a
**Configuration**. Security actions are managed by configurations you
create in Cortex XSIAM and then assign to each of the child tenants.
Each action requires its own configuration and allocation to a child
tenant.

> **Note**
>
> Once a configuration is created Cortex XSIAM resets the child tenant
> data and synchronizes the security actions configured in the parent
> tenant.

You can create configuration for the following actions:

- Starred Alerts Policies

- Alert Exclusions

- Profiles

- Allow/Block Lists

#### Track your tenant management

To view child tenant details, in Cortex XSIAM, select Settings \>
Configurations \> Tenant Management.

The **Tenant Management** page displays the following information about
each of your child tenants:

+-----------------------------------------------------+-----------------------------------+
| Field                                               | Description                       |
+=====================================================+===================================+
| ![](media/rId593.png){width="0.23437445319335082in" | Identifies whether the child      |
| height="0.20833333333333334in"} (Status Indicator)  | tenant is connected.              |
+-----------------------------------------------------+-----------------------------------+
| Tenant ID                                           | The Cortex XSIAM tenant ID.       |
+-----------------------------------------------------+-----------------------------------+
| Tenant name                                         | Name you defined during the       |
|                                                     | pairing process or during child   |
|                                                     | tenant activation.                |
+-----------------------------------------------------+-----------------------------------+
| Account ID                                          | The CSP account ID.               |
+-----------------------------------------------------+-----------------------------------+
| Account name                                        | Name of the parent tenant.        |
+-----------------------------------------------------+-----------------------------------+
| Pairing status                                      | Status of the child paring        |
|                                                     | process:                          |
|                                                     |                                   |
|                                                     | - Pending                         |
|                                                     |                                   |
|                                                     | - Paired                          |
|                                                     |                                   |
|                                                     | - Approved                        |
|                                                     |                                   |
|                                                     | - Declined                        |
|                                                     |                                   |
|                                                     | - Pending                         |
|                                                     |                                   |
|                                                     | - Paired to another               |
|                                                     |                                   |
|                                                     | - Not Paired                      |
+-----------------------------------------------------+-----------------------------------+
| Last sync                                           | Timestamp of the last security    |
|                                                     | action sync initiated by the      |
|                                                     | parent tenant.                    |
+-----------------------------------------------------+-----------------------------------+
| BIOC Rules & exceptions                             | Name of the configuration         |
|                                                     | managing the BIOC rules and       |
|                                                     | exceptions actions.               |
+-----------------------------------------------------+-----------------------------------+
| Starred incidents policy                            | Name of the configuration         |
|                                                     | managing the starred incidents    |
|                                                     | policy actions.                   |
+-----------------------------------------------------+-----------------------------------+
| Alert exclusion                                     | Name of the configuration         |
|                                                     | managing the alert exclusion      |
|                                                     | actions.                          |
+-----------------------------------------------------+-----------------------------------+
| Profiles                                            | Name of the configuration         |
|                                                     | managing the profile actions.     |
+-----------------------------------------------------+-----------------------------------+
| Region                                              | > **Note**                        |
|                                                     | >                                 |
|                                                     | > This field is not enabled by    |
|                                                     | > default. To enable, contact     |
|                                                     | > your account administrator.     |
|                                                     |                                   |
|                                                     | Region of child tenant.           |
+-----------------------------------------------------+-----------------------------------+

#### Investigate child tenant data

With Cortex XSIAM multi-tenancy, you can investigate the Cortex XSIAM
child tenant data.

By default, Cortex XSIAM displays data for your tenant. To display data
for your child tenant, select the tenant from the drop-down.

![](media/rId597.png){width="4.888888888888889in" height="2.875in"}

Some common tasks that you might perform include:

- Investigate incidents on a child tenant.

- Investigate alerts on a child tenant.

#### Create and allocate configurations

To manage security actions on behalf of your child tenant, you need to
first create and allocate an action configuration.

1.  Navigate to each of the following Cortex XSIAM pages and follow the
    detailed steps:

    - Incident Response \> Incident Configuration \> Alert Exclusions \>
      Alert Exclusions Configuration panel

    - Incident Response \> Incident Configuration \> Starred Alerts \>
      Starred Alerts Configuration panel

    - Endpoints \> Policy Management \> Prevention \> Profiles \>
      Profile Configuration panel

    - Incident Response \> Response \> Action Center \> Currently
      Applied Actions \> Block List/Allow List \> Allow List/Block List
      configuration panel

2.  In the corresponding Configuration panel, **+ Create New**
    configuration.

3.  Enter the configuration **Name** and **Description**.

4.  **Create**.

- The new configuration appears in the **Configuration** pane.

5.  Navigate to Settings \> Tenant Management.

6.  In the **Tenant Management** table, right-click a child tenant row
    and **Edit Configurations**.

7.  Assign the configuration you want to use to manage each of the
    security actions.

- > **Note**

  > You can configure **Profiles** only as **Managed** or **Unmanaged**.
  > All profiles you create are automatically cloned to your child
  > tenants.

8.  **Update**.

- The **Tenant Management** table is updated with your assigned
  configurations.

#### Create a security managed action

After you have created and assigned a configuration for each of your
child tenant's security actions, you can define the specific managed
action on behalf of the child tenant.

1.  Navigate to each of the following Cortex XSIAM pages:

    - Investigation \> Incident Management \> Exclusions \> Alert
      Exclusions Configuration panel

    - Investigation \> Incident Management \> Starred Alerts \> Starred
      Alerts Configuration panel

    - Endpoints \> Policy Management \> Prevention \> Profiles \>
      Profile Configuration panel

    - Response \> Action Center \> Currently Applied Actions \> Block
      List/Allow List \> Allow List/Block List configuration panel

2.  In the corresponding **Configuration** panel, select the [action
    configuration](#UUIDc8d687cc167494c62b112dbcc3bee66a) you created
    and allocated to your child tenant.

- The corresponding security action **Table** displays the actions
  managing the child tenant.

3.  Depending on the security action, select:

    - **+ Add Exclusion** to create an Alert Exclusion.

    - **+ Add Starring Configuration** to create a starred alert
      inclusion.

    - **+ New Profile** to create a new endpoint profile.

- > **Note**

  > Profiles you create are automatically cloned to your child tenants.

### About managed threat hunting

Cortex XSIAM provides the Managed Threat Hunting service as an add-on
security service. To use Managed Threat Hunting, you must purchase a
Managed Threat Hunting license and have a license with a minimum of 500
endpoints.

Managed Threat Hunting augments your security by providing 24/7,
year-round monitoring by Palo Alto Networks threat researchers and Unit
42 experts. The Managed Threat Hunting teams proactively safeguard your
organization and provide threat reports for critical security incidents
and impact reports for emerging threats that provide an analysis of
exposure in your organization. In addition, the Managed Threat Hunting
team can identify incidents and provide indepth review of related threat
reports.

this is a test

#### Set up Managed Threat Hunting

To get started with Managed Threat Hunting:

1.  Open the Cortex XSIAM tenant and approve the pairing request sent to
    your tenant.

    a.  Navigate to **Notifications** and locate the
        **Request for Pairing** notification.

    b.  Select **Approve** and then **Yes** to confirm.

    - After the request is approved, Cortex XSIAM displays the Managed
      Threat Hunting label at the top of the page.

2.  Configure notification emails for the impact reports and threat
    inquiries you want to send.

    a.  Select Settings \> Configurations \> Managed Services.

    b.  Enter one or more email addresses to which you want to send
        reports and inquires and **ADD** each one.

    c.  **Save** your changes.

3.  Test the email, by going to your defined email address mailbox, and
    locate the **Welcome to the Palo Alto Networks Cortex
    XSIAM Managed Threat Hunting Service** email. If you did not receive
    the email, contact Customer Support.

4.  (*Optional*) If desired, forward Managed Threat Hunting alerts to
    external sources such as email or slack from the Settings \>
    Configurations \> General \> Notifications page.

- This forwards the alert and the detailed report in a PDF format.

#### Investigate Managed Threat Hunting reports

The Managed Threat Hunting team proactively scans, identifies, and
analyzes your Cortex XSIAM tenant for possible threats and creates
detailed threat and impact reports to help you track and manage your
Cortex XSIAM data.

Cortex XSIAM displays the reports in a dedicated page that allows you to
investigate and communicate with your Managed Threat Hunting team. When
a new report is sent, MTH send a notification to your Notification
Center. **MTH** type notifications will appear at the top of your
notification list and offer the following options:

- **Open**---Pivot to report in the **Managed Threat Hunting** table.

- **Dismiss**---Delete the notification from your **Notifications**
  list.

> **Note**
>
> The MTH page is available for users with the Managed Threat Hunting
> license and have the necessary permission to view and triage alerts
> and incidents in Cortex XSIAM.

To investigate your reports:

1.  In the Cortex XSIAM console, select **MTH**.

- The Managed Threat Hunting page displays a side-by-side view of all
  your reports and their corresponding report details and communication.

2.  In the left-pane, select the report you want to investigate. You can
    sort the list according to the report **Type**, **Insert Time**, or
    **Severity**, and use the search bar to help you locate reports.

- After selecting a report, the right-pane view displays a summary of
  the Managed Threat Hunting findings along with an attachment of the
  complete report.

3.  In the right-pane, investigate the report findings and add your
    comments.

- The comments are a way for you to communicate directly with the
  Managed Threat Hunting without the need to send separate emails. When
  you post a comment, the Managed Threat Hunters team is notified and
  can see and reply to your comments. Comments are listed
  chronologically and are visible to all the Cortex XSIAM tenant users
  with access to the MTH page and the Managed Threat Hunting team. You
  can attach up to ten PDF or image format files with a maximum of 10MB
  per file in each comment. Editing and deleting a comments is available
  only on comments you wrote.

# Protect your endpoints

This section outlines how Cortex XSIAM, with its integration of the
Cortex XDR agent, provides comprehensive protection for your endpoints.
It details the key features and functionalities that enable you to
prevent sophisticated attacks, rapidly detect and investigate threats,
and automate response actions across all your entire endpoints, whether
on-premises or remote.

> **Note**
>
> Cortex endpoint security is not included in the Cortex XSIAM NG SIEM
> license.

