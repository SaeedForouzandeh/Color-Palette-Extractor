# 🎨 Color Palette Extractor | استخراج پالت رنگی

> A bilingual GUI tool to extract dominant color palettes from any image using KMeans clustering. یک ابزار گرافیکی دو زبانه برای استخراج پالت‌های رنگی غالب از تصاویر با استفاده از الگوریتم KMeans.

---

## 🖼️ Features | ویژگی‌ها

* 🎨 Extract dominant colors using **KMeans clustering**
* 🖥️ Modern dark-themed UI with golden highlights
* 🌐 Bilingual support: **English & فارسی**
* 🖼️ Image preview and color palette display
* 🔢 Customizable number of colors (1–10)
* 🌈 Show color in RGB and HEX with contrast-aware text
* 🧠 Smart icon loading (`logo.ico` or `logo.png`)

---

## 🧪 Installation | نصب و راه‌اندازی

### 1. Clone the repo | کلون مخزن:

```bash
git clone https://github.com/SaeedForouzandeh/ColorPaletteExtractor.git
cd ColorPaletteExtractor
```

### 2. Install dependencies | نصب پیش‌نیازها:

```bash
pip install -r requirements.txt
```
یا 

### برای اجرای این برنامه نیاز به نصب کتابخانه‌های زیر دارید:
```bash
pip install opencv-python numpy scikit-learn pillow matplotlib
```

### 3. Run the app | اجرای برنامه:

```bash
python ColorPaletteExtractor.py
```

---

## 🗂️ File Structure | ساختار فایل‌ها

```bash
├── ColorPaletteExtractor.py               # فایل اصلی برنامه
├── logo.png              # لوگو
├── README.md             # مستندات
└── requirements.txt      # وابستگی‌ها
```

---

## 💡 How It Works | عملکرد برنامه

This app uses OpenCV to read the image, scikit-learn’s **KMeans** to cluster pixels, and displays the dominant colors in both RGB and HEX formats.

این ابزار با استفاده از OpenCV تصویر را بارگذاری کرده، پیکسل‌ها را با KMeans خوشه‌بندی می‌کند و رنگ‌های غالب را در قالب RGB و HEX نمایش می‌دهد.

---

## 🔤 Language Switch | تغییر زبان

Use the button on the top-right of the window to toggle between English and فارسی.

با دکمه بالای صفحه می‌توانید زبان رابط را بین انگلیسی و فارسی تغییر دهید.

---

## 🔧 Dependencies | وابستگی‌ها

```txt
tk
opencv-python
numpy
Pillow
scikit-learn
matplotlib

```

---

## 👤 Developer | توسعه‌دهنده

**Saeed Forouzandeh**
🔗 [GitHub Profile](https://github.com/SaeedForouzandeh)

---

## 📜 License | مجوز

This project is licensed under the **MIT License**. Feel free to use it.

این پروژه تحت مجوز MIT منتشر شده و استفاده از آن آزاد است.
