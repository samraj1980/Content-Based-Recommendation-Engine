#                                   Content Based Recommendation Engine for Health Care Providers 

[![](https://img.shields.io/badge/authors-%40Sam%20Raj-blue)](https://www.linkedin.com/in/samraj-anand-jeyachandran-pmp-7b273a6/)

## Abstract
A recent evolution of big data technology enables people to handle huge amounts of data which have been collected in healthcare databases representing patients' health states (e.g., as laboratory results, treatment plans, medical reports). Hence, digital information available for patient-oriented decision-making has increased drastically but is often scattered across different data sources. Yet, expert-oriented language, complex interrelations of medical facts and information overload in general pose major obstacles for patients to understand their own record and to draw adequate conclusions. 
In this context, recommendation systems may supply patients as well as physicians with additional laymen-friendly information helping to better comprehend their health status and get answers to commonly known topics. However, such systems must be adapted to cope with the specific requirements in the health domain in order to deliver highly relevant information for physicians. They are referred to as recommendation systems. 


## Introduction
InpharmD is a service provider for doctors and pharmacists (healthcare providers) to have better access to better health information, so they can make better decisions. The primary benefit of the service is connecting questions from healthcare providers to customized, evidence-based responses from a nationwide network of academic drug information centers, optimized with advanced machine learning algorithms and search mechanisms. In this project, our team has built a recommendation system to provide meaningful medical articles and references to questions of healthcare providers.


## Objective
The goal of a recommendation system is to supply InpharmD users with medical information, which is meant to be highly relevant to the question the healthcare providers are looking for. By Implementing this recommendation system, InpharmD is looking to provide its user base with highly relevant medical information in real time based on similar past responses w/o having to wait for a research analyst to analyze and get back to users after a few hours or days. This will provide a quicker turnaround time, enhance user experience and free up the time of the analysts. 

Depending on the questions, matching healthcare documents in InpharmD would extracted from the repository and rendered in the Web application real time. The system in the backend would execute AI NLP based models, rank existing documents based on similarity to the posed question, and display in a format, which is comprehensible to the physician or Pharmacist.

Data entries in a recommendation database (DB) constitute the medical research documents from InpharmD source database. Such items originate from InpharmD health knowledge repositories and will be displayed as recommendations when a user is about to post a new question online. 

Thus, it is possible to compute and deliver potentially relevant information documents from the recommendation system leveraging the breakthrough innovations in the field of Natural Language processing algorithms. Based on the similarity of the new question with those already present in the repository, the top ‘n’ relevant documents can be rendered.


## System Architecture
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
            <a href="#" class="text-inherit">Fig 1: System Architecture </a>
        </div>
    </td>
  </tr>
</table>


