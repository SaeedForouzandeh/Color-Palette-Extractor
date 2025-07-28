#https://github.com/SaeedForouzandeh

import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageTk
import matplotlib.colors as mcolors
import os

class ColorPaletteExtractor:

    def __init__(self, root):
        self.root = root
        self.root.title("Color Palette Extractor")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a1a")
        
        try:
            # روش 1: برای ویندوز (فایل .ico)
            self.root.iconbitmap('logo.ico')
        
        # یا روش 2: برای همه پلتفرم‌ها (فایل .png)
            logo = Image.open("logo.png")
            logo = logo.resize((32, 32), Image.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(logo)
            self.root.tk.call('wm', 'iconphoto', self.root._w, self.logo_img)
        except Exception as e:
            print("خطا در بارگذاری لوگو:", e)
    

        # تنظیمات زبان
        self.language = "english"  # پیش‌فرض انگلیسی
        self.texts = {
            "english": {
                "title": "Color Palette Extractor",
                "select_image": "Select Image",
                "no_image": "No image selected",
                "color_count": "Number of colors:",
                "extract": "Extract Palette",
                "status_ready": "Ready",
                "status_success": "Image loaded successfully",
                "status_error": "Error loading image",
                "color": "Color",
                "rgb": "RGB",
                "hex": "HEX",
                "language": "فارسی"
            },
            "persian": {
                "title": "استخراج پالت رنگی",
                "select_image": "انتخاب تصویر",
                "no_image": "هیچ تصویری انتخاب نشده",
                "color_count": "تعداد رنگ‌ها:",
                "extract": "استخراج پالت",
                "status_ready": "آماده",
                "status_success": "تصویر با موفقیت بارگذاری شد",
                "status_error": "خطا در بارگذاری تصویر",
                "color": "رنگ",
                "rgb": "آر‌جی‌بی",
                "hex": "هگز",
                "language": "English"
            }
        }
        
        # رنگ‌های تم
        self.theme = {
            "bg": "#1a1a1a",  # مشکی
            "fg": "#d4af37",  # طلایی
            "secondary": "#2a2a2a",
            "active": "#d4af37",
            "text": "#ffffff",
            "highlight": "#d4af37"
        }
        
        self.create_widgets()
        
    def create_widgets(self):
        # نوار ابزار بالا
        toolbar = tk.Frame(self.root, bg=self.theme["bg"], bd=0, height=40)
        toolbar.pack(fill=tk.X)
        
        # دکمه تغییر زبان
        self.language_btn = tk.Button(
            toolbar,
            text=self.texts[self.language]["language"],
            command=self.toggle_language,
            font=("Tahoma", 10),
            bg=self.theme["bg"],
            fg=self.theme["fg"],
            activebackground=self.theme["bg"],
            activeforeground=self.theme["fg"],
            relief=tk.FLAT,
            bd=0,
            padx=10
        )
        self.language_btn.pack(side=tk.RIGHT, padx=10)
        
        # عنوان برنامه
        title_label = tk.Label(
            self.root, 
            text=self.texts[self.language]["title"], 
            font=("Tahoma", 18, "bold"), 
            bg=self.theme["bg"],
            fg=self.theme["fg"]
        )
        title_label.pack(pady=(10, 20))
        
        # فریم اصلی
        main_frame = tk.Frame(self.root, bg=self.theme["bg"], padx=20, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # فریم آپلود تصویر
        upload_frame = tk.Frame(main_frame, bg=self.theme["bg"])
        upload_frame.pack(fill=tk.X, pady=(0, 20))
        
        # دکمه انتخاب تصویر
        self.upload_btn = tk.Button(
            upload_frame,
            text=self.texts[self.language]["select_image"],
            command=self.upload_image,
            font=("Tahoma", 11),
            bg=self.theme["secondary"],
            fg=self.theme["fg"],
            padx=20,
            pady=8,
            relief=tk.FLAT,
            activebackground=self.theme["highlight"],
            activeforeground="#000000"
        )
        self.upload_btn.pack(side=tk.LEFT)
        
        # برچسب مسیر فایل
        self.file_path_label = tk.Label(
            upload_frame,
            text=self.texts[self.language]["no_image"],
            font=("Tahoma", 10),
            bg=self.theme["bg"],
            fg=self.theme["text"],
            anchor=tk.W
        )
        self.file_path_label.pack(side=tk.LEFT, padx=15, fill=tk.X, expand=True)
        #https://github.com/SaeedForouzandeh
        # فریم نمایش تصویر و پالت
        display_frame = tk.Frame(main_frame, bg=self.theme["bg"])
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # نمایش تصویر
        self.image_frame = tk.Frame(
            display_frame, 
            bg=self.theme["secondary"], 
            bd=1, 
            relief=tk.SUNKEN,
            highlightbackground=self.theme["fg"],
            highlightthickness=1
        )
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        self.image_label = tk.Label(
            self.image_frame, 
            bg=self.theme["secondary"],
            text=self.texts[self.language]["select_image"] + " →",
            fg=self.theme["text"]
        )
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # نمایش پالت رنگی
        self.palette_frame = tk.Frame(
            display_frame, 
            bg=self.theme["secondary"], 
            bd=1, 
            relief=tk.SUNKEN,
            highlightbackground=self.theme["fg"],
            highlightthickness=1
        )
        self.palette_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        #https://github.com/SaeedForouzandeh
        # کنترل‌های پالت
        controls_frame = tk.Frame(self.palette_frame, bg=self.theme["secondary"])
        controls_frame.pack(fill=tk.X, pady=(10, 5), padx=10)
        
        tk.Label(
            controls_frame,
            text=self.texts[self.language]["color_count"],
            font=("Tahoma", 10),
            bg=self.theme["secondary"],
            fg=self.theme["text"]
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.color_count = tk.IntVar(value=5)
        self.color_spinbox = tk.Spinbox(
            controls_frame,
            from_=1,
            to=10,
            textvariable=self.color_count,
            font=("Tahoma", 10),
            width=5,
            bg=self.theme["secondary"],
            fg=self.theme["text"],
            insertbackground=self.theme["text"],
            buttonbackground=self.theme["bg"],
            buttonuprelief=tk.FLAT,
            buttondownrelief=tk.FLAT,
            highlightbackground=self.theme["fg"],
            highlightcolor=self.theme["fg"],
            highlightthickness=1,
            relief=tk.FLAT
        )
        self.color_spinbox.pack(side=tk.LEFT)
        
        self.extract_btn = tk.Button(
            controls_frame,
            text=self.texts[self.language]["extract"],
            command=self.extract_palette,
            font=("Tahoma", 11),
            bg=self.theme["secondary"],
            fg=self.theme["fg"],
            padx=15,
            pady=5,
            relief=tk.FLAT,
            state=tk.DISABLED,
            activebackground=self.theme["highlight"],
            activeforeground="#000000"
        )

        self.extract_btn.pack(side=tk.RIGHT)
        
        # نمایش رنگ‌ها
        self.colors_frame = tk.Frame(
            self.palette_frame, 
            bg=self.theme["secondary"]
        )
        self.colors_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # نوار وضعیت
        self.status_label = tk.Label(
            main_frame,
            text=self.texts[self.language]["status_ready"],
            font=("Tahoma", 9),
            bg=self.theme["bg"],
            fg=self.theme["text"],
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X, pady=(15, 0))
        
    def toggle_language(self):
        self.language = "persian" if self.language == "english" else "english"
        self.update_texts()
        
    def update_texts(self):
        texts = self.texts[self.language]
        self.root.title(texts["title"])
        self.language_btn.config(text=texts["language"])
        
        # به روزرسانی متن‌ها
        self.upload_btn.config(text=texts["select_image"])
        self.extract_btn.config(text=texts["extract"])
        self.status_label.config(text=texts["status_ready"])
        
        if not hasattr(self, 'file_path'):
            self.file_path_label.config(text=texts["no_image"])
        
        if not hasattr(self, 'tk_image'):
            self.image_label.config(text=texts["select_image"] + " →")
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
  #https://github.com/SaeedForouzandeh      
        if file_path:
            self.file_path = file_path
            self.file_path_label.config(text=os.path.basename(file_path))
            self.display_image(file_path)
            self.extract_btn.config(state=tk.NORMAL)
            self.status_label.config(text=self.texts[self.language]["status_success"])
    
    def display_image(self, file_path):
        try:
            image = Image.open(file_path)
            # تغییر اندازه تصویر برای نمایش
            width, height = image.size
            ratio = min(400/width, 400/height)
            new_size = (int(width*ratio), int(height*ratio))
            image = image.resize(new_size, Image.LANCZOS)
            
            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.tk_image, text="")
        except Exception as e:
            self.status_label.config(text=self.texts[self.language]["status_error"])
    
    def extract_palette(self):
        if not hasattr(self, 'file_path'):
            self.status_label.config(text=self.texts[self.language]["select_image"])
            return
            
        try:
            num_colors = self.color_count.get()
            
            # خواندن تصویر
            image = cv2.imread(self.file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # تغییر شکل تصویر به آرایه پیکسل‌ها
            pixels = image.reshape(-1, 3)
            
            # استفاده از K-Means برای خوشه‌بندی رنگ‌ها
            kmeans = KMeans(n_clusters=num_colors, n_init=10)
            kmeans.fit(pixels)
            
            # رنگ‌های غالب
            colors = kmeans.cluster_centers_.astype(int)
            
            # نمایش پالت
            self.display_palette(colors)
            
            self.status_label.config(text=f"{num_colors} {self.texts[self.language]['color']} extracted")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
    
    def display_palette(self, colors):
        # پاک کردن فریم قبلی
        for widget in self.colors_frame.winfo_children():
            widget.destroy()
        
        # نمایش هر رنگ در پالت
        for i, color in enumerate(colors):
            color_hex = mcolors.to_hex([x/255 for x in color])
            r, g, b = color
            
            # نمایش رنگ
            color_frame = tk.Frame(
                self.colors_frame,
                bg=color_hex,
                bd=1,
                relief=tk.RAISED,
                height=50,
                highlightbackground=self.theme["fg"],
                highlightthickness=1
            )
            color_frame.pack(fill=tk.X, pady=2)
            
            # نمایش اطلاعات رنگ
            info_frame = tk.Frame(color_frame, bg=color_hex)
            info_frame.pack(fill=tk.BOTH, expand=True)
            
            tk.Label(
                info_frame,
                text=f"{self.texts[self.language]['color']} {i+1}",
                font=("Tahoma", 10),
                bg=color_hex,
                fg=self.get_contrast_color(color)
            ).pack(side=tk.LEFT, padx=10)
            
            tk.Label(
                info_frame,
                text=f"{self.texts[self.language]['rgb']}: {r}, {g}, {b}",
                font=("Tahoma", 10),
                bg=color_hex,
                fg=self.get_contrast_color(color)
            ).pack(side=tk.LEFT, padx=10)
            
            tk.Label(
                info_frame,
                text=f"{self.texts[self.language]['hex']}: {color_hex}",
                font=("Tahoma", 10),
                bg=color_hex,
                fg=self.get_contrast_color(color)
            ).pack(side=tk.RIGHT, padx=10)
    
    def get_contrast_color(self, rgb_color):
        # محاسبه روشنایی رنگ برای تعیین رنگ متن مناسب
        r, g, b = rgb_color
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "#000000" if brightness > 128 else "#ffffff"
#https://github.com/SaeedForouzandeh
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPaletteExtractor(root)
    root.mainloop()