# ⚡ Ansari Neural Forge

🚀 A Multi-Agent AI System for Task, Schedule & Notes Management

---

## 🧠 Overview

ForgeFlow AI is an intelligent multi-agent system that helps users manage tasks, schedules, and notes through a conversational interface.

It demonstrates how multiple AI agents can collaborate using shared data and tools to execute real-world workflows.

---

## 🏗️ Architecture

- 🧠 Orchestrator Agent (Main Controller)
- 📝 Task Agent
- 📅 Calendar Agent (with conflict detection)
- 🗒️ Notes Agent
- 🗄️ SQLite Database
- 🌐 FastAPI Backend
- 💬 Chat UI (HTML/CSS/JS)

---

## ⚡ Features

- ✅ Multi-agent coordination
- 🔄 Full CRUD operations
- ⚠️ Conflict detection for scheduling
- 💬 Chat-based interaction
- ⚡ Smart input parsing
- ☁️ Deployed on Google Cloud Run

---

## 🎯 Example Commands

- create task submit hackathon
- schedule meeting tomorrow at 5pm
- show tasks
- update task 1 finish work
- delete task 1

---

## 🌐 Live Demo

👉 https://forgeflow-558706742858.asia-south1.run.app/

---

## 🎥 Demo Video


---

## 🚀 Tech Stack

- Python (FastAPI)
- SQLite
- HTML, CSS, JavaScript
- Docker
- Google Cloud Run

---

## 💡 Key Innovation

Unlike traditional apps, Ansari Neural Forge uses a **multi-agent architecture** where specialized agents collaborate over shared data to execute workflows efficiently.

---

## 📦 Setup Instructions

```bash
pip install -r requirements.txt
uvicorn main:app --reload
