import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `districts` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    """Status Bangunan"""
    """Bangunan Milik Sendiri"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_bangunan LIKE '1' ")
    bangunan_milik_sendiri = str(cur.fetchone()[0])
    """Bangunan Sewa atau Kontrak"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_bangunan LIKE '2' ")
    bangunan_sewa = str(cur.fetchone()[0])
    """Bangunan bebas sewa"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_bangunan LIKE '3' ")
    bangunan_bebas_sewa = str(cur.fetchone()[0])
    """Bangunan dinas"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_bangunan LIKE '4' ")
    bangunan_dinas = str(cur.fetchone()[0])
    """Bangunan lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_bangunan LIKE '5' ")
    bangunan_lainnya = str(cur.fetchone()[0])


    """Status Lahan"""
    """Status lahan milik sendiri"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_lahan LIKE '1' ")
    lahan_milik_sendiri = str(cur.fetchone()[0])
    """Status lahan milik orang lain"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_lahan LIKE '2' ")
    lahan_milik_orglain = str(cur.fetchone()[0])
    """Status lahan tanah negara"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_lahan LIKE '3' ")
    lahan_tanah_negara = str(cur.fetchone()[0])
    """Status lahan lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND status_lahan LIKE '4' ")
    lahan_lainnya = str(cur.fetchone()[0])

    """Insert to Database"""
    cur.execute("UPDATE `statistik_bangunan_kec` SET `bangunan_milik_sendiri`='"+bangunan_milik_sendiri+"', `bangunan_sewa`='"+bangunan_sewa+"', \
        `bangunan_bebas_sewa`='"+bangunan_bebas_sewa+"', `bangunan_dinas`='"+bangunan_dinas+"', \
        `bangunan_lainnya`='"+bangunan_lainnya+"', `lahan_milik_sendiri`='"+lahan_milik_sendiri+"', `lahan_milik_orglain`='"+lahan_milik_orglain+"',\
        `lahan_tanah_negara`='"+lahan_tanah_negara+"', `lahan_lainnya`='"+lahan_lainnya+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Jenis Lantai"""
    """Lantai marmer, granit"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '1' ")
    lantai_marmer_granit = str(cur.fetchone()[0])
    """Lantai keramik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '2' ")
    lantai_keramik = str(cur.fetchone()[0])
    """Lantai parket, vinil, permadani"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '3' ")
    lantai_parket_vinil_permadani = str(cur.fetchone()[0])
    """Lantai ubin, tegel, teraso"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '4' ")
    lantai_ubin_tegel_teraso = str(cur.fetchone()[0])
    """Lantai kayu kualitas bagus"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '5' ")
    lantai_kayu_papan_bagus = str(cur.fetchone()[0])
    """Lantai semen/bata"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '6' ")
    lantai_semen_bata = str(cur.fetchone()[0])
    """Lantai bambu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '7' ")
    lantai_bambu = str(cur.fetchone()[0])
    """Lantai kayu papan kualitas jelek"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '8' ")
    lantai_kayu_papan_jelek = str(cur.fetchone()[0])
    """Lantai tanah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '9' ")
    lantai_tanah = str(cur.fetchone()[0])
    """Lantai lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_lantai_terluas LIKE '10' ")
    lantai_lainnya = str(cur.fetchone()[0])

    """Jenis dinding"""
    """Dinding tembok"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '1' ")
    dinding_tembok = str(cur.fetchone()[0])
    """Dinding plesteran, kawat"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '2' ")
    dinding_plesteran_kawat = str(cur.fetchone()[0])
    """Dinding kayu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '3' ")
    dinding_kayu = str(cur.fetchone()[0])
    """Dinding anyaman bambu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '4' ")
    dinding_anyaman_bambu = str(cur.fetchone()[0])
    """Dinding batang kayu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '5' ")
    dinding_batang_kayu = str(cur.fetchone()[0])
    """Dinding bambu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '6' ")
    dinding_bambu = str(cur.fetchone()[0])
    """Dinding lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '7' ")
    dinding_lainnya = str(cur.fetchone()[0])

    """Insert to Database"""
    cur.execute("UPDATE `statistik_bangunan_kec` SET `lantai_marmer_granit`='"+lantai_marmer_granit+"', `lantai_keramik`='"+lantai_keramik+"', \
            `lantai_parket_vinil_permadani`='"+lantai_parket_vinil_permadani+"', `lantai_ubin_tegel_teraso`='"+lantai_ubin_tegel_teraso+"', \
            `lantai_kayu_papan_bagus`='"+lantai_kayu_papan_bagus+"', `lantai_semen_bata`='"+lantai_semen_bata+"', `lantai_bambu`='"+lantai_bambu+"',\
            `lantai_kayu_papan_jelek`='"+lantai_kayu_papan_jelek+"', `lantai_tanah`='"+lantai_tanah+"', `lantai_lainnya`='"+lantai_lainnya+"', \
            `dinding_tembok`='"+dinding_tembok+"', `dinding_plesteran_kawat`='"+dinding_plesteran_kawat+"', `dinding_kayu`='"+dinding_kayu+"',\
            `dinding_anyaman_bambu`='"+dinding_anyaman_bambu+"', `dinding_batang_kayu`='"+dinding_batang_kayu+"', `dinding_bambu`='"+dinding_bambu+"', \
            `dinding_lainnya`='"+dinding_lainnya+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Dinding kualitas baik"""
    """Tembok"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '1' AND kualitas_dinding123 LIKE '1' ")
    jenisdinding_tembok_baik = str(cur.fetchone()[0])
    """Plesteran anyaman"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '2' AND kualitas_dinding123 LIKE '1' ")
    jenisdinding_plesteran_kawat_baik = str(cur.fetchone()[0])
    """Tembok kayu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '3' AND kualitas_dinding123 LIKE '1' ")
    jenisdinding_kayu_baik = str(cur.fetchone()[0])

    """Dinding kualitas jelek"""
    """Tembok"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '1' AND kualitas_dinding123 LIKE '2' ")
    jenisdinding_tembok_jelek = str(cur.fetchone()[0])
    """Plesteran, anyaman"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '2' AND kualitas_dinding123 LIKE '2' ")
    jenisdinding_plesteran_kawat_jelek = str(cur.fetchone()[0])
    """Tembok kayu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_dinding_terluas LIKE '3' AND kualitas_dinding123 LIKE '2' ")
    jenisdinding_kayu_jelek = str(cur.fetchone()[0])

    """Insert to Database"""
    cur.execute("UPDATE `statistik_bangunan_kec` SET `jenisdinding_tembok_baik`='"+jenisdinding_tembok_baik+"', \
        `jenisdinding_plesteran_kawat_baik`='"+jenisdinding_plesteran_kawat_baik+"', `jenisdinding_kayu_baik`='"+jenisdinding_kayu_baik+"', \
        `jenisdinding_tembok_jelek`='"+jenisdinding_tembok_jelek+"', `jenisdinding_plesteran_kawat_jelek`='"+jenisdinding_plesteran_kawat_jelek+"', \
        `jenisdinding_kayu_jelek`='"+jenisdinding_kayu_jelek+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Jenis Atap"""
    """Genteng beton"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '1' ")
    atap_gentengbeton = str(cur.fetchone()[0])
    """Genteng keramik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '2' ")
    atap_gentengkeramik = str(cur.fetchone()[0])
    """Genteng metal"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '3' ")
    atap_gentengmetal = str(cur.fetchone()[0])
    """Genteng tanah liat"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '4' ")
    atap_gentengtanahliat = str(cur.fetchone()[0])
    """Asbes"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '5' ")
    atap_asbes = str(cur.fetchone()[0])
    """Seng"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '6' ")
    atap_seng = str(cur.fetchone()[0])
    """Sirap"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '7' ")
    atap_sirap = str(cur.fetchone()[0])
    """Bambu"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '8' ")
    atap_bambu = str(cur.fetchone()[0])
    """Jerami, ijuk, daun-daunan, rumbia"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '9' ")
    atap_jerami_ijuk_rumbia = str(cur.fetchone()[0])
    """Lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '10' ")
    atap_lainnya = str(cur.fetchone()[0])

    """Atap kualitas bagus"""
    """Genteng beton"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '1' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_gentengbeton_baik = str(cur.fetchone()[0])
    """Genteng keramik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '2' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_gentengkeramik_baik = str(cur.fetchone()[0])
    """Genteng metal"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '3' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_gentengmetal_baik = str(cur.fetchone()[0])
    """Genteng tanah liat"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '4' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_gentengtanahliat_baik = str(cur.fetchone()[0])
    """Asbes"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '5' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_asbes_baik = str(cur.fetchone()[0])
    """Seng"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '6' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_seng_baik = str(cur.fetchone()[0])
    """Sirap"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '7' AND kondisi_atap1234567 LIKE '1' ")
    jenisatap_sirap_baik = str(cur.fetchone()[0])


    """Atap kualitas jelek"""
    """Genteng beton"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '1' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_gentengbeton_jelek = str(cur.fetchone()[0])
    """Genteng keramik"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '2' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_gentengkeramik_jelek = str(cur.fetchone()[0])
    """Genteng metal"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '3' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_gentengmetal_jelek = str(cur.fetchone()[0])
    """Genteng tanah liat"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '4' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_gentengtanahliat_jelek = str(cur.fetchone()[0])
    """Asbes"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '5' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_asbes_jelek = str(cur.fetchone()[0])
    """Seng"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '6' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_seng_jelek = str(cur.fetchone()[0])
    """Sirap"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kec_id='"+a[0]+"' AND jenis_atap_terluas LIKE '7' AND kondisi_atap1234567 LIKE '2' ")
    jenisatap_sirap_jelek = str(cur.fetchone()[0])

    """Insert to Database"""
    cur.execute("UPDATE `statistik_bangunan_kec` SET `atap_gentengbeton`='"+atap_gentengbeton+"', `atap_gentengkeramik`='"+atap_gentengkeramik+"', \
            `atap_gentengmetal`='"+atap_gentengmetal+"', `atap_gentengtanahliat`='"+atap_gentengtanahliat+"', \
            `atap_asbes`='"+atap_asbes+"', `atap_seng`='"+atap_seng+"', `atap_sirap`='"+atap_sirap+"',\
            `atap_bambu`='"+atap_bambu+"', `atap_jerami_ijuk_rumbia`='"+atap_jerami_ijuk_rumbia+"', `atap_lainnya`='"+atap_lainnya+"', \
            `jenisatap_gentengbeton_baik`='"+jenisatap_gentengbeton_baik+"', `jenisatap_gentengkeramik_baik`='"+jenisatap_gentengkeramik_baik+"', \
            `jenisatap_gentengmetal_baik`='"+jenisatap_gentengmetal_baik+"', `jenisatap_gentengtanahliat_baik`='"+jenisatap_gentengtanahliat_baik+"', \
            `jenisatap_asbes_baik`='"+jenisatap_asbes_baik+"', `jenisatap_seng_baik`='"+jenisatap_seng_baik+"', \
            `jenisatap_sirap_baik`='"+jenisatap_sirap_baik+"', `jenisatap_gentengbeton_jelek`='"+jenisatap_gentengbeton_jelek+"', \
            `jenisatap_gentengkeramik_jelek`='"+jenisatap_gentengkeramik_jelek+"', `jenisatap_gentengmetal_jelek`='"+jenisatap_gentengmetal_jelek+"', \
            `jenisatap_gentengtanahliat_jelek`='"+jenisatap_gentengtanahliat_jelek+"', `jenisatap_asbes_jelek`='"+jenisatap_asbes_jelek+"', \
            `jenisatap_seng_jelek`='"+jenisatap_seng_jelek+"', `jenisatap_sirap_jelek`='"+jenisatap_sirap_jelek+"' WHERE id='"+a[0]+"' ")
    db.commit()
