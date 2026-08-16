<div dir="rtl">

# 📱 Telegram Keep-Alive

[![סטטוס Workflow](https://img.shields.io/github/actions/workflow/status/daniel-malka-148/telegram-keepalive/keepalive.yml)](https://github.com/daniel-malka-148/telegram-keepalive/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![רישיון MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> שומר על חשבון הטלגרם פעיל על ידי שליחת הודעה קצרה וחלקה ל-Saved Messages.

הפרויקט הזה הוא אוטומציה פשוטה מבוססת GitHub Actions שמטרתה לשמור על חשבון טלגרם פעיל לאורך זמן. הוא תוכנן להיות קל להבנה, קל להרצה, וקל להתאמה לצרכים האישיים שלך.

---

## ⚡ איך זה עובד

```
לוח זמנים ב-GitHub ──▶ GitHub Actions ──▶ keepalive.py ──▶ Saved Messages בטלגרם
```

1. GitHub Actions מריץ את ה-workflow **כל יום ראשון בשעה 10:00 UTC** (או ידנית).
2. הסקריפט מתחבר לטלגרם עם הפרטים שלך.
3. הוא שולח הודעה קצרה ל-**Saved Messages** שלך.
4. החשבון נשאר פעיל — אין יותר סיכון למחיקה.

---

## 🚀 התקנה

### 1. יצירת Session String

הרץ פעם אחת במחשב שלך:

```bash
pip install -r requirements.txt
python create_session.py
```

הסקריפט יבקש את פרטי ה-API שלך (מ-[my.telegram.org](https://my.telegram.org)), מספר טלפון וקוד אימות. הוא שומר את ה-Session String בקובץ `session.txt`.

> ⚠️ **ה-Session String הוא סיסמה לחשבון שלך. לעולם אל תשתף אותו ואל תעלה אותו ל-GitHub.**

### 2. הוספת GitHub Secrets

בריפו שלך, עבור אל **Settings → Secrets and variables → Actions** והוסף:

| Secret | תיאור |
|---|---|
| `API_ID` | ה-API ID של טלגרם |
| `API_HASH` | ה-API HASH של טלגרם |
| `SESSION_STRING` | ה-Session String משלב 1 |

### 3. הפעלת ה-workflow

הפעל אותו ידנית פעם אחת כדי לבדוק:

1. פתח את הטאב **Actions**
2. בחר **Telegram Keep-Alive**
3. לחץ **Run workflow** → **Run workflow**
4. בדוק את הלוגים — זה אמור להסתיים בדקה ✅

מעכשיו זה רץ אוטומטית כל יום ראשון.

---

## 🎨 התאמה אישית

כל ההגדרות אופציונליות.

| Secret | מה זה עושה | דוגמה |
|---|---|---|
| `KEEPALIVE_MESSAGE` | הודעה מותאמת. אפשר כמה עם `\|\|`. | `"עוד חי \|\| פינג שבועי"` |
| `KEEPALIVE_MIN_DELAY_SECONDS` | עיכוב אקראי מינימלי | `5` |
| `KEEPALIVE_MAX_DELAY_SECONDS` | עיכוב אקראי מקסימלי | `60` |

**לוח זמנים:** ערוך את שורת ה-`cron` בקובץ [`.github/workflows/keepalive.yml`](.github/workflows/keepalive.yml).

---

## 📁 מבנה

```
├── .github/workflows/keepalive.yml   # ה-workflow של GitHub Actions
├── keepalive.py                      # הסקריפט הראשי
├── create_session.py                 # יצירת Session String (פעם אחת)
├── requirements.txt                  # תלויות
├── .gitignore                        # מגן על session.txt 🔒
└── LICENSE                           # MIT
```

---

## ❓ שאלות נפוצות

**האם זה חינמי?** כן — המכסה החינמית של GitHub Actions מספיקה בקלות.

**האם זה בטוח?** הוא שולח הודעה אחת בשבוע ל-Saved Messages שלך. עם זאת, פעילות אוטומטית עלולה להפר את תנאי השימוש של טלגרם — השתמש על אחריותך.

**ה-workflow נכשל. מה לעשות?** פתח את הלוגים בריצה שנכשלה. הסיבה הנפוצה: `SESSION_STRING` שגוי או Secrets חסרים.

---

## ⚠️ כתב ויתור

הפרויקט משתמש ב-[Telethon](https://github.com/LonamiWebs/Telethon) ומבצע פעילות אוטומטית בחשבון. טלגרם עלולה להגביל חשבונות שמראים התנהגות אוטומטית. **השתמש על אחריותך בלבד.**

---

## 📄 רישיון

MIT — ראה [LICENSE](LICENSE).

---

## 🌐 שפות

- [English](README.md) · [עברית](README.he.md)

<div align="center">נוצר באהבה ❤️ על ידי <a href="https://github.com/daniel-malka-148">דניאל מלכא</a></div>

</div>