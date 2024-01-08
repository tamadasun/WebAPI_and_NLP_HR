
![Big Data for HR](https://suyati.com/blog/wp-content/uploads/2015/09/BIG-DATA-FOR-HR.jpg) 



# From Data to Careers: A Subreddit Journey through r/datascience and r/jobs

---

## Overview

This project aims to uncover valuable insights from two diverse subreddits, r/datascience and r/jobs. By analyzing the content of these two subreddits, researchers and stakeholders can gain a better understanding of the job market for data scientists and the types of questions and challenges they face. This can also help inform potential employers of the type of skills and qualifications they are looking for in potential candidates. By utilizing Reddit's API, I will gather posts and apply Natural Language Processing (NLP) techniques to understand and classify posts. Ultimately, the objective is to build classifiers that can be used to determine the origin of a post, to shed light on the unique discussions occurring within the data science and job-seeking communities.

---

## Problem Statement

In my role as a newly onboarded data scientist at a thriving startup, I have been entrusted with a pivotal task — assisting the HR team in identifying the ideal candidate for employment. Navigating the expansive and dynamic realm of online discussions, the HR team and hiring managers have tasked me with distilling invaluable insights from the abundant data available on platforms like Reddit. The overarching objective is to craft a robust classification model capable of discerning whether a post originates from the r/datascience or r/jobs subreddit.

Delving deeper, the goal extends to extracting key characteristics that define an exemplary data scientist, as expressed in these posts. By undertaking this endeavor, we are not only aiming to gain a comprehensive understanding of the distinctive language and concerns embedded in these online communities, but also to provide a practical tool for individuals seeking information that is precisely tailored to their needs.

---

## Questions

What linguistic nuances and thematic elements differentiate posts from the r/datascience and r/jobs subreddits, and how can these distinctions be harnessed to construct a reliable classification model? 

Furthermore, what distinctive characteristics, as reflected in these posts, define an ideal data scientist for our startup, as perceived by the hiring team?

---

## Part 1: Data Wrangling/Gathering/Acquisition

In this section, I will craft a data collection script to retrieve posts from r/datascience and r/jobs, storing information in a structured format. Detailed explanation of the scripts will be highlighted in order to guarantee a continuous flow of relevant data. Emphasis will be placed on user input, API credential storage, and advanced functionality for data cleanup and maintenance.

- Detailed explanation of the data gathering script
- Ensure effective handling of missing values and outliers
- User input for subreddit selection and API credentials
- Script for data collection and transaction log creation
- Bonus explanation and implementation details with relevant summary statistics

---

## Part 2: Natural Language Processing (NLP)

Part 2 will delve into NLP techniques, transforming standard text data from titles and body of post into a format suitable for analysis. Using this approach, an enhanced understanding of the language used in the two subreddits will be gained, enabling a more accurate classification.

- Verify successful conversion of text data to a matrix representation.
- Preprocessing steps for textual data
- Explore methods such as stop words, stemming, and lemmatization.
- Perform Topic Modeling

---

## Part 3: Classification Modeling

The final phase focuses on creating and comparing classification models to understand which model was best in discerning the origin of a post. The goal is to develop a robust and accurate classification system using a combination of logistic regression, Naive Bayes, and KNN. These models will not only provide insights into the distinctive characteristics of each subreddit but also serve as a valuable tool for those navigating the realms of data science and job-seeking. 

- Identify and explain the baseline score for the classification models.
- Provide an explanation of how the chosen model works.
- Select and use metrics that are relevant to the problem objective.
- Ensure proper splitting and/or sampling of data for validation/training purposes.
- Test and evaluate a variety of models, including at least two classification models (KNN, Naive Bayes, logistic regression)
- Evaluate the performance successes and downfalls of the model.

---

## Executive Summary

This project delves into the diverse discussions within the r/datascience and r/jobs subreddits, extracting valuable insights through the analysis of posts. Utilizing Reddit's API, posts utilized Natural Language Processing (NLP) techniques, that contributed to a nuanced understanding of the job market for data scientists. The primary objective was to construct classifiers capable of discerning the origin of a post, shedding light on unique discussions within these communities.

- Model Performance Metrics:
    - **Best Model:** Multinomial Naive Bayes emerges as the preferred choice due to its balanced accuracy, in that it performed well on both the training and testing sets, without overfitting. It achieved the highest cross-validation score of 91.91% between all the other model, indicating it effectiveness in distinguishing between r/datascience and r/jobs posts. Moreover, the model shows high precision and recall for both classes, indicating that the model is effective in correctly classifying posts from both subreddits.
    - **Additional Models:** Logistic Regression demonstrates strong performance, balancing accuracy and generalization. However, there was a slight concern about potential overfitting. The training accuracy is significantly higher (99.77%) than the testing accuracy (89.63%), suggesting that the model may be fitting the training data too closely and may not generalize well to new data.  K- Nearest Neighbors (KNN) exhibits satisfactory results, but compared to other models, it had significantly lower overall  accuracy. KNN model also showed indication of potential overfit as the trainning accuracy was notably higher thann the testing accuracy. All of this indicate potential for further refinement.
- Insight Gained:
    - Leveraging  Latent Dirichlet Allocation (LDA), the project identifies abstract topics within the subreddit posts. Analysis of word clouds reveals key topics extracted from r/datascience topics included General NLP and Data Processing, Python and Web Technologies, Image Processing, Team/Collaboration, and Academic Research/Time Management. From r/jobs topics extracted included Job Search and Interview, Work Experience and Company Knowledge, Retail and Management, and Job Preferences and Desires. 
    - In context of finding the ideal candidate for HR, some key attributes are, the candidate must be 
    1. Technical proficient: Strong proficiency and experience in Python and relevant technologies (evident in topics related to Python, regression, machine learning, web-related technologies data processing, NLP, and image processing.
    2. Good with Collaboration and Team Skills: Demonstrated collaboration and teamwork skills (indicated by topics related to team, experience, and collaboration).
    3. Have familiarity with Academic Research and good with Time Management: Academic research experience and effective time management skills (reflected in topics related to thesis, research, time management, and speed).
    4. Work Experience and Company Knowledge: Relevant work experience and a good understanding of companies and industries (indicated by topics related to work, years of experience, knowledge, and degrees).
    5. Adaptability and Desire for Growth: Willingness to learn and adapt, with a focus on personal and professional growth (indicated by topics related to career, time, better, advice, using, learn) 



---

