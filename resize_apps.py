import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageFilter

def resize_image_to_6x4(image_path, output_path, dpi=300):
    with Image.open(image_path) as img:
        width_inch = 6
        height_inch = 4
        target_size = (int(width_inch * dpi), int(height_inch * dpi))
        img_resized = img.resize(target_size, Image.LANCZOS)
        img_sharpened = img_resized.filter(ImageFilter.SHARPEN)
        img_sharpened.save(output_path, dpi=(dpi, dpi))

def select_image():
    # Testing the file dialog separately
    file_path = filedialog.askopenfilename(
        filetypes=[("JPG Files", "*.jpg"), 
                   ("JPEG Files", "*.jpeg"),
                   ("PNG Files", "*.png"), 
                   ("Bitmap Files", "*.bmp"), 
                   ("GIF Files", "*.gif"),
                   ("All Files", "*.*")]
    )
    if file_path:
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if output_path:
            resize_image_to_6x4(file_path, output_path)
            Label(root, text="Image resized and saved!").pack()

# Set up the GUI
root = Tk()
root.title("6x4 Image Resizer")
Label(root, text="Select an image to resize:").pack(pady=10)
Button(root, text="Browse image", command=select_image).pack(pady=10)
root.mainloop()
