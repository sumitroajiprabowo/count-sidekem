import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `villages` WHERE id LIKE '%3327%' ")
desa=cur.fetchall()
for a in desa:
    """Counting Penerangan"""
    """listrik_pln"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' ")
    listrik_pln = str(cur.fetchone()[0])
    """listrik_non_pln"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '2' ")
    listrik_non_pln = str(cur.fetchone()[0])
    """bukan_listrik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '3' ")
    bukan_listrik = str(cur.fetchone()[0])

    """Counting Daya Listrik"""
    """daya_450watt"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '1' ")
    daya_450watt = str(cur.fetchone()[0])
    """daya_900watt"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '2' ")
    daya_900watt = str(cur.fetchone()[0])
    """daya_1300watt"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '3' ")
    daya_1300watt = str(cur.fetchone()[0])
    """daya_2200watt"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '4' ")
    daya_2200watt = str(cur.fetchone()[0])
    """daya_>2200watt"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '5' ")
    daya_lebihdari2200watt = str(cur.fetchone()[0])
    """tanpa_meteran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE desa_id='"+a[0]+"' AND sumber_penerangan LIKE '1' AND daya_listrik LIKE '6' ")
    tanpa_meteran = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_penerangan_desa` SET `listrik_pln`='"+listrik_pln+"', `listrik_non_pln`='"+listrik_non_pln+"', \
        `bukan_listrik`='"+bukan_listrik+"', \
        `daya_450watt`='"+daya_450watt+"', `daya_900watt`='"+daya_900watt+"', `daya_1300watt`='"+daya_1300watt+"',\
        `daya_2200watt`='"+daya_2200watt+"', `daya_>2200watt`='"+daya_lebihdari2200watt+"', `tanpa_meteran`='"+tanpa_meteran+"' WHERE id='"+a[0]+"' ")
    db.commit()
