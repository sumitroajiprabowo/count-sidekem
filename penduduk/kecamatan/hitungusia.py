import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="12345678", db="sidekem")
cur = db.cursor()
cur.execute("SELECT id FROM `statistik_usia_kec` WHERE id LIKE '%3327%' ")
kecamatan=cur.fetchall()
for a in kecamatan:
    #LK_0-4 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN(0,1,2,3,4)")
    umur1 = str(cur.fetchone()[0])
    #PR_0-4 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (0,1,2,3,4)")
    umur2 = str(cur.fetchone()[0])
    #Total_0-4 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (0,1,2,3,4)")
    umur3 = str(cur.fetchone()[0])
    #LK_5-9 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN(5,6,7,8,9)")
    umur4 = str(cur.fetchone()[0])
    #PR 5-9 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (5,6,7,8,9)")
    umur5 = str(cur.fetchone()[0])
    #Total 5-9 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (5,6,7,8,9)")
    umur6 = str(cur.fetchone()[0])
    #LK_10-14 tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN(10,11,12,13,14)")
    umur7 = str(cur.fetchone()[0])
    #PR_10-14 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (10,11,12,13,14)")
    umur8 = str(cur.fetchone()[0])
    #Total_10-14 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (10,11,12,13,14)")
    umur9 = str(cur.fetchone()[0])
    #LK_15-19 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN(15,16,17,18,19)")
    umur10 = str(cur.fetchone()[0])
    #PR_15-19 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (15,16,17,18,19)")
    umur11 = str(cur.fetchone()[0])
    #Total_15-19 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (15,16,17,18,19)")
    umur12 = str(cur.fetchone()[0])
    #LK_20-24 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (20,21,22,23,24)")
    umur13 = str(cur.fetchone()[0])
    #PR_20-24 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (20,21,22,23,24)")
    umur14 = str(cur.fetchone()[0])
    #Total_20-24 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (20,21,22,23,24)")
    umur15 = str(cur.fetchone()[0])
    #LK_25-29 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (25,26,27,28,29)")
    umur16 = str(cur.fetchone()[0])
    #PR_25-29 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (25,26,27,28,29)")
    umur17 = str(cur.fetchone()[0])
    #Total_25-29 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (25,26,27,28,29)")
    umur18 = str(cur.fetchone()[0])
    #LK_30-34 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (30,31,32,33,34)")
    umur19 = str(cur.fetchone()[0])
    #PR_30-34 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (30,31,32,33,34)")
    umur20 = str(cur.fetchone()[0])
    #Total_30-34 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (30,31,32,33,34)")
    umur21 = str(cur.fetchone()[0])
    #LK_35-39 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (35,36,37,38,39)")
    umur22 = str(cur.fetchone()[0])
    #PR_35-39 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (35,36,37,38,39)")
    umur23 = str(cur.fetchone()[0])
    #Total 35-39 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (35,36,37,38,39)")
    umur24 = str(cur.fetchone()[0])
    #LK_40-44 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (40,41,42,43,44)")
    umur25 = str(cur.fetchone()[0])
    #PR_40-44 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (40,41,42,43,44)")
    umur26 = str(cur.fetchone()[0])
    #Total_40-44 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (40,41,42,43,44)")
    umur27 = str(cur.fetchone()[0])
    #LK_45-49 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (45,46,47,48,49)")
    umur28 = str(cur.fetchone()[0])
    #PR_45-49 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (45,46,47,48,49)")
    umur29 = str(cur.fetchone()[0])
    #Total_45-49 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (45,46,47,48,49)")
    umur30 = str(cur.fetchone()[0])
    #LK_50-54 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (50,51,52,53,54)")
    umur31 = str(cur.fetchone()[0])
    #PR_50-54 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (50,51,52,53,54)")
    umur32 = str(cur.fetchone()[0])
    #Total_50-54 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (50,51,52,53,54)")
    umur33 = str(cur.fetchone()[0])
    #LK_55-60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun IN (55,56,57,58,59)")
    umur34 = str(cur.fetchone()[0])
    #PR_55-60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun IN (55,56,57,58,59)")
    umur35 = str(cur.fetchone()[0])
    #Total_55-60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun IN (55,56,57,58,59)")
    umur36 = str(cur.fetchone()[0])
    #LK_>= 60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun>=60")
    umur37 = str(cur.fetchone()[0])
    #PR_>= 60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun>=60")
    umur38 = str(cur.fetchone()[0])
    #Total_>=60 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND tahun>=60")
    umur39 = str(cur.fetchone()[0])
    #LK_<= 16 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun<=16")
    umur40 = str(cur.fetchone()[0])
    #PR_<= 16 tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun<=16")
    umur41 = str(cur.fetchone()[0])
    #Total_<=16 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND tahun<=16")
    umur42 = str(cur.fetchone()[0])
    #LK_>=17 tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'L%' AND tahun>=17")
    umur43 = str(cur.fetchone()[0])
    #PR_>= 17 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND jk LIKE 'P%' AND tahun>=17")
    umur44 = str(cur.fetchone()[0])
    #Total_>=17 Tahun
    cur.execute("SELECT COUNT(no) FROM `datapenduduk-33` WHERE kec_id='"+a[0]+"' AND  tahun>=17")
    umur45 = str(cur.fetchone()[0])
    #Eksekusi
    cur.execute("UPDATE `statistik_usia_kec` SET `lk_0-4`='"+umur1+"', `pr_0-4`='"+umur2+"', `total_0-4`='"+umur3+"', `lk_5-9`='"+umur4+"', `pr_5-9`='"+umur5+"', `total_5-9`='"+umur6+"', `lk_10-14`='"+umur7+"', `pr_10-14`='"+umur8+"', `total_10-14`='"+umur9+"', `lk_15-19`='"+umur10+"', `pr_15-19`='"+umur11+"', `total_15-19`='"+umur12+"', `lk_20-24`='"+umur13+"', `pr_20-24`='"+umur14+"', `total_20-24`='"+umur15+"', `lk_25-29`='"+umur16+"', `pr_25-29`='"+umur17+"', `total_25-29`='"+umur18+"', `lk_30-34`='"+umur19+"', `pr_30-34`='"+umur20+"', `total_30-34`='"+umur21+"', `lk_35-39`='"+umur22+"', `pr_35-39`='"+umur23+"', `total_35-39`='"+umur24+"', `lk_40-44`='"+umur25+"', `pr_40-44`='"+umur26+"', `total_40-44`='"+umur27+"', `lk_45-49`='"+umur28+"', `pr_45-49`='"+umur29+"', `total_45-49`='"+umur30+"', `lk_50-54`='"+umur31+"', `pr_50-54`='"+umur32+"', `total_50-54`='"+umur33+"', `lk_55-59`='"+umur34+"', `pr_55-59`='"+umur35+"', `total_55-59`='"+umur36+"', `lk_>60`='"+umur37+"', `pr_>60`='"+umur38+"', `total_>60`='"+umur39+"', `lk_0-16`='"+umur40+"', `pr_0-16`='"+umur41+"', `total_0-16`='"+umur42+"', `lk_>17`='"+umur43+"', `pr_>17`='"+umur44+"', `total_>17`='"+umur45+"'  WHERE id='"+a[0]+"' ")
    db.commit()