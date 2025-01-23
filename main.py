import tkinter as tk
from PIL import Image, ImageTk


def show_fullscreen_image():
    fullscreen = tk.Toplevel()
    fullscreen.attributes('-fullscreen', True)
    fullscreen.configure(bg="black")

    def resize_image(event):
        resized_image = original_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        img_label.config(image=photo)
        img_label.image = photo

    original_image = Image.open("assets/detected.jpeg")
    resized_image = original_image.resize(
        (fullscreen.winfo_screenwidth(), fullscreen.winfo_screenheight()), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    img_label = tk.Label(fullscreen, image=photo, bg="black")
    img_label.image = photo
    img_label.pack(fill=tk.BOTH, expand=True)

    fullscreen.bind("<Configure>", resize_image)
    fullscreen.bind("<Escape>", lambda e: fullscreen.destroy())


def main():
    root = tk.Tk()
    root.title("Shrimp Detector")
    root.geometry("800x600")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame, text="Shrimp Detector", font=("Arial", 24))
    label.pack(pady=20)

    image = Image.open("assets/shrimp.png")
    image = ImageTk.PhotoImage(image)
    img_label = tk.Label(frame, image=image)
    img_label.image = image
    img_label.pack(pady=10)

    button = tk.Button(frame, text="Detect", command=show_fullscreen_image)
    button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
