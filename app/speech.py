import wave

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


def main():
    file_name = "audio.wav"
    duration = 5

    record_audio(file_name, duration)

    text = recognize_speech(file_name)

    print("You said:", text)


if __name__ == '__main__':
    main()
