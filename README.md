# Bitcoin Price Tracker

[![N|Solid](https://miro.medium.com/max/1200/1*YJNS0JVl7RsVDTmORGZ6xA.png)](https://scrapy.org/)

Bitcoin price tracker is real time price tracking system which helps in getting the price of bitcoin and it's related features/


## Installation

Bitcoin Price Tracker requires [Scrapy](https://scrapy.org/) v1+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install scrapy
```

Then clone this repo and 

```sh
cd Bitcoin-price-tracker
scrapy crawl bitcoin
```

and if you want to save this record into csv then run the below command

```sh
scrapy crawl bitcoin -o results.csv
```

