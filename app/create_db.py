import sqlite3

conn = sqlite3.connect('speech_improvement.db')
c = conn.cursor()

# создаем таблицу exercises
c.execute('''CREATE TABLE exercises
             (id INTEGER PRIMARY KEY, title TEXT, description TEXT, audio_file TEXT, language TEXT)''')

# добавляем упражнения в таблицу exercises
exercises = [
    ('1', 'Exercise 1', 'Description of exercise 1', 'audio/exercise1.mp3', 'English'),
    ('2', 'Exercise 2', 'Description of exercise 2', 'audio/exercise2.mp3', 'Spanish'),
    ('3', 'Exercise 3', 'Description of exercise 3', 'audio/exercise3.mp3', 'French')
]
c.executemany('INSERT INTO exercises VALUES (?, ?, ?, ?, ?)', exercises)

# создаем таблицу user_responses
c.execute('''CREATE TABLE user_responses
             (id INTEGER PRIMARY KEY, exercise_id INTEGER, user_id INTEGER, response_file TEXT, response_time TIMESTAMP)''')

conn.commit()
conn.close()

