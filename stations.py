# wdir = 'E:/data/bike/test'
wdir = 'E:/data/bike/CitiBike/csv'
# ftrip = 'test.csv'
# ftrip = '2013-07 - Citi Bike trip data.csv'
# ftrip = '201609-citibike-tripdata.csv'
# ftrip = '201608-citibike-tripdata.csv'
# dtFormat = "%Y-%m-%d %H:%M:%S"
dtFormat = "%m/%d/%Y %H:%M:%S"

import sys, os, json, pickle
# sys.path = [gdir]+sys.path; 
os.chdir(wdir)
from datetime import *
import csv

def Stind(snam,sla,slo):
   if snam in S: sin = S[snam][0]
   #   sin, Sla, Slo = S[snam]; ok = True
   #   if abs(sla-Sla) > 0.0005: ok = False # print('lat', sla, Sla)
   #   if abs(slo-Slo) > 0.0005: ok = False # print('lon', slo, Slo)
   #   if not ok:
   #      print(tripsreader.line_num,snam,sla,Sla,slo,Slo,file=rep);
   #      sys.exit()
   else:
      sin = len(S) 
      S[snam] = [sin,sla,slo]
   return sin

def addStart(u,v,t):
   key = (u,v)
   if not(key in G): G[key] = [0]*48
   i = 2*t.hour+int(30<=t.minute)
   G[key][i] += 1

def Table(L):
   T = {}
   for a in L:
      if not(a in T): T[a] = 0
      T[a] += 1
   return T

DirCiti = [ 
 "2013-07 - Citi Bike trip data.csv", "2013-08 - Citi Bike trip data.csv",
 "2013-09 - Citi Bike trip data.csv", "2013-10 - Citi Bike trip data.csv",
 "2013-11 - Citi Bike trip data.csv", "2013-12 - Citi Bike trip data.csv",
 "2014-01 - Citi Bike trip data.csv", "2014-02 - Citi Bike trip data.csv",
 "2014-03 - Citi Bike trip data.csv", "2014-04 - Citi Bike trip data.csv",
 "2014-05 - Citi Bike trip data.csv", "2014-06 - Citi Bike trip data.csv",
 "2014-07 - Citi Bike trip data.csv", "2014-08 - Citi Bike trip data.csv",
 "201409-citibike-tripdata.csv"     , "201410-citibike-tripdata.csv"     ,
 "201411-citibike-tripdata.csv"     , "201412-citibike-tripdata.csv"     ,
 "201501-citibike-tripdata.csv"     , "201502-citibike-tripdata.csv"     ,
 "201503-citibike-tripdata.csv"     , "201504-citibike-tripdata.csv"     ,
 "201505-citibike-tripdata.csv"     , "201506-citibike-tripdata.csv"     ,
 "201507-citibike-tripdata.csv"     , "201508-citibike-tripdata.csv"     ,
 "201509-citibike-tripdata.csv"     , "201510-citibike-tripdata.csv"     ,
 "201511-citibike-tripdata.csv"     , "201512-citibike-tripdata.csv"     ,
 "201601-citibike-tripdata.csv"     , "201602-citibike-tripdata.csv"     ,
 "201603-citibike-tripdata.csv"     , "201604-citibike-tripdata.csv"     ,
 "201605-citibike-tripdata.csv"     , "201606-citibike-tripdata.csv"     ,
 "201607-citibike-tripdata.csv"     , "201608-citibike-tripdata.csv"     ,
 "201609-citibike-tripdata.csv"     ]
       
print("*** Bikes: Stations\n")
Utype = {"Customer":1,"Subscriber":2}
G = {}
rep = open('report.txt','wt')
if os.path.isfile('./stations.pickle'):
    with open('stations.pickle', 'rb') as sPick: S = pickle.load(sPick)
