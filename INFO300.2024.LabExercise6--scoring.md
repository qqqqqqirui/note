# INFO300.LabExercise 6--Scoring
Date: November 13, 2024

Student Name: _Qirui Zhang_  Class:_B_ Email:_320220941080@lzu.edu.cn_

Goals: Practice with ElasticSearch Scoring

Notes:
+ Use your name to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.

---

##  1). Upload the yelp data (business.json) to ES 

Note: 

+ The "location" field should set to "geo_point" data type. 

##  2). Script Score Query

### Step 1. Run the Command:

```json
GET /zhangqirui_business/_mapping
```

What's the data type of the following field?

Your Answer:
```text
"name"：text
"location": geo_point
"stars": double
"review_count": long
"city": keyword
"state": keyword
```
Run the following command:
```json
GET /suwei_yelp/_search
{
  "query":{
    "script_score":{
      "query":{
       "match":{
        "name":"Chinese"
      }
    },
      "script":{
        "source":"doc['stars'].value+doc['review_count'].value/10"
      }
    }
  }
}
```
Your Response:
```json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3,
      "relation": "eq"
    },
    "max_score": 29.5,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "dTyMI5MBzrtgRTHV44Ls",
        "_score": 29.5,
        "_source": {
          "business_id": "44YFU284Z3KDEy25QyVoUw",
          "name": "Nee House Chinese Restaurant",
          "address": "13843 N Tatum Blvd, Ste 15",
          "city": "Phoenix",
          "state": "AZ",
          "postal_code": "85032",
          "location": "33.6130201898,-111.9770356779",
          "stars": 3.5,
          "review_count": 269,
          "is_open": 1,
          "attributes": {
            "Caters": "True",
            "GoodForKids": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsPriceRange2": "2",
            "BusinessAcceptsCreditCards": "True",
            "HasTV": "False",
            "OutdoorSeating": "False",
            "RestaurantsTakeOut": "True",
            "RestaurantsTableService": "True",
            "RestaurantsDelivery": "False",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "RestaurantsReservations": "True",
            "BikeParking": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "Ambience": "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "WiFi": "u'no'",
            "Alcohol": "'beer_and_wine'",
            "RestaurantsGoodForGroups": "True",
            "RestaurantsAttire": "'casual'"
          },
          "categories": "Chinese, Restaurants",
          "hours": {
            "Monday": "11:0-21:0",
            "Tuesday": "11:0-21:0",
            "Wednesday": "11:0-21:0",
            "Thursday": "11:0-21:0",
            "Friday": "11:0-21:30",
            "Saturday": "11:0-21:30",
            "Sunday": "11:0-21:30"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "4jyMI5MBzrtgRTHV44Ls",
        "_score": 21,
        "_source": {
          "business_id": "MhnihE0alud0ereVInSt8Q",
          "name": "Yummy Yummy Chinese Restaurant",
          "address": "2765 N Scottsdale Rd, Ste 105",
          "city": "Scottsdale",
          "state": "AZ",
          "postal_code": "85257",
          "location": "33.478754,-111.925484",
          "stars": 3,
          "review_count": 188,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "RestaurantsGoodForGroups": "False",
            "RestaurantsTakeOut": "True",
            "GoodForKids": "True",
            "BikeParking": "True",
            "WiFi": "u'no'",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsDelivery": "True",
            "Alcohol": "u'none'",
            "RestaurantsReservations": "False",
            "HasTV": "True",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "Caters": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "Ambience": "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': True, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}",
            "NoiseLevel": "'average'"
          },
          "categories": "Chinese, Restaurants",
          "hours": {
            "Monday": "11:0-21:30",
            "Tuesday": "11:0-21:30",
            "Wednesday": "11:0-21:30",
            "Thursday": "11:0-21:30",
            "Friday": "11:0-22:0",
            "Saturday": "11:0-22:0",
            "Sunday": "11:0-21:30"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "KDyMI5MBzrtgRTHV44Ls",
        "_score": 14.5,
        "_source": {
          "business_id": "QXAEGFB4oINsVuTFxEYKFQ",
          "name": "Emerald Chinese Restaurant",
          "address": "30 Eglinton Avenue W",
          "city": "Mississauga",
          "state": "ON",
          "postal_code": "L5R 3E7",
          "location": "43.6054989743,-79.652288909",
          "stars": 2.5,
          "review_count": 128,
          "is_open": 1,
          "attributes": {
            "RestaurantsReservations": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "Caters": "True",
            "NoiseLevel": "u'loud'",
            "RestaurantsTableService": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2",
            "OutdoorSeating": "False",
            "BikeParking": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "HasTV": "False",
            "WiFi": "u'no'",
            "GoodForKids": "True",
            "Alcohol": "u'full_bar'",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Specialty Food, Restaurants, Dim Sum, Imported Food, Food, Chinese, Ethnic Food, Seafood",
          "hours": {
            "Monday": "9:0-0:0",
            "Tuesday": "9:0-0:0",
            "Wednesday": "9:0-0:0",
            "Thursday": "9:0-0:0",
            "Friday": "9:0-1:0",
            "Saturday": "9:0-1:0",
            "Sunday": "9:0-0:0"
          }
        }
      }
    ]
  }
}
```
What's the score of each business?
```text
1. name: "Nee House Chinese Restaurant"
   score: 29.5
2. name: "Yummy Yummy Chinese Restaurant"
   score: 21
3. name: "Emerald Chinese Restaurant"
   score: 14.5
```


