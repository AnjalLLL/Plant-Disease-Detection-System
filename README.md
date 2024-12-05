# Plant-Disease-Detection-System
Plant-Disease-Detection-System is a web based application where user can uplode image of plant leave either healthy or diseased and can get the information related to it. This system is build by using django frame work for handelling frontend and backend where as for model training we have use two powerfull algorithms, Convulational Neural Network (CNN) for extracting features and the Random Forest algorithm for classification, ensuring precise and reliable disease detection. Users can upload an image of a diseased plant, and the system processes it by utilizing CNNs to extract critical features such as texture, color, and patterns that are indicative of specific plant diseases. These extracted features are then fed into the Random Forest model, which uses its ensemble of decision trees to classify the disease accurately.
The integration of CNNs for feature extraction ensures that the system captures even the most subtle visual characteristics of plant diseases, while the Random Forest classifier enhances prediction accuracy by aggregating multiple decision paths.

Once the disease is identified, the website provides comprehensive information about it,  causes, preventive measures, and treatment suggestions. Here when the user uplode the image and click on detect button only the partial information ie. whats detected and its discription the user will get further information only after loging in and testing again.

Here we have used MongoDb atlas for storing our user data,plant data and disease data.Here we have created a single database name Project_Database and inside we have created collection named
 user for storing data from signup form and fetching it through login form for user authentication, diseases-data for storing disease-name ,discription ,prevention and treatment and fetching of it is handled by assigning authentication token to user while loging in and storing it in cookies and displaying the full information of the detected diseased or healthy leaf. In this process we have handled our cookies by making our custom folder named middleware.py.we have created another table name plant-info for storing facts about our plants and fetched these data in our slider part. 

The website is user-friendly, responsive, and accessible, making it a valuable tool for farmers, gardeners, and agricultural professionals. By providing timely and accurate disease detection, the platform supports sustainable farming practices and contributes to improved crop health and yield.



Team members : 
Ashmita Timalsina - https://github.com/Ashmita1555
Ruth Ghising - https://github.com/RuthTmg
Anjal Ghimire

