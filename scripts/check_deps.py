#!/usr/bin/env python3
"""检查小黎的依赖服务是否正常"""
import urllib.request, sys

SERVICES = [
    ("OpenSpace Cloud", "https://open-space.cloud/api/v1/ping", "x-api-key"),
    ("GitHub API", "https://api.github.com", None),
]

def check(name, url, auth_header=None):
    try:
        h = {"User-Agent": "xiaoli-agent/1.0"}
        if auth_header:
            import os
            h[auth_header] = os.environ.get("OPENSPACE_API_KEY", "")
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=8) as r:
            print(f"✅ {name}: OK")
            return True
    except Exception as e:
        print(f"❌ {name}: {str(e)[:60]}")
        return False

ok = all(check(n, u, a) for n, u, a in SERVICES)
sys.exit(0 if ok else 1)