### Step 2. Write a command to search "Sushi" in the "name" field and rank the retrieved documents according to the following formula.

+ saturation(*review_count*,10)

Your Command
```json
GET /zhangqirui_business/_search
{
"query": {
  "script_score": {
    "query": {
      "match": {
        "name": "Sushi"
        }
      },
    "script": {
      "source":"doc['stars'].value + (doc['review_count'].value / 10)"
      }
    }
  }
}
```
Your Response:
```json
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": 14.5,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "cDyMI5MBzrtgRTHV44Ls",
        "_score": 14.5,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "oDyMI5MBzrtgRTHV44Ls",
        "_score": 6.5,
        "_source": {
          "business_id": "aql8K6zVoJDGRJ3P-IgtpQ",
          "name": "Ume Fashion Sushi",
          "address": "1732 Kingston Road",
          "city": "Toronto",
          "state": "ON",
          "postal_code": "M1N 1S8",
          "location": "43.6927912,-79.2626299",
          "stars": 4.5,
          "review_count": 25,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "RestaurantsGoodForGroups": "True",
            "BikeParking": "True",
            "RestaurantsReservations": "True",
            "GoodForKids": "True",
            "RestaurantsAttire": "'casual'",
            "Alcohol": "'beer_and_wine'",
            "RestaurantsTakeOut": "True",
            "NoiseLevel": "'quiet'",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}",
            "RestaurantsDelivery": "True",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "HasTV": "False",
            "WiFi": "u'no'"
          },
          "categories": "Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-22:0",
            "Tuesday": "11:0-22:0",
            "Wednesday": "11:0-22:0",
            "Thursday": "11:0-22:0",
            "Friday": "11:0-22:0",
            "Saturday": "14:0-22:0",
            "Sunday": "14:0-22:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "4DyMI5MBzrtgRTHV44Ls",
        "_score": 5,
        "_source": {
          "business_id": "SJBzyJDCR_f6dx5tpYAABA",
          "name": "Kibo Sushi House",
          "address": "2945 Lake Shore Boulevard",
          "city": "Toronto",
          "state": "ON",
          "postal_code": "M8V 1J5",
          "location": "43.6005226,-79.5055159",
          "stars": 4,
          "review_count": 15,
          "is_open": 1,
          "attributes": {
            "RestaurantsDelivery": "True",
            "HasTV": "True",
            "WiFi": "'no'",
            "BikeParking": "False",
            "Alcohol": "'none'",
            "NoiseLevel": "'average'",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsReservations": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "OutdoorSeating": "False",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsTableService": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2"
          },
          "categories": "Sushi Bars, Japanese, Restaurants",
          "hours": {
            "Monday": "16:0-22:0",
            "Tuesday": "11:30-22:0",
            "Wednesday": "11:30-22:0",
            "Thursday": "11:30-22:0",
            "Friday": "11:30-22:0",
            "Saturday": "11:30-22:0",
            "Sunday": "16:0-22:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "3DyMI5MBzrtgRTHV44Ls",
        "_score": 3,
        "_source": {
          "business_id": "Rs8Wi4OEjeOX7LVlzsXDOA",
          "name": "Sushi Mocorito",
          "address": "3415 West Glendale Ave, Bldg 25A",
          "city": "Phoenix",
          "state": "AZ",
          "postal_code": "85051",
          "location": "33.5371638,-112.1329258",
          "stars": 3,
          "review_count": 9,
          "is_open": 1,
          "attributes": {
            "RestaurantsGoodForGroups": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "True",
            "RestaurantsReservations": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2"
          },
          "categories": "Restaurants, Mexican, Sushi Bars",
          "hours": {
            "Monday": "11:0-22:0",
            "Tuesday": "11:0-22:0",
            "Wednesday": "11:0-22:0",
            "Thursday": "11:0-22:0",
            "Friday": "11:0-23:0",
            "Saturday": "11:0-23:0",
            "Sunday": "11:0-22:0"
          }
        }
      }
    ]
  }
}
```

Calculate the score by yourself (You need to give the details of your calculation). Are they same with the result of ES?

Your Answer:
```text
1. score=stars+review_count/10=15.1
2. score=stars+review_count/10=7
3. score=stars+review_count/10=5.5

Not the same with the result
```

Re-write a command to rank the retrieved documents according to the following formula.

+ sigmoid(*review_count*, 2, 1)+sigmoid(*stars*, 2, 3)