else: S = {}
print("# of stations = ",len(S))
modul = 50000; nRec = 0
t1 = datetime.now()
print("started: ",t1.ctime(),"\n")
tripFiles = DirCiti[27:]
for ftrip in tripFiles:
    print("tripFile = ",ftrip); print(ftrip,file=rep);
    with open(ftrip, newline='') as csvfile:
       tripsreader = csv.reader(csvfile, delimiter=',', quotechar='"')
       header = next(tripsreader)
    #   print(header)
       for trip in tripsreader:
    #      print(', '.join(trip),"\n")
          if tripsreader.line_num % modul == 0:
             print(".",sep="",end="",flush=True)
          dur = int(trip[0])
          bt = datetime.strptime(trip[1], dtFormat)
          et = datetime.strptime(trip[2], dtFormat)
          bwd = bt.isoweekday(); ewd = et.isoweekday()
          bs = int(trip[3]); bn = trip[4]
          bla = float(trip[5]); blo = float(trip[6])
          es = int(trip[7]); en = trip[8]
          ela = float(trip[9]); elo = float(trip[10])
          bid = int(trip[11])
          uty = Utype.get(trip[12])
          y = trip[13]; uy = 0 if y in ['','\\N'] else int(y)
          ug = int(trip[14])
          bind = Stind(bn,bla,blo)
          eind = Stind(en,ela,elo)
          addStart(bind,eind,bt)
    #      print(dur,(et-bt).seconds,bid,uy,ug)
       print("\n# of records = ",tripsreader.line_num)
       nRec += tripsreader.line_num
    t2 = datetime.now()
    print("processed: ",t2.ctime(),"\n")

print("\ntotal # of records = ",nRec)       
t3 = datetime.now()
print("\ncomputed: ",t3.ctime(),"\ntime used: ", t3-t1)
print("# of stations = ",len(S))
print("\npickle")
with open('stations.pickle','wb') as sPick:
    pickle.dump(S, sPick, pickle.HIGHEST_PROTOCOL)
with open('tripStart.pickle','wb') as sPick:
    pickle.dump(G, sPick, pickle.HIGHEST_PROTOCOL)

print("\nnetwork")
W = [ sum(L) for k, L in G.items() ]
w = Table(W)
# ws = [ (k, w[k]) for k in sorted(w) ]
# wC = ws[100:]; swC = sum([v for k,v in wC ])
list = open('tripDist.csv','wt')
print('trips,links', file=list)
for trip in sorted(w): print(trip,w[trip],sep=',',file=list)
list.close(); rep.close()
Sname = { v[0]: k for k,v in S.items() }
tresh = 1250
sos = open('SOs.csv','wt')
F = ['f'+str(i) for i in range(48)]
print('u,v,uName,vName,',','.join(F),sep='',file=sos)
for k in G:
   if sum(G[k])>=tresh:
      u,v = k; un = Sname[u]; vn = Sname[v]
      print(u,v,'"'+un+'"','"'+vn+'"',','.join([str(a) for a in G[k]]),sep=',',file=sos)
sos.close()

print("\nstations")
StSumO = [ 0 ] * len(S); StSumI = [ 0 ] * len(S)
for i in range(len(S)): StSumO[i] = [0]*48
for i in range(len(S)): StSumI[i] = [0]*48
for k in G:
   u,v = k; V = G[k]
   for i in range(48): 
      StSumO[u-1][i] = StSumO[u-1][i]+V[i]; StSumI[v-1][i] = StSumI[v-1][i]+V[i]
sos = open('SO2s.csv','wt')
O = ['o'+str(i) for i in range(48)]; I = ['i'+str(i) for i in range(48)]
print('v,Name,',','.join(O+I),sep='',file=sos)
for s in range(len(S)):
   print(s+1,'"'+Sname[s]+'"',
         ','.join([str(a) for a in (StSumO[s]+StSumI[s])]),
         sep=',',file=sos)
sos.close()

t4 = datetime.now()
print("\ncomputed: ",t4.ctime(),"\ntime used: ", t4-t3)

