"""
AUTHOR: Sam Raj Anand
DATED:  03/01/2021
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
from flask_restful import Api
from flask.views import MethodView
from json import dumps
from flask import jsonify
import pickle
import os
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
from werkzeug.security import generate_password_hash, check_password_hash
from flask import g

# initialization
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class recommendation(MethodView):
    def get(self):
        # Loading the pickled model and the vectorizer for train dataset
        train_data = pd.read_pickle('train_data.pkl')
        count_vectorizer = pd.read_pickle('count_vectorizer.pkl')
        train_data_tfidf = pd.read_pickle('train_data_tfidf.pkl')

        # Loading the question, username and password
        username_or_token = request.args.get('username')
        password = request.args.get('password')
        question = request.args.get('question')
        method = request.args.get('method')

        if method is None:
            method = "01"


        # Validate the Username and password
        flag = recommendation.verify_password(username_or_token, password)
        # print(username_or_token, password, flag)

        if flag is True:
            # Invoke the Vectorization method passing the question as I/P parameter
            test_data_tfidf = recommendation.vectorize(self, question, count_vectorizer)

            response =  train_data['question'].astype(str) + '|' + train_data['custom_response_text'].astype(str)+ '|' + train_data['background'].astype(str) + '|' + train_data['view_everyone'].astype(str)  + '|' + train_data['shareable_url'].astype(str)

            # Invoke the recommendation picker method to get the top 5 recommendations based on method

            print(method)

            if method == "01": # Similarity Scores Method
                top_n_recs, sorted_sim_scores = recommendation.get_top_n_recommendation_01(self, train_data_tfidf, response.values , test_data_tfidf, n = 5 )
            elif method == "02": # KNN Method
                top_n_recs, sorted_sim_scores = recommendation.get_top_n_recommendation_02(self, train_data_tfidf, response.values , test_data_tfidf, n = 5 )
            else:
                 return {'data': 'Invalid Selection'}, 404

            sorted_sim_scores = sorted_sim_scores.tolist()
            top_n_recs = top_n_recs.tolist()

            d = {'Similarity_Scores': sorted_sim_scores , 'top_n_recs' : top_n_recs}
            recommendation_df = pd.DataFrame(data=d)
            result = recommendation_df.to_dict()
            print(result)
            return {'data': result}, 200

        else:
            return {'data': 'Not Authoorized'}, 404


    def verify_password(username_or_token, password):
        # first try to authenticate by token
        user = User.verify_auth_token(username_or_token)
        if not user:
            # try to authenticate with username/password
            user = User.query.filter_by(username=username_or_token).first()
            if not user or not user.verify_password(password):
                return False
        g.user = user
        return True

    def vectorize(self, question, count_vectorizer):
        test_data_tfidf = count_vectorizer.transform([question])
        return(test_data_tfidf)

    def get_top_n_recommendation_01(self,train_data_tfidf, train_data, test_data_tfidf, n):
        # calculate similarity between the corpus (i.e. the sample "test" data) and the user's question
        similarity_scores = train_data_tfidf.dot(test_data_tfidf.toarray().T)

        # get sorted similarity score indicies
        sorted_indicies = np.argsort(similarity_scores, axis = 0)[::-1]
        #print(sorted_indicies)

        # get sorted similarity scores
        sorted_sim_scores = similarity_scores[sorted_indicies]

       # train_data.loc[sorted_indicies[:n], ['view_everyone','shareable_url']])

        # get top n most similar documents
        top_n_recs = train_data[sorted_indicies[:n]]

        sorted_indicies = sorted_indicies[:n]
        sorted_sim_scores = sorted_sim_scores[:n]

        # return recommendations and corresponding article meta-data
        return top_n_recs , sorted_sim_scores

    def get_top_n_recommendation_02(self,train_data_tfidf, train_data, test_data_tfidf, n):

        from sklearn.neighbors import NearestNeighbors
        n_neighbors = n

        # Finding the n Nearest Neighbors

        KNN = NearestNeighbors(n_neighbors, p=2)
        KNN.fit(train_data_tfidf)
        NNs = KNN.kneighbors(test_data_tfidf, return_distance=True)

        # calculate Nearest Neighbors between the corpus (i.e. the sample "train" data) and the user's question

        # get sorted euclidean distances
        sorted_sim_scores = NNs[0][0][0:]

        # get top n most nearest documents
        top = NNs[1][0]
        top_n_recs = train_data[top]

        # return recommendations and corresponding article meta-data
        return top_n_recs , sorted_sim_scores

api.add_resource(recommendation, '/recommendation') # Route_1


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id'])


if __name__ == '__main__':
    import os
    if not os.path.exists('db.sqlite'):
        db.create_all()
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
