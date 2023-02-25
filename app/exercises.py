import sqlite3

class Exercise:
    def __init__(self, name, description, level, audio_file, answer):
        self.name = name
        self.description = description
        self.level = level
        self.audio_file = audio_file
        self.answer = answer

    def add_to_db(self):
        conn = sqlite3.connect('speech_improvement.db')
        c = conn.cursor()
        c.execute("INSERT INTO exercises (name, description, level, audio_file, answer) VALUES (?, ?, ?, ?, ?)",
                  (self.name, self.description, self.level, self.audio_file, self.answer))
        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect('speech_improvement.db')
        c = conn.cursor()
        c.execute("DELETE FROM exercises WHERE name=?", (self.name,))
        conn.commit()
        conn.close()

    def update_in_db(self, name, description, level, audio_file, answer):
        conn = sqlite3.connect('speech_improvement.db')
        c = conn.cursor()
        c.execute("UPDATE exercises SET name=?, description=?, level=?, audio_file=?, answer=? WHERE name=?",
                  (name, description, level, audio_file, answer, self.name))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('speech_improvement.db')
        c = conn.cursor()
        c.execute("SELECT * FROM exercises")
        rows = c.fetchall()
        conn.close()
        return [cls(*row) for row in rows]
