# Munaf Studios 🖼️  
**The AI-powered product image studio in your browser**  

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/Munaf_Studios?style=for-the-badge)](https://github.com/aliii-codes/Munaf_Studios/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/Munaf_Studios?style=for-the-badge)](https://github.com/aliii-codes/Munaf_Studios/network)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/Munaf_Studios?style=for-the-badge)](https://github.com/aliii-codes/Munaf_Studios/issues)
[![License](https://img.shields.io/github/license/aliii-codes/Munaf_Studios?style=for-the-badge)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20.0%2B-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Pillow](https://img.shields.io/badge/Pillow-9.0.0%2B-green?style=for-the-badge&logo=python)](https://python-pillow.org/)

---

## 🚀 What's New in v2.0
- **Generative Fill**: Draw masks and generate content in specific areas ✨
- **Erase Elements**: Remove unwanted objects with AI inpainting 🧹
- **Enhanced Prompting**: AI-powered prompt enhancement for better results 💡
- **Improved Error Handling**: More robust API integrations and retries ⚙️

---

| **Feature**               | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **AI Image Generation**   | Create stunning product images from text prompts or uploaded photos 🖼️          |
| **Packshot Creator**      | Generate professional packshots with customizable backgrounds 📦                |
| **Shadow Studio**         | Add natural or drop shadows with adjustable intensity and blur 🌞               |
| **Lifestyle Generator**   | Place products in AI-generated lifestyle scenes 🏡                             |
| **Prompt Enhancer**       | Automatically refine text prompts for better image generation 💡                |
| **Generative Fill**       | Fill masked areas with AI-generated content ✨                                  |
| **Image Eraser**          | Remove unwanted elements from images with AI inpainting 🧹                      |

---

## 🛠️ Tech Stack
| Category       | Technologies                                                                 |
|----------------|------------------------------------------------------------------------------|
| **Framework**  | Streamlit, Gradio (demo)                                                    |
| **AI Services**| Bria AI API (Image Generation, Enhancement, Editing)                        |
| **Image Processing** | Pillow (PIL), NumPy, OpenCV (via Streamlit Canvas)                          |
| **Utilities**  | Python-Magic (file validation), Dotenv (env management)                    |

---

## 🏗️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/Munaf_Studios.git
   cd Munaf_Studios
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with:
   ```
   BRIA_API_KEY=your_bria_api_key_here
   ```

---

## 🚀 Usage
1. **Run the App**:
   ```bash
   streamlit run Munaf.Studios/main.py
   ```

2. **Access the Demo**:
   ```bash
   python Munaf.Studios/demo.py
   ```

---

## 📂 Project Structure
```
Munaf_Studios/
├── Components/                  # Reusable UI components
│   ├── image_preview.py
│   ├── sidebar.py
│   └── uploader.py
├── Services/                   # API service integrations
│   ├── __init__.py
│   ├── erase_foreground.py
│   ├── generative_fill.py
│   ├── hd_image_generation.py
│   ├── lifestyle_shot.py
│   ├── packshot.py
│   ├── prompt_enhancement.py
│   └── shadow.py
├── Workflows/                  # Multi-step workflows
│   └── generate_ad_set.py
├── Munaf.Studios/              # Main application
│   ├── demo.py                 # Gradio demo
│   └── main.py                 # Streamlit app
└── requirements.txt
```

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to branch: `git push origin feature/new-feature`
5. Open a pull request

---

## 🐞 Bug Reports & Feature Requests
[Open an issue](https://github.com/aliii-codes/Munaf_Studios/issues/new/choose)

---

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  
Built with ❤️ using Streamlit and Bria AI. Special thanks to the open-source community for the amazing tools that made this possible.
