# A Deep Hybrid Learning Approach to Detect Bangla Fake News

## Abstract
Fake news has become a genuine threat to political, economical, religious and social stability. Although there has been an enormous amount of study done on the detection of fake news in English, the possibilities of research remain open for detecting Bangla fake news owing to the resource constraints and the morphological complexity of the Bangla language. In this paper, a deep hybrid model for detecting Bangla fake news is proposed, which utilized a 1D Convolutional Neural Networks (CNN) for the extraction of features and standard Machine Learning techniques for classification. Our presented model enables one to reduce human effort in extracting features from the dataset since the neural network takes the responsibility of it. To our knowledge, no research has been done on classifying fake news in Bangla using deep hybrid learning models combining Deep Learning and Machine Learning models. In the BanFakeNews dataset, our proposed model successfully distinguishes between fake and real news, obtaining a similar performance of around 99% and 82% in the F1 metric as the most other state-of-the-art models for the overall and fake only dataset respectively.
```
@INPROCEEDINGS{9604712,  
    author={Adib, Quazi Adibur Rahman and Mehedi, Md. Humaion Kabir and Sakib, Md. Sadman and Patwary, Kabbya Kantam and Hossain, Md Sabbir and Rasel, Annajiat Alim},   
    booktitle={2021 5th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT)},   
    title={A Deep Hybrid Learning Approach to Detect Bangla Fake News},   
    year={2021},  
    volume={},  number={},  
    pages={442-447},  
    doi={10.1109/ISMSIT52890.2021.9604712}}
```

## Data Description
Dataset available in Kaggle: [BanFakeNews](https://www.kaggle.com/cryptexcode/banfakenews)

In this work, we have used `BanFakeNews` dataset for both trainning and testing.


## Project Tree Structure
```
 .
├── src
│   ├── data_preprocessing.py
│   ├── NN_FeatureExtraction.py
│   ├── model_creation_and_prediction.py
└── README.md
└── workflow.png
```

## 🛠 Tools used

Here, Pandas, Scikit-learn, Tensoflow, Matplotlib, Seaborn are used to build the whole model.

- Visual Studio Code is used as an IDE.
- For visualization of the plots, Matplotlib and Seaborn are used.
