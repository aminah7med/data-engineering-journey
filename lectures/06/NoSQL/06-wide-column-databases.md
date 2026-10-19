# 06. Wide-Column Databases

Wide-column databases organize data by partition and row keys, with groups of columns that can vary across rows. They are designed for distributed storage and access patterns that can be served efficiently from a chosen partition key. Their terms and implementation details vary by product.

## Typical workload

A telemetry service could store readings keyed by `(device_id, time_bucket)` and cluster each device's events by timestamp. Queries for a device's readings over a time interval can be efficient when that key design matches the query.

## Design trade-offs

Partition keys determine data placement and must avoid oversized or hot partitions. Query patterns often need to be known in advance; arbitrary joins and ad hoc relational queries are usually not the primary design goal. Data may be duplicated into multiple tables to serve distinct access paths, which adds write and consistency work.

Do not pick a wide-column system merely because a dataset is large. Validate partition distribution, query patterns, consistency, retention, and operational requirements with the specific product.
