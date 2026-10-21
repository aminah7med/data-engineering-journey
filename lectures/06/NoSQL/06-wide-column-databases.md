# 06. Wide-Column Databases

Wide-column databases organize data by partition and row keys, with groups of columns that can vary across rows. They are designed for distributed storage and access patterns that can be served efficiently from a chosen partition key. Their terms and implementation details vary by product.

This differs conceptually from a relational table with a fixed set of columns and general-purpose joins. Wide-column systems organize and distribute rows around keys and workload-specific access paths. The schema and query design therefore need to account for partition keys, clustering or row ordering, and the fields that a query retrieves. “Wide-column” does not mean that every row must have millions of columns.

## Cassandra and HBase

Apache Cassandra and Apache HBase are both distributed wide-column systems, but they are not identical:

- **Cassandra** uses a peer-to-peer architecture and Cassandra Query Language (CQL), a SQL-like interface. Its tables are designed around partition keys and query patterns; it supports configurable consistency levels for many operations.
- **HBase** is modeled after Google's Bigtable design and commonly runs with the Hadoop ecosystem, using HDFS for persistent storage. Applications typically use HBase client APIs (including Java APIs), while operators can use the HBase shell. Its data is organized into tables, rows, column families, and cells.

These architectural and interface differences affect deployment, consistency behavior, integration, and operations. Check the specific product documentation and version when selecting or operating either system.

## Typical workload

A telemetry service could store readings keyed by `(device_id, time_bucket)` and cluster each device's events by timestamp. Queries for a device's readings over a time interval can be efficient when that key design matches the query.

High-volume event ingestion, time-series lookups, or recommendation features can be candidates when the workload matches the system's write and partition model. For example, a recommendation service might store precomputed user-item interactions for predictable key-based retrieval; discovering novel relationships or performing broad historical analytics may fit other systems better. Wide-column databases are not automatically analytical databases or replacements for warehouses and lakehouses.

## Design trade-offs

Partition keys determine data placement and must avoid oversized or hot partitions. Query patterns often need to be known in advance; arbitrary joins and ad hoc relational queries are usually not the primary design goal. Data may be duplicated into multiple tables to serve distinct access paths, which adds write and consistency work.

Do not pick a wide-column system merely because a dataset is large. Validate partition distribution, query patterns, consistency, retention, and operational requirements with the specific product.
