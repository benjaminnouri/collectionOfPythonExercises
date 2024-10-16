class SchoolClass:
    def __init__(self, number_of_students, ages, heights, weights):
        self.number_of_students = number_of_students
        self.ages = ages
        self.heights = heights
        self.weights = weights

    def calculate_averages(self):
        average_age = sum(self.ages) / self.number_of_students
        average_height = sum(self.heights) / self.number_of_students
        average_weight = sum(self.weights) / self.number_of_students
        return average_age, average_height, average_weight

def main():
    # خواندن اطلاعات کلاس A
    num_students_A = int(input())
    ages_A = list(map(int, input().split()))
    heights_A = list(map(int, input().split()))
    weights_A = list(map(int, input().split()))
    
    # ایجاد شیء برای کلاس A
    class_A = SchoolClass(num_students_A, ages_A, heights_A, weights_A)
    
    # خواندن اطلاعات کلاس B
    num_students_B = int(input())
    ages_B = list(map(int, input().split()))
    heights_B = list(map(int, input().split()))
    weights_B = list(map(int, input().split()))
    
    # ایجاد شیء برای کلاس B
    class_B = SchoolClass(num_students_B, ages_B, heights_B, weights_B)
    
    # محاسبه و چاپ میانگین‌ها برای کلاس A
    avg_age_A, avg_height_A, avg_weight_A = class_A.calculate_averages()
    print(avg_age_A)
    print(avg_height_A)
    print(avg_weight_A)
    
    # محاسبه و چاپ میانگین‌ها برای کلاس B
    avg_age_B, avg_height_B, avg_weight_B = class_B.calculate_averages()
    print(avg_age_B)
    print(avg_height_B)
    print(avg_weight_B)
    
    # مقایسه قد و وزن و چاپ نتیجه
    if avg_height_A > avg_height_B:
        print("A")
    elif avg_height_A < avg_height_B:
        print("B")
    else:
        if avg_weight_A < avg_weight_B:
            print("A")
        elif avg_weight_A > avg_weight_B:
            print("B")
        else:
            print("Same")

if __name__ == "__main__":
    main()


