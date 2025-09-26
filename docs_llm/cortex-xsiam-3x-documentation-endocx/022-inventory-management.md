## Inventory management

### Asset management

#### 

A comprehensive overview and management interface for all assets in your
environment, ensuring complete visibility, control, and protection.

#### All Assets

The **All Assets** page provides a centralized repository containing
information about all assets within your environment, including
enterprise, multi-cloud, code, and external surfaces. Dedicated asset
modules allow multi-method asset coverage, such as agent, agentless,
logs, from various sources. Having full visibility of assets allows for
timely incident response, effective threat hunting, and attack surface
reduction.

![](media/rId3241.gif){width="4.083333333333333in"
height="2.245833333333333in"}

The asset card provides a unified view of an asset, consolidating
attributes, enhancements, and related cases, issues, or findings. The
**Highlights** section provides an overview of the security risks
associated with the asset. When you click an asset, the asset card opens
in a tab, enabling users to easily switch between multiple assets cards
at the same time.

On each Asset card, you can perform the following actions:

- Leave comments for collaboration, and perform actions on the asset,
  depending on the type.

- Share links for easy access.

- View asset data: see all relevant data and raw information connected
  to the asset.

- Use Copilot for insights and recommendations.

Category, class, and type are terms used to facilitate the organization
and classification of assets.

- **Class**: represents the highest-level grouping of assets based on
  their general purpose or domain. It is a broad classification that
  defines the overall function of the assets.

  - Examples: Compute, Network, Data

- **Category**: represents a more detailed grouping within a class. It
  categorizes assets based on their normalized function or common type,
  regardless of the provider or implementation.

  - Examples: For Compute: Virtual Machine, Container

  - For Data: Bucket, Database

- **Type**: the most specific level of classification and represents the
  provider-specific name for a particular asset within a category. This
  level directly refers to the specific implementation of an asset.

  - Examples: For the Virtual Machine category: EC2 Instance (AWS),
    Compute Engine Instance (GCP).

> **Note**
>
> Keep the following caveats in my mind when working with the Asset
> Inventory page:

