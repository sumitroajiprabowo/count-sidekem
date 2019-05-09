import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_penduduk_kab` WHERE id LIKE '%3327%' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    """Hitung KK"""
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33`  WHERE kab_id='"+a[0]+"' AND shdk LIKE 'KEPALA KELUARGA' ")
    hasilkk = str(cur.fetchone()[0])
    """Hitung Anggota Keluarga"""
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND shdk NOT LIKE 'KEPALA KELUARGA'")
    hasilak = str(cur.fetchone()[0])
    """Hitung Semua Penduduk"""
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' ")
    hasilpenduduk = str(cur.fetchone()[0])
    """Insert to Database"""
    cur.execute("UPDATE statistik_penduduk_kab SET total_kk='"+hasilkk+"',total_ak='"+hasilak+"',total_penduduk='"+hasilpenduduk+"' WHERE id='"+a[0]+"' ")
    db.commit()
