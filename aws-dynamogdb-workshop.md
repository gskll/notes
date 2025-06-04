dynamob

OLTP usecases

partition key - primary key - determines data distribution
optional sort key - forms composite primary key with partition key - for querying - modeling 1:n relationships

partition key must be unique if acting as primary key (key/value access) but if composite with sort key can be duplicated

partitions stored under hood as bit tree

each query will have max 1mb response with paged responses

dynamo api

- batch… will return failures
- transact… is all or nothing - if one fails nothing returns/gets written
- scan - recommended to never use - dangerous - can remove permissions to scan in IAM - gets very expensive

PartiQL is sql-compatible query language for dynamo - stops you from shifting to nosql mindset by using relationship language

global secondary index - alternate partition and sort key to create different composite keys for querying - can also add attribute - as if you had a separate table with the columns reversed - 20 GSIs per tabled
RCU/WCUs provisioned separately for GSIs
can define the attributes that you want for an index
GSIs can be created at any point, Local secondary index have to be created with the table
GSIs can also be used as a filter - if item added with missing GSI attribute will be ignored

LSI - lots of limitations - only 5/table, has to be created with table, RCU/WCU consumed from base table - but consistent

LSI - item collection <= 10GB - this size limit only exists on the table if there is an LSI - strong consistency
GSI no size limits = eventual consistency
item collection is all items with the same partition key

two types of costs - data and operations - index creation is operations

O1 partitioning - hash on partition key

automatic replication in 3 availability zones - quorum 2-3
putitem path goes through request router (containing auth and metadata) then to db in same availability zone then replicated

heartbeats are the health pings from leaders

get item - if strong consistency goes straight to the leader, for eventual consistency goes to any node - RCUs are halved for eventual consistency
eventual by default

each table 3k rcu/1k wcu

gsi can have partition key update - will be delete then put, 2x cost

throughput

- on-demand - default - pay for what you use - guaranteed up to twice your previous peak for maximum throughput
- provisioned - requires monitoring - steady workloads with gradual ramps - cheaper

can set TTL with no cost

can change table class - standard-infrequenet access table with lower cost

RCU - 10 units is 10 * 8kb / second
WCU - 5 units is 5 *1kb / second

The highest level of abstraction in DynamoDB is a Table (there isn't a concept of a "Database" that has a bunch of tables inside of it like in other NOSQL or RDBMS services). Inside of a Table you will insert Items, which are analogous to what you might think of as a row in other services. Items are a collection of Attributes, which are analogous to columns. Every item must have a Primary Key which will uniquely identify that row (two items may not contain the same Primary Key). At a minimum when you create a table you must choose an attribute to be the Partition Key (aka the Hash Key) and you can optionally specify another attribute to be the Sort Key.
If your table is a Partition Key only table, then the Partition Key is the Primary Key and must uniquely identify each item. If your table has both a Partition Key and Sort Key, then it is possible to have multiple items that have the same Partition Key, but the combination of the Partition Key and Sort Key will be the Primary Key and uniquely identify the row. In other words, you can have multiple items that have the same Partition Key as long as their Sort Keys are different. Items with the same Partition Key are said to belong to the same Item Collection.

Operations in DynamoDB consume capacity from the table. When the table is using On-Demand capacity, read operations will consume Read Request Units (RRUs) and write operations will consume Write Request Units (WRUs). When the table is using Provisioned Capacity, read operations will consume Read Capacity Units (RCUs) and write operations will consume Write Capacity Units (WCUs).

Design patterns

- single table vs multiple table - depends how linked the data is - if separate and used separately in different apps then advantages for having multiple tables in terms of provisioning/configuration
- with single table makes sense if data is used together to be able to do less queries

- think use case and access pattern
- partition key and composite sort keys, fallback to filtering or indexes

- for high write throughput and low cardinality e.g. voting for candidates

  - write shard the partition key to increase throughput then collect all shard data in parallel
  - convert data to have high cardinality e.g. uuid and then aggregate in second phase
  - or use index but careful of scaling

- read distribution imbalance ‘popular items’
- add caching with DAX - define memory/size of cache cluster

DynamoDB streams - ordered stream of item changes - exactly once & strictly ordered by key

- can read the stream for free from a lambda
  alternative kinesis data streams - much more scalable - can configure how long data is kept - with dynamodb streams it’s always 24h
- more complex stream picking but you lose the ordering

- as read units is based on size make sure frequent operations don’t include the data if not necessary - can use indices
- vertical partitioning with sort keys to reduce item size

hierarchical data structures - use composite sort keys to define the hierarchy

transactions api - up to 100 items

- not for maintaining normalized data
- atomic writes of related data