Your Command:
```json
GET /zhangqirui_business/_search  
{  
  "query": {  
    "script_score": {  
      "query": {  
        "match": {  
          "name": "Sushi"  
        }  
      },  
      "script": {  
        "source": """  
          // Define the sigmoid function  
          double sigmoid(double x, double a, double b) {  
            return 1 / (1 + Math.exp(-a * (x - b)));  
          }  
          // Calculate score using the provided formula  
          return sigmoid(doc['review_count'].value, 2, 1) + sigmoid(doc['stars'].value, 2, 3);  
        """  
      }  
    }  
  }  
}
```
Your Response:
```json
{
  "took": 12,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": 1.9525741,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "cDyMI5MBzrtgRTHV44Ls",
        "_score": 1.9525741,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "oDyMI5MBzrtgRTHV44Ls",
        "_score": 1.9525741,
        "_source": {
          "business_id": "aql8K6zVoJDGRJ3P-IgtpQ",
          "name": "Ume Fashion Sushi",
          "address": "1732 Kingston Road",
          "city": "Toronto",
          "state": "ON",
          "postal_code": "M1N 1S8",
          "location": "43.6927912,-79.2626299",
          "stars": 4.5,
          "review_count": 25,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "RestaurantsGoodForGroups": "True",
            "BikeParking": "True",
            "RestaurantsReservations": "True",
            "GoodForKids": "True",
            "RestaurantsAttire": "'casual'",
            "Alcohol": "'beer_and_wine'",
            "RestaurantsTakeOut": "True",
            "NoiseLevel": "'quiet'",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}",
            "RestaurantsDelivery": "True",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "HasTV": "False",
            "WiFi": "u'no'"
          },
          "categories": "Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-22:0",
            "Tuesday": "11:0-22:0",
            "Wednesday": "11:0-22:0",
            "Thursday": "11:0-22:0",
            "Friday": "11:0-22:0",
            "Saturday": "14:0-22:0",
            "Sunday": "14:0-22:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "4DyMI5MBzrtgRTHV44Ls",
        "_score": 1.880797,
        "_source": {
          "business_id": "SJBzyJDCR_f6dx5tpYAABA",
          "name": "Kibo Sushi House",
          "address": "2945 Lake Shore Boulevard",
          "city": "Toronto",
          "state": "ON",
          "postal_code": "M8V 1J5",
          "location": "43.6005226,-79.5055159",
          "stars": 4,
          "review_count": 15,
          "is_open": 1,
          "attributes": {
            "RestaurantsDelivery": "True",
            "HasTV": "True",
            "WiFi": "'no'",
            "BikeParking": "False",
            "Alcohol": "'none'",
            "NoiseLevel": "'average'",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsReservations": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "OutdoorSeating": "False",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsTableService": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2"
          },
          "categories": "Sushi Bars, Japanese, Restaurants",
          "hours": {
            "Monday": "16:0-22:0",
            "Tuesday": "11:30-22:0",
            "Wednesday": "11:30-22:0",
            "Thursday": "11:30-22:0",
            "Friday": "11:30-22:0",
            "Saturday": "11:30-22:0",
            "Sunday": "16:0-22:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "3DyMI5MBzrtgRTHV44Ls",
        "_score": 1.4999999,
        "_source": {
          "business_id": "Rs8Wi4OEjeOX7LVlzsXDOA",
          "name": "Sushi Mocorito",
          "address": "3415 West Glendale Ave, Bldg 25A",
          "city": "Phoenix",
          "state": "AZ",
          "postal_code": "85051",
          "location": "33.5371638,-112.1329258",
          "stars": 3,
          "review_count": 9,
          "is_open": 1,
          "attributes": {
            "RestaurantsGoodForGroups": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "True",
            "RestaurantsReservations": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2"
          },
          "categories": "Restaurants, Mexican, Sushi Bars",
          "hours": {
            "Monday": "11:0-22:0",
            "Tuesday": "11:0-22:0",
            "Wednesday": "11:0-22:0",
            "Thursday": "11:0-22:0",
            "Friday": "11:0-23:0",
            "Saturday": "11:0-23:0",
            "Sunday": "11:0-22:0"
          }
        }
      }
    ]
  }
}
```
### Step 3. Write a command to search "Chinese" in the "name" field and rank the retrieved documents according to the following formula.

+ randomScore(12)

