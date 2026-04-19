import re
from datetime import datetime

teks = """Pada tanggal 1945-08-17 Indonesia merdeka.
Pangeran Diponegoro (1785-11-11),
Pattimura (1783-06-08),
Ki Hajar Dewantara (1889-05-02)."""

tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

today = datetime.now()

for t in tanggal_list:
    tgl = datetime.strptime(t, "%Y-%m-%d")
    selisih = (today - tgl).days
    print(tgl, "selisih", selisih, "hari")