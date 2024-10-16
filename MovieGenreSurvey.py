def movie_survey():
    # تعریف ژانرها و تعداد علاقه‌مندی اولیه (همه صفر)
    genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]
    genre_count = {genre: 0 for genre in genres}

    # دریافت تعداد افراد
    n = int(input())

    # دریافت نام افراد و ژانرهای مورد علاقه‌ی آن‌ها
    for _ in range(n):
        # دریافت ورودی به صورت خطی
        data = input().split()
        
        # استخراج ژانرهای انتخابی و افزایش تعداد علاقه‌مندی‌ها
        person_genres = data[1:]
        for genre in person_genres:
            if genre in genre_count:
                genre_count[genre] += 1

    # مرتب‌سازی ژانرها بر اساس تعداد علاقه‌مندی (از بیشترین به کمترین)
    sorted_genres = sorted(genre_count.items(), key=lambda x: (-x[1], x[0]))

    # چاپ نتیجه
    for genre, count in sorted_genres:
        print(f"{genre} : {count}")

# اجرای برنامه
movie_survey()