Your Command:
```json
GET /zhangqirui_business/_search  
{  
  "query": {  
    "function_score": {  
      "query": {  
        "match": {  
          "name": "Chinese"  
        }  
      },  
      "functions": [  
        {  
          "random_score": {  
            "seed": 12  
          }  
        }  
      ],  
      "boost_mode": "sum"  
    }  
  }  
}
```
Your Response:
```json
#! As of version 7.0 Elasticsearch will require that a [field] parameter is provided when a [seed] is set
#! Loading the fielddata on the _id field is deprecated and will be removed in future versions. If you require sorting or aggregating on this field you should also include the id in the body of your documents, and map this field as a keyword field that has [doc_values] enabled
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3,
      "relation": "eq"
    },
    "max_score": 4.37903,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "4jyMI5MBzrtgRTHV44Ls",
        "_score": 4.37903,
        "_source": {
          "business_id": "MhnihE0alud0ereVInSt8Q",
          "name": "Yummy Yummy Chinese Restaurant",
          "address": "2765 N Scottsdale Rd, Ste 105",
          "city": "Scottsdale",
          "state": "AZ",
          "postal_code": "85257",
          "location": "33.478754,-111.925484",
          "stars": 3,
          "review_count": 188,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "RestaurantsGoodForGroups": "False",
            "RestaurantsTakeOut": "True",
            "GoodForKids": "True",
            "BikeParking": "True",
            "WiFi": "u'no'",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsDelivery": "True",
            "Alcohol": "u'none'",
            "RestaurantsReservations": "False",
            "HasTV": "True",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "Caters": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "Ambience": "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': True, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}",
            "NoiseLevel": "'average'"
          },
          "categories": "Chinese, Restaurants",
          "hours": {
            "Monday": "11:0-21:30",
            "Tuesday": "11:0-21:30",
            "Wednesday": "11:0-21:30",
            "Thursday": "11:0-21:30",
            "Friday": "11:0-22:0",
            "Saturday": "11:0-22:0",
            "Sunday": "11:0-21:30"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "KDyMI5MBzrtgRTHV44Ls",
        "_score": 4.198821,
        "_source": {
          "business_id": "QXAEGFB4oINsVuTFxEYKFQ",
          "name": "Emerald Chinese Restaurant",
          "address": "30 Eglinton Avenue W",
          "city": "Mississauga",
          "state": "ON",
          "postal_code": "L5R 3E7",
          "location": "43.6054989743,-79.652288909",
          "stars": 2.5,
          "review_count": 128,
          "is_open": 1,
          "attributes": {
            "RestaurantsReservations": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "Caters": "True",
            "NoiseLevel": "u'loud'",
            "RestaurantsTableService": "True",
            "RestaurantsTakeOut": "True",
            "RestaurantsPriceRange2": "2",
            "OutdoorSeating": "False",
            "BikeParking": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "HasTV": "False",
            "WiFi": "u'no'",
            "GoodForKids": "True",
            "Alcohol": "u'full_bar'",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Specialty Food, Restaurants, Dim Sum, Imported Food, Food, Chinese, Ethnic Food, Seafood",
          "hours": {
            "Monday": "9:0-0:0",
            "Tuesday": "9:0-0:0",
            "Wednesday": "9:0-0:0",
            "Thursday": "9:0-0:0",
            "Friday": "9:0-1:0",
            "Saturday": "9:0-1:0",
            "Sunday": "9:0-0:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "dTyMI5MBzrtgRTHV44Ls",
        "_score": 3.6182508,
        "_source": {
          "business_id": "44YFU284Z3KDEy25QyVoUw",
          "name": "Nee House Chinese Restaurant",
          "address": "13843 N Tatum Blvd, Ste 15",
          "city": "Phoenix",
          "state": "AZ",
          "postal_code": "85032",
          "location": "33.6130201898,-111.9770356779",
          "stars": 3.5,
          "review_count": 269,
          "is_open": 1,
          "attributes": {
            "Caters": "True",
            "GoodForKids": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsPriceRange2": "2",
            "BusinessAcceptsCreditCards": "True",
            "HasTV": "False",
            "OutdoorSeating": "False",
            "RestaurantsTakeOut": "True",
            "RestaurantsTableService": "True",
            "RestaurantsDelivery": "False",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}",
            "RestaurantsReservations": "True",
            "BikeParking": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "Ambience": "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "WiFi": "u'no'",
            "Alcohol": "'beer_and_wine'",
            "RestaurantsGoodForGroups": "True",
            "RestaurantsAttire": "'casual'"
          },
          "categories": "Chinese, Restaurants",
          "hours": {
            "Monday": "11:0-21:0",
            "Tuesday": "11:0-21:0",
            "Wednesday": "11:0-21:0",
            "Thursday": "11:0-21:0",
            "Friday": "11:0-21:30",
            "Saturday": "11:0-21:30",
            "Sunday": "11:0-21:30"
          }
        }
      }
    ]
  }
}
```
### Step 4. Write a command to search "Pittsburgh" in the "city" field and rank the retrieved documents according to the following formula.

+ decayGeoExp(params.origin, params.scale, params.offset, params.decay,*location*)

  Note: You can use the following parameters and values.
