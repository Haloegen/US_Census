Using the us census data the goal of this project is to first make a hypothesis and see if that hypothesis is correct

Using sql and python I have begun sorting out the total numbers of people who have children, and who smoke, as the main hypothesis of this is to find out if smokers pay more in insurance then those with children.

I have counted the total amounts of smokers with children, without children, non smokers with children and non smokers no children to see what percentage of the total pool is made up

The total amount of people/entries in the census is 1338. 
The average charge for insurance is 13270.42 dollars. 
Averages being non robust stats means that a small percentage of incredibly small insurance charges or on the other end incredibly large insurance charges could skew the average.

So next what I will do is find the top 5 insurance charges and the bottom 5 and calculate the range of their averages to see if this is truly the case

the assumption was that the range would show us something but the values of the top 5 are relatively close together, 
we shall expand to the top 10 and the bottom 10 to see if that changes anything
this also proved unhelpful.

Using Interquartile ranges and standard deviation I have found that the variability in the insurance charges is high, with their being 11,899 dollars between the 25th percentile and 75th percentile. Which in turn suggests that although the average is around 13,270 the individuals involved in the data set can vary greatly from the mean.

The standard deviation being 12,110 meands that the possibility of higher or lower insurance costs skewing the data is incredibly likely.

Using this information we can make an assumption that the information we have could be skewed in either direction, i'm leaning towards slightly right skewed with the highest insurance charges being over 6 times the lowest.