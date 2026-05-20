#!/usr/bin/env python3
"""Build the Open Graph share image 1200×630 for social media."""

from pathlib import Path
from weasyprint import HTML, CSS
import shutil

HERE = Path(__file__).resolve().parent
LOGO = HERE / "assets" / "logo.jpg"
OUT_PDF = HERE / "assets" / "og-image.pdf"
OUT_PNG = HERE / "assets" / "og-image.png"

HTML_TEMPLATE = f"""
<!doctype html>
<html><head><meta charset="utf-8"></head><body>
<div class="card">
  <div class="head">
    <img src="file://{LOGO}" class="logo">
    <span class="brand">УЧЕБНЫЙ ЦЕНТР 101%</span>
  </div>
  <h1>Готовим в&nbsp;<span class="accent">Westminster</span>,<br>на&nbsp;нацсертификат и&nbsp;IELTS</h1>
  <div class="stats">
    <div><strong>7</strong><span>в Westminster в&nbsp;2025</span></div>
    <div><strong>400+</strong><span>выпускников</span></div>
    <div><strong>с&nbsp;2019</strong><span>работает центр</span></div>
    <div><strong>4.9★</strong><span>Яндекс.Карты</span></div>
  </div>
  <p class="bottom">Нодир Нуриддинов · Ташкент, Джангох · 101percent.uz</p>
</div>
</body></html>
"""

CSS_STYLES = """
@page { size: 1200px 630px; margin: 0; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  background: linear-gradient(135deg, #FFC93C 0%, #F39C12 100%);
  width: 1200px;
  height: 630px;
  overflow: hidden;
  position: relative;
}
body::before {
  content: "";
  position: absolute;
  top: -100px;
  right: -100px;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(22,22,22,0.06), transparent 70%);
}
.card {
  padding: 60px 80px;
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.head { display: flex; align-items: center; gap: 18px; }
.logo { width: 72px; height: 72px; border-radius: 16px; }
.brand {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #161616;
}
h1 {
  font-size: 76px;
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.03em;
  color: #161616;
  margin: 20px 0 0;
}
.accent {
  background: #161616;
  color: #FFC93C;
  padding: 2px 16px;
  border-radius: 12px;
  display: inline-block;
}
.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin: 0 0 16px;
  padding: 26px 0;
  border-top: 2px solid rgba(22,22,22,0.18);
}
.stats strong {
  display: block;
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #161616;
  line-height: 1;
  margin-bottom: 6px;
}
.stats span {
  font-size: 14px;
  color: rgba(22,22,22,0.65);
}
.bottom {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: rgba(22,22,22,0.72);
}
"""

def main():
    HTML(string=HTML_TEMPLATE).write_pdf(target=str(OUT_PDF), stylesheets=[CSS(string=CSS_STYLES)])
    # Convert PDF page to PNG via macOS native sips (Quartz) for speed
    import subprocess
    subprocess.run(
        ["sips", "-s", "format", "png", "-Z", "1200", str(OUT_PDF), "--out", str(OUT_PNG)],
        check=False, capture_output=True
    )
    if OUT_PDF.exists() and OUT_PNG.exists():
        print(f"OK: {OUT_PNG} ({OUT_PNG.stat().st_size//1024} KB)")
    OUT_PDF.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