```text
    "origin":"40.4812,-80.1234",
    "scale":"40km",
    "offset":"0km",
    "decay" : 0.2
```
Your Command
```json
GET /zhangqirui_business/_search  
{  
  "query": {  
    "script_score": {  
      "query": {  
        "match": {
          "city": "Pittsburgh"
        }
      },  
      "script": {  
        "source": "decayGeoExp(params.origin, params.scale, params.offset, params.decay, doc['location'].value)",
        "params":{
          "origin":"40.4812,-80.1234",
          "scale": "40km",
          "offset": "0km",
          "decay": 0.2
        }
      }  
    }  
  }  
}
```
Your Response:
```json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 5,
      "relation": "eq"
    },
    "max_score": 0.6553727,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "PjyMI5MBzrtgRTHV44Ls",
        "_score": 0.6553727,
        "_source": {
          "business_id": "1RHY4K3BD22FK7Cfftn8Mg",
          "name": "Marathon Diner",
          "address": "Center Core - Food Court, Fl 3, Pittsburgh International Airport",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15231",
          "location": "40.4961769456,-80.2460112364",
          "stars": 4,
          "review_count": 35,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsDelivery": "False",
            "RestaurantsReservations": "False",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "RestaurantsGoodForGroups": "True",
            "DriveThru": "False",
            "GoodForKids": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "HasTV": "False",
            "OutdoorSeating": "False"
          },
          "categories": "Sandwiches, Salad, Restaurants, Burgers, Comfort Food",
          "hours": null
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "cDyMI5MBzrtgRTHV44Ls",
        "_score": 0.6375066,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "2DyMI5MBzrtgRTHV44Ls",
        "_score": 0.6281007,
        "_source": {
          "business_id": "5WMIvoMx3l1vn1uJ3HZB6Q",
          "name": "Subway",
          "address": "411 7th Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15219",
          "location": "40.4428627,-79.996412",
          "stars": 3,
          "review_count": 3,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessAcceptsCreditCards": "True",
            "Alcohol": "u'none'",
            "RestaurantsPriceRange2": "1",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsReservations": "False",
            "GoodForKids": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Fast Food, Sandwiches, Restaurants",
          "hours": null
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "aTyMI5MBzrtgRTHV44Ls",
        "_score": 0.55073345,
        "_source": {
          "business_id": "dQj5DLZjeDK3KFysh1SYOQ",
          "name": "Apteka",
          "address": "4606 Penn Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15224",
          "location": "40.4656937,-79.9493238",
          "stars": 4.5,
          "review_count": 242,
          "is_open": 1,
          "attributes": {
            "CoatCheck": "False",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "HappyHour": "True",
            "Smoking": "u'no'",
            "WiFi": "u'free'",
            "RestaurantsTableService": "False",
            "RestaurantsDelivery": "False",
            "Alcohol": "u'full_bar'",
            "RestaurantsPriceRange2": "2",
            "HasTV": "False",
            "Caters": "True",
            "Music": "{'dj': False, 'background_music': True, 'jukebox': False, 'live': False, 'video': False, 'karaoke': False}",
            "RestaurantsTakeOut": "True",
            "BestNights": "{'monday': False, 'tuesday': False, 'friday': True, 'wednesday': True, 'thursday': True, 'sunday': False, 'saturday': False}",
            "WheelchairAccessible": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "False",
            "BusinessAcceptsBitcoin": "False",
            "GoodForDancing": "False",
            "BikeParking": "True",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsReservations": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': True, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "OutdoorSeating": "False"
          },
          "categories": "Nightlife, Bars, Polish, Modern European, Restaurants, Vegan",
          "hours": {
            "Wednesday": "17:0-0:0",
            "Thursday": "17:0-0:0",
            "Friday": "17:0-0:0",
            "Saturday": "17:0-0:0",
            "Sunday": "17:0-0:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "ujyMI5MBzrtgRTHV44Ls",
        "_score": 0.50493497,
        "_source": {
          "business_id": "t-6tdxRaz7s9a0sf94Tguw",
          "name": "Impressionz",
          "address": "6008 Broad St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15206",
          "location": "40.4623454064,-79.9241651595",
          "stars": 4.5,
          "review_count": 29,
          "is_open": 0,
          "attributes": {
            "RestaurantsDelivery": "False",
            "RestaurantsGoodForGroups": "True",
            "HasTV": "False",
            "RestaurantsReservations": "False",
            "OutdoorSeating": "False",
            "Caters": "False",
            "BikeParking": "True",
            "NoiseLevel": "u'average'",
            "GoodForKids": "True",
            "BusinessAcceptsCreditCards": "False",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsAttire": "u'casual'",
            "WiFi": "u'no'",
            "RestaurantsTakeOut": "True",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "Alcohol": "u'none'"
          },
          "categories": "Restaurants, Caribbean",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-21:0",
            "Saturday": "11:0-21:0"
          }
        }
      }
    ]
  }
}
```
Write down the "name", "location" and score of each retrieved document.
```text
1. Name: Marathon Diner, Location: 40.4961769456,-80.2460112364, Score: 0.6553727  
2. Name: No. 1 Sushi Sushi, Location: 40.441062,-80.002126, Score: 0.6375066  
3. Name: Subway, Location: 40.4428627,-79.996412, Score: 0.6281007  
4. Name: Apteka, Location: 40.4656937,-79.9493238, Score: 0.55073345  
5. Name: Impressionz, Location: 40.4623454064,-79.9241651595, Score: 0.50493497
```
---

##  3). Re-upload the yelp file to ES 

Note: The "stars" and "review_count" fields should set to "rank_feature" data type. Use another index name such as "suwei_yelp_rank".

##  4). Rank Feature Query
Note: You should use the new index "suwei_yelp_rank" for the following steps.

### Step 1. Run the Command:

```json
GET /zhangqirui_business_rank/_mapping
```

Your Response:
```json
{
  "zhangqirui_business_rank": {
    "mappings": {
      "_meta": {
        "created_by": "file-data-visualizer"
      },
      "properties": {
        "address": {
          "type": "text"
        },
        "attributes": {
          "properties": {
            "AcceptsInsurance": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "AgesAllowed": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Alcohol": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Ambience": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BYOB": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BYOBCorkage": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BestNights": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BikeParking": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BusinessAcceptsBitcoin": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BusinessAcceptsCreditCards": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "BusinessParking": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "ByAppointmentOnly": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Caters": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "CoatCheck": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Corkage": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "DogsAllowed": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "DriveThru": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "GoodForDancing": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "GoodForKids": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "GoodForMeal": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "HairSpecializesIn": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "HappyHour": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "HasTV": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Music": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "NoiseLevel": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "OutdoorSeating": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsAttire": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsDelivery": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsGoodForGroups": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsPriceRange2": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsReservations": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsTableService": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "RestaurantsTakeOut": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Smoking": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "WheelchairAccessible": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "WiFi": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "business_id": {
          "type": "keyword"
        },
        "categories": {
          "type": "text"
        },
        "city": {
          "type": "keyword"
        },
        "hours": {
          "properties": {
            "Friday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Monday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Saturday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Sunday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Thursday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Tuesday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "Wednesday": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "is_open": {
          "type": "long"
        },
        "location": {
          "type": "keyword"
        },
        "name": {
          "type": "text"
        },
        "postal_code": {
          "type": "keyword"
        },
        "review_count": {
          "type": "rank_feature"
        },
        "stars": {
          "type": "rank_feature"
        },
        "state": {
          "type": "keyword"
        }
      }
    }
  }
}
```
 Run the Command:
