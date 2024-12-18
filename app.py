import re
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)#__name__ используется для определения корневого пути приложения, чтобы оно могло найти файлы, такие как шаблоны или статические файлы.
app.secret_key = "supersecretkey"  # для работы flash-сообщений

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
    return render_template("home.html", title="My Dictionary")

@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        word1 = request.form["word1"]
        word2 = request.form["word2"]

        # Проверка на то, что слова содержат только буквы 
        if not re.match("^[A-Za-zА-Яа-яЁё]+$", word1) or not re.match("^[A-Za-zА-Яа-яЁё]+$", word2):
            flash("Слова должны содержать только буквы. Пожалуйста, введите корректные слова.")
            return redirect(url_for("add_word"))  # Перенаправление для отображения сообщения об ошибке

        add_to_file(word1, word2)  # Функция для добавления в файл
        return redirect(url_for("home"))

    return render_template("add_word.html", title="Добавить слово")

@app.route("/words_list")
def words_list():
    words1, words2 = read_from_file()
    words = list(zip(words1, words2))
    return render_template("words_list.html", words=words, title="Words List")

app.run()







'''Основные свойства класса Flask:
config: Это объект конфигурации приложения, где можно задавать различные параметры, такие как DEBUG, SECRET_KEY, DATABASE_URI и другие настройки. Доступ к нему осуществляется как к словарю.

debug: Свойство, которое указывает, запущено ли приложение в режиме отладки. Режим отладки помогает выявлять ошибки и автоматически перезапускает сервер при изменениях в коде.

name: Имя модуля приложения, переданное при создании объекта Flask. Обычно это значение равно __name__.

static_folder: Путь к папке, в которой хранятся статические файлы (например, CSS, изображения, JavaScript). По умолчанию это static.

static_url_path: URL-префикс для доступа к статическим файлам. По умолчанию это /static.

template_folder: Путь к папке с шаблонами HTML. По умолчанию это templates.

url_map: Объект, содержащий карту всех маршрутов (routes) в приложении. Он показывает, какие URL-адреса связаны с какими представлениями.

view_functions: Словарь, где ключами являются имена маршрутов, а значениями — функции-представления, которые обрабатывают запросы на эти маршруты.

before_request_funcs, after_request_funcs, teardown_request_funcs: Списки функций, которые выполняются до или после обработки запроса, а также при завершении обработки.

blueprints: Словарь зарегистрированных Blueprints (модулей приложения), которые позволяют организовывать приложение на отдельные компоненты.

extensions: Словарь, содержащий расширения, подключённые к приложению.

instance_path: Путь к папке с инстансом приложения, где можно хранить файлы, специфичные для данной установки (например, конфигурационные файлы, которые не следует включать в контроль версий).

root_path: Корневой путь к модулю приложения, используемый для поиска ресурсов.

Примеры использования этих свойств:
app.config['DEBUG'] = True: Включение режима отладки.
app.static_folder: Можно изменить путь к папке со статическими файлами.
app.url_map: Позволяет увидеть все маршруты, зарегистрированные в приложении.

'''