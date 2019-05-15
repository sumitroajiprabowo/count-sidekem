import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `villages` WHERE id LIKE '%3327%' ")
desa=cur.fetchall()
for a in desa:
    """Kepemilikan Kartu Identitas"""
    """Akta Kelahiran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND akta_kelahiran LIKE 'Ya' ")
    akta_kelahiran = str(cur.fetchone()[0])
    """Kartu Pelajar"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND kartu_pelajar LIKE 'Ya' ")
    kartu_pelajar = str(cur.fetchone()[0])
    """KTP"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND ktp LIKE 'Ya' ")
    ktp = str(cur.fetchone()[0])
    """SIM"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND sim LIKE 'Ya' ")
    sim = str(cur.fetchone()[0])
    """Tidak Memiliki Kartu Identitas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND tidak_memiliki_kartu_identitas LIKE 'Ya' ")
    tidak_memiliki_kartu_identitas = str(cur.fetchone()[0])
    cur.execute("UPDATE `statistik_kepemilikankartuidentitas_desa` SET `akta_kelahiran`='"+akta_kelahiran+"', \
        `kartu_pelajar`='"+kartu_pelajar+"', `ktp`='"+ktp+"', `sim`='"+sim+"', \
        `tidak_memiliki_kartu_identitas`='"+tidak_memiliki_kartu_identitas+"' WHERE id='"+a[0]+"' ")
    db.commit()
