# pip & Dependencies

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**pip** is Python's standard package installer. It allows developers to install, upgrade, remove, and inspect third-party Python packages.

A **dependency** is a package or component that a project needs to run correctly. For example, a data engineering project may depend on Pandas for data manipulation, SQLAlchemy for database interaction, and a MySQL driver for connecting to a MySQL database.

Managing dependencies correctly helps make projects reproducible, maintainable, and easier to deploy across development, testing, and production environments.

This section covers pip commands, dependency files, version constraints, package conflicts, and dependency management practices used in Python projects.

---

## 🧠 Concepts

### 1. What Is pip?

`pip` is a package installer for Python. It downloads and installs packages from package indexes such as PyPI, the Python Package Index.

Common operations include:

- Installing a package.
- Upgrading an installed package.
- Uninstalling a package.
- Inspecting installed packages.
- Installing dependencies listed in a file.

**Best practice:** Use `python -m pip` to make it clear which Python interpreter is running pip.

```bash
python -m pip --version
```

This displays the pip version and helps identify the Python installation associated with it.

### 2. What Is a Python Package?

A package is reusable Python code that provides functionality you can import into your application.

Examples include:

| Package | Typical Use |
|---|---|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `sqlalchemy` | SQL database abstraction and SQL toolkit |
| `pymysql` | MySQL database connectivity |
| `requests` | HTTP requests |
| `pytest` | Automated testing |
| `python-dotenv` | Loading configuration from `.env` files |

Installing a package and importing it are different operations.

```bash
python -m pip install pandas
```

Then, inside Python:

```python
import pandas as pd

print(pd.__version__)
```

The package is installed into an environment; the `import` statement makes its functionality available to Python code.

Note that the distribution name used by pip and the import name used in Python are not always identical.

### 3. What Is a Dependency?

A dependency is something a project requires to operate.

Consider this example:

```python
import pandas as pd
import sqlalchemy
```

The project directly depends on Pandas and SQLAlchemy because its code imports them.

However, those packages may also require other packages to function. These are called **transitive dependencies**.

There are two main categories:

- **Direct dependencies:** Packages your project explicitly uses.
- **Transitive dependencies:** Packages required by your direct dependencies or other installed packages.

For example:

```text
Your Application
├── pandas
│   └── numpy
└── sqlalchemy
```

This diagram is illustrative; the actual dependency tree depends on the package versions and installation environment.

### 4. PyPI and Package Installation

PyPI is the default public package index commonly used by pip.

When you run:

```bash
python -m pip install pandas
```

pip typically resolves a compatible package version and its dependencies, downloads the required distributions, and installs them into the selected environment.

Package installation can also involve building packages from source when a suitable prebuilt distribution is unavailable.

For production systems, use trusted package sources and review package names before installing them.

### 5. Installing, Upgrading, and Removing Packages

Install a package:

```bash
python -m pip install pandas
```

Upgrade a package:

```bash
python -m pip install --upgrade pandas
```

Uninstall a package:

```bash
python -m pip uninstall pandas
```

Inspect a package:

```bash
python -m pip show pandas
```

List installed packages:

```bash
python -m pip list
```

These commands operate on the environment associated with the selected Python interpreter.

### 6. Dependency Versioning

Packages evolve over time. A newer release may add features, fix bugs, change behavior, or introduce incompatibilities.

Common version specifications include:

```text
pandas==2.2.3
pandas>=2.2
pandas>=2.2,<3.0
pandas~=2.2.0
```

Their general meanings are:

| Specification | Meaning |
|---|---|
| `==2.2.3` | Require exactly version 2.2.3 |
| `>=2.2` | Require version 2.2 or newer |
| `>=2.2,<3.0` | Require a version in the specified range |
| `~=2.2.0` | Allow compatible releases within the corresponding patch-level range |

These versions are examples, not recommendations for the latest release.

**Important:** Version constraints are not all equally strict. A broad lower bound can allow a future release that introduces breaking changes. Choose constraints according to the project's compatibility and release strategy.

### 7. The `requirements.txt` File

`requirements.txt` is a commonly used file for declaring or recording Python dependencies.

