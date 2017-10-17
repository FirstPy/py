# -*- coding: utf-8 -*-
import  MySQLdb
db=MySQLdb.connect("ats_adp-master.flight.db.tuniu-sst.org","ats_adp_rw","tuniu520","ats_adp")
cursor=db.cursor()
cursor.execute("SELECT * FROM avupd_daily_call_log WHERE MODE=1 ")
data=cursor.fetchall()
print data
dalen=len(data)
for i in range(dalen):
    a=data[i]
    id=a[0]
    date=a[1]
    mode=a[2]
    result=a[3]
    times=a[4]
    print("id=%s,date=%s,mode=%s,result=%s,times=%s" %(id,date,mode,result,times))

db.close()