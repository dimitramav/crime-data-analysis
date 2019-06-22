# Crime data analysis
## Introduction
The assignment is about data analysis and visualization based on the data crime system of Boston.

## Number of crimes per year/location
Based on the diagrams, most crimes took place in 2017(almost 100000). Correspondingly, most crimes were noticed in August (almost 35000)
and on Fridays (almost 50000).
The most criminal area of Boston, according the data, is B2. 

## Year and area with the most shooting incidents
The year with the most shooting incident is 2017, which was also the year with the greatest number of crimes.
Most shooting incidents took place in B2, which happens to be the most criminal area of Boston.

## Time of the day with the most crimes
Most crimes took place in the daytime (189442 crimes). Even though this may look unexpected, marked number of crimes during night was only 138378. 

## Most frequent type of crime in daytime

Most frequent type of crimes in daytime is Motor Vehicle Accident Response. It seems logical due to the fact that many accidents occur during rush hour.

## Kmeans location
The algorithm separates the data in clusters, based on the coordinates. The clusters' boundaries remain clear, regardless their number.


## Kmeans location - offense code
The algorithm separates the data in clusters, based on the coordinates and the offense code. The results of clustering is three dimensional thus its representation is in a three dimensional graph. When the number of clusters increase, their boundaries become more vague. 


## Kmeans location - month
The algorithm separates the data in clusters, based on the coordinates and the month that the crime took place. The clustering ends up
with a three dimensional graph. In comparison with kmeans location - offense code clustering is more discrete in larger number of clusters.
Thus, it is more efficient to use location and month in case we want to achieve a better clustering.

## Interactive map to represent crimes of a certain type
The library folium is imported to represent the location of a certain type of crime. However, we have to limit the number of data that will be depicted in 5000, because the library does not support a larger number of points. 

Collaborators: Ioannis Charamis (https://github.com/charamis) Dimitra Mavroforaki (https://github.com/dimitramav) 
