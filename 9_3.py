def create_dictionary():
    return {
        "привет": "hello",
        "мир": "world",
        "музыка": "music",
        "котенок": "kitten",
        "милый": "cute",
        "кексик": "cupcake",
        "спасибо": "thank you",
        "пожалуйста": "please",
        "да": "yes",
        "нет": "no",
        "и": "and",
    }


def translate_text(text, dictionary):
    words = text.split()  # Разделяем текст на слова
    translated_words = []

    for word in words:
        # Переводим слово или оставляем его в исходном виде
        translated_word = dictionary.get(word.lower(), word)
        translated_words.append(translated_word)

    return ' '.join(translated_words)  # Объединяем переведённые слова в строку


slovar = create_dictionary()
input_text = input("Введите строку текста для перевода: ")
translated_text = translate_text(input_text, slovar)
formatted_output = translated_text.capitalize() + '.'
print("Переведённый текст:", formatted_output)
