"""Gera os ícones PNG. Rode: python3 icons/make_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw
out = Path(__file__).parent
TEAL, LIGHT, WARM = (31, 122, 114), (241, 245, 244), (232, 167, 102)
def icon(size, maskable=False):
    s = size * 4
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if maskable: d.rectangle([0, 0, s, s], fill=TEAL)
    else: d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * .22), fill=TEAL)
    k = .62 if maskable else .78            # área segura do ícone maskable
    c, r = s / 2, s * k / 2
    # balão de fala (comunicação) com um ponto de sentimento dentro
    d.ellipse([c - r * .85, c - r * .78, c + r * .85, c + r * .62], fill=LIGHT)
    d.polygon([(c - r * .45, c + r * .40), (c - r * .62, c + r * .92), (c - r * .05, c + r * .55)], fill=LIGHT)
    d.ellipse([c - r * .22, c - r * .30, c + r * .22, c + r * .14], fill=WARM)
    return im.resize((size, size), Image.LANCZOS)
for n in (180, 192, 512): icon(n).save(out / f"icon-{n}.png")
icon(512, True).save(out / "icon-maskable-512.png")
print("ícones gerados")
