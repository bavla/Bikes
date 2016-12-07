
http://stackoverflow.com/questions/1174799/how-to-make-execution-pause-sleep-wait-for-x-seconds-in-r



See help(Sys.sleep).

For example, from ?Sys.sleep

testit <- function(x)
{
    p1 <- proc.time()
    Sys.sleep(x)
    proc.time() - p1 # The cpu usage should be negligible
}
testit(3.7)

Yielding

> testit(3.7)
   user  system elapsed 
  0.000   0.000   3.704 


wdir <- "C:/Users/batagelj/data/bikes/philly"
setwd(wdir)
stat <- "https://gbfs.bcycle.com/bcycle_indego/station_status.json"
num <- 0
setInternet2(use = TRUE)
p1 <- proc.time()
while (num < 5){
   num <- num+1
   fsave <- paste('status_',as.character(num),'.json',sep='')
   test <- tryCatch(download.file(stat,fsave,method="auto"),error=function(e) e)
   Sys.sleep(60)
   p2 <- proc.time()
   cat(p2 - p1,'\n'); flush.console()
   p1 <- p2
}

--------------------------------
> D <- dir(pattern = "^yell")
> head(D)
[1] "yellow_tripdata_2009-01.csv" "yellow_tripdata_2009-02.csv"
[3] "yellow_tripdata_2009-03.csv" "yellow_tripdata_2009-04.csv"
[5] "yellow_tripdata_2009-05.csv" "yellow_tripdata_2009-06.csv"
> D <- dir(pattern = "csv$")
> head(D)
[1] "green_tripdata_2013-08.csv" "green_tripdata_2013-09.csv"
[3] "green_tripdata_2013-10.csv" "green_tripdata_2013-11.csv"
[5] "green_tripdata_2013-12.csv" "green_tripdata_2014-01.csv"
> 
---------------------------------------------------------------------------

# http://stackoverflow.com/questions/9372211/reading-csv-with-date-and-time
DateConvert<-function(x){
  dt<-strsplit(x,split = " ")
  dt<-unlist(dt)
  d1<-dt[1:length(dt) %% 2==1 ]
  d2<-dt[1:length(dt) %% 2==0 ]
  a<-as.POSIXlt(chron(dates.=d1, times.=d2, format = c(dates = "y-m-d", times = "h:m:s")))
  return(a)
}

> DateConvert(S)
[1] "2013-07-01 02:00:00 CEST" "2013-07-01 02:00:02 CEST"
[3] "2013-07-01 02:01:04 CEST" "2013-07-01 02:01:06 CEST"
[5] "2013-07-01 02:01:10 CEST" "2013-07-01 02:01:23 CEST"
[7] "2013-07-01 02:01:59 CEST" "2013-07-01 02:02:16 CEST"
[9] "2013-07-01 02:02:16 CEST"
> DT <- DateConvert(S)
> DT[1]
[1] "2013-07-01 02:00:00 CEST"
> as.numeric(DT[1])
[1] 1372636800
> as.numeric(DT[2])
[1] 1372636802

wdir <- 'E:/data/bike/test'
setwd(wdir)
fdat <- 'test.csv'
T <- read.csv(fdat,head=TRUE,sep=',',colClasses="character")
dur <- as.integer(T[,1])
S <- DateConvert(T[,2])
F <- DateConvert(T[,3])
B <- as.integer(T[,4])
Bla <- as.numeric(T[,6])
Blo <- as.numeric(T[,7])
E <- as.integer(T[,8])
Ela <- as.numeric(T[,10])
Elo <- as.numeric(T[,11])
bid <- as.integer(T[,12])
utyp <- factor(T[,13],levels=c("Customer","Subscriber"))
Y <- T[,14]; Y[Y=='\\N'] <- "0"
year <- as.integer(Y)
gend <- as.integer(T[,15])


> w <- weekdays(S)
> w
[1] "ponedeljek" "ponedeljek" "ponedeljek" "ponedeljek" "ponedeljek"
[6] "ponedeljek" "ponedeljek" "ponedeljek" "ponedeljek"
> S$wday
[1] 1 1 1 1 1 1 1 1 1
> S$mon
[1] 6 6 6 6 6 6 6 6 6
> S$mday
[1] 1 1 1 1 1 1 1 1 1
> S$year
[1] 113 113 113 113 113 113 113 113 113
> S$hour
[1] 2 2 2 2 2 2 2 2 2
> S
[1] "2013-07-01 02:00:00 CEST" "2013-07-01 02:00:02 CEST"
[3] "2013-07-01 02:01:04 CEST" "2013-07-01 02:01:06 CEST"
[5] "2013-07-01 02:01:10 CEST" "2013-07-01 02:01:23 CEST"
[7] "2013-07-01 02:01:59 CEST" "2013-07-01 02:02:16 CEST"
[9] "2013-07-01 02:02:16 CEST"
> S$min
[1] 0 0 1 1 1 1 1 2 2
> S$sac
NULL
> S$sec
[1]  0  2  4  6 10 23 59 16 16

> T <- read.csv('tripDist.csv',head=TRUE,sep=',')
> head(T)
  trips links
1     1 37362
2     2 20902
3     3 14128
4     4 10683
5     5  8241
6     6  6712
> tail(T)
     trips links
1641  4396     1
1642  4648     1
1643  4913     1
1644  4989     1
1645  6466     1
1646 11986     1
> plot(T,log='xy',pch=16,cex=0.7,col='red',main='CitiBike 2015/10-2016/09')





