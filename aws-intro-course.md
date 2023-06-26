# aws intro course

- [link](https://www.udemy.com/course/introduction-to-cloud-computing-on-amazon-aws-for-beginners)

## IT fundamentals

### client-server computing

- computer: cpu, ram (non-persistent, high performance), sdd/hdd (persistant), network interface card NIC connects to networks
  - cpu GHz
  - RAM/HDD GB
  - NIC Mbps/Gbps
- same core components regardless of laptop/desktop/server
  - but designed specifically so that multiple users can connect over a network
  - more specialized/expensive hardware
  - includes redundancy
- client devices (laptop, desktop, IOT) connect to server
- servers running in the cloud offer services including application, processing and data storage
- client applicaiton finds server by IP address using protocol and port, port is like a door into the server
  - web server: HTTP port 80
  - file server: SMB port 445
  - email server: SMTP port 25
- servers connect to other servers
  - e.g. databases

### storage

- block based storage system such as hdd/sdd
  - OS sees a volume which can be partitioned and formatted
  - disk attached to a computer (internal or network attached)
- network attached storage
  - through a NIC
  - get to a NAS network attached storage server: file-based storage system
  - can't partition it but can just connect to it
  - filesystem mounted to OS using network share - shared by many users
- object storage system
  - user uploads object using web browser
  - HTTP with REST api
  - no hierarchy of objects in a container - every file at same level
  - objects can be files, videos, images etc
  - low cost, massively scalable

### ip addresses and DNS

- IPv4: web server has network card attached to network, card has IP address
- Ip addresses are used by computers to communicate between each other
- DNS server will map domain name to IP address corresponding to web server
- IPv4 structure
  - dotted decimal notation
  - each part is a binary octet
  - first three parts are network ID - shared by everything on network
  - last part is host ID - individual to every computer on network
  - subnet mask used to define network and host id
- some ranges are private use according to IETF RFC
  - 10.0.0.0 - 10.255.255.255
  - 172.16.0.0 - 172.31.255.255
  - 192.168.0.0 - 192.168.0.255

### bandwitdth and latency

- bandwith is the rate of data transfer for a fixed period of time measured in Gbps
- latency is amount of time it takes to send data from one point to another measured in micro/milliseconds
  - depends on distance: measured in microsends within a data center (meters) and milliseconds between data centers (km)
- importance of latency depends on type of application e.g. voice call VS email
- distance is biggest factor in latency but also number of devices it passes through

### networking - routers, switches, firewalls

- switch as layer 2 device, doesn't know about IP, we don't handle them when in cloud
- decides how to send communications between computers within a current network
- routers: layer 3: understands network numbers: communicates between different networks: maps destinations and interfaces
- firewalls for security: placed in different places in network: restrict ports/protocols options
  - e.g. allow web server HTTP port 80 or HTTPS 443 but deny everything else
  - can put firewalls at different levels of the networks including on the server itself

### APIs

- api provides instructions developers use in their code
- instructions sent to API using HTTP
- then connects to various backend services

## cloud computing concepts

### legacy/traditional IT

- coporate data center with racks housing various equipment: servers, storage serves, backup systems, routers, switch, firewall
- IT equipment owned by the company, often lease space in a data center, very capital intensive, very high security buildings
- users in corporate office need to connect to data center, IT staff needed to configure the whole thing
- costs for building, security, hardware, software licensing, maintenance, power, internet, staff etc. also very slow

### cloud computing

- email server --> gmail, file server --> dropbox, CRM --> salesforce
- you don't own/manage the infrastructure, offered on subscription/consumption model, scales automatically
- cloud services characteristics:
  - on-demand, self-service
  - broad network access: available over internet
  - resource pooling: serve multiple consumers using multi-tenant model
  - rapid elasticity: scale easily based on demand
  - measured service: monitored/metered, you pay for what you use
- launching cloud services: management console, command line, code (sdk)

### cloud computing service models

- private coud: managed by you: hardware, software, application
  - companies often deploy a private cloud in their own data center
  - lots of control, must also satisfy the characteristics, slow expensive etc.
- infrastructure as a service: same but without hardware, hypervisor
  - you manage from the virtual server upwards
  - e.g. EC2 instances, azure virtual machines, google compute engines
- platform as a service: upload your code and data
  - e.g. aws elastic beanstalk, azure webapps, compute app engine
- SaaS: nothing managed by you but software ready to consume, pure consumption model
  - e.g. salesforce

### cloud computing deployment models

- private cloud: enterprise deploys own infra/apps into own data center
  - VMware, redhat, openstack
- public cloud: IT services that you consume are hosted and delivered from a 3rd party and accessed over the internet
  - AWS, azure, GCP
  - variable operation expense instead of capital expense
  - economies of scale
  - massive elasticity
- hybrid: combination of private/public/on-premises
- multicloud: usage of two+ public clouds at a time, possibly multiple private clouds
  - if you find certain clouds are better suited to different clouds

### scaling up vs scaling out

- scalability - more resources assigned to our cloud services
- elasticity - automatically scales up and down based on need
- up or out depends on stateless or stateful
  - are you seeing same information as everyone else or not
  - stateless: news website: no state about user's session
  - stateful: netflix
- ecommerce: add to cart in browser cookies, connects to stateless web server, application server processes the order, database stores it so stateful
- where we have stateful apps we want to scale up: add resources: don't want users to go to wrong server
- stateless we can scale out: load balance requests: doesn't matter which server the user connects to

### high availability and fault tolerance

- load balancing: user connects to load balancer, which forwards connection to available server --> high availability
- fault tolerance: no downtime at all: server fails if hard drive or network card fails, so have built-in redundancy
- availability zone as a separate data center
- autoscaling

### monolithic and microservices architecture

- monolithic: different components as part of individual server
  - any updates/failures for a single component can take whole applicaiton down
  - different layers in each server
- microservice: independently deployable unit of code
  - separate components and make sure they're loosely coupled: each component doesn't have to talk directly
    - can buffer data for another component to consume at a later time
  - often organized around business capabilities
  - often using docker containers
  - use of APIs: easier integrations between components
  - independent blocks can be scaled and maintained independently
  - business-oriented architecture: teams may be cross-functional, services reused
  - flexible use of technologies: each service can be written using different technologies
  - speed and agility: fast to deploy and update: easy to include high availability and fault tolerance for each microservice

## AWS Access Control and Networking

- AWS created by amazon to deal with varying demand e.g. holiday season
- pricing:
  - compute: amount of resources such as CPU/RAM/duration
  - storage: quantity of date stored
  - outbound data transfer: moving data out of AWS
- regions around the world: availability zone (1+ data center), always min. 2 availability zones in each region
- can also use AWS outposts to run some services in private data center
- AWS local zone: resources closer to end users to reduce latency
- AWS wavelength zone: low latency to mobile devices/users near mobile data networks

### IAM

- used to authenticate to access resources
- console/api/cli
- 4 types of principals/ identities:
  - users
  - roles: so services can access other services
  - federated users: come from other applications
  - application: needs to access resouces
- IAM principals must be authenticated to send requests
- principal is person/app that can make a request for action/operation on an AWS resource
- use identity/resource-based policy: determine whether to authenticate or not

- methods of authentication
  - username/password/MFA
  - CLI/API: access key ID and secret access key: used for programmatic access

### VPC - virtual private cloud

- place in the cloud where we can put our own resources
- logically isolated portion of the AWS cloud within a region
- private and not seen by anyone else deploying to AWS
- can put our subnets in availability zones and then put our resources in there
- internet gateway used to connect to the internet
- routing in/out of VPC: router in VPC with route table to configure VPC router
- can have multiple VPCs in each region
- each vpc has a block of IP addresses
- CIDR block: classless interdomain routing
- each subnet has a block of IP addresses from the CIDR block
- some services within AWS can be considered public/private
  - private services can have public IP addresses but exist within the VPC e.g. EC2 instance
  - public services have public IP addresses/endpoints only: e.g. dynamoDB, S3, cloudfront, route53
  - accessed through the internet gateway

### security groups and network ACLs

- stateful vs stateless firewalls
  - src/dest ports switch on return traffic
  - stateful firewall allows return traffic automatically
  - stateless firewall needs return traffic to be set manually
- Network ACL are stateless firewalls that apply at the subnet level
  - they apply only to traffic entering/exiting the subnet
  - support allow and deny rules
  - processes rules in order
  - applies to all instances in the subnets its associated with
- Security groups are stateful firewalls that apply to instances/interfaces
  - only supports allow rules
  - evaluates all rules
  - applies to an instance only if associated with a group

## EC2

- virtual cloud servers
- EC2 hosts are managed by AWS
- we then run EC2 instances running windows, linux or mac
- different instance types with differnt cpu,memory, storage, networking
- instance attached to a network, in your VPC, choose subnets assigned to ec2
- each instance has 1+ IP address
  - public IP add: lost when instance is stopped, used in public subnets, no charge, associated with private IP add on instance, can't move
  - private IP add: retained when the instance is stopped, used in public and private
  - elastic IP: static public IP, charged if not used, associated with a private IP address on instance, can be moved between instances and elastic network adapters

### launching ec2 instance

- select instance type, determines hardware profile and cost
- select AMI (amazon machine image) defining configuration of the instance
  - linux, mac or windows
  - backed by EBS snapshots: point-in-time backup of instance
  - can have custom AMI

### access keys and IAM roles with ec2

- so that aws services can communicate between them
- aws cli configured with access keys
- access key will use any permissions assigned to the IAM user
- downsides: access keys stored in plain text on instance and long-term credentials
- better: IAM roles: role is assumed by ec2 instance, no credentials stored on instance
  - assigned using instance profile

### ec2 autoscaling

- what happens if instance fails? autoscaling will replace
- sending metrics to cloud watch
- if cpu>80%, auto scaling group will add an instance
- and remove instances if not needed

### elastic load balancing

- users connect to load balancer, balancer distributes connections to available instances
- constantly checking health of instances
- auto scaling will replace unhealthy instances
- application load balancer: request level
  - layer 7 http and https
  - put instances in target group
  - decides where to route based on information in request header
  - can route based on path, host, query string, source IP
  - targets can be instances, IP addresses, lambda functions, containers
- network load balancer: connection level
  - layer 4 tcp, tls, udp, tcp_udp
  - based on IP protocol data
  - high performance, low latency and TLS offloading at scale
  - can have static/elastic IP
  - targets UDP and static IP addresses
- ALB: web apps with l7 routing, microservices, lambdas
- NLB: TCP and UDP based applications, VPC endpoint services, static IP addresses, low latency

## AWS storage

- EBS elastic block storage - attached to EC2 instances - persistant/long-term configurable storage
  - EBS snapshots of the storage at a given time with any config or data
  - Can create images from the snapshots and use them to create private AMIs and launch other instances with same config

- EFS elastic file storage
    - can attach EC2 instances to file system: instances across availability zones can read/write to same EFS
    - mounted using /efs-mnt, NFS protocol to access, linux only
    - can also connect on-premises client with direct connection/VPN

- S3 object based with rest api
    - amazon simple storage service
    - object store with containers into which files are put -> s3 bucket
    - object is a file you upload -> any files
    - millions of objects in a bucket
    - objects accessed using a URL
    - object consists of key (name), version ID, value (data), metadata, subresources, access control information
    - accessed with REST api -> http protocol to GET/PUT/POST/SELECT/DELETE
    - s3 available via public internet but data in a region unless configured to be replicated
    - OR can also access from VPC via the internet gateway
        - EC2 instances connect using public addresses
        - must be in public subnet, or private subnet with a NAT gateway
    - OR s3 gateway endpoint where instances connect using private addresses
        - if don't want to use public addresses at any point

- file vs object
    - file:
        - data stored in directories
        - hierarchy of directories can be formed
        - file systems mounted to an OS
        - work like local storage
        - network connection maintained
    - object:
        - data stored in buckets
        - flat namespace
        - hierarchy can be mimicked with prefixes
        - accessed by REST api and cannot be mounted
        - network connection completed after each request

## AWS Database Services

- amazon relational database service RDS - runs with most relational database systems
    - managed relational database (updates,patching performed by AWS in window that you can define)
    - runs on EC2 so you choose the instance type
    - Amazon Aurora (AWS own relational db), mysql, postgresql, mariaDB, oracle, microsoft sql server
    - can scale up: increase instance type stats: scale for reads and writes
    - horizontal scaling with disaster recovery
        - multi-AZ: creates passive standby used for disaster recovery: synchronous replication
        - read replica (async replication): used for scaling database queries
        - application servers can read from read replicas and write to master

- aws dynamoDB - noSql and serverless
  - fully managed, creating tables on existing database, key-value type of database
  - offers seamless, horizontal scaling - no downtime if change performance characteristics
  - data is multiplicated around several AZs in a region
  - structure:
    - table
    - item (row)
    - attributes
  - can use DAX to reduce latency for dynamodb

## Automation and Devops

- infrastructure as code to automate the deployment of infra
- cloudformation: infra patterns defined in template file using code
- define it once and then reuse
- cloudformation builds infra according to template
  - template: text file with instructions
  - stack: envi described by template and created/updated/deleted as a single unit
  - stackset: extends stacks by modifying stacks across account and regions in 1 operation
  - change set: summary of proposed changes to tyour stack - preview on how changes might impact resources before implementing
- platform as a service: elastic beanstalk
  - just the code and data, don't manage OS and apps
  - PaaS manages the rest for us
  - upload zipfile and creates beanstalk environment
  - 'web apps made easy'
- CI/CD
  - aws codecommit - similar to github - source control
  - aws codebuild - builds/tests code - jenkins
  - aws codedeploy - deploys to instances in environment - ansible
  - aws codepipeline - manages the three

## DNS, Caching and Performance

- Route 53 - DNS
  - domain registration
  - hosted zone - created on registration
    - holds records belonging to a domain which need resolution
    - A record - ip address for a name
  - health checks - checks endpoints to make sure accessible
  - traffic flow
  - intelligent dns
    - simple: simple
    - failover: health checks, if primary down send to secondary
    - geolocation: route to closest region
    - geoproximity: to closest region with geographic area
    - latency: tries to calculate lowest latency route to resources
    - multivalue answer: similar to load balancing
    - weighted: relative weights to determine route - e.g. a/b tests
- cloudfront CDN
  - location where static files are cached to get content closer to users
  - cloudfront origin: s3 or ec2
  - distribution to edge location
  - edge location around the world
- global accelerator - helps direct users to best endpoint and decrease latency
  - leverages cloudfront infrastructure
  - user traffic ingresses using closest edge location
  - from edge location goes to global accelerator network -
  - static anycast ip addresses
  - traffic traverses the aws global network
  - users redirected to another endpoint if problem
  - can use other ports outside of http/https

## containers and serverless computing

- serverless = you don't manage the underlying servers
- docker containers on amazon ECS
  - ECS cluster logical grouping of tasks (running docker container) or services
  - task defniition: blueprint describing how docker container should launch using images
    - amazon elastic container registry stores images
  - services used to maintain a desired count of tasks
  - ec2 launch type with auto scaling
  - or fargate - serverless and auto scaling - don't have to manage underlying instances
- aws lambda - serverless compute service
  - developer uploads some code
  - only pay for function execution: based on time/memory
  - every occurs from cli, api, sdk or trigger
  - code is executed
  - max execution time is 15 minutes, you can have concurrent executions
- application integration services for decoupling
  - event-driven architecture
  - SNS simple notification service
    - publishers send information to topics
    - subscribers subscribe to topics
    - push model - subscribers waiting for event in topics
    - e.g. notification email
  - SQS simple queue service
    - direct app tier polls SQS when ready
    - don't lose any messages
    - lambda, ecs etc.
- amazon eventbridge
  - event sources: aws, custom, saas
  - eventbridge event bus decides what to do with an event in event stream
- amazon api gateway
  - create http/rest/website apis
  - single application entry point, microservices behind
  - published api, method request, integration request, integration request maps request parameters of method request to format required by backend
    - endpoint, integration response, method response maps status codes, headers, payload into format for client
