import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `districts` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    """Aset Bergerak"""
    """tabung_gas_5_5kg_lebih"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND tabung_gas_5_5kg_lebih LIKE '1' ")
    tabung_gas_5_5kg_lebih = str(cur.fetchone()[0])
    """kulkas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND kulkas LIKE '3' ")
    kulkas = str(cur.fetchone()[0])
    """AC"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND ac LIKE '1' ")
    ac = str(cur.fetchone()[0])
    """Pemanas Air"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND pemanas_air LIKE '3' ")
    pemanas_air = str(cur.fetchone()[0])
    """Telp Rumah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND telp_rumah LIKE '1' ")
    telp_rumah = str(cur.fetchone()[0])
    """Televisi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND televisi LIKE '3' ")
    televisi = str(cur.fetchone()[0])
    """Emas Perhiasan, Tabungan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND emas_perhiasan_tabungan LIKE '1' ")
    emas_perhiasan_tabungan = str(cur.fetchone()[0])
    """Komputer"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND komputer LIKE '3' ")
    komputer = str(cur.fetchone()[0])
    """Sepeda"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND sepeda LIKE '1' ")
    sepeda = str(cur.fetchone()[0])
    """Sepeda Motor"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND sepeda_motor LIKE '3' ")
    sepeda_motor = str(cur.fetchone()[0])
    """Mobil"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND mobil LIKE '1' ")
    mobil = str(cur.fetchone()[0])
    """Perahu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND perahu LIKE '3' ")
    perahu = str(cur.fetchone()[0])
    """Motor Tempel"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND motor_tempel LIKE '1' ")
    motor_tempel = str(cur.fetchone()[0])
    """Perahu Motor"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND perahu_motor LIKE '3' ")
    perahu_motor = str(cur.fetchone()[0])
    """Kapal"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND kapal LIKE '1' ")
    kapal = str(cur.fetchone()[0])

    """Aset Tidak Bergerak"""
    """Lahan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND aset_lahan LIKE '1' ")
    lahan = str(cur.fetchone()[0])
    """Rumah ditempat lain"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND rumah_ditempat_lain LIKE '3' ")
    rumah_ditempatlain = str(cur.fetchone()[0])

    """Ternak"""
    """Sapi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jumlah_sapi>=1 ")
    sapi = str(cur.fetchone()[0])
    """Kerbau"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jumlah_kerbau>=1 ")
    kerbau = str(cur.fetchone()[0])
    """Kuda"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jumlah_kuda>=1 ")
    kuda = str(cur.fetchone()[0])
    """Babi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jumlah_babi>=1 ")
    babi = str(cur.fetchone()[0])
    """Kambing atau Domba"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jumlah_kambing_domba>=1 ")
    kambing = str(cur.fetchone()[0])

    """insert to sql"""
    cur.execute("UPDATE `statistik_kepemilikanaset_kec` SET `tabung_gas_5_5kg_lebih`='"+tabung_gas_5_5kg_lebih+"', \
        `kulkas`='"+kulkas+"', `ac`='"+ac+"', `pemanas_air`='"+pemanas_air+"', `telp_rumah`='"+telp_rumah+"', \
        `televisi`='"+televisi+"', `emas_perhiasan_tabungan`='"+emas_perhiasan_tabungan+"', `komputer`='"+komputer+"', \
        `sepeda`='"+sepeda+"', `sepeda_motor`='"+sepeda_motor+"', `mobil`='"+mobil+"', \
        `perahu`='"+perahu+"', `motor_tempel`='"+motor_tempel+"', `perahu_motor`='"+perahu_motor+"', \
        `kapal`='"+kapal+"', `lahan`='"+lahan+"', `rumah_ditempatlain`='"+rumah_ditempatlain+"', \
        `sapi`='"+sapi+"', `kerbau`='"+kerbau+"', `kuda`='"+kuda+"', \
        `babi`='"+babi+"', `kambing/domba`='"+kambing+"' WHERE id='"+a[0]+"' ")
    db.commit()
