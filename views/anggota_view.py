import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):

  def __init__(self):
    super().__init__()
    self.title("Sistem Manajemen Perpustakaan - Anggota")
    self.geometry("800x450")

    # Konfigurasi Grid Utama (1 Baris, 2 Kolom)[span_0](start_span)[span_0](end_span)
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=2)
    self.grid_rowconfigure(0, weight=1)

    # ==================== FRAME KIRI: FORMULIR INPUT ANGGOTA ====================
    self.frame_kiri = ctk.CTkFrame(self)
    self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    ctk.CTkLabel(
        self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Label & Entry untuk Nama Anggota[span_1](start_span)[span_1](end_span)
    ctk.CTkLabel(
        self.frame_kiri, text="Nama Anggota:", font=("Arial", 12, "bold")
    ).pack(anchor="w", padx=15)
    self.entry_nama = ctk.CTkEntry(
        self.frame_kiri, placeholder_text="Masukkan Nama Anggota"
    )
    self.entry_nama.pack(pady=(5, 10), padx=15, fill="x")

    # Label & Entry untuk Alamat[span_2](start_span)[span_2](end_span)
    ctk.CTkLabel(
        self.frame_kiri, text="Alamat:", font=("Arial", 12, "bold")
    ).pack(anchor="w", padx=15)
    self.entry_alamat = ctk.CTkEntry(
        self.frame_kiri, placeholder_text="Masukkan Alamat Anggota"
    )
    self.entry_alamat.pack(pady=(5, 10), padx=15, fill="x")

    # Tombol Aksi (Simpan, Update, Delete)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
    self.btn_simpan = ctk.CTkButton(
        self.frame_kiri, text="Simpan Data", fg_color="green"
    )
    self.btn_simpan.pack(pady=10, padx=15, fill="x")

    self.btn_update = ctk.CTkButton(
        self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue"
    )
    self.btn_update.pack(pady=5, padx=15, fill="x")

    self.btn_delete = ctk.CTkButton(
        self.frame_kiri, text="Hapus Data (Delete)", fg_color="red"
    )
    self.btn_delete.pack(pady=5, padx=15, fill="x")

    # ==================== FRAME KANAN: TABEL DAFTAR ANGGOTA ====================
    self.frame_kanan = ctk.CTkFrame(self)
    self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    ctk.CTkLabel(
        self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Kolom Tabel Anggota (ID, Nama Anggota, Alamat)[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)
    kolom = ("id_anggota", "nama_anggota", "alamat")
    self.tabel = ttk.Treeview(
        self.frame_kanan, columns=kolom, show="headings", height=15
    )

    # Konfigurasi Header Tabel[span_7](start_span)[span_7](end_span)
    self.tabel.heading("id_anggota", text="ID")
    self.tabel.heading("nama_anggota", text="Nama Anggota")
    self.tabel.heading("alamat", text="Alamat")

    # Konfigurasi Lebar Kolom[span_8](start_span)[span_8](end_span)
    self.tabel.column("id_anggota", width=40, anchor="center")
    self.tabel.column("nama_anggota", width=150)
    self.tabel.column("alamat", width=180)

    self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

    # ==================== DATA SPESIFIK ANGGOTA (ALAMAT SIMPEL) ====================
    sample_anggota = [
        (1, "Anjar", "Bandung"),
        (2, "Intan", "Jakarta"),
        (3, "Nawilla", "Yogyakarta"),
        (4, "Jeonghan", "Surabaya"),
    ]

    for anggota in sample_anggota:
      self.tabel.insert("", "end", values=anggota)


if __name__ == "__main__":
  app = AnggotaView()
  app.mainloop()