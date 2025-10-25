import os
import subprocess

# Run the Streamlit app on the correct port
port = os.environ.get("PORT", "8501")
subprocess.run([
    "streamlit", "run", "pdf_analyzer.py",
    "--server.port", port,
    "--server.address", "0.0.0.0"
])
