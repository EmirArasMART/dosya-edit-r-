import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

DOSYA_TURLERI = {
    "Resimler": [".jpg", ".jpeg", ".png", ".gif"],
    "Belgeler": [".pdf", ".doc", ".docx", ".txt"],
    "Videolar": [".mp4", ".avi", ".mkv"],
    "Müzikler": [".mp3", ".wav"],
    "Python": [".py"],
    "Sıkıştırılmış": [".zip", ".rar", ".7z"]
}

def klasor_sec():
    klasor = filedialog.askdirectory(title="Bir klasör seç")
    if klasor:
        klasor_label.config(text=klasor)
        duzenle_btn.config(state="normal")

def duzenle():
    klasor = klasor_label.cget("text")
    tasinan = 0
    for dosya in os.listdir(klasor):
        yol = os.path.join(klasor, dosya)
        if os.path.isfile(yol):
            uzanti = os.path.splitext(dosya)[1].lower()
            for hedef, uzantilar in DOSYA_TURLERI.items():
                if uzanti in uzantilar:
                    hedef_klasor = os.path.join(klasor, hedef)
                    os.makedirs(hedef_klasor, exist_ok=True)
                    shutil.move(yol, os.path.join(hedef_klasor, dosya))
                    tasinan += 1
                    break
    sonuc.config(text=f"✅ {tasinan} dosya düzenlendi.")
    messagebox.showinfo("Tamamlandı", "Dosyalar başarıyla düzenlendi!")

pencere = tk.Tk()
pencere.title("Dosya Organizatörü")
pencere.geometry("500x280")
pencere.resizable(False, False)

tk.Label(pencere, text="📁 Dosya Organizatörü", font=("Arial",18,"bold")).pack(pady=15)
tk.Button(pencere, text="📂 Klasör Seç", command=klasor_sec, width=20).pack()

klasor_label = tk.Label(pencere, text="Henüz klasör seçilmedi", wraplength=450)
klasor_label.pack(pady=10)

duzenle_btn = tk.Button(pencere, text="🚀 Dosyaları Düzenle", command=duzenle, state="disabled", width=20)
duzenle_btn.pack(pady=10)

sonuc = tk.Label(pencere, text="", font=("Arial",11))
sonuc.pack(pady=10)

pencere.mainloop()
