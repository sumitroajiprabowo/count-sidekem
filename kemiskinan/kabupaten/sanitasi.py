import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `regencies` WHERE id LIKE '3327' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    """Count Sumber Air Ngecer"""
    """air_kemasan_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '1' AND cara_memperloleh_air_minum LIKE '1' ")
    air_kemasan_eceran = str(cur.fetchone()[0])
    """air_isi_ulang_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '2' AND cara_memperloleh_air_minum LIKE '1' ")
    air_isi_ulang_eceran = str(cur.fetchone()[0])
    """leding_meteran_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '3' AND cara_memperloleh_air_minum LIKE '1' ")
    leding_meteran_eceran = str(cur.fetchone()[0])
    """leding_eceran_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '4' AND cara_memperloleh_air_minum LIKE '1' ")
    leding_eceran_eceran = str(cur.fetchone()[0])
    """sumur_bor_pompa_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '5' AND cara_memperloleh_air_minum LIKE '1' ")
    sumur_bor_pompa_eceran = str(cur.fetchone()[0])
    """sumur_terlindung_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '6' AND cara_memperloleh_air_minum LIKE '1' ")
    sumur_terlindung_eceran = str(cur.fetchone()[0])
    """sumur_tak_terlindung_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '7' AND cara_memperloleh_air_minum LIKE '1' ")
    sumur_tak_terlindung_eceran = str(cur.fetchone()[0])
    """mata_air_terlindung_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '8' AND cara_memperloleh_air_minum LIKE '1' ")
    mata_air_terlindung_eceran = str(cur.fetchone()[0])
    """mata_air_tak_terlindung_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '9' AND cara_memperloleh_air_minum LIKE '1' ")
    mata_air_tak_terlindung_eceran = str(cur.fetchone()[0])
    """air_sungai_danau_waduk_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '10' AND cara_memperloleh_air_minum LIKE '1' ")
    air_sungai_danau_waduk_eceran = str(cur.fetchone()[0])
    """air_hujan_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '11' AND cara_memperloleh_air_minum LIKE '1' ")
    air_hujan_eceran = str(cur.fetchone()[0])
    """lainnya_eceran"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '12' AND cara_memperloleh_air_minum LIKE '1' ")
    lainnya_eceran = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `air_kemasan_eceran`='"+air_kemasan_eceran+"', `air_isi_ulang_eceran`='"+air_isi_ulang_eceran+"', \
        `leding_meteran_eceran`='"+leding_meteran_eceran+"', `leding_eceran_eceran`='"+leding_eceran_eceran+"', `sumur_bor_pompa_eceran`='"+sumur_bor_pompa_eceran+"', \
        `sumur_terlindung_eceran`='"+sumur_terlindung_eceran+"', `sumur_tak_terlindung_eceran`='"+sumur_tak_terlindung_eceran+"', `mata_air_terlindung_eceran`='"+mata_air_terlindung_eceran+"', \
        `mata_air_tak_terlindung_eceran`='"+mata_air_tak_terlindung_eceran+"', `air_sungai_danau_waduk_eceran`='"+air_sungai_danau_waduk_eceran+"', \
        `air_hujan_eceran`='"+air_hujan_eceran+"', `lainnya_eceran`='"+lainnya_eceran+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Counting Sumber Air Langganan"""
    """air_kemasan_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '1' AND cara_memperloleh_air_minum LIKE '2' ")
    air_kemasan_langganan = str(cur.fetchone()[0])
    """air_isi_ulang_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '2' AND cara_memperloleh_air_minum LIKE '2' ")
    air_isi_ulang_langganan = str(cur.fetchone()[0])
    """leding_meteran_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '3' AND cara_memperloleh_air_minum LIKE '2' ")
    leding_meteran_langganan = str(cur.fetchone()[0])
    """leding_eceran_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '4' AND cara_memperloleh_air_minum LIKE '2' ")
    leding_eceran_langganan = str(cur.fetchone()[0])
    """sumur_bor_pompa_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '5' AND cara_memperloleh_air_minum LIKE '2' ")
    sumur_bor_pompa_langganan = str(cur.fetchone()[0])
    """sumur_terlindung_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '6' AND cara_memperloleh_air_minum LIKE '2' ")
    sumur_terlindung_langganan = str(cur.fetchone()[0])
    """sumur_tak_terlindung_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '7' AND cara_memperloleh_air_minum LIKE '2' ")
    sumur_tak_terlindung_langganan = str(cur.fetchone()[0])
    """mata_air_terlindung_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '8' AND cara_memperloleh_air_minum LIKE '2' ")
    mata_air_terlindung_langganan = str(cur.fetchone()[0])
    """mata_air_tak_terlindung_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '9' AND cara_memperloleh_air_minum LIKE '2' ")
    mata_air_tak_terlindung_langganan = str(cur.fetchone()[0])
    """air_sungai_danau_waduk_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '10' AND cara_memperloleh_air_minum LIKE '2' ")
    air_sungai_danau_waduk_langganan = str(cur.fetchone()[0])
    """air_hujan_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '11' AND cara_memperloleh_air_minum LIKE '2' ")
    air_hujan_langganan = str(cur.fetchone()[0])
    """lainnya_langganan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '12' AND cara_memperloleh_air_minum LIKE '2' ")
    lainnya_langganan = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `air_kemasan_langganan`='"+air_kemasan_langganan+"', `air_isi_ulang_langganan`='"+air_isi_ulang_langganan+"', \
        `leding_meteran_langganan`='"+leding_meteran_langganan+"', `leding_eceran_langganan`='"+leding_eceran_langganan+"', `sumur_bor_pompa_langganan`='"+sumur_bor_pompa_langganan+"', \
        `sumur_terlindung_langganan`='"+sumur_terlindung_langganan+"', `sumur_tak_terlindung_langganan`='"+sumur_tak_terlindung_langganan+"', `mata_air_terlindung_langganan`='"+mata_air_terlindung_langganan+"', \
        `mata_air_tak_terlindung_langganan`='"+mata_air_tak_terlindung_langganan+"', `air_sungai_danau_waduk_langganan`='"+air_sungai_danau_waduk_langganan+"', \
        `air_hujan_langganan`='"+air_hujan_langganan+"', `lainnya_langganan`='"+lainnya_langganan+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Counting Sumber Air Tidak Membeli"""
    """air_kemasan_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '1' AND cara_memperloleh_air_minum LIKE '3' ")
    air_kemasan_tdk_beli = str(cur.fetchone()[0])
    """air_isi_ulang_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '2' AND cara_memperloleh_air_minum LIKE '3' ")
    air_isi_ulang_tdk_beli = str(cur.fetchone()[0])
    """leding_meteran_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '3' AND cara_memperloleh_air_minum LIKE '3' ")
    leding_meteran_tdk_beli = str(cur.fetchone()[0])
    """leding_eceran_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '4' AND cara_memperloleh_air_minum LIKE '3' ")
    leding_eceran_tdk_beli = str(cur.fetchone()[0])
    """sumur_bor_pompa_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '5' AND cara_memperloleh_air_minum LIKE '3' ")
    sumur_bor_pompa_tdk_beli = str(cur.fetchone()[0])
    """sumur_terlindung_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '6' AND cara_memperloleh_air_minum LIKE '3' ")
    sumur_terlindung_tdk_beli = str(cur.fetchone()[0])
    """sumur_tak_terlindung_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '7' AND cara_memperloleh_air_minum LIKE '3' ")
    sumur_tak_terlindung_tdk_beli = str(cur.fetchone()[0])
    """mata_air_terlindung_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '8' AND cara_memperloleh_air_minum LIKE '3' ")
    mata_air_terlindung_tdk_beli = str(cur.fetchone()[0])
    """mata_air_tak_terlindung_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '9' AND cara_memperloleh_air_minum LIKE '3' ")
    mata_air_tak_terlindung_tdk_beli = str(cur.fetchone()[0])
    """air_sungai_danau_waduk_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '10' AND cara_memperloleh_air_minum LIKE '3' ")
    air_sungai_danau_waduk_tdk_beli = str(cur.fetchone()[0])
    """air_hujan_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '11' AND cara_memperloleh_air_minum LIKE '3' ")
    air_hujan_tdk_beli = str(cur.fetchone()[0])
    """lainnya_tdk_beli"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' \
        AND sumber_air_minum LIKE '12' AND cara_memperloleh_air_minum LIKE '3' ")
    lainnya_tdk_beli = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `air_kemasan_tdk_beli`='"+air_kemasan_tdk_beli+"', `air_isi_ulang_tdk_beli`='"+air_isi_ulang_tdk_beli+"', \
        `leding_meteran_tdk_beli`='"+leding_meteran_tdk_beli+"', `leding_eceran_tdk_beli`='"+leding_eceran_tdk_beli+"', `sumur_bor_pompa_tdk_beli`='"+sumur_bor_pompa_tdk_beli+"', \
        `sumur_terlindung_tdk_beli`='"+sumur_terlindung_tdk_beli+"', `sumur_tak_terlindung_tdk_beli`='"+sumur_tak_terlindung_tdk_beli+"', `mata_air_terlindung_tdk_beli`='"+mata_air_terlindung_tdk_beli+"', \
        `mata_air_tak_terlindung_tdk_beli`='"+mata_air_tak_terlindung_tdk_beli+"', `air_sungai_danau_waduk_tdk_beli`='"+air_sungai_danau_waduk_tdk_beli+"', \
        `air_hujan_tdk_beli`='"+air_hujan_tdk_beli+"', `lainnya_tdk_beli`='"+lainnya_tdk_beli+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Count Total Penggunaan Sumber Air"""
    """air_kemasan_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '1' ")
    air_kemasan_total = str(cur.fetchone()[0])
    """air_isi_ulang_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '2' ")
    air_isi_ulang_total = str(cur.fetchone()[0])
    """leding_meteran_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '3' ")
    leding_meteran_total = str(cur.fetchone()[0])
    """leding_eceran_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '4' ")
    leding_eceran_total = str(cur.fetchone()[0])
    """sumur_bor_pompa_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '5' ")
    sumur_bor_pompa_total = str(cur.fetchone()[0])
    """sumur_terlindung_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '6' ")
    sumur_terlindung_total = str(cur.fetchone()[0])
    """sumur_tak_terlindung_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '7' ")
    sumur_tak_terlindung_total = str(cur.fetchone()[0])
    """mata_air_terlindung_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '8' ")
    mata_air_terlindung_total = str(cur.fetchone()[0])
    """mata_air_tak_terlindung_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '9' ")
    mata_air_tak_terlindung_total = str(cur.fetchone()[0])
    """air_sungai_danau_waduk_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '10' ")
    air_sungai_danau_waduk_total = str(cur.fetchone()[0])
    """air_hujan_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '11' ")
    air_hujan_total = str(cur.fetchone()[0])
    """lainnya_total"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND sumber_air_minum LIKE '12' ")
    lainnya_total = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `air_kemasan_total`='"+air_kemasan_total+"', `air_isi_ulang_total`='"+air_isi_ulang_total+"', \
        `leding_meteran_total`='"+leding_meteran_total+"', `leding_eceran_total`='"+leding_eceran_total+"', `sumur_bor_pompa_total`='"+sumur_bor_pompa_total+"', \
        `sumur_terlindung_total`='"+sumur_terlindung_total+"', `sumur_tak_terlindung_total`='"+sumur_tak_terlindung_total+"', `mata_air_terlindung_total`='"+mata_air_terlindung_total+"', \
        `mata_air_tak_terlindung_total`='"+mata_air_tak_terlindung_total+"', `air_sungai_danau_waduk_total`='"+air_sungai_danau_waduk_total+"', \
        `air_hujan_total`='"+air_hujan_total+"', `lainnya_total`='"+lainnya_total+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Counting Fasilitas BAB"""
    """fasilitas_bab_sendiri"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND fasilitas_bab LIKE '1' ")
    fasilitas_bab_sendiri = str(cur.fetchone()[0])
    """fasilitas_bab_umum"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND fasilitas_bab LIKE '2' ")
    fasilitas_bab_umum = str(cur.fetchone()[0])
    """fasilitas_bab_bersama"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND fasilitas_bab LIKE '3' ")
    fasilitas_bab_bersama = str(cur.fetchone()[0])
    """fasilitas_bab_tdk_ada"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND fasilitas_bab LIKE '4' ")
    fasilitas_bab_tdk_ada = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `fasilitas_bab_sendiri`='"+fasilitas_bab_sendiri+"', \
        `fasilitas_bab_umum`='"+fasilitas_bab_umum+"', `fasilitas_bab_bersama`='"+fasilitas_bab_bersama+"', \
        `fasilitas_bab_tdk_ada`='"+fasilitas_bab_tdk_ada+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Counting Jenis Kloset"""
    """jenis_kloset_leher_angsa"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND jenis_kloset LIKE '1' ")
    jenis_kloset_leher_angsa = str(cur.fetchone()[0])
    """jenis_kloset_plengsengan"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND jenis_kloset LIKE '2' ")
    jenis_kloset_plengsengan = str(cur.fetchone()[0])
    """jenis_kloset_cemplung/cubluk"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND jenis_kloset LIKE '3' ")
    jenis_kloset_cemplungcubluk = str(cur.fetchone()[0])
    """jenis_kloset_tdk_pakai"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND jenis_kloset LIKE '4' ")
    jenis_kloset_tdk_pakai = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `jenis_kloset_leher_angsa`='"+jenis_kloset_leher_angsa+"', \
        `jenis_kloset_plengsengan`='"+jenis_kloset_plengsengan+"', `jenis_kloset_cemplung/cubluk`='"+jenis_kloset_cemplungcubluk+"', \
        `jenis_kloset_tdk_pakai`='"+jenis_kloset_tdk_pakai+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Counting TPA"""
    """pembuangan_tangki"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '1' ")
    pembuangan_tangki = str(cur.fetchone()[0])
    """pembuangan_spal"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '2' ")
    pembuangan_spal = str(cur.fetchone()[0])
    """pembuangan_lubang_tanah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '3' ")
    pembuangan_lubang_tanah = str(cur.fetchone()[0])
    """pembuangan_kolamsawahsungaidanaulaut"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '4' ")
    pembuangan_kolamsawahsungaidanaulaut = str(cur.fetchone()[0])
    """pembuangan_pantai_tanahlapang_kebun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '5' ")
    pembuangan_pantai_tanahlapang_kebun = str(cur.fetchone()[0])
    """pembuangan_lainnya"""
    cur.execute("SELECT COUNT(*) FROM `bdt_kemiskinan-33`  WHERE kab_id='"+a[0]+"' AND tpa_tinja LIKE '6' ")
    pembuangan_lainnya = str(cur.fetchone()[0])
    """insert to sql"""
    cur.execute("UPDATE `statistik_sanitasi_kab` SET `pembuangan_tangki`='"+pembuangan_tangki+"', \
        `pembuangan_spal`='"+pembuangan_spal+"', `pembuangan_lubang_tanah`='"+pembuangan_lubang_tanah+"', \
        `pembuangan_kolamsawahsungaidanaulaut`='"+pembuangan_kolamsawahsungaidanaulaut+"', \
        `pembuangan_pantai_tanahlapang_kebun`='"+pembuangan_pantai_tanahlapang_kebun+"', \
        `pembuangan_lainnya`='"+pembuangan_lainnya+"' WHERE id='"+a[0]+"' ")
    db.commit()