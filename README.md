# Capstone-Netflix-Movies-and-TV-Shows-Clustering

![netflix-1658388017](https://github.com/sidpatondikar/Capstone-Netflix-Movies-and-TV-Shows-Clustering/assets/83869822/d5e625a9-ef50-48c5-9697-ca25dcdb92cd)


# Project Summary

This project focused on analyzing a dataset of movies and TV shows from Netflix, with the main objective of text-based clustering to group similar content together. The project can be summarized as follows:

After conducting Exploratory Data Analysis (EDA) on the dataset, valuable insights about the content were uncovered. To facilitate clustering, feature engineering was performed, and specific columns, including cast, country, rating, listed_in, and description, were selected for text-based features.

Textual preprocessing involved removing punctuations and stopwords, followed by text-vectorization using the TF-IDF vectorizer, generating 5000 features. To reduce dimensionality and retain meaningful information, Principal Component Analysis (PCA) was applied, resulting in 3000 features explaining 80% of the variance.

Two clustering models, K-Means clustering and Hierarchical clustering, were employed to group the content. For K-Means clustering, the optimal number of clusters (7) was determined using the Elbow Method and Silhouette Analysis. For Hierarchical clustering, dendrogram analysis revealed 8 optimal clusters, and the Agglomerative clustering technique was used.

In conclusion, the Hierarchical Clustering approach yielded the most favorable results, as it effectively differentiated and grouped similar content. The identified clusters can serve as a valuable tool for content organization and recommendation systems, enhancing the overall user experience on the Netflix platform.
