# 📊 Professional Portfolio QR Generator

An interactive, AI-augmented web application built with **Streamlit** and **Pillow (PIL)** that generates high-resolution, professionally framed, and labeled business QR codes on the fly. 

Designed specifically for enterprise networking, startup showcases, and tech conventions.

## 🚀 Live Application
👉 **[Launch the Live App on Streamlit Cloud]([https://generatedqrcode-o4c9u7iprbc9bzkqrxqu4j.streamlit.app/])**  

---

## 🛠️ Core Engineering & Layout Architecture

The script handles responsive input gathering, image matrix transformations, and precise typographical rendering entirely in-memory:

* **High-Density Matrix Generation:** Configured with `qrcode.QRCode (Version 4, Error Correction Level M)` ensuring clean, reliable smartphone scanning across a wide range of mobile hardware and lighting conditions.
* **Dynamic Canvas Extensions:** Leverages the **Pillow** image library to dynamically pad, size, and auto-center custom strings (such as professional credentials and titles) safely beneath the matrix boundary paths.
* **Linux Server Font Routing:** Implements automated native lookups across server system paths (`/usr/share/fonts/`) to load true vector typography scales (`LiberationSans`) natively on cloud infrastructure without requiring external network fetches.
* **Web Layout Framing System:** Injects targeted HTML/CSS blocks to bind standard inputs into a card style container layout, delivering a modern desktop interface.

---

## 📁 Repository Structure

```text
├── app.py              # Main Streamlit web application logic & layout engine
├── requirements.txt    # Production environment package declarations
└── README.md           # Technical documentation and ecosystem portfolio 
```

---

## 💻 Local Installation & Setup

If you want to run this application locally on your computer workstation:

1. **Clone the repository to your machine:**
   ```bash
   git clone https://github.com/Srinivasta
   cd YOUR_REPO_NAME
   ```

2. **Install all required production dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Boot up the Streamlit engine server:**
   ```bash
   streamlit run app.py
   ```

---

## 👤 Developer Profile

* **Developer:** Appala Srinivas Tanakala
* **Role:** Data Scientist & AI / FinTech Exploration Leader
* **GitHub Profile:** [://github.com](https://://github.com)
