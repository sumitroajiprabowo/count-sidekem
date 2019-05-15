import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `districts` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    """Anak Usia 5 Tahun keatas Partisipasi Sekolah"""
    """Tidak/Belum pernah sekolah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '0' AND umur>=5 ")
    lima_th_keatas_tdk_blm_pernah_sekolah = str(cur.fetchone()[0])
    """Masih sekolah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND umur>=5 ")
    lima_th_keatas_masih_sekolah = str(cur.fetchone()[0])
    """Tidak bersekolah lagi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND umur>=5 ")
    lima_th_keatas_tdk_sekolah_lagi = str(cur.fetchone()[0])
    """Insert to DB"""
    cur.execute("UPDATE `statistik_partisipasi_sekolah_kec` SET `5th_keatas_tdk_blm_pernah_sekolah`='"+lima_th_keatas_tdk_blm_pernah_sekolah+"', \
        `5th_keatas_masih_sekolah`='"+lima_th_keatas_masih_sekolah+"', `5th_keatas_tdk_sekolah_lagi`='"+lima_th_keatas_tdk_sekolah_lagi+"' WHERE id='"+a[0]+"' ")
    db.commit()

    """Partisipasi Sekolah ""Tidak Belum pernah"" sekolah Berdasarkan Umur"""
    """Usia 5-20 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '0' AND umur IN (5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20) ")
    lima_duapuluh_th_tdk_blm_pernah_sekolah = str(cur.fetchone()[0])
    """Usia 21-40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '0' AND umur IN (21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40) ")
    duasatu_empat_puluh_th_tdk_blm_pernah_sekolah = str(cur.fetchone()[0])
    """Usia diatas 40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '0' AND umur>40 ")
    lebihdari_empatpuluh_th_tdk_blm_pernah_sekolah = str(cur.fetchone()[0])


    """Partisipasi Sekolah ""Masih Bersekolah"" sekolah Berdasarkan Umur"""
    """Usia 5-20 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND umur IN (5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20) ")
    lima_duapuluh_th_masih_bersekolah = str(cur.fetchone()[0])
    """Usia 21-40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND umur IN (21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40) ")
    duasatu_empatpuluh_th_masih_bersekolah = str(cur.fetchone()[0])
    """Usia diatas 40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND umur>40 ")
    lebihdari_empatpuluh_th_masih_bersekolah = str(cur.fetchone()[0])

    """Partisipasi Sekolah ""Tidak Bersekolah lagi"" sekolah Berdasarkan Umur"""
    """Usia 5-20 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND umur IN (5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20) ")
    lima_duapuluh_th_tdk_bersekolah_lagi = str(cur.fetchone()[0])
    """Usia 21-40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND umur IN (21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40) ")
    duasatu_empatpuluh_th_tdk_bersekolah_lagi = str(cur.fetchone()[0])
    """Usia diatas 40 tahun"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND umur>40 ")
    lebihdari_empatpuluh_th_tdk_bersekolah_lagi = str(cur.fetchone()[0])
    """Insert to DB"""
    cur.execute("UPDATE `statistik_partisipasi_sekolah_kec` SET `5_20th_tdk_blm_pernah_sekolah`='"+lima_duapuluh_th_tdk_blm_pernah_sekolah+"', \
        `21_40th_tdk_blm_pernah_sekolah`='"+duasatu_empat_puluh_th_tdk_blm_pernah_sekolah+"', `>40_th_tdk_blm_pernah_sekolah`='"+lebihdari_empatpuluh_th_tdk_blm_pernah_sekolah+"', \
        `5_20th_masih_bersekolah`='"+lima_duapuluh_th_masih_bersekolah+"', `21_40th_masih_bersekolah`='"+duasatu_empatpuluh_th_masih_bersekolah+"', \
        `>40_th_masih_bersekolah`='"+lebihdari_empatpuluh_th_masih_bersekolah+"', `5_20th_tdk_bersekolah_lagi`='"+lima_duapuluh_th_tdk_bersekolah_lagi+"', \
        `21_40th_tdk_bersekolah_lagi`='"+duasatu_empatpuluh_th_tdk_bersekolah_lagi+"', `>40_th_tdk_bersekolah_lagi`='"+lebihdari_empatpuluh_th_tdk_bersekolah_lagi+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Jenjang Pendidikan Tertinggi Yang Sedang/Pernah Diduduki"""
    """Masih bersekolah SD"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '1' ")
    masih_sekolah_sd = str(cur.fetchone()[0])
    """Masih bersekolah Paket A"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '2' ")
    masih_sekolah_paket_a = str(cur.fetchone()[0])
    """Masih bersekolah M. Ibtidaiyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '3' ")
    masih_sekolah_m_ibtidaiyah = str(cur.fetchone()[0])
    """Masih bersekolah SMP/SMPLB"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '4' ")
    masih_sekolah_smp_smplb = str(cur.fetchone()[0])
    """Masih bersekolah Paket B"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '5' ")
    masih_sekolah_paket_b = str(cur.fetchone()[0])
    """Masih bersekolah M.Tsanawiyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '6' ")
    masih_sekolah_m_tsanawiyah = str(cur.fetchone()[0])
    """Masih bersekolah SMA/SMK/SMALB"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '7' ")
    masih_sekolah_sma_smk_smalb = str(cur.fetchone()[0])
    """Masih bersekolah Paket C"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '8' ")
    masih_sekolah_paket_c = str(cur.fetchone()[0])
    """Masih bersekolah M.Aliyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '9' ")
    masih_sekolah_m_aliyah = str(cur.fetchone()[0])
    """Masih bersekolah di perguruan tinggi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '10' ")
    masih_sekolah_perguruan_tinggi = str(cur.fetchone()[0])


    """Jenjang Pendidikan Tertinggi Anak yang tidak bersekolah lagi"""
    """Pendidikan tertinggi SD"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '1' ")
    pddkn_tertinggi_sd = str(cur.fetchone()[0])
    """Pendidikan tertinggi Paket A"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '2' ")
    pddkn_tertinggi_paket_a = str(cur.fetchone()[0])
    """Pendidikan tertinggi M. Ibtidaiyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '3' ")
    pddkn_tertinggi_m_ibtidaiyah = str(cur.fetchone()[0])
    """Pendidikan tertingggi SMP"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '4' ")
    pddkn_tertinggi_smp_smplb = str(cur.fetchone()[0])
    """Pendidikan tertinggi Paket"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '5' ")
    pddkn_tertinggi_paket_b = str(cur.fetchone()[0])
    """Pendidikan tertinggi M.Tsanawiyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '6' ")
    pddkn_tertinggi_m_tsanawiyah = str(cur.fetchone()[0])
    """Pendidikan tertinggi SMA/SMK/SMALB"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '7' ")
    pddkn_tertinggi_sma_smk_smalb = str(cur.fetchone()[0])
    """Pendidikan tertinggi Paket C"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '8' ")
    pddkn_tertinggi_paket_c = str(cur.fetchone()[0])
    """Pendidikan tertinggi M. Aliyah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '9' ")
    pddkn_tertinggi_m_aliyah = str(cur.fetchone()[0])
    """Pendidikan tertinggi perguruan tinggi"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_jenjang_pendidikan_tertinggi LIKE '10' ")
    pddkn_tertinggi_perguruan_tinggi = str(cur.fetchone()[0])
    cur.execute("UPDATE `statistik_partisipasi_sekolah_kec` SET `masih_sekolah_sd`='"+masih_sekolah_sd+"', \
        `masih_sekolah_paket_a`='"+masih_sekolah_paket_a+"', `masih_sekolah_m_ibtidaiyah`='"+masih_sekolah_m_ibtidaiyah+"', \
        `masih_sekolah_smp_smplb`='"+masih_sekolah_smp_smplb+"', `masih_sekolah_paket_b`='"+masih_sekolah_paket_b+"', \
        `masih_sekolah_m_tsanawiyah`='"+masih_sekolah_m_tsanawiyah+"', `masih_sekolah_sma_smk_smalb`='"+masih_sekolah_sma_smk_smalb+"', \
        `masih_sekolah_paket_c`='"+masih_sekolah_paket_c+"', `masih_sekolah_m_aliyah`='"+masih_sekolah_m_aliyah+"', \
        `masih_sekolah_perguruan_tinggi`='"+masih_sekolah_perguruan_tinggi+"', `pddkn_tertinggi_sd`='"+pddkn_tertinggi_sd+"', \
        `pddkn_tertinggi_paket_a`='"+pddkn_tertinggi_paket_a+"', `pddkn_tertinggi_m_ibtidaiyah`='"+pddkn_tertinggi_m_ibtidaiyah+"', \
        `pddkn_tertinggi_smp_smplb`='"+pddkn_tertinggi_smp_smplb+"', `pddkn_tertinggi_paket_b`='"+pddkn_tertinggi_paket_b+"', \
        `pddkn_tertinggi_m_tsanawiyah`='"+pddkn_tertinggi_m_tsanawiyah+"', `pddkn_tertinggi_sma_smk_smalb`='"+pddkn_tertinggi_sma_smk_smalb+"', \
        `pddkn_tertinggi_paket_c`='"+pddkn_tertinggi_paket_c+"', `pddkn_tertinggi_m_aliyah`='"+pddkn_tertinggi_m_aliyah+"', \
        `pddkn_tertinggi_perguruan_tinggi`='"+pddkn_tertinggi_perguruan_tinggi+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Jenjang Kelas Tertinggi yang pernah diduduki untuk anak yang masih bersekolah"""
    """Masih bersekolah Kelas tertinggi kelas 1"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '1' ")
    msh_sekolah_kls_tertinggi_1 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 2"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '2' ")
    msh_sekolah_kls_tertinggi_2 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '3' ")
    msh_sekolah_kls_tertinggi_3 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 4"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '4' ")
    msh_sekolah_kls_tertinggi_4 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 5"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '5' ")
    msh_sekolah_kls_tertinggi_5 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 6"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '6' ")
    msh_sekolah_kls_tertinggi_6 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 7"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '7' ")
    msh_sekolah_kls_tertinggi_7 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 8"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '8' ")
    msh_sekolah_kls_tertinggi_8 = str(cur.fetchone()[0])
    """Masih bersekolah Kelas tertinggi kelas 9"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '9' ")
    msh_sekolah_kls_tertinggi_9 = str(cur.fetchone()[0])

    """Jenjang Kelas Tertinggi yang pernah diduduki untuk anak yang tidak bersekolah lagi"""
    """Tidak bersekolah lagi, kelas tertinggi kelas 1"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '1' ")
    tdk_sekolah_lagi_kls_tertinggi_1 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 2"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '2' ")
    tdk_sekolah_lagi_kls_tertinggi_2 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '3' ")
    tdk_sekolah_lagi_kls_tertinggi_3 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 4"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '4' ")
    tdk_sekolah_lagi_kls_tertinggi_4 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 5"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '5' ")
    tdk_sekolah_lagi_kls_tertinggi_5 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 6"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '6' ")
    tdk_sekolah_lagi_kls_tertinggi_6 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 7"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_kelas_tertinggi LIKE '7' ")
    tdk_sekolah_lagi_kls_tertinggi_7 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 8"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '8' ")
    tdk_sekolah_lagi_kls_tertinggi_8 = str(cur.fetchone()[0])
    """Tidak bersekolah lagi, kelas tertinggi kelas 9"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' AND \
        5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_kelas_tertinggi LIKE '9' ")
    tdk_sekolah_lagi_kls_tertinggi_9 = str(cur.fetchone()[0])
    """Insert to DB"""
    cur.execute("UPDATE `statistik_partisipasi_sekolah_kec` SET `msh_sekolah_kls_tertinggi_1`='"+msh_sekolah_kls_tertinggi_1+"', \
        `msh_sekolah_kls_tertinggi_2`='"+msh_sekolah_kls_tertinggi_2+"', `msh_sekolah_kls_tertinggi_3`='"+msh_sekolah_kls_tertinggi_3+"', \
        `msh_sekolah_kls_tertinggi_4`='"+msh_sekolah_kls_tertinggi_4+"', `msh_sekolah_kls_tertinggi_5`='"+msh_sekolah_kls_tertinggi_5+"', \
        `msh_sekolah_kls_tertinggi_6`='"+msh_sekolah_kls_tertinggi_6+"', `msh_sekolah_kls_tertinggi_7`='"+msh_sekolah_kls_tertinggi_7+"', \
        `msh_sekolah_kls_tertinggi_8`='"+msh_sekolah_kls_tertinggi_8+"', `msh_sekolah_kls_tertinggi_9`='"+msh_sekolah_kls_tertinggi_9+"', \
        `tdk_sekolah_lagi_kls_tertinggi_1`='"+tdk_sekolah_lagi_kls_tertinggi_1+"', `tdk_sekolah_lagi_kls_tertinggi_2`='"+tdk_sekolah_lagi_kls_tertinggi_2+"', \
        `tdk_sekolah_lagi_kls_tertinggi_3`='"+tdk_sekolah_lagi_kls_tertinggi_3+"', `tdk_sekolah_lagi_kls_tertinggi_4`='"+tdk_sekolah_lagi_kls_tertinggi_4+"', \
        `tdk_sekolah_lagi_kls_tertinggi_5`='"+tdk_sekolah_lagi_kls_tertinggi_5+"', `tdk_sekolah_lagi_kls_tertinggi_6`='"+tdk_sekolah_lagi_kls_tertinggi_6+"', \
        `tdk_sekolah_lagi_kls_tertinggi_7`='"+tdk_sekolah_lagi_kls_tertinggi_7+"', `tdk_sekolah_lagi_kls_tertinggi_8`='"+tdk_sekolah_lagi_kls_tertinggi_8+"', \
        `tdk_sekolah_lagi_kls_tertinggi_9`='"+tdk_sekolah_lagi_kls_tertinggi_9+"' WHERE id='"+a[0]+"' ")
    db.commit()


    """Ijazah Pendidikan Tertinggi anak masih bersekolah"""
    """Masih sekolah tidak punya ijazah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '0' ")
    msh_sekolah_tdk_punya_ijazah = str(cur.fetchone()[0])
    """Masih sekolah ijazah SD"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '1' ")
    msh_sekolah_ijazah_sd = str(cur.fetchone()[0])
    """Masih sekolah ijazah SMP"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '2' ")
    msh_sekolah_ijazah_smp = str(cur.fetchone()[0])
    """Masih sekolah ijazah SMA"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '3' ")
    msh_sekolah_ijazah_sma = str(cur.fetchone()[0])
    """Masih sekolah ijazah D1, D2 danD3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '4' ")
    msh_sekolah_ijazah_d1_d2_d3 = str(cur.fetchone()[0])
    """Masih sekolah ijazah D4 dan S1"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '5' ")
    msh_sekolah_ijazah_d4_s1 = str(cur.fetchone()[0])
    """Masih sekolah ijazah S2 dan S3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '1' AND 5th_keatas_ijazah_tertinggi LIKE '6' ")
    msh_sekolah_ijazah_s2_s3 = str(cur.fetchone()[0])

    """Ijazah Pendidikan Tertinggi yang dimiliki anak tidak bersekolah lagi"""
    """Sudah tidak bersekolah, tidak punya ijazah"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '0' ")
    tdk_sekolah_lagi_tdk_punya_ijazah = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah SD"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '1' ")
    tdk_sekolah_lagi_ijazah_sd = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah SMP"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '2' ")
    tdk_sekolah_lagi_ijazah_smp = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah SMA"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '3' ")
    tdk_sekolah_lagi_ijazah_sma = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah D1,D2 dan D3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '4' ")
    tdk_sekolah_lagi_ijazah_d1_d2_d3 = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah D4 dan S1"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '5' ")
    tdk_sekolah_lagi_ijazah_d4_s1 = str(cur.fetchone()[0])
    """Sudah tidak bersekolah, ijazah S2 dan S3"""
    cur.execute("SELECT COUNT(*) FROM `bdt_rumahtangga-33`  WHERE kec_id='"+a[0]+"' \
        AND 5th_keatas_partisipasi_sekolah LIKE '2' AND 5th_keatas_ijazah_tertinggi LIKE '6' ")
    tdk_sekolah_lagi_ijazah_s2_s3 = str(cur.fetchone()[0])
    """Insert to DB"""
    cur.execute("UPDATE `statistik_partisipasi_sekolah_kec` SET `msh_sekolah_tdk_punya_ijazah`='"+msh_sekolah_tdk_punya_ijazah+"', \
        `msh_sekolah_ijazah_sd`='"+msh_sekolah_ijazah_sd+"', `msh_sekolah_ijazah_smp`='"+msh_sekolah_ijazah_smp+"', \
        `msh_sekolah_ijazah_sma`='"+msh_sekolah_ijazah_sma+"', `msh_sekolah_ijazah_d1_d2_d3`='"+msh_sekolah_ijazah_d1_d2_d3+"', \
        `msh_sekolah_ijazah_d4_s1`='"+msh_sekolah_ijazah_d4_s1+"', `msh_sekolah_ijazah_s2_s3`='"+msh_sekolah_ijazah_s2_s3+"', \
        `tdk_sekolah_lagi_tdk_punya_ijazah`='"+tdk_sekolah_lagi_tdk_punya_ijazah+"', `tdk_sekolah_lagi_ijazah_sd`='"+tdk_sekolah_lagi_ijazah_sd+"', \
        `tdk_sekolah_lagi_ijazah_smp`='"+tdk_sekolah_lagi_ijazah_smp+"', `tdk_sekolah_lagi_ijazah_sma`='"+tdk_sekolah_lagi_ijazah_sma+"', \
        `tdk_sekolah_lagi_ijazah_d1_d2_d3`='"+tdk_sekolah_lagi_ijazah_d1_d2_d3+"', `tdk_sekolah_lagi_ijazah_d4_s1`='"+tdk_sekolah_lagi_ijazah_d4_s1+"', \
        `tdk_sekolah_lagi_ijazah_s2_s3`='"+tdk_sekolah_lagi_ijazah_s2_s3+"' WHERE id='"+a[0]+"' ")
    db.commit()
