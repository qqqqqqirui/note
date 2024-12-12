# INFO300.LabExercise 4 Part One
Date: October 30, 2024

Student Name: __Qirui Zhang_ Student ID: _320220941080_ Email:__320220941080@lzu.edu.cn_

Goals: Practice with ElasticSearch single document APIs

+ Submit a Makedown file named "Week4Lab-1.yourName.md" and a PDF file named "Week4Lab-1.yourName.pdf" 
 ( you may use this file as a template ) 

Notes:
+ Use your name to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.

## Working with ElasticSearch single document APIs

###  1). POST vs. PUT

Run the Command:
```json
POST /zhangqirui_docs/_doc
{
  "t1":"abc"
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "rjuO25IBzrtgRTHVQOjY",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}
```

Run the Command:
```json
PUT /suwei_docs/_doc
{
  "t1":"abc"
}
```
+ Why there is an error?
+ Your Answer:
```text
When posting POST /zhangqirui_docs/_doc, the document will create an ID randomly. While PUT /zhangqirui_docs/_doc need a specified index.
```
Run the Command:
```json
PUT /suwei_docs/_doc/1
{
  "t1":"abc"
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 1,
  "_primary_term": 1
}
```

Run the Command:
```json
PUT zhangqirui_docs/_create/2
{
  "t2":"nbc"
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "2",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 2,
  "_primary_term": 1
}
```
Run the Command:
```json
POST /zhangqirui_docs/_create/3
{
  "t2":"nba"
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "3",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 3,
  "_primary_term": 1
}
```

### 2). GET and HEAD


Run the Command:
```json
GET /zhangqirui_docs/_doc/2
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "2",
  "_version": 1,
  "_seq_no": 2,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "t2": "nbc"
  }
}
```
Run the Command:
```json
HEAD /zhangqirui_docs/_doc/2
```
Your Response:
```json
200 - OK
```

Run the Command:
```json
GET /zhangqirui_docs/_source/2
```
Your Response:
```json
{
  "t2": "nbc"
}
```

Run the Command:
```json
HEAD /zhangqirui_docs/_source/1234
```
Your Response:
```json
404 - Not Found
```
+ What's meaning of 404?
+ Your Answer:
```text

```

### 3). Delete

Run the Command:
```json
DELETE /zhangqirui_docs/_doc/2 
```
Your Response:
```json
{
  "_index": "zhangqirui_docs",
  "_id": "2",
  "_version": 2,
  "result": "deleted",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 4,
  "_primary_term": 1
}
```

Run the Command:
```json
POST /zhangqirui_docs/_delete_by_query
{
  "query":{
    "match":{
      "t2":"nbc"
    }
  }
}
```
Your Response:
```json
{
  "took": 1,
  "timed_out": false,
  "total": 0,
  "deleted": 0,
  "batches": 0,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1,
  "throttled_until_millis": 0,
  "failures": []
}
```

Run the Command:
```json
PUT /zhangqirui_docs1/_doc/1
{
  "title":"Catch me if you can"
}

POST zhangqirui_docs,zhangqirui_docs1/_delete_by_query
{
  "query":{
    "match_all":{}
  }
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs1",
  "_id": "1",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 1,
  "_primary_term": 1
}

{
  "took": 56,
  "timed_out": false,
  "total": 4,
  "deleted": 4,
  "batches": 1,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1,
  "throttled_until_millis": 0,
  "failures": []
}
```
+ Are there any documents in the index "zhangqirui_docs1" now? Does the index "zhangqirui_docs1" still exist?
+ Your Answer:
```text
The index zhangqirui_docs1 still exist
```

### 4). Update

Run the Command:
```json
PUT /zhangqirui_docs1/_doc/1
{
  "Ntest":1,
  "date":["2021-11-04"]
}

POST /zhangqirui_docs1/_update/1
{
  "script":{
    "source": "ctx._source.Ntest+=params.aa",
    "lang": "painless", 
    "params":{
      "aa":6
    }
  }
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs1",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 3,
  "_primary_term": 1
}

{
  "_index": "zhangqirui_docs1",
  "_id": "1",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 4,
  "_primary_term": 1
}

```
+ What's the value of "Ntest" now?
+ Your Answer:
```text
The value of "Ntest" is 7. The first code set "Ntest" as 1, and the second code add 6 to "Ntest", so the value of "Ntest" is 7.
```

Run the Command:
```json
POST /suwei_docs1/_update/1
{
  "script":{
    "source": "ctx._source.date.add(params.dt)",
    "lang": "painless", 
    "params":{
      "dt":"2024-10-28"
    }
  }
}
```
Your Response:
```json
{
  "_index": "zhangqirui_docs1",
  "_id": "1",
  "_version": 3,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 5,
  "_primary_term": 1
}
```
Write a query to see the document content of index "suwei_docs1"

Your Command:
```json
GET /zhangqirui_docs1/_doc/1
```
Your Response:
```json
{
  "_index": "zhangqirui_docs1",
  "_id": "1",
  "_version": 3,
  "_seq_no": 5,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "Ntest": 7,
    "date": [
      "2021-11-04",
      "2024-10-28"
    ]
  }
}
```


