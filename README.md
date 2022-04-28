# House price estimation
Project made mostly in Jupyter Notebook focusing on using linear regression model to predict the price of houses depending on city, area, floor number, number of rooms and year of construction as well as data visualizaition. Dataset used in this project is taken from Kaggle. 

## Data description
| column name | full name| description 
|-------------|----------|-----------------------
| no          | number   | - 
| adress      | -        | street name
| city        | -        | either 'Kraków', 'Warszawa' or 'Poznań'
| floor       | -        | floor on which the house (flat) is located
| id          | -        | -
| latitude    | -        | -
| longitude   | -        | -
| price       | -        | in PLN
| rooms       | -        | number of rooms in house (flat)
| sq          | area     | in square meters
| year        | -        | year of construction

## Libraries used
* pandas
* numpy
* matplotlib
* seaborn
* sklearn

## Methods used
* cleaning data
* data visualization
* linear regression
* least square method

## How it works
At the end of a Jupyter Notebook file is programme which after user's input prints estimated house price (user's input on the right).
![image](https://user-images.githubusercontent.com/101597257/165583144-0128cf1e-42e1-498a-baaf-69f4bf9ba703.png)

If city picked is 'Poznan' programme will not take the data about number of rooms as it was proven using least square method that this variable is insignifcant and can distort the result
![image](https://user-images.githubusercontent.com/101597257/165763938-2f6796d7-e99f-4029-9800-c4fe9819e312.png)


 
