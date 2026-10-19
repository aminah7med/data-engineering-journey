# 13. Consistency and Replication

Consistency describes what reads are allowed to observe after writes and failures. The exact meaning depends on the system and its configured read/write guarantees. Replication maintains copies of data on multiple nodes; it can improve availability and resilience, but it does not replace backups and can introduce lag or failover behavior.

## MongoDB replica sets

> **MongoDB-specific:** a replica set has one primary that accepts writes and secondary members that replicate the primary's oplog. Elections can choose a new primary after failure. Read preference, write concern, and read concern influence the guarantees requested and observed.

For example, acknowledging a write after a majority of voting members confirm it differs from acknowledging only at the primary. Stronger acknowledgement may improve durability expectations but can increase latency or fail during unavailability. Review the actual deployment and configuration before relying on a guarantee.

## CAP theorem, accurately

CAP concerns behavior during a network partition in a distributed system: a system must trade off between always returning a response (availability) and returning a response consistent with the single-copy/linearizable view (strong consistency) for affected operations. Partition tolerance is not a convenient optional feature for a system that must continue across network splits; the meaningful trade-off is how it behaves when a partition occurs.

CAP does not say that a database permanently chooses only two of three properties in all conditions. Without a partition, consistency and availability may both be provided. CAP's “consistency” is not the same as every database use of that word, and real products expose nuanced, operation-level choices.

## Engineering implications

- Define acceptable stale reads and acknowledged-write loss explicitly.
- Distinguish replication from backup, retention, and disaster recovery.
- Test failover and recovery procedures.
- Make downstream ingestion tolerant of retries and duplicate delivery.

See [MongoDB replication documentation](https://www.mongodb.com/docs/manual/replication/) for product-specific details.
