import os
import subprocess

# Ensure the environment variable is set for Streamlit
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

if __name__ == "__main__":
    command = ["streamlit", "run", "application.py"]
    subprocess.run(command)
