import struct
import wave

SPEED = 0.5 # Можно изменить скорость


def word_to_morze(text):
    morze = {'А': '.-', 'Б': '-...', 'В': '.--',
             'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.',
             'Ж': '...-', 'З': '--..', 'И': '..',
             'Й': '.---', 'К': '-.-', 'Л': '.-..',
             'М': '--', 'Н': '-.', 'О': '---',
             'П': '.--.', 'Р': '.-.', 'С': '...',
             'Т': '-', 'У': '..-', 'Ф': '..-.',
             'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
             'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.',
             'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
             'Ю': '..--', 'Я': '.-.-', ' ': ' ',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ', ': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}
    return "+".join([morze[letter] for letter in text.upper()])


dot = wave.open("dot.wav", mode="rb")
dash = wave.open("dash.wav", mode="rb")
result = wave.open("result.wav", mode="wb")
result.setparams(dot.getparams())

dot_frames = dot.getnframes()
dash_frames = dash.getnframes()
dot_data = struct.unpack("<" + str(dot_frames) + "i",
                         dot.readframes(dot_frames))
dash_data = struct.unpack("<" + str(dash_frames) + "i",
                          dash.readframes(dash_frames))

new_data = ()
for el in word_to_morze(input('Введите текст для шифровки')):
    if el == "-":
        new_data += dash_data
    elif el == ".":
        new_data += dot_data
    elif el == "+":
        new_data += tuple(0 for _ in range(50000))
    elif el == " ":
        new_data += tuple(0 for _ in range(100000))
new_data += tuple(0 for _ in range(1000))
newframes = struct.pack("<" + str(len(new_data)) + "i", *new_data)
result.setframerate(result.getframerate() * SPEED)
result.writeframes(newframes)
dash.close()
dot.close()
result.close()
