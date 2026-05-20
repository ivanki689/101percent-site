#!/usr/bin/env python3
"""Generate the 50-formula lead-magnet PDF for 101% (v3 full)."""

from pathlib import Path
from weasyprint import HTML, CSS

HERE = Path(__file__).resolve().parent
LOGO = HERE / "assets" / "logo.jpg"
OUT  = HERE / "assets" / "lead-magnet.pdf"


BASIC_FORMULAS = [
    {
        "n": "01", "title": "Квадратное уравнение",
        "expr": "x = (−b ± √(b² − 4ac)) / (2a)",
        "body": "Для уравнения <em>ax² + bx + c = 0</em> корни находятся через дискриминант <em>D = b² − 4ac</em>. Скобки в знаменателе — обязательны.",
        "example": "<strong>Пример.</strong> 2x² − 5x + 2 = 0 → D = 25 − 16 = 9 → √D = 3 → x₁ = 2, x₂ = 0.5",
    },
    {
        "n": "02", "title": "Теорема Виета",
        "expr": "x₁ + x₂ = −b/a · · · x₁ · x₂ = c/a",
        "body": "Сумма и произведение корней приведённого квадратного уравнения <em>x² + px + q = 0</em>.",
        "example": "<strong>Пример.</strong> x² − 5x + 6 = 0 → x₁ + x₂ = 5, x₁ · x₂ = 6 → корни 2 и 3.",
    },
    {
        "n": "03", "title": "Арифметическая прогрессия",
        "expr": "aₙ = a₁ + d(n−1) · · · Sₙ = n(a₁ + aₙ) / 2",
        "body": "Каждый член отличается от предыдущего на одно и то же число <em>d</em> (разность).",
        "example": "<strong>Пример.</strong> a₁ = 3, d = 2 → a₁₀ = 21 → S₁₀ = 10·(3+21)/2 = 120",
    },
    {
        "n": "04", "title": "Геометрическая прогрессия",
        "expr": "bₙ = b₁ · q^(n−1) · · · Sₙ = b₁(qⁿ − 1) / (q − 1), q ≠ 1",
        "body": "Каждый член — предыдущий умноженный на знаменатель <em>q</em>. При q = 1 все члены равны b₁, и сумма Sₙ = n·b₁.",
        "example": "<strong>Пример.</strong> b₁ = 2, q = 3 → b₅ = 162 → S₅ = 242",
    },
    {
        "n": "05", "title": "Свойства логарифмов",
        "expr": "log(ab) = log a + log b · · · log(a/b) = log a − log b · · · log(aⁿ) = n · log a",
        "body": "Три ключевых тождества. Условия: <em>a > 0, b > 0</em>, основание > 0 и ≠ 1.",
        "example": "<strong>Пример.</strong> log₂ 32 = log₂(2⁵) = 5 · log₂ 2 = 5",
    },
    {
        "n": "06", "title": "Основное тригонометрическое тождество",
        "expr": "sin²α + cos²α = 1",
        "body": "Из него выводятся ВСЕ остальные тождества. Запомнить раз и навсегда.",
        "example": "<strong>Пример.</strong> Если sin α = 3/5, то cos²α = 16/25 → cos α = ±4/5",
    },
    {
        "n": "07", "title": "Формулы сокращённого умножения",
        "expr": "(a±b)² = a² ± 2ab + b² · · · a² − b² = (a−b)(a+b) · · · (a±b)³ = a³ ± 3a²b + 3ab² ± b³",
        "body": "База разложения многочленов на множители. Используется в каждом 3-м задании нацсертификата.",
        "example": "<strong>Пример.</strong> x² − 9 = (x − 3)(x + 3); 4x² + 12x + 9 = (2x + 3)²",
    },
    {
        "n": "08", "title": "Производная — базовые формулы",
        "expr": "(xⁿ)' = n·xⁿ⁻¹ · · · (sin x)' = cos x · · · (cos x)' = −sin x · · · (eˣ)' = eˣ · · · (ln x)' = 1/x",
        "body": "Минимум для большинства задач на производные. Производная суммы = сумма производных.",
        "example": "<strong>Пример.</strong> f(x) = 3x⁴ + sin x → f'(x) = 12x³ + cos x",
    },
    {
        "n": "09", "title": "Комбинаторика — основные формулы",
        "expr": "Pₙ = n! · · · Aₙᵏ = n! / (n−k)! · · · Cₙᵏ = n! / (k! · (n−k)!)",
        "body": "Перестановки (P), размещения (A), сочетания (C). «Три кита» комбинаторики.",
        "example": "<strong>Пример.</strong> Выбрать 3 из 5: C₅³ = 5! / (3!·2!) = 10",
    },
    {
        "n": "10", "title": "Теорема Пифагора и площади",
        "expr": "a² + b² = c² · · · S△ = ½·a·h · · · S○ = π·r²",
        "body": "Прямоугольный треугольник + базовые формулы площадей — фундамент геометрии в тесте.",
        "example": "<strong>Пример.</strong> Катеты 3 и 4 → гипотенуза 5. Радиус 2 → S = 4π.",
    },
]


