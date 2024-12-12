# INFO 300 Assignment 3

## 1. Student(s)

+ Weimao Ke, wk77@drexel.edu
+ John Smith, jps2020@drexel.edu

## 2. Tasks and Steps

## 2.2. Identification of Use Cases (2 points)

### 2.2.1 Use Case 1: Narrow Keywords

Keywords: environmental protection

Brief description of information need: The field of articles I found that related to the issues of environmental protection


### 2.2.2 Use Case 2: Broad Keywords

Keywords: CO2

Brief description of information need: Articles related to CO2


### 2.2.3 Use Case 3: Author + Broad Keywords

Keywords:Wu, SB (Wu, Shengbo) CO2

Brief description of information need: Articles writen by Wu, SB (Wu, Shengbo) related to CO2


## 2.3. Basic Search and Scoring

### 2.3.1 Use Case 1: Basic Search (1 points)

Request:
```json
 GET /zhangqirui_articles/_search
 {
   "from" : 0, "size" : 3,
   "query": {
     "multi_match" : {
       "query": "environmental protection",
       "fields": [ "author", "title", "abstract" ]
     }
   }
 }
```

Results (top 3) in table:

| Doc ID | Author             | Title                                 | Score |
|--------|--------------------|---------------------------------------|-------|
|   14   |Weidner, T (Weidner, Till)|Energy optimisation of plant factories and greenhouses for different climatic conditions|3.0993161|
|   10   |Ng, KS (Ng, Kok Siew)|Global biorenewable development strategies for sustainable aviation fuel production|2.7277792|
|    3   |Huo, JL (Huo, Jinlin)|Integrated network pharmacology and intestinal flora analysis to determine the protective effect of Xuanbai-Chengqi decoction on lung and gut injuries in influenza virus-infected mice|2.1660666|

### 2.3.2 Use Case 2: Basic Search (1 points)

Request:
```json
 GET /zhangqirui_articles/_search
 {
   "from" : 0, "size" : 3,
   "query": {
     "multi_match" : {
       "query": "CO2",
       "fields": [ "author", "title", "abstract" ]
     }
   }
 }
```

Results in table:

| Doc ID | Author                       | Title                                                              | Score |
|--------|------------------------------|--------------------------------------------------------------------|-------|
|   8    |Bullock, LA (Bullock, Liam A.)|Kinetics-informed global assessment of mine tailings for CO2 removal|3.1649363|
|   5    |Xing, L (Xing, Lei) |Potential of enhanced weathering of calcite in packed bubble columns with seawater for carbon dioxide removal| 2.559362|
|   17    | Xing, L (Xing, Lei)|Enhanced weathering to capture atmospheric carbon dioxide: Modeling of a trickle-bed reactor|2.3954537|


### 2.3.3 Use Case 3: Basic Search (1 points)

Request:
```json
  GET /zhangqirui_articles/_search
 {
   "from" : 0, "size" : 3,
   "query": {
     "multi_match" : {
       "query": "Wu, SB (Wu, Shengbo) environmental protection",
       "fields": [ "author", "title", "abstract" ]
     }
   }
 }
```

Results in table:

| Doc ID | Author             | Title                                 | Score |
|--------|--------------------|---------------------------------------|-------|
|   4    |Wu, SB (Wu, Shengbo)|Machine learning aided construction of the quorum sensing communication network for human gut microbiota|8.036458|
|   12   |Wu, SB (Wu, Shengbo)|QSIdb: quorum sensing interference molecules|8.036458|
|   11   |Wu, SB (Wu, Shengbo)|Combinational quorum sensing devices for dynamic control in cross-feeding cocultivation|8.036458|


### 2.3.4 Use Case 3: Boosted Search (1 points)

Request:
```json
  GET /zhangqirui_articles/_search
 {
   "from" : 0, "size" : 3,
   "query": {
     "multi_match" : {
       "query": "Wu, SB (Wu, Shengbo) environmental protection",
       "fields": [ "author^3", "title", "abstract" ]
     }
   }
 }
```

Results in table:

| Doc ID | Author             | Title                                 | Score |
|--------|--------------------|---------------------------------------|-------|
|    4   |Wu, SB (Wu, Shengbo)|Machine learning aided construction of the quorum sensing communication network for human gut microbiota|24.109375|
|   12   |Wu, SB (Wu, Shengbo)|QSIdb: quorum sensing interference molecules|24.109375|
|   11   |Wu, SB (Wu, Shengbo)|Combinational quorum sensing devices for dynamic control in cross-feeding cocultivation|24.109375|

### 2.3.4 Comparison and Discussion
1. Refine keyword search (use case 1): A multi-field search for the keyword "environmental protection" yielded some research articles related to the environment. The results show that although the more relevant documents present a variety of topics, there are not many articles that are directly related to "environmental protection".

