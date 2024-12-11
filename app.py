from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список курсов (можно заменить на базу данных, если нужно)
courses = []

# Главная страница, отображающая все курсы
@app.route('/')
def index():
    return render_template('courses.html', courses=courses)  # Исправлено на 'courses.html'

# Страница для добавления нового курса
@app.route('/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        if course_name:
            courses.append(course_name)  # Добавляем курс в список
            return redirect(url_for('index'))  # Перенаправляем на главную страницу
    return render_template('add_courses.html')  # Исправлено на 'add_courses.html'

if __name__ == '__main__':
    app.run(debug=True)
