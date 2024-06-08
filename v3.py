import tkinter as tk
class AlphabetSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alphabet Selector App")
        self.alphabet = list("AEIOUBCDGHLMNRSTFPKVWXYZ")
        self.current_index = 0
        self.sentence = ""
        self.alphabet_frame = tk.Frame(root)
        self.alphabet_frame.pack(pady=20)
        self.letter_labels = []
        for letter in self.alphabet:
            label = tk.Label(self.alphabet_frame, text=letter, font=("Helvetica", 24), width=2, fg="black")
            label.pack(side=tk.LEFT, padx=2)
            self.letter_labels.append(label)
        self.highlight_letter()
        self.sentence_label = tk.Label(root, text="Sentence: ", font=("Helvetica", 24))
        self.sentence_label.pack(pady=20)
        self.backspace_button = tk.Button(root, text="Backspace", command=self.backspace)
        self.backspace_button.pack(side=tk.LEFT, padx=10)
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_sentence)
        self.clear_button.pack(side=tk.RIGHT, padx=10)
        self.root.bind("<Right>", self.next_letter)
        self.root.bind("<Left>", self.previous_letter)
        self.root.bind("<Return>", self.add_letter)
        self.root.bind("<space>", self.add_space)
        self.root.bind("<BackSpace>", self.backspace)
    def highlight_letter(self):
             for label in self.letter_labels:
            label.config(bg="SystemButtonFace")
        self.letter_labels[self.current_index].config(bg="yellow")
    def update_sentence_label(self):
        self.sentence_label.config(text=f"Sentence: {self.sentence}")
    def add_letter(self, event=None):
        current_letter = self.alphabet[self.current_index]
        self.sentence += current_letter
        self.update_sentence_label()
    def add_space(self, event=None):
        self.sentence += " "
        self.update_sentence_label()
