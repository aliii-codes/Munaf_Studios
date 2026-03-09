```markdown
# Munaf Studios

**A Streamlit-based tool for generating and enhancing product images with advanced AI features.**

Munaf Studios provides a user-friendly interface to create professional product images, including packshots, lifestyle shots, and enhanced visuals with shadows and generative fills.

## Features

- **Image Generation**: Generate high-quality product images from text or uploaded images.
- **Packshot Creation**: Create professional packshots with customizable backgrounds.
- **Shadow Addition**: Add natural or drop shadows to product images.
- **Lifestyle Shots**: Generate lifestyle context for products based on user descriptions.
- **Image Enhancement**: Enhance prompts and apply generative fills.
- **Image Preview & Download**: Preview generated images and download them directly.

## Tech Stack

- **Python**
- **Streamlit**
- **Pillow (PIL)**
- **Requests**
- **Python-Magic**

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Munaf_Studios.git
   cd Munaf_Studios
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload an Image**: Use the file uploader to upload a product image (optional).
2. **Configure Settings**: Adjust settings in the sidebar for packshots, shadows, lifestyle shots, and more.
3. **Generate Images**: Click the generate button to create images based on your configuration.
4. **Preview & Download**: Preview the generated images and download them using the provided buttons.

## Project Structure

```
Munaf_Studios/
├── Components/
│   ├── image_preview.py
│   ├── sidebar.py
│   └── uploader.py
├── Services/
│   ├── __init__.py
│   ├── lifestyle_shot.py
│   ├── shadow.py
│   ├── packshot.py
│   ├── prompt_enhancement.py
│   ├── generative_fill.py
│   ├── hd_image_generation.py
│   └── erase_foreground.py
├── app.py
└── requirements.txt
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
```
