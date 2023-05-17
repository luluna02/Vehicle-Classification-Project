# Vehicle Classification Project
-Vehicle identity is an image classification project that uses RandomForest
pre-trained model to classify images of vehicles into three categories: 
truck, bike, or car. The program will be able to accurately classify an 
image of a vehicle without prior knowledge of the vehicle's type, after 
being trained on a large dataset of labeled images. 
Accurate identification of different types of vehicles is crucial in 
various industries, including transportation, logistics, and law 
enforcement. The ability to classify images of vehicles accurately and 
efficiently can aid in traffic management and improve safety and security 
on the roads. 


-In this project,the dataset was collected from various sources, including Kaggle and open-source images on the internet.

The Random Forest model was selected based on its simplicity and ability to handle high-dimensional data. We tuned two important hyperparameters, the number of decision trees (n_estimators) and the maximum depth of each tree (max_depth), using a grid search technique.

Evaluation of the model was done using accuracy as the primary metric since the data was perfectly balanced. The Random Forest model achieved an accuracy of 87.6% on the test set, demonstrating its effectiveness in classifying vehicle images. We also used a confusion matrix to analyze specific classes where the model may have struggled.

To showcase the model, we developed a web application using Flask and HTML/CSS. Users can upload an image, and the model predicts the type of vehicle. The application handles file upload, preprocessing, model prediction, and serves the uploaded files to the user.