# 3. User Management and Authentication

After activating your tenant, you need to manage user roles, permissions, and authentication methods. [cite_start]Cortex XSIAM uses a combination of Role-Based Access Control (RBAC) and Scope-Based Access Control (SBAC). [cite: 173, 174]

## Assigning User Roles and Groups

[cite_start]You can manage roles and users from either **Cortex Gateway** (for multiple tenants) or **Cortex XSIAM Access Management** (for a specific tenant). [cite: 180, 181, 192] [cite_start]It is recommended to create user groups in the Cortex XSIAM tenant, as this supports granular scoping and SAML group mapping. [cite: 237, 238, 239]

### Predefined User Roles

Cortex XSIAM provides several default roles with specific access rights. [cite_start]These roles cannot be edited directly, but you can save them as new roles and customize the permissions. [cite: 200, 207, 208] Key roles include:

* [cite_start]**Account Admin**: A super user with full access to all Cortex products and tenants. [cite: 212]
* [cite_start]**Instance Administrator**: Has full view and edit permissions for all components within a specific tenant. [cite: 212]
* [cite_start]**Investigator**: Can view and triage issues and cases. [cite: 212]
* [cite_start]**Responder**: Can view and triage issues and access response capabilities (excluding Live Terminal). [cite: 212]
* [cite_start]**Viewer**: Can view most features and edit reports. [cite: 212]

### Creating User Groups

[cite_start]It is best practice to create user groups with assigned roles and then add users to these groups. [cite: 195] [cite_start]A user group can only have one role, but users can be part of multiple groups, inheriting the highest level of access from the combination of their roles. [cite: 216, 218]

To create a user group:
1.  [cite_start]Go to **Settings > Configurations > Access Management > User Groups**. [cite: 241]
2.  [cite_start]Click **New Group** and provide a name, description, and assign a role. [cite: 243, 244]
3.  [cite_start]Add users and any nested groups. [cite: 244]
4.  [cite_start](Optional) Configure granular scoping for Assets, Cases and Issues, and Endpoints. [cite: 245]

## Setting Up Authentication

[cite_start]You can authenticate users through the Customer Support Portal (CSP) or by using SAML Single Sign-On (SSO). [cite: 291]

### CSP Authentication

[cite_start]This is the default authentication method. [cite: 295] [cite_start]Users are added to your CSP account and then assigned a role or user group in Cortex Gateway or the tenant to gain access. [cite: 317, 318]

1.  [cite_start]Add users to your CSP account by creating a new user or sending an account registration link. [cite: 330, 331, 336]
2.  [cite_start]Once the user accepts the invitation, they will appear in Cortex Gateway. [cite: 345]
3.  [cite_start]Assign a role to the user directly or add them to a user group. [cite: 346]

### SAML Single Sign-On (SSO) Authentication

[cite_start]SSO allows users to authenticate using your organization's Identity Provider (IdP), such as Okta or Azure AD, that supports SAML 2.0. [cite: 298, 299] [cite_start]This method enforces multi-factor authentication (MFA) at the IdP level and simplifies access management by mapping SAML groups to Cortex XSIAM user groups. [cite: 302, 303]

[cite_start]**Note:** If you use SSO, users must log in directly via the tenant's FQDN, not through the Cortex Gateway. [cite: 356, 472]

#### Setting up Okta as the IdP

1.  [cite_start]**Configure Okta Groups**: Create groups in Okta that correspond to user groups in Cortex XSIAM. [cite: 418]
2.  [cite_start]**Copy SSO and URI values from Cortex XSIAM**: In Cortex XSIAM, navigate to `Settings > Configurations > Access Management > Authentication Settings` and copy the `Single Sign-On URL` and `Audience URI (SP Entity ID)`. [cite: 425, 429]
3.  **Configure the Application in Okta**: Create a new application in Okta and paste the values copied from Cortex XSIAM into the SAML settings. [cite_start]Configure the required attribute statements (FirstName, LastName, Email, memberOf). [cite: 433, 434, 437, 445]
4.  [cite_start]**Copy IdP values from Okta**: Copy the `Identity Provider Single Sign-On URL`, `Identity Provider Issuer`, and the `X.509 Certificate` from Okta. [cite: 449]
5.  [cite_start]**Configure Cortex XSIAM SSO Integration**: Paste the values from Okta into the SSO Integration settings in Cortex XSIAM. [cite: 457]
6.  [cite_start]**Map SAML Groups**: In Cortex XSIAM, edit your user groups and add the corresponding Okta group names in the `SAML Group Mapping` field. [cite: 465]
7.  [cite_start]**Test the SSO Login**: Go to your tenant URL and click `Sign-In with SSO`. [cite: 470]

#### Setting up Azure AD as the IdP

1.  [cite_start]**Configure Azure AD Security Groups**: Create security groups in Azure AD that match user groups in Cortex XSIAM. [cite: 485]
2.  [cite_start]**Copy SSO and URI values from Cortex XSIAM**: Follow the same process as with Okta to get the necessary URLs from Cortex XSIAM. [cite: 491, 496]
3.  **Configure the Application in Azure AD**: Create an enterprise application in Azure AD. In the Basic SAML Configuration, paste the URLs from Cortex XSIAM. The `Sign on URL` from XSIAM goes into the `Reply URL` and `Sign on URL` fields in Azure. [cite_start]The `Audience URI` goes into the `Identifier (Entity ID)` and `Relay State` fields. [cite: 503, 505, 506]
4.  **Configure Attributes & Claims**: Add a group claim to send security groups using the `Group ID` as the source attribute. [cite_start]Customize the claim name to `memberOf`. [cite: 509, 510, 512]
5.  [cite_start]**Copy URLs and Certificate from Azure**: Copy the `Login URL`, `Azure AD Identifier`, and download the `Certificate (Base64)`. [cite: 518, 526]
6.  **Copy Object IDs**: For each security group, copy its `Object Id` from Azure AD. [cite_start]This is what you'll use for mapping. [cite: 529, 531]
7.  [cite_start]**Configure Cortex XSIAM SSO Integration**: Paste the values from Azure into the SSO settings in Cortex XSIAM. [cite: 540]
8.  [cite_start]**Map SAML Groups**: Edit your user groups in Cortex XSIAM and paste the corresponding Azure AD group `Object Id`s into the `SAML Group Mapping` field. [cite: 554]
9.  [cite_start]**Test the SSO Login**: Go to your tenant URL and test the login. [cite: 559]
```

-----

### **`04_Agent_Configuration.md`**

```markdown
