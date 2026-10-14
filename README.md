# Data Engineering Journey

A concise, evidence-based record of study and practical notes for foundational Data Engineering topics. This repository collects lecture notes, command references, and practical guidance used during learning and practice. It is intended as a navigable study log — not a production codebase.

## Overview

- Purpose: Document learning materials (lecture notes, commands, and exercises) that build practical understanding of data engineering concepts and tooling.
- Audience: Other learners, reviewers, and recruiters who want to see a structured study record and reference materials.

## Learning roadmap & direct navigation

Open the folders below to read the verified lecture notes and reference material.

- lectures/01/notes.md — Lecture 01: core data engineering concepts (data lake vs warehouse, OLTP vs OLAP, schemas, scaling, clusters).
- lectures/02/notes.md — Lecture 02: Linux & shell fundamentals for data engineering (permissions, users, processes, shell scripting, HDFS examples).
- lectures/02/git.md — Git & GitHub: repository workflows, branching, commits, merge/fix workflows and best practices.
- lectures/03/Python/README.md — Python learning path and links to detailed topic notes and exercises (see the Python folder for individual files).
  - lectures/03/Python/01-python-basics.md
  - lectures/03/Python/11-python-for-data-engineering.md
- lectures/04/Docker/README.md — Docker notes and exercise references for local development and container workflows.

(Each link above is a relative path inside this repository and was verified to exist at the time of this edit.)

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
    └── 04/
        └── Docker/              # Docker study notes and exercises
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
