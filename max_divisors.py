# تابعی که تعداد مقسوم علیه‌های یک عدد را محاسبه می‌کند
def count_divisors(number):
    count = 0  # شمارش مقسوم علیه ها
    for i in range(1, number + 1):  # چک کردن تمام اعداد تا خود عدد
        if number % i == 0:  # اگر عدد مقسوم علیه است
            count += 1
    return count

# متغیرهای مورد نیاز برای ذخیره کردن عددی که بیشترین مقسوم علیه‌ها را دارد
max_number = 0
max_divisors = 0

# خواندن 20 عدد از ورودی
for _ in range(20):
    number = int(input())
    
    # تعداد مقسوم علیه‌های این عدد را محاسبه می‌کنیم
    divisors_count = count_divisors(number)
    
    # بررسی اینکه آیا این عدد بیشترین تعداد مقسوم علیه‌ها را دارد
    if divisors_count > max_divisors or (divisors_count == max_divisors and number > max_number):
        max_divisors = divisors_count
        max_number = number

# چاپ عددی که بیشترین تعداد مقسوم علیه‌ها را دارد به همراه تعداد آنها
print(f"{max_number} {max_divisors}")


       
                

 
 
   
   