ALGEBRA_FORMULAS = [
    {
        "n": "11", "title": "Свойства степеней",
        "expr": "aᵐ · aⁿ = aᵐ⁺ⁿ · · · (aᵐ)ⁿ = aᵐⁿ · · · aᵐ / aⁿ = aᵐ⁻ⁿ · · · a⁰ = 1 · · · a⁻ⁿ = 1/aⁿ",
        "body": "Базовые операции со степенями с одинаковым основанием.",
        "example": "<strong>Пример.</strong> 2³ · 2⁵ = 2⁸ = 256; (3²)⁴ = 3⁸; 5⁻² = 1/25",
    },
    {
        "n": "12", "title": "Свойства корней",
        "expr": "ⁿ√(ab) = ⁿ√a · ⁿ√b · · · ⁿ√(a/b) = ⁿ√a / ⁿ√b · · · ⁿ√(aᵐ) = aᵐ⁄ⁿ",
        "body": "Корень n-й степени = степень с дробным показателем. Для чётного n обязательно a, b ≥ 0 (иначе √(−4·−9) ≠ √−4·√−9).",
        "example": "<strong>Пример.</strong> √12 = 2√3; ³√(2⁶) = 4",
    },
    {
        "n": "13", "title": "Сумма и разность кубов",
        "expr": "a³ + b³ = (a + b)(a² − ab + b²) · · · a³ − b³ = (a − b)(a² + ab + b²)",
        "body": "Формулы разложения суммы и разности кубов на множители.",
        "example": "<strong>Пример.</strong> x³ − 8 = (x − 2)(x² + 2x + 4)",
    },
    {
        "n": "14", "title": "Переход к новому основанию логарифма",
        "expr": "log_a b = log_c b / log_c a · · · log_a b · log_b a = 1 · · · a^(log_a b) = b",
        "body": "Любой логарифм можно выразить через другое основание. Условия: a, b, c > 0; a ≠ 1, c ≠ 1; для второй формулы ещё b ≠ 1.",
        "example": "<strong>Пример.</strong> log₈ 32 = log₂ 32 / log₂ 8 = 5/3",
    },
    {
        "n": "15", "title": "Сумма бесконечной геометрической прогрессии",
        "expr": "S = b₁ / (1 − q), где |q| < 1",
        "body": "Если |q| < 1, бесконечная сумма сходится к конечному значению.",
        "example": "<strong>Пример.</strong> 1 + 1/2 + 1/4 + 1/8 + … = 1/(1 − 1/2) = 2",
    },
    {
        "n": "16", "title": "Бином Ньютона",
        "expr": "(a + b)ⁿ = Σ Cₙᵏ · aⁿ⁻ᵏ · bᵏ, k = 0…n",
        "body": "Разложение n-й степени двучлена. Коэффициенты — биномиальные числа Cₙᵏ (треугольник Паскаля).",
        "example": "<strong>Пример.</strong> (a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴",
    },
    {
        "n": "17", "title": "Показательные уравнения",
        "expr": "aᶠ⁽ˣ⁾ = aᵍ⁽ˣ⁾ ⇔ f(x) = g(x), при a > 0, a ≠ 1",
        "body": "Если основания равны, уравнение сводится к равенству показателей.",
        "example": "<strong>Пример.</strong> 2^(x+1) = 8 → 2^(x+1) = 2³ → x = 2",
    },
    {
        "n": "18", "title": "Логарифмические уравнения",
        "expr": "log_a f(x) = log_a g(x) ⇔ f(x) = g(x), при f(x) > 0, g(x) > 0",
        "body": "При равных основаниях логарифмов аргументы равны. Проверка ОДЗ обязательна.",
        "example": "<strong>Пример.</strong> log₃(x + 1) = log₃ 5 → x = 4",
    },
    {
        "n": "19", "title": "Уравнения с модулем",
        "expr": "|x| = a ⇔ x = ±a (a ≥ 0) · · · |f(x)| = |g(x)| ⇔ f(x) = ±g(x)",
        "body": "Модуль раскрывается с двумя знаками. При a < 0 уравнение решений не имеет.",
        "example": "<strong>Пример.</strong> |2x − 3| = 5 → 2x − 3 = ±5 → x = 4 или x = −1",
    },
    {
        "n": "20", "title": "Квадратичные неравенства",
        "expr": "При D > 0, a > 0, x₁ < x₂: ax²+bx+c > 0 ⇔ x < x₁ или x > x₂ · · · < 0 ⇔ x₁ < x < x₂",
        "body": "Правило работает при D > 0 (есть два разных корня) и a > 0. Если D ≤ 0 — трёхчлен не меняет знак: либо всегда положителен (a > 0), либо всегда отрицателен (a < 0).",
        "example": "<strong>Пример.</strong> x² − 5x + 6 > 0: корни 2 и 3 → x < 2 или x > 3",
    },
    {
        "n": "21", "title": "Метод интервалов",
        "expr": "(x − x₁)…(x − xₙ): расставить корни, чередовать знаки справа налево с «+»",
        "body": "Универсальный способ решения рациональных неравенств.",
        "example": "<strong>Пример.</strong> (x − 1)(x − 4) ≤ 0 ⇔ 1 ≤ x ≤ 4",
    },
    {
        "n": "22", "title": "Системы линейных уравнений (Крамер)",
        "expr": "Δ = a₁b₂ − a₂b₁ · · · Δₓ = c₁b₂ − c₂b₁ · · · Δᵧ = a₁c₂ − a₂c₁ · · · x = Δₓ/Δ, y = Δᵧ/Δ (Δ ≠ 0)",
        "body": "Для системы a₁x + b₁y = c₁; a₂x + b₂y = c₂. Δ — главный определитель, Δₓ и Δᵧ получаются заменой соответствующего столбца на столбец свободных членов. Δ = 0 → нет единственного решения.",
        "example": "<strong>Пример.</strong> 2x + y = 5; x − y = 1 → Δ = −3, Δₓ = −6, Δᵧ = −3 → x = 2, y = 1",
    },
    {
        "n": "23", "title": "Область определения функции (ОДЗ)",
        "expr": "√f: f ≥ 0 · · · 1/f: f ≠ 0 · · · log_a f: f > 0, a > 0, a ≠ 1 · · · tg x: x ≠ π/2 + πn, n ∈ ℤ",
        "body": "Перед решением уравнения или неравенства всегда находят ОДЗ. Корни, не входящие в ОДЗ, отбрасываются.",
        "example": "<strong>Пример.</strong> y = √(x − 3) + log(5 − x): ОДЗ = [3; 5)",
    },
    {
        "n": "24", "title": "Обратная функция",
        "expr": "y = f(x) · · · f⁻¹(f(x)) = x · · · графики f и f⁻¹ симметричны относительно прямой y = x",
        "body": "Обратная функция существует, если f монотонна на области определения. Чтобы найти f⁻¹: поменять местами x и y, выразить y.",
        "example": "<strong>Пример.</strong> y = 2x + 3 → x = 2y + 3 → y = (x − 3) / 2",
    },
    {
        "n": "25", "title": "Преобразования графиков функций",
        "expr": "y = f(x) + a: сдвиг вверх/вниз · · · y = f(x − b): сдвиг вправо/влево · · · y = k·f(x): растяжение · · · y = f(−x): отражение",
        "body": "Базовые геометрические преобразования. Сдвиг внутри аргумента — в обратную сторону.",
        "example": "<strong>Пример.</strong> y = (x − 2)² + 3: парабола сдвинута на 2 вправо и 3 вверх",
    },
]


