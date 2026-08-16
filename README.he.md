<div dir="rtl">

# 📱 Telegram Keep-Alive

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/daniel-malka-148/telegram-keepalive/keepalive.yml)](https://github.com/daniel-malka-148/telegram-keepalive/actions)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com)

> שומר על חשבון הטלגרם פעיל על ידי שליחת הודעה קצרה וחלקה ל-Saved Messages.

הפרויקט הזה הוא אוטומציה פשוטה מבוססת GitHub Actions שמטרתה לשמור על חשבון טלגרם פעיל לאורך זמן. הוא תוכנן להיות קל להבנה, קל להרצה, וקל להתאמה לצרכים האישיים שלך.

---

## ✨ למה הפרויקט הזה שימושי

- רץ בחינם על GitHub Actions
- מופעל אוטומטית אחרי ההגדרה הראשונית
- קל להבנה ולתחזוקה
- קל לשכפל ולהתאים אישית
- תלויות מינימליות וזרימת עבודה פשוטה

---

## ⚠️ לפני שמתחילים

הפרויקט משתמש ב-Session String ובפרטי API של טלגרם. ערכים אלה רגישים וצריך להתייחס אליהם כמו לסיסמאות.

- לעולם אל להעלות ל-GitHub את קובץ `session.txt` או כל קובץ סשן של טלגרם
- שמור סודות רק ב-GitHub Secrets
- אל תשתף את ה-API HASH או את ה-Session String עם אף אחד
- השתמש בפרויקט על אחריותך בלבד
- טלגרם עשויה להגביל או להשבית חשבון אם היא מזהה התנהגות אוטומטית חריגה

---

## 🧭 רשימת בדיקה מהירה

השתמש בזרימה הזו לפי הסדר:

1. הורד או שכפל את הריפו
2. התקן את התלות של Python
3. צור Session String מקומי
4. הוסף את פרטי ה-API ואת ה-Session String ב-GitHub Secrets
5. הפעל את ה-workflow פעם אחת כדי לבדוק
6. תן ל-GitHub Actions להמשיך לבד אחר כך

---

## 🧠 איך זה עובד

```text
לוח זמנים ב-GitHub
    ↓
GitHub Actions
    ↓
keepalive.py
    ↓
Telegram API
    ↓
Saved Messages
```

1. GitHub Actions מפעיל את ה-workflow לפי לוח זמנים או ידנית.
2. ה-workflow מתקין את החבילות הנדרשות.
3. הסקריפט מתחבר לטלגרם בעזרת API ID, API HASH ו-Session String.
4. הוא מחכה מספר שניות אקראיות ואז שולח הודעה ל-Saved Messages.
5. החשבון נשאר פעיל יותר ונראה ככזה.

---

## 🚀 תכונות

- ✅ אוטומציה בחינם ב-GitHub Actions
- ✅ לוח זמנים שבועי או מותאם אישית
- ✅ עיכוב אקראי לפני שליחה
- ✅ בחירה אקראית של הודעה מרשימת הודעות מובנות
- ✅ תמיכה בהודעה מותאמת דרך secret
- ✅ מבנה קטן, פשוט וקל להתאמה

---

## 📦 דרישות מוקדמות

לפני שמתחילים, וודא שיש לך:

1. חשבון טלגרם
2. פרטי API מ-[my.telegram.org](https://my.telegram.org)
   - `api_id`
   - `api_hash`
3. Python 3.12+
4. חשבון GitHub

---

## 🛠 התחלה מהירה

### שלב 1: יצירת Session String

הרץ זאת פעם אחת במחשב המקומי:

```bash
pip install -r requirements.txt
python create_session.py
```

הסקריפט יבקש:

1. API ID
2. API HASH
3. מספר טלפון עם קידומת מדינה
4. קוד אימות מטלגרם
5. סיסמת 2FA אם היא מופעלת

בסוף, הוא יודפיס את ה-Session String וישמור אותו בקובץ `session.txt`.

> ה-Session String הוא סיסמה אמיתית. שמור אותו בסוד.

### שלב 2: שכפול או Fork של הריפו

```bash
git clone https://github.com/YOUR_USERNAME/telegram-keepalive.git
cd telegram-keepalive
```

### שלב 3: הוספת GitHub Secrets

עבור אל:

Settings → Secrets and variables → Actions → New repository secret

הוסף את הדברים הבאים:

| שם ה-secret | ערך |
|---|---|
| `API_ID` | ה-API ID של חשבון הטלגרם |
| `API_HASH` | ה-API HASH של חשבון הטלגרם |
| `SESSION_STRING` | ה-Session String שנוצר בשלב 1 |

ערכים אופציונליים:

| שם ה-secret | ערך |
|---|---|
| `KEEPALIVE_MESSAGE` | טקסט של הודעה או מספר הודעות מופרדות ב-`||` |
| `KEEPALIVE_MIN_DELAY_SECONDS` | עיכוב מינימלי, למשל `5` |
| `KEEPALIVE_MAX_DELAY_SECONDS` | עיכוב מקסימלי, למשל `60` |

### שלב 4: הפעלת ה-workflow

ה-workflow כבר מוגדר בקובץ `.github/workflows/keepalive.yml`.

אפשר גם:

- לחכות שהעבודה תרוץ לפי לוח זמנים, או
- להפעיל אותה ידנית דרך הכרטיסייה Actions

כדי לבדוק מהר:

1. פתח את הריפו ב-GitHub
2. עבור אל הכרטיסייה Actions
3. בחר Telegram Keep-Alive
4. לחץ Run workflow
5. בדוק את הלוגים אחרי כמה דקות

---

## 🎯 רעיונות להתאמה אישית

### הודעות אקראיות

אפשר להגדיר רשימת הודעות בעזרת `||`:

```bash
KEEPALIVE_MESSAGE="בודק אם הכול בסדר || עדיין חי || פינג שבועי || הכל בסדר פה"
```

אם ה-secret לא מוגדר, הסקריפט בוחר הודעה אקראית מרשימת ההודעות המובנות.

### לוח זמנים פחות צפוי

במקום להריץ כל שבוע באותו זמן, אפשר לשנות את הביטוי `cron` בקובץ `.github/workflows/keepalive.yml`.

דוגמה:

```yaml
- cron: "0 6,12,18 * * *"
```

זה יוצר דפוס טבעי יותר מאשר לוח זמנים קשיח אחד.

### עיכוב אקראי

אפשר לשנות את זמני ההשהיה:

```bash
KEEPALIVE_MIN_DELAY_SECONDS=5
KEEPALIVE_MAX_DELAY_SECONDS=60
```

כך כל הפעלה נראית פחות כמו תהליך בוטי.

---

## 📁 מבנה הפרויקט

```text
telegram-keepalive/
├── .github/
│   └── workflows/
│       └── keepalive.yml
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README.he.md
├── SECURITY.md
├── .env.example
├── create_session.py
├── keepalive.py
├── requirements.txt
├── session.txt
└── telegram-keepalive/
    └── keepalive.py
```

---

## ❓ שאלות נפוצות

### האם זה באמת חינמי?
כן. GitHub Actions מספיק לרוב תהליכי עבודה קלים כאלה.

### האם זה בטוח?
הסקריפט שולח הודעה אמיתית רק ל-Saved Messages הפרטי שלך. הוא לא בוט ספאם ולא פונה למשתמשים אקראיים. עם זאת, טלגרם עדיין עשויה לזהות דפוסי אוטומציה חריגים.

### מה קורה אם ה-workflow נכשל?
פתח את הריצה שנכשלה בכרטיסייה Actions וצפה בלוגים. הסיבה הנפוצה היא Session String לא תקין או Secret חסר.

### האם אפשר לשנות את לוח הזמנים?
כן. ערוך את הביטוי `cron` בקובץ `.github/workflows/keepalive.yml`.

### האם אפשר לשנות את רשימת ההודעות?
כן. השתמש ב-secret `KEEPALIVE_MESSAGE` עם מספר ערכים מופרדים ב-`||`.

---

## 🔐 אבטחה

הפרויקט שומר סודות מחוץ לקוד המקור ומצפה שהם יישמרו ב-GitHub Secrets.

עקרונות מומלצים:

- אל תשלח את ה-Session String ל-GitHub
- שמור `.env` פרטי מקומי בסוד
- אל תציג סודות בלוגים או ב-issues
- אם יש חשש שה-session נחשף, צור אחד חדש

ראה את [SECURITY.md](SECURITY.md) למדיניות אבטחה.

---

## ⚠️ כתב ויתור

השתמש בפרויקט זה על אחריותך בלבד.

- הוא מסתמך על הספרייה Telethon כדי לתקשר עם ה-API של טלגרם
- פעילות אוטומטית בחשבון עלולה להפר תנאי שימוש של טלגרם או לגרום להגבלות
- הכותב אינו אחראי לכל תוצאה הנובעת משימוש בתוכנה זו
- הפרויקט מסופק כמות שהוא, ללא כל אחריות

---

## 📄 רישיון

הפרויקט מופץ תחת רישיון MIT. ראה את [LICENSE](LICENSE) לפרטים.

---

## 🌐 שפות

- [English](README.md)
- [עברית](README.he.md)

---

<div align="center">
  נוצר באהבה ❤️ על ידי <a href="https://github.com/daniel-malka-148">דניאל מלכא</a>
</div>

</div>
