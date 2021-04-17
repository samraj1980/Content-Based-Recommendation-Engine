#                                   Content Based Recommendation Engine for Health Care Providers 

[![](https://img.shields.io/badge/authors-%40Sam%20Raj-blue)](https://www.linkedin.com/in/samraj-anand-jeyachandran-pmp-7b273a6/)

## Abstract
A recent evolution of big data technology enables people to handle huge amounts of data which have been collected in healthcare databases representing patients' health states (e.g., as laboratory results, treatment plans, medical reports). Hence, digital information available for patient-oriented decision-making has increased drastically but is often scattered across different data sources. Yet, expert-oriented language, complex interrelations of medical facts and information overload in general pose major obstacles for patients to understand their own record and to draw adequate conclusions. 
In this context, recommendation systems may supply patients as well as physicians with additional laymen-friendly information helping to better comprehend their health status and get answers to commonly known topics. However, such systems must be adapted to cope with the specific requirements in the health domain in order to deliver highly relevant information for physicians. They are referred to as recommendation systems. 


## 1.0 Introduction
InpharmD is a service provider for doctors and pharmacists (healthcare providers) to have better access to better health information, so they can make better decisions. The primary benefit of the service is connecting questions from healthcare providers to customized, evidence-based responses from a nationwide network of academic drug information centers, optimized with advanced machine learning algorithms and search mechanisms. In this project, our team has built a recommendation system to provide meaningful medical articles and references to questions of healthcare providers.


## 2.0 Objective
The goal of a recommendation system is to supply InpharmD users with medical information, which is meant to be highly relevant to the question the healthcare providers are looking for. By Implementing this recommendation system, InpharmD is looking to provide its user base with highly relevant medical information in real time based on similar past responses w/o having to wait for a research analyst to analyze and get back to users after a few hours or days. This will provide a quicker turnaround time, enhance user experience and free up the time of the analysts. 

Depending on the questions, matching healthcare documents in InpharmD would extracted from the repository and rendered in the Web application real time. The system in the backend would execute AI NLP based models, rank existing documents based on similarity to the posed question, and display in a format, which is comprehensible to the physician or Pharmacist.

Data entries in a recommendation database (DB) constitute the medical research documents from InpharmD source database. Such items originate from InpharmD health knowledge repositories and will be displayed as recommendations when a user is about to post a new question online. 

Thus, it is possible to compute and deliver potentially relevant information documents from the recommendation system leveraging the breakthrough innovations in the field of Natural Language processing algorithms. Based on the similarity of the new question with those already present in the repository, the top ‘n’ relevant documents can be rendered.


## 3.0 System Architecture
In this project, we are going to use various content-based recommendation algorithms to come up with recommendations. Based on the results from the three algorithms, we will be evaluating and choosing the model, which renders the best recommendation. We will also be exploring an ensemble approach to determine the common recommendations for the specific question across all the trained models.

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_1.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 1: System Architecture       </a>
        </div>
   </td>
  </tr>
</table>

## 4.0 Data Engineering 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_2.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 2: Data Engineering Flow     </a>
        </div>
   </td>
  </tr>
</table>

### 4.1 DATA SOURCE
InpharmD provided a Json extract from their Medical Repository, which is stored in heroku cloud. This repository contains all the past answered questions posed by health care providers. The Json extract contains about 5,223 documents which is the data we will be using for this project


### 4.2 DATA EXPLORATION 
Please refer to Appendix A where the data attributes and a sample record from the raw file is displayed for reference. 

### 4.3 DATA MINING
After initial analysis of data, we found that there are multiple documents, which were test documents and did not contain any relevant information. We wanted to filter them off before proceeding further with data wrangling. Removed all the documents whose title element has no data. Post this step the number of documents to be considered for further processing dropped down to 4,167 documents. 
We also found that the information that is really required to train the models are present in the following metadata elements. 
1.	id
2.	question
3.	title
4.	custom_response_text
5.	view_everyone
6.	shareable_url
Except for the above-mentioned elements, the rest of the elements dropped. 

### 4.4 DATA WRANGLING 
Before doing feature engineering, the data had to be transformed to a usable format. The following sequence of steps were performed. 
1.	New metadata element called ‘document’ was created and it is essentially a concatenation of title, question, custom response text and background. 
2.	On the document metadata, the following operations were performed. 
a.	Removed all URLs
b.	Removed all punctuations
c.	Converted the entire text to lowercase
d.	Removed all English & Spanish stopwords
e.	Eliminated a set of repeating words which did not add any value 
f.	Normalized some of the keywords as they were represented in different ways (eg: covid19, covid-19, covid, etc) 
g.	Removed words with less than 2 characters 
h.	Removed New line characters
i.	Removed Non printable characters
j.	Removed words with only numbers
k.	Removed all non-alpha-numeric characters in string 

### 4.5 DATA VISUALIZATION 
Word cloud result after Data Wrangling and optimization (removal of non-relevant or conflicting words) was created. 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_3.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 3: Word cloud post Data Wrangling     </a>
        </div>
   </td>
  </tr>
</table>

Top 20 most commonly occurred word pairs (Two Gram) were also analyzed

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_4.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 4: Frequently occurring word pairs       </a>
        </div>
   </td>
  </tr>
</table>

## 5.0 Feature Engineering 
The entire corpus of documents was vectorized using the Term Frequency Inverse Document frequency (TFIDF) vectorizer.  This essentially converts a collection of raw documents to a matrix of TF-IDF features. 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_5.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 5: TF-IDF workings       </a>
        </div>
   </td>
  </tr>
</table>

The output from the TFIDF vectorizer is a sparse matrix where each row is a document, the features or columns are the words occurring in them, and the value is the TF-IDF weights assigned to these words. The total number of features that were derived from this step was 41,683.

## 6.0 MODEL ENGINEERING 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_6.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 6: Model Lifecycle        </a>
        </div>
   </td>
  </tr>
</table>

### 6.1 COSINE SIMILARITY ALGORITHM
Cosine similarity is a metric used to determine how similar the documents are irrespective of their size. Consider a new user question; we first transform/Vectorize the user question using the same trained TF-IDF vectorizer. 
We then calculate the cosine of the angle between two vectors projected in a multi-dimensional space. In this case, the angle between the vectorized user question and each of the vectors (documents) in the sparse matrix is calculated. The smallest cosine angles are extracted and those represent the documents, which is very similar to the user question.  

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_7.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 7: Cosine Similarity        </a>
        </div>
   </td>
  </tr>
</table>

### 6.2 K-NEAREST NEIGHBORS (KNN)
The trained TF-IDF vectorizer is used to train the K-nearest neighbor’s algorithm. The user question is first transformed/vectorized using the trained TF-IDF vectorizer. This vector is then fed to the trained KNN algorithm and the closest neighbors are calculated by measuring the Euclidean distance. The documents with the smallest Euclidean distances are then rendered as recommendations to the user.

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_8.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 8: KNN visualization of Documents in the Corpus       </a>
        </div>
   </td>
  </tr>
</table>

### 6.3 TOPIC MODELING (LDA)
Topic modeling is an unsupervised machine learning modeling approach, which can scan a set of documents, detect words, and phrase patterns. The power of this approach is automatic clustering word group/similar expressions that best characterize a set of documents. Algorithm used for this approach is Latent Dirichlet Algorithm (LDA)
The entire corpus of documents was segmented into topics and the number of topics was adjusted based on the coherence score, which is a method for hyper tuning the model. 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_9.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 9: Topics Segmented by LDA Algorithm        </a>
        </div>
   </td>
  </tr>
  <tr> 
  </tr> 
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_10.png">
    </td>
  </tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 10: Documents tagged to topics in the corpus     </a>
        </div>
   </td>
  
</table>

After the documents are segmented by topic, we can feed the vectorized user question as input to the trained LDA model to get the topic this question is assigned to and then the cosine similarity between the vectorized user question and the subset of corpus which are associated to the same topic is performed to get the documents similar to the user question. 

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_11.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 11: Topic distribution for a User question         </a>
        </div>
   </td>
  </tr>
</table>

### 6.4 TRUNCATED SVD
Truncated Singular Value Decomposition (SVD) is a matrix factorization technique that factors a matrix M into the three matrices U, Σ, and V. This is very similar to PCA, except that the factorization for SVD is done on the data matrix, whereas for PCA, the factorization is done on the covariance matrix. The truncated SVD works well on sparse matrix and gives us the ability to control the number of features or dimensions we want this to be reduced. 
In this case, the total number of features decreased from the original 41,683 to a fraction of about 3000 dimensions. We can feed the vectorized user question as input to the trained Truncated SVD model to get the transformed vector with only 3000 dimensions. Finally, we can apply the cosine similarity between the vectorized user question and the corpus to get the documents similar to the user question.

<table>
  <tr>
     <td>
      <img src="https://github.com/samraj1980/ISYE-6748/blob/main/Images/Screenshot_12.png">
    </td>
  </tr>
  <tr>
  <td>
        <div class="text-purple">
          <a href="#" class="text-inherit">       Fig 12: Determine Optimal Number of Dimensions in TruncSVD         </a>
        </div>
   </td>
  </tr>
</table>
