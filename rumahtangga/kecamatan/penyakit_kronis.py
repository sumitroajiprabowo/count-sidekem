import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `districts` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    """Penyakit Kronis Menahun"""
    """Tidak Ada Penyakit"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '0' ")
    tidak_ada = str(cur.fetchone()[0])
    """Hipertensi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '1' ")
    hipertensi = str(cur.fetchone()[0])
    """Rematik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '2' ")
    rematik = str(cur.fetchone()[0])
    """Asma"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '3' ")
    asma = str(cur.fetchone()[0])
    """Jantung"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '4' ")
    masalah_jantung = str(cur.fetchone()[0])
    """diabetes"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '5' ")
    diabetes = str(cur.fetchone()[0])
    """TBC"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '6' ")
    tbc = str(cur.fetchone()[0])
    """Stroke"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '7' ")
    stroke = str(cur.fetchone()[0])
    """kanker_tumor_ganas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '8' ")
    kanker_tumor_ganas = str(cur.fetchone()[0])
    """Penyakit Lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND penyakit_kronis LIKE '9' ")
    lainnya = str(cur.fetchone()[0])
    """Insert to DB"""
    cur.execute("UPDATE `statistik_penyakit_kronis_kec` SET `tidak_ada`='"+tidak_ada+"', `hipertensi`='"+hipertensi+"', \
        `rematik`='"+rematik+"', `asma`='"+asma+"', `masalah_jantung`='"+masalah_jantung+"', `diabetes`='"+diabetes+"',\
        `tbc`='"+tbc+"', `stroke`='"+stroke+"',`kanker_tumor_ganas`='"+kanker_tumor_ganas+"', `lainnya`='"+lainnya+"' WHERE id='"+a[0]+"' ")
    db.commit()
