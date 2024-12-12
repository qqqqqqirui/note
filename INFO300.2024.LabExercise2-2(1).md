# INFO300.LabExercise 2 Part Two
Date: October 16, 2024

Student: __Qirui Zhang_  Email: __320220941080@lzu.edu.cn_ Student ID:___320220941080____

+ Goals: Practice with ElasticSearch Mapping


+ Submit a Makedown file named "Week2Lab-2.yourName.md" and a PDF file named "Week2Lab-2.yourName.pdf" 
 ( you may use this file as a template ) 

## 1. Working with ElasticSearch Mapping


### 1). Create an index with a name of "yourName_course", put a document including four fields into the index. 
  + "course_name": "Machine Learning"
  + "credit":3
  + "start_date":"2023/10/08"
  + "score":"75"

Your command 1:
```json
PUT /zhangqirui_course  
{  
  "mappings": {  
    "properties": {  
      "course_name": {  
        "type": "text"  
      },  
      "credit": {  
        "type": "integer"  
      },  
      "start_date": {  
        "type": "date",  
        "format": "yyyy/MM/dd"  
      },  
      "score": {  
        "type": "float"  
      }  
    }  
  }  
}

POST /zhangqirui_course/_doc  
{  
  "course_name": "Machine Learning",  
  "credit": 3,  
  "start_date": "2023/10/08",  
  "score": 75  
}

```

Response 1:
```json
{
  "_index": "zhangqirui_course",
  "_id": "Ujtok5IBzrtgRTHVDOey",
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

### 2). Write a command to get the mapping of your index and answer the following questions:

Your command 2:
```json
GET /zhangqirui_course/_mapping
```

Response 2:
```json
{
  "zhangqirui_course": {
    "mappings": {
      "properties": {
        "course_name": {
          "type": "text"
        },
        "credit": {
          "type": "integer"
        },
        "score": {
          "type": "float"
        },
        "start_date": {
          "type": "date",
          "format": "yyyy/MM/dd"
        }
      }
    }
  }
}
```

+ What are data types of the following fields:
  + "course_name":___text____
  + "credit":___integer____
  + "start_date":____date_____
  + "score":__float_____


### 3). Delete the above index 

Your command 3:
```json
DELETE /zhangqirui_course
```

Response 3:
```json
{
  "acknowledged": true
}
```

### 4). Re-create the index of "yourName_course", Create a mapping for the index with the following data type.

  + "course_name": keyword
  + "credit": integer
  + "start_date":date
  + "score":float

Your command 4:
```json
PUT /zhangqirui_course  
{  
  "mappings": {  
    "properties": {  
      "course_name": {  
        "type": "keyword"  
      },  
      "credit": {  
        "type": "integer"  
      },  
      "start_date": {  
        "type": "date",  
        "format": "yyyy/MM/dd"  
      },  
      "score": {  
        "type": "float"  
      }  
    }  
  }  
}
```

Response 4:
```json
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "zhangqirui_course"
}
```

### 5). After you have properly configured the mappings for your index, load a document data to the index with PUT command.

Your command 5:
```json
PUT /zhangqirui_course/_doc/1  
{  
  "course_name": "Machine Learning",  
  "credit": 3,  
  "start_date": "2024-10-16",  
  "score": 90  
}
```

Response 5:
```json
{
  "error": {
    "root_cause": [
      {
        "type": "document_parsing_exception",
        "reason": "[4:17] failed to parse field [start_date] of type [date] in document with id '1'. Preview of field's value: '2024-10-16'"
      }
    ],
    "type": "document_parsing_exception",
    "reason": "[4:17] failed to parse field [start_date] of type [date] in document with id '1'. Preview of field's value: '2024-10-16'",
    "caused_by": {
      "type": "illegal_argument_exception",
      "reason": "failed to parse date field [2024-10-16] with format [yyyy/MM/dd]",
      "caused_by": {
        "type": "date_time_parse_exception",
        "reason": "Text '2024-10-16' could not be parsed at index 4"
      }
    }
  },
  "status": 400
}
```

### 6). Looking up mapping records for the index of "info300_students" and "news" 

Your command 6:
```json
GET /info300_students/_mapping  
GET /news/_mapping
```  

Response 6:
```json
{
  "info300_students": {
    "mappings": {
      "properties": {
        "class": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "color": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "course": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "favor_food": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "favor_fruit": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "favor_university": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "from": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "interest": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "studentID": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        }
      }
    }
  }
}

{
  "news": {
    "mappings": {
      "_meta": {
        "created_by": "file-data-visualizer"
      },
      "properties": {
        "authors": {
          "type": "text"
        },
        "category": {
          "type": "keyword"
        },
        "date": {
          "type": "date",
          "format": "iso8601"
        },
        "headline": {
          "type": "text"
        },
        "ignore_malformed": {
          "type": "boolean"
        },
        "index": {
          "properties": {
            "_index": {
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
        "link": {
          "type": "keyword"
        },
        "short_description": {
          "type": "text"
        }
      }
    }
  }
}
```