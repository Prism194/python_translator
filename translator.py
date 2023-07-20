import tkinter as tk
from tkinter import messagebox, Text, BOTH
from PyDictionary import PyDictionary
import re

# PyDictionary를 사용하여 단어의 뜻을 찾습니다.
dictionary = PyDictionary()

def show_meaning(word):
    meanings = dictionary.meaning(word)
    if meanings:
        # 첫 번째 뜻만 표시합니다.
        messagebox.showinfo(word, list(meanings.values())[0][0])
    else:
        messagebox.showinfo(word, 'No meaning found')

def submit():
    # 이전에 번역된 단어들을 제거합니다.
    for label in word_labels:
        label.destroy()
    word_labels.clear()

    # 입력 필드의 내용을 가져옵니다.
    sentence = text_field.get("1.0", "end-1c")
    
    # 입력 필드를 비웁니다.
    text_field.delete("1.0", tk.END)

    # 특수 문자를 제외하고 문장을 토큰화합니다.
    words = re.findall(r'\b\w+\b', sentence)

    # 각 단어에 대해 라벨을 생성합니다.
    total_length = 0
    for word in words:
        label = tk.Label(root, text=word, fg='blue', cursor='hand2')
        label.bind('<Button-1>', lambda e, word=word: show_meaning(word))
        label.pack(side=tk.LEFT)
        
        # 단어 라벨의 길이를 추가합니다.
        total_length += len(word) + 1  # 공백을 포함합니다.
        
        # 창의 너비를 넘어서면 다음 행으로 넘어갑니다.
        if total_length > 50:  # 창의 너비에 따라 이 값을 조정해야 합니다.
            total_length = len(word) + 1
            label.pack(side=tk.LEFT)

        # 단어 라벨을 추적하는 리스트에 추가합니다.
        word_labels.append(label)

root = tk.Tk()

# 텍스트 필드를 생성합니다.
text_field = tk.Text(root, width=50, height=10)
text_field.pack(expand=True, fill=BOTH)

# 제출 버튼을 생성합니다.
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# 단어 라벨을 추적하는 리스트를 생성합니다.
word_labels = []

root.mainloop()
