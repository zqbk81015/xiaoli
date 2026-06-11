#!/usr/bin/env python3
"""小黎健康检查脚本 - 检查各服务连通性"""
import urllib.request, json, subprocess, sys

def check(url, name):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            return f"✅ {name}: OK ({r.status})"
    except Exception as e:
        return f"❌ {name}: {str(e)[:40]}"

checks = [
    ("https://open-space.cloud/api/v1/ping", "OpenSpace Cloud"),
    ("https://api.github.com", "GitHub API"),
    ("https://openai.com", "OpenAI"),
]
for url, name in checks:
    print(check(url, name))
