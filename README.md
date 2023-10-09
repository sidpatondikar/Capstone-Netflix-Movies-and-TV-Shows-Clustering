# Capstone-Netflix-Movies-and-TV-Shows-Clustering

## Recommender System App : Deployed
https://netflix-recommender-system-sidpatondikar.streamlit.app/


-------------------------------------------------------------------
![image](https://github.com/sidpatondikar/Capstone-Netflix-Movies-and-TV-Shows-Clustering/assets/83869822/8a40d866-2ff5-4dc5-b0f0-eb6ad883990a)



## Project Summary

### Objective
The objective of the Netflix Movies and TV Show clustering project is to improve content organization and enhance the recommendation system on the Netflix platform.
By clustering similar content together, Netflix can achieve the following business objectives:
- Content Discovery: Improve how users discover content by grouping similar movies and TV shows together.
- Personalized Recommendations: Enhance the recommendation system by suggesting content from the same clusters to users.
- Content Curation: Enable thematic content collections for easier user navigation and engagement.
- Content Licensing: Make informed decisions about licensing and acquiring new content based on cluster insights.
- User Engagement: Increase user engagement and retention by offering content that aligns with individual preferences.

-----------------------------------------------------------------------------
### Key EDA Insights
1. Content Disparity : 69.1% are movies and 30.9% are shows
2. Alastair Fothergill stands out as the director with the highest number of TV shows on Netflix, having directed 3 shows.
3. Raul Campos and Jan Suter share the top position, each having directed an impressive 18 movies on Netflix.
4. Takahiro Sakurai leads the list of actors with the highest number of TV show appearances on Netflix, having acted in an impressive 22 shows, whereas Anupam Kher holds the top position for actors with the most movie appearances on Netflix, boasting 41 movies.
5. The United States leads the chart with an impressive production count of over 2,500 Netflix Original movies and TV shows.
6. Most of the content on Netflix is released in 2000 or later. 2018 being the year in which most content was added.
7. The majority of movies and TV shows on Netflix fall into the TV-MA (Mature Audiences Only) category, followed closely by TV-14 (For Children 14+ with parental company).
8. The U.S. content primarily caters to mature viewers on Netflix, with over 800 titles in this category. In contrast to the trend observed in most top countries, India and Egypt have a significant number of titles rated for audiences aged 14 and above (TV-14).
9. The majority of movies on Netflix have a running time of around 100 minutes and the majority of TV shows on Netflix have a single season.
10. The top genre on Netflix is International Movies, which primarily refers to non-English movies, reflecting the significant demand for foreign content on our platform. The least popular genre on Netflix is LGBTQ Movies, followed by genres like Sci-Fi Fantasy shows and Sport Movies.
11. The most frequently used words in content descriptions are 'Life,' 'Family,' 'Find,' and 'Love.' These recurring themes indicate that the primary focus of most movies on Netflix revolves around life, family, and the search for love.
12. Among the top 10 countries, India has the highest ratio of movies to TV shows on Netflix. In contrast, South Korea has the highest ratio of TV shows to movies on Netflix among the top 10 countries.
13. A significant portion, 63.72%, of the content on Netflix consists of licensed or added content, while 36.28% is produced by Netflix.
14. Netflix initiated its foray into original content production, primarily in 2013. Among its original content, Netflix has been directing a greater portion of its investments towards TV shows than movies in recent years.

---------------------------------------------------------------------------------

### Impact Quantification

The project resulted in deployment of recommender system application on Streamlit for Netflix. Enhancing content curation with clustering and content recommendation with recommender system, thus increasing user engagement and satisfaction


Two clustering models, K-Means clustering and Hierarchical clustering, were employed to group the content. For K-Means clustering, the optimal number of clusters (7) was determined using the Elbow Method and Silhouette Analysis. For Hierarchical clustering, dendrogram analysis revealed 8 optimal clusters, and the Agglomerative clustering technique was used.

In conclusion, the Hierarchical Clustering approach yielded the most favorable results, as it effectively differentiated and grouped similar content. The identified clusters can serve as a valuable tool for content organization and recommendation systems, enhancing the overall user experience on the Netflix platform.