2. Broad keyword search (use case 2): Search results for "CO2" show a range of articles on the topic of carbon dioxide, which cover a wide range of content from practical applications to policy recommendations. At this point, using a wide range of keywords can lead to more relevant research, showing the diversity of the topic.

3. Author plus broad keyword search (use case 3): By combining the author's name with the keyword "environmental protection", the results show that the author's related research is relatively concentrated and has a high score, showing the influence of the author's research in a specific field.

4. Enhanced Search (Use Case 4): A weighted search for "Wu, SB (Wu, Shengbo) Environmental Protection" was performed with the weight of the author field set to a higher (^3) and the score of the results was significantly improved.



There are pros and cons to refinement and broad keyword search, with the former providing focused relevance and the latter showcasing broader research context and trends.

Combining author information with subject keywords can significantly improve the relevance of search results, especially when looking for expert research in a specific field.

By enhancing the search strategy, especially the weight adjustment, the relevant research of important authors can be better highlighted, which helps users to obtain high-impact literature.




## 2.6. Setup for Custom Scoring and Similarity

```json
PUT /zhangqirui_papers/_mapping  
{  
  "properties": {  
    "author": {  
      "type": "text"  
    },  
    "title": {  
      "type": "text",  
      "analyzer": "english"  
    },  
    "abstract": {  
      "type": "text",  
      "analyzer": "english"  
    },  
    "citations": {  
      "type": "integer"  
    }  
  }  
}
```

Impact: This mapping defines the structure of the zhangqirui_papers index, establishing the data types for each field. The author, title, and abstract fields are set as text, allowing for full-text search capabilities, while citations is defined as an integer to store citation counts. The use of the English analyzer for title and abstract fields will help in processing and indexing English texts effectively, enhancing search relevance.

### 2.6.1 Custom Similarity (0.5 point)

```json
 PUT /zhangqirui_papers
 {
   "settings":{
     "index":{
       "similarity":{
         "my_bm25":{
           "type":"BM25",
           "k1":2.0,
           "b":1.0
         },
         "my_dfr":{
           "type":"DFR",
           "basic_model":"g",
           "after_effect":"l",
           "normalization":"h2",
           "normalization.h2.c":"3.0"
          }
        }
     }
    }
}
```

Impact:This command creates the zhangqirui_papers index with specified custom similarity settings for BM25 and DFR models. The BM25 configuration uses parameters that fine-tune how term frequency and document length affect scoring, while the DFR settings introduce a probabilistic model that focuses on term distribution. Together, these similarities enhance the precision and relevance of search results.

### 2.6.2 Abstract Field with the Custom BM25 Similarity (0.5 point)

```json
PUT /zhangqirui_papers/_mapping
{
  "properties":{
    "abstract":{
      "type":"text",
      "analyzer":"english",
      "similarity":"my_bm25"
    }
}}
```

Impact:By assigning the custom BM25 similarity to the abstract field, search results that rely on this field will be more relevant, particularly for documents where the abstract captures critical information. This setting optimizes the search based on the terms contained in abstracts, leveraging the parameters of BM25 to provide results that are more aligned with user queries.

### 2.6.3 Title Field with the Custom DFR Similarity (0.5 point)

```json

PUT /zhangqirui_papers/_mapping
{
  "properties":{
    "abstract":{
      "type":"text",
      "analyzer":"english",
      "similarity":"my_dfr"
    }
}}
```

Impact:Applying the custom DFR similarity to the title field enhances the precision of search hits based on document titles, as the DFR model accounts for term rarity and document frequency in a probabilistic manner. This allows for efficient retrieval of documents that closely match the title queries, especially valuable when users are looking for specific papers or articles.

### 2.6.4 Author Field with Boolean Similarity (0.5 point)

```json
PUT /zhangqirui_papers/_mapping
{
  "properties":{
    "author":{
      "type":"text",
      "analyzer":"standard",
      "similarity":"boolean"
    }
}}
```

Impact:Setting the author field to use Boolean similarity means that the search will return results only when there’s an exact match for the author’s name. This configuration is crucial for ensuring accuracy in author searches, preventing irrelevant documents from appearing when users are looking for works by specific authors.

### 2.6.5 Citations Field as a Rank Feature (0.5 point)

```json
PUT /zhangqirui_papers/_mapping
{
  "properties":{
     "citations":{
       "type":"rank_feature",
       "positive_score_impact":true
     }
}}
```

Impact:Defining the citations field as a rank feature allows the Elasticsearch index to factor citation counts into the scoring of search results. Documents with higher citation counts will receive a boost in relevance during searches, making it easier for users to find influential and highly-referenced works. This feature plays a significant role in highlighting impactful literature in academic searches.

## 2.7. Index Documents in the New Index (0.5 point)

Code to reindex:

```json
POST _reindex  
{  
  "source": {  
    "index": "zhangqirui_articles"  
  },  
  "dest": {  
    "index": "zhangqirui_papers"  
  }  
}
```


