# 14. Partitioning and Sharding

Partitioning is the broad practice of dividing a dataset or table into smaller logical or physical parts. For example, **range partitioning** can place records in date ranges such as one partition per month; **hash partitioning** can apply a hash to a key to spread records across a set of partitions. A database may partition data within one machine or across multiple machines.

Sharding commonly describes distributing partitions across multiple machines (shards), a form of horizontal partitioning. It can increase aggregate storage and capacity when the workload and shard key distribute well, but it adds routing and operational complexity. Terminology varies by database, so verify how a particular product implements partitions and shards.

Partitioning and sharding describe how a dataset is divided and placed; replication describes maintaining copies of data on multiple nodes. Replication does not divide the dataset into independent subsets, and partitioning does not by itself create redundant copies. A distributed deployment can combine sharding and replication, with each shard replicated for availability.

## MongoDB sharding

> **MongoDB-specific:** a sharded cluster routes operations through `mongos`; shard-key values determine how documents are distributed among shards. MongoDB splits sharded data into chunks and balances those chunks across shards. It supports ranged and hashed shard-key strategies, with different implications for range queries and distribution.

Shard-key choice influences distribution, hot spots, targeted queries, and data movement. A monotonically increasing key can concentrate writes depending on the design. A hashed key can spread values but may not support range queries efficiently. Cardinality alone does not guarantee a good key: consider value skew, expected growth, write patterns, and the filters used by common queries. Measure candidate keys and query targeting before deployment.

## Partitioning is not a magic performance switch

Sharding can add network hops and make some queries scatter across shards. Poorly aligned queries may touch every partition; uneven key distributions create hotspots. Resharding and operational incidents need planning. A single-node or replica-set deployment may be simpler and sufficient for many workloads.

## Design workflow

1. Confirm measurable capacity or availability requirements that require distribution.
2. List common query filters and write keys.
3. Estimate key cardinality, skew, growth, and time-range patterns.
4. Prototype candidate keys and measure distribution and query targeting.
5. Plan monitoring, backups, scaling, and recovery with the chosen product's documentation.

Do not confuse partitioning, sharding, and replication: partitioning divides a dataset into parts; sharding commonly distributes those parts across machines for horizontal scale; replication copies data for redundancy and availability. A deployment may partition data locally, shard across machines, replicate each shard, or use only some of these approaches as its requirements dictate.
