import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class BildVergleicherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel-für-Pixel Bildvergleich")
        self.root.geometry("950x700")
        
        self.pfad_bild1 = None
        self.pfad_bild2 = None
        
        # --- Oberer Bereich: Vergleichs-Button & Ergebnis ---
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=20)
        
        self.btn_vergleich = tk.Button(
            self.top_frame, text="Bilder vergleichen", command=self.starte_vergleich, 
            state=tk.DISABLED, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", 
            padx=10, pady=5
        )
        self.btn_vergleich.pack()
        
        self.lbl_ergebnis = tk.Label(self.top_frame, text="Bitte wähle zwei Bilder aus.", font=("Arial", 12, "bold"), fg="#333333", pady=10)
        self.lbl_ergebnis.pack()
        
        # --- Unterer Bereich: Die Rahmen für die Bilder ---
        self.img_container = tk.Frame(root)
        self.img_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Linker Rahmen (Bild 1)
        self.frame_links = tk.LabelFrame(self.img_container, text=" Bild 1 ", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.frame_links.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        self.btn_laden1 = tk.Button(self.frame_links, text="Bild 1 durchsuchen...", command=self.laden_bild1)
        self.btn_laden1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.lbl_vorschau1 = tk.Label(self.frame_links)
        
        # Rechter Rahmen (Bild 2)
        self.frame_rechts = tk.LabelFrame(self.img_container, text=" Bild 2 ", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.frame_rechts.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        self.btn_laden2 = tk.Button(self.frame_rechts, text="Bild 2 durchsuchen...", command=self.laden_bild2)
        self.btn_laden2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.lbl_vorschau2 = tk.Label(self.frame_rechts)

    def laden_bild1(self):
        self.pfad_bild1 = filedialog.askopenfilename(filetypes=[("Bilddateien", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if self.pfad_bild1:
            self.btn_laden1.place_forget()  # Button verstecken
            self.zeige_vorschau(self.pfad_bild1, self.lbl_vorschau1, self.frame_links)
            self.pruefe_startbereitschaft()

    def laden_bild2(self):
        self.pfad_bild2 = filedialog.askopenfilename(filetypes=[("Bilddateien", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if self.pfad_bild2:
            self.btn_laden2.place_forget()  # Button verstecken
            self.zeige_vorschau(self.pfad_bild2, self.lbl_vorschau2, self.frame_rechts)
            self.pruefe_startbereitschaft()

    def zeige_vorschau(self, pfad, label_objekt, frame_objekt):
        img = Image.open(pfad)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        
        label_objekt.config(image=img_tk)
        label_objekt.image = img_tk
        label_objekt.pack(fill=tk.BOTH, expand=True)

    def pruefe_startbereitschaft(self):
        if self.pfad_bild1 and self.pfad_bild2:
            self.btn_vergleich.config(state=tk.NORMAL)

    def starte_vergleich(self):
        try:
            img1 = Image.open(self.pfad_bild1).convert('RGB')
            img2 = Image.open(self.pfad_bild2).convert('RGB')
            
            if img1.size != img2.size:
                messagebox.showerror("Fehler", f"Die Bilder müssen die gleiche Auflösung haben!\n\nBild 1: {img1.size}px\nBild 2: {img2.size}px")
                return
            
            arr1 = np.array(img1)
            arr2 = np.array(img2)
            unterschieds_maske = np.any(arr1 != arr2, axis=-1)
            
            anzahl_ziel = int(np.sum(unterschieds_maske))
            gesamt_pixel = img1.size[0] * img1.size[1]
            
            self.animiere_ergebnis(0, anzahl_ziel, gesamt_pixel)
            
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten:\n{str(e)}")

    def animiere_ergebnis(self, aktueller_wert, ziel_wert, gesamt_pixel):
        schritt = max(1, int((ziel_wert - aktueller_wert) / 15))
        neuer_wert = aktueller_wert + schritt
        
        if neuer_wert >= ziel_wert:
            neuer_wert = ziel_wert
            
        prozent = (neuer_wert / gesamt_pixel) * 100
        
        self.lbl_ergebnis.config(
            text=f"Ergebnis: {neuer_wert:,} von {gesamt_pixel:,} Pixeln unterschiedlich ({prozent:.2f}%)".replace(",", ".")
        )
        
        if neuer_wert < ziel_wert:
            self.root.after(20, lambda: self.animiere_ergebnis(neuer_wert, ziel_wert, gesamt_pixel))

if __name__ == "__main__":
    root = tk.Tk()
    app = BildVergleicherApp(root)
    root.mainloop()
