def standardize_names():
    # دریافت تعداد افراد
    n = int(input().strip())

    # لیست‌ها برای ذخیره اسامی استاندارد شده بر اساس جنسیت
    males = []
    females = []

    # پردازش ورودی‌ها
    for _ in range(n):
        entry = input().strip()
        # تجزیه جنسیت، اسم و زبان
        gender, name, language = entry.split('.')
        
        # استانداردسازی اسم (حرف اول بزرگ و بقیه کوچک)
        standardized_name = name.capitalize()

        # ذخیره در لیست مربوط به جنسیت
        if gender == 'm':
            males.append((standardized_name, language))
        elif gender == 'f':
            females.append((standardized_name, language))

    # مرتب‌سازی اسامی بر اساس حروف الفبا
    males.sort(key=lambda x: x[0])
    females.sort(key=lambda x: x[0])

    # چاپ خروجی برای زنان
    for name, language in females:
        print(f"f {name} {language}")

    # چاپ خروجی برای مردان
    for name, language in males:
        print(f"m {name} {language}")

# اجرای برنامه
standardize_names()
