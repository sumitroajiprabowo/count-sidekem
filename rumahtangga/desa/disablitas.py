import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `villages` WHERE id LIKE '%3327%' ")
desa=cur.fetchall()
for a in desa:
    """Disablitas"""

    """Tidak Cacat"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '0' ")
    tidak_cacat = str(cur.fetchone()[0])

    """Tuna daksa/ cacat tubuh"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '1' ")
    tuna_daksa = str(cur.fetchone()[0])

    """Tuna netra/buta"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '2' ")
    tuna_netra = str(cur.fetchone()[0])

    """Tuna Rungu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '3' ")
    tuna_rungu = str(cur.fetchone()[0])

    """Tuna Wicara"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '4' ")
    tuna_wicara = str(cur.fetchone()[0])

    """Tuna rungu & wicara"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '5' ")
    tuna_rungu_wicara = str(cur.fetchone()[0])

    """Tuna netra & cacat tubuh"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '6' ")
    tuna_netra_daksa = str(cur.fetchone()[0])

    """Tuna netra, rungu & wicara"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '7' ")
    tuna_netra_rungu_wicara = str(cur.fetchone()[0])
    
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '8' ")
    tuna_rungu_wicara_daksa = str(cur.fetchone()[0])

    """Tuna rungu, wicara & cacat tubuh"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '9' ")
    tuna_rungu_wicara_netra_daksa = str(cur.fetchone()[0])

    """Cacat Mental retardasi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '10' ")
    cacat_mental = str(cur.fetchone()[0])

    """Mantan penderita gangguan jiwa"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '11' ")
    mantan_penderita_gangguan_jiwa = str(cur.fetchone()[0])

    """Cacat mental & fisik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE desa_id='"+a[0]+"' AND jenis_cacat LIKE '12' ")
    cacat_fisik_mental = str(cur.fetchone()[0])

    """Insert to DB"""
    cur.execute("UPDATE `statistik_disabilitas_desa` SET `tidak_cacat`='"+tidak_cacat+"', `tuna_daksa`='"+tuna_daksa+"',\
        `tuna_netra`='"+tuna_netra+"', `tuna_rungu`='"+tuna_rungu+"', `tuna_wicara`='"+tuna_wicara+"', `tuna_rungu_wicara`='"+tuna_rungu_wicara+"', \
        `tuna_netra_daksa`='"+tuna_netra_daksa+"', `tuna_netra_rungu_wicara`='"+tuna_netra_rungu_wicara+"', \
        `tuna_rungu_wicara_daksa`='"+tuna_rungu_wicara_daksa+"', `tuna_rungu_wicara_netra_daksa`='"+tuna_rungu_wicara_netra_daksa+"', \
        `cacat_mental`='"+cacat_mental+"', `mantan_penderita_gangguan_jiwa`='"+mantan_penderita_gangguan_jiwa+"', \
        `cacat_fisik_mental`='"+cacat_fisik_mental+"' WHERE id='"+a[0]+"' ")
    db.commit()
