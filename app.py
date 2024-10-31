from flask import Flask, render_template, request, redirect, url_for  # Импортируем нужные функции и классы из Flask

app = Flask(__name__)  # экземпляр приложения Flask


def add_to_file(word1: str, word2: str):
    with open("words.txt", "a", encoding="utf-8") as file:  # Открываем файл для добавления строк в кодировке UTF-8
        file.write(word1 + "-" + word2 + "\n")  # Записываем слова в формате "слово1-слово2" и перенос строки


def read_from_file():
    with open("words.txt", "r", encoding="utf-8") as file:  # Открываем файл для чтения в кодировке UTF-8
        lines = file.read().splitlines()  # Читаем строки и удаляем символы переноса строки
    words1, words2 = [], []  # Инициализируем списки для слов
    for line in lines:  # Проходимся по каждой строке файла
        word1, word2 = line.split("-")  # Разделяем строку по дефису на два слова
        words1.append(word1)  # Добавляем первое слово в список words1
        words2.append(word2)  # Добавляем второе слово в список words2
    return words1, words2  # Возвращаем оба списка

@app.route("/")  # Определяем маршрут для корневого URL

def home():
    return render_template("home.html", title="My dictionary")  # Отображаем шаблон home.html с заголовком


@app.route("/add_word", methods=["GET", "POST"])  # для добавления нового слова с поддержкой GET и POST
def add_word():
    if request.method == "POST":  # если метод запроса POST 
        word1 = request.form["word1"]  # Получаем слово1 из формы
        word2 = request.form["word2"]  # Получаем слово2 из формы
        add_to_file(word1, word2) 
        return redirect(url_for("home"))  # Перенаправляем пользователя на домашнюю страницу
    return render_template("add_word.html", title="Add a Word")  # Отображаем шаблон add_word.html для добавления слова


@app.route("/words_list")
def words_list():
    words1, words2 = read_from_file()  
    words = list(zip(words1, words2))  # zip группирует их в кортежи
    return render_template("words_list.html", words=words, title="Words List") 


if __name__ == "__main__":
    app.run(debug=True) 
