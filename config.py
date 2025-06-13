import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not ASSEMBLYAI_API_KEY or not GEMINI_API_KEY:
    raise ValueError("API keys for AssemblyAI and Gemini must be set in the .env file.")