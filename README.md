# SQLAlchemy-Challenge - Surfs Up!

## Table of Contents
  * [Introduction](#introduction)
  * [Observations](#observations)
  * [Data Visualization](#data-visualization)
    * [Temperature (F) vs. Latitude](#temp)
    * [Humidity (%) vs. Latitude](#hum)
    * [Cloudiness (%) vs. Latitude](#clo)
    * [Wind Speed (mph) vs. Latitude](#win)
    

# <a name="introduction">Introduction</a>

This project is aimed at doing a climate analysis on Honolulu, Hawaii to help clients plan trips accordingly. 
I have used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. 
All of the following analysis are completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


## <a name="precipitation">Precipitation Analysis</a>

- A query was designed to retrieve the last 12 months of precipitation data.

- Only the date and prcp values were selected.

- Query results were loaded into a Pandas DataFrame, and the index was set to the date column.

- The DataFrame values were sorted by date.

- The results were plotted using the DataFrame plot method. The created plot is the following:
<br>![image](https://user-images.githubusercontent.com/69221324/114065924-2b471980-9869-11eb-8cf8-0bd5cea90770.png)



## <a name="station">Station Analysis</a>
- A query was designed to calculate the total number of stations and to find the most active stations.

  - The stations and observation counts were listed in descending order to find the most active stations, and the station has the highest number of observations using func.min, func.max, func.avg, and func.count in the queries.

- A query was to retrieve the last 12 months of temperature observation data (TOBS), and the data were filtered by the station with the highest number of observations.

  - The results were plotted as a histogram with bins=12. The created plot is the following:
<br>![image](https://user-images.githubusercontent.com/69221324/114065830-15395900-9869-11eb-960a-2241d772814a.png)