## 2.8. Search with Custom Scoring and Boosting

### 2.8.1 Use Case 1: Search with Custom Scoring (1 points)


Request:
```json
 GET /zhangqirui_papers/_search
 {
   "from" : 0, "size" : 3,
   "query": {
     "multi_match" : {
       "query": "environmental protection",
       "fields": [ "author", "title", "abstract" ]
     }
   }
 }
```

Results in table:

| Doc ID | Author             | Title                                 | Score |
|--------|--------------------|---------------------------------------|-------|
|   14   |Weidner, T (Weidner, Till)|Energy optimisation of plant factories and greenhouses for different climatic conditions|3.4454405|
|   10   |Ng, KS (Ng, Kok Siew)|Global biorenewable development strategies for sustainable aviation fuel production|2.310903|
|    3   |Huo, JL (Huo, Jinlin)|Integrated network pharmacology and intestinal flora analysis to determine the protective effect of Xuanbai-Chengqi decoction on lung and gut injuries in influenza virus-infected mice|1.9597646|

Comparison:
In both indexes,Doc ID 14(Weidner, T) consistently ranked first, but scored higher in zhangqirui papers (3.4454405) than zhangqirui articles (3.0993161). Doc ID 10(Ng, KS) ranked second in both results, but its score was reversed in both indexes: the score of zhangqirui articles (2.7277792) was higher than that of zhangqirui papers(2.310903), indicating a higher score in zhangqirui articles In line with the query conditions Doc ID 3(Huo, JL) also ranked third in both indexes, but there was a slight decline in the scores of both indexes, with Doc ID 3 performing slightly worse than the other documents, showing a depreciation in the scores across the different indexes (from 2.1660666 to 1.9597646). Documents in zhangqirui papers generally score higher, especially those that rank first, probably because the index is defined with a greater focus on text relevance and possible similarity calculations for zhangqirui articles The drop in the index appears to be more pronounced under specific topics than in previous documents, possibly due to configuration or similarity Settings of other fields


### 2.8.2 Use Case 2: Search with Custom Scoring (1 points)

Request:
```json
GET /zhangqirui_papers/_search
{
  "query":{
    "bool":{
      "must":[
        {
          "match":{
            "abstract":"CO2"
          }
        }
      ],
    "should":{
      "rank_feature":{
        "field":"citations",
        "saturation":{
          "pivot":5
        }
      }
    }
  }
}}
```

Results in table:

| Doc ID | Author             | Title                                 | Score |
|--------|--------------------|---------------------------------------|-------|
|   19   |Yang, ZM (Yang, Ziming)|Modeling and Upscaling Analysis of Gas Diffusion Electrode-Based Electrochemical Carbon Dioxide Reduction Systems|2.3163185|
|    7   |Devlin, A (Devlin, Alexandra)|Regional supply chains for decarbonising steel: Energy efficiency and green premium mitigation|2.158479|
|    5   |Xing, L (Xing, Lei)|Potential of enhanced weathering of calcite in packed bubble columns with seawater for carbon dioxide removal|2.1461253|

Comparison: In table2, we search the index and find documents that contain CO2 from multiple fields; While in table6, we used boolean search, "must" make sure that the field "abstract" must contain "CO2". So the search results of these two tables are different.


# 3. Questions (3 points)

## 3.1 Question 1
Best query: For the enhanced search for use case 3, this query performed best and returned the highest score for the documents, especially the documents written by Wu SB(Wu, Shengbo) whose weighting of the author field significantly improved the relevance of the results, indicating that the documents for that particular author got the right prioritization Worst query: The basic search for use case 1, with the keyword environmental protection, returned documents that, while relevant, failed to focus on the topic, and the results included a number of articles not directly related to environmental protection, showing the lack of specificity of the query compared to what was expected: The enhanced search effectively prioritizes relevant documents and meets expectations. However, the basic search fails to meet expectations of concreteness.

## 3.2 Question 2
Similarities: PageRank and citation score both measure the impact or importance of an article in a network and both can indicate the relevance of an article based on how it is connected to other articles. Indicates that the number of times an article has been cited by other articles reflects the PageRank score of the article's direct impact in academia: This is based on the structure of the citation network, taking into account not only the number of citations, but also the quality and relevance of the articles cited. An article cited by a high-impact paper will have a higher PageRank score than an article cited by an obscure work, even if the latter has more citations PageRank provides a qualitative assessment based on the context of the reference

## 3.3 Question 3
Replacing reference fields with PageRank fields in ranking features may improve the relevance and quality of search results for the following reasons: PageRank considers the quality of the cited article, meaning that if an article is cited by a more influential paper, its ranking will be higher, which can lead to more meaningful robustness of search results: Citation counts can be artificially elevated through self-citation or citations, while PageRank is less susceptible to such manipulation. In short, using PageRank instead of citation counts may lead to more refined and context-relevant article rankings, thereby increasing user satisfaction with search results