GEOMETRY_FORMULAS = [
    {
        "n": "26", "title": "Сумма углов треугольника",
        "expr": "α + β + γ = 180°",
        "body": "Сумма трёх внутренних углов любого треугольника всегда равна 180°.",
        "example": "<strong>Пример.</strong> Два угла 45° и 70° → третий = 65°.",
    },
    {
        "n": "27", "title": "Площадь треугольника через синус",
        "expr": "S = ½ · a · b · sin C",
        "body": "Половина произведения двух сторон на синус угла между ними.",
        "example": "<strong>Пример.</strong> a = 6, b = 8, C = 30° → S = 12.",
    },
    {
        "n": "28", "title": "Формула Герона",
        "expr": "S = √(p(p−a)(p−b)(p−c)), p = (a+b+c)/2",
        "body": "Площадь треугольника через три стороны и полупериметр p.",
        "example": "<strong>Пример.</strong> Стороны 3, 4, 5: p = 6 → S = √36 = 6.",
    },
    {
        "n": "29", "title": "Теорема косинусов",
        "expr": "a² = b² + c² − 2bc · cos A",
        "body": "Обобщение теоремы Пифагора (при A = 90° даёт a² = b² + c²).",
        "example": "<strong>Пример.</strong> b = 5, c = 8, A = 60° → a² = 49 → a = 7.",
    },
    {
        "n": "30", "title": "Теорема синусов",
        "expr": "a/sin A = b/sin B = c/sin C = 2R",
        "body": "Отношение стороны к синусу противолежащего угла = диаметр описанной окружности 2R.",
        "example": "<strong>Пример.</strong> a = 10, A = 30° → 2R = 20 → R = 10.",
    },
    {
        "n": "31", "title": "Радиусы вписанной и описанной окружностей",
        "expr": "r = S/p · · · R = abc / (4S)",
        "body": "Радиус вписанной — S/полупериметр. Радиус описанной — abc/(4S).",
        "example": "<strong>Пример.</strong> Треугольник 3-4-5: r = 1, R = 2.5.",
    },
    {
        "n": "32", "title": "Площадь параллелограмма",
        "expr": "S = a · h = a · b · sin α",
        "body": "Основание на высоту, либо две смежные стороны на синус угла между ними.",
        "example": "<strong>Пример.</strong> Стороны 6 и 10, угол 30° → S = 30.",
    },
    {
        "n": "33", "title": "Площадь трапеции",
        "expr": "S = ((a + b) / 2) · h",
        "body": "Полусумма параллельных оснований на высоту.",
        "example": "<strong>Пример.</strong> Основания 6 и 10, высота 4 → S = 32.",
    },
    {
        "n": "34", "title": "Длина окружности",
        "expr": "C = 2π · r = π · d",
        "body": "Произведение диаметра на π. Принимают π ≈ 3.14.",
        "example": "<strong>Пример.</strong> r = 5 → C = 31.4.",
    },
    {
        "n": "35", "title": "Длина дуги и площадь сектора",
        "expr": "l = r · α · · · S = ½ · r² · α   (α в радианах)",
        "body": "Длина дуги — радиус на угол в радианах. Площадь сектора — половина r² на α.",
        "example": "<strong>Пример.</strong> r = 6, α = π/3 → l = 2π, S = 6π.",
    },
    {
        "n": "36", "title": "Теорема о вписанном угле",
        "expr": "∠вписанный = ½ · ∠центральный",
        "body": "Вписанный угол вдвое меньше центрального, опирающегося на ту же дугу. Вписанный угол на диаметр = 90°.",
        "example": "<strong>Пример.</strong> Центральный 80° → вписанный 40°.",
    },
    {
        "n": "37", "title": "Средняя линия треугольника",
        "expr": "MN ∥ AC, MN = ½ · AC",
        "body": "Соединяет середины двух сторон, параллельна третьей и равна её половине.",
        "example": "<strong>Пример.</strong> AC = 14 → средняя линия = 7.",
    },
    {
        "n": "38", "title": "Объём призмы и параллелепипеда",
        "expr": "V = S · h   (куб: V = a³)",
        "body": "Площадь основания на высоту. Куб со стороной a имеет объём a³.",
        "example": "<strong>Пример.</strong> Параллелепипед 3 × 4 × 5 → V = 60.",
    },
    {
        "n": "39", "title": "Объём цилиндра и конуса",
        "expr": "V_цил = π · r² · h · · · V_кон = ⅓ · π · r² · h",
        "body": "Объём конуса в 3 раза меньше цилиндра с теми же r и h.",
        "example": "<strong>Пример.</strong> r = 3, h = 5 → V_цил = 45π, V_кон = 15π.",
    },
    {
        "n": "40", "title": "Объём и площадь поверхности шара",
        "expr": "V = (4/3) · π · r³ · · · S = 4π · r²",
        "body": "Объём — 4/3 π на куб радиуса. Площадь поверхности — 4 площади большого круга.",
        "example": "<strong>Пример.</strong> r = 3 → V = 36π, S = 36π.",
    },
]


