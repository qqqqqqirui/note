# INFO300.LabExercise 4-2--Term Vectors APIs
Date: October 30, 2024

Student Name: __Qirui Zhang_ Student ID: _320220941080_  Email:_320220941080@lzu.edu.cn_

Goals: Practice with ElasticSearch term vectors APIs


+ Use your name to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.
+ Submit your MD and PDF file with the name of "LabExercise4-TermVectors-yourname"


##  1). term vectors 1

Run the Command:
```json
GET /news/_termvectors/zjkoiZIBzrtgRTHV_WL1?fields=headline
```
Your Response:
```json
{
  "_index": "news",
  "_id": "zjkoiZIBzrtgRTHV_WL1",
  "_version": 1,
  "found": true,
  "took": 0,
  "term_vectors": {
    "headline": {
      "field_statistics": {
        "sum_doc_freq": 821677,
        "doc_count": 82495,
        "sum_ttf": 834668
      },
      "terms": {
        "but": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 10,
              "start_offset": 57,
              "end_offset": 60
            }
          ]
        },
        "dad": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 5,
              "start_offset": 30,
              "end_offset": 33
            }
          ]
        },
        "day": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 2,
              "start_offset": 15,
              "end_offset": 18
            }
          ]
        },
        "does": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 12,
              "start_offset": 64,
              "end_offset": 68
            }
          ]
        },
        "doesn't": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 6,
              "start_offset": 34,
              "end_offset": 41
            }
          ]
        },
        "father's": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 1,
              "start_offset": 6,
              "end_offset": 14
            }
          ]
        },
        "gifts": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 3,
              "start_offset": 19,
              "end_offset": 24
            }
          ]
        },
        "he": {
          "term_freq": 2,
          "tokens": [
            {
              "position": 8,
              "start_offset": 47,
              "end_offset": 49
            },
            {
              "position": 11,
              "start_offset": 61,
              "end_offset": 63
            }
          ]
        },
        "know": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 7,
              "start_offset": 42,
              "end_offset": 46
            }
          ]
        },
        "wants": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 9,
              "start_offset": 50,
              "end_offset": 55
            }
          ]
        },
        "weird": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 0,
              "start_offset": 0,
              "end_offset": 5
            }
          ]
        },
        "your": {
          "term_freq": 1,
          "tokens": [
            {
              "position": 4,
              "start_offset": 25,
              "end_offset": 29
            }
          ]
        }
      }
    }
  }
}
```
+ What's the value of term_freq for the word "he"?
+ Your Answer:
```text
According to the response, the term_freq for the word "he" is 2.
```

