from flask import Flask, render_template, request, redirect, url_for  

# Flask - для создания экземпляра приложения
# render_template - для отображения HTML-шаблонов
# request - для обработки данных из форм
# redirect, url_for - для перенаправления пользователей и создания URL-адресов

app = Flask(__name__)  # Создаем экземпляр приложения Flask,  __name__ позволяет Flask определить местоположение приложения 

def add_to_file(word1: str, word2: str):
    with open("words.txt", "a") as file:  
        file.write(word1 + "-" + word2 + "\n")  

def read_from_file():
    with open("words.txt", "r") as file:  
        lines = file.read().splitlines() 
    words1, words2 = [], [] 
    for line in lines:  
        word1, word2 = line.split("-") 
        words1.append(word1)  
        words2.append(word2)  
    return words1, words2  

@app.route("/")  

def home():
    return render_template("home.html", title="My dictionary")  
    # Отображаем шаблон home.html и передаем заголовок страницы

@app.route("/add_word", methods=["GET", "POST"])  
# Определяем маршрут для добавления нового слова, поддерживающий методы GET и POST

def add_word():
    if request.method == "POST":  # Проверяем, является ли метод запроса POST
        word1 = request.form["word1"]  # Получаем слово1 из данных формы
        word2 = request.form["word2"]  # Получаем слово2 из данных формы
        add_to_file(word1, word2)  # Вызываем функцию add_to_file для сохранения слов
        return redirect(url_for("home"))  # Перенаправляем пользователя на домашнюю страницу
    return render_template("add_word.html", title="Add a Word")  
    # Если метод запроса GET, отображаем шаблон add_word.html и передаем заголовок

@app.route("/words_list")  # Определяем маршрут для отображения списка слов

def words_list():
    words1, words2 = read_from_file()  # Читаем слова из файла
    words = list(zip(words1, words2))  # Объединяем words1 и words2 в список кортежей
    return render_template("words_list.html", words=words, title="Words List")  
    # Отображаем шаблон words_list.html и передаем список слов и заголовок

if __name__ == "__main__":  # Проверяем, запущен ли скрипт напрямую
    app.run(debug=True)  # Запускаем Flask-приложение в режиме отладки для упрощения поиска ошибок
