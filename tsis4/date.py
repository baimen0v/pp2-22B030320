<<<<<<< HEAD
from datetime import datetime as date
from datetime import timedelta as delta
#1
vremya= date.now()
new_date= vremya-delta(days=5)
print(new_date)
#2
yesterday= vremya-delta(days=1)
tomorrow= vremya+delta(days=1)
print(yesterday)
print(vremya)
print(tomorrow)
#3
print(vremya.replace(microsecond=0))
#4
date1=date(2022,2,14,12,0,0)
date2=date(1999,2,14,0,10,0)
diff=(date1-date2).total_seconds()
=======
from datetime import datetime as date
from datetime import timedelta as delta
#1
vremya= date.now()
new_date= vremya-delta(days=5)
print(new_date)
#2
yesterday= vremya-delta(days=1)
tomorrow= vremya+delta(days=1)
print(yesterday)
print(vremya)
print(tomorrow)
#3
print(vremya.replace(microsecond=0))
#4
date1=date(2022,2,14,12,0,0)
date2=date(1999,2,14,0,10,0)
diff=(date1-date2).total_seconds()
>>>>>>> f775ad08de5f3f842b08b0679d3d303024ca044f
print(diff)