Example:

```text
pandas==2.2.3
sqlalchemy>=2.0,<3.0
pymysql>=1.1,<2.0
```

Install the listed requirements:

```bash
python -m pip install -r requirements.txt
```

The `-r` option tells pip to read requirements from a file.

A requirements file can contain exact pins, version ranges, and other supported pip requirement specifications. Its contents should match the needs of the project.

### 8. `pip freeze` vs `pip list`

Both commands inspect packages in the current environment, but they serve different purposes.

| Command | Purpose |
|---|---|
| `python -m pip list` | Displays installed packages in a human-readable list |
| `python -m pip freeze` | Outputs installed packages in a requirements-style format |

Example:

```bash
python -m pip freeze
```

Save the output to a file:

```bash
python -m pip freeze > requirements.txt
```

**Important distinction:** `pip freeze` records installed distributions and their versions. It does not automatically identify which packages your application directly needs versus which packages were installed as transitive dependencies.

For a small project, this is a useful snapshot. For larger projects, explicitly maintaining direct dependencies and using a lockfile or dependency manager may provide clearer dependency management.

### 9. Dependency Conflicts

A dependency conflict occurs when installed packages have incompatible requirements.

For example:

```text
Package A requires Library X < 2.0
Package B requires Library X >= 2.0
```

If both requirements must be satisfied in the same environment, there is no compatible version of Library X.

Possible solutions include:

- Using compatible package versions.
- Upgrading or replacing a conflicting package.
- Separating projects into different virtual environments.
- Reviewing package compatibility before upgrading.
- Recreating the environment from a known dependency specification.

Do not solve every conflict by blindly upgrading all packages. First identify the incompatible requirements and understand their impact.

### 10. Dependency Management Tools

pip is the package installer, but other tools can help manage dependencies and project environments.

| Tool | Primary Role |
|---|---|
| `pip` | Installs and manages Python packages |
| `venv` | Creates lightweight virtual environments |
| `pip-tools` | Helps compile and synchronize pinned dependencies |
| Poetry | Manages project metadata, dependencies, and environments |
| uv | Provides fast Python package and project management workflows |

These tools have overlapping capabilities, but they are not identical. A project should select a consistent workflow instead of mixing several dependency-management systems without a clear reason.

### 11. Requirements Files vs Lockfiles

A dependency declaration and a lockfile are related but distinct concepts.

- A **dependency declaration** describes the packages a project needs and the acceptable versions.
- A **lockfile** records a resolved dependency set, often including exact versions and additional metadata.

For example, a project may declare a compatible range for Pandas while a lockfile records the exact version selected for a reproducible installation.

The precise behavior depends on the package-management tool. A plain `requirements.txt` can contain exact pins, but it does not automatically provide all the guarantees of every dedicated lockfile format.

### 12. Development Dependencies

Some packages are required only during development or testing.

Examples include:

- `pytest` for testing.
- `ruff` for linting.
- `black` for formatting.
- `mypy` for static type checking.

Separating development dependencies from runtime dependencies helps keep production environments focused on what the application actually needs.

The separation mechanism depends on the chosen tool and project structure.

---

## 💻 Syntax & Examples

### Example 1: Set Up a Project Environment

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip --version
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
```

Using a virtual environment keeps the project's package installations separate from unrelated Python projects.

### Example 2: Install Project Dependencies

```bash
python -m pip install pandas sqlalchemy pymysql
```

Verify the installations:

```bash
python -m pip show pandas
python -m pip list
```

Check imports:

```bash
python -c "import pandas, sqlalchemy, pymysql; print('Imports successful')"
```

### Example 3: Create a Requirements File

Capture the current environment:

```bash
python -m pip freeze > requirements.txt
```

Review the file before committing it.

A generated file may contain packages unrelated to the project's direct requirements if the environment contains unrelated installations.

For a cleaner project, maintain an explicit list of direct dependencies or use a tool that distinguishes direct dependencies from transitive ones.

### Example 4: Install from a Requirements File

In a clean virtual environment:

```bash
python -m pip install -r requirements.txt
```

Then verify that the application and tests run successfully.

### Example 5: Inspect Dependency Relationships

Use:

```bash
python -m pip show pandas
```

This displays package metadata, including its declared dependencies.

For a dependency consistency check:

```bash
python -m pip check
```

`pip check` reports whether installed packages have compatible declared dependencies. It does not prove that the application behaves correctly at runtime.

### Example 6: Upgrade a Package Carefully

Inspect the current version:

```bash
python -m pip show pandas
```

Upgrade within the intended constraints:

```bash
python -m pip install --upgrade pandas
```

Then run the project's tests:

```bash
python -m pytest
```

This example assumes `pytest` is installed and that the project has tests. If an upgrade breaks compatibility, investigate the dependency changes and restore a known-good set of versions.

### Example 7: Example Project Structure

```text
data_pipeline/
├── .venv/
├── src/
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