TRIG_CALC_PROB_FORMULAS = [
    {
        "n": "41", "title": "Формулы двойного угла",
        "expr": "sin 2α = 2 sin α · cos α · · · cos 2α = cos²α − sin²α = 1 − 2sin²α = 2cos²α − 1",
        "body": "Базовые формулы для упрощения и решения тригонометрических уравнений.",
        "example": "<strong>Пример.</strong> sin α = 3/5 → cos α = 4/5 → sin 2α = 24/25.",
    },
    {
        "n": "42", "title": "Формулы суммы и разности",
        "expr": "sin(α ± β) = sin α · cos β ± cos α · sin β · · · cos(α ± β) = cos α · cos β ∓ sin α · sin β",
        "body": "Для вычисления тригонометрических функций нестандартных углов и упрощения выражений.",
        "example": "<strong>Пример.</strong> cos 75° = cos(45° + 30°) = (√6 − √2) / 4.",
    },
    {
        "n": "43", "title": "Формулы понижения степени",
        "expr": "sin²α = (1 − cos 2α) / 2 · · · cos²α = (1 + cos 2α) / 2",
        "body": "Незаменимы при интегрировании тригонометрических выражений и уравнениях sin²x = a.",
        "example": "<strong>Пример.</strong> sin²x = 1/4 → cos 2x = 1/2 → x = ±π/6 + πk.",
    },
    {
        "n": "44", "title": "Значения функций основных углов",
        "expr": "sin: 0°→0, 30°→½, 45°→√2/2, 60°→√3/2, 90°→1 · · · cos: зеркально · · · tg 45° = 1, tg 60° = √3",
        "body": "Таблицу нужно знать наизусть — без неё ни одна задача не решается.",
        "example": "<strong>Пример.</strong> sin 30° + cos 60° + tg 45° = 1/2 + 1/2 + 1 = 2.",
    },
    {
        "n": "45", "title": "Производная произведения и частного",
        "expr": "(u · v)' = u' · v + u · v' · · · (u / v)' = (u' · v − u · v') / v²",
        "body": "При дифференцировании произведений, дробей, многочленов.",
        "example": "<strong>Пример.</strong> f = x² · sin x → f' = 2x · sin x + x² · cos x.",
    },
    {
        "n": "46", "title": "Производная сложной функции (цепное правило)",
        "expr": "(f(g(x)))' = f'(g(x)) · g'(x)",
        "body": "Для функций «функция от функции» — sin(2x), e^(3x), √(x²+1).",
        "example": "<strong>Пример.</strong> y = sin(3x² + 1) → y' = cos(3x² + 1) · 6x.",
    },
    {
        "n": "47", "title": "Уравнение касательной к графику",
        "expr": "y = f(x₀) + f'(x₀) · (x − x₀)",
        "body": "Касательная в точке x₀: значение функции плюс наклон на отклонение.",
        "example": "<strong>Пример.</strong> y = x², x₀ = 2 → касательная: y = 4x − 4.",
    },
    {
        "n": "48", "title": "Формула Ньютона–Лейбница",
        "expr": "∫ₐᵇ f(x) dx = F(b) − F(a), где F'(x) = f(x)",
        "body": "Определённый интеграл = разность значений первообразной. Геометрически — площадь под графиком.",
        "example": "<strong>Пример.</strong> ∫₀¹ x² dx = [x³/3]₀¹ = 1/3.",
    },
    {
        "n": "49", "title": "Классическое определение вероятности",
        "expr": "P(A) = m / n, где m — благоприятных, n — общее число равновозможных исходов",
        "body": "Для конечного числа равновозможных исходов: монеты, кости, карты, шары.",
        "example": "<strong>Пример.</strong> В урне 3 белых и 7 чёрных. P(белый) = 3/10.",
    },
    {
        "n": "50", "title": "Сложение и умножение вероятностей",
        "expr": "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) · · · независимые: P(A ∩ B) = P(A) · P(B)",
        "body": "Сложение — «хотя бы одно событие». Умножение — «оба события произошли» (для независимых).",
        "example": "<strong>Пример.</strong> Две монеты. P(оба орла) = 1/2 · 1/2 = 1/4.",
    },
]


