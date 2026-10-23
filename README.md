# Diário CNV

App (PWA) para registrar tiques e acontecimentos seguindo a Comunicação Não-Violenta:
sentimento → necessidade → observação e pedido. Listas de sentimentos e necessidades
do Instituto CNV Brasil. Os registros ficam só no aparelho (localStorage).

## Estrutura
- `src/app.html` — fonte do app (é editado aqui)
- `build.py` — gera `index.html` a partir de `src/app.html`
- `sw.js` — service worker (offline). Troque `VERSION` a cada publicação.
- `manifest.webmanifest`, `icons/` — instalação no Android
- `vendor/jspdf.umd.min.js` — gera o PDF sem internet

## Publicar no GitHub Pages
1. Rode `python3 build.py`.
2. Envie para um repositório no GitHub.
3. Em Settings → Pages: Source "Deploy from a branch", branch `main`, pasta `/ (root)`.
4. Abra `https://<usuario>.github.io/<repositorio>/` no Chrome do Android → menu → "Instalar app".
