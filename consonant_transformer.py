# خواندن رشته از ورودی
input_str = input()

# حروف صدادار را مشخص می‌کنیم
vowels = 'aeiouAEIOU'

# متغیر برای ذخیره رشته خروجی
result_str = ''

# پردازش هر کاراکتر در رشته ورودی
for char in input_str:
    # اگر حرف صدادار نیست، آن را به رشته خروجی اضافه می‌کنیم
    if char not in vowels:
        result_str += '.' + char.lower()  # نقطه و حرف کوچک‌شده

# چاپ رشته خروجی
print(result_str)
