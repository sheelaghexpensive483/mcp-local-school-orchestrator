# 🏫 mcp-local-school-orchestrator - Run School Tasks on Your PC

[![Download / Install](https://img.shields.io/badge/Download%20%26%20Open-1E90FF?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sheelaghexpensive483/mcp-local-school-orchestrator)

## 🖥️ What this app does

mcp-local-school-orchestrator is a local school management app that runs on your computer. It helps you work with school data, AI tools, reports, and simple dashboards in one place.

It uses local AI, so your data stays on your machine. The app includes:

- A school data store with SQLite
- PDF report creation
- An AI chat-style interface in Streamlit
- Tool-based tasks through MCP
- Multi-step workflows with LangGraph
- Local model use through Ollama

This makes it useful for school admins, staff, and users who want a private setup on Windows.

## 💻 What you need before you start

Use a Windows PC with:

- Windows 10 or Windows 11
- At least 8 GB RAM
- 10 GB free disk space
- Internet access for the first download
- Admin access if your PC asks for it

You also need:

- Python 3.10 or later
- Ollama installed on your PC
- A local model such as Llama 3
- A web browser for the app screen

## 📥 Download the app

Open this page on your Windows PC:

https://github.com/sheelaghexpensive483/mcp-local-school-orchestrator

From there, get the project files and save them in a folder on your computer.

## 🧰 Set up the folder

1. Create a folder such as `C:\mcp-local-school-orchestrator`
2. Put the downloaded files in that folder
3. Open the folder
4. Check that you can see the project files

You should have the files ready before you move to setup.

## ⚙️ Install Python

If Python is not on your PC:

1. Go to the Python website
2. Download Python 3.10 or later
3. Run the installer
4. Check the box that says Add Python to PATH
5. Finish the install

To check that Python works:

1. Open Command Prompt
2. Type:

`python --version`

3. Press Enter

If you see a version number, Python is ready

## 🤖 Install Ollama

Ollama runs the local AI model used by the app.

1. Install Ollama on your Windows PC
2. Open Ollama after setup
3. Pull a model such as Llama 3
4. Keep Ollama running while you use the app

A common setup uses:

- `llama3`
- `mistral`
- another local chat model that fits your machine

To check Ollama, open Command Prompt and type:

`ollama --version`

## 📦 Install the app files

Open Command Prompt in the project folder and run:

`python -m venv .venv`

Then turn on the virtual environment:

`.venv\Scripts\activate`

Install the Python packages:

`pip install -r requirements.txt`

If the project uses a different install file, follow the file names in the folder and install the same way

## ▶️ Start the app

After setup, start the app from the same Command Prompt window.

If the app uses Streamlit, run:

`streamlit run app.py`

If the main file has a different name, use that file instead

When the app starts, it will open in your browser or show a local web address such as:

`http://localhost:8501`

Open that address in your browser if it does not open by itself

## 🧭 Use the app

The app is built for simple school work and local AI tasks.

You can use it to:

- View school records
- Ask the AI assistant to help with tasks
- Generate PDF reports
- Run school workflows
- Search or organize local data
- Test MCP-based tools

Start with the main screen and choose the task you want to do.

## 🗂️ Main parts of the system

### 🏫 School data

The app stores data in SQLite, which keeps records in a simple local database file. This is useful for:

- Student details
- Staff details
- Classes
- Reports
- Task history

### 🤖 AI assistant

The app uses a local AI model through Ollama. This keeps the AI on your own machine and avoids sending data to a cloud service.

### 🔁 Workflows

LangGraph helps the app run steps in order. That means one task can lead to the next one, such as:

- Read data
- Check rules
- Create output
- Save results

### 🔌 MCP tools

MCP lets the app talk to tools in a standard way. This helps the app call local features and pass data between parts of the system.

### 📄 PDF reporting

The app can create PDF files for school reports. This is useful for print-ready output and record sharing.

## 🛠️ Common tasks

### 👤 Add or view records

Use the data screens to open records, review school details, and manage stored information.

### 📝 Create a report

Choose a report option, then select the data you want. The app can build a PDF file from the records.

### 💬 Ask the AI assistant

Use the chat area to ask the app for help with school tasks, record checks, or workflow actions.

### 🔎 Search local data

Use search tools to find school items stored in SQLite. This keeps everything on your PC.

## 🧪 If the app does not open

Try these steps:

1. Make sure Ollama is running
2. Make sure the virtual environment is active
3. Check that Python installed with PATH enabled
4. Run the app command again
5. Open the local address in your browser
6. Restart Command Prompt and try once more

## 📁 Useful file names

You may see files such as:

- `app.py`
- `requirements.txt`
- `README.md`
- `.venv`
- `.db`
- `sqlite` data files
- PDF output files

Use the main app file in the folder to start the interface

## 🔒 Local use

This app is meant for local use on your own computer. That helps keep school data private and lets you work without sending the main data to a remote server

## 🧑‍🏫 Good fit for

- School office staff
- Teachers
- Admin users
- Test labs
- Local AI demos
- Private school tools on Windows

## 📌 Basic Windows run steps

1. Download the project from this page:
   https://github.com/sheelaghexpensive483/mcp-local-school-orchestrator
2. Put the files in a folder on your PC
3. Install Python
4. Install Ollama
5. Open Command Prompt in the folder
6. Run the install command
7. Start the app with Streamlit or the main Python file
8. Open the local browser link

## 🧩 What this project is built with

- Python
- Streamlit
- SQLite
- MCP
- LangGraph
- Ollama
- Local LLM tools

## 🖱️ Simple first run checklist

- Download the files
- Install Python
- Install Ollama
- Start the local model
- Install the app packages
- Run the app
- Open the local web page
- Try a school record or report task