Example `.gitignore` entries:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
.pytest_cache/
```

The `.env` entry helps prevent accidental commits of local configuration and credentials. Review your Git configuration and secret-handling practices rather than relying on `.gitignore` alone.

---

## ⚠️ Common Mistakes

1. **Installing packages into the wrong environment:** Verify the selected interpreter and use `python -m pip`.
2. **Confusing package names with import names:** The name used by pip may differ from the name used in Python code.
3. **Using `pip freeze` as an automatically curated dependency list:** It records installed packages, not just the dependencies your application directly uses.
4. **Leaving every package unpinned without considering compatibility:** Future releases may change behavior.
5. **Pinning every package without a maintenance plan:** Exact pins improve repeatability but can prevent important fixes from being adopted until dependencies are reviewed and updated.
6. **Upgrading packages without testing:** An upgrade may introduce incompatible changes.
7. **Ignoring transitive dependencies:** Your project can break even if you did not directly install or import the package that changed.
8. **Committing virtual environment files:** Commit dependency declarations and setup instructions instead of `.venv/`.
9. **Committing credentials:** Never store passwords, access tokens, or database secrets in requirements files or source code.
10. **Assuming `pip check` guarantees application correctness:** It checks declared dependency compatibility, not every runtime behavior.
11. **Installing packages from untrusted sources:** Check package names and use trusted indexes to reduce supply-chain risk.
12. **Mixing package-management workflows without understanding them:** Decide which files are authoritative for dependencies and how the environment is recreated.

---

## 👨‍💻 Data Engineering Connection

Dependency management is essential for reliable data pipelines because these systems often combine database drivers, data-processing libraries, API clients, testing frameworks, and orchestration tools.

### 1. Managing Pipeline Dependencies

A pipeline might require:

- Pandas for data transformation.
- SQLAlchemy for database interaction.
- A database-specific driver.
- Requests for API ingestion.
- Pytest for automated tests.

Each dependency should be selected and maintained according to the project's requirements.

### 2. Reproducible Pipeline Development

Imagine a pipeline works on your machine but fails on another developer's machine because the two environments contain different library versions.

A clear dependency manifest helps both developers install compatible packages and investigate differences.

For reliable reproduction, document the Python version and relevant external requirements as well.

### 3. DataPulse Example

For DataPulse, dependency management should be part of the repository setup process.

A possible workflow is:

1. Create a virtual environment.
2. Install the packages required by the current project components.
3. Record or lock compatible dependency versions.
4. Commit the dependency-management files.
5. Exclude `.venv/` and local secrets from Git.
6. Recreate the environment from scratch.
7. Run tests to validate the setup.

Only add dependencies that the project actually needs. For example, do not install an Airflow package into the main environment simply because Airflow appears in the planned architecture; first decide how Airflow will be developed and deployed.

### 4. Local Development vs Production

A local development environment may include testing and formatting tools, while a production environment may require only runtime dependencies.

This distinction reduces unnecessary packages in deployment environments and helps clarify what is required to run the application.

### 5. Dependency Management in Docker

Docker images can include the required Python packages as part of the image build.

A simplified Dockerfile might contain:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "src/pipeline.py"]
```

