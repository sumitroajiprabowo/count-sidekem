import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_agama_kec` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    #Total Islam
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND `agama` LIKE 'Islam' ")
    agama1 = str(cur.fetchone()[0])
    #Total Kristen, Protestan, Kristen Protestan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama IN ('Kristen','Protestan','Kristen Protestan') ")
    agama2 = str(cur.fetchone()[0])
    #Total Katholik, Kristen Katolik, Katolik
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama IN ('Katholik','Kristen Katolik','Katolik') ")
    agama3 = str(cur.fetchone()[0])
    #Total Budha
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama LIKE 'Budha' ")
    agama4 = str(cur.fetchone()[0])
    #Total Hindu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama LIKE 'Hindu' ")
    agama5 = str(cur.fetchone()[0])
    #Total Konghuchu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama IN ('Aliran Khonghuchu','Konghuchu, Khonghucu') ")
    agama6 = str(cur.fetchone()[0])
    #Total Aliran Kepercayaan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama IN ('Aliran Kepercayaan','Kepercayaan', 'Aliran Ke-percayaan', 'KEPERCAYAAN TERHADAP TUHAN YANG MAHA ESA') ")
    agama7 = str(cur.fetchone()[0])
    #Total Agama Lainnya
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND agama NOT IN ('Islam','Kristen','Protestan','Kristen Protestan','Katholik','Kristen Katolik','Katolik','Hindu','Budha','Konghuchu','Aliran Kepercayaan','Kepercayaan','Khonghuchu','Khonghucu','Aliran Ke-percayaan') ")
    agama8 = str(cur.fetchone()[0])
    #Total Laki-laki Islam
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama LIKE 'Islam' ")
    agama9 = str(cur.fetchone()[0])
    #Total Laki-laki Kristen, Protestan, Kristen Protestan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama IN ('Kristen','Protestan','Kristen Protestan') ")
    agama10 = str(cur.fetchone()[0])
    #Total Laki-laki Katholik, Kristen Katolik, Katolik
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama IN ('Katholik','Kristen Katolik','Katolik') ")
    agama11 = str(cur.fetchone()[0])
    #Total laki-laki Budha
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama LIKE 'Budha' ")
    agama12 = str(cur.fetchone()[0])
    #Total Laki-laki Hindu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama LIKE 'Hindu' ")
    agama13 = str(cur.fetchone()[0])
    #Total Laki-laki Konghuchu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama IN ('Aliran Khonghuchu','Konghuchu, Khonghucu') ")
    agama14 = str(cur.fetchone()[0])
    #total Laki-laki Aliran Kepercayaan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama IN ('Aliran Kepercayaan','Kepercayaan', 'Aliran Ke-percayaan', 'KEPERCAYAAN TERHADAP TUHAN YANG MAHA ESA') ")
    agama15 = str(cur.fetchone()[0])
    #Total Laki-laki Agama Lainnya
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND agama NOT IN ('Islam','Kristen','Protestan','Kristen Protestan','Katholik','Kristen Katolik','Katolik','Hindu','Budha','Konghuchu','Aliran Kepercayaan','Kepercayaan','Khonghuchu','Khonghucu','Aliran Ke-percayaan') ")
    agama16 = str(cur.fetchone()[0])
    #Total Perempuan Islam
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama LIKE 'Islam' ")
    agama17 = str(cur.fetchone()[0])
    #Total Perempuan Kristen, Protestan, Kristen Protestan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama IN ('Kristen','Protestan','Kristen Protestan') ")
    agama18 = str(cur.fetchone()[0])
    #Total Perempuan Katholik, Kristen Katolik, Katolik
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama IN ('Katholik','Kristen Katolik','Katolik') ")
    agama19 = str(cur.fetchone()[0])
    #Total Perempuan Budha
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama LIKE 'Budha' ")
    agama20 = str(cur.fetchone()[0])
    #Total Perempuan Hindu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama LIKE 'Hindu' ")
    agama21 = str(cur.fetchone()[0])
    #Total Perempuan Konghuchu
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama IN ('Aliran Khonghuchu','Konghuchu, Khonghucu') ")
    agama22 = str(cur.fetchone()[0])
    #Total Perempuan Aliran Kepercayaan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama IN ('Aliran Kepercayaan','Kepercayaan', 'Aliran Ke-percayaan', 'KEPERCAYAAN TERHADAP TUHAN YANG MAHA ESA') ")
    agama23 = str(cur.fetchone()[0])
    #Total Perempuan Agama Lainnya
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND agama NOT IN ('Islam','Kristen','Protestan','Kristen Protestan','Katholik','Kristen Katolik','Katolik','Hindu','Budha','Konghuchu','Aliran Kepercayaan','Kepercayaan','Khonghuchu','Khonghucu','Aliran Ke-percayaan') ")
    agama24 = str(cur.fetchone()[0])
    #Eksekusi SQL
    cur.execute("UPDATE `statistik_agama_kec` SET `total_islam`='"+agama1+"', `total_kristen_protestan`='"+agama2+"', `total_kristen_katolik`='"+agama3+"', `total_budha`='"+agama4+"', `total_hindu`='"+agama5+"', `total_konghuchu`='"+agama6+"', `total_aliran_kepercayaan`='"+agama7+"', `total_agama_lainnya`='"+agama8+"', `lk_islam`='"+agama9+"', `lk_kristen_protestan`='"+agama10+"', `lk_kristen_katolik`='"+agama11+"', `lk_budha`='"+agama12+"', `lk_hindu`='"+agama13+"', `lk_konghuchu`='"+agama14+"', `lk_aliran_kepercayaan`='"+agama15+"', `lk_agama_lainnya`='"+agama16+"', `pr_islam`='"+agama17+"', `pr_kristen_protestan`='"+agama18+"', `pr_kristen_katolik`='"+agama19+"', `pr_budha`='"+agama20+"', `pr_hindu`='"+agama21+"', `pr_konghuchu`='"+agama22+"', `pr_aliran_kepercayaan`='"+agama23+"', `pr_agama_lainnya`='"+agama24+"' WHERE id='"+a[0]+"' ")
    db.commit()
