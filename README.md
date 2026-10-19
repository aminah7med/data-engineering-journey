# Data Engineering Journey

A concise, evidence-based record of study and practical notes for foundational Data Engineering topics. This repository collects lecture notes, command references, and practical guidance used during learning and practice. It is intended as a navigable study log — not a production codebase.

## Overview

- Purpose: Document learning materials (lecture notes, commands, and exercises) that build practical understanding of data engineering concepts and tooling.
- Audience: Other learners, reviewers, and recruiters who want to see a structured study record and reference materials.
## Learning Roadmap

Explore the learning materials in the following order:

| Topic | Description | Resource |
|---|---|---|
| Data Engineering Fundamentals | Data lakes, data warehouses, OLTP vs. OLAP, schemas, and scalability | [Lecture 01](lectures/01/notes.md) |
| Linux and Shell | Linux fundamentals, permissions, processes, shell scripting, and HDFS examples | [Lecture 02](lectures/02/notes.md) |
| Git and GitHub | Version control, branching, commits, and repository workflows | [Git Notes](lectures/02/git.md) |
| Python | Python fundamentals and topics relevant to Data Engineering | [Python Learning Path](lectures/03/Python/README.md) |
| Docker | Container fundamentals, image building, networking, persistence, and Docker Compose | [Docker Learning Path](lectures/04/Docker/README.md) |
| SQL | Relational databases, query design, SQL for Data Engineering, and practical analytics patterns | [SQL Learning Path](lectures/05/SQL/README.md) |
| NoSQL | NoSQL data models, MongoDB, document design, and Data Engineering practice | [NoSQL Learning Path](lectures/06/NoSQL/README.md) |

Each section contains learning materials and references intended to support practical understanding. Explore the individual folders for detailed notes, exercises, and instructions.

## Technologies represented (based on repository contents)

- Python — primary programming language used in lecture notes and exercises.
- Git / GitHub — detailed notes and workflows in `lectures/02/git.md`.
- Docker — documented in `lectures/04/Docker/README.md` and related exercises.
- HDFS / Hadoop / Spark — discussed in lecture notes as conceptual and command examples (see `lectures/01/notes.md` and `lectures/02/notes.md`).

Note: This repository is a study and notes collection. Technologies are listed because the materials discuss or demonstrate them; this is not a deployable pipeline repository.

## Repository structure (concise)

```
data-engineering-journey/
├── README.md
├── .gitignore
└── lectures/
    ├── 01/                      # Lecture 01 notes (data engineering fundamentals)
    │   └── notes.md
    ├── 02/                      # Linux fundamentals, shell examples, and Git notes
    │   ├── notes.md
    │   └── git.md
    ├── 03/
    │   └── Python/              # Python topic notes and exercises (many files)
    │       └── README.md
    ├── 04/
    │   └── Docker/              # Docker study notes and exercises
    │       └── README.md
    ├── 05/
        └── SQL/                 # SQL fundamentals, exercises, and Data Engineering practice
            └── README.md
    └── 06/
        └── NoSQL/               # NoSQL concepts, MongoDB lessons, and exercises
            └── README.md
```

## How to use these materials

1. Clone the repository:

```bash
git clone https://github.com/aminah7med/data-engineering-journey.git
```

2. Read the lecture notes in order to follow the author's learning sequence. Start with:
   - `lectures/01/notes.md` (conceptual foundations)
   - `lectures/02/notes.md` (practical Linux & HDFS examples) and `lectures/02/git.md` (source control practices)

3. Explore `lectures/03/Python/README.md` for the Python topic index and the individual topic files.

4. Follow any per-folder instructions (run scripts or exercises) that appear inside each lecture folder. Execution steps and dependencies are documented per lecture where required.

## Contribution and edits

- If you want to suggest changes, open a branch, make edits, and submit a pull request. Keep changes focused to the relevant lecture folder.
- This README was updated to improve navigation and factual accuracy; no lecture content was modified.

## Closing

This repository is a focused study record and reference for fundamental data engineering concepts and practice. For questions about specific lecture content, open the relevant file under `lectures/` and raise an issue or PR with suggested improvements.
