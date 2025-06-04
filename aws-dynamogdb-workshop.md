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

each partition 3k rcu/1k wcu

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




## Advanced DynamoDB Insights & Optimization Strategies

Here are some key takeaways and advanced considerations for optimizing DynamoDB usage:

### Core Mechanics & Nuances
* **Primary Keys Deep Dive:**
    * The **partition key** is fundamental for data distribution.
    * A **composite primary key** (partition key + sort key) is powerful for complex querying and modeling 1:N relationships within an item collection.
* **Indexing Strategies:**
    * **GSIs (Global Secondary Indexes)** offer flexible querying on alternate keys, acting like separate, denormalized views of your data. Remember they have their own provisioned throughput and are eventually consistent. GSI key updates incur double the write cost (delete old, put new).
    * **LSIs (Local Secondary Indexes)** provide strongly consistent reads on the same partition key but with a different sort key. However, they must be created with the table, share the base table's throughput, have a 5-per-table limit, and impose a 10GB item collection size limit on the table.
    * GSIs can be used for filtering: if an item lacks a GSI attribute, it's not indexed, which can be a deliberate design choice.
* **API Call Behavior:**
    * `BatchWriteItem`/`BatchGetItem`: Individual operations within a batch can fail, and the API will return details on failures.
    * `TransactWriteItems`/`TransactGetItems`: These are all-or-nothing atomic operations across up to 100 items. If one part fails, the entire transaction is rolled back. Crucially, they are *not* for maintaining normalized relational data structures.

---
### Performance & Cost Optimization
* **Throughput Management:**
    * **On-Demand:** Default and simplifies capacity management. It accommodates peaks by allowing bursts up to twice your previous peak. Ideal for unpredictable workloads.
    * **Provisioned:** Can be more cost-effective for steady, predictable workloads with gradual ramps but requires monitoring and auto-scaling configuration.
* **Read/Write Cost Factors:**
    * **RCUs/WCUs:** Understand the calculation (e.g., RCUs based on 4KB eventually consistent reads or 8KB strongly consistent; WCUs on 1KB writes). Eventual consistency reads halve RCU consumption.
    * **GSI Costs:** GSIs have separate RCU/WCU provisioning. Updates to attributes that are part of a GSI key will incur write costs on both the base table and the GSI.
* **Data Size & Operations:**
    * Queries return up to 1MB of data per request, with pagination for larger result sets.
    * Minimize item size for frequently accessed data, especially in queries, as RCUs are based on data scanned.
* **Caching with DAX:** For read-heavy workloads with popular items experiencing distribution imbalance, DynamoDB Accelerator (DAX) provides an in-memory cache for microsecond latency.

---
### Advanced Design Patterns
* **Single Table vs. Multiple Tables:**
    * **Single Table:** Often preferred when data is used together, enabling fewer queries to fetch related information.
    * **Multiple Tables:** Can be advantageous if data is logically separate, used by different applications, or requires distinct provisioning/configuration.
* **Write Sharding for High Cardinality:**
    * To handle high write throughput on low-cardinality partition keys (e.g., voting), shard the partition key by adding a suffix.
    * This distributes writes across more logical partitions, increasing throughput. Reads require aggregating data from all shards in parallel.
* **Vertical Partitioning with Sort Keys:**
    * Break down large items or complex documents.
    * Store related but distinct pieces of information under the same partition key but with different sort keys. This helps reduce item size for specific access patterns and can make queries more targeted.
* **Modeling Hierarchical Data:**
    * Use composite sort keys with concatenated values to define and query hierarchical relationships efficiently (e.g., `COUNTRY#STATE#CITY`).
* **Streams for Event-Driven Architectures:**
    * **DynamoDB Streams:** Provide an ordered stream of item changes (exactly once, strictly ordered by key within a shard) with a 24-hour retention. Lambdas can process these for free.
    * **Kinesis Data Streams:** Offer more scalability and configurable retention for stream processing but lose the strict per-key ordering if not managed carefully at the application level.

---
### Operational Considerations
* **Scan Operations:** Strongly discourage direct `Scan` operations in production. They are expensive as they read every item in the table. Consider restricting scan permissions in IAM.
* **PartiQL:** While SQL-compatible and useful for ad-hoc queries or exploration, be mindful that over-reliance can hinder a true NoSQL design mindset which focuses on access patterns rather than relational ad-hoc querying.
* **TTL (Time To Live):** A no-cost feature to automatically delete items, useful for managing ephemeral data like sessions or logs.
* **Table Classes:** Consider the **Standard-Infrequent Access (Standard-IA)** table class for tables with large amounts of data that are not frequently accessed to significantly reduce storage costs.
