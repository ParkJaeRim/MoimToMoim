# import numpy as np
# # import surprise  # run 'pip install scikit-surprise' to install surprise
# from surprise import NMF
# from surprise import KNNBasic
# from surprise import SVD
# from surprise.model_selection import cross_validate
# import surprise
# class SVD_SGD(surprise.AlgoBase):
    
#     def __init__(self, learning_rate, n_epochs, n_factors):
        
#         self.lr = learning_rate  # learning rate for SGD
#         self.n_epochs = n_epochs  # number of iterations of SGD
#         self.n_factors = n_factors  # number of factors (몇 개의 Latent Factor로 요인 벡터를 만들지를 정함)
        
#     def train(self, trainset):
#         '''Learn the vectors p_u and q_i with SGD'''
        
#         print('Fitting data with SGD...')
        
#         # Randomly initialize the user and item factors.
#         p = np.random.normal(0, .1, (trainset.n_users, self.n_factors))
#         q = np.random.normal(0, .1, (trainset.n_items, self.n_factors))
        
#         # SGD procedure
#         for _ in range(self.n_epochs):
#             for u, i, r_ui in trainset.all_ratings():
#                 err = r_ui - np.dot(p[u], q[i])
#                 # Update vectors p_u and q_i
#                 p[u] += self.lr * err * q[i]
#                 q[i] += self.lr * err * p[u]
#                 # Note: in the update of q_i, we should actually use the previous (non-updated) value of p_u.
#                 # In practice it makes almost no difference.
        
#         self.p, self.q = p, q
#         self.trainset = trainset

#     def estimate(self, u, i):
#         '''Return the estmimated rating of user u for item i.'''
        
#         # return scalar product between p_u and q_i if user and item are known,
#         # else return the average of all ratings
#         if self.trainset.knows_user(u) and self.trainset.knows_item(i):
#             return np.dot(self.p[u], self.q[i])
#         else:
#             return self.trainset.global_mean

# # data loading. We'll use the movielens dataset (https://grouplens.org/datasets/movielens/100k/)
# # it will be downloaded automatically.
# data = surprise.Dataset.load_builtin('ml-100k')
# print(data)
# #data.split(n_folds=2)  # split data for 2-folds cross validation

# algo = SVD_SGD(learning_rate=.01, n_epochs=10, n_factors=10)
# cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=True)
import pandas as pd
import numpy as np
import surprise # run 'pip install scikit-surprise' to install surprise
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import Reader
total_review_df = pd.read_csv("../data/total_review_df.csv")
# Load the dataset (download it if needed)
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(total_review_df[["user_name","res_id","rating"]],reader)

# Use the famous SVD algorithm
algo = SVD()
print("---------------------------SVD--------------------------------")
# Run 5-fold cross-validation and then print results
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=10, verbose=True)

print()

print("---------------------------테스트--------------------------------")

uid = 1
iid = "형석"
pred = algo.predict(uid,iid,5)
print(pred)

# Use the ALS algorithm
bsl_options = {
    'method': 'als',
    'n_epochs': 5,
    'reg_u': 12,
    'reg_i': 5
}
algo = surprise.BaselineOnly(bsl_options)

print("--------------------------------------------------------------")
print()

print("---------------------------SGD--------------------------------")

cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True, return_train_measures =True)


# Use the SGD algorithm
bsl_options = {
    'method': 'sgd',
    'n_epochs': 5,
    'reg_u': 12,
    'reg_i': 5
}
algo = surprise.BaselineOnly(bsl_options)

cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)

print("--------------------------------------------------------------")
print()
print()

print("---------------------------테스트--------------------------------")

uid = 1
iid = "형석"
pred = algo.predict(uid,iid,5)
print(pred)
print("---------------------------KNN/MSD--------------------------------")
# Use the KNN algorithm
# Use cosine Similarity
sim_options = {'name': 'msd'}
algo = surprise.KNNBasic(sim_options=sim_options)
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)
print("--------------------------------------------------------------")
print()
print()

print("---------------------------테스트--------------------------------")

uid = 1
iid = "형석"
pred = algo.predict(uid,iid,5)
print(pred)
print("---------------------------KNN/COS--------------------------------")
# Use cosine Similarity
sim_options = {'name': 'cosine'}
algo = surprise.KNNBasic(sim_options=sim_options)
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)


print("--------------------------------------------------------------")
print()
print()

print("---------------------------테스트--------------------------------")

uid = 1
iid = "형석"
pred = algo.predict(uid,iid,5)
print(pred)
print("---------------------------KNN/PEARSON--------------------------------")
# Use cosine Similarity
sim_options = {'name': 'pearson'}
algo = surprise.KNNBasic(sim_options=sim_options)
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)

print("--------------------------------------------------------------")
print()

print("---------------------------테스트--------------------------------")

uid = 1
iid = "형석"
pred = algo.predict(uid,iid,5)
print(pred)
