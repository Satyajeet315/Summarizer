import tkinter as tk
from tkinter import messagebox, scrolledtext
from transformers import pipeline
import threading

# Text Summarizer App using Hugging Face Transformers
class TextSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Text Summarizer")
        self.root.geometry("720x640")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        self.summarizer = None
        self.model_loaded = False

        # Title
        title_label = tk.Label(root, text="🧠 AI Text Summarizer", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#333")
        title_label.pack(pady=20)

        # Input Label
        tk.Label(root, text="Enter or paste your text below:", font=("Arial", 12), bg="#f4f4f4").pack(anchor="w", padx=20)

        # Input Textbox
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=12, font=("Arial", 11))
        self.input_text.pack(padx=20, pady=10, fill="both")

        # Summarize Button
        self.summarize_btn = tk.Button(
            root, text="⏬ Summarize Text", font=("Arial", 12, "bold"),
            bg="#007acc", fg="white", width=20, height=2, command=self.summarize_text
        )
        self.summarize_btn.pack(pady=10)

        # Output Label
        tk.Label(root, text="Generated Summary:", font=("Arial", 12), bg="#f4f4f4").pack(anchor="w", padx=20)

        # Output Textbox
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, font=("Arial", 11), fg="#1a1a1a")
        self.output_text.pack(padx=20, pady=10, fill="both")

        # Status Label
        self.status_label = tk.Label(root, text="🔄 Loading model, please wait...", font=("Arial", 10), bg="#f4f4f4", fg="gray")
        self.status_label.pack(pady=5)

        # Load model in background
        threading.Thread(target=self.load_model).start()

    def load_model(self):
        try:
            # Load Hugging Face summarization pipeline
            self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            self.model_loaded = True
            self.status_label.config(text="✅ Model Loaded Successfully", fg="green")
        except Exception as e:
            self.status_label.config(text="❌ Failed to load model.", fg="red")
            messagebox.showerror("Model Load Error", str(e))

    def summarize_text(self):
        if not self.model_loaded:
            messagebox.showinfo("Please Wait", "Model is still loading, please try again shortly.")
            return

        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Text", "Please enter some text to summarize.")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "🧠 Generating summary, please wait...\n")

        def summarize():
            try:
                summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, summary)
            except Exception as e:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, "❌ Error generating summary.")
                messagebox.showerror("Summarization Error", str(e))

        threading.Thread(target=summarize).start()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TextSummarizerApp(root)
    root.mainloop()
