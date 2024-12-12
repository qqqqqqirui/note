# INFO300.LabExercise 2 Part One
Date: October 16, 2024

Student: _Qirui Zhang_Email: __320220941080@lzu.edu.cn_ Student ID:_320220941080_

Goals: Practice with ElasticSearch queries and submit your md and PDF file.



## 1. Working with ElasticSearch queries

+ Logon to Kibana and open the "Dev Tools"
+ Run the ES queries to answer the following questions:
 + What are the total numbers of documents in the NEWS colletions?
 + Find all the news between 01/20/17 and 09/09/17 in this collection
 + How many news that mentions "basketball" in the headline or short_description in this collection?
 + How many news that mentions "basketball" in the headline and which is in the category of "SPORTS"?
 + Find all the news that mentions "basketball" but not in the category "SPORTS"
 + What are the categories for news about "basketball"?  How many news are in each of the categories?


1). What are the total numbers of documents in the NEWS colletions?
```json
GET news/_search
{
  "track_total_hits": true
}
```

2). Find all the news between 6/20/15 and 09/22/15 in this collection
```json
GET news/_search
{
  "query": {
    "range": {
      "date": {
        "gte": "2015-06-20",
        "lte": "2015-09-22"
      }
    }
  }
}
```

3). How many news that mentions "basketball" in the headline or short_description in this collection?
```json
GET news/_search
{
  "query": {
    "multi_match": {
      "query": "basketball",
      "fields": [
        "headline",
        "short_description"
      ]
    }
  }
}
```
4). How many news that mentions "basketball" in the headline and which is in the category of "SPORTS"?
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "headline": "basketball"
          }
        },
        {
          "match": {
            "category": "SPORTS"
          }
        }
      ]
    }
  }
}
```
Does the following comand get same result with the above comand?
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": {
          "match": {
            "headline": "basketball"
          }
        },
      "should": {
          "match": {
            "category": "SPORTS"
          }
        }
    }
  }
}
```
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "headline": "basketball"
        }
      },
      "filter": {
        "term": {
          "category": "SPORTS"
        }
      }
    
    }
  }
}
```
5). Find all the news that mentions "basketball" but not in the category "SPORTS"
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "headline": "Basketball"
        }
      },
      "must_not": [
        {
        "term": {
          "category": {
            "value": "SPORTS"
          }
        }
        }
      ]
    }
  }
}
```
6). What are the categories for news about "basketball"?  How many news are in each of the categories?
```json
GET news/_search
{
  "query": {
    "match": {
      "headline": "basketball"
    }
  },
  "aggs": {
    "by_category": {
      "terms": {
        "field": "category",
        "size": 100
      }
    }
  }
}
```

## 2. Write your own queries to answer the following questions:
+ Are there any news about tennis in this collection?
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "headline": "Tennis"
        }
      }
    }
  }
}
```
+ Find all the articles about football in the Sports category
```json
GET news/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "headline": "Football"
          }
        },
        {
          "match": {
            "category": "SPORTS"
          }
        }
      ]
    }
  }
}
```
+ Get the top 20 articles about "basketball" and "football"
```json
GET news/_search  
{  
  "query": {  
    "bool": {  
      "should": [  
        {  
          "match": {  
            "headline": "basketball"  
          }  
        },  
        {  
          "match": {  
            "headline": "football"  
          }  
        }  
      ]  
    }  
  },  
  "size": 20  
}
```
+ Find the articles that discuss costs of attending universities.
```json
GET news/_search  
{  
  "query": {  
    "bool": {  
      "should": [  
        { "match_phrase": { "headline": "cost of attending" } },  
        { "match_phrase": { "short_description": "cost of attending" } }  
      ],  
      "minimum_should_match": 1  
    }  
  }  
}
```
## 3. Submit your queries for the above four questions in a Makedown file named "LabExercise2-1.yourName.md" and PDF file

 + you may use this file as a template.
