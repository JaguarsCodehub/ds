IP_DATA_ALL<-read.csv("D:/DSPrac/Files/IP_DATA_ALL.csv")
> View(IP_DATA_ALL)
>spec(IP_DATA_ALL)
>library(tibble)
>set_tidy_names(IP_DATA_ALL,syntactic=TRUE,quiet=FALSE)
>IP_DATA_ALL_FIX=set tidy names(IP_DATA_ALL, syntactic= TRUE, quiet=TRUE)
>sapply(IP_DATA_ALL_FIX,typeof)
>library(data.table)
>hist_country=data.table(Country=unique(IP_DATA_ALL_FIX[is.na(IP_DATA_ALL_FIX[‘Country’])==0,]$Country))
>setorder(hist_country,’Country’)
>hist_country_with_id=rowid_to_column(hist_country,var=”RowIDCountry”)
>View(hist_country_fix)
>IP_DATA_COUNTRY_FREQ=data.table(with(IP_DATA_ALL_FIX,table(Country)))
>View(IP_DATA_COUNTRY_FREQ)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],min,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Country’],min,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],max,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Country’],max,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],mean,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],median,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],range,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],quantile,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Latitude’],sd,na.rm=TRUE)
>sapply(IP_DATA_ALL_FIX[,’Longitude’],sd,na.rm=TRUE)