SECTIONS = [
    ("Базовые формулы", "Минимум, без которого ни одна задача нацсертификата не решается.", BASIC_FORMULAS),
    ("Алгебра", "Степени, корни, логарифмы, уравнения и неравенства, функции.", ALGEBRA_FORMULAS),
    ("Геометрия", "Планиметрия (треугольники, окружности, многоугольники) и стереометрия (объёмы).", GEOMETRY_FORMULAS),
    ("Тригонометрия, анализ и теорвер", "Тригонометрические тождества, производные, интегралы, вероятности.", TRIG_CALC_PROB_FORMULAS),
]


def render_wall_sheet():
    """Single-page concentrate: 18 must-know formulas, designed to be printed
    and stuck on the wall above a student's desk."""
    return '''
<section class="wall-sheet">
  <header class="ws-head">
    <div class="ws-title">СТЕНА</div>
    <div class="ws-meta">
      <div class="ws-sub">18 формул, которые решают нацсертификат</div>
      <div class="ws-url">101percent.uz · Нодир Нуриддинов</div>
    </div>
  </header>

  <div class="ws-grid">
    <div class="ws-col">
      <div class="ws-band">АЛГЕБРА</div>
      <div class="ws-f ws-anchor"><span class="ws-n">01</span><div class="ws-t">Квадратное уравнение</div><div class="ws-e">x = (−b ± √(b² − 4ac)) / (2a)</div></div>
      <div class="ws-f"><span class="ws-n">02</span><div class="ws-t">Виета</div><div class="ws-e">x₁ + x₂ = −b/a · · · x₁ · x₂ = c/a</div></div>
      <div class="ws-f"><span class="ws-n">07</span><div class="ws-t">Сокращённое умножение</div><div class="ws-e">(a ± b)² = a² ± 2ab + b²<br>a² − b² = (a − b)(a + b)<br>(a ± b)³ = a³ ± 3a²b + 3ab² ± b³</div></div>
      <div class="ws-f"><span class="ws-n">11</span><div class="ws-t">Степени</div><div class="ws-e">aᵐ · aⁿ = aᵐ⁺ⁿ · · · (aᵐ)ⁿ = aᵐⁿ<br>aᵐ / aⁿ = aᵐ⁻ⁿ · · · a⁻ⁿ = 1/aⁿ</div></div>
      <div class="ws-f"><span class="ws-n">12</span><div class="ws-t">Корни</div><div class="ws-e">ⁿ√(ab) = ⁿ√a · ⁿ√b<br>ⁿ√(aᵐ) = aᵐ⁄ⁿ</div></div>
      <div class="ws-f"><span class="ws-n">05</span><div class="ws-t">Логарифмы</div><div class="ws-e">log(ab) = log a + log b<br>log(a/b) = log a − log b<br>log(aⁿ) = n · log a</div></div>
      <div class="ws-f ws-anchor"><span class="ws-n">23</span><div class="ws-t">ОДЗ — частая ловушка</div><div class="ws-e">√f: f ≥ 0 · · · 1/f: f ≠ 0<br>log f: f > 0 · · · tg x: x ≠ π/2 + πn</div></div>
    </div>

    <div class="ws-col">
      <div class="ws-band">ГЕОМЕТРИЯ</div>
      <div class="ws-f"><span class="ws-n">10</span><div class="ws-t">Пифагор + площади</div><div class="ws-e">a² + b² = c²<br>S△ = ½ · a · h · · · S○ = π · r²</div></div>
      <div class="ws-f"><span class="ws-n">27</span><div class="ws-t">Площадь через синус</div><div class="ws-e">S = ½ · a · b · sin C</div></div>
      <div class="ws-f"><span class="ws-n">29</span><div class="ws-t">Теорема косинусов</div><div class="ws-e">a² = b² + c² − 2bc · cos A</div></div>
      <div class="ws-f"><span class="ws-n">30</span><div class="ws-t">Теорема синусов</div><div class="ws-e">a / sin A = b / sin B = c / sin C = 2R</div></div>
      <div class="ws-f"><span class="ws-n">39</span><div class="ws-t">Цилиндр и конус</div><div class="ws-e">V_цил = π · r² · h<br>V_кон = ⅓ · π · r² · h</div></div>
      <div class="ws-f"><span class="ws-n">40</span><div class="ws-t">Шар</div><div class="ws-e">V = (4/3) · π · r³<br>S = 4π · r²</div></div>
    </div>

    <div class="ws-col">
      <div class="ws-band">ТРИГ · АНАЛИЗ · ВЕРОЯТНОСТЬ</div>
      <div class="ws-f ws-anchor"><span class="ws-n">06</span><div class="ws-t">Главное тождество</div><div class="ws-e">sin²α + cos²α = 1</div></div>
      <div class="ws-f ws-anchor"><span class="ws-n">44</span><div class="ws-t">Углы — наизусть</div>
        <table class="ws-tab">
          <tr><th>α</th><th>0°</th><th>30°</th><th>45°</th><th>60°</th><th>90°</th></tr>
          <tr><th>sin</th><td>0</td><td>½</td><td>√2⁄2</td><td>√3⁄2</td><td>1</td></tr>
          <tr><th>cos</th><td>1</td><td>√3⁄2</td><td>√2⁄2</td><td>½</td><td>0</td></tr>
        </table>
      </div>
      <div class="ws-f"><span class="ws-n">08</span><div class="ws-t">Производные</div><div class="ws-e">(xⁿ)' = n · xⁿ⁻¹<br>(sin x)' = cos x · (cos x)' = −sin x<br>(eˣ)' = eˣ · (ln x)' = 1/x</div></div>
      <div class="ws-f"><span class="ws-n">09</span><div class="ws-t">Комбинаторика</div><div class="ws-e">Pₙ = n!<br>Aₙᵏ = n! / (n − k)!<br>Cₙᵏ = n! / (k! · (n − k)!)</div></div>
      <div class="ws-f"><span class="ws-n">50</span><div class="ws-t">Вероятности</div><div class="ws-e">P(A ∪ B) = P(A) + P(B) − P(A ∩ B)<br>независимые: P(A ∩ B) = P(A) · P(B)</div></div>
    </div>
  </div>

  <footer class="ws-foot">
    ЗАПОМНИЛ ЭТИ 18 — СДАЛ НА 70+
    <span class="ws-foot-tag">вырежи и наклей над столом · 101percent.uz</span>
  </footer>
</section>
'''


