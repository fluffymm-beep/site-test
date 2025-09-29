# گالری پرامپت ChatGPT

یک پروژه‌ی ساده جنگو برای نمایش مجموعه‌ای از پرامپت‌های ساختاریافته به زبان فارسی.

## اجرای پروژه

1. ایجاد و فعال‌سازی محیط مجازی:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. نصب وابستگی‌ها:
   ```bash
   pip install -r requirements.txt
   ```
3. اجرای سرور توسعه:
   ```bash
   python manage.py runserver
   ```

سپس در مرورگر آدرس [http://localhost:8000](http://localhost:8000) را باز کنید تا گالری پرامپت‌ها را مشاهده کنید.

## ساختار

- `promptgallery/` تنظیمات اصلی پروژه
- `prompts/` اپلیکیشن حاوی نما و داده‌ها
- `templates/` قالب‌های HTML شامل طراحی مینیمال برای نمایش پرامپت‌ها

شما می‌توانید با ویرایش لیست `PROMPT_CATEGORIES` در فایل `prompts/views.py` دسته‌ها و پرامپت‌های جدید اضافه کنید.
