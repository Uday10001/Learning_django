import os

port = os.getenv("PORT", "8000")
bind = f"0.0.0.0:{port}"
workers = 3
worker_class = "sync"
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
