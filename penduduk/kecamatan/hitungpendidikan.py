import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_pendidikan_kec` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    #Hitung_total_tdk_blm_sekolah IN('Tidak/Belum Sekolah','BELUM TAMAT SD/SEDERAJAT')
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Belum masuk TK/Kelompok Bermain','Tidak/Belum Sekolah','Tidak pernah sekolah','Sedang TK/Kelompok Bermain') ")
    pend1 = str(cur.fetchone()[0])
    #Hitung_total_tdk_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Belum Tamat SD/Sederajat','Sedang SD/sederajat','Tidak Tamat SD/Sederajat') ")
    pend2 = str(cur.fetchone()[0])
    #Hitung_total_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan='Tamat SD/Sederajat' ")
    pend3 = str(cur.fetchone()[0])
    #Hitung_total_sltp_sederajat Sedang SLTP/Sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Sedang SLTP/Sederajat','SLTP/Sederajat','Tamat SLTP/sederajat') ")
    pend4 = str(cur.fetchone()[0])
    #Hitung_total_slta_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('SLTA/Sederjat','SLTA/Sederajat','Sedang SLTA/sederajat','Tamat SLTA/sederajat') ")
    pend5 = str(cur.fetchone()[0])
    #Hitung_total_d1_d2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Diploma I/II','Tamat D-2/sederajat') ")
    pend6 = str(cur.fetchone()[0])
    #Hitung_total_akademi_d3_s_muda
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Akademi/Diploma III/S. Muda','AKADEMI/DIPLOMA III/SARJANA MUDA','Tamat D-3/sederajat','Tamat D-4/sederajat','Tamat D-3/sederajat') ")
    pend7 = str(cur.fetchone()[0])
    #Hitung_total_d4_s1 
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Diploma IV/Strata I','DIPLOMA-IV/STRATA-I','DilpomaIV/Strata','Sedang S-1/sederajat','Tamat S-1/sederajat')")
    pend8 = str(cur.fetchone()[0])
    #Hitung_total_s2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Strata II','Strata-II','Tamat S-2/sederajat') ")
    pend9 = str(cur.fetchone()[0])
    #Hitung_total_s3
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan IN ('Strata III','Strata-III','Sedang S-3/sederajat') ")
    pend10 = str(cur.fetchone()[0])
    #Hitung_total_pend_non_formal
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan='Pendidikan Non Formal' ")
    pend11 = str(cur.fetchone()[0])
    #Hitung_lk_tdk_blm_sekolah
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan  IN ('Belum masuk TK/Kelompok Bermain','Tidak/Belum Sekolah','Tidak pernah sekolah','Sedang TK/Kelompok Bermain') ")
    pend12 = str(cur.fetchone()[0])
    #Hitung_lk_tdk_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Belum Tamat SD/Sederajat','Sedang SD/sederajat','Tidak Tamat SD/Sederajat') ")
    pend13 = str(cur.fetchone()[0])
    #Hitung_lk_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan='Tamat SD/Sederajat' ")
    pend14 = str(cur.fetchone()[0])
    #Hitung_lk_sltp_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Sedang SLTP/Sederajat','SLTP/Sederajat','Tamat SLTP/sederajat') ")
    pend15 = str(cur.fetchone()[0])
    #Hitung_lk_slta_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('SLTA/Sederjat','SLTA/Sederajat','Sedang SLTA/sederajat','Tamat SLTA/sederajat') ")
    pend16 = str(cur.fetchone()[0])
    #Hitung_lk_d1_d2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Diploma I/II','Tamat D-2/sederajat') ")
    pend17 = str(cur.fetchone()[0])
    #Hitung_lk_akademi_d3_s_muda
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Akademi/Diploma III/S. Muda','AKADEMI/DIPLOMA III/SARJANA MUDA','Tamat D-3/sederajat','Tamat D-4/sederajat','Tamat D-3/sederajat') ")
    pend18 = str(cur.fetchone()[0])
    #Hitung_lk_d4_s1
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Diploma IV/Strata I','DIPLOMA-IV/STRATA-I','DilpomaIV/Strata','Sedang S-1/sederajat','Tamat S-1/sederajat')")
    pend19 = str(cur.fetchone()[0])
    #Hitung_lk_s2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Strata II','Strata-II','Tamat S-2/sederajat') ")
    pend20 = str(cur.fetchone()[0])
    #Hitung_lk_s3
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan IN ('Strata III','Strata-III','Sedang S-3/sederajat') ")
    pend21 = str(cur.fetchone()[0])
    #Hitung_lk_pend_non_formal
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan='Pendidikan Non Formal' ")
    pend22 = str(cur.fetchone()[0])
    #Hitung_pr_tdk_blm_sekolah
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Belum masuk TK/Kelompok Bermain','Tidak/Belum Sekolah','Tidak pernah sekolah','Sedang TK/Kelompok Bermain') ")
    pend23 = str(cur.fetchone()[0])
    #Hitung_pr_tdk_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Belum Tamat SD/Sederajat','Sedang SD/sederajat','Tidak Tamat SD/Sederajat') ")
    pend24 = str(cur.fetchone()[0])
    #Hitung_pr_tamat_sd_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan='Tamat SD/Sederajat' ")
    pend25 = str(cur.fetchone()[0])
    #Hitung_pr_sltp_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Sedang SLTP/Sederajat','SLTP/Sederajat','Tamat SLTP/sederajat') ")
    pend26 = str(cur.fetchone()[0])
    #Hitung_pr_slta_sederajat
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('SLTA/Sederjat','SLTA/Sederajat','Sedang SLTA/sederajat','Tamat SLTA/sederajat') ")
    pend27 = str(cur.fetchone()[0])
    #Hitung_pr_d1_d2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Diploma I/II','Tamat D-2/sederajat') ")
    pend28 = str(cur.fetchone()[0])
    #Hitung_pr_akademi_d3_s_muda  
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Akademi/Diploma III/S. Muda','AKADEMI/DIPLOMA III/SARJANA MUDA','Tamat D-3/sederajat','Tamat D-4/sederajat','Tamat D-3/sederajat') ")
    pend29 = str(cur.fetchone()[0])
    #Hitung_pr_d4_s1
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Diploma IV/Strata I','DIPLOMA-IV/STRATA-I','DilpomaIV/Strata','Sedang S-1/sederajat','Tamat S-1/sederajat') ")
    pend30 = str(cur.fetchone()[0])
    #Hitung_pr_s2
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Strata II','Strata-II','Tamat S-2/sederajat') ")
    pend31 = str(cur.fetchone()[0])
    #Hitung_pr_s3
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan IN ('Strata III','Strata-III','Sedang S-3/sederajat') ")
    pend32 = str(cur.fetchone()[0])
    #Hitung_pr_pend_non_formal
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan='Pendidikan Non Formal' ")
    pend33 = str(cur.fetchone()[0])
    #Total Data Pendidikan Kosong/Tidak Sesuai
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND pendidikan NOT IN ('Tidak/Belum Sekolah','Tidak Tamat SD/Sederajat','Tamat SD/Sederajat','SLTP/Sederajat','SLTA/Sederajat','Diploma I/II','Akademi/Diploma III/S. Muda','Diploma IV/Strata I','Strata II','Strata III','Pendidikan Non Formal','Belum Tamat SD/Sederajat','AKADEMI/DIPLOMA III/SARJANA MUDA','DIPLOMA-IV/STRATA-I','Strata-II','Strata-III','DilpomaIV/Strata I','SLTA/Sederjat','Belum masuk TK/Kelompok Bermain','Tamat SLTP/sederajat','Sedang SLTP/Sederajat','Sedang SLTA/sederajat','Sedang S-1/sederajat','Sedang SD/sederajat','Tamat SLTA/sederajat','Tidak pernah sekolah','Sedang TK/Kelompok Bermain','Tamat D-4/sederajat','Tamat S-1/sederajat','Tamat D-3/sederajat','Tamat S-2/sederajat','Sedang S-3/sederajat','Tamat D-2/sederajat') ")
    pend34 = str(cur.fetchone()[0])
    #Total Data Pendidikan Kosong/Tidak Sesuai (Laki-laki)
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND pendidikan NOT IN ('Tidak/Belum Sekolah','Tidak Tamat SD/Sederajat','Tamat SD/Sederajat','SLTP/Sederajat','SLTA/Sederajat','Diploma I/II','Akademi/Diploma III/S. Muda','Diploma IV/Strata I','Strata II','Strata III','Pendidikan Non Formal','Belum Tamat SD/Sederajat','AKADEMI/DIPLOMA III/SARJANA MUDA','DIPLOMA-IV/STRATA-I','Strata-II','Strata-III','DilpomaIV/Strata I','SLTA/Sederjat','Belum masuk TK/Kelompok Bermain','Tamat SLTP/sederajat','Sedang SLTP/Sederajat','Sedang SLTA/sederajat','Sedang S-1/sederajat','Sedang SD/sederajat','Tamat SLTA/sederajat','Tidak pernah sekolah','Sedang TK/Kelompok Bermain','Tamat D-4/sederajat','Tamat S-1/sederajat','Tamat D-3/sederajat','Tamat S-2/sederajat','Sedang S-3/sederajat','Tamat D-2/sederajat') ")
    pend35 = str(cur.fetchone()[0])
    #Total Data Pendidikan Kosong/Tidak Sesuai (Perempuan)
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND pendidikan NOT IN ('Tidak/Belum Sekolah','Tidak Tamat SD/Sederajat','Tamat SD/Sederajat','SLTP/Sederajat','SLTA/Sederajat','Diploma I/II','Akademi/Diploma III/S. Muda','Diploma IV/Strata I','Strata II','Strata III','Pendidikan Non Formal','Belum Tamat SD/Sederajat','AKADEMI/DIPLOMA III/SARJANA MUDA','DIPLOMA-IV/STRATA-I','Strata-II','Strata-III','DilpomaIV/Strata I','SLTA/Sederjat','Belum masuk TK/Kelompok Bermain','Tamat SLTP/sederajat','Sedang SLTP/Sederajat','Sedang SLTA/sederajat','Sedang S-1/sederajat','Sedang SD/sederajat','Tamat SLTA/sederajat','Tidak pernah sekolah','Sedang TK/Kelompok Bermain','Tamat D-4/sederajat','Tamat S-1/sederajat','Tamat D-3/sederajat','Tamat S-2/sederajat','Sedang S-3/sederajat','Tamat D-2/sederajat') ")
    pend36 = str(cur.fetchone()[0])
    #Eksekusi SQL
    cur.execute("UPDATE `statistik_pendidikan_kec` SET `total_tdk_blm_sekolah`='"+pend1+"', `total_tdk_tamat_sd_sederajat`='"+pend2+"', `total_tamat_sd_sederajat`='"+pend3+"', `total_sltp_sederajat`='"+pend4+"', `total_slta_sederajat`='"+pend5+"', `total_d1_d2`='"+pend6+"', `total_akademi_d3_s_muda`='"+pend7+"', `total_d4_s1`='"+pend8+"', `total_s2`='"+pend9+"', `total_s3`='"+pend10+"', `total_pend_non_formal`='"+pend11+"', `total_data_tdk_sesuai`='"+pend34+"', `lk_tdk_blm_sekolah`='"+pend12+"', `lk_tdk_tamat_sd_sederajat`='"+pend13+"', `lk_tamat_sd_sederajat`='"+pend14+"', `lk_sltp_sederajat`='"+pend15+"', `lk_slta_sederajat`='"+pend16+"', `lk_d1_d2`='"+pend17+"', `lk_akademi_d3_s_muda`='"+pend18+"', `lk_d4_s1`='"+pend19+"', `lk_s2`='"+pend20+"', `lk_s3`='"+pend21+"', `lk_pend_non_formal`='"+pend22+"', `lk_data_tdk_sesuai`='"+pend35+"', `pr_tdk_blm_sekolah`='"+pend23+"', `pr_tdk_tamat_sd_sederajat`='"+pend24+"', `pr_tamat_sd_sederajat`='"+pend25+"', `pr_sltp_sederajat`='"+pend26+"', `pr_slta_sederajat`='"+pend27+"', `pr_d1_d2`='"+pend28+"', `pr_akademi_d3_s_muda`='"+pend29+"', `pr_d4_s1`='"+pend30+"', `pr_s2`='"+pend31+"', `pr_s3`='"+pend32+"',  `pr_pend_non_formal`='"+pend33+"', `pr_data_tdk_sesuai`='"+pend36+"' WHERE `id`='"+a[0]+"' ")
    db.commit()
