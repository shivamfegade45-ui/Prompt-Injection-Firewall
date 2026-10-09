# 🛡️ Prompt Injection Firewall

A defensive security prototype designed to detect potential prompt injection attempts before input reaches an AI agent.

## 📌 Project Overview

AI systems can receive untrusted instructions through user messages and uploaded documents. This project provides a basic security layer that scans text, identifies known suspicious patterns, assigns a risk level, and blocks inputs that match its detection rules.

## ✨ Features

* **Prompt Injection Detection:** Detects seven categories of suspicious instruction patterns using rule-based matching.
* **Risk Assessment:** Assigns Low, Medium, or High risk based on the number of detected categories.
* **PDF Text Extraction:** Extracts readable text from uploaded PDF documents.
* **Request Blocking:** Prevents flagged input from reaching the simulated AI agent.
* **Security Logging:** Records scan results for review.
* **Security Dashboard:** Displays previously recorded security events.
* **Web Interface:** Provides a simple interface built with Flask, HTML, and CSS.

## 🔍 Detection Categories

1. Instruction Override
2. Role Change
3. Secret Extraction
4. Tool Abuse
5. Context Poisoning
6. Encoded Instructions
7. Indirect Prompt Injection

**Important:** Detection is based on predefined text patterns. It is a prototype and may miss attacks or flag harmless text. It is not a production-grade security solution.

## 🏗️ Architecture

```text
User Input / PDF
       |
       v
Flask Web Application
       |
       v
PDF Text Extraction (if applicable)
       |
       v
Rule-Based Detection Engine
       |
       v
Risk Assessment
       |
       +------ No known pattern detected ------+
       |                                       |
       v                                       v
Simulated AI Agent                       Block Request
       |                                       |
       +-------------------+-------------------+
                           |
                           v
                    Security Logging
                           |
                           v
                   Security Dashboard
```

## 🧰 Technology Stack

* Python
* Flask
* pypdf
* HTML
* CSS
* Git and GitHub

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shivamfegade45-ui/Prompt-Injection-Firewall.git
cd Prompt-Injection-Firewall
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install Flask pypdf
```

### 4. Start the application

```bash
python app.py
```

Open this address in your browser:

`http://127.0.0.1:5000/`

## 🧪 Testing

Test the application with:

* Ordinary, harmless text to check the safe-input path.
* Harmless test phrases that match the detector's predefined rules.
* A text-based PDF containing ordinary text.
* A test PDF containing a known detection phrase.

Review the results and the Security Dashboard to verify that scans are recorded.

## 🔐 Security and Limitations

* This project uses basic rule-based detection, not a trained security model.
* Encoded, obfuscated, multilingual, or previously unseen attacks may not be detected.
* PDF text extraction may not work for scanned documents that require OCR.
* The AI agent is simulated; this prototype does not connect to a live external AI model.
* Security logs may contain submitted text. Do not use real passwords, API keys, personal data, or confidential documents during testing.
* Do not expose the development server publicly without appropriate security hardening.

## 🚀 Future Improvements

* Add stronger text normalization and context-aware detection.
* Add automated tests and detection-performance metrics.
* Support additional document formats and OCR.
* Add safer handling of uploaded files and sensitive log data.
* Integrate a real AI model behind a properly secured gateway.
* Evaluate false positives, false negatives, and robustness against unseen inputs.

## 👨‍💻 Author

**Shivam Fegade**

GitHub: https://github.com/shivamfegade45-ui

---

*Built as a defensive prototype for an agentic cybersecurity hackathon project.*
