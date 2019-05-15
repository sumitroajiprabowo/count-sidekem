import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `regencies` WHERE id LIKE '%3327%' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    """Keikutsertaan Program Pemerintah"""
    """Kartu Keluarga Sejahtera (KKS)/ Kartu Perlindungan Sosial (KPS)"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND kks_kps LIKE '1' ")
    kks_kps = str(cur.fetchone()[0])
    """Kartu Indonesia Pintar (KIP)/ Bantuan Siswa Miskin (BSM)"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bip_bsm LIKE '3' ")
    kip_bsm = str(cur.fetchone()[0])
    """Kartu Indonesia Sehat (KIS)/ BPJS Kesehatan/Jamkesmas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND kis_bpjs_jamkesmas LIKE '1' ")
    kis_bpjs_jamkesmas = str(cur.fetchone()[0])
    """BPJS Kesehatan peserta mandiri"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bpjs_mandiri LIKE '3' ")
    bpjs_mandiri = str(cur.fetchone()[0])
    """Jaminan sosial tenaga kerja (Jamsostek)/ BPJS ketenagakerjaan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND jamsostek_bpjs_ketenagakerjaan LIKE '1' ")
    jamsostek_bpjs_ketenagakerjaan = str(cur.fetchone()[0])
    """Asuransi kesehatan lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND asuransi_kesehatan_lainnya LIKE '3' ")
    asuransi_kesehatan_lainnya = str(cur.fetchone()[0])
    """Program Keluarga Harapan (PKH)"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND pkh LIKE '1' ")
    pkh = str(cur.fetchone()[0])
    """Beras untuk orang miskin (Raskin)"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND kur LIKE '1' ")
    raskin = str(cur.fetchone()[0])
    """Kredit Usaha Rakyat (KUR)"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND raskin LIKE '3' ")
    kur = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_keikutsertaanprogram_kab` SET `kks_kps`='"+kks_kps+"', \
        `kip_bsm`='"+kip_bsm+"', `kis_bpjs_jamkesmas`='"+kis_bpjs_jamkesmas+"', `bpjs_mandiri`='"+bpjs_mandiri+"', \
        `jamsostek_bpjs_ketenagakerjaan`='"+jamsostek_bpjs_ketenagakerjaan+"', `asuransi_kesehatan_lainnya`='"+asuransi_kesehatan_lainnya+"', \
        `pkh`='"+pkh+"', `raskin`='"+raskin+"', `kur`='"+kur+"' WHERE id='"+a[0]+"' ")
    db.commit()