```json
GET /zhangqirui_business_rank/_search
{
  "query":{
    "bool":{
      "must":{
        "match":{"city":"Pittsburgh"}
      },
      "should":{
        "rank_feature":{
          "field":"review_count"
        }
      }
    }
  }
}
```
Your Response:
```json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 5,
      "relation": "eq"
    },
    "max_score": 4.5423565,
    "hits": [
      {
        "_index": "zhangqirui_business_rank",
        "_id": "MTz2JZMBzrtgRTHV1-fK",
        "_score": 4.5423565,
        "_source": {
          "business_id": "dQj5DLZjeDK3KFysh1SYOQ",
          "name": "Apteka",
          "address": "4606 Penn Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15224",
          "location": "40.4656937,-79.9493238",
          "stars": 4.5,
          "review_count": 242,
          "is_open": 1,
          "attributes": {
            "CoatCheck": "False",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "HappyHour": "True",
            "Smoking": "u'no'",
            "WiFi": "u'free'",
            "RestaurantsTableService": "False",
            "RestaurantsDelivery": "False",
            "Alcohol": "u'full_bar'",
            "RestaurantsPriceRange2": "2",
            "HasTV": "False",
            "Caters": "True",
            "Music": "{'dj': False, 'background_music': True, 'jukebox': False, 'live': False, 'video': False, 'karaoke': False}",
            "RestaurantsTakeOut": "True",
            "BestNights": "{'monday': False, 'tuesday': False, 'friday': True, 'wednesday': True, 'thursday': True, 'sunday': False, 'saturday': False}",
            "WheelchairAccessible": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "False",
            "BusinessAcceptsBitcoin": "False",
            "GoodForDancing": "False",
            "BikeParking": "True",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsReservations": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': True, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "OutdoorSeating": "False"
          },
          "categories": "Nightlife, Bars, Polish, Modern European, Restaurants, Vegan",
          "hours": {
            "Wednesday": "17:0-0:0",
            "Thursday": "17:0-0:0",
            "Friday": "17:0-0:0",
            "Saturday": "17:0-0:0",
            "Sunday": "17:0-0:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "ODz2JZMBzrtgRTHV1-fK",
        "_score": 4.483858,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "Bjz2JZMBzrtgRTHV1-fJ",
        "_score": 4.321788,
        "_source": {
          "business_id": "1RHY4K3BD22FK7Cfftn8Mg",
          "name": "Marathon Diner",
          "address": "Center Core - Food Court, Fl 3, Pittsburgh International Airport",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15231",
          "location": "40.4961769456,-80.2460112364",
          "stars": 4,
          "review_count": 35,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsDelivery": "False",
            "RestaurantsReservations": "False",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "RestaurantsGoodForGroups": "True",
            "DriveThru": "False",
            "GoodForKids": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "HasTV": "False",
            "OutdoorSeating": "False"
          },
          "categories": "Sandwiches, Salad, Restaurants, Burgers, Comfort Food",
          "hours": null
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "gjz2JZMBzrtgRTHV1-fK",
        "_score": 4.2830195,
        "_source": {
          "business_id": "t-6tdxRaz7s9a0sf94Tguw",
          "name": "Impressionz",
          "address": "6008 Broad St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15206",
          "location": "40.4623454064,-79.9241651595",
          "stars": 4.5,
          "review_count": 29,
          "is_open": 0,
          "attributes": {
            "RestaurantsDelivery": "False",
            "RestaurantsGoodForGroups": "True",
            "HasTV": "False",
            "RestaurantsReservations": "False",
            "OutdoorSeating": "False",
            "Caters": "False",
            "BikeParking": "True",
            "NoiseLevel": "u'average'",
            "GoodForKids": "True",
            "BusinessAcceptsCreditCards": "False",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsAttire": "u'casual'",
            "WiFi": "u'no'",
            "RestaurantsTakeOut": "True",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "Alcohol": "u'none'"
          },
          "categories": "Restaurants, Caribbean",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-21:0",
            "Saturday": "11:0-21:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "oDz2JZMBzrtgRTHV1-fK",
        "_score": 3.7803397,
        "_source": {
          "business_id": "5WMIvoMx3l1vn1uJ3HZB6Q",
          "name": "Subway",
          "address": "411 7th Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15219",
          "location": "40.4428627,-79.996412",
          "stars": 3,
          "review_count": 3,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessAcceptsCreditCards": "True",
            "Alcohol": "u'none'",
            "RestaurantsPriceRange2": "1",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsReservations": "False",
            "GoodForKids": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Fast Food, Sandwiches, Restaurants",
          "hours": null
        }
      }
    ]
  }
}
```

### Step 2. Write a command to search "Pittsburgh" in the "city" field and rank the retrieved documents by rank_feature (*review_count*) and *saturation* function (with the following parameter).

+ "pivot": 8

