import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View untuk Anggota
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding (mengikat) tombol-tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Memuat data ke tabel saat aplikasi anggota pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke dalam tabel View
        for anggota in data_anggota:
            self.view.tabel.insert(
                "", "end",
                values=(
                    anggota['id_anggota'],
                    anggota['nama'],
                    anggota['alamat']
                )
            )

    def simpan_data(self):
        # Mengambil teks dari kotak input di View
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        # Validasi Form Kosong
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form anggota harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            
            # Bersihkan form input
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_alamat.delete(0, 'end')
            
            # Muat ulang tabel
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data anggota.")

    def perbarui_data(self):
        # Ambil baris tabel yang dipilih
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota pada tabel yang ingin diperbarui terlebih dahulu!")
            return
        
        # Ambil ID anggota dari kolom pertama
        item_data = self.view.tabel.item(selected_item)
        id_anggota = item_data['values'][0]

        # Ambil data baru dari form
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk memperbarui!")
            return

        try:
            self.model.update_anggota(id_anggota, nama, alamat)
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_alamat.delete(0, 'end')
            self.muat_data_tabel()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat memperbarui data anggota: {e}")

    def hapus_data(self):
        # Ambil baris tabel yang dipilih
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota pada tabel yang ingin dihapus terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?")
        if konfirmasi:
            item_data = self.view.tabel.item(selected_item)
            id_anggota = item_data['values'][0]

            try:
                self.model.delete_anggota(id_anggota)
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                
                self.view.entry_nama.delete(0, 'end')
                self.view.entry_alamat.delete(0, 'end')
                self.muat_data_tabel()
            except Exception as e:
                messagebox.showerror("Error", f"Terjadi kesalahan saat menghapus data anggota: {e}")

    def run(self):
        self.view.mainloop()