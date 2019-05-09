import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_goldarah_kab` WHERE id LIKE '%3327%' ")
kabupaten=cur.fetchall()
for a in kabupaten:
    #Total Golongan Darah
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'A' ")
    goldar1 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'B' ")
    goldar2 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'AB' ")
    goldar3 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'O' ")
    goldar4 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'A+' ")
    goldar5 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'A-' ")
    goldar6 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'B+' ")
    goldar7 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'B-' ")
    goldar8 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'AB+' ")
    goldar9 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'AB-' ")
    goldar10 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'O+' ")
    goldar11 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah LIKE 'O-' ")
    goldar12 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND goldarah IN('-','','Tidak Tahu','Tdk Tahu') ")
    goldar13 = str(cur.fetchone()[0])
    #Laki-laki
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'A' ")
    goldar14 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'B' ")
    goldar15 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'AB' ")
    goldar16 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'O' ")
    goldar17 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'A+' ")
    goldar18 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'A-' ")
    goldar19 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'B+' ")
    goldar20 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'B-' ")
    goldar21 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'AB+' ")
    goldar22 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'AB-' ")
    goldar23 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'O+' ")
    goldar24 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah LIKE 'O-' ")
    goldar25 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'L%' AND goldarah IN('-','','Tidak Tahu','Tdk Tahu') ")
    goldar26 = str(cur.fetchone()[0])
    #Perempuan
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'A' ")
    goldar27 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'B' ")
    goldar28 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'AB' ")
    goldar29 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'O' ")
    goldar30 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'A+' ")
    goldar31 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'A-' ")
    goldar32 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'B+' ")
    goldar33 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'B-' ")
    goldar34 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'AB+' ")
    goldar35 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'AB-' ")
    goldar36 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'O+' ")
    goldar37 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah LIKE 'O-' ")
    goldar38 = str(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM `datapenduduk-33` WHERE kab_id='"+a[0]+"' AND jk LIKE 'P%' AND goldarah IN('-','','Tidak Tahu','Tdk Tahu') ")
    goldar39 = str(cur.fetchone()[0])
    #Eksekusi
    cur.execute("UPDATE `statistik_goldarah_kab` SET `total_a`='"+goldar1+"', `total_b`='"+goldar2+"', `total_ab`='"+goldar3+"', `total_o`='"+goldar4+"', `total_a+`='"+goldar5+"', `total_a-`='"+goldar6+"', `total_b+`='"+goldar7+"', `total_b-`='"+goldar8+"', `total_ab+`='"+goldar9+"', `total_ab-`='"+goldar10+"', `total_o+`='"+goldar11+"', `total_o-`='"+goldar12+"', `total_tdk_tahu`='"+goldar13+"', `lk_a`='"+goldar14+"', `lk_b`='"+goldar15+"', `lk_ab`='"+goldar16+"', `lk_o`='"+goldar17+"', `lk_a+`='"+goldar18+"', `lk_a-`='"+goldar19+"', `lk_b+`='"+goldar20+"', `lk_b-`='"+goldar21+"', `lk_ab+`='"+goldar22+"', `lk_ab-`='"+goldar23+"', `lk_o+`='"+goldar24+"', `lk_o-`='"+goldar25+"', `lk_tdk_tahu`='"+goldar26+"', `pr_a`='"+goldar27+"', `pr_b`='"+goldar28+"', `pr_ab`='"+goldar29+"', `pr_o`='"+goldar30+"', `pr_a+`='"+goldar31+"', `pr_a-`='"+goldar32+"', `pr_b+`='"+goldar33+"', `pr_b-`='"+goldar34+"', `pr_ab+`='"+goldar35+"', `pr_ab-`='"+goldar36+"', `pr_o+`='"+goldar37+"', `pr_o-`='"+goldar38+"', `pr_tdk_tahu`='"+goldar39+"' WHERE id='"+a[0]+"' ")
    db.commit()