- > Instance Administrators are able to view all Inventory views without
  > restrictions, even if Scope Based Access Control (SBAC) roles are in
  > effect. Learn more about
  > [SBAC](#UUID071cdbb66c6a6afe3a671fa79991a0a8).

- > SBAC is not currently available for custom roles with View/Edit
  > permissions on the Inventory page.

- > SBAC based asset group changes may take up to a maximum of five
  > hours to update.

##### Fields on the All Assets page

The following is a list of the fields displayed on the All
Assets page. The assets shown, and their data, depend on your system\'s
licensing.

+-----------------------------------+-------------------------------------------------+
| Column                            | Description                                     |
+===================================+=================================================+
| Name                              | Displays the name that describes the asset.     |
+-----------------------------------+-------------------------------------------------+
| Provider                          | The provider that hosts cloud assets, such as   |
|                                   | GCP, AWS, or Azure.                             |
+-----------------------------------+-------------------------------------------------+
| Class                             | Grouping of assets according to industry        |
|                                   | standards. For example, Compute, Network, and   |
|                                   | Storage.                                        |
+-----------------------------------+-------------------------------------------------+
| Category                          | Asset types given by each cloud vendor are      |
|                                   | normalized into this field.                     |
+-----------------------------------+-------------------------------------------------+
| Type                              | A type is the most specific level of            |
|                                   | classification and represents the               |
|                                   | provider-specific name for a particular asset   |
|                                   | within a category.                              |
|                                   |                                                 |
|                                   | > **Note**                                      |
|                                   | >                                               |
|                                   | > The options available are dependent on        |
|                                   | > your license.                                 |
+-----------------------------------+-------------------------------------------------+
| Region                            | Displays the region as provided by the Cloud    |
|                                   | provider.                                       |
+-----------------------------------+-------------------------------------------------+
| Realm                             | Account ID.                                     |
+-----------------------------------+-------------------------------------------------+
| Tags                              | Users can add information about the asset by    |
|                                   | adding tags.                                    |
+-----------------------------------+-------------------------------------------------+
| Cases breakdown                   | The                                             |
|                                   | [Cases](#UUID7ce7cc737fa2a154a1361f612ff59896)  |
|                                   | attached to the asset.                          |
+-----------------------------------+-------------------------------------------------+
| Critical cases                    | When a critical Case is attached to an asset,   |
|                                   | the number of High or Critical cases appears in |
|                                   | brackets.                                       |
+-----------------------------------+-------------------------------------------------+
| Issues breakdown                  | The                                             |
|                                   | [Issues](#UUID7ce7cc737fa2a154a1361f612ff59896) |
|                                   | attached to the asset.                          |
+-----------------------------------+-------------------------------------------------+
| Critical issues                   | When a critical Issue is attached to an asset,  |
|                                   | the number of high or critical cases appears in |
|                                   | brackets.                                       |
+-----------------------------------+-------------------------------------------------+
| Groups                            | Users can group assets using [asset             |
|                                   | groups](#UUIDa299007a63312a26ae182d415c512454). |
|                                   | The asset group indicates which assets are      |
|                                   | grouped together.                               |
+-----------------------------------+-------------------------------------------------+
| First observed                    | Timestamp of when the asset was first observed  |
|                                   | by the source that reported it.                 |
+-----------------------------------+-------------------------------------------------+
| Last observed                     | Timestamp of when the asset was last observed   |
|                                   | by the source that reported it.                 |
+-----------------------------------+-------------------------------------------------+

##### Asset tabs

Assets are separated by their respective classes. The following table
describes the tabs shown under All Assets.

+-----------------------------------+-----------------------------------+
| Tab                               | Description                       |
+===================================+===================================+
| AI                                | Provides a detailed view of       |
|                                   | AI-related assets, their          |
|                                   | attributes, and associated risks. |
|                                   | Key metrics at the top summarize  |
|                                   | the number of Assets at Risk, AI  |
|                                   | resources across cloud            |
|                                   | environments like AWS, Azure, and |
|                                   | GCP, and the presence of AI       |
|                                   | Assets With Sensitive Data.       |
+-----------------------------------+-----------------------------------+
| All Cloud                         | Asset inventory of cloud accounts |
|                                   | and applications.                 |
+-----------------------------------+-----------------------------------+
| APIs                              | Provides a comprehensive view of  |
|                                   | APIs in your organization,        |
|                                   | including their distribution      |
|                                   | across cloud platforms, exposure  |
|                                   | status, and detailed attributes.  |
|                                   | Key metrics at the top summarize: |
|                                   |                                   |
|                                   | - APIs per Cloud                  |
|                                   |                                   |
|                                   | - APIs per Service                |
|                                   |                                   |
|                                   | - Internet Exposed APIs           |
+-----------------------------------+-----------------------------------+
| Application                       | The Application Inventory         |
|                                   | provides a high-level summary and |
|                                   | detailed insights into the        |
|                                   | applications within your          |
|                                   | environment, including their      |
|                                   | classification, providers, and    |
|                                   | categories.                       |
|                                   |                                   |
|                                   | Click **View Dashboard** to       |
|                                   | navigate to a detailed dashboard  |
|                                   | for deeper analysis.              |
+-----------------------------------+-----------------------------------+
| Code                              | This section provides an overview |
|                                   | of code assets, including all     |
|                                   | code repositories, Infrastructure |
|                                   | as Code (IaC) resources, CI/CD    |
|                                   | pipelines, and software packages. |
|                                   |                                   |
|                                   | Click **View Dashboard** to       |
|                                   | navigate to a detailed dashboard  |
|                                   | for deeper analysis.              |
+-----------------------------------+-----------------------------------+
| Compute                           | The Compute Inventory provides a  |
|                                   | detailed overview of compute      |
|                                   | resources, including virtual      |
|                                   | machines, containers, serverless  |
|                                   | functions, Kubernetes clusters,   |
|                                   | general devices and other compute |
|                                   | assets across your environment.   |
|                                   |                                   |
|                                   | Click **View Dashboard** to       |
|                                   | navigate to a detailed dashboard  |
|                                   | for deeper analysis.              |
+-----------------------------------+-----------------------------------+
| Data                              | The Data Inventory provides an    |
|                                   | overview of data assets and their |
|                                   | associated risks, including the   |
|                                   | number of Assets at Risk, data    |
|                                   | stored in AWS, Azure, and GCP,    |
|                                   | Sensitive Assets, and assets      |
|                                   | marked as Open to the World.      |
+-----------------------------------+-----------------------------------+
| Device                            | Overview of assets with devices   |
|                                   | that have an Cortex XDR agent     |
|                                   | installed.                        |
+-----------------------------------+-----------------------------------+
| External Surface                  | The All External Surface          |
|                                   | Inventory provides an overview of |
|                                   | external-facing assets, including |
|                                   | services versus websites, domains |
|                                   | versus certificates, and their    |
|                                   | distribution across providers.    |
+-----------------------------------+-----------------------------------+
| Identity                          | The Identity section provides an  |
|                                   | overview of identity-related      |
|                                   | assets, including All Identity    |
|                                   | Assets, Human Identities,         |
|                                   | Non-Human Identities, Cloud       |
|                                   | Service Accounts, IAM Groups, and |
|                                   | IAM Policies, giving visibility   |
|                                   | into both user and service-based  |
|                                   | identities and their associated   |
|                                   | permissions.                      |
|                                   |                                   |
|                                   | Click **View Dashboard** to       |
|                                   | navigate to a detailed dashboard  |
|                                   | for deeper analysis.              |
+-----------------------------------+-----------------------------------+
| Network                           | The Network section provides an   |
|                                   | overview of network-related       |
|                                   | assets, including All Network     |
|                                   | resources, Load Balancers,        |
|                                   | Network Interfaces, Security      |
|                                   | Groups, and Subnets, offering     |
|                                   | visibility into the network       |
|                                   | infrastructure and security       |
|                                   | configurations within your        |
|                                   | environment.                      |
|                                   |                                   |
|                                   | Click **View Dashboard** to       |
|                                   | navigate to a detailed dashboard  |
|                                   | for deeper analysis.              |
+-----------------------------------+-----------------------------------+
| Security Services                 | This section provides a complete  |
|                                   | overview of the security services |
|                                   | being actively managed within     |
|                                   | your environment.                 |
+-----------------------------------+-----------------------------------+
| All Other Assets                  | All assets that are               |
|                                   | uncategorized.                    |
+-----------------------------------+-----------------------------------+

##### Container Images

Container Images are fundamental, immutable assets that package
applications and their dependencies for consistent deployment across
cloud environments. Each image is uniquely identified by a SHA256
digest, ensuring content verifiability throughout its lifecycle across
build, deploy, and run stages. You can assign multiple names and tags to
a single container image, allowing you to reference the same image in
various contexts and versions within container registries.

###### Container Image Types

Understanding the different types of container images helps you manage
assets, investigate [findings](#UUID2ae21def97f6fe6bc8ec11ea40ca9c54),
and resolve related issues more efficiently. You can also use this
information to: 

- query assets by image **Type** using [graph
  searches](#UUIDa21fc83d244e6548a636287dac538ba6) or
  [XQL](/document/preview/1282353#UUID-6b616ab5-87bc-e353-5aa5-51e6d5370560)

- [group assets](#UUIDa299007a63312a26ae182d415c512454) based on image
  classification

- apply [cloud workload policies](#UUID2ee0545f21385fb500eb302bfa13bc99)
  to monitor and protect your environment

The following table summarizes each container image type, its purpose,
and key characteristics to help you effectively manage container images.

+-----------------------+-----------------------+-------------------------------------------+
| Image Type            | Description           | Key Characteristics                       |
+=======================+=======================+===========================================+
| Core Image            | Represents the        | **Purpose:**                              |
|                       | immutable content of  |                                           |
|                       | the container image   | - Forms the foundation for other image    |
|                       | itself.               |   types: Build, Registry, and Runtime     |
|                       |                       |   Images.                                 |
|                       |                       |                                           |
|                       |                       | **Properties:**                           |
|                       |                       |                                           |
|                       |                       | - Identified by a unique SHA256 digest.   |
|                       |                       |                                           |
|                       |                       | - Contains file-related findings (for     |
|                       |                       |   example, vulnerabilities, secrets,      |
|                       |                       |   malware).                               |
|                       |                       |                                           |
|                       |                       | - Has no scope and cannot directly be     |
|                       |                       |   part of an asset group or policy, as it |
|                       |                       |   purely represents the image\'s content. |
|                       |                       |                                           |
|                       |                       | - Does **not** include issues.            |
|                       |                       |                                           |
|                       |                       | **Relationships with other image types:** |
|                       |                       |                                           |
|                       |                       | - Can reference another Core Image as its |
|                       |                       |   base, establishing a hierarchical       |
|                       |                       |   relationship between images.            |
|                       |                       |                                           |
|                       |                       | - Can be the \"base of\" another Core     |
|                       |                       |   Image.                                  |
|                       |                       |                                           |
|                       |                       | **User Interaction:**                     |
|                       |                       |                                           |
|                       |                       | - You can query Core Image assets through |
|                       |                       |   XQL.                                    |
|                       |                       |                                           |
|                       |                       | - Find Core Images listed under Inventory |
|                       |                       |   \> All Assets \> Compute \> Container   |
|                       |                       |   Images                                  |
+-----------------------+-----------------------+-------------------------------------------+
| Build Image           | Represents a          | **Purpose:**                              |
|                       | container image       |                                           |
|                       | created from a CI/CD  | - Exists when discovered through CLI      |
|                       | pipeline or build     |   scanning in the platform.               |
|                       | processes.            |                                           |
|                       |                       | - Helps with build traceability and       |
|                       |                       |   integrity verification.                 |
|                       |                       |                                           |
|                       |                       | **Properties:**                           |
|                       |                       |                                           |
|                       |                       | - Includes build metadata such as build   |
|                       |                       |   time, source code repository, and build |
|                       |                       |   environment.                            |
|                       |                       |                                           |
|                       |                       | - Contains findings and issues related to |
|                       |                       |   the build image.                        |
|                       |                       |                                           |
|                       |                       | **Relationships with other image types:** |
|                       |                       |                                           |
|                       |                       | - A Build Image represents a Core Image,  |
|                       |                       |   and a Core Image can be represented by  |
|                       |                       |   a Build Image.                          |
|                       |                       |                                           |
|                       |                       | **User Interaction:**                     |
|                       |                       |                                           |
|                       |                       | - You can query Build Image assets        |
|                       |                       |   through XQL.                            |
|                       |                       |                                           |
|                       |                       | - Find Build Images listed under          |
|                       |                       |   Inventory \> All Assets \> Compute \>   |
|                       |                       |   Container Images                        |
+-----------------------+-----------------------+-------------------------------------------+
| Registry Image        | Represents a          | **Purpose:**                              |
|                       | container image       |                                           |
|                       | stored within a       | - Exists only when discovered through     |
|                       | container registry    |   cloud discovery or registry scanning    |
|                       | (for example, AWS     |   for onboarded registries.               |
|                       | ECR, Azure ACR,       |                                           |
|                       | Google GAR, JFrog     | - Helps manage images within registries   |
|                       | Artifactory, Docker). |   and ensures compliance with registry    |
|                       |                       |   policies.                               |
|                       |                       |                                           |
|                       |                       | **Properties:**                           |
|                       |                       |                                           |
|                       |                       | - Includes registry-specific findings     |
|                       |                       |   (for example, retention policy, FQDN,   |
|                       |                       |   repository name, image tags, manifest   |
|                       |                       |   digests).                               |
|                       |                       |                                           |
|                       |                       | **Relationship with other image types:**  |
|                       |                       |                                           |
|                       |                       | - The container image registry contains   |
|                       |                       |   an image repository, and a Registry     |
|                       |                       |   Image resides within the image          |
|                       |                       |   repository.                             |
|                       |                       |                                           |
|                       |                       | - A Registry Image represents a Core      |
|                       |                       |   Image, and a Core Image can be          |
|                       |                       |   represented by a Registry Image.        |
|                       |                       |                                           |
|                       |                       | **User Interaction:**                     |
|                       |                       |                                           |
|                       |                       | - You can query Registry Image assets     |
|                       |                       |   through XQL.                            |
|                       |                       |                                           |
|                       |                       | - Find Registry Images listed under       |
|                       |                       |   Inventory \> All Assets \> Compute \>   |
|                       |                       |   Container Images                        |
+-----------------------+-----------------------+-------------------------------------------+
| Runtime Image         | Represents container  | **Purpose:**                              |
|                       | images stored,        |                                           |
|                       | running, or defined   | - Exists when discovered through          |
|                       | in a workload asset   |   Agentless Disk scan and XDR agent scan. |
|                       | (such as VMs,         |                                           |
|                       | Kubernetes            | - Ensures that runtime images adhere to   |
|                       | workloads).           |   security policies and provides          |
|                       |                       |   visibility into their deployment and    |
|                       |                       |   operational state.                      |
|                       |                       |                                           |
|                       |                       | **Properties:**                           |
|                       |                       |                                           |
|                       |                       | - Contains findings related to its        |
|                       |                       |   deployment and operational state, such  |
|                       |                       |   as configuration deviations and         |
|                       |                       |   security policy violations.             |
|                       |                       |   File-related findings are derived from  |
|                       |                       |   the connected Core Image.               |
|                       |                       |                                           |
|                       |                       | **Relationships with other images:**      |
|                       |                       |                                           |
|                       |                       | - A Runtime Image \"represents\" a Core   |
|                       |                       |   Image, linking the runtime state to the |
|                       |                       |   immutable content of the image.         |
|                       |                       |                                           |
|                       |                       | - A Core Image is \"represented by\" a    |
|                       |                       |   Runtime Image, ensuring that any        |
|                       |                       |   findings related to the image files are |
|                       |                       |   considered during runtime evaluations.  |
|                       |                       |                                           |
|                       |                       | **User Interactions:**                    |
|                       |                       |                                           |
|                       |                       | - You can query Runtime Image assets      |
|                       |                       |   through XQL.                            |
|                       |                       |                                           |
|                       |                       | - Find Runtime images listed under        |
|                       |                       |   Inventory \> All Assets \> Compute \>   |
|                       |                       |   Container Images                        |
+-----------------------+-----------------------+-------------------------------------------+

###### Container Images asset inventory

The Container Images asset inventory provides a centralized view of all
scanned container images and their details across your environments. The
platform enables efficient tracking and management of your container
images, ensuring compliance with security and governance standards. 

You can directly access container image issues and findings within the
inventory, which allows you to prioritize and remediate them without
navigating to a separate remediation section.

To access container image assets:

1.  Go to **Inventory**.

2.  All Assets \> Compute \> Container Images.

###### Explore the container images inventory

The **Container Image** assets inventory includes a dashboard with
**OS Distro**, **OS Version**, and **Base Image** widgets displayed by
default, and an inventory table. Selecting a widget automatically
filters the inventory table based on the widget\'s criteria.

The inventory table includes the following fields. You can filter
results by any heading and value:

+-----------------------------------+-----------------------------------+
| Fields                            | Description                       |
+===================================+===================================+
| **Asset ID**                      | A unique identifier assigned to   |
|                                   | the image.                        |
+-----------------------------------+-----------------------------------+
| **Provider**                      | The provider that hosts cloud     |
|                                   | assets, such as **AWS**,          |
|                                   | **Azure**, **Docker**, **GCP**,   |
|                                   | **JFrog Artifactory**, **OCI**,   |
|                                   | and **Not Applicable** (for core  |
|                                   | images).                          |
+-----------------------------------+-----------------------------------+
| **Asset Type**                    | Types of container images:        |
|                                   |                                   |
|                                   | - **Core Image**: Represents the  |
|                                   |   immutable content of the        |
|                                   |   container image itself. It is   |
|                                   |   identified by a unique SHA256   |
|                                   |   digest, ensuring that any       |
|                                   |   alteration to its content       |
|                                   |   results in the creation of a    |
|                                   |   new Core Image.                 |
|                                   |                                   |
|                                   | - **Build Image**: Represents the |
|                                   |   image created from a pipeline   |
|                                   |   or build process, capturing the |
|                                   |   context of the build            |
|                                   |   environment and time.           |
|                                   |                                   |
|                                   | - **Registry Image**: Represents  |
|                                   |   the container image stored in   |
|                                   |   an artifact repository within a |
|                                   |   container registry. It exists   |
|                                   |   only when discovered as part of |
|                                   |   cloud discovery or registry     |
|                                   |   scan for onboarded registries.  |
|                                   |                                   |
|                                   | - **Runtime Image**:  Represents  |
|                                   |   container images stored,        |
|                                   |   running, or defined in a        |
|                                   |   workload asset (VMs, Kubernetes |
|                                   |   workloads), identified by its   |
|                                   |   name and digest in the runtime  |
|                                   |   environment.                    |
+-----------------------------------+-----------------------------------+
| **Name**                          | The container image name.         |
+-----------------------------------+-----------------------------------+
| **Image Type**                    | Image file format. For example,   |
|                                   | Docker and OCI formats.           |
+-----------------------------------+-----------------------------------+
| **Image Identifier**              | A unique identifier assigned to a |
|                                   | specific version of a container   |
|                                   | image, used to distinguish it     |
|                                   | from other images and ensure      |
|                                   | consistency across deployments.   |
+-----------------------------------+-----------------------------------+
| **Names**                         | Aggregation of all the observed   |
|                                   | image names over time.            |
+-----------------------------------+-----------------------------------+
| **Realms**                        | Indicates which connector the     |
|                                   | registry belongs to. For managed  |
|                                   | registries (such as ECR, GAR, and |
|                                   | ACR), this field shows the CSP    |
|                                   | account.                          |
+-----------------------------------+-----------------------------------+
| **SDLC Stages**                   | Shows the SDLC stage when the     |
|                                   | image was created. For example,   |
|                                   | Runtime.                          |
+-----------------------------------+-----------------------------------+
| **Base Image**                    | Indicates whether an image is a   |
|                                   | base image (**Yes**) or a         |
|                                   | non-base (derived or              |
|                                   | application-specific) image       |
|                                   | (**No**).                         |
+-----------------------------------+-----------------------------------+
| **Base Image**                    | Displays the number of images     |
|                                   | derived from the base image.      |
|                                   |                                   |
|                                   | For example, **Base image \|2**   |
|                                   | indicates there are two images    |
|                                   | derived from it.                  |
+-----------------------------------+-----------------------------------+
| **Tags**                          | Labels assigned to container      |
|                                   | images to identify and reference  |
|                                   | specific versions or variants.    |
+-----------------------------------+-----------------------------------+
| **Digest**                        | A unique, content-based SHA256    |
|                                   | hash that immutably identifies a  |
|                                   | specific container image version. |
+-----------------------------------+-----------------------------------+
| **Architecture**                  | The CPU architecture for which    |
|                                   | the container image is built. For |
|                                   | example, amd64, arm64, x86        |
+-----------------------------------+-----------------------------------+
| **Image OS**                      | The base operating system         |
|                                   | environment version the container |
|                                   | image uses. For example, 12.10    |
+-----------------------------------+-----------------------------------+
| **OS Distribution**               | The operating system (OS)         |
|                                   | distribution name. For example,   |
|                                   | Debian.                           |
+-----------------------------------+-----------------------------------+
| **Operating System**              | Operating system details of the   |
|                                   | image. For example, Linux.        |
+-----------------------------------+-----------------------------------+
| **OS Version**                    | The version or release number of  |
|                                   | that OS distribution. For         |
|                                   | example, 20.04 for Ubuntu)        |
+-----------------------------------+-----------------------------------+
| **OS Concat**                     | Shows combined values of OS       |
|                                   | distribution and OS version. For  |
|                                   | example, Debian 11 or Debian      |
|                                   | bookworm.                         |
+-----------------------------------+-----------------------------------+
| **Size**                          | Size of the container image in    |
|                                   | bytes.                            |
+-----------------------------------+-----------------------------------+
| **First Observed**                | Timestamp of when the image was   |
|                                   | first observed by the source that |
|                                   | reported it.                      |
+-----------------------------------+-----------------------------------+
| **Last Observed**                 | Timestamp of when the image was   |
|                                   | last observed by the source that  |
|                                   | reported it.                      |
+-----------------------------------+-----------------------------------+

###### Expanded Container Images asset information

On the **Container Image** page, select an asset in the inventory table
to open a detailed **Asset card**, which provides additional, in-depth
information about the asset. The information is organized into tabs,
including an **Overview** tab (displayed by default) that provides
highlights and a general summary, while contextual tabs focus on
particular properties of the asset. The card also includes details about
detected risks, allowing you to explore them directly from the asset
inventory. You can also perform actions on the asset using the
**Actions** menu.

###### Container Image summary

The **Container Image Summary**, displayed at the top of the card,
provides concise details about the image, such as its type, cloud
provider, and name.

###### Overview

The **Overview** tab summarizes container image **Highlights**,
**Properties**, **Scan information** details, and **Relationships**
between the current image and its **Core Image**.

**Highlights** include:

- **Critical/High issues**: An aggregation of critical and high issues
  associated with the container image. Clicking on this property
  redirects you to the **Issues** page, filtered by specific asset and
  severity level.

- **Visibility timeline**: When the container image was first and last
  detected.

- **Risk summary**: The risks associated with the container image,
  grouped by category (cases, issues, and findings). Each category
  includes the total number of associated risks, as well as a specific
  count for each severity level.

**Properties** include:

- Includes identifying information and cloud location of the container
  image: **Name**, **ID** (such as ARN in AWS), cloud **Provider**,
  cloud **Region**, and **Account ID**.

- Additional details: Includes **Asset category**, **Asset Groups**,
  **Image Digest**, **Base image** name along with its URL (if present),
  and **Image** name.

**OS/ARCH** includes:

**OS information**:  Includes OS related information for that container
image, such as **OS distro**, **OS release**, **size** in bytes,
**operating system**, **Docker Labels**, and the type of
**architecture** the image is compatible with.

**Scan management** includes:

Information about the last scan, including scanner name, version, and
scan status for vulnerabilities, compliance, secrets, and malware.

**Relationships** include:

Information about how each logical image (**Build**, **Registry**,
**Runtime**) is linked to the **Core Image** it represents, ensuring
that any findings related to the **Core Image** are contextualized
within the scope of the logical images.

###### SBOM

The **SBOM** tab displays details about the Software Bill of Materials
(SBOM) generated by the scanning process. Exposed properties include
**Type**, **Name**, **Binary Packages**, **Version**, **Path**, and
**License**.

**Export SBOM**: You can export the entire SBOM, or selected attributes
from any of the tabs in the expanded card: 

Select menu \> file format. Supported formats: `XML`, `json`

###### Vulnerabilities

The **Vulnerabilities** tab provides inventories for **Findings**,
**Packages**, and **Layers**, enabling you to assess potential risks and
prioritize remediation efforts.

**Findings**: Displays a list of findings, along with their associated
**CVE ID** and description, **EPSS** score, **CVSS** score and severity,
**CVE** risk factors, affected software, and fix versions, when
available. 

**Packages**: Displays a list of packages, their name and version, the
total number of vulnerabilities found within each package, a breakdown
of vulnerabilities by severity level and count, their EPSS (Exploit
Prediction Scoring System), which estimates the likelihood of
exploitation; CVSS (Common Vulnerability Scoring System), which rates
the technical severity of the vulnerability; location; base image
vulnerability; and whether a fix is available.

**Layers:** Displays the various layers and their contents within a
container image.

###### Applications

The **Applications** tab identifies any embedded applications within the
image, helping you assess security risks associated with the bundled
software.

##### Kubernetes Cluster

Navigate to Inventory \> All Assets \> Compute \> Kubernetes Cluster for
a Kubernetes clusters assets overview.

To see all resources within a connected cluster, click on the cluster,
then on **Resource Explorer**. The **Resource Explorer** provides
granular visibility of the cluster, helping detect security breaches and
fully understand the cluster\'s components. Disconnected clusters show
no data. Ensure all clusters are connected for maximum protection.

Click **Kubernetes Connectivity Management** to manage the
connector-connectivity of cluster assets, including connector versions,
upgrades, statuses, and more. Here, you can check if a cluster is
connected, view the status, and see the connector version. When a new
version from Palo Alto Networks is available, the user can update the
connector version here.

##### Container Instances

Container Instance assets are dynamically added to the
**Asset Inventory** when a drift is detected between a running container
and its original image. This drift may reveal vulnerabilities,
misconfigurations, compliance violations, or other security risks that
were not present or detected in the base container image, indicating
changes introduced at runtime.

To view all Container Instance assets:

1.  Go to Asset Inventory \> Compute \> Container Instances.

2.  Click a Container Instance asset to open its asset card. The asset
    card provides:

    - Detailed asset properties, such as container ID, image, host,
      cluster, and namespace.

    - Relationships to the container image, pod, workload, and host
      machine.

    - A breakdown of findings and an option to view all associated
      security issues.

    - The ability to export the container\'s image and host data as a
      Software Bill of Materials (SBOM) in JSON or XML format.

##### External Surface assets

The **External Surface** inventory provides a searchable, filterable
view of the internet-facing assets that Cortex XSIAM has discovered and
attributed to your organization, including certificates, domains,
services, and websites.

> **Note**
>
> Requires the Attack Surface Management (ASM) add-on

The following sections provide information about each External Surface
asset type. For information about external IP address ranges, see
[Network configuration](#UUID790a0874d9417120d119c739cb89c08f).

###### Certificates

Certificates (also known as digital or public key certificates) are used
when establishing encrypted communication channels to identify and
authenticate a trusted party. Certificates are typically used for
SSL/TLS, HTTPS, FTPS, SSH, and VPN connections. The most common use of
certificates is for HTTPS-based websites, which enable a web browser to
validate that an HTTPS web server is an authentic website. 

Cortex XSIAM tracks information for each certificate, such as Issuer,
Public key, Public Key Algorithm, Subject, Subject Alternative Names,
Subject Organization, Subject Country, and Subject State. Cortex XSIAM
also tracks the following "cryptographic health" checks for each
certificate:

- Is it self-signed?

- Is wildcard?

- Is domain control validated?

- Expired when scanned?

- Public key bits

- Signature algorithm

These health checks are referred to in the asset details as Certificate
Classifications.

###### Domains

The **External Surface **inventory includes all domains that Cortex
XSIAM has attributed to your organization and whether each domain has a
recent resolution. Root domains and subdomains are displayed as separate
entries in the inventory. However, if an organization owns a wildcard
DNS entry, we group all subdomains of that wildcard that resolve to the
same IP address under that one wildcard domain asset entry. We also
collapse subdomains under the parent domain if we observe more than
1,000 subdomains.

Cortex XSIAM collects domains and DNS data from a combination of active
and passive global collection techniques. For DNS scanning, Cortex XSIAM
sends a BIND version query as the payload. This approach still
identifies DNS servers that are not BIND compliant as their response
informs us of a DNS server's existence.

###### Services

The **External Surface** inventory includes all internet-facing services
attributed to your organization. A service can be any internet-facing
device or software that communicates on
a *domain:port* or *IP:port* pair that responds to scanners on an
application-level protocol over the public internet.

Services include classifications which are fingerprint-based identifiers
of software, technologies, and behaviors observed on the service.
Classifications can be either active or inactive based on the most
recent observations of a service. In addition to classifications,
services will also include banner, response, and header information
from Cortex XSIAM data collection.

####### Services field descriptions

The **Services** table includes the fields.

+-----------------------------------+-------------------------------------+
| Field                             | Description                         |
+===================================+=====================================+
| Active classifications            | Facts that have been inferred about |
|                                   | each of your services by examining  |
|                                   | a response for fingerprints.        |
|                                   | Classifications cover a variety of  |
|                                   | details including:                  |
|                                   |                                     |
|                                   | - Identifying specific software and |
|                                   |   versions.                         |
|                                   |                                     |
|                                   | - Configuration details of note.    |
|                                   |                                     |
|                                   | - Identifying when the services do  |
|                                   |   not implement best practices like |
|                                   |   web security headers or           |
|                                   |   certificate security standards.   |
|                                   |                                     |
|                                   | Some Classifications merely note    |
|                                   | that a fact is true or false, like  |
|                                   | **Missing Cache Control Header**.   |
|                                   | Other Classifications provide       |
|                                   | additional information, such as a   |
|                                   | version number for "nginx Server".  |
|                                   | These details are viewable in the   |
|                                   | services table and on the details   |
|                                   | page for the service by clicking    |
|                                   | the name of the service in the      |
|                                   | **All External Services** table.    |
+-----------------------------------+-------------------------------------+
| Business units                    | A Business Unit is a designation to |
|                                   | classify assets. Cortex XSIAM       |
|                                   | tracks business units as a means to |
|                                   | identify owning organizations of    |
|                                   | these assets. Business units become |
|                                   | extremely important when an         |
|                                   | organization has subsidiaries and   |
|                                   | groups established through M&A      |
|                                   | activities.                         |
+-----------------------------------+-------------------------------------+
| Discovery type                    | Services are identified with one of |
|                                   | the following two discovery types,  |
|                                   | depending on the level of           |
|                                   | confidence Cortex XSIAM has in      |
|                                   | attributing it to your              |
|                                   | organization.                       |
|                                   |                                     |
|                                   | - **Directly Discovered**: services |
|                                   |   that are definitively associated  |
|                                   |   with an asset that belongs to     |
|                                   |   your organization.                |
|                                   |                                     |
|                                   | <!-- -->                            |
|                                   |                                     |
|                                   | - Examples include:                 |
|                                   |                                     |
|                                   |   - It is hosted on one of your     |
|                                   |     on-prem IP ranges.              |
|                                   |                                     |
|                                   |   - The service advertises one of   |
|                                   |     your organization\'s            |
|                                   |     certificates.                   |
|                                   |                                     |
|                                   |   - It is on a managed cloud        |
|                                   |     resource that is known to be    |
|                                   |     yours.                          |
|                                   |                                     |
|                                   | <!-- -->                            |
|                                   |                                     |
|                                   | - **Colocated with your Services**: |
|                                   |   the service is running on the     |
|                                   |   same IP as a different            |
|                                   |   directly-discovered service.      |
|                                   |                                     |
|                                   | <!-- -->                            |
|                                   |                                     |
|                                   | - In a multi-tenant hosting         |
|                                   |   environment, these co-located     |
|                                   |   services may belong to other      |
|                                   |   organizations but can sometimes   |
|                                   |   pose adjacency risks to your      |
|                                   |   services hosted on that IP. If    |
|                                   |   your organization has             |
|                                   |   "single-tenant environment only"  |
|                                   |   policies with 3rd party hosting   |
|                                   |   providers, you can use this       |
|                                   |   functionality to identify         |
|                                   |   possible violations of that       |
|                                   |   policy.                           |
+-----------------------------------+-------------------------------------+
| Domain                            | The most recent domain on which the |
|                                   | service is running.                 |
+-----------------------------------+-------------------------------------+
| Externally detected providers     | The provider of the asset is        |
|                                   | determined by an external           |
|                                   | assessment.                         |
+-----------------------------------+-------------------------------------+
| Externally inferred CVEs          | Externally Inferred CVEs are        |
|                                   | identified by comparing the product |
|                                   | name and version of active service, |
|                                   | if identifiable, with CVES for      |
|                                   | those products in the National      |
|                                   | Vulnerability Database. Additional  |
|                                   | investigation may be required to    |
|                                   | confirm if the CVE is present.      |
|                                   |                                     |
|                                   | Click on the service to view the    |
|                                   | service details, which include the  |
|                                   | complete list of all the externally |
|                                   | inferred CVEs.                      |
+-----------------------------------+-------------------------------------+
| Externally inferred vulnerability | This score is based on the highest  |
| score                             | CVSSv3 score for Externally         |
|                                   | Inferred CVEs on this service. If   |
|                                   | there is no CVSSv3 score for the    |
|                                   | CVE, then the CVSSv2 score is used. |
|                                   |                                     |
|                                   | This field applies only to services |
|                                   | with Externally Inferred CVEs.      |
+-----------------------------------+-------------------------------------+
| First observed                    | When the asset was first observed   |
|                                   | via any of the sources.             |
+-----------------------------------+-------------------------------------+
| Inactive Classifications          | Previously observed classifications |
|                                   | that are no longer observed.        |
+-----------------------------------+-------------------------------------+
| IP addresses                      | Array column specifying a list of   |
|                                   | IPs associated with this asset.     |
+-----------------------------------+-------------------------------------+
| Is active                         | - **Yes**--- indicates the service  |
|                                   |   is active, which means that the   |
|                                   |   service has been observed         |
|                                   |   recently.                         |
|                                   |                                     |
|                                   | - **No**--- indicates the service   |
|                                   |   is inactive, which means Cortex   |
|                                   |   XSIAM no longer sees it on the    |
|                                   |   internet.                         |
+-----------------------------------+-------------------------------------+
| Last observed                     | When the asset was last observed    |
|                                   | via any of the sources.             |
+-----------------------------------+-------------------------------------+
| Port                              | The most recent port for the        |
|                                   | service.                            |
+-----------------------------------+-------------------------------------+
| Protocol                          | The application-level protocol on   |
|                                   | the public internet over which      |
|                                   | Cortex XSIAM validated the service. |
+-----------------------------------+-------------------------------------+
| Service name                      | The service type along with the     |
|                                   | specific *domain:port* or *IP:port* |
|                                   | pair for the service.               |
+-----------------------------------+-------------------------------------+
| Service type                      | The type of server or software for  |
|                                   | the service.                        |
+-----------------------------------+-------------------------------------+

###### Websites

Cortex XSIAM websites data extends Attack Surface Management (ASM)
protection by identifying insecure websites, web components, and
technologies running on your managed and unmanaged web assets. Cortex
XSIAM scans your public-facing websites, creating a continuously updated
inventory of your web assets, including the server software and other
technologies powering your web applications.

Websites data in Cortex XSIAM enables you to accomplish the following:

- Develop a single source of truth for all of your organization\'s web
  inventory

- Track and monitor your risk due to third-party libraries

- Continuously discover and monitor external web application inventory
  and third-party technologies

- Identify insecure and misconfigured websites, vulnerable technologies,
  and dependencies

- Improve security ratings by identifying sites failing security best
  practices

**The difference between websites and external services**

In Cortex XSIAM, external services are public-facing network services;
for example, an RDP server or an HTTP server. Websites represent the
content and the software stack that was used to generate the website.

An HTTP service represents a single HTTP server (on-prem) or a cohesive
group of HTTP servers (cloud). A website can be served by a single HTTP
server or by multiple HTTP servers. Some of these HTTP servers could be
hosted by a cloud provider, others on-prem. Generally, the relationship
between HTTP services and websites can be described as follows:

- A website is supported by one or more HTTP services.

- A cloud HTTP service serves a single website.

- An on-prem HTTP service serves multiple websites, potentially
  hundreds.

**The difference between websites and domains**

A domain is simply the registration of a domain (for example, your
organization might own www.example.com). You can have a domain without a
website behind it. You can also have a domain that does not resolve to
an IP address (which means it does not have a website behind it). Cortex
XSIAM includes websites with a domain name or an IP address.

####### Websites field descriptions

The Websites page lists your websites in a table format that can be
sorted, filtered, and downloaded. Some of the key fields are described
in the table below.

+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| Authentication                    | Detected authentication method.   |
|                                   | Results could be none, form based |
|                                   | authentication (e.g. user ID and  |
|                                   | password), or a single-sign on    |
|                                   | method.                           |
+-----------------------------------+-----------------------------------+
| Business Units                    | Business unit this website is     |
|                                   | associated with.                  |
+-----------------------------------+-----------------------------------+
| Externally Detected Providers     | Hosting provider.                 |
+-----------------------------------+-----------------------------------+
| Failed Security Assessments       | Which of the security best        |
|                                   | practices the website failed.     |
+-----------------------------------+-----------------------------------+
| First Observed                    | When the website was first        |
|                                   | observed.                         |
+-----------------------------------+-----------------------------------+
| Host                              | Domain or IP of the website host. |
|                                   |                                   |
|                                   | - A closed lock indicates HTTPS.  |
|                                   |                                   |
|                                   | - An open lock indicates HTTP.    |
+-----------------------------------+-----------------------------------+
| HTTP Type                         | HTTPS, HTTP redirecting to HTTPS, |
|                                   | or HTTP.                          |
+-----------------------------------+-----------------------------------+
| IP Addresses                      | IP addresses associated with this |
|                                   | website.                          |
+-----------------------------------+-----------------------------------+
| Is Active                         | **Yes **--- Indicates the website |
|                                   | is active, which means it has     |
|                                   | been observed recently.           |
|                                   |                                   |
|                                   | **No **--- Indicates the website  |
|                                   | is inactive, which means Cortex   |
|                                   | Xpanse no longer sees it on the   |
|                                   | internet or it is no longer       |
|                                   | attributed to your organization.  |
+-----------------------------------+-----------------------------------+
| Last Observed                     | When the website was most         |
|                                   | recently observed in a Cortex     |
|                                   | Xpanse scan.                      |
+-----------------------------------+-----------------------------------+
| Port                              | Port for the website.             |
+-----------------------------------+-----------------------------------+
| Site Category                     | The inferred business purpose of  |
|                                   | the website based on the          |
|                                   | technologies used on that         |
|                                   | website. Full list of site        |
|                                   | categories is Ecommerce,          |
|                                   | Advertising, Affiliate Programs,  |
|                                   | Appointment scheduling, Blogs,    |
|                                   | CMS, CRM, Development,            |
|                                   | Documentation, Issue Tracker,     |
|                                   | LMS, Reservations & Delivery,     |
|                                   | Recruitment & Staffing.           |
|                                   |                                   |
|                                   | If a technology doesn\'t fit into |
|                                   | one of the listed categories,     |
|                                   | this field will be blank.         |
+-----------------------------------+-----------------------------------+
| Technologies                      | Any technologies detected on the  |
|                                   | website.                          |
+-----------------------------------+-----------------------------------+
| Third Party Script Domains        | Third-party domains that serve    |
|                                   | the scripts (not the scripts      |
|                                   | themselves).                      |
+-----------------------------------+-----------------------------------+
| Website ID                        | Unique ID associated with the     |
|                                   | website.                          |
+-----------------------------------+-----------------------------------+

####### Website details

Click a row in the **Websites **table to open the details page for that
website. The following sections describe the information on the website
details page.

**Site Details, Site Categories, Site Deployment Details**

Summarizes key information about the security of the website.

**Most Recent Screenshot**

A screenshot and link to the website to make it easier to investigate
issues. If you don\'t see a screen shot, the website may have been down
when we scanned the page or that access was blocked for our scanner (in
which case you probably won\'t see any technologies listed under
Technologies Used either). If the screenshot is incomplete (a blank or
invalid layout), the page may have loaded too slowly---we take the
screenshot six seconds after we request the page.

**Security Best Practices Analysis**

Provides an at-a-glance look at whether the website is following broadly
accepted security best practices.

We perform only the relevant security best practice assessments on each
website. For example, if a website redirects somewhere else, many of the
security assessments are performed on the website the user is redirected
to; only the Has HTTPS Enabled and Protocol Downgrade assessments are
performed on the original website. And some security assessments don't
make sense on non-HTTPS websites (e.g. mixed content and HSTS header),
so those assessments are not performed.

Some security best practice assessments are performed only on webpages
without \"transient errors\". We consider a page to have a transient
error if the HTTP status code is 405, 407, 408, 409 or greater than 411.
In this case, we assume this is not a normal condition of the website
and visiting the page later or in different conditions would yield a
different result.

If we have no matching observation for an assessment, the assessment
will not be displayed. For example, if https://acme.com has a single
page with a 404 status code, the Mixed Content assessment would be
performed (404 is not a transient error) but the X-Frame-Options
assessment would not be.

The table below lists each of the security best practices, which
websites and webpages the analysis is performed on, and the criteria we
use to determine whether the website Passes or Fails the assessment.

+------------------------------------------------+-----------------+-----------------+-----------------------------+
| Website Security Best Practice                 | Performed on    | Performed on    | Pass/Fail Criteria          |
|                                                | these websites  | these pages     |                             |
+================================================+=================+=================+=============================+
| **Has HTTPS Enabled**                          | All websites    | All             | Passes if the website is    |
|                                                |                 |                 | accessed over TLS or        |
|                                                |                 |                 | redirects to an HTTPS       |
|                                                |                 |                 | website.                    |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Secure Forms**                               | HTTPS websites  | Pages without   | Fails if we find an HTML    |
|                                                | that do not     | transient       | form with an action to an   |
|                                                | always redirect | errors          | insecure website. This      |
|                                                |                 |                 | applies only to static      |
|                                                |                 |                 | forms and will not detect   |
|                                                |                 |                 | dynamically rendered forms. |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **No Mixed Content**                           | HTTPS websites  | Pages without   | Fails if we find a page     |
|                                                | that do not     | transient       | that is using a resource    |
|                                                | always redirect | errors          | (image, stylesheet, script  |
|                                                |                 |                 | but not just a \<a\> link)  |
|                                                |                 |                 | loaded over HTTP.           |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Protocol Downgrade**                         | All websites    | All             | Fails if we find a          |
|                                                |                 |                 | transition from HTTPS to    |
|                                                |                 |                 | HTTP in the redirect chain. |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Sets Valid X-Frame-Options Header**          | Websites that   | Pages with 2xx  | Fails if:                   |
|                                                | do not always   | status code     |                             |
|                                                | redirect        |                 | - X-Frame-Options header is |
|                                                |                 |                 |   not empty and is neither  |
|                                                |                 |                 |   DENY or SAMEORIGIN        |
|                                                |                 |                 |                             |
|                                                |                 |                 | - Content-Security-Policy   |
|                                                |                 |                 |   header is not set or      |
|                                                |                 |                 |   syntactically invalid     |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Sets Valid X-Content-Type-Options Header**   | Websites that   | Pages with 2xx  | Fails if                    |
|                                                | do not always   | status code     | X-Content-Type-Options is   |
|                                                | redirect        |                 | not set or not "nosniff"    |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Sets valid Content-Type Header**             | Websites that   | Pages with 2xx  | Fails if Content-Type is    |
|                                                | do not always   | status code     | not set or set to an        |
|                                                | redirect        |                 | invalid value.              |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Sets HTTP Strict Transport-Security-Header** | HTTPS websites  | Pages without   | Fails if there is no        |
|                                                | that do not     | transient       | "Strict-Transport-Security" |
|                                                | always redirect | errors          | header.                     |
+------------------------------------------------+-----------------+-----------------+-----------------------------+
| **Sets valid Referrer-Policy Header**          | Websites that   | Pages without   | Fails if Referrer-Policy    |
|                                                | do not always   | transient       | header not set or set to an |
|                                                | redirect        | errors          | invalid value.              |
+------------------------------------------------+-----------------+-----------------+-----------------------------+

**Technologies Used**

List of the technologies used on your website.

**HTML Form Analysis**

List of login forms. Login forms are only detected in a static
environment, so if the form is created by JavaScript, it will not be
detected. Only login forms are displayed in analysis.

**Domain Details**

Information about the website domain, including a link to the domain in
the **Inventory**.

**Third Party Resources**

List of the scripts and CSS loaded from domains that are not owned by
your organization.

**Other Websites Hosted with This Website**

List of other websites owned by your organization and hosted on the same
IP addresses.

**Services Hosting This Website**

List of services hosting the website in the last 30 days.

**GeoMap**

Map indicating the IP region of the website.

**Externally Inferred CVEs**

Externally inferred CVEs associated with the technologies used on your
website.

####### Websites dashboard

The **Websites **dashboard provides an overview of the security of your
entire web attack surface. It enables you to continuously monitor your
web resources at a high level and drill down into the details as needed.
Some of the key data displayed on the **Websites **dashboard includes
the following:

- Website security misconfigurations and best practice failures

- Websites using HTTP and HTTPS

- Authentication providers, server software, technologies detected

- A breakdown of your websites by category

- Third-party technologies used on your websites

- Privacy-impacting packages your websites are using

<!-- -->

- Privacy-impacting packages are technologies that track users. The
  \"privacy-impacting\" designation is based on the purpose of the
  technology and is not an evaluation of whether the technology itself
  has privacy problems. Any technology in the following categories is
  considered "privacy impacting":

  - Analytics

  - Geolocation

  - Browser fingerprinting

  - Loyalty and rewards

  - Marketing automation

  - Referral marketing

  - Retargeting

###### External Surface attribution evidence

Cortex XSIAM provides attribution information about each asset in your
External Surface inventory, so you know at-a-glance why we believe an
asset belongs to your organization.

To review the attribution evidence for an asset, click on an asset in
the External Surface inventory to open the asset details panel, and find
the **Asset Attribution Evidence** section.

For each asset, Cortex XSIAM provides the seed term that was used to
attribute the asset to your organization and the specific piece of scan
data that we matched to the seed term. A seed term is a text string that
our research team generated and associated with your organization. For
example, seed terms for Cortex Xpanse might include: Xpanse, Cortex,
Cortex Xpanse, Palo Alto Networks, PANW, PAN, etc.  We use machine
learning models as well as manual research to match the seed terms with
our scan data to attribute assets to your organization.

Depending on the asset type and scan data, most assets will have one or
more pieces of attribution evidence. Assets that don\'t have attribution
evidence do not have a seed term match. The following are reasons we may
not have a seed term match: 

- The domain or IP range is provided by the customer and cannot be
  externally validated using public data.

- The domain registration information is redacted, blank, or private. We
  attribute these through manual routing.

- The domain is attributed by an associated website (e.g. example.com is
  attributed to Example Corp because the website at www.example.com
  shows clear evidence of belonging to Example Corp).

- The domain is attributed based on a DNS record.

If you have questions about a specific asset, reach out to Customer
Success.

#### Network configuration

Network asset visibility is a crucial investigative tool for discovering
rogue devices and preventing malicious activity within your network. The
number of managed and unmanaged assets in your network provides vital
information for assessing security exposure and tracking network
communication effectively.

Cortex XSIAM **Network Configuration** accurately represents your
network assets by collecting and analyzing the following network
resources:

- User-defined IP Address Ranges and Domain Names associated with your
  internal network.

- EDR data collected by Firewall Logs.

- Cortex XSIAM Agent Logs.

- ARP Cache

- **Broker VM Network Mapper**

- **Pathfinder Data Collector**

In addition to the network resources, Cortex XSIAM allows you to
configure a **Windows Agent Profile** to scan your endpoints using Ping.
This scan provides updated identifiers of your network assets, such as
IP addresses and OS platforms. The scan is automatically distributed by
Cortex XSIAM to all the agents configured in the profile and cannot be
initiated by request.

With the data aggregated by Cortex XSIAM **Network Configuration**, you
can locate and manage your assets more effectively and reduce the amount
of research required to:

- Distinguish between assets managed and unmanaged by a Cortex XSIAM
  agent.

- Identify assets that are part of your internal network.

- Monitor network data communications both within and outside your
  network.

##### Configure your network parameters

Internal IP address ranges and domain names must be defined in order to
track and identify assets in the network. This enables Cortex XSIAM to
analyze, locate, and display your network assets.

###### Define internal IP address ranges

1.  In Cortex XSIAM, select Assets Network Configuration.

2.  Define an IP address range.

- By default, Cortex XSIAM creates **Private Network** ranges that
  specify reserved industry-approved ranges. These ranges can only be
  renamed.

  To **Add New Range**, select either:

  - **Create New**.

    i.  In the **Create IP Address Range** dialog box, enter the IP
        address **Name** and **IP Address, Range or CIDR values**.

    - > **Note**

      > You can add a range that is fully contained in an existing
      > range, however, you cannot add a new range that partially
      > intersects with another range.

    ii. Click **Save**.

  - **Upload from File**

    i.  In the **Upload IP Address Range** dialogue box, drag and drop
        or search for a CSV file listing the IP address ranges.
        **Download example file** to view the correct format.

    ii. Click **Add**.

###### View external IP address ranges

> **Note**
>
> Viewing external IP address ranges requires the Attack Surface
> Management add-on.

An external IP address range is an IPv4 or IPv6 address range that
Cortex XSIAM has discovered through ASM scans and attributed to your
organization. The complete list of external IP Address Ranges can be
viewed on the **External IP Address Ranges** page, as explained in the
following steps. External IP address range information is also available
on asset details pages when an external IP address is used to attribute
an asset to your organization.

1.  In Cortex XSIAM, select Assets \> Network Configuration \> IP
    Address Ranges \> External IP Address Ranges.

2.  Review your external IP address ranges, as needed.

- The IP Address Ranges table displays the following fields:

  - First IP Address: First IP address value of the defined range

  - Last IP Address: Last IP address value of the defined range.

  - IPs Count: Number of IP addresses in the range.

  - Active Responsive IPS count: Number of IP addresses in the range
    that are currently active and responsive.

  - Business Units: Business units associated with this external IP
    range.

  - Date Added: The first time that Cortex XSIAM identified this IP
    Range.

  - Organization Handles: Unique identifiers for the organizations
    managing the IP range.

3.  Display details about an external IP range by selecting a row in the
    table.

- The detailed view is displayed to the right of the table. External IP
  address range details include registration data, which Cortex XSIAM
  pulls from public RIR (Regional Internet Registries) databases.
  Registration data includes network records and organization records.

###### Define domain names

1.  In Cortex XSIAM , select Assets \> Network Configuration \> Internal
    Domain Suffixes.

2.  In the **Internal Domain Suffixes** section, **+Add** the domain
    suffix you want to include as part of your internal network. For
    example, `acme.com`.

3.  Select ![](media/rId3274.png){width="0.14583333333333334in"
    height="0.20833333333333334in"} to add to the **Domains List**.

###### IP address ranges fields

  -----------------------------------------------------------------------
  FIELD                               DESCRIPTION
  ----------------------------------- -----------------------------------
  Range Name                          Name of the IP address range
                                      defined.

  First IP Address                    First IP address value of the
                                      defined range.

  Last IP Address                     Last IP address value of the
                                      defined range.

  Active Assets                       Number of assets within the defined
                                      range that have reported Cortex
                                      Agent logs or appeared in your
                                      Network Firewall Logs.

  Active Managed Assets               Number of assets within the defined
                                      range reported Cortex XSIAM Agent
                                      logs.

  Modified By                         Username of the user who last
                                      changed the range.

  Modification Time                   The timestamp shows when this range
                                      was last changed.
  -----------------------------------------------------------------------

#### Asset Groups

By grouping assets based on shared attributes, you can address them
collectively. This enables more efficient bulk actions and simplifies
both filtering and scoping within the inventory and across the platform.

To create an **Asset Group**:

1.  Navigate to Inventory \> Assets \> Groups \> Add Group.

2.  Define a meaningful **Group Name** that represents the group\'s
    purpose to improve usability. You can choose between two types of
    Asset Groups:

    - **Dynamic Groups**: Use the filters **Provider** or **Realm**, to
      group current and future assets that meet the defined criteria.
      Click **Create Dynamic Group** to save.

    - **Static Groups**: Manually select individual assets to include in
      a group. After selection, click **Create Static Group**.

3.  Add an optional **Description** to further clarify.

##### Use cases

Once your **Asset Group** has been defined, you can use it in specific
areas of the platform for the following:

- Enrich asset data: Add information to a set of assets that isn\'t
  directly stored on the asset itself.

- Reuse asset groups: Reference the same group across different areas of
  Cortex XSIAM, for example, in Policies and Rules.

> **Note**
>
> When you create or edit an Asset Group, the changes are applied
> immediately to new assets and to existing assets that have been
> updated. However, it may take a few hours for the changes to appear on
> existing assets that have not been updated.

#### Asset Roles

> **Note**
>
> Asset Roles are available only if the Identity Threat Module add-on is
> enabled.

Cortex XSIAM continuously analyzes your users and endpoints, and
automatically classifies them based on their activities under asset
roles, for example, Domain Controller, Administrator, and Executive
User. You can edit, add, and fine-tune the assets associated with each
asset role at any time.

Fine-tuned asset roles aid Cortex XSIAM Analytics in the following
areas.

- Enhancement of the accuracy of the analytics that runs on assets,
  enabling better detection of uncommon activities by the asset based on
  the baseline for the asset role.

- Asset role visualization in the Incident view, the User view, and the
  Host view as background information for risk assessment.

- Analysis of User and Host peer groups for score trend comparison over
  selected timelines.

You can add users and endpoints to any asset role manually or by
importing a CSV file.

You can remove users from asset roles manually and override the
automatically detected asset roles.

The tag family for asset roles provides the ability to slice and dice
alerts and incidents. Automated and customizable asset role
classification is based on constant analysis of the users and hosts in
your network. You can edit and manage the [User Asset
Roles](#UUID6533030077f2c79f5550169a76b4c012) and [Host Asset
Roles](#UUID105a6c4cb84c9581211c871e8d8bc7d7) to meet the needs of your
organization.

The **Asset Roles Configuration** page displays the asset roles, their
type, the number of assets that are associated with each asset role, and
the last modification date. On this page, you can refresh the data,
filter it, and change the layout.

To edit an asset role, right-click and select **Edit Asset Role**.
Depending on the type of asset, you can manage the user asset role list
or the endpoint asset role list for the asset role.

##### Manage Asset Roles for Endpoints

> **Note**
>
> Endpoint Role Management is available only if the Identity Threat
> Module add-on is enabled.

The Edit Endpoint Role page enables you to edit the host lists assigned
to asset roles. You may want to exclude some endpoints from certain
asset roles even if Cortex XSIAM automatically detected the endpoint as
having this asset role. For example, if an endpoint is reassigned to
another user and you want their Analytics to be adjusted accordingly.

The **Endpoints** list on the page displays the endpoints classified
under the asset role, if the asset role was assigned automatically or
edited manually for the endpoint, the last modification date, and the
modifier.

To access the **Edit Endpoint Role** page, from
**Asset Role Configuration**, right-click to select the endpoint asset
role and click **Edit Asset Role**.

**Included Endpoints** displays all the endpoints Cortex XSIAM
automatically detects as having this asset role and the endpoints you
specify manually as having this asset role. **Excluded Endpoints**
displays the endpoints that were manually removed from an asset role.
When you exclude an endpoint, it remains in the **Excluded Endpoints**
list and if detected automatically again in the future as having this
role, will not be included in the role list.

If you want to remove an endpoint from the list of endpoints with this
asset role, right-click the endpoint and select **Exclude Endpoint**.
The endpoint is then listed under **Excluded Endpoints** for this asset
role. When you exclude an endpoint from an asset role, by default Cortex
XSIAM also removes the endpoint from the parent asset roles of the
current asset role. To remove the endpoint from the child asset role,
but to leave it in any of its parent asset roles, click
**Advanced Exclusion Settings**, and select **Don\'t Exclude** next to
the name of the parent asset role(s).

To include an **Excluded endpoint** back in the asset role, in the
**Excluded Endpoints** list, right-click the endpoint and select
**Delete Endpoint**. If the endpoint was automatically detected as
having this asset role. it will be added back to the
**Included Endpoints** list again. Otherwise, the next time Cortex XSIAM
scans the assets and automatically detects their asset roles, this
endpoint will be included in the asset role list.

To include endpoints from your system manually in an asset role list, in
the asset role page, click **Add Endpoint**. Select the endpoint from
the displayed endpoint list, which displays the endpoints managed by the
tenant. You can only add endpoints that have the Cortex XSIAM agent
installed on them.

Manually added endpoints are analyzed by Analytics when it runs next and
are displayed in the **Incident view** and the **Host Risk view**.

To delete a manually added endpoint from the Included Endpoints list,
right-click and **Delete Endpoint**.

> **Note**
>
> Deleting a manually added endpoint removes the endpoint from the
> **Included Endpoints** list. If this endpoint is detected
> automatically as having this asset role in the future, it will appear
> in the **Included Endpoints** list.
>
> Excluding a manually added endpoint ensures that even if in the future
> the endpoint is detected as having this asset role, this detection is
> overridden and the endpoint isn\'t included in the asset role.

To change the name of an endpoint, right-click the endpoint name and
**Edit Endpoint**.

##### Manage Asset Roles for Users

> **Note**
>
> User Role Management is available only if the Identity Threat Module
> add-on is enabled.

The Edit User Role page enables you to edit the user lists assigned to
asset roles. You may want to exclude some users from certain asset roles
even if Cortex XSIAM automatically detected the user as having this
asset role. For example, if a user\'s position in the organization is
changed and you want their Analytics to be adjusted accordingly.

The User list on the page displays the users classified under the asset
role, if the asset role was assigned automatically or edited manually
for the user, the last modification date, and the modifier.

To access the Edit User Role page, from **Asset Roles Configuration**,
right-click to select the user asset role and click **Edit Asset Role**.

Some asset roles are nested under parent asset roles which are higher in
the hierarchy of asset roles. The information icon next to the asset
role name provides the name of the parent rule this asset role may be
nested under. For example, an Admin User asset role may be a child asset
role of the parent asset role Sensitive User.

**Included Users** displays all the users Cortex XSIAM automatically
detects as having this asset role and the users you specify manually as
having this asset role. **Excluded Users** displays the users that were
manually removed from an asset role. When you exclude a user from an
asset role, it remains in the **Excluded Users** list and even if it\'s
detected automatically again in the future as having this asset role, it
will not be included in the asset role list.

If you want to remove a user from the list of users with this asset
role, right-click the user and select **Exclude User**. The user is then
listed under **Excluded Users** for this asset role. When you exclude a
user from an asset role, by default Cortex XSIAM also removes the user
from the parent asset roles of the current asset role. To remove the
user from the child asset role, but to leave it in any of its parent
asset roles, click **Advanced Exclusion Settings**, and select
**Don\'t Exclude** next to the name of the parent asset role(s).

To include an excluded user back in the asset role, right-click the user
in the **Excluded Users** list and select **Delete User**. If the user
was automatically detected as having this asset role, it will be added
back to the **Included Users** list again. Otherwise, the next time
Cortex XSIAM analyzes the assets and automatically detects their asset
roles, this user will be included in the asset role list.

To include users from your system manually in an asset role list, in the
asset role page, click **Add User**.

- To add one or more users manually, click **Add New**, and then type
  the user names one by one in the format Netbios\\samAccount.

- To add users from a CSV file, click **Import from File**. You can use
  the example file provided to structure your CSV file.

Manually added users are also analyzed by Analytics when it runs next,
and are displayed in the Incident view and the User Risk view.

To delete a manually added user from the **Included Users**, right-click
and **Delete User**.

> **Note**
>
> Deleting a manually added user removes the user from the
> **Included Users** list. If this user is detected automatically as
> having this asset role in the future, it will appear in the
> **Included Users** list again.
>
> Excluding a manually added user ensures that even if in the future the
> user is detected as having this asset role, this detection is
> overridden and the user isn\'t included in the asset role.

To change the name of a user, right-click the user name and
**Edit User**.

###### Honey user

> **Prerequisite**
>
> The honey user role is available only if the Identity Threat Module
> add-on is enabled.

A honey user is a decoy account designed to mimic a legitimate user
within your environment. This kind of user looks attractive to potential
attackers, with access to many assets, and is used for triggering alerts
if accessed.

One of the techniques used by an attacker trying to gain access to your
network is attempting to use the credentials of accounts in your
organization. By setting up honey users, you can detect these access
attempts as soon as they occur. Unlike genuine user accounts, honey
users have no legitimate purpose within the organization, making any
activity involving them inherently suspicious. Cortex XSIAM uses its
out-of-the-box Identity Threat Module to automatically detect activity
on the honey user role for identifying suspicious activities.

To use a honey user account for detection, you must configure it
manually.

**Configure a honey user**

1.  In Assets \> Asset Roles Configuration, right click to select
    **Honey User**.

2.  Click **Edit Asset Role**.

3.  Select Add User \> Add New and enter the honey user account details
    in the NetBIOS\\SAM Account format.

#### Manage Asset Scores

The **Asset Scores** page provides a central location from which you can
view and investigate information relating to **User Scores** and
**Host Scores** in your network.

> **Note**
>
> The Hosts tab is available if the Identity Threat Module add-on is
> enabled.

Cortex XSIAM aggregates Workday and Active Directory data to create a
list of user and host assets within your network. When alerts and
incidents occur, they are associated with a host or user asset and
Cortex XSIAM calculates a score that represents the risk level of each
asset. This score helps to identify high-risk assets in your
organization and detect compromised accounts and malicious activities.

To **Include System Users** in the table, select the
**Include System Users** checkbox: system users are SYSTEM,
administrators, NT authority, and others.

> **Note**
>
> As new alerts are associated with incidents, the User and Host Scores
> are recalculated. You can view the latest User and Host Scores on the
> Asset Scores page, or track the Score trend on the User Risk View and
> Host Risk View.

To investigate your users and hosts:

1.  Select Assets \> Asset Scores. Use the toggle in the page header to
    switch between the **Users** and **Hosts** tabs.

2.  Filter and review your assets.

- The fields in the **Users** tab

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  Starred                             Whether the user is included in the
                                      watchlist.

  Score                               Represents the Cortex XSIAM
                                      high-risk user score. The score is
                                      updated continuously as new alerts
                                      are associated with incidents.

  User name                           Name of the user as provided by
                                      Cortex XSIAM.

  Full name                           Name of the user as provided by
                                      Workday or Active Directory.

  Department                          Department of the user as provided
                                      by Workday or Active Directory.

  Email                               Email of the user as provided by
                                      Workday or Active Directory.

  Member of                           (Derived from AD) The security
                                      groups that the user is associated
                                      with.

  Featured                            Whether the user is flagged as a
                                      featured user in the platform.

  Location                            Location of the user as provided by
                                      Workday or Active Directory.

  Last login                          Last date and time the user
                                      accessed Cortex XSIAM.

  Asset role                          Asset roles that the user is
                                      associated with.
  -----------------------------------------------------------------------

- The fields in the **Hosts** tab

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  Starred                             Whether the host is included in the
                                      watchlist.

  Hostname                            Unique ID of the host.

  Score                               Host score.

  IP                                  IP on which the endpoint is
                                      running.

  Has XDR agent                       Whether the endpoint has an XDR
                                      agent installed.

  Users                               Users assigned to the endpoint.

  Agent installation date             Date and time that the XDR agent
                                      was installed.

  Last communication                  Date and time of last
                                      communication.

  Operating system                    Operating system with which the
                                      endpoint is running.

  Endpoint isolated                   Whether the endpoint is isolated.

  Featured                            Whether the host is flagged as a
                                      featured host in the platform.

  Tags                                Endpoint tags applied to the host.

  Group names                         User groups that the host is
                                      associated with.

  Asset role                          Asset roles that the host is
                                      associated with.
  -----------------------------------------------------------------------

3.  To investigate further, right-click on a selected host or user and
    click **Open User Risk View** or **Open Host Risk View**. For more
    information, see
    [/document/preview/1006373#UUID-bce93c44-4b7d-55ac-36af-6971fa051a40](/document/preview/1006373#UUID-bce93c44-4b7d-55ac-36af-6971fa051a40)
    and
    [/document/preview/899560#UUID-cb6bf926-a2e7-3874-ebec-c672cbffda9a](/document/preview/899560#UUID-cb6bf926-a2e7-3874-ebec-c672cbffda9a).

- > **Note**

  > Some **User Associated Insights** may not appear as part of the
  > **User Associated Incidents** due to the insight generation
  > mechanism. For example, when an insight related to one of the assets
  > in an incident is generated a few days after the associated
  > incident, the insight may not be associated with the incident.

#### Vulnerability Assessment

Cortex XSIAM vulnerability assessment enables you to identify and
quantify the security vulnerabilities on an endpoint. After evaluating
the risks to which each endpoint is exposed and the vulnerability status
of an installed application in your network, you can mitigate and patch
these vulnerabilities on all the endpoints in your organization.

Legacy Vulnerability Assessment

For a comprehensive understanding of the vulnerability severity, Cortex
XSIAM retrieves the latest data for each Common Vulnerabilities and
Exposures (CVE) from the [NIST National Vulnerability
Database](https://nvd.nist.gov/), including CVE severity and metrics.

> **Prerequisites**
>
> The following are prerequisites for Cortex XSIAM to perform a
> vulnerability assessment of your endpoints.

+-----------------------------------+-----------------------------------------------------------------------------------+
| > Requirement                     | > Description                                                                     |
+===================================+===================================================================================+
| > Licenses and Add-ons            | - > Host Insights Add-on.                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Supported Platforms             | - > **Windows**                                                                   |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM lists only CVEs relating to the operating system, and not CVEs |
|                                   |     > relating to applications provided by other vendors.                         |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM retrieves the latest data for each CVE from the NIST National  |
|                                   |     > Vulnerability Database as well as from the Microsoft Security Response      |
|                                   |     > Center (MSRC).                                                              |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM collects KB and application information from the agents but    |
|                                   |     > calculates CVE only for KBs based on the data collected from MSRC and other |
|                                   |     > sources                                                                     |
|                                   |                                                                                   |
|                                   |   - > For endpoints running Windows Insider, Cortex XSIAM cannot guarantee an     |
|                                   |     > accurate CVE assessment.                                                    |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM does not display open CVEs for endpoints running Windows       |
|                                   |     > releases for which Microsoft no longer fixes CVEs.                          |
|                                   |                                                                                   |
|                                   | - > **Linux**                                                                     |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM collects all the information about the operating system and    |
|                                   |     > the installed applications, and calculates CVE based on the the latest data |
|                                   |     > retrieved from the NIST.                                                    |
|                                   |                                                                                   |
|                                   | - > **MacOS**                                                                     |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM collects only the applications list from MacOS without CVE     |
|                                   |     > calculation.                                                                |
|                                   |                                                                                   |
|                                   | > If Cortex XSIAM doesn\'t match any CVE to its corresponding application, an     |
|                                   | > error message is displayed, No CVEs Found.                                      |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Setup and Permissions           | > Ensure [Host Inventory Data                                                     |
|                                   | > Collection](/document/preview/868498#UUID-416260cf-dda6-2267-9eaa-b66a68471cb6) |
|                                   | > is enabled for your Cortex XDR agent.                                           |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Limitations                     | > Cortex XSIAM calculates CVEs for applications according to the application      |
|                                   | > version, and not according to application build numbers.                        |
+-----------------------------------+-----------------------------------------------------------------------------------+

Enhanced Vulnerability Assessment

The **Enhanced Vulnerability Assessment** mode uses an advanced
algorithm to collect extensive details on CVEs from comprehensive
databases and to produce an in-depth analysis of the endpoint
vulnerabilities. Turn on the **Enhanced Vulnerability Assessment** mode
from Settings \> Configurations \> Vulnerability Assessment. This option
may be disabled for the first few days after updating Cortex XSIAM as
the **Enhanced Vulnerability Assessment** engine is initialized.

> **Prerequisites**
>
> The following are prerequisites for Cortex XSIAM to perform an
> **Enhanced Vulnerability Assessment** of your endpoints.

+-----------------------------------+-----------------------------------------------------------------------------------+
| > Requirement                     | > Description                                                                     |
+===================================+===================================================================================+
| > Licenses and Add-ons            | - > Host Insights Add-on.                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Supported Platforms             | - > **Windows**                                                                   |
|                                   |                                                                                   |
|                                   |   - > Cortex XDR agent 8.3 or a later release.                                    |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM collects all the information about the operating system and    |
|                                   |     > the installed applications, and calculates CVE based on the latest data     |
|                                   |     > retrieved from the NIST.                                                    |
|                                   |                                                                                   |
|                                   |   - > CVEs that apply to applications that are installed by one user aren\'t      |
|                                   |     > detected when another user without the application installed is logged in   |
|                                   |     > during the scan.                                                            |
|                                   |                                                                                   |
|                                   | - > **MacOS**                                                                     |
|                                   |                                                                                   |
|                                   |   - > Cortex XDR agent 8.3 or a later release.                                    |
|                                   |                                                                                   |
|                                   |   - > Cortex XSIAM collects all the information about the operating system and    |
|                                   |     > the installed applications, and calculates CVE based on the latest data     |
|                                   |     > retrieved from the NIST.                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Setup and Permissions           | > Ensure [Host Inventory Data                                                     |
|                                   | > Collection](/document/preview/868498#UUID-416260cf-dda6-2267-9eaa-b66a68471cb6) |
|                                   | > is enabled for your Cortex XDR agent.                                           |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Certificates for Windows and    | > When Advanced Vulnerability and Assessment is enabled, these certificates are a |
| > macOS                           | > prerequisite for Windows and macOS.                                             |
|                                   | >                                                                                 |
|                                   | > Download the certificates from                                                  |
|                                   | > [here](https://docs-cortex.paloaltonetworks.com/v/u/EJVLvtinTtrAb~Na9XuXag).    |
|                                   |                                                                                   |
|                                   | - > Import the* Digicert Trusted Root G4* certificate into the Trusted Root       |
|                                   |   > Certification Authorities store in the local machine.                         |
|                                   |                                                                                   |
|                                   | - > In some environments, if the scan does not initialize, the                    |
|                                   |   > *DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1* certificate, may   |
|                                   |   > also be required.                                                             |
|                                   |                                                                                   |
|                                   | <!-- -->                                                                          |
|                                   |                                                                                   |
|                                   | - > Import the signed certificate into the Intermediate Certification Authorities |
|                                   |   > store in the local machine.                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------+
| > Limitations                     | - > Some CVEs may be outdated if the Cortex XDR agent wasn\'t updated recently.   |
|                                   |                                                                                   |
|                                   | - > Application versions which have reached end-of-life (EOL) may have their      |
|                                   |   > version listed as 0. This doesn\'t affect the detection of the CVEs.          |
|                                   |                                                                                   |
|                                   | - > Some applications are listed twice. One of the instances may display          |
|                                   |   > `invalid version`, however, this doesn\'t affect the functionality.           |
|                                   |                                                                                   |
|                                   | - > The scanning process may impact performance on the Cortex XDR agent during    |
|                                   |   > scanning. The scan may take up to two minutes.                                |
+-----------------------------------+-----------------------------------------------------------------------------------+

You can access the **Vulnerability Assessment** panel from Inventory \>
Endpoints \> Host Inventory \> Vulnerability Assessment.

After enabling the feature for the first time, it may take up to a week
to get the updated data into the platform. Re-collecting the data from
all endpoints in your network could take up to 6 hours. After that,
Cortex XSIAM initiates periodical recalculations to rescan the endpoints
and retrieve the updated data. If at any point you want to force data
recalculation, click **Recalculate**. The recalculation performed by any
user on a tenant updates the list displayed to every user on the same
tenant.

##### CVE Analysis

To evaluate the extent and severity of each CVE across your endpoints,
you can drill down into each CVE in Cortex XSIAM and view all the
endpoints and applications in your environment that are impacted by the
CVE. Cortex XSIAM retrieves the latest information from the NIST public
database. From Inventory \> Endpoints \> Host Inventory \> Vulnerability
Assessment, select **CVEs** on the upper-right bar. This information is
also available in the `va_cves` dataset, which you can use to build
queries in XQL Search.

If you have the Identity Threat Module enabled, you can also view the
CVE analysis in the Host Risk View. To do so, from Inventory \> Assets
\> Asset Scores, select the **Hosts** tab, right click on any endpoint,
and select **Open Host Risk View**.

For each vulnerability, Cortex XSIAM displays the following default and
optional values.

+-----------------------------------+-----------------------------------+
| Value                             | Description                       |
+===================================+===================================+
| **Affected endpoints**            | The number of endpoints that are  |
|                                   | currently affected by this CVE.   |
|                                   | For excluded CVEs, the affected   |
|                                   | endpoints are **N/A**.            |
+-----------------------------------+-----------------------------------+
| **Applications**                  | The names of the applications     |
|                                   | affected by this CVE.             |
+-----------------------------------+-----------------------------------+
| **CVE**                           | The name of the CVE.              |
|                                   |                                   |
|                                   | > **Tip**                         |
|                                   | >                                 |
|                                   | > You can click each individual   |
|                                   | > CVE to view in-depth details    |
|                                   | > about it on a panel that        |
|                                   | > appears on the right.           |
+-----------------------------------+-----------------------------------+
| **Description**                   | The general NIST description of   |
|                                   | the CVE.                          |
+-----------------------------------+-----------------------------------+
| **Excluded**                      | Indicates whether this CVE is     |
|                                   | excluded from all endpoint and    |
|                                   | application views and filters,    |
|                                   | and from all Host Insights        |
|                                   | widgets.                          |
+-----------------------------------+-----------------------------------+
| **Platforms**                     | The name and version of the       |
|                                   | operating system affected by this |
|                                   | CVE.                              |
+-----------------------------------+-----------------------------------+
| **Severity**                      | The severity level (Critical,     |
|                                   | High, Medium, or Low) of the CVE  |
|                                   | as ranked in the NIST database.   |
+-----------------------------------+-----------------------------------+
| **Severity score**                | The CVE severity score is based   |
|                                   | on the NIST Common Vulnerability  |
|                                   | Scoring System (CVSS). Click the  |
|                                   | score to see the full CVSS        |
|                                   | description.                      |
+-----------------------------------+-----------------------------------+

You can perform the following actions from Cortex XSIAM as you analyze
the existing vulnerabilities:

- **View CVE details**: Left-click the CVE to view in-depth details
  about it on a panel that appears on the right. Use the in-panel links
  as needed.

- **View a complete list of all endpoints in your network that are impacted by a CVE**:
  Right-click the CVE and then select **View affected endpoints**.

- **Learn more about the applications in your network that are impacted by a CVE**:
  Right-click the CVE and then select **View applications**.

- **Exclude irrelevant CVEs from your endpoints and applications analysis**:
  Right-click the CVE and then select **Exclude**. You can add a comment
  if needed, as well as **Report CVE as incorrect** for further analysis
  and investigation by Palo Alto Networks. The CVE is grayed out and
  labeled **Excluded** and no longer appears on the **Endpoints** and
  **Applications** views in **Vulnerability Assessment**, or in the Host
  Insights widgets. To restore the CVE, you can right-click the CVE and
  **Undo exclusion** at any time.

<!-- -->

- > **Note**

  > The CVE will be removed/reinstated to all views, filters, and
  > widgets after the next vulnerability recalculation.

##### Endpoint Analysis

To help you assess the vulnerability status of an endpoint, Cortex XSIAM
provides a full list of all installed applications and existing CVEs per
endpoint and also assigns each endpoint a vulnerability severity score
that reflects the highest NIST vulnerability score detected on the
endpoint. This information helps you to determine the best course of
action for remediating each endpoint. From Inventory \> Endpoints \>
Host Inventory \> Vulnerability Assessment, select **Endpoints** on the
upper-right bar. This information is also available in the va_endpoints
dataset. In addition, the host_inventory_endpoints preset lists all
endpoints, CVE data, and additional metadata regarding the endpoint
information. You can use this dataset and preset to build queries in XQL
Search.

For each vulnerability, Cortex XDR displays the following default and
optional values.

+-----------------------------------+-----------------------------------+
| Value                             | Description                       |
+===================================+===================================+
| **CVEs**                          | A list of all CVEs that exist on  |
|                                   | applications that are installed   |
|                                   | on the endpoint.                  |
+-----------------------------------+-----------------------------------+
| **Endpoint ID**                   | Unique ID assigned by Cortex      |
|                                   | XSIAM that identifies the         |
|                                   | endpoint.                         |
+-----------------------------------+-----------------------------------+
| **Endpoint name**                 | Hostname of the endpoint.         |
|                                   |                                   |
|                                   | > **Tip**                         |
|                                   | >                                 |
|                                   | > You can click each individual   |
|                                   | > endpoint to view in-depth       |
|                                   | > details about it on a panel     |
|                                   | > that appears on the right.      |
+-----------------------------------+-----------------------------------+
| **Last Reported Timestamp**       | The date and time of the last     |
|                                   | time the Cortex XDR agent started |
|                                   | the process of reporting its      |
|                                   | application inventory to Cortex   |
|                                   | XSIAM.                            |
+-----------------------------------+-----------------------------------+
| **MAC address**                   | The MAC address associated with   |
|                                   | the endpoint.                     |
+-----------------------------------+-----------------------------------+
| **IP address**                    | The IP address associated with    |
|                                   | the endpoint.                     |
+-----------------------------------+-----------------------------------+
| **Platform**                      | The name of the platform running  |
|                                   | on the endpoint.                  |
+-----------------------------------+-----------------------------------+
| **Severity**                      | The severity level (Critical,     |
|                                   | High, Medium, or Low) of the CVE  |
|                                   | as ranked in the NIST database.   |
+-----------------------------------+-----------------------------------+
| **Severity score**                | The CVE severity score based on   |
|                                   | the NIST Common Vulnerability     |
|                                   | Scoring System (CVSS). Click the  |
|                                   | score to see the full CVSS        |
|                                   | description.                      |
+-----------------------------------+-----------------------------------+

You can perform the following actions from Cortex XSIAM as you
investigate and remediate your endpoints:

- **View endpoint details**: Left-click the endpoint to view in-depth
  details about it on a panel that appears on the right. Use the
  in-panel links as needed.

- **View a complete list of all applications installed on an endpoint**:
  Right-click the endpoint and then select
  **View installed applications**. This list includes the application
  name, and version, of applications on the endpoint. If an installed
  application has known vulnerabilities, Cortex XSIAM also displays the
  list of CVEs and the highest **Severity**.

- (*Windows only*) **Isolate an endpoint from your network**:
  Right-click the endpoint and then select **Isolate the endpoint**
  before or during your remediation to allow the Cortex XSIAM agent to
  communicate only with Cortex XSIAM .

- (*Windows only*)
  **View a complete list of all KBs installed on an endpoint**:
  Right-click the endpoint and then select **View installed KBs**. This
  list includes all the Microsoft Windows patches that were installed on
  the endpoint and a link to the Microsoft official Knowledge Base (KB)
  support article. This information is also available in the
  `host_inventory_kbs` preset, which you can use to build queries in XQL
  Search.

- **Retrieve an updated list of applications installed on an endpoint**:
  Right-click the endpoint and then select **Rescan endpoint**.

##### Application Analysis

You can assess the vulnerability status of applications in your network
using the Host inventory. Cortex XSIAM compiles an application inventory
of all the applications installed in your network by collecting from
each Cortex XDR agent the list of installed applications. For each
application on the list, you can see the existing CVEs and the
vulnerability severity score that reflects the highest NIST
vulnerability score detected for the application. Any new application
installed on the endpoint will appear in Cortex XSIAM within 24 hours.
Alternatively, you can re-scan the endpoint to retrieve the most updated
list.

> **Note**
>
> Starting with macOS 10.15, Mac built-in system applications are not
> reported by the Cortex XDR agent and are not part of the Cortex XSIAM
> Application Inventory.

From Inventory \> Endpoints \> Host Inventory, select **Applications**.

- To view the details of all the endpoints in your network on which an
  application is installed, right-click the application and select
  **View endpoints**.

- To view in-depth details about the application, left-click the
  application name.