def render_section(title, intro, formulas):
    cards = []
    for f in formulas:
        cards.append(f'''
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
    return f'''
<section class="section">
  <div class="section-head">
    <h2>{title}</h2>
    <p class="section-intro">{intro}</p>
  </div>
  {"".join(cards)}
</section>
'''


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
    <p class="meta">Версия 3.0 · 2026 · 101percent.uz</p>
  </div>
</section>

<section class="intro">
  <h2>Что внутри</h2>
  <p>50 ключевых формул, которые встречаются на национальном сертификате по математике
  в Узбекистане <strong>каждый год</strong>. Это не «отличная подборка для отличников» —
  это <strong>обязательный минимум</strong>, без которого ребёнок не наберёт даже 60 баллов.</p>
  <p>Структура: <strong>4 раздела</strong> — базовые формулы, алгебра, геометрия,
  тригонометрия с анализом и теорвером. Каждая карточка содержит формулу,
  объяснение и конкретный пример применения.</p>

  <div class="callout">
    <h3>Как пользоваться шпаргалкой</h3>
    <ol>
      <li><strong>Следующая страница — «СТЕНА»</strong>: выжимка из 18 самых критичных формул. Распечатайте отдельно, наклейте над столом.</li>
      <li>Каждый день — по 5 формул из полного набора: прочитать → объяснить себе → решить пример. Поставьте галочку в чекбоксе справа.</li>
      <li>За 10 дней — все 50 формул закрыты. Это даёт прирост 15–25 баллов нацсертификата.</li>
      <li>Раз в неделю — пересматривайте «СТЕНА». Если запомнили эти 18 — сдадите на 70+.</li>
    </ol>
  </div>
</section>

{render_wall_sheet()}

{render_section(*SECTIONS[0])}
{render_section(*SECTIONS[1])}
{render_section(*SECTIONS[2])}
{render_section(*SECTIONS[3])}

<section class="cta">
  <h2>Что дальше</h2>
  <p>Запишитесь на <strong>бесплатный пробный урок</strong> с диагностикой уровня — Нодир
  лично разберёт пробелы вашего ребёнка и составит план подготовки к нацсертификату
  на 6–12–24 месяца.</p>
  <p class="phone-link">📞 +998 90 023-45-60</p>
  <p class="tg-link">✈️ t.me/LC101percent</p>
  <p class="small">Учебный центр 101% · Ташкент, Шайхантахурский район, м-в Джангох д. 26</p>
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
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-size: 8pt;
    color: #6B6B6B;
  }
}
@page wall {
  size: A4;
  margin: 0;
  @bottom-center { content: none; }
}

* { box-sizing: border-box; }

html, body {
  /* DejaVu has full Cyrillic + subscript Unicode (ₙ ₖ ᵐ ᵏ) — fixes "?" boxes in formulas */
  font-family: "DejaVu Sans", "Helvetica", "Arial", sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
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
.brand { font-size: 12pt; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; margin: 0 0 28mm; }
.cover h1 { font-size: 38pt; font-weight: 800; line-height: 1.05; letter-spacing: -0.02em; margin: 0 0 18mm; }
.subtitle { font-size: 13pt; font-weight: 500; margin-bottom: 30mm; }
.meta { font-size: 9pt; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(22,22,22,0.6); margin: 0; }

h2 {
  font-size: 20pt;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #161616;
  margin: 0 0 5mm;
  padding-bottom: 3mm;
  border-bottom: 3px solid #FFC93C;
}
h3 { font-size: 12pt; font-weight: 700; color: #161616; margin: 0; }
p { margin: 0 0 3mm; }

.intro { padding: 6mm 0 8mm; page-break-after: always; }

.callout {
  background: #FFF6DC;
  border-left: 4px solid #F39C12;
  padding: 5mm 6mm;
  margin: 6mm 0;
  border-radius: 4px;
  page-break-inside: avoid;
}
.callout h3 { font-size: 12pt; margin-bottom: 2mm; color: #C76A0A; }
.callout ol { margin: 0; padding-left: 5mm; }
.callout li { padding: 1mm 0; font-size: 10pt; }

/* Sections: keep first formula with header, but DON'T force page break before each section */
.section { padding: 5mm 0 3mm; }
.section:first-of-type { padding-top: 0; }
.section-head { margin-bottom: 4mm; page-break-after: avoid; }
.section-intro { color: #6B6B6B; font-size: 10pt; margin-top: 2mm; }

.formula-card {
  background: #FAF8F3;
  border-left: 3px solid #161616;
  border-radius: 0 8px 8px 0;
  padding: 3.5mm 5mm;
  margin: 2.5mm 0;
  page-break-inside: avoid;
  position: relative;
}
/* Checkbox in upper-right — progress mechanic */
.formula-card::after {
  content: "";
  position: absolute;
  top: 4mm;
  right: 4mm;
  width: 4mm;
  height: 4mm;
  border: 1px solid #999;
  border-radius: 2px;
}
.formula-head {
  display: flex;
  align-items: baseline;
  gap: 3mm;
  margin-bottom: 2mm;
  padding-right: 8mm;
}
.formula-num {
  background: #161616;
  color: #FFC93C;
  font-weight: 800;
  padding: 1mm 2.5mm;
  border-radius: 3px;
  font-size: 8.5pt;
  letter-spacing: 0.08em;
  flex-shrink: 0;
  font-family: "DejaVu Sans", "Helvetica", sans-serif;
}
.formula-body { font-size: 9.5pt; color: #2A2A2A; margin-bottom: 2mm; line-height: 1.45; }
.formula-expr {
  /* DejaVu Sans Mono renders Unicode subscripts and √ correctly */
  font-family: "DejaVu Sans Mono", "Cambria Math", "Courier New", monospace;
  font-size: 10.5pt;
  background: #FFFFFF;
  padding: 3mm 4mm;
  border: 1px dashed #F39C12;
  border-radius: 4px;
  margin: 2mm 0;
  word-spacing: 0.2em;
  line-height: 1.5;
}
.formula-example {
  background: #FFF6DC;
  padding: 2.5mm 4mm;
  border-radius: 4px;
  font-size: 9.5pt;
  font-family: "DejaVu Sans", "Helvetica", sans-serif;
  line-height: 1.45;
}

/* ===== WALL SHEET (single-page concentrate, "СТЕНА") ===== */
.wall-sheet {
  page: wall;
  width: 210mm;
  height: 297mm;
  margin: 0;
  padding: 0;
  font-family: "DejaVu Sans", "Helvetica", sans-serif;
  color: #161616;
  display: flex;
  flex-direction: column;
  page-break-before: always;
  page-break-after: always;
}
.ws-head {
  background: #161616;
  color: #FFC93C;
  padding: 7mm 12mm 6mm;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}
.ws-title {
  font-size: 36pt;
  font-weight: 800;
  letter-spacing: 4px;
  line-height: 1;
}
.ws-meta { text-align: right; }
.ws-sub { font-size: 10pt; font-weight: 700; color: #fff; }
.ws-url {
  font-size: 8pt;
  font-family: "DejaVu Sans Mono", monospace;
  color: #FFC93C;
  margin-top: 1mm;
  letter-spacing: 0.5px;
}

.ws-grid {
  flex: 1;
  display: flex;
  padding: 4mm 8mm 3mm;
  gap: 4mm;
}
.ws-col { flex: 1; display: flex; flex-direction: column; }

.ws-band {
  background: #FFC93C;
  color: #161616;
  font-weight: 800;
  font-size: 8.5pt;
  letter-spacing: 1.5px;
  padding: 2mm 3mm;
  text-align: center;
  border-left: 3px solid #161616;
  margin-bottom: 2.5mm;
}

.ws-f {
  position: relative;
  padding: 1.5mm 2mm 1.5mm 8mm;
  margin-bottom: 1.5mm;
  border-bottom: 0.3pt dashed #BBB;
  page-break-inside: avoid;
}
.ws-f:last-child { border-bottom: none; }
.ws-n {
  position: absolute;
  left: 0;
  top: 1.8mm;
  font-size: 7pt;
  font-weight: 800;
  color: #F39C12;
  font-family: "DejaVu Sans Mono", monospace;
}
.ws-t {
  font-size: 6.8pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  color: #444;
  margin-bottom: 0.8mm;
}
.ws-e {
  font-size: 9pt;
  line-height: 1.35;
  font-family: "DejaVu Sans Mono", "Cambria Math", monospace;
  color: #161616;
}

.ws-anchor {
  background: #FFF4D0;
  padding: 2mm 2.5mm 2mm 8mm;
  border-bottom: none;
  border-left: 3px solid #F39C12;
  margin: 0 0 2mm 0;
  border-radius: 0 3px 3px 0;
}
.ws-anchor .ws-e { font-size: 9.5pt; font-weight: 600; }

.ws-tab {
  width: 100%;
  border-collapse: collapse;
  font-family: "DejaVu Sans Mono", "Cambria Math", monospace;
  font-size: 8pt;
  margin-top: 1mm;
}
.ws-tab th, .ws-tab td {
  border: 0.4pt solid #161616;
  text-align: center;
  padding: 0.6mm 0;
}
.ws-tab th { background: #FFC93C; font-weight: 800; }

.ws-foot {
  background: #161616;
  color: #FFC93C;
  text-align: center;
  padding: 4mm 12mm;
  font-size: 12pt;
  font-weight: 800;
  letter-spacing: 1.5px;
  position: relative;
}
.ws-foot-tag {
  display: block;
  font-size: 6.5pt;
  font-weight: 500;
  color: #999;
  letter-spacing: 0.5px;
  text-transform: lowercase;
  margin-top: 1.5mm;
}

.cta {
  background: #161616;
  color: #FFFFFF;
  padding: 10mm;
  border-radius: 12px;
  margin: 8mm 0;
  page-break-inside: avoid;
  page-break-before: always;
}
.cta h2 { color: #FFC93C; border-bottom-color: #FFC93C; }
.cta p { color: rgba(255,255,255,0.85); }
.phone-link, .tg-link {
  font-family: "Courier New", monospace;
  font-size: 13pt;
  font-weight: 700;
  background: rgba(255, 201, 60, 0.15);
  color: #FFC93C !important;
  padding: 3mm;
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
    total = sum(len(s[2]) for s in SECTIONS)
    print(f"Rendering PDF → {OUT}")
    HTML(string=HTML_TEMPLATE).write_pdf(
        target=str(OUT),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    size_kb = OUT.stat().st_size / 1024
    print(f"OK · {size_kb:.1f} KB · {total} formulas in {len(SECTIONS)} sections")


if __name__ == "__main__":
    main()
