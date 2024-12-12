
# Python for ElasticSearch

Date: November 20, 2024

The following highlights what you need to create such a python program.

## Preparation

On the shell / command line:

```shell
pip3 install elasticsearch
```

## Test Your Connection to TUX-ES Cluster

First, create a ```suwei_search.py``` to test connection to our ElasticSearch cluster with your username and password.

```python

from elasticsearch import Elasticsearch


es = Elasticsearch(
    ['http://172.16.249.198:9200'],
    http_auth=('YourUserName', 'YourTuxElasticSearchPassword'),
)

print(es.info())
```

Then, run the test program on the command line:

```shell
python3 suwei_search.py
```

If you see the following in your output, you are good to go:

```json
{
  'name': 'node-1', 
  'cluster_name': 'elasticsearch', 
  'cluster_uuid': 'lzV9EP8rTaiXPETd0bluHQ', 
  'version': 
  {
    'number': '8.10.2', 
    'build_flavor': 'default', 
    'build_type': 'tar', 
    'build_hash': '6d20dd8ce62365be9b1aca96427de4622e970e9e', 
    'build_date': '2023-09-19T08:16:24.564900370Z', 
    'build_snapshot': False, 
    'lucene_version': '9.7.0', 
    'minimum_wire_compatibility_version': '7.17.0', 
    'minimum_index_compatibility_version': '7.0.0'
  }, 
  'tagline': 'You Know, for Search'
}
```

Note that, in addition to the above, you will get warnings against an unverified certificate because of options ```context.check_hostname = False```
and ```context.verify_mode = ssl.CERT_NONE```. This is okay for now as you can trust our servers at CCI.

## Code to Create an Index and Create a Document

Now you can add the following after the authentication code:

```python
from datetime import datetime
doc = {
    'author': 'Zhang Qirui',
    'text': 'Information Retrieval Systems 2024',
    'timestamp': datetime.now(),
}

# Load the doc to an index as doc #1
res = es.index(index="zhangqirui_python2024", id=1, document=doc)

# Show results from server response
print(res['result'])
```

This should index the document and, if successful, return the following result:

```
created
```

## Code to Query and Show Results

Now you can test a search query such as:

```python
# query to search on title and content fields
keywords = "Presidential Election"
query2=  {
    "multi_match" : {
      "query": keywords,
      "fields": ["headline", "short_description" ]
    }
  }

# issue the query to elastic search
res = es.search(index="news",query=query2,from_=0,size=20)
# show the number of hits (matches)
print("Got %d Hits:" % res['hits']['total']['value'])
# show the results with author and title information
a=0
for hit in res['hits']['hits']:
    a=a+1
    print(a,end=". ")
    print("%(authors)s: %(headline)s \n" % hit["_source"])
```

## For More

This gives you a starting point to program in Python to create a front end for your ElasticSearch index. There is much more you can do from here:

You want to make this interactive and should ask for user's query input, for example:

```python
print("Please enter your search query: ")
keywords = input()
```

For more about you can do with the Python APIs for ElasticSearch, consults the following references.


## References

+ https://elasticsearch-py.readthedocs.io/en/master/
+ https://elasticsearch-py.readthedocs.io/en/master/api.html
