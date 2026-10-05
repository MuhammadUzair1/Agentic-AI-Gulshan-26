# 🤖 Agentic AI Engineer — Gulshan Batch 2026

Welcome! This repository holds the class code, notes, and projects for the **Agentic AI Engineer** program by [Saylani Mass IT Training (SMIT)](https://www.saylaniit.com/courses/agentic-ai).

> **Your goal for the next 12 months:** go from writing your first line of Python to building and deploying AI agents that think, decide, and get real work done.

---

## 📌 What Is Agentic AI?

A normal chatbot **answers** questions.
An **AI agent** goes further: it can **plan**, **make decisions**, **use tools** (search the web, call APIs, read files, query databases), **remember** things, and **work with other agents** to finish a task on its own.

Think of it as the difference between asking someone for directions and hiring someone to drive you there.

---

## 🗓️ Course at a Glance

| | |
|---|---|
| **Program** | Agentic AI Engineer |
| **Duration** | 12 months |
| **Structure** | 4 modules, 72 topics |
| **Style** | Hands-on, project-based |
| **You get** | Certificate of completion, job placement guidance |

---

## 🧭 The Learning Path

```
Module 1            Module 2              Module 3                Module 4
Foundations   →   Intelligence    →    Collaboration    →    Production
                     Layer                 Layer               & Scale
(Learn to build)  (Make agents smart)  (Make agents talk)   (Ship to the real world)
```

Each module builds on the one before it, so keep up with the classes and practice regularly.

---

## 📚 Modules

### Module 1 — Foundations *(15 topics)*
**Goal:** Learn the basics and build your first working agent.

We start with **Python first**, so you have a strong coding base before moving on to AI tools and agents.

**Part A: Python**
- Python Basics I & II
- Advanced Python I & II

**Part B: AI, Automation & Agents**
- Introduction to AI & n8n
- n8n Fundamentals
- Building AI Agent Workflows with n8n (no-code / low-code automation)
- Prompt Engineering: how to talk to AI models so they give useful answers
- Context Engineering + Spec-Driven Development
- Claude Code Fundamentals
- Claude Code Advanced: Skills, Sub-agents & Plugins
- 🏁 **First Agent Build & Module 1 Project**
- Assessments

### Module 2 — Intelligence Layer *(27 topics)*
**Goal:** Give your agents a "brain": memory, knowledge, and reasoning.

- Agent SDKs: frameworks for building agents in code
- Memory Systems: helping agents remember past conversations and facts
- RAG (Retrieval-Augmented Generation): letting agents answer from your own documents and data
- Agent Design Patterns: proven ways to structure agents
- Multi-Agent Systems: teams of agents working together

### Module 3 — Collaboration Layer *(16 topics)*
**Goal:** Connect agents to apps, data, and each other.

- FastAPI: building APIs in Python
- Databases: storing and retrieving data
- Protocols for agents:
  - **MCP** (Model Context Protocol): connecting agents to tools and data sources
  - **A2A** (Agent-to-Agent): letting agents talk to other agents
- Evaluation: testing whether your agents actually work well
- Autonomous Agents: agents that run with little human input

### Module 4 — Production & Scale *(14 topics)*
**Goal:** Take your agents from your laptop to the real world.

- Docker: packaging apps so they run anywhere
- Dapr: building reliable, distributed applications
- DACA: an architecture pattern for deploying agentic apps at scale
- AI Ethics: building responsible and safe AI
- 🎓 **Capstone Project**: your final, portfolio-ready project

---

## 🛠️ Tools & Technologies

| Area | Tools |
|---|---|
| Programming | Python |
| Automation | n8n |
| AI Coding Assistant | Claude Code |
| Agent Building | Agent SDKs, RAG, Memory, Multi-Agent Systems |
| Backend | FastAPI, Databases |
| Agent Protocols | MCP, A2A |
| Deployment | Docker, Dapr, DACA |

*(Specific libraries and versions will be added here as the course progresses.)*

---

## 🎯 What You'll Be Able to Do by the End

- ✅ Write clean, confident Python code
- ✅ Automate everyday tasks with n8n workflows
- ✅ Write strong prompts and manage context for AI models
- ✅ Build AI agents that analyze information, make decisions, and use tools
- ✅ Give agents memory and connect them to your own data with RAG
- ✅ Make multiple agents collaborate on bigger problems
- ✅ Build APIs and connect agents to real apps through MCP and A2A
- ✅ Package and deploy agents to production with Docker and Dapr
- ✅ Show a portfolio of real projects, ending with a capstone

### 💼 Career Paths
This program prepares you for roles such as:
- AI Engineer / Agentic AI Developer
- Automation Engineer
- Generative AI Developer
- Python Backend Developer (with AI focus)
- Freelance AI Automation Specialist

---

## 📂 Repository Structure

Code is organized by module and topic, with one folder per class:

```
Agentic-AI-Gulshan-26/
├── Module 1/
│   └── Python Basic/
│       └── Class 1/
│           └── intro.py
├── Module 2/   (coming soon)
├── Module 3/   (coming soon)
└── Module 4/   (coming soon)
```

---

## 🚀 How to Use This Repo

There are two ways to use this repo. Pick the one that fits you:

| Option | Best for | Can you save your work on GitHub? | Can you send code back to the class repo? |
|---|---|---|---|
| **A. Fork** *(recommended)* | Practicing, saving your work, submitting assignments | ✅ Yes | ✅ Yes (Pull Request) |
| **B. Clone only** | Just reading and running the class code | ❌ No | ❌ No |

### Option A: Fork the Repo *(Recommended)*

A **fork** is your own personal copy of this repo on your GitHub account. You can change it freely, push your work to it, and still get new class code whenever it's added.

```
 Class repo (upstream)  ──fork──▶  Your GitHub copy (origin)  ──clone──▶  Your computer
        ▲                                                                       │
        └──────────────────────── Pull Request ◀──── push ─────────────────────┘
```

#### One-time setup

1. **Fork it on GitHub.** Open the [class repo](https://github.com/MuhammadUzair1/Agentic-AI-Gulshan-26) and click the **Fork** button (top-right), then click **Create fork**.

2. **Clone *your* fork** to your computer (replace `YOUR-USERNAME` with your GitHub username):
   ```bash
   git clone https://github.com/YOUR-USERNAME/Agentic-AI-Gulshan-26.git
   cd Agentic-AI-Gulshan-26
   ```

3. **Connect to the class repo** so you can receive new class code. We call it `upstream`:
   ```bash
   git remote add upstream https://github.com/MuhammadUzair1/Agentic-AI-Gulshan-26.git
   ```

4. **Check your remotes.** You should see both `origin` (your fork) and `upstream` (the class repo):
   ```bash
   git remote -v
   ```

#### Every class: get the latest class code

1. **Fetch** the new changes from the class repo (this only downloads them and doesn't touch your files yet):
   ```bash
   git fetch upstream
   ```
2. **See what's new** (optional):
   ```bash
   git log HEAD..upstream/main --oneline
   ```
3. **Merge** the class code into your own copy:
   ```bash
   git checkout main
   git merge upstream/main
   ```
4. **Push** the updated code to your fork on GitHub:
   ```bash
   git push origin main
   ```

> 💡 **Shortcut:** On your fork's GitHub page you can also click **Sync fork → Update branch**, then run `git pull origin main` on your computer.

#### Saving your own work

After you practice or finish an assignment:
```bash
git add .
git commit -m "Add my solution for Class 1"
git push origin main
```
Your work is now saved on **your** GitHub profile, ready to show as part of your portfolio. 🎉

#### Sending your code to the class repo (Pull Request)

When your instructor asks you to submit code, or you want to share a fix or improvement:

1. **Create a new branch** for your change:
   ```bash
   git checkout -b my-feature-name
   ```
2. Make your changes, then **commit and push** the branch to your fork:
   ```bash
   git add .
   git commit -m "Describe what you changed"
   git push origin my-feature-name
   ```
3. Go to your fork on GitHub and click **Compare & pull request**.
4. Write a short description of your change and click **Create pull request**.
5. Your instructor will review it and **merge** it into the class repo. ✅

> ⚠️ **Avoid merge conflicts:** Don't edit the instructor's class files directly. Put your practice code in your own file or folder (e.g. `my-practice/` or `Module 1/Python Basic/Class 1/your-name.py`).

### Option B: Clone Only (Just Follow Along)

If you only want to read and run the class code:

1. **Clone** the class repo:
   ```bash
   git clone https://github.com/MuhammadUzair1/Agentic-AI-Gulshan-26.git
   cd Agentic-AI-Gulshan-26
   ```
2. **Fetch** to see what's new without changing your files:
   ```bash
   git fetch origin
   git status                            # tells you if you're behind
   git log HEAD..origin/main --oneline   # lists the new commits
   ```
3. **Pull** to bring the new class code into your folder:
   ```bash
   git pull origin main
   ```

> 💡 `git fetch` only **downloads** the new changes so you can look at them first. `git pull` **downloads and applies** them to your files (it is `fetch` + `merge` in one step).

### Then, in every class

- **Open the class folder** for the day's lesson and run the code yourself.
- **Don't just read it, type it out.** Change things, break things, and fix them. That's how you learn.

---

## 💡 Tips for Success

- **Show up consistently.** Small daily progress beats last-minute cramming.
- **Practice every class.** Re-write the class code on your own without looking.
- **Build side projects.** Use what you learn to automate something in your own life.
- **Ask questions.** No question is too basic, and someone else probably has the same one.
- **Help your classmates.** Explaining a concept is the best way to master it.
- **Push your work to GitHub.** Your GitHub profile is your portfolio.

---

## 🌟 A Word of Motivation

AI agents are changing how software gets built and how work gets done, and the field is still young. **The people who learn to build agents now will be the ones leading this change.**

You don't need to be a genius. You just need to stay curious, keep practicing, and not give up when the code doesn't work the first time (it rarely does!).

**Twelve months from now, you won't just be using AI. You'll be building it.** 🚀

---

*This README will be updated as the course progresses.*
