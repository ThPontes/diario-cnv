"""Monta index.html (PWA) a partir de src/app.html. Rode: python3 build.py"""
from pathlib import Path
root = Path(__file__).parent
src = (root / "src" / "app.html").read_text(encoding="utf-8")
head, body = src.split("<!-- BODY -->", 1)
# no app instalado o jsPDF vem junto, para funcionar offline
head = head.replace("https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js", "vendor/jspdf.umd.min.js")
page = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1f7a72">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}[hidden]{{display:none!important}}</style>
{head.strip()}
</head>
<body>
{body.strip()}
<script>if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js");</script>
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html gerado")
