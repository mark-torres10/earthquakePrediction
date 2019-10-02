# Predicting Earthquake Damage (DrivenData competition)

Link to competition: https://www.drivendata.org/competitions/57/nepal-earthquake/

My goal is to predict the extent of damage in an area after an earthquake. To do so, 
I used geographic features and a variety of models to classify the extent of damage. 

After my analysis, the model that I found to work the best was an xgboost model 
with hypertuning. There is still room for further analysis and for improvement 
of the existing model. 

The Rmd files contain code that created my models and predictions. The Jupyter notebooks haven't been updated, but they were an attempt to recreate the code in the Rmd files because there is an algorithm that I would have liked to have run but wasn't possible in R. However, it wouldn't converge in Python either so I decided against it. 
