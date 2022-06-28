# chrome-Review

The goal is to identify the reviews where the semantics of review text does not match rating, that is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users.

The data used in the project will be in "chrome_review.csv".

"ipynb" file contains coding for the model to train to get the result.

The model is selected by performing hyper parameter tuning on different algorithms like Logistic regression, Naive Baye's, support vector classifier, random forest classifier and more. The model which gives best accuracy for both train and test dataset is saved and choosen for our solution.

I have deployed it in AWS Ec2 instance, code for deployment is written in "review_api.py" where we load the model and deployed it in "Amazon Web Service EC2 instance" using "Streamlit".
