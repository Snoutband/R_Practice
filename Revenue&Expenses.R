# The original excercise can be found at https://www.superdatascience.com/pages/rcourse Section 3
# I only used the exercise for reference. 
# Their learning material can be purchased on Udemy. 


install.packages('plyr') # required for count 
library(plyr)
install.packages("scales") # required for the percent function                                    
library("scales")

count(revenue) # gives us 12 
MeanofRevenue <- sum(revenue)/12
MeanOfExpenses <- sum(expenses)/12
revenue <- c(14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50)
expenses <- c(12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96)

N <- 12
d <- rep(NA, N) # creating the required empty spaces 
for(i in 1:N){
  d  <- append(revenue,expenses)} # appending expenses to the end of revenue 
cat(d)

Values <- c(revenue,expenses) # Other way to combine the values 
cat(Values)

for(a in revenue){ # calculating after tax of 30%
 aftertax <- round(revenue * .30,2)
}
cat(aftertax) 

Profitmargin <- scales::percent(round((aftertax / revenue),1)) # using the scales function to get a percentage
Goodmonth <- max(aftertax > mean(revenue))
badmonth <- min(aftertax< mean(revenue))







