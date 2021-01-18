install.packages(c("MASS","tidyverse","car","interactions"))
install.packages("pacman")
library(pacman) #package manager
p_load(tidyverse,MASS ,car , interactions)

###########################################################
pollution <- read_csv("/home/waedas/Downloads/pollutionData201669.csv")
distinct(pollution)
class(pollution$timestamp)
#2014-08-01 for one day
pollution <- head(pollution , 287)
t.str <- strptime(pollution$timestamp, "%Y-%m-%d %H:%M:%S")
m.str <- as.numeric(format(t.str, "%H")) * 60 +
  as.numeric(format(t.str, "%M")) +  as.numeric(format(t.str, "%S")) / 60
summary(pollution)
ggplot(data = pollution, aes(x = m.str ,yLable="Pollutant Concentration")) +
  geom_line(aes(y = nitrogen_dioxide), color="blue") +
  geom_line(aes(y =  ozone), color="black") +    
  geom_line(aes(y = particullate_matter), color = "red") + 
  geom_line(aes(y = sulfure_dioxide), color="green") +
  xlab("Time (min)") + ylab("Pollutant Concentration")  +
  labs(tag = "Ozone - Black  , Particullate Matter - Red , Sulpher Dioxide - Green , Nitrogen Dioxide - Blue") +
  theme(plot.tag.position = c(0.5, 0.99))
  