This is an illustrative example, not a complete production Dockerfile. The Python version and dependencies should match the project's compatibility requirements. Production images should also be built, tested, and updated through a controlled process.

A container image packages the runtime environment, but it does not eliminate the need to manage and review dependencies.

---

## 🎯 Interview Questions

### Q1. What is pip?

pip is a Python package installer used to install, upgrade, remove, and inspect packages.

### Q2. What is the difference between a package and a dependency?

A package is a distributable unit of reusable code. A dependency is a package or component that a project requires. A package can itself have dependencies.

### Q3. What is the difference between direct and transitive dependencies?

A direct dependency is explicitly required by the project. A transitive dependency is required by one of its dependencies or another package in the dependency tree.

### Q4. What is the purpose of `requirements.txt`?

It provides a list of Python requirements that pip can install, helping developers recreate the project's package environment.

### Q5. What is the difference between `pip list` and `pip freeze`?

`pip list` presents installed packages for inspection. `pip freeze` produces a requirements-style list of installed distributions and their versions.

### Q6. Why is `python -m pip` often recommended?

It runs pip through the selected Python interpreter, reducing confusion when multiple Python installations or virtual environments exist.

### Q7. What causes dependency conflicts?

Conflicts occur when packages require incompatible versions of the same dependency or when the environment cannot satisfy all declared constraints.

### Q8. Does `pip freeze` create a complete lockfile?

Not necessarily. It records installed package versions, but dedicated lockfile formats may capture additional resolution information and platform-related details.

### Q9. How would you troubleshoot a dependency conflict?

Inspect the error message, identify the incompatible version constraints, check package compatibility, choose a compatible set of versions, recreate or update the environment, and run tests.

### Q10. How do you keep development and production dependencies separate?

Use the dependency-management mechanism supported by the project to distinguish runtime packages from development and testing tools. Install only the necessary groups in each environment.

### Q11. What is the relationship between pip and `venv`?

`venv` creates a virtual environment, while pip installs packages into the environment associated with the selected Python interpreter.

### Q12. Why does dependency management matter in Data Engineering?

Data pipelines rely on multiple libraries and integrations. Controlled dependencies make development more consistent, simplify deployment, and reduce failures caused by incompatible package versions.

---

## 📝 Practice

### Exercise 1: Install and Inspect Packages

1. Create and activate a virtual environment.
2. Install Pandas and SQLAlchemy.
3. Display the installed package versions.
4. Explain the difference between installing and importing a package.

### Exercise 2: Generate a Dependency File

1. Run `python -m pip freeze`.
2. Save the output to `requirements.txt`.
3. Inspect the file.
4. Identify which packages are direct dependencies and which may be transitive.
5. Explain why the generated list may contain more packages than expected.

### Exercise 3: Recreate an Environment

1. Create a fresh virtual environment.
2. Install packages from `requirements.txt`.
3. Run `python -m pip check`.
4. Test the project's imports.
5. Explain why a successful dependency check does not guarantee that the application works correctly.

### Exercise 4: Investigate a Version Conflict

Imagine Package A requires `library-x<2.0`, while Package B requires `library-x>=2.0`.

Answer:

1. Can both requirements be satisfied by one version of Library X?
2. What information would you inspect before changing versions?
3. What are two possible ways to resolve the conflict?
4. Why might separate virtual environments be appropriate for unrelated projects?

### Exercise 5: DataPulse Dependency Plan

Create a dependency-management plan for DataPulse:

1. Identify the direct dependencies needed by the current implementation.
2. Choose a dependency declaration or lockfile strategy.
3. Document the required Python version.
4. Exclude `.venv/` and secrets from Git.
5. Recreate the environment from scratch.
6. Run automated tests after installation.

### Exercise 6: Interview Practice

Explain, without memorizing a definition, how you would make a Python data pipeline's dependencies consistent across local development, CI, and Docker deployment.

Your answer should cover virtual environments, dependency declarations, version constraints, testing, and the production runtime.

---

> **Next Step:** Practice installing packages, generating a dependency file, and recreating a clean environment. Keep the status as `🟡 In Progress` until you can explain and demonstrate the full workflow independently.