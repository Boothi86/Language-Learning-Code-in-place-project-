import tkinter as tk

# Extended list of basic Japanese words
word_data = [
    {"word": "ねこ", "pronunciation": "neko", "meaning": "cat", "emoji": "🐱"},
    {"word": "いぬ", "pronunciation": "inu", "meaning": "dog", "emoji": "🐶"},
    {"word": "やま", "pronunciation": "yama", "meaning": "mountain", "emoji": "⛰️"},
    {"word": "かわ", "pronunciation": "kawa", "meaning": "river", "emoji": "🌊"},
    {"word": "はな", "pronunciation": "hana", "meaning": "flower", "emoji": "🌸"},
    {"word": "みず", "pronunciation": "mizu", "meaning": "water", "emoji": "💧"},
    {"word": "そら", "pronunciation": "sora", "meaning": "sky", "emoji": "☁️"},
    {"word": "ひと", "pronunciation": "hito", "meaning": "person", "emoji": "🧍"},
    {"word": "たまご", "pronunciation": "tamago", "meaning": "egg", "emoji": "🥚"},
    {"word": "やさい", "pronunciation": "yasai", "meaning": "vegetable", "emoji": "🥦"},
    {"word": "くだもの", "pronunciation": "kudamono", "meaning": "fruit", "emoji": "🍎"},
    {"word": "くるま", "pronunciation": "kuruma", "meaning": "car", "emoji": "🚗"},
]

class WordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Japanese Word Viewer")

        self.main_frame = tk.Frame(master)
        self.detail_frame = tk.Frame(master)

        self.current_index = 0

        self.build_home_page()

    def build_home_page(self):
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Basic Japanese Words", font=("Helvetica", 20)).pack(pady=10)
        grid = tk.Frame(self.main_frame)
        grid.pack()

        for i, word in enumerate(word_data):
            btn = tk.Button(grid,
                            text=f"{word['emoji']}\n{word['word']}\n({word['pronunciation']})",
                            font=("Helvetica", 14),
                            width=10, height=4,
                            command=lambda idx=i: self.show_detail(idx))
            btn.grid(row=i // 4, column=i % 4, padx=10, pady=10)

    def show_detail(self, index):
        self.current_index = index
        self.main_frame.pack_forget()
        self.detail_frame.pack()
        self.display_word()

    def display_word(self):
        for widget in self.detail_frame.winfo_children():
            widget.destroy()

        word = word_data[self.current_index]

        tk.Label(self.detail_frame, text=word['emoji'], font=("Helvetica", 80)).pack(pady=10)
        tk.Label(self.detail_frame, text=word['word'], font=("Helvetica", 36)).pack()
        tk.Label(self.detail_frame, text=f"Pronunciation: {word['pronunciation']}", font=("Helvetica", 18)).pack()
        tk.Label(self.detail_frame, text=f"Meaning: {word['meaning']}", font=("Helvetica", 18)).pack()

        nav = tk.Frame(self.detail_frame)
        nav.pack(pady=20)

        tk.Button(nav, text="Previous", command=self.show_previous).pack(side="left", padx=20)
        tk.Button(nav, text="Next", command=self.show_next).pack(side="right", padx=20)
        tk.Button(self.detail_frame, text="Back to Menu", command=self.back_to_menu).pack(pady=10)

    def show_next(self):
        self.current_index = (self.current_index + 1) % len(word_data)
        self.display_word()

    def show_previous(self):
        self.current_index = (self.current_index - 1) % len(word_data)
        self.display_word()

    def back_to_menu(self):
        self.detail_frame.pack_forget()
        self.main_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordApp(root)
    root.mainloop()

