def find_key_words(text):
    # جدا کردن جملات از هم
    sentences = text.split('.')
    
    # ذخیره‌سازی کلمات شاخص به همراه شماره آنها
    key_words = []

    # شمارش کلمات
    word_index = 1

    # پردازش هر جمله
    for sentence in sentences:
        # حذف فضای خالی در ابتدا و انتهای جمله و جدا کردن کلمات
        words = sentence.strip().split()

        # پردازش هر کلمه در جمله
        for i, word in enumerate(words):
            # حذف نشانه‌های ویرگول و نقطه از انتهای کلمه
            word = word.rstrip(",.")
            
            # بررسی شرایط کلمه شاخص
            if (word[0].isupper() and not word.isnumeric() and i != 0):
                key_words.append(f"{word_index}:{word}")

            # افزایش شمارشگر کلمات
            word_index += 1

    # چاپ خروجی
    if key_words:
        for key_word in key_words:
            print(key_word)
    else:
        print("None")

# ورودی نمونه
text = input().strip()

# اجرای برنامه
find_key_words(text)
