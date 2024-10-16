def translator():
    # دریافت تعداد کلمات در دیکشنری
    n = int(input().strip())
    
    # دیکشنری برای نگهداری ترجمه‌ها
    translations = {}

    # دریافت کلمات و ترجمه‌های آن‌ها و ذخیره در دیکشنری
    for _ in range(n):
        original, english, french, german = input().strip().split()
        translations[english] = original
        translations[french.replace(" ", "")] = original  # حذف فاصله در ترجمه فرانسوی
        translations[german] = original

    # دریافت جمله‌ای که نیاز به ترجمه دارد
    sentence = input().strip().split()

    # ترجمه جمله
    translated_sentence = []
    for word in sentence:
        if word in translations:
            translated_sentence.append(translations[word])
        else:
            translated_sentence.append(word)

    # چاپ جمله‌ی ترجمه شده
    print(" ".join(translated_sentence))

# اجرای برنامه
translator()
