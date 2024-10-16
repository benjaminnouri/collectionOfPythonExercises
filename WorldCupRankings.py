class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0

    @property
    def points(self):
        return self.wins * 3 + self.draws

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def __str__(self):
        return f"{self.name}  wins:{self.wins} , loses:{self.losses} , draws:{self.draws} , goal difference:{self.goal_difference} , points:{self.points}"

def process_results(results):
    teams = {
        "Iran": Team("Iran"),
        "Spain": Team("Spain"),
        "Portugal": Team("Portugal"),
        "Morocco": Team("Morocco"),
    }

    matches = [
        ("Iran", "Spain"),
        ("Iran", "Portugal"),
        ("Iran", "Morocco"),
        ("Spain", "Portugal"),
        ("Spain", "Morocco"),
        ("Portugal", "Morocco")
    ]

    for i, result in enumerate(results):
        team1, team2 = matches[i]
        score1, score2 = map(int, result.split('-'))

        # ثبت گل‌های زده و خورده
        teams[team1].goals_for += score1
        teams[team1].goals_against += score2
        teams[team2].goals_for += score2
        teams[team2].goals_against += score1

        # تعیین نتیجه بازی و به‌روز رسانی اطلاعات تیم‌ها
        if score1 > score2:
            teams[team1].wins += 1
            teams[team2].losses += 1
        elif score1 < score2:
            teams[team2].wins += 1
            teams[team1].losses += 1
        else:
            teams[team1].draws += 1
            teams[team2].draws += 1

    # مرتب‌سازی تیم‌ها بر اساس امتیاز، تعداد برد، و ترتیب الفبایی
    sorted_teams = sorted(
        teams.values(),
        key=lambda team: (-team.points, -team.wins, team.name)
    )

    # چاپ اطلاعات تیم‌ها
    for team in sorted_teams:
        print(team)

# دریافت نتایج بازی‌ها از کاربر
results = []
# print("Please enter the results of the 6 matches in the format 'score1-score2':")
for i in range(6):
    # result = input(f"Enter result for match {i+1}: ")
    result = input(f"")
    results.append(result)

# پردازش نتایج بازی‌ها
process_results(results)
