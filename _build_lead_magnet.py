#!/usr/bin/env python3
"""
Generate the lead-magnet PDF for 101% learning centre (v2).

V2 has 10 REAL formulas from school maths that always appear on UZ
national certificate (нацсертификат) and most entrance exams: quadratic,
Vieta, progressions, log/exp, trig, derivatives, basic combinatorics,
geometry. Nodir can expand to 50 by adding his actual exam patterns.

Run:  python3 _build_lead_magnet.py
"""

from pathlib import Path
from weasyprint import HTML, CSS

HERE = Path(__file__).resolve().parent
LOGO = HERE / "assets" / "logo.jpg"
OUT  = HERE / "assets" / "lead-magnet.pdf"

FORMULAS = [
    {
        "n": "01",
        "title": "Квадратное уравнение",
        "expr": "x = (−b ± √(b² − 4ac)) / 2a",
        "body": "Для уравнения <em>ax² + bx + c = 0</em> корни находятся через дискриминант.",
        "example": "<strong>Пример.</strong> 2x² − 5x + 2 = 0 → D = 25 − 16 = 9 → √D = 3 → x₁ = 2, x₂ = 0.5",
    },
    {
        "n": "02",
        "title": "Теорема Виета",
        "expr": "x₁ + x₂ = −b/a · · · x₁ · x₂ = c/a",
        "body": "Сумма и произведение корней приведённого квадратного уравнения <em>x² + px + q = 0</em>.",
        "example": "<strong>Пример.</strong> x² − 5x + 6 = 0 → x₁ + x₂ = 5, x₁ · x₂ = 6 → корни 2 и 3.",
    },
    {
        "n": "03",
        "title": "Арифметическая прогрессия",
        "expr": "aₙ = a₁ + d(n−1) · · · Sₙ = n(a₁ + aₙ) / 2",
        "body": "Каждый член отличается от предыдущего на одно и то же число <em>d</em> (разность).",
        "example": "<strong>Пример.</strong> a₁ = 3, d = 2 → a₁₀ = 3 + 2·9 = 21 → S₁₀ = 10·(3+21)/2 = 120",
    },
    {
        "n": "04",
        "title": "Геометрическая прогрессия",
        "expr": "bₙ = b₁ · q^(n−1) · · · Sₙ = b₁(q^n − 1) / (q − 1)",
        "body": "Каждый член — предыдущий умноженный на знаменатель <em>q</em>.",
        "example": "<strong>Пример.</strong> b₁ = 2, q = 3 → b₅ = 2·81 = 162 → S₅ = 2·(243−1)/(3−1) = 242",
    },
    {
        "n": "05",
        "title": "Свойства логарифмов",
        "expr": "log(ab) = log a + log b · · · log(a/b) = log a − log b · · · log(aⁿ) = n · log a",
        "body": "Три ключевых тождества. Из них выводится почти всё в задачах на логарифмы.",
        "example": "<strong>Пример.</strong> log₂ 32 = log₂(2⁵) = 5 · log₂ 2 = 5",
    },
    {
        "n": "06",
        "title": "Основное тригонометрическое тождество",
        "expr": "sin²α + cos²α = 1",
        "body": "Из него выводятся ВСЕ остальные тождества. Запомнить раз и навсегда.",
        "example": "<strong>Пример.</strong> Если sin α = 3/5, то cos²α = 1 − 9/25 = 16/25 → cos α = ±4/5",
    },
    {
        "n": "07",
        "title": "Формулы сокращённого умножения",
        "expr": "(a±b)² = a² ± 2ab + b² · · · a² − b² = (a−b)(a+b) · · · (a±b)³ = a³ ± 3a²b + 3ab² ± b³",
        "body": "База разложения многочленов на множители. Используется в каждом 3-м задании нацсертификата.",
        "example": "<strong>Пример.</strong> x² − 9 = (x − 3)(x + 3); 4x² + 12x + 9 = (2x + 3)²",
    },
    {
        "n": "08",
        "title": "Производная — базовые формулы",
        "expr": "(xⁿ)' = n·xⁿ⁻¹ · · · (sin x)' = cos x · · · (cos x)' = −sin x · · · (eˣ)' = eˣ",
        "body": "Минимум для большинства задач на производные. Производная суммы = сумма производных.",
        "example": "<strong>Пример.</strong> f(x) = 3x⁴ + sin x → f'(x) = 12x³ + cos x",
    },
    {
        "n": "09",
        "title": "Комбинаторика — основные формулы",
        "expr": "Pₙ = n! · · · Aₙᵏ = n! / (n−k)! · · · Cₙᵏ = n! / (k! · (n−k)!)",
        "body": "Перестановки (P), размещения (A), сочетания (C). Это «три кита» комбинаторики.",
        "example": "<strong>Пример.</strong> Сколькими способами выбрать 3 из 5 человек? C₅³ = 5! / (3!·2!) = 10",
    },
    {
        "n": "10",
        "title": "Теорема Пифагора и площади",
        "expr": "a² + b² = c² · · · S△ = ½·a·h · · · S○ = π·r²",
        "body": "Прямоугольный треугольник + базовые формулы площадей — фундамент геометрии в тесте.",
        "example": "<strong>Пример.</strong> Катеты 3 и 4 → гипотенуза √(9+16) = 5. Радиус 2 → площадь круга 4π.",
    },
]


