import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `regencies` WHERE id LIKE '%3327%' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    """Counting Bahan Bakar Masak"""
    """bahan_bakar_masak_listrik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '1' ")
    bahan_bakar_masak_listrik = str(cur.fetchone()[0])
    """bahan_bakar_masak_gas>3kg"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '2' ")
    bahan_bakar_masak_gaslebih3kg = str(cur.fetchone()[0])
    """bahan_bakar_masak_gas3kg"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '3' ")
    bahan_bakar_masak_gas3kg = str(cur.fetchone()[0])
    """bahan_bakar_masak_biogas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '4' ")
    bahan_bakar_masak_biogas = str(cur.fetchone()[0])
    """bahan_bakar_masak_minyaktanah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '5' ")
    bahan_bakar_masak_minyaktanah = str(cur.fetchone()[0])
    """bahan_bakar_masak_briket"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '6' ")
    bahan_bakar_masak_briket = str(cur.fetchone()[0])
    """bahan_bakar_masak_arang"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '7' ")
    bahan_bakar_masak_arang = str(cur.fetchone()[0])
    """bahan_bakar_masak_kayubakar"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '8' ")
    bahan_bakar_masak_kayubakar = str(cur.fetchone()[0])
    """bahan_bakar_masak_tdkmemasakdirumah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND bahan_bakar_masak LIKE '9' ")
    bahan_bakar_masak_tdkmemasakdirumah = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_bahanbakarmasak_kab` SET `bahan_bakar_masak_listrik`='"+bahan_bakar_masak_listrik+"', \
        `bahan_bakar_masak_gaslebih3kg`='"+bahan_bakar_masak_gaslebih3kg+"', `bahan_bakar_masak_gas3kg`='"+bahan_bakar_masak_gas3kg+"', \
        `bahan_bakar_masak_biogas`='"+bahan_bakar_masak_biogas+"', `bahan_bakar_masak_minyaktanah`='"+bahan_bakar_masak_minyaktanah+"', \
        `bahan_bakar_masak_briket`='"+bahan_bakar_masak_briket+"',\
        `bahan_bakar_masak_arang`='"+bahan_bakar_masak_arang+"', `bahan_bakar_masak_kayubakar`='"+bahan_bakar_masak_kayubakar+"', \
        `bahan_bakar_masak_tdkmemasakdirumah`='"+bahan_bakar_masak_tdkmemasakdirumah+"' WHERE id='"+a[0]+"' ")
    db.commit()


