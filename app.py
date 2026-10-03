from flask import Flask, render_template, request
from detector import detect_prompt_injection
from agent import safe_ai_agent
from datetime import datetime
from pypdf import PdfReader

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    user_input = request.form.get("user_input", "").strip()

    # PDF upload
    uploaded_file = request.files.get("document")

    if uploaded_file and uploaded_file.filename:
        if uploaded_file.filename.lower().endswith(".pdf"):
            try:
                reader = PdfReader(uploaded_file)

                pdf_text = ""

                for page in reader.pages:
                    text = page.extract_text()

                    if text:
                        pdf_text += text + "\n"

                if pdf_text.strip():
                    user_input = pdf_text.strip()
                else:
                    user_input = "PDF contains no readable text."

            except Exception:
                user_input = "Unable to read the uploaded PDF."

    # Firewall detection
    result = detect_prompt_injection(user_input)

    # Security log data
    log_entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": user_input,
        "attacks": result["attacks"],
        "risk": result["risk"],
        "safe": result["safe"]
    }

    # Terminal log
    print("\n========== SECURITY LOG ==========")
    print("Time:", log_entry["time"])
    print("Input:", log_entry["input"][:500])
    print("Attack Types:", log_entry["attacks"])
    print("Risk:", log_entry["risk"])
    print("Safe:", log_entry["safe"])
    print("==================================\n")

    # Save security log
    with open("security_logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(
            f"{log_entry['time']} | "
            f"Input: {log_entry['input'][:500]} | "
            f"Attacks: {log_entry['attacks']} | "
            f"Risk: {log_entry['risk']} | "
            f"Safe: {log_entry['safe']}\n"
        )

    # Only safe content reaches the AI agent
    if result["safe"]:
        agent_response = safe_ai_agent(user_input)
    else:
        agent_response = "Request blocked by Prompt Injection Firewall."

    return render_template(
        "result.html",
        safe=result["safe"],
        attacks=", ".join(result["attacks"]),
        risk=result["risk"],
        agent_response=agent_response
    )


@app.route("/logs")
def logs():
    try:
        with open("security_logs.txt", "r", encoding="utf-8") as log_file:
            log_data = log_file.readlines()
    except FileNotFoundError:
        log_data = []

    return render_template("logs.html", logs=log_data)


if __name__ == "__main__":
    app.run(debug=True)