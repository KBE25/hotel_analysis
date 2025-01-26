<img src="images/hotel.jpg">

[Credit: vecteezy.com](https://www.vecteezy.com/photo/44153869-beautiful-interior-view-of-a-room-at-coastal)

# Hotel Analysis

**Author: <a href="https://www.linkedin.com/in/karina-basto-eyzaguirre-203a0445/"> Karina Basto-Eyzaguirre</a>**

## Business Understanding
The rise of online booking platforms has significantly increased cancellation rates, posing a major financial challenge for hotels. Beyond revenue loss, cancellations disrupt hotel operations. To address these challenges and improve our hotel's overall efficiency, I propose developing a predictive model to forecast hotel booking’s cancellations. This will enable my company to carefully balance occupancy rates with the risk of denied stays, ultimately optimizing revenue, enhancing operational efficiency, and improving the guest experience.

## Data Understanding
To complete this analysis I used the <a href="https://www.kaggle.com/datasets/youssefaboelwafa/hotel-booking-cancellation-prediction/data">Hotel Booking Cancellation Prediction</a> dataset from Kaggle. This comprehensive dataset has information from 2017-2018 with 36,285 unique lines and 17 columns. 

This dataset is a valuable resource for building a classification model as it encompasses a good variety of features. These features provide insights into factors that influence guest behavior and cancellation tendencies.

## Data Preparation
To prepare the data for modelling I completed four different steps:
1. Data Cleaning: I identified null values and duplicates as well as drop unnecessary columns and rows.
2. Feature Engineering: I created the total_guest feature and transform target feature as well as date of reservation.
3. Feature Selection: I run a correlation matrix to identify highly correlated features and then determine the best features to keep in the model by using OLS, Linear Regression Models and a Decision Tree.
4. Data Transformation: I encoded the categorical features and scale the numerical values. I also defined the Target and Feature dataframes to use in the modelling part.

## ModelLing and Evaluation
As the analysis has a binary outcome because I am predicting if a hotel booking will be cancelled or not, I used a Logistic Regression as my baseline model. For my initial model I evaluated p-values based on an alpha = 0.05 and removed the features that were not statistically significant. Once I had a dataframe with only statistically significant features, I ran three additional Logistic Regressions, one without incorporating class imbalances, a second one using class weight, and a final one using SMOTE.

The next model I run was a Decision Tree Classifier. For this model I ran a baseline model and then optimized my model using 'precision' by running a GridSearchGV based on these parameters: `max_depth`, `min_samples_split`, `min_samples_leaf`, `class_weight` and `criterion`.

My final model is a ***Decision Tree Classifier*** with the `max_depth`= 13, `min_samples_split`= 2, `min_samples_leaf`= 2, `class_weight`= 'None' and `criterion` = 'gini'. Based on the ***evaluation metrics, this model has an accuracy of 88%, precision 82%, recall 80%, F1 score 81% and AUC of 92%***. These metrics show that this model is high in precision which means that when the model predicts a cancellation, it is likely to be correct, which is really important to help minimize False Positives. The recall demonstrates that the model is better at identifying actual cancellations compared to the baseline model, while the high AUC further supports the model's ability to distinguish between the two classes (cancelled hotel bookings vs not cancelled). Overall, these metrics suggest that the model is performing well and can be used to make reliable predictions on new data.

## Recommendations
Based on my  analysis my recommendations are the following:
1. Start with a cautious overselling strategy (5%-10%) while monitoring the metrics. Keep adjusting the overselling rates based on the metrics.
2. Investigate the impact of the top 5 features influencing Hotel Booking Cancellations (`lead_time`, `average_price`, `special_requests`, `market_segment_offline` and `total_guests`). Based on the investigation, develop mitigation strategies for each feature.
3. Create a "Check with Guest" Program focusing on high-risk bookings (long lead times, high-priced bookings, large groups). Developed the program tailoring to the individual booking characteristics and offer incentives to encourage early confirmation.


#### Limitations of the analysis
1. The dataset only contains information from 2017-2018.
2. Key Hospitality Market Trends not incorporated into the model.
3. Final model only has a precision of 82%.
   
## For More Information:
See the full analysis in the <a href="https://github.com/KBE25/hotel_analysis/blob/main/notebook.ipynb">Jupyter Notebook</a>.
The business information can also be found in <a href="https://github.com/KBE25/hotel_analysis/blob/main/presentation%20.pdf">this presentation. </a>

For additional info, contact Karina Basto-Eyzaguirre at karinabastoe@gmail.com.

### Repository Structure
- <a href="https://github.com/KBE25/hotel_analysis/tree/main/images"> images </a>
- <a href="https://github.com/KBE25/hotel_analysis/blob/main/.gitignore"> .gitignore </a>
- <a href="https://github.com/KBE25/hotel_analysis/blob/main/README.md"> README.md </a>
- <a href="https://github.com/KBE25/hotel_analysis/blob/main/helper.py"> helper.py </a>
- <a href="https://github.com/KBE25/hotel_analysis/blob/main/notebook.ipynb"> notebook.ipynb </a>
- <a href="https://github.com/KBE25/hotel_analysis/blob/main/presentation%20.pdf"> presentation </a>

### Resources
- <a href="https://www.ahla.com/">American Hotel and Lodging Association</a>
- <a href="https://www.phocuswright.com/Travel-Research/Hotels-Lodging">Phocuswright: Hotels & Lodging</a>
- <a href="https://www.mirai.com/blog/cancellations-on-booking-com-104-more-than-on-the-hotel-website-expedia-31-more/"> Cancellations on Booking.com: 104% more than on the hotel website. Expedia, 31% more</a>