## Working with ElasticSearch multiple document APIs

### 1). Mget

Run the Command:
```json
GET /news/_mget
{
  "docs":[
    {
      "_id":"zjspiZIBzrtgRTHVJE4i"
    },
    {
      "_id":"9DkpiZIBzrtgRTHVB9my"
    }
    ]
}
```
Your Response:
```json
{
  "docs": [
    {
      "_index": "news",
      "_id": "zjspiZIBzrtgRTHVJE4i",
      "_version": 1,
      "_seq_no": 125985,
      "_primary_term": 1,
      "found": true,
      "_source": {
        "category": "COLLEGE",
        "headline": "Colleges Flush With Cash Saddle Poorest Students With Debt",
        "authors": "Annie Waldman and Sisi Wei, ProPublica",
        "link": "https://www.huffingtonpost.com/entry/colleges-flush-with-cash-saddle-poorest-students-with-debt_us_55f49b7ce4b042295e369755",
        "short_description": "Many private universities with lavish endowments give little aid to poor students, according to new data.",
        "date": "2015-09-12",
        "ignore_malformed": "false"
      }
    },
    {
      "_index": "news",
      "_id": "9DkpiZIBzrtgRTHVB9my",
      "_version": 1,
      "_seq_no": 30535,
      "_primary_term": 1,
      "found": true,
      "_source": {
        "category": "POLITICS",
        "headline": "Dear, Boy Scout Leaders: Apology Not Accepted",
        "authors": "David Fagin, ContributorWriter, musician, Trump Resister, food snob",
        "link": "https://www.huffingtonpost.com/entry/dear-boy-scout-leaders-apology-not-accepted_us_597a5aa6e4b09982b7376331",
        "short_description": "These kids need people with conviction and principles leading them forward.",
        "date": "2017-07-27",
        "ignore_malformed": "false"
      }
    }
  ]
}
```

Run the Command:
```json
GET /_mget
{
  "docs":[
    {
      "_index":"news",
      "_id":"DjkpiZIBzrtgRTHVCvsu",
      "_source":["authors","headline","short_description"]
    },
    {
      "_index":"info300_students",
      "_id":"PzRfb5IBzrtgRTHVN1gi"
    }
  ]
}
```
Your Response:
```json
{
  "docs": [
    {
      "_index": "news",
      "_id": "DjkpiZIBzrtgRTHVCvsu",
      "_version": 1,
      "_seq_no": 39009,
      "_primary_term": 1,
      "found": true,
      "_source": {
        "headline": "There's So Much I Want To Write About But Trump Keeps Getting In The Way",
        "authors": "David Fagin, ContributorWriter, musician, Trump Resister, food snob",
        "short_description": "Every time I sit down to write, whether it be a piece on the car insurance racket, the Net Neutrality issue, the dismantling"
      }
    },
    {
      "_index": "info300_students",
      "_id": "PzRfb5IBzrtgRTHVN1gi",
      "_version": 1,
      "_seq_no": 260,
      "_primary_term": 1,
      "found": true,
      "_source": {
        "studentID": "zzT7bpIBzrtgRTHV4lY6",
        "name": "Jielun Zhou",
        "class": "Data Science 2020",
        "from": "Fujian",
        "favor_food": "Orange Beef",
        "favor_fruit": "Apple",
        "favor_university": "Drexel",
        "interest": [
          "reading",
          "traveling",
          "programming",
          "Information retrieval",
          "visualization",
          "information visualization"
        ]
      }
    }
  ]
}
```

### 2). Bulk API
Run the Command:
```json
POST /_bulk
{"index":{"_index":"zhangqirui_test3","_id":"3"}}
{"name":"tom","age":21}
{"update":{"_index":"zhangqirui_test3","_id":"1"}}
{"doc":{"t2":"male"}}
{"index":{"_index":"zhangqirui_test3","_id":"4"}}
{"name":"mike","age":23}
```
Your Response:
```json
{
  "errors": true,
  "took": 400,
  "items": [
    {
      "index": {
        "_index": "zhangqirui_test3",
        "_id": "3",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 0,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "update": {
        "_index": "zhangqirui_test3",
        "_id": "1",
        "status": 404,
        "error": {
          "type": "document_missing_exception",
          "reason": "[1]: document missing",
          "index_uuid": "H7cqnbHTTqqN0Ew5UWqWfw",
          "shard": "0",
          "index": "zhangqirui_test3"
        }
      }
    },
    {
      "index": {
        "_index": "zhangqirui_test3",
        "_id": "4",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 1,
        "_primary_term": 1,
        "status": 201
      }
    }
  ]
}
```

### 3). Reindex API
Run the Command:
```json
POST /_reindex
{
  "source":{
    "index":"suwei_test3"
  },
  "dest": {
    "index":"suwei_test4"
  }
}
```
Your Response:
```json
{
  "took": 281,
  "timed_out": false,
  "total": 2,
  "updated": 0,
  "created": 2,
  "deleted": 0,
  "batches": 1,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1,
  "throttled_until_millis": 0,
  "failures": []
}
```
