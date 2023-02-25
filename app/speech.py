import wave

import librosa
import numpy as np
import pyaudio
import speech_recognition as sr


def record_audio(file_name, duration):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = duration

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Recording...")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def recognize_speech(file_name):
    r = sr.Recognizer()

    with sr.AudioFile(file_name) as source:
        audio_data = r.record(source)

    text = r.recognize_google(audio_data, language='en-US')

    return text


def detect_errors(filename):
    # загружаем аудиофайл и извлекаем характеристики
    y, sr = librosa.load(filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    # вычисляем среднее значение для каждой фичи по времени
    means = np.mean(mfcc, axis=1)
    # находим разности между соседними фичами
    diffs = np.diff(means)
    # находим индексы, где разность превышает пороговое значение
    errors = np.where(diffs > 1.5)[0] + 1
    return errors

def generate_comments(errors):
    comments = []
    for i, error in enumerate(errors):
        comment = f"Ошибка {i+1}: "
        if error < 0:
            comment += "нет ошибок"
        else:
            comment += f"Ошибка в слове '{words[error]}'"
            comment += f", звук '{sounds[error]}' не произнесен правильно."
            comment += " Попробуйте произносить звук более ясно и отчетливо."
        comments.append(comment)
    return comments


def main():
    file_name = "audio.wav"
    duration = 5

    record_audio(file_name, duration)

    text = recognize_speech(file_name)
    errors = detect_errors(file_name)
    print("You said:", text)
    print("errors:", errors)


if __name__ == '__main__':
    main()
