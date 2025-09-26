## Reference

### Cloud service provider permissions

When you set up Cortex XSIAM to collect data from your cloud
environments, the onboarding wizard will ensure that the correct
permissions are granted for Cortex XSIAM. The following tables list the
permissions required for each of the options available in the onboarding
wizards.

Review the permissions required for each cloud service provider:

- [Amazon Web Services](#UUID64221d5367815f02277decdbc841e1a9)

- [Google Cloud Platform](#UUID424144339eaaead35299c441135b736e)

- [Microsoft Azure](#UUID3482aefacaee2c3d5d2cbeb591ff394f)

- [Oracle Cloud Infrastructure](#UUID31528075eb5ca24460a8d35cd8f4cf81)

#### Amazon Web Services provider permissions

ADS

+-------------------------------------+-----------------------+-----------------------+
| Permission                          | Scope                 | Purpose               |
+=====================================+=======================+=======================+
| ec2:ModifySnapshotAttribute         | - Snapshots with      | Share snapshot with   |
|                                     |   managed_by:         | the outpost account   |
|                                     |   paloaltonetworks    |                       |
|                                     |   tag                 |                       |
|                                     |                       |                       |
|                                     | - The snapshots can   |                       |
|                                     |   be shared only with |                       |
|                                     |   the outpost account |                       |
+-------------------------------------+-----------------------+-----------------------+
| ec2:DeleteSnapshot                  | Snapshots with        | Delete scanned        |
|                                     | managed_by:           | snapshot              |
|                                     | paloaltonetworks tag  |                       |
+-------------------------------------+-----------------------+-----------------------+
| ec2:CreateTags                      | Only as part of       | Add tags for          |
|                                     | CreateSnapshot and    | permission scoping    |
|                                     | CopySnapshot          | and cost visibility   |
|                                     | operations            |                       |
+-------------------------------------+-----------------------+-----------------------+
| ec2:DescribeSnapshots               | Snapshots with        | Retrieve snapshot     |
|                                     | managed_by:           | creation status       |
|                                     | paloaltonetworks tag  |                       |
+-------------------------------------+-----------------------+-----------------------+
| ec2:CreateSnapshot                  | Snapshots created     | Create disk snapshot  |
|                                     | with managed_by:      |                       |
|                                     | paloaltonetworks tag  |                       |
+-------------------------------------+-----------------------+-----------------------+
| ec2:CopySnapshot                    | Snapshots copied with | Re-encrypt snapshot   |
|                                     | managed_by:           | with PANW\'s KMS key  |
|                                     | paloaltonetworks tag  |                       |
+-------------------------------------+-----------------------+-----------------------+
| kms:DescribeKey                     | - PANW\'s KMS key     | To allow the          |
|                                     |                       | re-encypt operation   |
|                                     | - Only EC2 Service    |                       |
|                                     |   can use this        |                       |
|                                     |   permission          |                       |
+-------------------------------------+-----------------------+-----------------------+
| kms:GenerateDataKeyWithoutPlaintext | - PANW\'s KMS key     | To allow the          |
|                                     |                       | re-encypt operation   |
|                                     | - Only EC2 Service    |                       |
|                                     |   can use this        |                       |
|                                     |   permission          |                       |
+-------------------------------------+-----------------------+-----------------------+
| kms:CreateGrant                     | - PANW\'s KMS key     | To allow the          |
|                                     |                       | re-encypt operation   |
|                                     | - Only EC2 Service    |                       |
|                                     |   can use this        |                       |
|                                     |   permission          |                       |
+-------------------------------------+-----------------------+-----------------------+

DSPM

  ----------------------------------------------------------------------------------------------------------
  Permission                                             Scope                   Purpose
  ------------------------------------------------------ ----------------------- ---------------------------
  s3:List\*                                              All S3 buckets          To allow the listing of all
                                                                                 S3 objects

  rds:DeleteDBSnapshot                                   PANW created snapshots  To delete snapshots created
                                                                                 as part of the
                                                                                 classification process

  rds:AddTagsToResource                                  RDS resources in the    Enables creating a unique
                                                         account                 tag for the created RDS
                                                                                 resourceCreateDBSnapshots
                                                                                 in order to find them at a
                                                                                 later stage

  rds:CancelExportTask                                   RDS resources in the    Enables cancelling export
                                                         account                 tasks in case of failure or
                                                                                 termination of the
                                                                                 classification process

  rds:CreateDBClusterSnapshot                            RDS resources in the    Enables creating a snapshot
                                                         account                 for the RDS clusters that
                                                                                 need to be scanned at a
                                                                                 later stage

  rds:CreateDBSnapshot                                   RDS resources in the    Enables creating a snapshot
                                                         account                 for the RDS instances that
                                                                                 need to be scanned at a
                                                                                 later stage

  rds:Describe\*                                         RDS resources in the    Describe permissions enable
                                                         account                 PANW to get metadata
                                                                                 information on the RDS
                                                                                 instance

  rds:List\*                                             RDS resources in the    List permissions enable
                                                         account                 PANW to understand which
                                                                                 instances and snapshots
                                                                                 exist in the account

  rds:StartExportTask                                    RDS resources in the    Enables to export data from
                                                         account                 the snapshots to an S3
                                                                                 bucket

  s3:PutObject\*                                         PANW created buckets    Enables writing data to an
                                                                                 object in PANW's bucket to
                                                                                 export data from the RDS
                                                                                 instances

  s3:DeleteObject\*                                      PANW created buckets    Enables deleting stale
                                                                                 objects that were created

  s3:Get\*                                               All S3 buckets          Enable PANW to read data
                                                                                 within S3 buckets

  kms:DescribeKey                                        KMS keys in the account Enables getting information
                                                                                 about the KMS keys in the
                                                                                 account

  kms:GenerateDataKeyWithoutPlaintext                    AWS account             Enables getting information
                                                                                 about the KMS keys in the
                                                                                 account

  kms:CreateGrant                                        KMS keys in the account The created EC2 instance
                                                                                 sends a CreateGrant request
                                                                                 to AWS KMS so that it can
                                                                                 share the encrypted
                                                                                 snapshot with the outpost
                                                                                 account

  iam:PassRole                                           PANW scanner role       Enables creating export
                                                                                 tasks for RDS snapshots

  arn:aws:iam::aws:policy/AmazonMemoryDBReadOnlyAccess   DynamoDB resource in    Read-only access to the
                                                         the account             MemoryDB resources

  dynamodb:DescribeTable                                 All DynamoDB tables     Enables getting information
                                                                                 about DynamoDB tables in
                                                                                 the account

  dynamodb:Scan                                          All DynamoDB tables     Enables accessing data in
                                                                                 DynamoDB tables in the
                                                                                 account

  cloudwatch:GetMetricStatistics                         All DynamoDB tables     Enables getting usage
                                                                                 statistics, which is used
                                                                                 to ensure that
                                                                                 classification processes do
                                                                                 not interfere with
                                                                                 production environments
  ----------------------------------------------------------------------------------------------------------

Discovery Engine

  -------------------------------------------------------------------------------------
  Permission                                        Purpose
  ------------------------------------------------- -----------------------------------
  arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess   Grants read-only access to Amazon
                                                    Simple Queue Service (SQS). Allows
                                                    the retrieval of SQS queue
                                                    attributes, messages, and
                                                    configurations.

  arn:aws:iam::aws:policy/ReadOnlyAccess            Grants read-only access to AWS
                                                    services and resources. Enables the
                                                    ability to list and view
                                                    configurations, metadata, and logs
                                                    across AWS resources.

  arn:aws:iam::aws:policy/SecurityAudit             Grants access to read security
                                                    configuration metadata. Allows
                                                    users to inspect IAM
                                                    configurations, security policies,
                                                    CloudTrail logs, and other
                                                    security-relevant settings.

  DS:DescribeDirectories                            Grants read access to directory
                                                    details in AWS Directory Service.

  DS:ListTagsForResource                            Lists tags associated with a
                                                    specific AWS Directory Service
                                                    resource

  DirectConnect:DescribeConnections                 Lists Direct Connect connections
                                                    and their attributes

  DirectConnect:DescribeDirectConnectGateways       Retrieves details about Direct
                                                    Connect gateways

  DirectConnect:DescribeVirtualInterfaces           Displays all virtual interfaces for
                                                    an AWS account

  Glue:GetSecurityConfigurations                    Retrieves security configurations
                                                    for AWS Glue

  WorkSpaces:DescribeTags                           Lists tags associated with
                                                    WorkSpaces resources

  WorkSpaces:DescribeWorkspaceDirectories           Retrieves details about WorkSpaces
                                                    directories

  WorkSpaces:DescribeWorkspaces                     Lists and describes WorkSpaces
                                                    instances

  apigateway:GetDomainNames                         Retrieves API Gateway custom domain
                                                    names

  bedrock-agent:GetAgents                           Retrieves details of Bedrock agents

  bedrock-agent:GetDataSource                       Retrieves details of a specific
                                                    data source

  bedrock-agent:GetKnowledgeBases                   Retrieves details of knowledge
                                                    bases

  bedrock-agent:ListAgentAliases                    Lists aliases associated with an
                                                    agent

  bedrock-agent:ListAgentKnowledgeBases             Lists knowledge bases linked to
                                                    agents

  bedrock-agent:ListAgents                          Lists all Bedrock agents

  bedrock-agent:ListDataSource                      Lists available data sources

  bedrock:ListCustomModel                           Lists custom AI models in Amazon
                                                    Bedrock, enabling visibility into
                                                    custom AI model configurations

  cloudcontrolapi:GetResource                       Retrieves the state of an AWS
                                                    resource managed via Cloud Control
                                                    API

  cloudformation:AmazonCloudFormation               General permission related to
                                                    CloudFormation resource management

  cloudformation:StackStatus                        Retrieves the status of
                                                    CloudFormation stacks

  cloudformation:StackSummary                       Provides a summary of
                                                    CloudFormation stacks

  cloudwatch:describeAlarms                         Retrieves details about CloudWatch
                                                    alarms

  comprehendmedical:ListEntitiesDetectionV2Jobs     Lists entity detection jobs in
                                                    Comprehend Medical

  configservice:DescribeDeliveryChannels            Retrieves details of AWS Config
                                                    delivery channels

  elasticfilesysttem:DescribeFileSystemPolicy       Retrieves policies associated with
                                                    an EFS file system

  elasticloadbalancingv2:DescribeSSLPolicies        Retrieves details of ELB SSL
                                                    policies

  forecast:ListTagsForResource                      Lists tags associated with an
                                                    Amazon Forecast resource

  glue:GetConnections                               Lists connection configurations for
                                                    AWS Glue

  glue:GetResourcePolicies                          Retrieves Glue Data Catalog
                                                    policies

  iam:AmazonIdentityManagement                      General IAM access for identity and
                                                    access management

  iam:AttachedPolicy                                Retrieves policies attached to IAM
                                                    identities

  iam:PolicyRole                                    Lists IAM roles associated with a
                                                    policy

  iam:RoleDetail                                    Retrieves detailed information
                                                    about IAM roles

  opensearchserverless:ListCollections              Lists collections in OpenSearch
                                                    Serverless

  s3-control:GetAccessPointPolicy                   Retrieves an S3 access point policy

  s3-control:GetAccessPointPolicyStatus             Retrieves the status of an access
                                                    point policy

  s3-control:GetPublicAccessBlock                   Retrieves the public access block
                                                    configuration for an account

  s3-control:ListAccessPoints                       Lists S3 access points that are
                                                    owned by the current account
                                                    that\'s associated with the
                                                    specified bucket

  servicecatalog-appregistry:ListApplications       Lists applications in AWS
                                                    AppRegistry

  servicecatalog-appregistry:ListAttributeGroups    Lists attribute groups in
                                                    AppRegistry
  -------------------------------------------------------------------------------------

Registry Scan

  ----------------------------------------------------------------------------------
  Permission                         Scope                   Purpose
  ---------------------------------- ----------------------- -----------------------
  ecr:BatchGetImage                  All ECR images in the   Gets detailed
                                     account                 information for an
                                                             image, required in
                                                             order to pull the image

  ecr:GetDownloadUrlForLayer         All ECR images in the   Used in the process of
                                     account                 pulling images, to
                                                             fetch the URL for the
                                                             various layers that
                                                             make up the image

  ecr:GetAuthorizationToken          All ECR images in the   Used to create a login
                                     account                 toker for pulling
                                                             images from ECR

  ecr-public:GetAuthorizationToken   All public ECR images   Used to create a login
                                     in the account          token for pulling
                                                             images from public ECR
  ----------------------------------------------------------------------------------

Log Collection

  -----------------------------------------------------------------------
  Permission                          Purpose
  ----------------------------------- -----------------------------------
  s3:GetObject                        Grants permission to download
                                      objects from the configured S3
                                      bucket

  s3:ListBucket                       Grants permission to see the
                                      specific bucket

  sqs:ReceiveMessage                  Grants permission to consume
                                      messages from the SQS queue to
                                      receive bucket notification
                                      messages

  sqs:DeleteMessage                   Grants permission to delete
                                      consumed messages, preventing
                                      re-processing of the same message

  sqs:GetQueueAttributes              Grants permission to retrieve SQS
                                      queue attributes, used for metrics
                                      and monitoring
  -----------------------------------------------------------------------

#### Google Cloud Platform provider permissions

ADS

  -------------------------------------------------------------------------------
  Permission                      Scope                   Purpose
  ------------------------------- ----------------------- -----------------------
  compute.snapshots.get           Snapshots with          Retrieve snapshot
                                  \"cortex-scan-\" prefix creation status

  compute.snapshots.create        Snapshots with          Create disk snapshot
                                  \"cortex-scan-\" prefix 

  compute.snapshots.delete        Snapshots with          Delete scanned snapshot
                                  \"cortex-scan-\" prefix 

  compute.snapshots.setLabels     Snapshots with          Add snapshot labels for
                                  \"cortex-scan-\" prefix a cost visibility

  compute.snapshots.useReadOnly   Snapshots with          Attach snapshot to a
                                  \"cortex-scan-\" prefix scanner VM
  -------------------------------------------------------------------------------

DSPM

  -----------------------------------------------------------------------------------------
  Permission                          Scope             Purpose           Notes
  ----------------------------------- ----------------- ----------------- -----------------
  bigquery.bireservations.get         All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.capacityCommitments.get    All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.capacityCommitments.list   All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.config.get                 All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.datasets.get               All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.datasets.getIamPolicy      All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.models.getData             All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.models.getMetadata         All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.models.list                All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.routines.get               All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.routines.list              All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.tables.export              All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.tables.get                 All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.tables.getData             All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.tables.getIamPolicy        All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  bigquery.tables.list                All BigQuery      Enables           
                                      instances         classification of 
                                                        BigQuery by       
                                                        allowing access   
                                                        to data and usage 

  cloudsql.backupRuns.get             All CloudSQL      Enables           
                                      instances         classification of 
                                                        CloudSQL by       
                                                        allowing access   
                                                        to data and       
                                                        backups           

  cloudsql.backupRuns.create          All CloudSQL      Enables           
                                      instances         classification of 
                                                        CloudSQL by       
                                                        allowing access   
                                                        to data and       
                                                        backups           

  cloudsql.backupRuns.delete          All CloudSQL      Enables           
                                      instances         classification of 
                                                        CloudSQL by       
                                                        allowing access   
                                                        to data and       
                                                        backups           

  cloudsql.backupRuns.get             All CloudSQL      Enables           
                                      instances         classification of 
                                                        CloudSQL by       
                                                        allowing access   
                                                        to data and       
                                                        backups           

  cloudsql.backupRuns.list            All CloudSQL      Enables           
                                      instances         classification of 
                                                        CloudSQL by       
                                                        allowing access   
                                                        to data and       
                                                        backups           

  roles/cloudfunctions.viewer                                             Built-in role

  roles/container.clusterViewer                                           Built-in role

  roles/storage.objectViewer                                              Built-in role

  roles/firebaserules.viewer                                              Built-in role
  -----------------------------------------------------------------------------------------

Discovery Engine

  -------------------------------------------------------------------------------------------------
  Permission                                        Purpose                 Notes
  ------------------------------------------------- ----------------------- -----------------------
  roles/viewer                                                              Built-in role

  roles/cloudfunctions.viewer                                               Built-in role

  roles/container.clusterViewer                                             Built-in role

  roles/firebaserules.viewer                                                Built-in role

  roles/storage.objectViewer                                                Built-in role

  serviceusage.services.use                         Use cloud services      

  storage.buckets.get                               Get metadata of a       
                                                    storage bucket          

  storage.buckets.getIamPolicy                      Get IAM policy of a     
                                                    storage bucket          

  storage.buckets.list                              List storage buckets    

  storage.buckets.listEffectiveTags                 List effective tags of  
                                                    storage buckets         

  storage.buckets.listTagBindings                   List tag bindings of    
                                                    storage buckets         

  storage.objects.getIamPolicy                      Get IAM policy of       
                                                    storage objects         

  run.services.list                                 List Cloud Run services 

  run.jobs.list                                     List Cloud Run jobs     

  run.jobs.getIamPolicy                             Get IAM policy of Cloud 
                                                    Run jobs                

  cloudscheduler.jobs.list                          List Cloud Scheduler    
                                                    jobs                    

  baremetalsolution.instances.list                  List Bare Metal         
                                                    Solution instances      

  baremetalsolution.networks.list                   List Bare Metal         
                                                    Solution networks       

  baremetalsolution.nfsshares.list                  List Bare Metal         
                                                    Solution NFS shares     

  baremetalsolution.volumes.list                    List Bare Metal         
                                                    Solution volumes        

  baremetalsolution.luns.list                       List Bare Metal         
                                                    Solution LUNs (Logical  
                                                    Unit Numbers)           

  analyticshub.dataExchanges.list                   List Analytics Hub data 
                                                    exchanges               

  analyticshub.listings.getIamPolicy                Get IAM policy for      
                                                    Analytics Hub listings  

  analyticshub.listings.list                        List Analytics Hub      
                                                    listings                

  notebooks.locations.list                          List notebook locations 

  notebooks.schedules.list                          List notebook schedules 

  composer.imageversions.list                       List Composer image     
                                                    versions                

  datamigration.connectionprofiles.list             List data migration     
                                                    connection profiles     

  datamigration.connectionprofiles.getIamPolicy     Get IAM policy for data 
                                                    migration connection    
                                                    profiles                

  datamigration.conversionworkspaces.list           List data migration     
                                                    conversion workspaces   

  datamigration.conversionworkspaces.getIamPolicy   Get IAM policy for data 
                                                    migration conversion    
                                                    workspaces              

  datamigration.migrationjobs.list                  List data migration     
                                                    jobs                    

  datamigration.migrationjobs.getIamPolicy          Get IAM policy for data 
                                                    migration jobs          

  datamigration.privateconnections.list             List data migration     
                                                    private connections     

  datamigration.privateconnections.getIamPolicy     Get IAM policy for data 
                                                    migration private       
                                                    connections             

  datamigration.migrationjobs.list                  List AI Platform batch  
                                                    prediction jobs         

  datamigration.migrationjobs.getIamPolicy          List AI Platform NAS    
                                                    jobs                    

  datamigration.privateconnections.list             List Cloud Security     
                                                    Scanner scans           

  datamigration.privateconnections.getIamPolicy     Allows viewing the      
                                                    access policy for a     
                                                    Database Migration      
                                                    Service private         
                                                    connection              

  aiplatform.batchPredictionJobs.list               Allows listing AI       
                                                    Platform batch          
                                                    prediction jobs         

  aiplatform.nasJobs.list                           Allows listing AI       
                                                    Platform Neural         
                                                    Architecture Search     
                                                    (NAS) jobs              

  cloudsecurityscanner.scans.list                   Allows listing Cloud    
                                                    Security Scanner scans  
  -------------------------------------------------------------------------------------------------

Log Collection

  -------------------------------------------------------------------------
  Permission                Purpose                 Notes
  ------------------------- ----------------------- -----------------------
  roles/pubsub.subscriber   Grants access to        Built-in role
                            consume messages from   
                            the subscription where  
                            audit logs are stored   

  -------------------------------------------------------------------------

Registry Scan

  -------------------------------------------------------------------------------------------------
  Permission                                        Scope                   Purpose
  ------------------------------------------------- ----------------------- -----------------------
  artifactregistry.repositories.downloadArtifacts   All artifacts listed in Needed in order to
                                                    the GAR of the          download images from
                                                    customer\'s account     GAR

  roles/iam.serviceAccountTokenCreator              Access to this          Allows impersonation to
                                                    permission is limited   a specfiic service
                                                    to a specific Service   account
                                                    Account defined within  
                                                    the Outpost. No account 
                                                    other than the defined  
                                                    Service Account can     
                                                    access the permission   
                                                    and access is limited   
                                                    to the permissions      
                                                    defined on the target   
                                                    SA                      
  -------------------------------------------------------------------------------------------------

#### Microsoft Azure provider permissions

ADS

  ----------------------------------------------------------------------------------------------
  Permission                               Module            Scope             Purpose
  ---------------------------------------- ----------------- ----------------- -----------------
  Microsoft.Compute/snapshots/write        ADS               No scoping        Create disk
                                                                               snapshot

  Microsoft.Compute/snapshots/delete       ADS               No scoping        Delete scanned
                                                                               snapshot

  Microsoft.Compute/virtualMachines/read   ADS               No scoping        Allow disk
                                                                               snapshot
                                                                               operation

  Microsoft.Compute/snapshots/read         ADS               No scoping        Convert snapshot
                                                                               to disk that will
                                                                               be attached to
                                                                               the scanner
  ----------------------------------------------------------------------------------------------

DSPM

  ---------------------------------------------------------------------------------------------------------------------------------
  Permission                                                                        Scope                   Purpose
  --------------------------------------------------------------------------------- ----------------------- -----------------------
  Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action       Entire subscription     Enabling a scan by
                                                                                                            assigning private
                                                                                                            endpoints to a storage
                                                                                                            account located in a
                                                                                                            private network

  Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read              All blobs               Enables classification
                                                                                                            of data in storage
                                                                                                            blobs

  Microsoft.Storage/storageAccounts/fileServices/fileshares/files/read              All fileshares          Enables classification
                                                                                                            of data in storage
                                                                                                            fileshares

  Microsoft.Storage/storageAccounts/listKeys/action                                 Entire subscription     Getting access key to
                                                                                                            the storage account to
                                                                                                            scan file share
                                                                                                            instances using API

  Microsoft.Storage/storageAccounts/ListAccountSas/action                           Entire subscription     Getting access SAS
                                                                                                            token to the storage
                                                                                                            account to scan file
                                                                                                            share instances using
                                                                                                            API

  Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action       Entire subscription     Enabling a scan by
                                                                                                            assigning private
                                                                                                            endpoints to a storage
                                                                                                            account located in a
                                                                                                            private network

  Microsoft.Storage/\*/read                                                         Entire subscription     Reading blobs data for
                                                                                                            data classification

  Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action   Entire subscription     Getting SAS token of
                                                                                                            blobServices to enable
                                                                                                            access

  Microsoft.DocumentDB/databaseAccounts/listKeys/                                   Entire subscription     Getting SAS token of
                                                                                                            CosmosDB to enable
                                                                                                            access

  Microsoft.Storage/storageAccounts/tableServices/tables/entities/read              All storage tables      Enables classification
                                                                                                            of data in storage
                                                                                                            tables

  Microsoft.CognitiveServices/\*/read                                               All deployments         Enables discovery of
                                                                                                            OpenAI resources and
                                                                                                            other Azure AI services

  Microsoft.CognitiveServices/\*/action                                             All deployments         Enables reading and
                                                                                                            scanning OpenAI files
                                                                                                            and other Azure AI data
                                                                                                            resources

  \*/read                                                                           Entire subscription     Read-only access, used
                                                                                                            to get metadata of all
                                                                                                            managed data assets in
                                                                                                            the subscription

  Microsoft.Network/routeTables/write                                               PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/routeTables/join/action                                         PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/routeTables/delete                                              PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/delete                                          PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/join/action                                     PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/subnets/delete                                  PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/subnets/join/action                             PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/subnets/write                                   PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/virtualNetworks/write                                           PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/networkSecurityGroups/securityRules/write                       PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/networkSecurityGroups/securityRules/delete                      PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/networkSecurityGroups/join/action                               PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/networkSecurityGroups/delete                                    PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Network/networkSecurityGroups/write                                     PANW resources          Enables routing and
                                                                                                            managing internal
                                                                                                            traffic for DB
                                                                                                            classification

  Microsoft.Sql/servers/databases/read                                              PANW resources          Enables getting
                                                                                                            configurations on Azure
                                                                                                            SQL databases

  Microsoft.Sql/servers/databases/write                                             PANW resources          Enables copying and
                                                                                                            managing SQL databases
                                                                                                            in Azure SQL server

  Microsoft.Sql/servers/databases/resume/action                                     PANW resources          Enables copying and
                                                                                                            managing SQL databases
                                                                                                            in Azure SQL server

  Microsoft.Sql/servers/databases/delete                                            PANW resources          Enable cleaning stale
                                                                                                            assets such as PANW's
                                                                                                            Azure SQL server
                                                                                                            databases

  Microsoft.Sql/servers/delete                                                      PANW resources          Enable cleaning stale
                                                                                                            assets such as PANW's
                                                                                                            Azure SQL server

  Microsoft.Sql/servers/write                                                       PANW resources          Enables creating and
                                                                                                            managing PANW's Azure
                                                                                                            SQL servers

  Microsoft.Sql/servers/virtualNetworkRules/write                                   PANW resources          Enables configuring
                                                                                                            network accessibility
                                                                                                            from the scanning VMs
                                                                                                            on PANW's Azure SQL
                                                                                                            servers

  Microsoft.Sql/servers/privateEndpointConnectionsApproval/action                   PANW resources          Enables connection
                                                                                                            using endpoints

  Microsoft.Sql/managedInstances/write                                              PANW resources          Enables creation of SQL
                                                                                                            Managed Instance for
                                                                                                            classification of
                                                                                                            managed instances

  Microsoft.Sql/managedInstances/databases/write                                    PANW resources          Used for copying PITR
                                                                                                            of SQL managed
                                                                                                            instances to PANW's
                                                                                                            resource group,
                                                                                                            enabling PANW to
                                                                                                            restore and scan it

  Microsoft.Sql/managedInstances/delete                                             PANW resources          Enable cleaning stale
                                                                                                            assets such as PANW's
                                                                                                            Azure SQL Managed
                                                                                                            Instance
  ---------------------------------------------------------------------------------------------------------------------------------

Discovery Engine

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  Permission                                                                                                            Purpose
  --------------------------------------------------------------------------------------------------------------------- -----------------------------------
  Domain.Read.All                                                                                                       

  EntitlementManagement.Read.All                                                                                        

  User.Read.All                                                                                                         

  Policy.ReadWrite.AuthenticationMethod                                                                                 

  GroupMember.Read.All                                                                                                  

  RoleManagement.Read.All                                                                                               

  Group.Read.All                                                                                                        

  AuditLog.Read.All                                                                                                     

  Policy.Read.All                                                                                                       

  IdentityProvider.Read.All                                                                                             

  Directory.Read.All                                                                                                    

  Organization.Read.All                                                                                                 

  Microsoft.ContainerInstance/containerGroups/containers/exec/action                                                    Execute commands in a container

  Microsoft.ContainerRegistry/registries/webhooks/getCallbackConfig/action                                              Get webhook callback config

  Microsoft.DocumentDB/databaseAccounts/listConnectionStrings/action                                                    List Cosmos DB connection strings

  Microsoft.DocumentDB/databaseAccounts/listKeys/action                                                                 List Cosmos DB access keys

  Microsoft.DocumentDB/databaseAccounts/readonlykeys/action                                                             Get Cosmos DB read-only keys

  Microsoft.Network/networkInterfaces/effectiveNetworkSecurityGroups/action                                             View effective NSGs on NICs

  Microsoft.Network/networkInterfaces/effectiveRouteTable/action                                                        View effective route table on NICs

  Microsoft.Network/networkWatchers/queryFlowLogStatus/\*                                                               Query NSG flow log status

  Microsoft.Network/networkWatchers/read                                                                                Read network watcher settings

  Microsoft.Network/networkWatchers/securityGroupView/action                                                            View effective security rules

  Microsoft.Network/virtualwans/vpnconfiguration/action                                                                 Download VPN config

  Microsoft.Storage/storageAccounts/listKeys/action                                                                     List storage account keys

  Microsoft.Web/sites/config/list/action                                                                                List web app configuration

  Microsoft.Advisor/configurations/read                                                                                 Read Advisor configuration

  Microsoft.AlertsManagement/prometheusRuleGroups/read                                                                  Read Prometheus rule groups

  Microsoft.AlertsManagement/smartDetectorAlertRules/read                                                               Read smart detector alert rules

  Microsoft.AnalysisServices/servers/read                                                                               Read Analysis Services servers

  Microsoft.ApiManagement/service/apis/diagnostics/read                                                                 Read diagnostics info of APIs

  Microsoft.ApiManagement/service/apis/policies/read                                                                    Read policies on APIs

  Microsoft.ApiManagement/service/apis/read                                                                             Read API details

  Microsoft.ApiManagement/service/identityProviders/read                                                                Read API Management identity
                                                                                                                        providers

  Microsoft.ApiManagement/service/portalsettings/read                                                                   Read developer portal settings

  Microsoft.ApiManagement/service/products/policies/read                                                                Read policies on API products

  Microsoft.ApiManagement/service/products/read                                                                         Read API products

  Microsoft.ApiManagement/service/read                                                                                  Read API Management service info

  Microsoft.ApiManagement/service/tenant/read                                                                           Read tenant info in API Management

  Microsoft.AppConfiguration/configurationStores/read                                                                   Read Azure App Configuration stores

  Microsoft.AppPlatform/Spring/apps/read                                                                                Read Spring apps in Azure App
                                                                                                                        Platform

  Microsoft.AppPlatform/Spring/read                                                                                     Read Azure App Platform Spring
                                                                                                                        resource info

  Microsoft.Attestation/attestationProviders/read                                                                       Read attestation providers

  Microsoft.Authorization/classicAdministrators/read                                                                    Read classic administrators info

  Microsoft.Authorization/locks/read                                                                                    Read resource locks

  Microsoft.Authorization/permissions/read                                                                              Read permissions

  Microsoft.Authorization/policyAssignments/read                                                                        Read policy assignments

  Microsoft.Authorization/policyDefinitions/read                                                                        Read policy definitions

  Microsoft.Authorization/roleAssignments/read                                                                          Read role assignments

  Microsoft.Authorization/roleDefinitions/read                                                                          Read role definitions

  Microsoft.Automanage/configurationProfiles/Read                                                                       Read Automanage configuration
                                                                                                                        profiles

  Microsoft.Automation/automationAccounts/credentials/read                                                              Read credentials in automation
                                                                                                                        accounts

  Microsoft.Automation/automationAccounts/hybridRunbookWorkerGroups/read                                                Read hybrid runbook worker groups

  Microsoft.Automation/automationAccounts/read                                                                          Read automation accounts

  Microsoft.Automation/automationAccounts/runbooks/read                                                                 Read runbooks

  Microsoft.Automation/automationAccounts/variables/read                                                                Read variables in automation
                                                                                                                        accounts

  Microsoft.AzureStackHCI/Clusters/Read                                                                                 Read Azure Stack HCI clusters

  Microsoft.Batch/batchAccounts/pools/read                                                                              Read batch account pools

  Microsoft.Batch/batchAccounts/read                                                                                    Read batch accounts

  Microsoft.Blueprint/blueprints/read                                                                                   Read blueprints

  Microsoft.BotService/botServices/read                                                                                 Read bot services

  Microsoft.Cache/redis/firewallRules/read                                                                              Read firewall rules on Redis cache

  Microsoft.Cache/redis/read                                                                                            Read Redis caches

  Microsoft.Cache/redisEnterprise/read                                                                                  Read Redis Enterprise caches

  Microsoft.Cdn/profiles/afdendpoints/read                                                                              Read CDN profile AFD endpoints

  Microsoft.Cdn/profiles/afdendpoints/routes/read                                                                       Read routes of CDN profile AFD
                                                                                                                        endpoints

  Microsoft.Cdn/profiles/customdomains/read                                                                             Read custom domains in CDN profiles

  Microsoft.Cdn/profiles/endpoints/customdomains/read                                                                   Read custom domains of CDN
                                                                                                                        endpoints

  Microsoft.Cdn/profiles/endpoints/read                                                                                 Read CDN profile endpoints

  Microsoft.Cdn/profiles/origingroups/read                                                                              Read origin groups in CDN profiles

  Microsoft.Cdn/profiles/read                                                                                           Read CDN profiles

  Microsoft.Cdn/profiles/securitypolicies/read                                                                          Read CDN profile security policies

  Microsoft.Chaos/experiments/read                                                                                      Read Chaos experiments

  Microsoft.ClassicCompute/VirtualMachines/read                                                                         Read classic compute virtual
                                                                                                                        machines

  Microsoft.ClassicNetwork/networkSecurityGroups/read                                                                   Read classic network security
                                                                                                                        groups

  Microsoft.ClassicNetwork/reservedIps/read                                                                             Read classic network reserved IPs

  Microsoft.ClassicNetwork/virtualNetworks/read                                                                         Read classic virtual networks

  Microsoft.ClassicStorage/StorageAccounts/read                                                                         Read classic storage accounts

  Microsoft.CognitiveServices/accounts/read                                                                             Read Cognitive Services accounts

  Microsoft.CognitiveServices/accounts/deployments/read                                                                 Read deployments in Cognitive
                                                                                                                        Services accounts

  Microsoft.CognitiveServices/accounts/raiPolicies/read                                                                 Read RAI policies in Cognitive
                                                                                                                        Services accounts

  Microsoft.CognitiveServices/models/read                                                                               Read Cognitive Services models

  Microsoft.CognitiveServices/accounts/models/read                                                                      Read models in Cognitive Services
                                                                                                                        accounts

  Microsoft.Communication/CommunicationServices/Read                                                                    Read Communication Services

  Microsoft.Compute/availabilitySets/read                                                                               Read availability sets

  Microsoft.Compute/cloudServices/read                                                                                  Read cloud services

  Microsoft.Compute/cloudServices/roleInstances/read                                                                    Read cloud service role instances

  Microsoft.Compute/diskEncryptionSets/read                                                                             Read disk encryption sets

  Microsoft.Compute/disks/beginGetAccess/action                                                                         Begin get access on disks (action)

  Microsoft.Compute/disks/read                                                                                          Read disks

  Microsoft.Compute/galleries/images/read                                                                               Read gallery images

  Microsoft.Compute/galleries/read                                                                                      Read galleries

  Microsoft.Compute/hostGroups/read                                                                                     Read host groups

  Microsoft.Compute/snapshots/read                                                                                      Read snapshots

  Microsoft.Compute/virtualMachineScaleSets/networkInterfaces/read                                                      Read network interfaces of VM scale
                                                                                                                        sets

  Microsoft.Compute/virtualMachineScaleSets/publicIPAddresses/read                                                      Read public IP addresses of VM
                                                                                                                        scale sets

  Microsoft.Compute/virtualMachineScaleSets/read                                                                        Read virtual machine scale sets

  Microsoft.Compute/virtualMachineScaleSets/virtualMachines/networkInterfaces/ipConfigurations/publicIPAddresses/read   Read public IPs of VM scale set VM
                                                                                                                        NICs IP configs

  Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read                                                        Read virtual machines in VM scale
                                                                                                                        sets

  Microsoft.Compute/virtualMachineScaleSets/virtualmachines/instanceView/read                                           Read instance view of VM scale set
                                                                                                                        VMs

  Microsoft.Compute/virtualMachines/extensions/read                                                                     Read VM extensions

  Microsoft.Compute/virtualMachines/instanceView/read                                                                   Read VM instance view

  Microsoft.Compute/virtualMachines/read                                                                                Read virtual machines

  Microsoft.Confluent/organizations/Read                                                                                Read Confluent organizations

  Microsoft.ContainerInstance/containerGroups/containers/exec/action                                                    Execute commands in container
                                                                                                                        instances

  Microsoft.ContainerInstance/containerGroups/read                                                                      Read container groups

  Microsoft.ContainerRegistry/registries/metadata/read                                                                  Read container registry metadata

  Microsoft.ContainerRegistry/registries/pull/read                                                                      Read/pull from container registries

  Microsoft.ContainerRegistry/registries/read                                                                           Read container registries

  Microsoft.ContainerRegistry/registries/webhooks/getCallbackConfig/action                                              Get webhook callback config

  Microsoft.ContainerService/managedClusters/read                                                                       Read managed Kubernetes clusters

  Microsoft.DBforMariaDB/servers/firewallRules/read                                                                     Read MariaDB server firewall rules

  Microsoft.DBforMariaDB/servers/read                                                                                   Read MariaDB servers

  Microsoft.DBforMySQL/flexibleServers/configurations/read                                                              Read MySQL flexible server
                                                                                                                        configurations

  Microsoft.DBforMySQL/flexibleServers/databases/read                                                                   Read MySQL flexible server
                                                                                                                        databases

  Microsoft.DBforMySQL/flexibleServers/firewallRules/read                                                               Read MySQL flexible server firewall
                                                                                                                        rules

  Microsoft.DBforMySQL/flexibleServers/read                                                                             Read MySQL flexible servers

  Microsoft.DBforMySQL/servers/firewallRules/read                                                                       Read MySQL server firewall rules

  Microsoft.DBforMySQL/servers/read                                                                                     Read MySQL servers

  Microsoft.DBforMySQL/servers/virtualNetworkRules/read                                                                 Read MySQL server virtual network
                                                                                                                        rules

  Microsoft.DBforPostgreSQL/flexibleServers/configurations/read                                                         Read PostgreSQL flexible server
                                                                                                                        configurations

  Microsoft.DBforPostgreSQL/flexibleServers/databases/read                                                              Read PostgreSQL flexible server
                                                                                                                        databases

  Microsoft.DBforPostgreSQL/flexibleServers/firewallRules/read                                                          Read PostgreSQL flexible server
                                                                                                                        firewall rules

  Microsoft.DBforPostgreSQL/flexibleServers/read                                                                        Read PostgreSQL flexible servers

  Microsoft.DBforPostgreSQL/servers/configurations/read                                                                 Read PostgreSQL server
                                                                                                                        configurations

  Microsoft.DBforPostgreSQL/servers/firewallRules/read                                                                  Read PostgreSQL server firewall
                                                                                                                        rules

  Microsoft.DBforPostgreSQL/servers/read                                                                                Read PostgreSQL servers

  Microsoft.DBforPostgreSQL/serversv2/firewallRules/read                                                                Read PostgreSQL servers v2 firewall
                                                                                                                        rules

  Microsoft.Dashboard/grafana/read                                                                                      Read Grafana dashboards

  Microsoft.DataBoxEdge/dataBoxEdgeDevices/read                                                                         Read DataBox Edge devices

  Microsoft.DataFactory/datafactories/read                                                                              Read Data Factory data factories

  Microsoft.DataFactory/factories/integrationruntimes/read                                                              Read Data Factory integration
                                                                                                                        runtimes

  Microsoft.DataFactory/factories/linkedservices/read                                                                   Read Data Factory linked services

  Microsoft.DataFactory/factories/read                                                                                  Read Data Factories

  Microsoft.DataLakeAnalytics/accounts/dataLakeStoreAccounts/read                                                       Read Data Lake Analytics associated
                                                                                                                        Data Lake Store accounts

  Microsoft.DataLakeAnalytics/accounts/firewallRules/read                                                               Read Data Lake Analytics firewall
                                                                                                                        rules

  Microsoft.DataLakeAnalytics/accounts/read                                                                             Read Data Lake Analytics accounts

  Microsoft.DataLakeAnalytics/accounts/storageAccounts/read                                                             Read Data Lake Analytics storage
                                                                                                                        accounts

  Microsoft.DataLakeStore/accounts/firewallRules/read                                                                   Read Data Lake Store firewall rules

  Microsoft.DataLakeStore/accounts/read                                                                                 Read Data Lake Store accounts

  Microsoft.DataLakeStore/accounts/trustedIdProviders/read                                                              Read Data Lake Store trusted ID
                                                                                                                        providers

  Microsoft.DataLakeStore/accounts/virtualNetworkRules/read                                                             Read Data Lake Store virtual
                                                                                                                        network rules

  Microsoft.DataMigration/services/read                                                                                 Read Data Migration services

  Microsoft.DataShare/accounts/read                                                                                     Read Data Share accounts

  Microsoft.Databricks/accessConnectors/read                                                                            Read Databricks access connectors

  Microsoft.Databricks/workspaces/read                                                                                  Read Databricks workspaces

  Microsoft.Datadog/monitors/read                                                                                       Read Datadog monitors

  Microsoft.DesktopVirtualization/applicationgroups/read                                                                Read Desktop Virtualization
                                                                                                                        application groups

  Microsoft.DesktopVirtualization/hostpools/read                                                                        Read Desktop Virtualization host
                                                                                                                        pools

  Microsoft.DesktopVirtualization/hostpools/sessionhostconfigurations/read                                              Read Desktop Virtualization host
                                                                                                                        pool session host configs

  Microsoft.DesktopVirtualization/hostpools/sessionhosts/read                                                           Read Desktop Virtualization host
                                                                                                                        pool session hosts

  Microsoft.DesktopVirtualization/workspaces/providers/Microsoft.Insights/diagnosticSettings/read                       Read Desktop Virtualization
                                                                                                                        workspace diagnostic settings

  Microsoft.DesktopVirtualization/workspaces/read                                                                       Read Desktop Virtualization
                                                                                                                        workspaces

  Microsoft.DevCenter/devcenters/read                                                                                   Read DevCenter devcenters

  Microsoft.DevTestLab/schedules/read                                                                                   Read DevTestLab schedules

  Microsoft.Devices/iotHubs/Read                                                                                        Read IoT Hubs

  Microsoft.Devices/iotHubs/privateLinkResources/Read                                                                   Read IoT Hubs private link
                                                                                                                        resources

  Microsoft.DigitalTwins/digitalTwinsInstances/read                                                                     Read Digital Twins instances

  Microsoft.DocumentDB/cassandraClusters/read                                                                           Read DocumentDB Cassandra clusters

  Microsoft.DocumentDB/databaseAccounts/listConnectionStrings/action                                                    List connection strings of
                                                                                                                        DocumentDB accounts (action)

  Microsoft.DocumentDB/databaseAccounts/listKeys/action                                                                 List keys of DocumentDB accounts
                                                                                                                        (action)

  Microsoft.DocumentDB/databaseAccounts/read                                                                            Read DocumentDB database accounts

  Microsoft.DocumentDB/databaseAccounts/readonlykeys/action                                                             List readonly keys of DocumentDB
                                                                                                                        accounts (action)

  Microsoft.DomainRegistration/domains/Read                                                                             Read Domain registrations

  Microsoft.Easm/workspaces/read                                                                                        Read Easm workspaces

  Microsoft.Elastic/monitors/read                                                                                       Read Elastic monitors

  Microsoft.EventGrid/domains/privateLinkResources/read                                                                 Read Event Grid domains private
                                                                                                                        link resources

  Microsoft.EventGrid/domains/read                                                                                      Read Event Grid domains

  Microsoft.EventGrid/namespaces/read                                                                                   Read Event Grid namespaces

  Microsoft.EventGrid/partnerNamespaces/read                                                                            Read Event Grid partner namespaces

  Microsoft.EventGrid/topics/privateLinkResources/read                                                                  Read Event Grid topics private link
                                                                                                                        resources

  Microsoft.EventGrid/topics/read                                                                                       Read Event Grid topics

  Microsoft.EventHub/Namespaces/PrivateEndpointConnections/read                                                         Read EventHub Namespace private
                                                                                                                        endpoint connections

  Microsoft.EventHub/clusters/read                                                                                      Read EventHub clusters

  Microsoft.EventHub/namespaces/authorizationRules/read                                                                 Read EventHub namespaces
                                                                                                                        authorization rules

  Microsoft.EventHub/namespaces/eventhubs/authorizationRules/read                                                       Read EventHub event hub
                                                                                                                        authorization rules

  Microsoft.EventHub/namespaces/eventhubs/read                                                                          Read EventHub event hubs

  Microsoft.EventHub/namespaces/ipfilterrules/read                                                                      Read EventHub IP filter rules

  Microsoft.EventHub/namespaces/read                                                                                    Read EventHub namespaces

  Microsoft.EventHub/namespaces/virtualnetworkrules/read                                                                Read EventHub virtual network rules

  Microsoft.HDInsight/clusters/applications/read                                                                        Read HDInsight cluster applications

  Microsoft.HDInsight/clusters/read                                                                                     Read HDInsight clusters

  Microsoft.HealthBot/healthBots/Read                                                                                   Read HealthBot bots

  Microsoft.HealthcareApis/workspaces/read                                                                              Read Healthcare APIs workspaces

  Microsoft.HybridCompute/machines/read                                                                                 Read Hybrid Compute machines

  Microsoft.Insights/ActivityLogAlerts/read                                                                             Read Insights activity log alerts

  Microsoft.Insights/Components/read                                                                                    Read Insights components

  Microsoft.Insights/DataCollectionEndpoints/Read                                                                       Read Insights data collection
                                                                                                                        endpoints

  Microsoft.Insights/DataCollectionRules/Read                                                                           Read Insights data collection rules

  Microsoft.Insights/LogProfiles/read                                                                                   Read Insights log profiles

  Microsoft.Insights/MetricAlerts/Read                                                                                  Read Insights metric alerts

  Microsoft.Insights/actionGroups/read                                                                                  Read Insights action groups

  Microsoft.Insights/diagnosticSettings/read                                                                            Read Insights diagnostic settings

  Microsoft.Insights/eventtypes/values/read                                                                             Read Insights event type values

  Microsoft.IoTCentral/IoTApps/read                                                                                     Read IoT Central applications

  Microsoft.KeyVault/vaults/keys/read                                                                                   Read Key Vault keys

  Microsoft.KeyVault/vaults/privateLinkResources/read                                                                   Read Key Vault private link
                                                                                                                        resources

  Microsoft.KeyVault/vaults/read                                                                                        Read Key Vault vaults

  Microsoft.Kusto/Clusters/Databases/read                                                                               Read Kusto cluster databases

  Microsoft.Kusto/Clusters/read                                                                                         Read Kusto clusters

  Microsoft.Kusto/clusters/read                                                                                         Read Kusto clusters (alternative)

  Microsoft.LabServices/labs/read                                                                                       Read Lab Services labs

  Microsoft.LoadTestService/loadTests/read                                                                              Read Load Test Service tests

  Microsoft.Logic/integrationAccounts/read                                                                              Read Logic integration accounts

  Microsoft.Logic/workflows/read                                                                                        Read Logic workflows

  Microsoft.Logic/workflows/versions/read                                                                               Read Logic workflow versions

  Microsoft.MachineLearningServices/workspaces/computes/read                                                            Read Machine Learning Services
                                                                                                                        workspace computes

  Microsoft.MachineLearningServices/workspaces/outboundRules/read                                                       Read Machine Learning Services
                                                                                                                        workspace outbound rules

  Microsoft.MachineLearningServices/workspaces/read                                                                     Read Machine Learning Services
                                                                                                                        workspaces

  Microsoft.ManagedIdentity/userAssignedIdentities/read                                                                 Read Managed Identity user assigned
                                                                                                                        identities

  Microsoft.ManagedServices/marketplaceRegistrationDefinitions/read                                                     Read Managed Services marketplace
                                                                                                                        registration defs

  Microsoft.ManagedServices/registrationAssignments/read                                                                Read Managed Services registration
                                                                                                                        assignments

  Microsoft.Management/managementGroups/descendants/read                                                                Read Management Groups descendants

  Microsoft.Management/managementGroups/read                                                                            Read Management Groups

  Microsoft.Management/managementGroups/subscriptions/read                                                              Read Management Groups
                                                                                                                        subscriptions

  Microsoft.Maps/accounts/read                                                                                          Read Maps accounts

  Microsoft.Migrate/moveCollections/read                                                                                Read Migrate move collections

  Microsoft.MixedReality/ObjectAnchorsAccounts/read                                                                     Read Mixed Reality Object Anchors
                                                                                                                        accounts

  Microsoft.NetApp/netAppAccounts/capacityPools/read                                                                    Read NetApp capacity pools

  Microsoft.NetApp/netAppAccounts/capacityPools/volumes/read                                                            Read NetApp volumes

  Microsoft.NetApp/netAppAccounts/read                                                                                  Read NetApp accounts

  Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/read                                               Read Application Gateway Web
                                                                                                                        Application Firewall Policies

  Microsoft.Network/applicationGateways/read                                                                            Read Application Gateways

  Microsoft.Network/applicationSecurityGroups/read                                                                      Read Application Security Groups

  Microsoft.Network/azurefirewalls/read                                                                                 Read Azure Firewalls

  Microsoft.Network/bastionHosts/read                                                                                   Read Bastion Hosts

  Microsoft.Network/connections/read                                                                                    Read Network Connections

  Microsoft.Network/ddosProtectionPlans/read                                                                            Read DDoS Protection Plans

  Microsoft.Network/dnsZones/read                                                                                       Read DNS Zones

  Microsoft.Network/expressRouteCircuits/authorizations/read                                                            Read ExpressRoute Circuit
                                                                                                                        authorizations

  Microsoft.Network/expressRouteCircuits/peerings/connections/read                                                      Read ExpressRoute Circuit peerings
                                                                                                                        connections

  Microsoft.Network/expressRouteCircuits/peerings/peerConnections/read                                                  Read ExpressRoute Circuit peer
                                                                                                                        connections

  Microsoft.Network/expressRouteCircuits/peerings/read                                                                  Read ExpressRoute Circuit peerings

  Microsoft.Network/expressRouteCircuits/read                                                                           Read ExpressRoute Circuits

  Microsoft.Network/expressRouteCrossConnections/peerings/read                                                          Read ExpressRoute Cross Connections
                                                                                                                        peerings

  Microsoft.Network/expressRouteCrossConnections/read                                                                   Read ExpressRoute Cross Connections

  Microsoft.Network/expressRouteGateways/expressRouteConnections/read                                                   Read ExpressRoute Gateways
                                                                                                                        connections

  Microsoft.Network/expressRouteGateways/read                                                                           Read ExpressRoute Gateways

  Microsoft.Network/expressRoutePorts/authorizations/read                                                               Read ExpressRoute Ports
                                                                                                                        authorizations

  Microsoft.Network/expressRoutePorts/links/read                                                                        Read ExpressRoute Ports links

  Microsoft.Network/expressRoutePorts/read                                                                              Read ExpressRoute Ports

  Microsoft.Network/expressRoutePortsLocations/read                                                                     Read ExpressRoute Ports locations

  Microsoft.Network/firewallPolicies/read                                                                               Read Firewall Policies

  Microsoft.Network/frontDoorWebApplicationFirewallPolicies/read                                                        Read Front Door Web Application
                                                                                                                        Firewall Policies

  Microsoft.Network/frontDoors/backendPools/read                                                                        Read Front Door backend pools

  Microsoft.Network/frontDoors/frontendEndpoints/read                                                                   Read Front Door frontend endpoints

  Microsoft.Network/frontDoors/healthProbeSettings/read                                                                 Read Front Door health probe
                                                                                                                        settings

  Microsoft.Network/frontDoors/loadBalancingSettings/read                                                               Read Front Door load balancing
                                                                                                                        settings

  Microsoft.Network/frontDoors/read                                                                                     Read Front Doors

  Microsoft.Network/frontDoors/routingRules/read                                                                        Read Front Door routing rules

  Microsoft.Network/frontDoors/rulesEngines/read                                                                        Read Front Door rules engines

  Microsoft.Network/loadBalancers/read                                                                                  Read Load Balancers

  Microsoft.Network/localnetworkgateways/read                                                                           Read Local Network Gateways

  Microsoft.Network/locations/usages/read                                                                               Read Network locations usage

  Microsoft.Network/natGateways/read                                                                                    Read NAT Gateways

  Microsoft.Network/networkInterfaces/effectiveNetworkSecurityGroups/action                                             Execute effective network security
                                                                                                                        groups action

  Microsoft.Network/networkInterfaces/effectiveRouteTable/action                                                        Execute effective route table
                                                                                                                        action

  Microsoft.Network/networkInterfaces/read                                                                              Read Network Interfaces

  Microsoft.Network/networkSecurityGroups/defaultSecurityRules/read                                                     Read Network Security Groups
                                                                                                                        default security rules

  Microsoft.Network/networkSecurityGroups/read                                                                          Read Network Security Groups

  Microsoft.Network/networkSecurityGroups/securityRules/read                                                            Read Network Security Groups
                                                                                                                        security rules

  Microsoft.Network/networkWatchers/queryFlowLogStatus/\*                                                               Query network watcher flow log
                                                                                                                        status

  Microsoft.Network/networkWatchers/read                                                                                Read Network Watchers

  Microsoft.Network/networkWatchers/securityGroupView/action                                                            Execute security group view action

  Microsoft.Network/p2sVpnGateways/read                                                                                 Read P2S VPN Gateways

  Microsoft.Network/privateDnsZones/ALL/read                                                                            Read Private DNS Zones ALL

  Microsoft.Network/privateDnsZones/read                                                                                Read Private DNS Zones

  Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read                                                          Read Private Endpoints DNS Zone
                                                                                                                        Groups

  Microsoft.Network/privateEndpoints/read                                                                               Read Private Endpoints

  Microsoft.Network/privateLinkServices/read                                                                            Read Private Link Services

  Microsoft.Network/publicIPAddresses/read                                                                              Read Public IP Addresses

  Microsoft.Network/publicIPPrefixes/read                                                                               Read Public IP Prefixes

  Microsoft.Network/routeFilters/read                                                                                   Read Route Filters

  Microsoft.Network/routeFilters/routeFilterRules/read                                                                  Read Route Filter Rules

  Microsoft.Network/routeTables/read                                                                                    Read Route Tables

  Microsoft.Network/routeTables/routes/read                                                                             Read Route Table Routes

  Microsoft.Network/serviceEndpointPolicies/read                                                                        Read Service Endpoint Policies

  Microsoft.Network/serviceEndpointPolicies/serviceEndpointPolicyDefinitions/read                                       Read Service Endpoint Policy
                                                                                                                        Definitions

  Microsoft.Network/trafficManagerProfiles/read                                                                         Read Traffic Manager Profiles

  Microsoft.Network/virtualNetworkGateways/read                                                                         Read Virtual Network Gateways

  Microsoft.Network/virtualNetworks/read                                                                                Read Virtual Networks

  Microsoft.Network/virtualNetworks/subnets/read                                                                        Read Virtual Network Subnets

  Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read                                                         Read Virtual Network Peerings

  Microsoft.Network/virtualWans/read                                                                                    Read Virtual WANs

  Microsoft.Network/virtualwans/vpnconfiguration/action                                                                 Execute VPN configuration action

  Microsoft.Network/vpnServerConfigurations/read                                                                        Read VPN Server Configurations

  Microsoft.NetworkFunction/azureTrafficCollectors/read                                                                 Read Azure Traffic Collectors

  Microsoft.NotificationHubs/Namespaces/NotificationHubs/read                                                           Read Notification Hubs

  Microsoft.NotificationHubs/Namespaces/read                                                                            Read Notification Hub namespaces

  Microsoft.OperationalInsights/clusters/read                                                                           Read Operational Insights clusters

  Microsoft.OperationalInsights/querypacks/read                                                                         Read Operational Insights query
                                                                                                                        packs

  Microsoft.OperationalInsights/workspaces/read                                                                         Read Operational Insights
                                                                                                                        workspaces

  Microsoft.OperationalInsights/workspaces/tables/read                                                                  Read Operational Insights workspace
                                                                                                                        tables

  Microsoft.Orbital/spacecrafts/read                                                                                    Read Orbital spacecrafts

  Microsoft.PowerBIDedicated/capacities/read                                                                            Read Power BI Dedicated capacities

  Microsoft.PowerBIDedicated/servers/read                                                                               Read Power BI Dedicated servers

  Microsoft.Quantum/Workspaces/Read                                                                                     Read Quantum Workspaces

  Microsoft.RecoveryServices/Vaults/backupProtectedItems/read                                                           Read Recovery Services Vault backup
                                                                                                                        protected items

  Microsoft.RecoveryServices/Vaults/read                                                                                Read Recovery Services Vaults

  Microsoft.RecoveryServices/vaults/backupPolicies/read                                                                 Read Recovery Services Vault backup
                                                                                                                        policies

  Microsoft.RedHatOpenShift/openShiftClusters/read                                                                      Read Red Hat OpenShift clusters

  Microsoft.Relay/Namespaces/read                                                                                       Read Relay namespaces

  Microsoft.Resources/Resources/read                                                                                    Read generic resources

  Microsoft.Resources/subscriptions/providers/read                                                                      Read subscription providers

  Microsoft.Resources/subscriptions/read                                                                                Read subscriptions

  Microsoft.Resources/subscriptions/resourceGroups/read                                                                 Read resource groups

  Microsoft.Resources/subscriptions/resourceGroups/write                                                                Write resource groups

  Microsoft.Resources/templateSpecs/read                                                                                Read template specs

  Microsoft.SaaS/applications/read                                                                                      Read SaaS applications

  Microsoft.Search/searchServices/read                                                                                  Read Azure Search services

  Microsoft.Security/advancedThreatProtectionSettings/read                                                              Read Security advanced threat
                                                                                                                        protection settings

  Microsoft.Security/autoProvisioningSettings/read                                                                      Read Security auto provisioning
                                                                                                                        settings

  Microsoft.Security/automations/read                                                                                   Read Security automations

  Microsoft.Security/iotSecuritySolutions/read                                                                          Read IoT Security Solutions

  Microsoft.Security/locations/jitNetworkAccessPolicies/read                                                            Read Just-in-Time network access
                                                                                                                        policies

  Microsoft.Security/locations/read                                                                                     Read Security locations

  Microsoft.Security/pricings/read                                                                                      Read Security pricings

  Microsoft.Security/secureScores/read                                                                                  Read Security secure scores

  Microsoft.Security/securityContacts/read                                                                              Read Security contacts

  Microsoft.Security/settings/read                                                                                      Read Security settings

  Microsoft.Security/workspaceSettings/read                                                                             Read Security workspace settings

  Microsoft.ServiceBus/namespaces/authorizationRules/read                                                               Read Service Bus namespace
                                                                                                                        authorization rules

  Microsoft.ServiceBus/namespaces/networkrulesets/read                                                                  Read Service Bus namespace network
                                                                                                                        rule sets

  Microsoft.ServiceBus/namespaces/privateEndpointConnections/read                                                       Read Service Bus namespace private
                                                                                                                        endpoint connections

  Microsoft.ServiceBus/namespaces/providers/Microsoft.Insights/diagnosticSettings/read                                  Read Service Bus namespace
                                                                                                                        diagnostic settings

  Microsoft.ServiceBus/namespaces/queues/read                                                                           Read Service Bus queues

  Microsoft.ServiceBus/namespaces/read                                                                                  Read Service Bus namespaces

  Microsoft.ServiceBus/namespaces/topics/read                                                                           Read Service Bus topics

  Microsoft.ServiceBus/namespaces/topics/subscriptions/read                                                             Read Service Bus topic
                                                                                                                        subscriptions

  Microsoft.ServiceFabric/clusters/read                                                                                 Read Service Fabric clusters

  Microsoft.SignalRService/SignalR/read                                                                                 Read SignalR Service SignalR

  Microsoft.SignalRService/WebPubSub/read                                                                               Read SignalR Web PubSub

  Microsoft.Solutions/applications/read                                                                                 Read Solutions applications

  Microsoft.Sql/managedInstances/databases/read                                                                         Read SQL managed instances
                                                                                                                        databases

  Microsoft.Sql/managedInstances/databases/transparentDataEncryption/read                                               Read SQL managed instances
                                                                                                                        databases Transparent Data
                                                                                                                        Encryption

  Microsoft.Sql/managedInstances/encryptionProtector/Read                                                               Read SQL managed instances
                                                                                                                        encryption protector

  Microsoft.Sql/managedInstances/read                                                                                   Read SQL managed instances

  Microsoft.Sql/managedInstances/vulnerabilityAssessments/Read                                                          Read SQL managed instances
                                                                                                                        vulnerability assessments

  Microsoft.Sql/servers/administrators/read                                                                             Read SQL server administrators

  Microsoft.Sql/servers/auditingSettings/read                                                                           Read SQL server auditing settings

  Microsoft.Sql/servers/databases/auditingSettings/read                                                                 Read SQL server databases auditing
                                                                                                                        settings

  Microsoft.Sql/servers/databases/dataMaskingPolicies/read                                                              Read SQL server databases data
                                                                                                                        masking policies

  Microsoft.Sql/servers/databases/dataMaskingPolicies/rules/read                                                        Read SQL server databases data
                                                                                                                        masking policies rules

  Microsoft.Sql/servers/databases/read                                                                                  Read SQL server databases

  Microsoft.Sql/servers/databases/securityAlertPolicies/read                                                            Read SQL server databases security
                                                                                                                        alert policies

  Microsoft.Sql/servers/databases/transparentDataEncryption/read                                                        Read SQL server databases
                                                                                                                        Transparent Data Encryption

  Microsoft.Sql/servers/encryptionProtector/read                                                                        Read SQL server encryption
                                                                                                                        protector

  Microsoft.Sql/servers/firewallRules/read                                                                              Read SQL server firewall rules

  Microsoft.Sql/servers/read                                                                                            Read SQL servers

  Microsoft.Sql/servers/securityAlertPolicies/read                                                                      Read SQL server security alert
                                                                                                                        policies

  Microsoft.Sql/servers/vulnerabilityAssessments/read                                                                   Read SQL server vulnerability
                                                                                                                        assessments

  Microsoft.SqlVirtualMachine/sqlVirtualMachines/read                                                                   Read SQL Virtual Machines

  Microsoft.Storage/storageAccounts/blobServices/read                                                                   Read Storage blob services

  Microsoft.Storage/storageAccounts/fileServices/read                                                                   Read Storage file services

  Microsoft.Storage/storageAccounts/fileServices/shares/read                                                            Read Storage file shares

  Microsoft.Storage/storageAccounts/listKeys/action                                                                     List Storage account keys (action)

  Microsoft.Storage/storageAccounts/providers/Microsoft.Insights/diagnosticSettings/read                                Read Storage account diagnostic
                                                                                                                        settings

  Microsoft.Storage/storageAccounts/queueServices/read                                                                  Read Storage queue services

  Microsoft.Storage/storageAccounts/read                                                                                Read Storage accounts

  Microsoft.Storage/storageAccounts/tableServices/read                                                                  Read Storage table services

  Microsoft.StorageCache/Subscription/caches/read                                                                       Read Storage Cache subscription
                                                                                                                        caches

  Microsoft.StorageCache/caches/read                                                                                    Read Storage Cache caches

  Microsoft.StorageMover/storageMovers/read                                                                             Read Storage Mover storage movers

  Microsoft.StorageSync/storageSyncServices/privateLinkResources/read                                                   Read Storage Sync private link
                                                                                                                        resources

  Microsoft.StorageSync/storageSyncServices/read                                                                        Read Storage Sync services

  Microsoft.StreamAnalytics/clusters/Read                                                                               Read Stream Analytics clusters

  Microsoft.StreamAnalytics/streamingjobs/Read                                                                          Read Stream Analytics streaming
                                                                                                                        jobs

  Microsoft.Subscription/Policies/default/read                                                                          Read Subscription default policies

  Microsoft.Synapse/privateLinkHubs/privateLinkResources/read                                                           Read Synapse private link hubs
                                                                                                                        private link resources

  Microsoft.Synapse/privateLinkHubs/read                                                                                Read Synapse private link hubs

  Microsoft.Synapse/workspaces/privateLinkResources/read                                                                Read Synapse workspace private link
                                                                                                                        resources

  Microsoft.Synapse/workspaces/read                                                                                     Read Synapse workspaces

  Microsoft.Synapse/workspaces/sparkConfigurations/read                                                                 Read Synapse workspaces spark
                                                                                                                        configurations

  Microsoft.Synapse/workspaces/sqlPools/geoBackupPolicies/read                                                          Read Synapse workspaces SQL pools
                                                                                                                        geo backup policies

  Microsoft.Synapse/workspaces/sqlPools/read                                                                            Read Synapse workspaces SQL pools

  Microsoft.VideoIndexer/accounts/read                                                                                  Read Video Indexer accounts

  Microsoft.VisualStudio/Account/Read                                                                                   Read Visual Studio accounts

  Microsoft.Web/certificates/read                                                                                       Read Web certificates

  Microsoft.Web/customApis/read                                                                                         Read Web custom APIs

  Microsoft.Web/hostingEnvironments/Read                                                                                Read Web hosting environments

  Microsoft.Web/serverfarms/Read                                                                                        Read Web server farms

  Microsoft.Web/sites/Read                                                                                              Read Web sites

  Microsoft.Web/sites/basicPublishingCredentialsPolicies/Read                                                           Read Web sites basic publishing
                                                                                                                        credentials policies

  Microsoft.Web/sites/config/list/action                                                                                Execute action to list Web sites
                                                                                                                        config

  Microsoft.Web/sites/config/read                                                                                       Read Web sites config

  Microsoft.web/sites/config/appsettings/read                                                                           Read Web sites app settings

  Microsoft.Web/sites/privateEndpointConnections/Read                                                                   Read Web sites private endpoint
                                                                                                                        connections

  Microsoft.Web/sites/read                                                                                              Read Web sites

  Microsoft.Web/sites/slots/Read                                                                                        Read Web sites slots

  microsoft.web/serverfarms/sites/read                                                                                  Read Server farms sites

  Microsoft.Web/staticSites/Read                                                                                        Read Web static sites

  Microsoft.Workloads/monitors/read                                                                                     Read Workloads monitors

  Microsoft.classicCompute/domainNames/read                                                                             Read Classic Compute domain names

  microsoft.app/containerapps/read                                                                                      Read App container apps

  microsoft.monitor/accounts/read                                                                                       Read Monitor accounts

  microsoft.network/virtualnetworkgateways/connections/read                                                             Read Virtual network gateways
                                                                                                                        connections
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

Log Collection

  -----------------------------------------------------------------------
  Permission              Scope                   Purpose
  ----------------------- ----------------------- -----------------------
  Azure Event Hubs Data   Event Hub that was      Allows receive access
  Receiver                created during the      to Azure Event Hubs
                          onboarding (containing  resources
                          the audit logs)         

  Storage Blob Data       Storage account that    Reads, writes, and
  Contributor             was created during the  deletes Azure Storage
                          onboarding              containers and blobs
  -----------------------------------------------------------------------

Registry Scan

  --------------------------------------------------------------------------
  Permission
  --------------------------------------------------------------------------
  Microsoft.ContainerRegistry/registries/metadata/read

  Microsoft.ContainerRegistry/registries/pull/read

  Microsoft.ContainerRegistry/registries/read

  Microsoft.ContainerRegistry/registries/webhooks/getCallbackConfig/action
  --------------------------------------------------------------------------

### Microsoft Windows security auditing setup

In Traps 6.1.3 and later releases, to enable Cortex XDR to collect
Windows event logs, configure the following settings.

#### Enable security auditing event IDs

You can enable security auditing events using GPO or set them up on a
local server. Active Directory Certificate Services (ADCS) events
require additional setup.

> **Note**
>
> We recommend you configure security auditing using Group Policy Object
> (GPO). Using GPO simplifies audit management and ensures that auditing
> settings are uniformly applied across your network, reducing the risk
> of misconfigurations on individual machines.

##### Enable security auditing event IDs with GPO

Use the Group Policy Management Editor to configure security auditing
policies across domain controllers or other target machines.

> **Note**
>
> We recommend that you configure the Group Policy Object (GPO) to apply
> to all endpoints and not just Domain Controllers. This ensures
> comprehensive auditing across your entire network.

1.  Log in to a Domain Controller (DC) as a domain admin.

2.  Open the **Group Policy Management Editor** using one of the
    following methods:

    - Navigate to Server Manager \> Tools \> Group Policy Management.

    - On your keyboard, press **Win + R**, type GPMC.exe, and press
      **Enter**.

3.  Create or select a GPO using one of the following methods:

    - Create a new GPO and link it to an Organizational Unit (OU)
      containing the computers where you want to apply the changes.

    - Use an existing GPO. For example, to apply changes to domain
      controllers, expand the **Domain Controllers OU**, right-click
      **Default Domain Controllers Policy**, and select **Edit**.

- ![](media/rId6911.png){width="4.666666666666667in"
  height="2.7416666666666667in"}

4.  In the **Group Policy Management Editor**, navigate to Computer
    Configuration \> Policies \> Windows Settings \> Security Settings
    \> Advanced Audit Policy Configuration \> Audit Policies.

- ![](media/rId6914.png){width="4.666666666666667in"
  height="3.5933333333333333in"}

5.  In the **Audit Policies** settings, enable logging for both
    successful and failed attempts for the following events.

+-----------------+------------------+-----------------+------------------------------------------------+
| **Event IDs**   | **Audit Policy** | **Subcategory** | **Additional configuration needed**            |
+:================+:=================+:================+================================================+
| 4776, 4822,     | Account Logon    | Audit           |                                                |
| 4823            |                  | Credential      |                                                |
|                 |                  | Validation      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4768, 4771,     | Account Logon    | Audit Kerberos  | DCs only                                       |
| 4824            |                  | Authentication  |                                                |
|                 |                  | Service         |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4769, 4770,     | Account Logon    | Audit Kerberos  | DCs only                                       |
| 4821            |                  | Service Ticket  |                                                |
|                 |                  | Operations      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4741, 4742,     | Account          | Audit Computer  | DCs only                                       |
| 4743            | Management       | Account         |                                                |
|                 |                  | Management      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4727, 4728,     | Account          | Audit Security  |                                                |
| 4729, 4731,     | Management       | Group           |                                                |
| 4732, 4733,     |                  | Management      |                                                |
| 4735, 4737,     |                  |                 |                                                |
| 4754, 4755,     |                  |                 |                                                |
| 4756, 4757,     |                  |                 |                                                |
| 4764, 4799      |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4720, 4722,     | Account          | Audit User      |                                                |
| 4723, 4724,     | Management       | Account         |                                                |
| 4725, 4726,     |                  | Management      |                                                |
| 4738, 4740,     |                  |                 |                                                |
| 4765, 4766,     |                  |                 |                                                |
| 4767, 4780,     |                  |                 |                                                |
| 4781            |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4662            | DS Access        | Audit Directory | [Additional setup for Active Directory         |
|                 |                  | Service Access  | Certificate Services (ADCS)                    |
|                 |                  |                 | events](#UUIDb13e2196cb555a4e2635bf76a814ab2b) |
|                 |                  |                 |                                                |
|                 |                  |                 | DCs only                                       |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4634, 4647      | Logon/Logoff     | Audit Logoff    |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4624, 4625,     | Logon/Logoff     | Audit Logon     |                                                |
| 4648            |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4649, 4778,     | Logon/Logoff     | Audit Other     |                                                |
| 4800, 4801,     |                  | Logon/Logoff    |                                                |
| 4802, 4803      |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4672            | Logon/Logoff     | Audit Special   |                                                |
|                 |                  | Logon           |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4880, 4881,     | Object Access    | Audit           | [Additional setup for Active Directory         |
| 4885, 4886,     |                  | Certification   | Certificate Services (ADCS)                    |
| 4887, 4888,     |                  | Services        | events](#UUIDb13e2196cb555a4e2635bf76a814ab2b) |
| 4896, 4898,     |                  |                 |                                                |
| 4899, 4900      |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 5140            | Object Access    | Audit File      |                                                |
|                 |                  | Share           |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4698, 4702      | Object Access    | Audit Other     |                                                |
|                 |                  | Object Access   |                                                |
|                 |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4713            | Policy Change    | Audit           |                                                |
|                 |                  | Authentication  |                                                |
|                 |                  | Policy Change   |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4616            | System           | Audit Security  |                                                |
|                 |                  | State Change    |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 1102            | System           | Other System    | Enabled by default                             |
|                 |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+

##### Set up local machine security auditing without GPO

To enable collection of event logs on a local machine without GPO, use
the following command in an administrator command prompt:

    auditpol /set /subcategory:[subcategory] /success:enable /failure:enable

Replace \[subcategory\] with the subcategories in the following table.

+-----------------+------------------+-----------------+------------------------------------------------+
| **Event IDs**   | **Audit Policy** | **Subcategory** | **Additional configuration needed**            |
+:================+:=================+:================+================================================+
| 4776, 4822,     | Account Logon    | Audit           |                                                |
| 4823            |                  | Credential      |                                                |
|                 |                  | Validation      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4768, 4771,     | Account Logon    | Audit Kerberos  | DCs only                                       |
| 4824            |                  | Authentication  |                                                |
|                 |                  | Service         |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4769, 4770,     | Account Logon    | Audit Kerberos  | DCs only                                       |
| 4821            |                  | Service Ticket  |                                                |
|                 |                  | Operations      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4741, 4742,     | Account          | Audit Computer  | DCs only                                       |
| 4743            | Management       | Account         |                                                |
|                 |                  | Management      |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4727, 4728,     | Account          | Audit Security  |                                                |
| 4729, 4731,     | Management       | Group           |                                                |
| 4732, 4733,     |                  | Management      |                                                |
| 4735, 4737,     |                  |                 |                                                |
| 4754, 4755,     |                  |                 |                                                |
| 4756, 4757,     |                  |                 |                                                |
| 4764, 4799      |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4720, 4722,     | Account          | Audit User      |                                                |
| 4723, 4724,     | Management       | Account         |                                                |
| 4725, 4726,     |                  | Management      |                                                |
| 4738, 4740,     |                  |                 |                                                |
| 4765, 4766,     |                  |                 |                                                |
| 4767, 4780,     |                  |                 |                                                |
| 4781            |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4662            | DS Access        | Audit Directory | [Additional setup for Active Directory         |
|                 |                  | Service Access  | Certificate Services (ADCS)                    |
|                 |                  |                 | events](#UUIDb13e2196cb555a4e2635bf76a814ab2b) |
|                 |                  |                 |                                                |
|                 |                  |                 | DCs only                                       |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4634, 4647      | Logon/Logoff     | Audit Logoff    |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4624, 4625,     | Logon/Logoff     | Audit Logon     |                                                |
| 4648            |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4649, 4778,     | Logon/Logoff     | Audit Other     |                                                |
| 4800, 4801,     |                  | Logon/Logoff    |                                                |
| 4802, 4803      |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4672            | Logon/Logoff     | Audit Special   |                                                |
|                 |                  | Logon           |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4880, 4881,     | Object Access    | Audit           | [Additional setup for Active Directory         |
| 4885, 4886,     |                  | Certification   | Certificate Services (ADCS)                    |
| 4887, 4888,     |                  | Services        | events](#UUIDb13e2196cb555a4e2635bf76a814ab2b) |
| 4896, 4898,     |                  |                 |                                                |
| 4899, 4900      |                  |                 |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 5140            | Object Access    | Audit File      |                                                |
|                 |                  | Share           |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4698, 4702      | Object Access    | Audit Other     |                                                |
|                 |                  | Object Access   |                                                |
|                 |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4713            | Policy Change    | Audit           |                                                |
|                 |                  | Authentication  |                                                |
|                 |                  | Policy Change   |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 4616            | System           | Audit Security  |                                                |
|                 |                  | State Change    |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+
| 1102            | System           | Other System    | Enabled by default                             |
|                 |                  | Events          |                                                |
+-----------------+------------------+-----------------+------------------------------------------------+

##### Additional setup for Active Directory Certificate Services (ADCS) events

ADCS events with IDs 4880, 4881, 4886, 4887, 4896, 4898, 4899, 4900
require additional setup.

> **Note**
>
> Enabling auditing for Active Directory Certificate Services (ADCS)
> restarts (events 4880 and 4881) can significantly slow down the
> service if you have a large database. To prevent delays:

- > Clean up the database: Remove any unnecessary entries to reduce its
  > size.

- > Skip this audit: If restart speed is critical, consider not enabling
  > auditing for ADCS starts and stops (event IDs 4880 and 4881).

##### Enable auditing access to AD domain objects - 4662

1.  Log in to a Domain Controller as a domain admin.

2.  In the **Start** menu, under **Administrative Tools**, open
    **Active Directory Users and Computers**.

3.  In the left pane, locate the domain you want to audit. This will
    typically be the name of your network.

4.  To see more details, in the **View** menu, select
    **Advanced Features**.

- ![](media/rId6920.png){width="4.666666666666667in"
  height="2.2691666666666666in"}

5.  To view detailed information about your domain, right-click its name
    and select **Properties**.

- ![](media/rId6923.png){width="4.666666666666667in"
  height="2.4091666666666667in"}

6.  Click the **Security** tab, usually located near the top of the
    **Properties** window.

7.  Click **Advanced** which is located within the Security tab or near
    the bottom of the window.

- ![](media/rId6926.png){width="3.5in" height="3.9436614173228346in"}

8.  In the **Advanced Security Settings** window that opens, select the
    **Auditing** tab and click **Add**.

- ![](media/rId6929.png){width="4.666666666666667in"
  height="3.1616666666666666in"}

9.  Click **Select a principal**.

- ![](media/rId6932.png){width="4.666666666666667in" height="2.905in"}

10. In the window that opens, under **Enter the object name to select**,
    type **Everyone**, click **Check Names**, and then **OK**.

- ![](media/rId6935.png){width="3.5in" height="1.89875in"}

11. In the **Auditing Entry** window, do the following:

    - **Type:** To track only successful attempts, select **Success**.

    - **Applies to:** To monitor actions by users within this group and
      any subgroups, select **Descendant User objects**.

    <!-- -->

    - ![](media/rId6938.png){width="4.666666666666667in"
      height="0.91in"}

    <!-- -->

    - **Permissions:** To remove any existing permissions from this
      audit entry, click **Clear all**.

    <!-- -->

    - ![](media/rId6941.png){width="4.666666666666667in"
      height="2.9808333333333334in"}

    <!-- -->

    - Scroll up to **Permissions** to see view the list of permissions.
      Click the checkbox next to **Full Control** which automatically
      selects all the individual permissions below it.

    - Uncheck the boxes next to the following:

      - **List contents**

      - **Read all properties**

      - **Read permissions**

    <!-- -->

    - ![](media/rId6944.png){width="4.666666666666667in"
      height="2.8641666666666667in"}

    <!-- -->

    - Click **OK** to save the changes.

12. Repeat step 11, with the following values in **Applies to**:

    - **Descendant Group Objects**

    - **Descendant Computer Objects**

    - **Descendant msDS-GroupManagedServiceAccount Objects**

    - **Descendant msDS-ManagedServiceAccount Objects**

    - **Descendant msDS-DelegatedManagedServiceAccount Objects**

    <!-- -->

    - > **Note**

      > The **Descendant msDS-DelegatedManagedServiceAccount Objects**
      > configuration is relevant only for Windows Server 2025.

#### Enable additional event logs using Event Viewer

For the following event IDs, the auditing setup is configured using the
**Windows Event Viewer**. Access the **Event Viewer** through the search
box in the **Start** menu.

![](media/rId6949.png){width="2.9166666666666665in"
height="3.5952744969378827in"}

##### Event IDs 1511, 1518

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> User Profile Service, right click **Operational** and select
**Enable Log**.

![](media/rId6952.png){width="2.9166666666666665in"
height="3.245247156605424in"}

##### Event IDs 11, 70, 90

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> CAPI2, right click **Operational** and select **Enable Log**.

![](media/rId6956.png){width="2.9166666666666665in"
height="4.539558180227472in"}

##### Event ID 3008

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> DNS Client Events, right click **Operational** and select
**Enable Log**.

![](media/rId6960.png){width="2.9166666666666665in"
height="3.0661406386701664in"}

##### Event ID 2004

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> DriverFrameworks-UserMode, right click **Operational** and
select **Enable Log**.

![](media/rId6964.png){width="2.9166666666666665in"
height="3.5842290026246717in"}

##### Event IDs 4103, 4104, 4105, 4106

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> PowerShell, right click **Operational** and select
**Enable Log**.

![](media/rId6968.png){width="2.9166666666666665in"
height="3.5952744969378827in"}

##### Event IDs 1006, 1009, 1116, 1119

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> Windows Defender, right click **Operational** and select
**Enable Log**.

![](media/rId6972.png){width="2.9166666666666665in"
height="2.7890616797900263in"}

##### Event ID 1024

In Event viewer \> Application and Services Logs \> Microsoft \> Windows
\> TerminalServices-ClientActiveXCore \>
Microsoft-Windows-TerminalServices-RDPClient, right click
**Operational** and select **Enable Log**.

![](media/rId6976.png){width="4.666666666666667in"
height="2.9633333333333334in"}

##### Event IDs 2005, 2006, 2009, 2033

In Event Viewer \> Expand Applications and Services Logs \> Microsoft \>
Windows \> Windows Firewall With Advanced Security \> Firewall, right
click **Operational** and select **Enable Log**.

![](media/rId6980.png){width="2.9166666666666665in"
height="2.9952930883639546in"}

#### Enable LDAP server events logging (1644)

You can enable LDAP server event logging using RegEdit or GPO.

##### Enable LDAP server events logging using RegEdit

Make the following changes on all LDAP servers in the domain for which
you want to configure auditing.

1.  Log in as an administrator to a computer in the domain that you want
    to configure.

2.  In the **Start** menu, type **regedit** to open the Registry Editor.

3.  Add the following values on the Domain controller registry.

- "15 Field Engineering"=dword:00000005
      [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters]
      "Expensive Search Results Threshold"=dword:00000001
      "Inefficient Search Results Threshold"=dword:00000001
      "Search Time Threshold (msecs)"=dword:00000001

##### Enable LDAP server events logging using GPO

1.  On a domain controller or a system with Remote Server Administration
    Tools (RSAT) installed, open the **Group Policy Management Console**
    (GPMC).

2.  Create a new Group Policy Object (GPO): Right-click on the domain or
    organizational unit (OU) where your domain controllers reside, then
    select **Create a GPO in this domain, and Link it here\...**. Give
    it a descriptive name, e.g. Domain Controller Registry Settings.

3.  Edit the GPO.

    a.  Right-click on the newly created GPO and select **Edit**.

    - ![](media/rId6986.png){width="5.4427099737532805in"
      height="3.7758792650918633in"}

    b.  In the **Group Policy Management Editor**, navigate to Computer
        Configuration \> Preferences \> Windows Settings \> Registry.

    - ![](media/rId6989.png){width="3.8307392825896764in"
      height="4.234375546806649in"}

    c.  Add Registry Items: Right-click on **Registry** and select New
        \> Registry Item.

    - ![](media/rId6992.png){width="4.500849737532809in"
      height="4.664815179352581in"}

    d.  Configure Registry Keys: For each of the registry keys you want
        to set, create a new Registry Item.

    - \[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NTDS\\Diagnostics\]
      Create the following Registry item:

      15 Field Engineering
      - **Action:** Update

      - **Hive:** HKEY_LOCAL_MACHINE

      - **Key Path:**
        SYSTEM\\CurrentControlSet\\Services\\NTDS\\Diagnostics

      - **Value name:** 15 Field Engineering

      - **Value type:** REG_DWORD

      - **Value data:** 5

      ![](media/rId6995.png){width="4.21875in"
      height="4.770833333333333in"}

      \[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters\]
      Create the following Registry items:

      Expensive Search Results Threshold
      - **Action:** Update

      - **Hive:** HKEY_LOCAL_MACHINE

      - **Key Path:**
        SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters

      - **Value name:** Expensive Search Results Threshold

      - **Value type:** REG_DWORD

      - **Value data:** 1

      ![](media/rId7000.png){width="4.197919947506562in"
      height="4.739586614173228in"}

      Inefficient Search Results Threshold
      - **Action:** Update

      - **Hive:** HKEY_LOCAL_MACHINE

      - **Key Path:**
        SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters

      - **Value name:** Inefficient Search Results Threshold

      - **Value type:** REG_DWORD

      - **Value data:** 1

      ![](media/rId7004.png){width="4.17707895888014in"
      height="4.7499956255468065in"}

      Search Time Threshold (msecs)
      - **Action:** Update

      - **Hive:** HKEY_LOCAL_MACHINE

      - **Key Path:**
        SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters

      - **Value name:** Search Time Threshold (msecs)

      - **Value type:** REG_DWORD

      - **Value data:** 1

      ![](media/rId7008.png){width="4.197919947506562in"
      height="4.760419947506562in"}

4.  Close the **Group Policy Management Editor**.

5.  To link the GPO to the OU where your domain controllers reside, in
    **Group Policy Management**, right-click the OU, select
    **Link an Existing GPO**, then select the GPO you just created.

- ![](media/rId7013.png){width="4.354169947506562in"
  height="4.214937664041995in"}

6.  Force Group Policy Update: Force a Group Policy update using the
    `gpupdate /force` command on each domain controller or by restarting
    them.

##### Validate log collection for LDAP Server events

View the LDAP Server Events logs.

1.  From the **Start** menu, open **Event Viewer**.

2.  Go to Application and Services Logs \> Directory Service.

3.  Filter for Event ID 1644.

- ![](media/rId7017.png){width="5.833333333333333in"
  height="2.3697911198600177in"}

### XDM fields for mapping authentication events

This section provides a comprehensive guide to mapping authentication
events from various customer log sources to the XDM (Cortex Data Model)
schema. Each relevant XDM field is detailed, including whether the field
is mandatory or optional, the corresponding **Authentication Story**
field , data type, and purpose, ensuring consistent data normalization
essential for robust security analysis and threat detection.

The fields that are mandatory to map are listed below with an asterisk
(\*) beside them as these fields must be mapped to automatically create
authentication stories for XDM identity data.

> **Note**
>
> For more information on the entire Cortex Data model (XDM) schema, see
> [Cortex XSIAM Data Model
> Schema](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/Introduction).

**1. xdm.source.port\***

**Authentication Story Field**: `action_local_port`

**Type**: integer

**Requirement**: Mandatory

**Note**: If there isn't a relevant field to map to the source port,
populate this field with an empty string (`""`).

**Data Model Rule example**:

     xdm.source.port=to_integer(0)

**2. xdm.target.ipv4\***

**Authentication Story Field**: `action_remote_ip`

**Type**: string

**Requirement**: Mandatory

**Note**: Map a field that isn\'t a String or list. If there is no
relevant field to map to the target IP, populate this field with an
empty string (`""`).

**Data Model Rule example**:

    xdm.target.ipv4 = ""

**3. xdm.target.port\***

**Authentication Story Field**: `action_remote_port`

**Type**: integer

**Requirement**: Mandatory

**Note**: If there is no relevant field to map to the target port,
populate this field with an empty string (`""`).

**Data Model Rule example**:

    xdm.target.port=to_integer(0)

**4. xdm.network.ip_protocol\***

**Authentication Story Field**: `action_network_protocol`

**Type**: integer

**Requirement**: Mandatory

See full list of options for this enum in the [XDM IP Protocol
documentation](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.IP_PROTOCOL).

**Data Model Rule example**:

    xdm.network.ip_protocol=XDM_CONST.IP_PROTOCOL_TCP

**5. xdm.event.type\***

**Authentication Story Field**: `dfe_labels`

**Type**: string

**Requirement**: Mandatory

**Description**: Represents events related to authentication activity,
such as login attempts, SSO sessions, and MFA challenges.

**Required Value**: Must contain `"authentication"`

**Data Model Rule example**:

    xdm.event.type = if(eventType in ("user.authentication.sso", "user.session.start", "user.mfa.okta_verify.deny_push", "user.mfa.factor.update", "user.authentication.auth_via_mfa", "user.authentication.auth_via_AD_agent", "user.authentication.verify", "user.authentication.auth_via_radius", "user.authentication.auth_via_richclient", "system.push.send_factor_verify_push"), "authentication", "")

**6. xdm.event.tags\***

**Authentication Story Field**: `dfe_labels`

**Type**: array\<string\>

**Requirement**: Mandatory

**Description**: Represents events related to authentication activity,
such as login attempts, SSO sessions, and MFA challenges.

**Required Value**: Must contain `XDM_CONST.EVENT_TAG_AUTHENTICATION`

**Data Model Rule example**:

    xdm.event.tags = arraycreate(XDM_CONST.EVENT_TAG_AUTHENTICATION)

**7. xdm.source.ipv4\***

**Authentication Story Field**: `action_local_ip`

**Type**: string

**Requirement**: Mandatory

**Description**: Represents the external IPv4 address from which the
user authenticated. This is the IP address observed by the identity
provider or SaaS system when the authentication request was processed.
It typically reflects the user's public-facing network location, such as
their home IP, office gateway, or VPN egress point.

> **Note**
>
> Do not map a static string, list, or empty string. You must map this
> field from the raw log field that best represents the actual source IP
> used in the authentication attempt. In cases where multiple IP fields
> are available, such as `client_ip`, `source_ip`, and
> `original_client_ip`, choose the field that captures the IP address
> from which the user initially triggered the authentication request -
> before any processing by proxies or intermediate systems.

**8. xdm.event.operation\***

**Authentication Story Field**: `event_sub_type`

**Type**: string

**Requirement**: Mandatory

**Description**: This field describes the type of authentication flow,
such as a regular login or a multi-factor authentication (MFA) event. It
helps standardize different event types from various sources into two
clear categories - making detection logic easier to build, understand,
and reuse across systems.

**Supported values**:

- `XDM_CONST.OPERATION_TYPE_AUTH_LOGIN`: Login using only a password

- `XDM_CONST.OPERATION_TYPE_AUTH_MFA`: Login that involves multi-factor
  authentication

**Data Model Rule example**: The following pseudocode is an example
only, which must be modified to implement the logic in the correct
syntax by the mapped data source to different event types.

    xdm.event.operation =
       if eventType IN ("authentication", "oauth2", "mfa", "mfa_challenge", "mfa_verify")
     then XDM_CONST.OPERATION_TYPE_AUTH_MFA
      else if eventType IN ("session", "access_request", "iwa", "ldap")
     then XDM_CONST.OPERATION_TYPE_AUTH_LOGIN
      else if is_null(eventType)
     then null  else to_string(eventType)

**9. xdm.event.original_event_type\***

**Authentication Story Field**: `sso_event_type`

**Type**: string

**Requirement**: Mandatory

**Description**: This field captures the original name or label of the
event as it appears in the raw log source. It serves as a direct
reflection of the source-specific event type and is essential for
maintaining source context.

**Example values**:

- `user.authentication.sso` *(Okta -- SSO authentication event)*

- `user.mfa.okta_verify.push.deny` *(Okta -- MFA denied)*

- `user.session.start` *(Okta -- Session initiated)*

- `microsoft.login.success` *(Azure AD -- Successful login)*

- `microsoft.mfa.challenge.fail` *(Azure AD -- MFA failure)*

- `google.sign_in.challenge` *(Google Workspace -- Sign-in challenged)*

- `user.lockout` *(Generic -- Account locked due to failed attempts)*

**10. xdm.auth.service\***

**Authentication Story Field**: `auth_service`

**Type**: string

**Requirement**: Mandatory

**Description**: This field defines the role the system played in the
authentication flow, such as identity provider or relying party, and
should reflect event-specific context.

**Supported values**:

- `״SP״` (Service Provider): The system initiating the authentication
  request.

- `״IDP״` (Identity Provider): The system that validates the user
  authentication.

**Data Model Rule example for Okta**:

    if(eventType = "user.authentication.auth_via_AD_agent", "IDP",
     eventType = "user.authentication.auth_via_radius", "IDP", ..., eventType = "user.authentication.sso", "SP", null)

> **Note**
>
> Mapping should be done per event type. The same system could be an IDP
> in one event and an SP in another.

**11. xdm.event.outcome\***

**Authentication Story Field**: `auth_outcome`

**Type**: string (ENUM)

**Requirement**: Mandatory

**Description**: Specifies the final result of the authentication
attempt. Use values such as `OUTCOME_SUCCESS` or `OUTCOME_FAILURE` only
for events that definitively represent the conclusion of the
authentication process, such as when access is explicitly granted or
denied. Avoid assigning these values to intermediate steps that don't
reflect the final outcome.

**Supported values**:

- `XDM_CONST.OUTCOME_SUCCESS`

- `XDM_CONST.OUTCOME_FAILED`

> **Note**
>
> For more information on the event outcome constants in the Cortex Data
> Model, see
> [XDM_CONST.OUTCOME](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.OUTCOME).

**Data Model Rule example logic**:

    if(res ~= "[Ss]uccess" OR res = "sent",
     XDM_CONST.OUTCOME_SUCCESS, res ~= "fail",
     XDM_CONST.OUTCOME_FAILED)

> **Note**
>
> Outcome is based on a conclusive event type reflecting the true end
> state of the authentication `flow.Critical` for effectiveness of
> detection rules. Incorrect derivation can lead to missed detections or
> false positives.

**12. xdm.event.outcome_reason\***

**Authentication Story Field**: `auth_outcome_reason_category`

**Type**: string

**Requirement**: Mandatory

**Description**: Specifies a standardized and descriptive reason for the
outcome of an authentication or access-related event. This field offers
detailed context beyond a simple success or failure result and is
essential for accurate risk assessment, efficient triage, and effective
incident response.

**Supported values**:

- `user_does_not_exist`

- `bad_credentials`

- `account_expired_or_disabled`

- `account_locked`

- `failed_login`

- `auth_policy_access_violation`

- `mfa_failure`

- `mfa_expired`

- `user_reject`

- `user_cancelled`

- `OTHER`

- `NOT_SPECIFIED`

**Required action**: Explicit mapping logic is required between the raw
event fields that contain outcome/error messages, such as `get_reason`
and `debug_data_error_code`, and this canonical field. Mapping must
normalize provider-specific strings or error codes into one of the
supported values.

**Data Model Rule example**: The following pseudocode is an example
only, which must be modified to implement the logic in the correct
syntax.

    xdm.event.outcome_reason = if(  get_reason ~= "UNKNOWN_USER",                        "user_does_not_exist",
      get_reason ~= "Login denied. No matching user",      "user_does_not_exist",
      get_reason ~= "INVALID_CREDENTIALS",                 "bad_credentials",  debugdata_errorcode ~= "1326",                       "bad_credentials",
      get_reason ~= "account is expired",                  "account_expired_or_disabled",
      get_reason ~= "USER_ACCOUNT_EXPIRE",                 "account_expired_or_disabled",  debugdata_errorcode IN ("1331", "1793"),             "account_expired_or_disabled",
      get_reason ~= "account is locked",                   "account_locked",
      get_reason ~= "LOCKED_OUT",                          "account_locked",
      get_reason ~= "Login failed",                        "failed_login",
      get_reason ~= "PASSWORD_BASED_LOGIN_DISALLOWED",     "auth_policy_access_violation",
      get_reason ~= "login denied",                        "auth_policy_access_violation",
      get_reason ~= "VERIFICATION_ERROR",                  "mfa_failure",
      get_reason ~= "DEL_AUTH_TIMEOUT",                    "mfa_expired",
      get_reason ~= "User rejected Okta push verify",      "user_reject",
      get_reason ~= "Login aborted",                       "user_cancelled",
      get_reason ~= "NOT_SPECIFIED",                       "OTHER")

**13. xdm.source.user.upn\***

**Authentication Story Field**: `auth_identity`

**Type**: string

**Requirement**: Mandatory

**Description**: Represents the user identity associated with the
authentication or access event. This field must be populated using the
User Principal Name (UPN) format. It cannot be left empty.

Using UPN as a normalized identity format ensures consistency across
diverse identity providers, such as Azure AD, Okta, and on-prem AD, and
authentication flows. It plays a central role in correlating activity
across logs, enriching detections, and building an accurate
authentication story across systems.

**Example values**: `jane.doe@company.com`

**14. xdm.event.description**

**Authentication Story Field**: `sso_display_message`

**Type**: string

**Requirement**: Optional

**Description**: Provides a human-readable summary describing the nature
of the authentication event. This value is typically derived from the
source system\'s descriptive message and is intended to offer clear
context for analysts during monitoring and investigations.

**Example values**:

- `“A push was sent to a user for verification”`

- `"User single sign on to app”`

- `“Authentication of user via MFA”`

**15. xdm.source.host.device.id**

**Authentication Story Field**: `agent_id`

**Type**: string

**Requirement**: Optional

**Description**: This field represents the unique identifier of the
device that initiated or is associated with the current authentication
event.

The value should remain consistent per device over time and be mapped
from the most reliable source-specific field, such as device ID, machine
ID, or equivalent. If there isn\'t a sufficient device ID field, the
alternative will be to map the IP address that initiated the
authentication (same as `xdm.source.ipv4`).

**16. xdm.source.host.hostname**

**Authentication Story Field**: `auth_device_name`

**Type**: string

**Requirement**: Optional

**Description**: Represents the host/device name associated that
initiated or is responsible for authentication events.

**17. xdm.logon.type**

**Authentication Story Field**: `auth_is_interactive`

**Type**: string

**Requirement**: Optional

**Description**: Represents the type of logon associated with the
authentication event, with a focus on distinguishing between interactive
(user-driven) and non-interactive (system or service-based) activity.
This distinction is important for behavioral analysis, risk scoring, and
threat detection.

**Common values**:

- `XDM_CONST.LOGON_TYPE_INTERACTIVE`: Indicates a user is interactively
  using the machine, such as logging in through a terminal session,
  remote shell, or console.

- `XDM_CONST.LOGON_TYPE_SERVICE`: Indicates a service-type logon, such
  as Windows service, automations, and application tokens, where the
  account must have the service logon privilege.

> **Note**
>
> These are the most common values, but other logon types also exist.
> For a complete list, see
> [XDM_CONST.LOGON_TYPE](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.LOGON_TYPE).

**18. xdm.event.operation.sub_type**

**Authentication Story Field**: `auth_method`

**Type**: string

**Requirement**: Optional

**Description**: Specifies a standardized and descriptive reason for the
outcome of an authentication or access-related event. This field offers
detailed context beyond a simple success or failure result and is
essential for accurate risk assessment, efficient triage, and effective
incident response.

**Required action**: You must define explicit mapping logic between the
raw field in the source log that contains the authentication method
information, such as `authMethod`, `authenticationFlow.type`, and
`factorUsed`, and this XDM field.

This mapping should translate raw values into one of the allowed
sub-category listed below.

**Data Model Rule example**: The following pseudocode is an example
only, which must be modified to implement the logic in the correct
syntax.

    if(lowercase_auth_method = "password",       "password",
       lowercase_auth_method = "otp_sms",        "sms",
       lowercase_auth_method = "push",           "application",
       lowercase_auth_method = "yubikey",        "hardware_token",
       lowercase_auth_method = "trusted_device", "trusted_login",
       lowercase_auth_method = "sso",            "Generic SSO",
       lowercase_auth_method = "email",          "email",
       lowercase_auth_method = "voice",          "voice",
       lowercase_auth_method = null,             null,   to_string(lowercase_auth_method))

**Supported values (per applicable event type)**:

- `hardware_token`: Physical device-based authentication, such as RSA
  token or YubiKey.

- `password` : Standard password-based login.

- `application`: Action approved via an authenticator app, such as push
  notification.

- `email`: Verification through email link or one-time code.

- `sms`: SMS-based one-time password (OTP) or verification.

- `voice`: Verification via voice call.

- `trusted_login`: Login from a known or previously trusted device.

- `Generic SSO`: Federated authentication using a standard single
  sign-on provider.

- `null`: No sub-type specified or not applicable.

**19. xdm.source.user.identifier**

**Authentication Story Field**: `auth_identity_id`

**Type**: string

**Requirement**: Optional

**Description**: This field should contain a unique and consistent
identifier for the user associated with the event.

**Example values**:

- `a1b2c3d4-e5f6-7890-ab12-3456789cdef0`: Directory object GUID, such as
  Azure AD object ID.

- `S-1-5-21-3623811015-3361044348-30300820-1013`: Windows Security
  Identifier (SID).

**Best Practice**: Populate with the most persistent and canonical user
identifier available from the identity source.

**20. xdm.source.user.username**

**Authentication Story Field**: `auth_identity_display_name`

**Type**: string

**Requirement**: Optional

**Description**: User Display Name Field. This field should contain the
user\'s name in a human-readable format, typically including the first
and last name, such as John Smith.

**21. xdm.source.user.user.type**

**Authentication Story Field**: `auth_normalized_user.identity_type`

**Type**: string

**Requirement**: Optional

**Description**: Indicates the type of identity associated with the
authentication event.

**Supported values (Constants)**:

- `XDM_CONST.USER_TYPE_REGULAR ("USER")`

- `XDM_CONST.USER_TYPE_SERVICE_ACCOUNT ("SERVICE ACCOUNT")`

- XDM_CONST.USER_TYPE_MACHINE_ACCOUNT (\"MACHINE ACCOUNT\")

**Example mapping logic**: The following pseudocode is an example only,
which must be modified to implement the logic in the correct syntax.

    if(actor_type in("User"), XDM_CONST.USER_TYPE_REGULAR, actor_type
     in("SystemPrincipal"),
     XDM_CONST.USER_TYPE_SERVICE_ACCOUNT,actor_type in("IP address"),
     XDM_CONST.USER_TYPE_MACHINE_ACCOUNT, to_string(actor_type))

> **Note**
>
> For more information, see
> [XDM_CONST.USER_TYPE](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.USER_TYPE).

**22. xdm.auth.privilege.level**

**Authentication Story Field**: `auth_normalized_user.privilege_level`

**Type**: string

**Requirement**: Optional

**Description**: Represents the privilege level or role of the user
during the authentication event, such as admin, user, or guest. Used to
assess risk and impact. Should reflect a canonical privilege level.

**Supported values (Constants)**:

- `XDM_CONST.PRIVILEGE_LEVEL_GUEST`

- `XDM_CONST.PRIVILEGE_LEVEL_USER`

- `XDM_CONST.PRIVILEGE_LEVEL_ADMIN`

- `XDM_CONST.PRIVILEGE_LEVEL_SYSTEM`

**Example mapping logic**: The following pseudocode is an example only,
which must be modified to implement the logic in the correct syntax.

    if(lowercase_user_type = "user", XDM_CONST.PRIVILEGE_LEVEL_USER,
     lowercase_user_type = "guest", XDM_CONST.PRIVILEGE_LEVEL_GUEST,
     lowercase_user_type = "admin", XDM_CONST.PRIVILEGE_LEVEL_ADMIN,
     lowercase_user_type = "system", XDM_CONST.PRIVILEGE_LEVEL_SYSTEM,
     lowercase_user_type = null, null, to_string(lowercase_user_type))

> **Note**
>
> For more information, see
> [XDM_CONST.PRIVILEGE_LEVEL](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.PRIVILEGE_LEVEL).

**23. xdm.target.resource.id**

**Authentication Story Field**: `auth_target_id`

**Type**: string

**Requirement**: Optional

**Description**: Represents the unique identifier of the accessed
resource or application during the authentication event, such as
application ID or internal resource ID.

**24. xdm.target.resource.name**

**Authentication Story Field**: `auth_target`

**Type**: string

**Requirement**: Optional

**Description**: Provides the readable name of the resource or
application accessed during the event. This should reflect the logical
service or platform the user interacted with.

**Example values**:
`״Exchange", ״SharePoint״, ״ServiceNow״, ״HR Portal״, ״Okta Admin Portal״`

**25. xdm.source.user.agent**

**Authentication Story Field**: `action_user_agent`

**Type**: string

**Requirement**: Optional

**Description**: Captures the full user-agent string from the client
initiating the authentication request. Typically includes information
about the browser, operating system, device type, and version details.

**Example values**:
`“Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36”`

**26. xdm.network.session_id**

**Authentication Story Field**: `sso_debug_data.session_id`

**Type**: string

**Requirement**: Optional

**Description**: Represents the session identifier associated with the
user interaction. This value is typically issued by the application or
identity platform and is used to group multiple related actions or
requests made by the same user or device within a defined time window,
commonly referred to as a session.

These can include login, token refresh, or other events that occur as
part of a continuous authenticated interaction.

**Example use cases**:

- Tracking session duration

- Linking session start and end events

- Grouping multiple MFA prompts within a single login session

**27. xdm.source.location.city**

**Authentication Story Field**: `action_location.city`

**Type**: string

**Requirement**: Optional

**Description**: Represents the city associated with the source IP
address.

**28. xdm.source.location.country**

**Authentication Story Field**: `action_location.country`

**Type**: string

**Requirement**: Optional

**Description**: Identifies the country where the authentication request
originated, based on the source IP address.

**Example values**: `“US,“ “IL“, “DE“, “FRANCE”`

**29. xdm.source.location.region**

**Authentication Story Field**: `action_location.region`

**Type**: string

**Requirement**: Optional

**Description**: Captures the region, province, or state associated with
the source IP address.

**Example values**: `“California“, “Bavaria“, “Tel Aviv“`

**30. xdm.source.location.latitude**

**Authentication Story Field**: `action_location.latitude`

**Type**: float

**Requirement**: Optional

**Description**: Represents the latitude coordinate of the source IP
address\'s estimated physical location.

**Example values**: `“40.7128”, “48.8566”`

**31. xdm.source.location.longitude**

**Authentication Story Field**: `action_location.longitude`

**Type**: float

**Requirement**: Optional

**Description**: Represents the longitude coordinate of the source IP
address\'s estimated physical location.

**32. xdm.source.location.continent**

**Authentication Story Field**: `action_location.continent`

**Type**: string

**Requirement**: Optional

**Description**: Indicates the continent associated with the source
IP\'s location, such as Europe, Asia, or North America.

**33. xdm.source.location.timezone**

**Authentication Story Field**: `action_location.timezone`

**Type**: string

**Requirement**: Optional

**Description**: This enables time-based correlation between user
activity and local context.

**Example values**: `"Asia/Jerusalem", "America/New_York", "UTC"`

**34. xdm.source.host.device.category**

**Authentication Story Field**: `auth_client_type`

**Type**: string

**Requirement**: Optional

**Description**: Represents the operating system family of the device or
client that initiated the event.

**Supported values**:

- `“Computer”`: A desktop or laptop device.

- `“Mobile”`: A mobile phone or smartphone.

- `“IOT”`: An Internet of Things device, such as smart TV or smart
  speaker.

- `“Tablet”`: A tablet computing device.

**35. xdm.source.application.name**

**Authentication Story Field**: `agent_extra_data.browser`

**Type**: string

**Requirement**: Optional

**Description**: Represents browser vendor used during the
authentication event.

**Example values**: `“Chrome“, “Firefox“, “Safari“, “Edge“`

**36. xdm.source.application.version**

**Authentication Story Field**: `agent_extra_data.browser_version`

**Type**: string

**Requirement**: Optional

**Description**: Represents the version of the browser used during the
authentication event.

**Example values**: `“Chrome 113“, “Firefox 102“, “Safari 16.3“`

**37. xdm.source.host.os.family**

**Authentication Story Field**: `agent_os_type`

**Type**: string

**Requirement**: Optional

**Description**: Provides a normalized, high-level abstraction of the
operating system associated with the source host. This field enables
consistent behavior across different data sources.

**Required action**: You must explicitly define a mapping logic between
the raw field in the original data source that contains the OS
information, such as `device.os_name`, and normalize into the XDM field.

**Common values (Constants)**:

- `XDM_CONST.OS_FAMILY_WINDOWS`

- `XDM_CONST.OS_FAMILY_MACOS`

- `XDM_CONST.OS_FAMILY_LINUX`

- `XDM_CONST.OS_FAMILY_ANDROID`

- `XDM_CONST.OS_FAMILY_IOS`

> **Note**
>
> For more information, see
> [XDM_CONST.OS_FAMILY](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Data-Model-Schema-Guide-for-Cortex-XSIAM-with-Cortex-Cloud/XDM_CONST.OS_FAMILY).

**Example mapping logic**: The following pseudocode is an example only,
which must be modified to implement the logic in the correct syntax.

    if raw_event.host_os contains "windows"      → XDM_CONST.OS_FAMILY_WINDOWS  
    if raw_event.host_os contains "mac"          → XDM_CONST.OS_FAMILY_MACOS  
    if raw_event.host_os contains "linux"        → XDM_CONST.OS_FAMILY_LINUX  
    if raw_event.host_os contains "android"      → XDM_CONST.OS_FAMILY_ANDROID  
    if raw_event.host_os contains "ios"          → XDM_CONST.OS_FAMILY_IOS  

**Data Model Rule example logic**:

     if(os contains "windows", XDM_CONST.OS_FAMILY_WINDOWS, os contains "mac", XDM_CONST.OS_FAMILY_MACOS, ...)

**38. xdm.source.host.os**

**Authentication Story Field**: `agent_os_sub_type`

**Type**: string

**Requirement**: Optional

**Description**: This field captures the raw operating system
information reported by the source host\'s telemetry.

**Example values**:
`“Microsoft Windows NT 10.0“, “Microsoft Windows NT 6.1 (Windows 7“), “Darwin Kernel Version 20.6.0“`

**39. xdm.session.context.id**

**Authentication Story Field**: `auth_correlation_id`

**Type**: string

**Requirement**: Optional

**Description**: Represents a correlation ID tied to a single
authentication or access-related request. This ID is generated by the
identity provider, such as Azure AD or Okta, and used to link events
belonging to a single logical transaction, such as an SSO login flow or
token issuance.

**Example values**: `”25423545-6364-5423-3232-42343760”`

> **Note**
>
> While `xdm.network.session_id` aggregates multiple user actions within
> a broader session window. `xdm.session.context.id` is used to
> correlate events that belong to a single authentication request or
> transaction.

**40. xdm.time**

**Authentication Story Field**: `generatedTime`

**Type**: timestamp

**Description**: Represents the timestamp of when the event occurred.
This field is essential for event sequencing and correlation. This field
is automatically mapped.

**Example values**:

    - ”2025-05-26T14:45:32Z” (UTC format ISO 8601)
    - “2025-05-26T14:45:32.123Z “ (UTC with millisecond precision),
    -“2025-05-26 14:45:32” (Standard datetime format non-ISO)
