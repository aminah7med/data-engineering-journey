# 14. Partitioning and Sharding

Partitioning divides a dataset into parts. A system can partition data within one machine or distribute partitions across machines. Sharding is a form of horizontal partitioning across multiple servers. It can increase aggregate storage and capacity when the workload and shard key distribute well, but it adds routing and operational complexity.

## MongoDB sharding

> **MongoDB-specific:** a sharded cluster routes operations through `mongos`; shard-key values determine where documents are stored. MongoDB supports ranged and hashed shard-key strategies, with different implications for range queries and distribution.

Shard-key choice influences distribution, hot spots, targeted queries, and data movement. A monotonically increasing key can concentrate writes depending on the design. A highly cardinal key can distribute data but may not support needed query patterns efficiently. Measure expected volume, write distribution, and filters before deployment.

## Partitioning is not a magic performance switch

Sharding can add network hops and make some queries scatter across shards. Poorly aligned queries may touch every partition; uneven key distributions create hotspots. Resharding and operational incidents need planning. A single-node or replica-set deployment may be simpler and sufficient for many workloads.

## Design workflow

1. Confirm measurable capacity or availability requirements that require distribution.
2. List common query filters and write keys.
3. Estimate key cardinality, skew, growth, and time-range patterns.
4. Prototype candidate keys and measure distribution and query targeting.
5. Plan monitoring, backups, scaling, and recovery with the chosen product's documentation.

Do not confuse replication with sharding: replication copies data for redundancy; sharding distributes data for scale. A deployment may use both.