Your Command:
```json
GET /zhangqirui_business_rank/_search
{
  "query" : {
    "bool" : {
      "must": {
        "match": { "city": "Pittsburgh" }
      },
      "should": {
        "rank_feature": {
          "field": "review_count",
          "saturation": {
            "pivot": 8
          }
        }
      }
    }
  }
}
```
Your Response:
```json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 5,
      "relation": "eq"
    },
    "max_score": 4.561569,
    "hits": [
      {
        "_index": "zhangqirui_business_rank",
        "_id": "MTz2JZMBzrtgRTHV1-fK",
        "_score": 4.561569,
        "_source": {
          "business_id": "dQj5DLZjeDK3KFysh1SYOQ",
          "name": "Apteka",
          "address": "4606 Penn Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15224",
          "location": "40.4656937,-79.9493238",
          "stars": 4.5,
          "review_count": 242,
          "is_open": 1,
          "attributes": {
            "CoatCheck": "False",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "HappyHour": "True",
            "Smoking": "u'no'",
            "WiFi": "u'free'",
            "RestaurantsTableService": "False",
            "RestaurantsDelivery": "False",
            "Alcohol": "u'full_bar'",
            "RestaurantsPriceRange2": "2",
            "HasTV": "False",
            "Caters": "True",
            "Music": "{'dj': False, 'background_music': True, 'jukebox': False, 'live': False, 'video': False, 'karaoke': False}",
            "RestaurantsTakeOut": "True",
            "BestNights": "{'monday': False, 'tuesday': False, 'friday': True, 'wednesday': True, 'thursday': True, 'sunday': False, 'saturday': False}",
            "WheelchairAccessible": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "False",
            "BusinessAcceptsBitcoin": "False",
            "GoodForDancing": "False",
            "BikeParking": "True",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsReservations": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': True, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "OutdoorSeating": "False"
          },
          "categories": "Nightlife, Bars, Polish, Modern European, Restaurants, Vegan",
          "hours": {
            "Wednesday": "17:0-0:0",
            "Thursday": "17:0-0:0",
            "Friday": "17:0-0:0",
            "Saturday": "17:0-0:0",
            "Sunday": "17:0-0:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "ODz2JZMBzrtgRTHV1-fK",
        "_score": 4.5233936,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "Bjz2JZMBzrtgRTHV1-fJ",
        "_score": 4.4075227,
        "_source": {
          "business_id": "1RHY4K3BD22FK7Cfftn8Mg",
          "name": "Marathon Diner",
          "address": "Center Core - Food Court, Fl 3, Pittsburgh International Airport",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15231",
          "location": "40.4961769456,-80.2460112364",
          "stars": 4,
          "review_count": 35,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsDelivery": "False",
            "RestaurantsReservations": "False",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "RestaurantsGoodForGroups": "True",
            "DriveThru": "False",
            "GoodForKids": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "HasTV": "False",
            "OutdoorSeating": "False"
          },
          "categories": "Sandwiches, Salad, Restaurants, Burgers, Comfort Food",
          "hours": null
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "gjz2JZMBzrtgRTHV1-fK",
        "_score": 4.377353,
        "_source": {
          "business_id": "t-6tdxRaz7s9a0sf94Tguw",
          "name": "Impressionz",
          "address": "6008 Broad St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15206",
          "location": "40.4623454064,-79.9241651595",
          "stars": 4.5,
          "review_count": 29,
          "is_open": 0,
          "attributes": {
            "RestaurantsDelivery": "False",
            "RestaurantsGoodForGroups": "True",
            "HasTV": "False",
            "RestaurantsReservations": "False",
            "OutdoorSeating": "False",
            "Caters": "False",
            "BikeParking": "True",
            "NoiseLevel": "u'average'",
            "GoodForKids": "True",
            "BusinessAcceptsCreditCards": "False",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsAttire": "u'casual'",
            "WiFi": "u'no'",
            "RestaurantsTakeOut": "True",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "Alcohol": "u'none'"
          },
          "categories": "Restaurants, Caribbean",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-21:0",
            "Saturday": "11:0-21:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business_rank",
        "_id": "oDz2JZMBzrtgRTHV1-fK",
        "_score": 3.8662965,
        "_source": {
          "business_id": "5WMIvoMx3l1vn1uJ3HZB6Q",
          "name": "Subway",
          "address": "411 7th Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15219",
          "location": "40.4428627,-79.996412",
          "stars": 3,
          "review_count": 3,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessAcceptsCreditCards": "True",
            "Alcohol": "u'none'",
            "RestaurantsPriceRange2": "1",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsReservations": "False",
            "GoodForKids": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Fast Food, Sandwiches, Restaurants",
          "hours": null
        }
      }
    ]
  }
}
```

##  5). Design a new scoring algorithm. 

The description of the new algorithm:
```text
score=doc['review_count'].value + doc['stars'].value

Score = review_count + stars
This means that each score will be the sum of its total reviews and its average rating. This straightforward approach incentivizes businesses that have both high review counts and high ratings, making it more likely that users will find popular and well-rated options.
```

Your Command:
```json
GET /zhangqirui_business/_search  
{  
  "query": {  
    "script_score": {  
      "query": {  
        "match": {
          "city": "Pittsburgh"
        }
      },  
      "script": {  
        "source": "doc['review_count'].value + doc['stars'].value",
        "params":{
          "origin":"40.4812,-80.1234",
          "scale": "40km",
          "offset": "0km",
          "decay": 0.2
        }
      }  
    }  
  }  
}
```

