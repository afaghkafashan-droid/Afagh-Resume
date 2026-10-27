# 🐍 سایت رزومه با پایتون — Cloudflare Pages + GitHub

سایت رزومه‌ای که با **پایتون** ساخته می‌شود: محتوا در فایل پایتون است، قالب **Jinja2**، و `build.py` فایل نهایی HTML را تولید می‌کند.

## ساختار پروژه

```
resume-site-py/
├── resume_data.py        ← تمام محتوای رزومه (اینجا را ویرایش کنید!)
├── build.py              ← اسکریپت ساخت سایت
├── templates/
│   └── index.html        ← قالب Jinja2 (ظاهر سایت)
├── requirements.txt      ← وابستگی‌ها (فقط Jinja2)
└── output/               ← خروجی ساخت (index.html) — از گیت رد می‌شود
```

## ۱) شخصی‌سازی

فایل `resume_data.py` را باز کنید و نام، عنوان شغلی، تجربه‌ها، پروژه‌ها و مهارت‌های خودتان را جایگزین کنید.

## ۲) ساخت و پیش‌نمایش محلی

```bash
pip install -r requirements.txt
python build.py                 # سایت در output/index.html ساخته می‌شود
python -m http.server -d output # پیش‌نمایش در http://localhost:8000
```

## ۳) گذاشتن روی GitHub

```bash
git init
git add .
git commit -m "Resume site in Python"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

یا با GitHub CLI:

```bash
gh repo create REPO --public --source=. --push
```

## ۴) استقرار روی Cloudflare Pages

1. [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. اتصال GitHub و انتخاب ریپو
3. تنظیمات بیلد:

   | تنظیم | مقدار |
   |---|---|
   | Framework preset | **None** |
   | Build command | `pip install -r requirements.txt && python build.py` |
   | Build output directory | `output` |

4. **Save and Deploy** — سایت با آدرس `https://REPO.pages.dev` بالا می‌آید.

هر پوش به `main` = استقرار خودکار. ✅

## ۵) روش جایگزین: استقرار با Wrangler (بدون اتصال Git)

```bash
pip install -r requirements.txt
python build.py
npx wrangler pages deploy output --project-name=my-resume
```

## ۶) دامنه‌ی اختیاری

در پروژه‌ی Pages → تب **Custom domains** → **Set up a custom domain**.

---

💡 **فارسی/RTL:** در `templates/index.html` تگ `<html lang="en">` را به `<html lang="fa" dir="rtl">` تغییر دهید و متن‌های `resume_data.py` را فارسی کنید.
