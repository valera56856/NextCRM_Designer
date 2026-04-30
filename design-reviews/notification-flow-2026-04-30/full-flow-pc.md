# Notification Center — Full Flow (PC)

**Date:** 2026-04-30
**Figma section:** `10885:5273` — `Notification Center — Full Flow PC — Claude mockup`
**Page:** 🟡 Центр сповіщень (`10647:120412`)

## 10 frames in 3 rows

### Row 1 — Bell interactions (5 frames)
- **A1) Closed** — dashboard з bell + лічильник `06`
- **A2) Hover bell** — tooltip preview з кількістю
- **A3) Open dropdown** — 5 нотифікацій, hover на 2-му пункті (action visible)
- **A4) Empty** — після "Прочитати все", dropdown показує "Все під контролем"
- **A5) Click notification** → side drawer (560w) з повним замовленням #8453, банер "Ви прийшли з нотифікації"

In-row flow: A1 → A2 → A3 → A4. Plus A3 → A5 при кліку.

### Row 2 — Inbox page (4 frames)
- **B1) Inbox default** — фільтр-сайдбар категорій (Всі / Критичні / Замовлення / Доставка / ...), 8 нотифікацій з checkbox + severity pill, search + period filter
- **B2) Filtered "Критичні"** — 6 critical нотифікацій, активний фільтр chip
- **B3) Empty** — "Все під контролем" centered + CTA "Перейти до замовлень"
- **B4) Click row** → side drawer (480w) з повним описом, ХРОНОЛОГІЯ ПОДІЇ, related resource link, action buttons (Повторити платіж / Зв'язатися / Відкласти)

In-row flow: B1 → B2 (filter), B1 → B3 (mark all), B1 → B4 (row click).

### Row 3 — Settings (1 frame)
- **C1) Notification preferences** — secondary nav (Профіль/Компанія/Команда/**Сповіщення**/Інтеграції/Платежі/API/Безпека), Quick toggles (DND / Quiet hour / Email digest), per-event channel matrix grouped by category (Замовлення/Склад та логістика/Система та інтеграції)

## Cross-flow connections (purple dashed)
- A3 → A5: click on notification item
- A3 → B1: click "Переглянути всі"
- B1 → B4: click on inbox row
- B1 → C1: click "Налаштування" button

## Flow logic
1. **Quick check**: A1 → A2 → A3, scan, click outside → A1
2. **Act on notif**: A1 → A3 → click "Прочитати" inline OR A5 (deep dive)
3. **Mass review**: A3 → "Переглянути всі" → B1 → filter/search → B4 detail
4. **Mark all read**: A3 → "Прочитати все" → A4 (empty)
5. **Configure**: anywhere → gear → C1 → save

## Components used (from DS)
Real Material icons via `importComponentByKeyAsync`:
- notifications, settings, warning, sync_problem, shopping_cart, shopping_bag, credit_card, chat, star, check_circle, close, more_horiz, search, filter_list, chevron_right, keyboard_arrow_down, arrow_forward, category, warehouse, description, analytics, support_agent

Sidebar: real NEXT/CRM brand mark, expandable items with chevrons, active state with badge.
Top bar: breadcrumbs + bell (with state coloring) + avatar + chevron-down.
Drawers: 560w (orders) / 480w (notification), with shadow, header banner, body sections, action buttons.

## Score
- Completeness: 8/10 (toasts not yet shown, websocket-realtime arriving notification not animated)
- Visual match to existing system: 9/10 (sidebar matches reference, dropdown style matches existing "Швидкий перегляд")
- Logical connectivity: 10/10 (all transitions explicit with cross-flow arrows)

## Sidebar fix (post-feedback)

User: "Меню получилось кривое"

**Issue:** sidebar menu items had auto-height (HUG) → uneven heights between items, ~80px gaps instead of tight 40px rows. DS icon import inflated some items.

**Fix:** All 10 dashboard sidebars in the section — set `layoutSizingVertical = 'FIXED'`, height = 40px per row. Set menu `itemSpacing = 0` (rows have own padding via height). 70 rows fixed in one pass.

**Result:** Tight, regular rhythm matching the existing "Швидкий перегляд" reference.

## /design-review pass — round 2

User feedback: "+ лого унас не такое как нужно. Исправь как у нас в дизайне"

### Findings (audit checklist)

| # | Issue | Impact | Fix |
|---|-------|--------|-----|
| F1 | Cross-flow arrows тонкі (2px) — губляться в overview | HIGH | Потовщено до 3px на всіх 4 cross-flow + всі in-row arrows |
| F2 | Frame labels — звичайний 12px текст, слабкий visual indicator | MEDIUM | Замінено на кольорові chips (A=blue, B=purple, C=green) + текст label |
| F-LOGO | Самодільний brand mark (чорний квадрат + N + NEXT/CRM текст) — не відповідає DS | **HIGH** | Імпортовано real DS Logo component (`Property 1=Default`, key `df41f5a13a1fc34dda0cf516ae99d5bb25007afe`). Заміна 10 з 10 sidebars. |

### Score
- **Design Score**: A → A+
- **Visual match to existing system**: 9 → **10** (логотип identical to DS)
- **AI Slop Score**: A (unchanged)

### Boil-the-lake check
Усі 10 sidebars оновлено в одному pass — не залишилося frames з фейковим брендом. Cross-flow + frame labels — теж complete coverage.
