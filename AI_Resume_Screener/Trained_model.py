import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split,RandomizedSearchCV,KFold,cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import joblib

Train_dataset=pd.read_csv("C:/Users/Lenovo/Downloads/AI_Resume_Screening (1).csv")
Train_dataset=Train_dataset.drop(columns=['Resume_ID','Name'])

Train_dataset['Text_cols']=(
    Train_dataset['Skills'].fillna("").astype(str) + " " +
    Train_dataset['Education'].fillna("").astype(str) + " " +
    Train_dataset['Certifications'].fillna("").astype(str)  + " " +
    Train_dataset['Job Role'].fillna("").astype(str)
)
Train_dataset['Recruiter Decision']=LabelEncoder().fit_transform(Train_dataset['Recruiter Decision'])
X=Train_dataset[['Text_cols','Experience (Years)','Salary Expectation ($)','Projects Count','AI Score (0-100)']]
y=Train_dataset['Recruiter Decision']

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

tfidf=TfidfVectorizer(ngram_range=(1,2))

preprocessor=ColumnTransformer([
    ('text',tfidf,'Text_cols'),
    ('nums',StandardScaler(),['Experience (Years)','Salary Expectation ($)','Projects Count','AI Score (0-100)'])
])

model=XGBClassifier(
    random_state=42
)
param_dist = {
    'n_estimators':[100,200,300],
    'max_depth':[1,3,5],
    'learning_rate': [0.1, 0.2]
}
kfold=KFold(n_splits=5,shuffle=True,random_state=42)
random_search = RandomizedSearchCV(
    model,
    param_dist,
    n_iter=10,
    cv=kfold
)

model2=Pipeline([
    ('preprocessor',preprocessor),
    ('classifier',random_search)
])

model2.fit(X_train,y_train)

y_pred=model2.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)

joblib.dump(model2,"resume_model.pkl")
joblib.dump(tfidf,"tfidf.pkl")
print("Model saved Successfully")