def render_formulas_html() -> str:
    out = []
    for f in FORMULAS:
        out.append(f'''
<div class="formula-card">
  <div class="formula-head">
    <span class="formula-num">№ {f["n"]}</span>
    <h3>{f["title"]}</h3>
  </div>
  <p class="formula-body">{f["body"]}</p>
  <p class="formula-expr">{f["expr"]}</p>
  <p class="formula-example">{f["example"]}</p>
</div>
''')
    return "\n".join(out)


HTML_TEMPLATE = f"""
<!doctype html>
<html lang="ru">
<head><meta charset="utf-8"><title>50 формул для нацсертификата — 101%</title></head>
<body>

<section class="cover">
  <div class="cover-inner">
    <img class="logo" src="file://{LOGO}" alt="101%">
    <p class="brand">УЧЕБНЫЙ ЦЕНТР 101%</p>
    <h1>50 формул<br>для нацсертификата</h1>
    <p class="subtitle">Шпаргалка от Нодира Нуриддинова<br>Учебный центр 101% · Ташкент · Джангох</p>
    <p class="meta">Версия 2.0 · 2026 · 101percent.uz</p>
  </div>
</section>

<section class="intro">
  <h2>Как пользоваться</h2>
  <p>В этом PDF — <strong>10 базовых формул</strong> (первая часть из 50). Это фундамент:
  если ребёнок не помнит их наизусть, то 30%+ задач нацсертификата он не сможет решить даже теоретически.</p>
  <p>Каждая карточка содержит <strong>формулу, объяснение и&nbsp;конкретный пример</strong>.
  Распечатайте или сохраните на телефон, разбирайте по одной в день.</p>

  <div class="callout">
    <h3>А где остальные 40 формул?</h3>
    <p>Полная версия с 50 формулами и 10 разобранными задачами уровня нацсертификата —
    отправляется в Telegram после регистрации на 101percent.uz. Там же —
    закрытый канал «Реальные тесты прошлых лет», доступ только для&nbsp;скачавших.</p>
  </div>
</section>

<section class="formulas">
  <h2>10 ключевых формул</h2>
  {render_formulas_html()}
</section>

<section class="cta">
  <h2>Что дальше</h2>
  <p>Запишитесь на <strong>бесплатный пробный урок</strong> с диагностикой уровня — Нодир
  лично разберёт пробелы и составит план подготовки.</p>
  <p class="phone-link">📞 +998 90 023-45-60</p>
  <p class="tg-link">✈️ @LC101percent</p>
  <p class="small">Учебный центр 101% · Ташкент, Шайхантахурский район, м-в Джангох д.26</p>
</section>

<footer class="page-footer">
  <p>101PERCENT ООО · 101percent.uz · 101_percent@mail.ru · +998 90 023-45-60</p>
</footer>

</body>
</html>
"""