Your Response:
```json
{
  "took": 7,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 5,
      "relation": "eq"
    },
    "max_score": 246.5,
    "hits": [
      {
        "_index": "zhangqirui_business",
        "_id": "aTyMI5MBzrtgRTHV44Ls",
        "_score": 246.5,
        "_source": {
          "business_id": "dQj5DLZjeDK3KFysh1SYOQ",
          "name": "Apteka",
          "address": "4606 Penn Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15224",
          "location": "40.4656937,-79.9493238",
          "stars": 4.5,
          "review_count": 242,
          "is_open": 1,
          "attributes": {
            "CoatCheck": "False",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "HappyHour": "True",
            "Smoking": "u'no'",
            "WiFi": "u'free'",
            "RestaurantsTableService": "False",
            "RestaurantsDelivery": "False",
            "Alcohol": "u'full_bar'",
            "RestaurantsPriceRange2": "2",
            "HasTV": "False",
            "Caters": "True",
            "Music": "{'dj': False, 'background_music': True, 'jukebox': False, 'live': False, 'video': False, 'karaoke': False}",
            "RestaurantsTakeOut": "True",
            "BestNights": "{'monday': False, 'tuesday': False, 'friday': True, 'wednesday': True, 'thursday': True, 'sunday': False, 'saturday': False}",
            "WheelchairAccessible": "True",
            "BusinessAcceptsCreditCards": "True",
            "GoodForKids": "False",
            "BusinessAcceptsBitcoin": "False",
            "GoodForDancing": "False",
            "BikeParking": "True",
            "RestaurantsAttire": "u'casual'",
            "RestaurantsGoodForGroups": "True",
            "NoiseLevel": "u'average'",
            "RestaurantsReservations": "False",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': True, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': True, 'brunch': False, 'breakfast': False}",
            "OutdoorSeating": "False"
          },
          "categories": "Nightlife, Bars, Polish, Modern European, Restaurants, Vegan",
          "hours": {
            "Wednesday": "17:0-0:0",
            "Thursday": "17:0-0:0",
            "Friday": "17:0-0:0",
            "Saturday": "17:0-0:0",
            "Sunday": "17:0-0:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "cDyMI5MBzrtgRTHV44Ls",
        "_score": 110.5,
        "_source": {
          "business_id": "v-scZMU6jhnmV955RSzGJw",
          "name": "No. 1 Sushi Sushi",
          "address": "436 Market St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15222",
          "location": "40.441062,-80.002126",
          "stars": 4.5,
          "review_count": 106,
          "is_open": 1,
          "attributes": {
            "OutdoorSeating": "False",
            "HasTV": "True",
            "NoiseLevel": "'average'",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsTableService": "True",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsDelivery": "False",
            "WiFi": "'no'",
            "RestaurantsReservations": "False",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "RestaurantsTakeOut": "True",
            "Alcohol": "'none'",
            "RestaurantsGoodForGroups": "False",
            "BikeParking": "True",
            "WheelchairAccessible": "True",
            "Caters": "True",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
            "RestaurantsAttire": "'casual'",
            "RestaurantsPriceRange2": "2",
            "GoodForKids": "True"
          },
          "categories": "Japanese, Sushi Bars, Restaurants",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-20:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "PjyMI5MBzrtgRTHV44Ls",
        "_score": 39,
        "_source": {
          "business_id": "1RHY4K3BD22FK7Cfftn8Mg",
          "name": "Marathon Diner",
          "address": "Center Core - Food Court, Fl 3, Pittsburgh International Airport",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15231",
          "location": "40.4961769456,-80.2460112364",
          "stars": 4,
          "review_count": 35,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}",
            "RestaurantsDelivery": "False",
            "RestaurantsReservations": "False",
            "BusinessAcceptsCreditCards": "True",
            "RestaurantsPriceRange2": "1",
            "RestaurantsGoodForGroups": "True",
            "DriveThru": "False",
            "GoodForKids": "True",
            "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
            "HasTV": "False",
            "OutdoorSeating": "False"
          },
          "categories": "Sandwiches, Salad, Restaurants, Burgers, Comfort Food",
          "hours": null
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "ujyMI5MBzrtgRTHV44Ls",
        "_score": 33.5,
        "_source": {
          "business_id": "t-6tdxRaz7s9a0sf94Tguw",
          "name": "Impressionz",
          "address": "6008 Broad St",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15206",
          "location": "40.4623454064,-79.9241651595",
          "stars": 4.5,
          "review_count": 29,
          "is_open": 0,
          "attributes": {
            "RestaurantsDelivery": "False",
            "RestaurantsGoodForGroups": "True",
            "HasTV": "False",
            "RestaurantsReservations": "False",
            "OutdoorSeating": "False",
            "Caters": "False",
            "BikeParking": "True",
            "NoiseLevel": "u'average'",
            "GoodForKids": "True",
            "BusinessAcceptsCreditCards": "False",
            "RestaurantsPriceRange2": "2",
            "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsAttire": "u'casual'",
            "WiFi": "u'no'",
            "RestaurantsTakeOut": "True",
            "Ambience": "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}",
            "Alcohol": "u'none'"
          },
          "categories": "Restaurants, Caribbean",
          "hours": {
            "Monday": "11:0-20:0",
            "Tuesday": "11:0-20:0",
            "Wednesday": "11:0-20:0",
            "Thursday": "11:0-20:0",
            "Friday": "11:0-21:0",
            "Saturday": "11:0-21:0"
          }
        }
      },
      {
        "_index": "zhangqirui_business",
        "_id": "2DyMI5MBzrtgRTHV44Ls",
        "_score": 6,
        "_source": {
          "business_id": "5WMIvoMx3l1vn1uJ3HZB6Q",
          "name": "Subway",
          "address": "411 7th Ave",
          "city": "Pittsburgh",
          "state": "PA",
          "postal_code": "15219",
          "location": "40.4428627,-79.996412",
          "stars": 3,
          "review_count": 3,
          "is_open": 1,
          "attributes": {
            "RestaurantsTakeOut": "True",
            "BusinessAcceptsCreditCards": "True",
            "Alcohol": "u'none'",
            "RestaurantsPriceRange2": "1",
            "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
            "RestaurantsReservations": "False",
            "GoodForKids": "True",
            "RestaurantsDelivery": "False"
          },
          "categories": "Fast Food, Sandwiches, Restaurants",
          "hours": null
        }
      }
    ]
  }
}
```