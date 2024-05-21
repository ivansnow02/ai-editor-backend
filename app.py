import os
from generate import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
