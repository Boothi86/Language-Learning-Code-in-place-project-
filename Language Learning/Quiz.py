import tkinter as tk
import random

# === Hiragana Data ===
hiragana_data = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo", "ん": "n",
    "ゐ": "wi (archaic)", "ゑ": "we (archaic)"
}

# === Basic Word Data ===
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

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Japanese Quiz")
        self.score = 0
        self.quiz_data = []
        self.current = 0

        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        self.intro_screen()

    def intro_screen(self):
        self.clear_frame()
        tk.Label(self.frame, text="Choose quiz type", font=("Helvetica", 18)).pack(pady=10)

        tk.Button(self.frame, text="Hiragana Only", width=20, command=lambda: self.setup_quiz("hiragana")).pack(pady=5)
        tk.Button(self.frame, text="Words Only", width=20, command=lambda: self.setup_quiz("words")).pack(pady=5)
        tk.Button(self.frame, text="Mixed (Both)", width=20, command=lambda: self.setup_quiz("mixed")).pack(pady=5)

    def setup_quiz(self, mode):
        self.mode = mode
        self.clear_frame()

        tk.Label(self.frame, text="How many questions?", font=("Helvetica", 14)).pack(pady=5)
        self.num_entry = tk.Entry(self.frame)
        self.num_entry.pack(pady=5)

        tk.Label(self.frame, text="Choose method:", font=("Helvetica", 14)).pack(pady=5)
        self.pick_var = tk.StringVar(value="random")
        tk.Radiobutton(self.frame, text="Random", variable=self.pick_var, value="random").pack()
        tk.Radiobutton(self.frame, text="First N", variable=self.pick_var, value="first").pack()

        tk.Button(self.frame, text="Start Quiz", command=self.start_quiz).pack(pady=10)

    def start_quiz(self):
        try:
            n = int(self.num_entry.get())
        except ValueError:
            return

        pick_type = self.pick_var.get()

        if self.mode == "hiragana":
            data = list(hiragana_data.items())
            selection = data[:n] if pick_type == "first" else random.sample(data, min(n, len(data)))
            self.quiz_data = [{"type": "hiragana", "char": k, "pron": v} for k, v in selection]

        elif self.mode == "words":
            selection = word_data[:n] if pick_type == "first" else random.sample(word_data, min(n, len(word_data)))
            self.quiz_data = [{"type": "word", **w} for w in selection]

        else:  # mixed
            hira_data = list(hiragana_data.items())
            if n == 1:
                # Pick one question from either hiragana or word randomly
                if random.choice(["hiragana", "word"]) == "hiragana":
                    mixed_h = random.sample(hira_data, 1)
                    mixed_w = []
                else:
                    mixed_h = []
                    mixed_w = random.sample(word_data, 1)
            else:
                half = n // 2
                word_count = n - half
                mixed_h = hira_data[:half] if pick_type == "first" else random.sample(hira_data, min(half, len(hira_data)))
                mixed_w = word_data[:word_count] if pick_type == "first" else random.sample(word_data, min(word_count, len(word_data)))

            self.quiz_data = [{"type": "hiragana", "char": k, "pron": v} for k, v in mixed_h] + \
                             [{"type": "word", **w} for w in mixed_w]
            random.shuffle(self.quiz_data)

        self.score = 0
        self.current = 0
        self.ask_question()

    def ask_question(self):
        self.clear_frame()
        if self.current >= len(self.quiz_data):
            self.show_result()
            return

        item = self.quiz_data[self.current]

        if item["type"] == "hiragana":
            tk.Label(self.frame, text=f"What is the pronunciation of '{item['char']}'?", font=("Helvetica", 18)).pack(pady=10)
        else:
            tk.Label(self.frame, text=f"What is the meaning of '{item['word']}'? {item['emoji']}", font=("Helvetica", 18)).pack(pady=10)

        self.answer = tk.Entry(self.frame)
        self.answer.pack(pady=10)
        tk.Button(self.frame, text="Submit", command=self.check_answer).pack()

    def check_answer(self):
        item = self.quiz_data[self.current]
        user_input = self.answer.get().strip().lower()
        correct = item["pron"] if item["type"] == "hiragana" else item["meaning"]

        self.clear_frame()

        if user_input == correct:
            self.score += 1
            feedback = "🎉 Awesome!"
        else:
            feedback = f"❌ Try again! Correct: {correct}"

        tk.Label(self.frame, text=feedback, font=("Helvetica", 16)).pack(pady=10)
        tk.Button(self.frame, text="Next", command=self.next_question).pack()

    def next_question(self):
        self.current += 1
        self.ask_question()

    def show_result(self):
        self.clear_frame()
        tk.Label(self.frame, text=f"✅ Quiz Complete! Score: {self.score} / {len(self.quiz_data)}", font=("Helvetica", 18)).pack(pady=10)
        tk.Button(self.frame, text="Try Again", command=self.intro_screen).pack()
        tk.Button(self.frame, text="Exit", command=self.master.quit).pack(pady=5)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
