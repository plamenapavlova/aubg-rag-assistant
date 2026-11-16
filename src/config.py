from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = PROJECT_ROOT/"data"/"sources.json"
RAW_DIR = PROJECT_ROOT/"data"/"raw"
INDEX_DIR = PROJECT_ROOT/"data"/"index"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing")

#LLM settings
LLM_MODEL = "gpt-6-luna"
LLM_MAX_OUTPUT_TOKENS = 1000
LLM_MAX_WAITING_TIME = 30

#Retrieval settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 5 #how many chunks to be sent to the LLM
MIN_SIMILARITY = 0.3 #TO BE REFINED

#Chunking
MAX_CHUNK_WORDS = 180
MIN_CHUNK_WORDS = 30
CHUNK_OVERLAP_WORDS = 30
MAX_HEADING_WORDS = 15
