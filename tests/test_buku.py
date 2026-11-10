from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # menginstalasi model
    model = BukuModel()

    # memanipulasi (mock) koneksi database agar tidak mengotori data asli 
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # memverifikasi apakah fungsi mengambilkan nilai true 
    assert hasil is True
    # memverifikasi apakah cursor.execute benar-benar dipanggil 
    mock_cursor.execute.assert_called_once()
    # memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

from models.buku_model import BukuModel

def test_get_all_buku_berhasil():
    # Inisialisasi model buku
    model = BukuModel()
    
    # Panggil fungsi get_all_buku
    result = model.get_all_buku()
    
    # Memastikan bahwa hasil yang dikembalikan berupa list (kumpulan data)
    assert isinstance(result, list)