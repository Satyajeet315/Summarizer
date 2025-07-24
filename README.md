# 🧠 AI Text Summarizer GUI

This is a desktop application that uses Hugging Face Transformers to generate concise summaries from large blocks of text. The app features a user-friendly GUI built with Python’s Tkinter module and leverages the powerful `distilbart-cnn-12-6` model for summarization.

---

## 📌 Features

- **Intuitive GUI:** Built with Tkinter for easy interaction
- **Real-time Summarization:** Uses the Hugging Face `pipeline` for fast, accurate text summarization
- **Responsive Performance:** Loads the model in a background thread to keep the UI responsive
- **Clean Design:** Organized layout with scrollable text fields and status messaging

---

## 🖼️ GUI Preview

_(Include a screenshot here if available)_

---

## ⚙️ Installation

### 1. Clone the Repository

git clone https://github.com/yourusername/ai-text-summarizer-gui.git
cd ai-text-summarizer-gui



### 2. Create a Virtual Environment (Optional)


### 3. Install Dependencies


> Note: `tkinter` is included by default in most Python distributions. If not, install it separately based on your OS.

---

## 🚀 Run the App


- The GUI will launch with a loading status.
- Once the model is ready, you can input text and get a summary with just one click.

---

## 🧠 Under the Hood

- **Model:** `sshleifer/distilbart-cnn-12-6` via Hugging Face
- **Summarization pipeline:** `pipeline("summarization")`
- **Max summary length:** 130 tokens
- **Min summary length:** 30 tokens
- **No sampling (`do_sample=False`) for deterministic results**

---

## 📁 File Structure


---

## 📋 Example Use

**Input:**
> Hugging Face is a company that develops tools for building applications using artificial intelligence. It is best known for its Transformers library which provides thousands of pre-trained models...

**Generated Summary:**
> Hugging Face develops tools for AI applications and is best known for its Transformers library with thousands of models.

---

## 🧾 License

This project is released under the MIT License.

---

## 🙌 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- Python Community