##  2). term_statistics and field_statistics
Run the Command:
```json
GET /news/_termvectors/zjkoiZIBzrtgRTHV_WL1
{
  "fields":["headline"],
  "offsets":true,
  "positions":true,
  "term_statistics":true,
  "field_statistics":true
}
```
Your Response:
```json
{
  "_index": "news",
  "_id": "zjkoiZIBzrtgRTHV_WL1",
  "_version": 1,
  "found": true,
  "took": 1,
  "term_vectors": {
    "headline": {
      "field_statistics": {
        "sum_doc_freq": 821677,
        "doc_count": 82495,
        "sum_ttf": 834668
      },
      "terms": {
        "but": {
          "doc_freq": 1107,
          "ttf": 1107,
          "term_freq": 1,
          "tokens": [
            {
              "position": 10,
              "start_offset": 57,
              "end_offset": 60
            }
          ]
        },
        "dad": {
          "doc_freq": 268,
          "ttf": 270,
          "term_freq": 1,
          "tokens": [
            {
              "position": 5,
              "start_offset": 30,
              "end_offset": 33
            }
          ]
        },
        "day": {
          "doc_freq": 1243,
          "ttf": 1269,
          "term_freq": 1,
          "tokens": [
            {
              "position": 2,
              "start_offset": 15,
              "end_offset": 18
            }
          ]
        },
        "does": {
          "doc_freq": 331,
          "ttf": 333,
          "term_freq": 1,
          "tokens": [
            {
              "position": 12,
              "start_offset": 64,
              "end_offset": 68
            }
          ]
        },
        "doesn't": {
          "doc_freq": 394,
          "ttf": 395,
          "term_freq": 1,
          "tokens": [
            {
              "position": 6,
              "start_offset": 34,
              "end_offset": 41
            }
          ]
        },
        "father's": {
          "doc_freq": 73,
          "ttf": 73,
          "term_freq": 1,
          "tokens": [
            {
              "position": 1,
              "start_offset": 6,
              "end_offset": 14
            }
          ]
        },
        "gifts": {
          "doc_freq": 88,
          "ttf": 88,
          "term_freq": 1,
          "tokens": [
            {
              "position": 3,
              "start_offset": 19,
              "end_offset": 24
            }
          ]
        },
        "he": {
          "doc_freq": 1080,
          "ttf": 1115,
          "term_freq": 2,
          "tokens": [
            {
              "position": 8,
              "start_offset": 47,
              "end_offset": 49
            },
            {
              "position": 11,
              "start_offset": 61,
              "end_offset": 63
            }
          ]
        },
        "know": {
          "doc_freq": 917,
          "ttf": 924,
          "term_freq": 1,
          "tokens": [
            {
              "position": 7,
              "start_offset": 42,
              "end_offset": 46
            }
          ]
        },
        "wants": {
          "doc_freq": 605,
          "ttf": 606,
          "term_freq": 1,
          "tokens": [
            {
              "position": 9,
              "start_offset": 50,
              "end_offset": 55
            }
          ]
        },
        "weird": {
          "doc_freq": 99,
          "ttf": 113,
          "term_freq": 1,
          "tokens": [
            {
              "position": 0,
              "start_offset": 0,
              "end_offset": 5
            }
          ]
        },
        "your": {
          "doc_freq": 2668,
          "ttf": 2795,
          "term_freq": 1,
          "tokens": [
            {
              "position": 4,
              "start_offset": 25,
              "end_offset": 29
            }
          ]
        }
      }
    }
  }
}
```

+ What's the value of doc_freq and ttf for the word "he"?
+ Your Answer:
```text
The value of doc_freq of "he" is 1080, ttf for "he" is 1115
```
+ What's the meaning of doc_freq and ttf?
+ Your Answer:
```text
The meaning of "doc_freq" is the number of documents where the word exists. While "ttf" refers to the total word frequency of a word
```

##  3). Dynamically generate term vectors
Run the Command:
```json
GET /news/_termvectors
{
  "doc":{
    "headline":"Lanzhou University"
  },
  "term_statistics":true,
  "field_statistics":true,
  "positions":false
}
```

Write a command to get the term_statistics and field_staticstics of your Name in the index "info300_students".

Your Command:
```json
GET /info300_students/_termvectors
{
"doc": {
"name": "Your Name"
},
"term_statistics": true,
"field_statistics": true,
"positions": false
}
```
Your Response:
```json
{
  "_index": "info300_students",
  "_version": 0,
  "found": true,
  "took": 0,
  "term_vectors": {
    "name": {
      "field_statistics": {
        "sum_doc_freq": 841,
        "doc_count": 382,
        "sum_ttf": 841
      },
      "terms": {
        "zhangirui": {
          "term_freq": 1,
          "tokens": [
            {
              "start_offset": 0,
              "end_offset": 9
            }
          ]
        }
      }
    },
    "name.keyword": {
      "field_statistics": {
        "sum_doc_freq": 382,
        "doc_count": 382,
        "sum_ttf": 382
      },
      "terms": {
        "zhangirui": {
          "term_freq": 1,
          "tokens": [
            {
              "start_offset": 0,
              "end_offset": 9
            }
          ]
        }
      }
    }
  }
}
```
