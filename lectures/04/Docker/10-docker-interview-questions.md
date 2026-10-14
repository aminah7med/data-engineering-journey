# 10 — Docker Interview Questions

## Conceptual questions

1. **What is Docker?** A platform for building, distributing, and running applications in isolated containers from images.
2. **Image vs container?** An image is a layered template; a container is a configured running or stopped instance with a writable layer.
3. **Container vs VM?** Containers share the relevant host kernel; a VM runs a guest OS/kernel on virtualized hardware.
4. **What is a registry?** A service that stores and distributes images. Tags are mutable references; digests identify exact content.
5. **What is a Dockerfile?** A text build recipe that produces an image; it is not YAML.
6. **CMD vs ENTRYPOINT?** ENTRYPOINT defines the executable; CMD supplies defaults or a default command. Runtime arguments replace CMD and commonly become ENTRYPOINT arguments.
7. **COPY vs ADD?** COPY copies context files. ADD has extra archive and remote-source behavior; prefer COPY unless those features are needed.
8. **What does EXPOSE do?** Documents a container port; it does not publish a host port.
9. **Named volume vs bind mount?** Docker-managed storage with container-independent lifecycle vs a specific host path mounted into a container.
10. **How does port mapping work?** `-p host:container` forwards traffic from the host port to a container port.
11. **How do Compose services find each other?** On a shared Compose network, use service-name DNS and the service's container port.
12. **Why is localhost misleading?** It resolves to the current network namespace: inside a container it is that container, not another service or the host.
13. **What does Compose provide?** A declarative way to configure and operate related containers, networks, and volumes for an application environment.
14. **Does depends_on guarantee readiness?** No. Use health conditions where suitable and implement client retries.
15. **How does build cache work?** Docker reuses unchanged build steps; a changed input invalidates that layer and subsequent layers.
16. **Why multi-stage builds?** They separate build tooling from runtime artifacts, often reducing final image size and attack surface.
17. **How handle secrets?** Keep them out of source and image layers; use runtime secret facilities or a secret manager with restricted access and rotation.
18. **What happens to container data on removal?** Its writable layer is removed; separately mounted volume data remains unless that volume is removed.
19. **How does Docker help data engineering?** It provides repeatable local databases and brokers, packages jobs, and standardizes CI. It does not replace data-system operations or orchestration needs.
20. **Docker vs Kubernetes?** Docker builds and runs containers; Kubernetes orchestrates workloads across a cluster. Compose supports multi-container environments and is not a universal Kubernetes replacement.

## Hands-on tasks

- Run Nginx in the background on host port 8080, inspect logs, and remove it safely.
- Build a Python image; change only app source and explain which build layers are reused.
- Demonstrate that container-layer data disappears after removal while named-volume data persists.
- Create two containers on a user-defined network and resolve one by name.
- Use Compose to start an app and database, inspect health/logs, and explain why service DNS uses `db:3306`.

## Scenario questions

1. **The API starts before MySQL accepts connections. How do you fix it?** Add a database health check, configure Compose health-based dependency ordering, and keep application retry/backoff because transient failures can still occur.
2. **A recreated database lost its records. Why?** Data may have been written to the container layer, the wrong mount path may have been used, or the volume may have been removed. Verify mounts and restore from backup if needed.
3. **The host can open the app but the app cannot reach MySQL on localhost.** Use the database service name and internal port from the app container; host publishing is unnecessary for service-to-service traffic.
4. **An image is unexpectedly large.** Inspect layers, exclude build context files, use a suitable base and multi-stage build, and avoid retaining build-only tools/caches.

## Advanced questions

- **Why can a digest improve reproducibility?** It identifies exact image content even if a human-readable tag later moves; updates still need controlled adoption.
- **What does rootless Docker change?** It runs the daemon and containers without host-root privileges, reducing some risks while changing operational constraints and feature availability.
- **What is the writable layer's performance implication?** It is convenient but often less suitable for durable or write-intensive data than a deliberately managed mount; actual performance depends on storage driver and host.
- **How do you reduce supply-chain risk?** Use trusted bases, pin and update inputs, scan, verify provenance where available, minimize privileges, and control registry access.

Answers are concise prompts for discussion; be ready to support them with commands and a concrete example.