CSS_STYLES = """
@page {
  size: A4;
  margin: 18mm 16mm;
}

* { box-sizing: border-box; }

html, body {
  font-family: "Helvetica", "Arial", sans-serif;
  font-size: 11pt;
  line-height: 1.55;
  color: #161616;
  margin: 0;
  padding: 0;
}

.cover {
  background: linear-gradient(160deg, #FFC93C 0%, #F39C12 100%);
  color: #161616;
  page-break-after: always;
  min-height: 240mm;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: -18mm -16mm;
  padding: 20mm;
}
.cover-inner { max-width: 140mm; }
.logo { width: 80px; height: 80px; border-radius: 16px; margin: 0 auto 16px; }
.brand { font-size: 12pt; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; margin: 0 0 30mm; }
.cover h1 { font-size: 38pt; font-weight: 800; line-height: 1.05; letter-spacing: -0.02em; margin: 0 0 20mm; }
.subtitle { font-size: 13pt; font-weight: 500; margin-bottom: 30mm; }
.meta { font-size: 9pt; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(22,22,22,0.6); margin: 0; }

h2 {
  font-size: 22pt;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #161616;
  margin: 0 0 6mm;
  padding-bottom: 3mm;
  border-bottom: 3px solid #FFC93C;
}
h3 { font-size: 13pt; font-weight: 700; color: #161616; margin: 0; }
p { margin: 0 0 3mm; }

.intro, .formulas, .cta { padding: 6mm 0; }

.callout {
  background: #FFF6DC;
  border-left: 4px solid #F39C12;
  padding: 5mm 6mm;
  margin: 6mm 0;
  border-radius: 4px;
  page-break-inside: avoid;
}
.callout h3 { font-size: 12pt; margin-bottom: 2mm; color: #C76A0A; }

.formula-card {
  background: #FAF8F3;
  border-left: 3px solid #161616;
  border-radius: 0 8px 8px 0;
  padding: 6mm 7mm;
  margin: 4mm 0;
  page-break-inside: avoid;
}
.formula-head {
  display: flex;
  align-items: baseline;
  gap: 4mm;
  margin-bottom: 3mm;
}
.formula-num {
  background: #161616;
  color: #FFC93C;
  font-weight: 800;
  padding: 1mm 3mm;
  border-radius: 4px;
  font-size: 9pt;
  letter-spacing: 0.1em;
  flex-shrink: 0;
}
.formula-body { font-size: 10.5pt; color: #2A2A2A; }
.formula-expr {
  font-family: "Courier New", monospace;
  font-size: 12.5pt;
  background: #FFFFFF;
  padding: 4mm 5mm;
  border: 1px dashed #F39C12;
  border-radius: 4px;
  margin: 3mm 0;
  word-spacing: 0.5em;
}
.formula-example {
  background: #FFF6DC;
  padding: 3mm 4mm;
  border-radius: 4px;
  font-size: 10pt;
}

.cta {
  background: #161616;
  color: #FFFFFF;
  padding: 10mm;
  border-radius: 12px;
  margin: 8mm 0;
  page-break-inside: avoid;
}
.cta h2 { color: #FFC93C; border-bottom-color: #FFC93C; }
.cta p { color: rgba(255,255,255,0.85); }
.phone-link, .tg-link {
  font-family: "Courier New", monospace;
  font-size: 14pt;
  font-weight: 700;
  background: rgba(255, 201, 60, 0.15);
  color: #FFC93C !important;
  padding: 4mm;
  border-radius: 6px;
  text-align: center;
  margin: 3mm 0;
}
.small { font-size: 9pt; color: rgba(255,255,255,0.6) !important; text-align: center; }

.page-footer {
  margin-top: 8mm;
  padding-top: 4mm;
  border-top: 1px solid #DDD;
  font-size: 8.5pt;
  color: #6B6B6B;
  text-align: center;
}
em { font-style: italic; }
strong { font-weight: 700; }
"""

def main():
    print(f"Rendering PDF → {OUT}")
    HTML(string=HTML_TEMPLATE).write_pdf(
        target=str(OUT),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    size_kb = OUT.stat().st_size / 1024
    print(f"OK · {size_kb:.1f} KB · {len(FORMULAS)} formulas")

if __name__ == "__main__":
    main()
