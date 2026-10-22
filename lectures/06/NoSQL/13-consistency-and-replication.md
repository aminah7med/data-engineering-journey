# 13. Consistency and Replication

In a distributed system, consistency describes which values reads may observe in relation to completed writes and to one another. The exact guarantees depend on the database, the operation, and its configuration. For example, a read served by a replica that has not yet applied a recent write may return an older value, called a stale read.

Replication lag is the delay before a replica applies a recent change; by itself, lag is not data loss. Data loss means that a change is no longer recoverable, for example if an acknowledged write is not present after a failure or is overwritten or deleted. The risk depends on which writes were acknowledged, replication progress, durability settings, and recovery procedures. Read and write settings affect what the application can observe and what acknowledgement it receives; they do not make every failure impossible.

Replication maintains copies of data on multiple nodes. Copies can help a system continue serving data after an individual node fails and provide redundancy, but replication can also copy accidental deletes or corruption. Replication is not a backup strategy: backups should be protected, retained, and tested for restoration independently.

## MongoDB replica sets

> **MongoDB-specific:** a replica set has one primary that normally accepts writes and secondary members that replicate changes from the primary's operation log (oplog). Replication is generally asynchronous, so a secondary may temporarily be behind the primary.

If the primary becomes unavailable, eligible voting members hold an election to select a replacement. Members exchange votes, and an eligible candidate needs votes from a majority of the replica set's voting members to become primary. A member that cannot reach a majority cannot safely elect a primary; the replica set may become read-only for writes until a primary can be elected. Arbiters can vote but do not store data. Membership, priority, and availability affect eligibility and election outcomes.

MongoDB settings shape read and write guarantees:

- **Write concern** controls the acknowledgement requested for a write. For example, `w: "majority"` requests acknowledgement from a majority of voting members. It can reduce the chance that a failover rolls back an acknowledged write, but may increase latency or fail when a majority is unavailable.
- **Read preference** selects which replica-set members may serve a read. Reads from secondaries can spread load but may return stale data while replication catches up. Reading from the primary avoids that particular secondary-lag path but does not alone define the full read guarantee.
- **Read concern** controls the consistency and isolation properties of data returned by a read. The appropriate guarantees depend on the application's needs and the deployment.

These controls are distinct and must be chosen together with the application's consistency and availability requirements. They do not make replicas synchronous or eliminate every data-loss scenario. Review the MongoDB version, topology, and configuration before relying on a guarantee.

## Multi-master concepts and Cassandra coordination

**Multi-master architecture** is a general term for a distributed design in which more than one node can accept writes, rather than routing all writes through one designated primary. It does not mean that all nodes necessarily store every record, nor does it define how concurrent writes are reconciled. Systems may coordinate, reject, merge, or resolve competing writes according to their data model and consistency rules.

For example, two application regions might concurrently update the same customer's preferred language while disconnected. When the updates meet, the system needs a defined outcome—such as choosing a version by timestamp, applying a domain-specific merge, or surfacing a conflict for application handling. “Last write wins” is one possible policy, not a universal behavior, and timestamps or arrival order may not match business intent.

Apache Cassandra uses a peer-to-peer architecture without a single primary for the cluster. A client can connect to any node; that node acts as a **coordinator** for the request, determines the replicas responsible for the partition key, and coordinates with them according to the requested consistency level. The coordinator is not a master and does not have to own the data. Any node can coordinate requests, while replicas store the relevant partitions. Cassandra's replication and consistency settings determine how many replicas must respond for reads and writes; concurrent updates to the same data are reconciled according to Cassandra's rules, commonly using cell timestamps and last-write-wins behavior. Applications should understand these semantics and use suitable consistency levels and data modeling rather than assuming arbitrary concurrent writes are merged safely.

This differs from a MongoDB replica set, where one primary accepts writes at a time and secondaries replicate its oplog. MongoDB deployments can shard data, but each shard is typically a replica set with its own primary; this is not the same as every node in a MongoDB replica set accepting writes as a multi-master system.

## CAP theorem, accurately

CAP concerns behavior during a network partition in a distributed system: a system must trade off between always returning a response (availability) and returning a response consistent with the single-copy/linearizable view (strong consistency) for affected operations. Partition tolerance is not a convenient optional feature for a system that must continue across network splits; the meaningful trade-off is how it behaves when a partition occurs.

CAP does not say that a database permanently chooses only two of three properties in all conditions. Without a partition, consistency and availability may both be provided. CAP's “consistency” is not the same as every database use of that word, and real products expose nuanced, operation-level choices.

## Engineering implications

- Define acceptable stale reads and acknowledged-write loss explicitly.
- Distinguish replication from backup, retention, and disaster recovery.
- Test failover and recovery procedures.
- Make downstream ingestion tolerant of retries and duplicate delivery.

See [MongoDB replication documentation](https://www.mongodb.com/docs/manual/replication/) and [write concern documentation](https://www.mongodb.com/docs/manual/reference/write-concern/) for product-specific details.
