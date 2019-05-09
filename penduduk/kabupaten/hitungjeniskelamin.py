import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_jk_kab` WHERE id LIKE '%3327%' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    #Kepala Keluarga Laki-laki
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Laki-laki' AND shdk LIKE 'Kepala Keluarga'")
    jk1 = str(cur.fetchone()[0])
    #Anggota Keluarga Laki-laki
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Laki-laki' AND shdk NOT LIKE 'Kepala Keluarga'")
    jk2 = str(cur.fetchone()[0])
    #Total Laki-laki
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Laki-laki' ")
    jk3 = str(cur.fetchone()[0])
    #Kepala Keluarga Perempuan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Perempuan' AND shdk LIKE 'Kepala Keluarga' ")
    jk4 = str(cur.fetchone()[0])
    #Anggota Keluarga Perempuan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Perempuan' AND shdk  NOT LIKE 'Kepala Keluarga' ")
    jk5 = str(cur.fetchone()[0])
    #Total Perempuan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'Perempuan' ")
    jk6 = str(cur.fetchone()[0])
    #Eksekusi Database
    cur.execute("UPDATE `statistik_jk_kab` SET `kk_lk`='"+jk1+"',`ak_lk`='"+jk2+"',`total_lk`='"+jk3+"',`kk_pr`='"+jk4+"',`ak_pr`='"+jk5+"',`total_pr`='"+jk6+"' WHERE id='"+a[0]+"' ")
    db.commit()