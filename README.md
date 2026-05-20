# 101% — лендинг учебного центра (v2)

Обновлённая версия с применением рекомендаций 4 экспертов (конверсия, UX, UI, perf+SEO+копирайт).

## Что изменилось vs v1

### Структура / воронка
- **Hero перестроен** — outcome-first headline («Готовим к нацсертификату, IELTS и Westminster»), фокус на бренде Нодира, inline 2-field форма прямо в hero, упоминание «7 в Westminster в 2025» как главное trust-сообщение.
- **Новая секция «Реальные результаты»** — карточки с именами выпускников (**Эшева Камола — 18 вузов**, **Каримов Исвандиер — 7 вузов**, **3 ученика на 100 баллов**). Удалена бесполезная цифра «414 подписчиков».
- **Новая секция «О Нодире»** — биография, выпускник РГУ нефти и газа им. Губкина, история про олимпиаду в Чехии, цитата.
- **Math как настоящий флагман** — отдельная full-width карточка, тёмный фон, не просто «жёлтая плашка как у всех».
- **Premium 1:1 переформулирован** — «6 мест в год, осталось 2» вместо безликого «по запросу».
- **12 TG-каналов сжаты** — 4 выделенных + collapsible details для остальных 8.
- **Лид-форма переехала** — теперь после value, а не после hero.

### Дизайн
- **Mobile menu (hamburger)** — фикс критичного UX-бага v1, где меню просто исчезало.
- **Focus states везде** — accessibility WCAG.
- **Emoji-иконки удалены** из USP — заменены на нумерацию 01–04.
- **Custom SVG-иконки** в navbar, FAB-кнопках и lock-замке вместо ✈️/🔒.
- **Один gradient момент** — только в hero accent. Удалены 3 дубликата (`.discount__big`, `.result-num`, `.course--flagship`).
- **Dual FAB** — Telegram + Call вместо только Telegram.
- **Static map placeholder** — кликаемый SVG, реальный iframe Яндекс загружается по клику (экономит ~2 MB JS на первой загрузке).
- **Скидки убраны как отдельная секция** — переформулировано как «бонусы», не как «купоны для скидок» (по совету эксперта-копирайтера).

### SEO / Performance
- **Schema.org JSON-LD** — EducationalOrganization + Person для Нодира + AggregateRating + Address + OpeningHours + sameAs всех соцсетей.
- **robots.txt** + **sitemap.xml** — добавлены.
- **Canonical URL** — добавлен.
- **Self-curated Google Fonts** — Manrope только 4 веса (400/600/700/800) вместо 5.
- **`decoding="async"`** на всех `<img>`.
- **Aspect-ratio на map** — устранение CLS.
- **Vercel: 7-day cache** на PDF вместо 1 hour.

### Копирайт
- **H1**: outcome-driven, не «Math + English in 101%».
- **«Записаться»** → **«Записаться на пробный урок»**.
- **«На Telegram»** → **«в Telegram»** (русская норма).
- **Tone**: больше голоса Нодира («открыто, без отбора», цитата из его поста).
- **Lead magnet promise**: «Что должен знать ребёнок к нацсертификату» (parent-emotion) вместо product-list «50 формул».
- **Опция «Просто PDF» удалена** из dropdown формы.

## Что ещё критично доделать перед лайвом

| # | Что | Кто | Срочность |
|---|---|---|---|
| 1 | **Реальное фото Нодира** для hero + about (300×400 портрет). Сейчас placeholder с инициалами «НН». | Нодир | 🔴 |
| 2 | **PDF — 10 формул вместо 50.** Можно запускать так, но в продакшене Нодир должен дописать остальные 40 в `_build_lead_magnet.py` и пересобрать. | Нодир | 🟡 |
| 3 | **TikTok URL** — короткая ссылка работает, но если хотим embed видео — нужны 3-5 прямых URL роликов. | Нодир | 🟢 |
| 4 | **Домен** — `101percent.uz` в реестре ACTIVE, нужно подтвердить владельца у Нодира и направить DNS на Vercel. | Нодир | 🟡 |
| 5 | **«6 мест осталось 2» — реальные цифры?** Сейчас стоит «осталось 2». Нодир должен подтвердить или поправить. | Нодир | 🟢 |
| 6 | **Logo SVG** — JPG 328×328 размыт на retina. Если можно достать оригинал — заменить. | Нодир | 🟢 |

## Структура проекта

```
site-v2-updated/
├── index.html              # обновлённая структура, schema.org JSON-LD
├── styles.css              # focus states, mobile menu, single gradient
├── script.js               # mobile menu toggle, dual forms, map trigger
├── _build_lead_magnet.py   # генератор PDF с 10 формулами
├── vercel.json             # security headers + cache
├── robots.txt              # NEW
├── sitemap.xml             # NEW
├── README.md               # этот файл
└── assets/
    ├── logo.jpg, cover.jpg
    └── lead-magnet.pdf
```

## Локальный запуск

```bash
cd site-v2-updated
python3 -m http.server 4174
# → http://localhost:4174
```

## Деплой на Vercel

```bash
npm i -g vercel
cd site-v2-updated
vercel          # preview
vercel --prod   # production
```

В дашборде Vercel → Domains → подключить `101percent.uz`.
DNS у регистратора `.uz`:
- A `@` → `76.76.21.21`
- CNAME `www` → `cname.vercel-dns.com`
