# import tkinter as tk
# from PIL import Image, ImageTk, ImageSequence
# import os
#
# # Dictionary of Hiragana characters with English pronunciation (in order)
# hiragana_data = {
#     "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
#     "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
#     "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
#     "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
#     "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
#     "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
#     "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
#     "や": "ya", "ゆ": "yu", "よ": "yo",
#     "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
#     "わ": "wa", "を": "wo", "ん": "n",
#     "ゐ": "wi (archaic)", "ゑ": "we (archaic)"
# }
#
# GIF_FOLDER = "/Users/shwethambarivenkatesh/Downloads/Hiragana"
#
# class HiraganaViewer:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Hiragana Stroke Order Viewer")
#
#         self.label_char = tk.Label(master, font=("Helvetica", 32))
#         self.label_char.pack(pady=10)
#
#         self.label_pron = tk.Label(master, font=("Helvetica", 18))
#         self.label_pron.pack()
#
#         self.canvas = tk.Label(master)
#         self.canvas.pack()
#
#         self.next_button = tk.Button(master, text="Next", command=self.show_next)
#         self.next_button.pack(pady=10)
#
#         # Match files to Hiragana characters in correct order
#         all_files = os.listdir(GIF_FOLDER)
#         self.gif_files = []
#         for char in hiragana_data:
#             for f in all_files:
#                 if f.endswith(".gif") and f"Hiragana_{char}_" in f:
#                     self.gif_files.append((char, f))
#                     break
#
#         self.index = 0
#         self.frames = []
#         self.current_frame = 0
#         self.after_id = None
#
#         self.show_next()
#
#     def show_next(self):
#         if self.after_id:
#             self.master.after_cancel(self.after_id)
#
#         if self.index >= len(self.gif_files):
#             self.index = 0
#
#         char, gif_file = self.gif_files[self.index]
#         pron = hiragana_data.get(char, "(unknown)")
#
#         self.label_char.config(text=f"Hiragana: {char}")
#         self.label_pron.config(text=f"Pronunciation: {pron}")
#
#         gif_path = os.path.join(GIF_FOLDER, gif_file)
#         self.gif = Image.open(gif_path)
#         self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
#         self.current_frame = 0
#         self.update_gif()
#
#         self.index += 1
#
#     def update_gif(self):
#         self.canvas.config(image=self.frames[self.current_frame])
#         self.current_frame = (self.current_frame + 1) % len(self.frames)
#         self.after_id = self.master.after(100, self.update_gif)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HiraganaViewer(root)
#     root.mainloop()


import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

# Hiragana dictionary in correct order
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

GIF_FOLDER = "/Users/shwethambarivenkatesh/Downloads/Hiragana"  # Replace with your actual path

class HiraganaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hiragana Dashboard")

        self.hiragana_list = list(hiragana_data.keys())
        self.gif_files = self.load_gif_files()

        self.index = 0
        self.frames = []
        self.current_frame = 0
        self.after_id = None

        self.main_frame = tk.Frame(master)
        self.main_frame.pack()

        self.detail_frame = tk.Frame(master)

        self.build_home_page()

    def load_gif_files(self):
        files = os.listdir(GIF_FOLDER)
        gif_files = []
        for char in self.hiragana_list:
            for f in files:
                if f.endswith(".gif") and f"Hiragana_{char}_" in f:
                    gif_files.append((char, f))
                    break
        return gif_files

    def build_home_page(self):
        tk.Label(self.main_frame, text="Select a Hiragana", font=("Helvetica", 20)).pack(pady=10)
        grid = tk.Frame(self.main_frame)
        grid.pack()

        for i, char in enumerate(self.hiragana_list):
            btn = tk.Button(grid, text=f"{char}\n({hiragana_data[char]})", width=6, height=3,
                            command=lambda idx=i: self.show_hiragana(idx))
            btn.grid(row=i // 8, column=i % 8, padx=5, pady=5)

    def show_hiragana(self, index):
        self.index = index
        self.main_frame.pack_forget()
        self.detail_frame.pack()

        self.label_char = tk.Label(self.detail_frame, font=("Helvetica", 32))
        self.label_char.pack(pady=10)

        self.label_pron = tk.Label(self.detail_frame, font=("Helvetica", 18))
        self.label_pron.pack()

        self.canvas = tk.Label(self.detail_frame)
        self.canvas.pack()

        nav = tk.Frame(self.detail_frame)
        nav.pack(pady=10)

        self.prev_button = tk.Button(nav, text="Previous", command=self.show_previous)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = tk.Button(nav, text="Next", command=self.show_next)
        self.next_button.pack(side="right", padx=10)

        self.back_button = tk.Button(self.detail_frame, text="Back to Hiragana Menu", command=self.back_to_menu)
        self.back_button.pack(pady=5)

        self.display_current_hiragana()

    def display_current_hiragana(self):
        if self.after_id:
            self.master.after_cancel(self.after_id)

        char, gif_file = self.gif_files[self.index]
        pron = hiragana_data.get(char, "(unknown)")
        self.label_char.config(text=f"Hiragana: {char}")
        self.label_pron.config(text=f"Pronunciation: {pron}")

        gif_path = os.path.join(GIF_FOLDER, gif_file)
        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.current_frame = 0
        self.update_gif()

    def show_next(self):
        self.index = (self.index + 1) % len(self.gif_files)
        self.display_current_hiragana()

    def show_previous(self):
        self.index = (self.index - 1) % len(self.gif_files)
        self.display_current_hiragana()

    def update_gif(self):
        self.canvas.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after_id = self.master.after(100, self.update_gif)

    def back_to_menu(self):
        if self.after_id:
            self.master.after_cancel(self.after_id)
        self.detail_frame.pack_forget()
        self.main_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = HiraganaApp(root)
    root.mainloop()
