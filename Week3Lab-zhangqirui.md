# INFO300.LabExercise 3
Date: October 23, 2024

Student: __Qirui Zhang___  Email: __320220941080@lzu.edu.cn_ Student ID: __320220941080____

+ Goals: Practice with ElasticSearch Analyzer 


+ Submit a Makedown and a PDF file named "Week3Lab-yourName" 
 ( you may use this file as a template ) 


### 1). Given the following text, use "whitespace", "standard", "english" Analyzer to analyze the text.

+ text: "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."

+ command example:
```json
POST _analyze
{
  "analyzer":"",
  "text": ""
}
```
Your Command 1:
```json
POST _analyze
{
  "analyzer":"whitespace",
  "text": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."
}
```

Your Command 2:
```json
POST _analyze
{
  "analyzer":"standard",
  "text": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."
}
```

Your Command 3:
```json
POST _analyze
{
  "analyzer":"english",
  "text": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."
}
```

Write the tokens under the three analyzers (sperated by semicolon):

+ whitespace:
```text
Lanzhou;University;has;2,135;full-time;teaching;faculty,;1,695;graduate;students’;supervisors;and;588;professors;on;2024/10/01.
```

+ standard: 
```text
lanzhou;university;has;2,135;full;time;teaching;faculty;1,695;graduate;students;supervisors;and;588;professors;on;2024;10;01
```
+ english: 
```text
lanzhou;univers;ha;2,135;full;time;teach;faculty;1,695;graduate;student;supervisor;588;professor;2024;10;01
```

### 2). Create an index of "yourName_books" and customized Analyzer with the type of "standard", the max token length of "9", the stopword of "_english_".

Command example:
```json
PUT /suwei_books
{
 "settings": {
   "analysis": {
     "analyzer": {
       "yourName_analyzer1":{
         "type":"",
         "max_token_length":"",
         "stopwords":""
       }
     }
   }
 }
}
```

Your Command 4:
```json
PUT /zhangqirui_books  
{  
  "settings": {  
    "analysis": {  
      "analyzer": {  
        "yourName_analyzer1": {  
          "type": "custom",  
          "tokenizer": "standard",  
          "filter": [  
            "lowercase",  
            "stop",  
            "length"  
          ]  
        }  
      },  
      "filter": {  
        "length": {  
          "type": "length",  
          "min": 1,  
          "max": 9  
        }  
      }  
    }  
  }  
}
```

Use the Analyzer to analyze the text: "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01.".

Command example:
```json
POST /suwei_books/_analyze
{
  "analyzer":"",
  "text": ""
}
```

Your Command 5:
```json
POST /zhangqirui_books/_analyze  
{  
  "analyzer": "yourName_analyzer1",  
  "text": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."  
}
```

Write all the tokens under the new Analyzer (sperated by semicolon):

+ yourName_analyzer:
```text
lanzhou;has;2,135;full;time;teaching;faculty;1,695;graduate;students;588;2024;10;01
```

### 3). Create a new index with name "yourName_analyzertest", Set the type of the field "introduction" to "text". Set the search time analyzer to "english" and the index time analyzer to "standard".

Command Example:
```json
PUT /suwei_analyzertest
{
  "mappings": {
   "properties": {
     "FieldName": {
       "type": "",
       "analyzer": "",
       "search_analyzer": ""
      }
    }
 }
}
```

Your Command 6:
```json
PUT /zhangqirui_analyzertest  
{  
  "mappings": {  
    "properties": {  
      "introduction": {  
        "type": "text",  
        "analyzer": "standard",  
        "search_analyzer": "english"  
      }  
    }  
  }  
}
```

Index a document including a field "introduction" with the text: "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01.".

Command example:
```json
PUT /suwei_analyzertest/_doc/1
{
  "": ""
}
```

Your Command 7:
```json
PUT /zhangqirui_analyzertest/_doc/1  
{  
  "introduction": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."  
}
```

Write three queries to retrieval the following text:

+ "University"
+ "university"
+ "full time"
+ "supervisors"
+ "supervisor"
+ "and"

Your Command 7:
```json
POST /zhangqirui_analyzertest/_search  
{  
  "query": {  
    "match": {  
      "introduction": "University"  
    }  
  }  
}
```
Response 7:
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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

Your Command 8:
```json
POST /zhangqirui_analyzertest/_search  
{  
  "query": {  
    "match": {  
      "introduction": "university"  
    }  
  }  
}
```

Response 8:
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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

Your Command 9:
```json
POST /yourName_analyzertest/_search 
{  
  "query": {  
    "match": {  
      "introduction": "full time"
    }  
  }  
}
```
Response 9:
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
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.5753642,
    "hits": [
      {
        "_index": "zhangqirui_analyzertest",
        "_id": "1",
        "_score": 0.5753642,
        "_source": {
          "introduction": "Lanzhou University has 2,135 full-time teaching faculty, 1,695 graduate students’ supervisors and 588 professors on 2024/10/01."
        }
      }
    ]
  }
}
```

Your Command 10:
```json
POST /yourName_analyzertest/_search 
{  
  "query": {  
    "match": {  
      "introduction": "supervisors"  
    }  
  }  
}
```
Response 10:
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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

Your Command 11:
```json
POST /yourName_analyzertest/_search 
{  
  "query": {  
    "match": {  
      "introduction": "supervisor"
    }  
  }  
}
```
Response 11:
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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

Your Command 12:
```json
{  
  "query": {  
    "match": {  
      "introduction":"and" 
    }  
  }  
}
```
Response 12:
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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

Give a short descrition why there IS or IS NO hit for each query.

Your Answer:
* "University":
```text
"University" is processed as "university" when creating the standard index analyzer, but is processed as "univers", so there is no hit when matching.
```

* "university":
```text
"University" is processed as "university" when creating the standard index analyzer, but is processed as "univers", so there is no hit when matching.
```
* "full time":
```text
"full-time" is processed as "full"and "time" when creating the standard index analyzer and the search_analyzer, so it can be searched.
```

* "supervisors":
```text
"supervisors" is processed as "supervisor" when creating the standard index analyzer, so there is no hit when matching.
```

* "supervisor":
```text
There is no "supervisor" in the introduction
```

* "and":
```text
"and" is not in "english" search_analyzer tokens 
```
