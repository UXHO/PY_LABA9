def calculate_statistics(participants):
    if not participants:
        print("Ошибка: словарь участников пуст.")
        return None, None, None

    scores = list(participants.values())
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    return min_score, max_score, avg_score


def get_above_average(participants, avg_score):
    return {name: score for name, score in participants.items() if score > avg_score}


partic = {
    "Иванов": 20,
    "Сидоров": 68,
    "Петров": 26,
    "Смирнов": 68,
}

# Добавление собственных данных
partic["Касимова"] = 100
partic["Дуров"] = 5

# Вычисление статистики
min_s, max_s, avg_s = calculate_statistics(partic)

print("Участники с баллом выше среднего:")
people_above_average = get_above_average(partic, avg_s)

for namee, scoree in people_above_average.items():
    print(f"{namee}: {scoree}")

print(f"\nМин балл: {min_s} (участники: {[name for name, score in partic.items() if score == min_s]})")
print(f"Макс балл: {max_s} (участники: {[name for name, score in partic.items() if score == max_s]})")
print(f"Средний балл: {avg_s:.2f}")
print(f"\nМин балл: {min_s}")
