# -*- coding: utf-8 -*-
"""Submission 2 MLT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/103ytl_GbQ3z5l0klAfxW7nQiS1ksacQk

# Sistem Rekomendasi : Film

## Content Based Filtering

### Data Understanding
"""

import pandas as pd
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

!gdown 1O72Dk-39aDykDIbGtvblCiBhzdqoJZt-

!gdown 1lG9UpK-auXf-f_kNHPy4nAoXfwZhaukH

movie = pd.read_csv('/content/movies.csv')
movie

movie.info()

movie.isna().sum()

movie.isnull().sum()

print('Banyak data: ', len(movie.movieId.unique()))
print('Jumlah judul: ', len(movie.title.unique()))
print('Jenis genre film: ', len(movie.genres.unique()))
print('Jenis genre film: ', movie.genres.unique())

movie.describe()

rating = pd.read_csv('/content/ratings.csv')
rating

rating.info()

rating.isna().sum()

rating.isnull().sum()

rating.describe()

print('Jumlah userId: ', len(rating.userId.unique()))
print('Jumlah movieId: ', len(rating.movieId.unique()))

"""### Exploratory Data Analysis

#### Univariate

##### Movie Variabel
"""

movie.groupby('genres')['genres'].agg('count')

"""##### Rating Variabel"""

plt.hist(rating.rating, color='#B4E1FF', edgecolor='black')
plt.ylabel('Total')
plt.xlabel('Rating')
plt.title("User Movie Ratings Distribution")
plt.show()

"""### Multivariate"""

rating_contribution = rating.groupby('movieId').count()
rating_contribution.head(3)

name_movie_rating_contribution = pd.merge(rating_contribution, movie, on = 'movieId', how = 'left')
name_movie_rating_contribution.sort_values(by = 'rating', ascending = False).head(10)

plt.figure(figsize = (20,15))
top10_movie = name_movie_rating_contribution[['title', 'rating']].sort_values(by = 'rating', ascending = False).head(10)

colors = ['#87255B', '#56CBF9', '#F5D491', '#BEB7A4', '#B4E1FF', '#F06C9B', '#D3C4D1', '#81F4E1', '#C2AFF0', '#C57B57']

labels = top10_movie[['title']].values.flatten()
values = top10_movie[['rating']].values.flatten()

plt.barh(labels, values, color = colors, edgecolor='black')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.title("Top 10 Movie Rating Contribution", fontdict = {'fontsize' : 20})
plt.show()

"""### Data Preprocessing

#### Menggabungkan Film
"""

movie = pd.merge(rating, movie , on = 'movieId', how = 'left')
movie

movie.isna().sum()

movie.isnull().sum()

"""### Data Preparation

#### Hapus Duplikasi
"""

movie = movie.drop_duplicates('movieId')
movie

movie_id = movie['movieId'].tolist()
movie_title = movie['title'].tolist()
movie_genre = movie['genres'].tolist()
 
print(len(movie_id))
print(len(movie_title))
print(len(movie_genre))

movie_new = pd.DataFrame({
    'id': movie_id,
    'title': movie_title,
    'genre': movie_genre
})
movie_new

"""### Model Developement"""

data = movie_new
data.sample(5)

"""#### TF-IDF Vectorizer"""

tf = TfidfVectorizer()
tf.fit(data['genre']) 
tf.get_feature_names()

tfidf_matrix = tf.fit_transform(data['genre'])
tfidf_matrix.shape

tfidf_matrix.todense()

pd.DataFrame(
    tfidf_matrix.todense(), 
    columns = tf.get_feature_names(),
    index = data.title
).sample(22, axis = 1).sample(10, axis = 0)

"""#### Consine Similarity"""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index = data['title'], columns = data['title'])
print('Shape:', cosine_sim_df.shape)
 
cosine_sim_df.sample(5, axis = 1).sample(10, axis = 0)

"""#### Mendapatkan Rekomendasi"""

def movie_recommendations(title, similarity_data = cosine_sim_df, items = data[['title', 'genre']], k = 5):
    index = similarity_data.loc[:, title].to_numpy().argpartition(range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k + 2):-1]]
    closest = closest.drop(title, errors = 'ignore')
    return pd.DataFrame(closest).merge(items).head(k)

data[data.title.eq('Toy Story (1995)')]

movie_recommendations('Toy Story (1995)')

"""## Collaborative Filtering

### Data Understanding
"""

df = rating
df

"""### Data Preparation"""

user_ids = df['userId'].unique().tolist()
print('list userID: ', user_ids)

user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

movie_ids = df['movieId'].unique().tolist()

movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

df['user'] = df['userId'].map(user_to_user_encoded)

df['movie'] = df['movieId'].map(movie_to_movie_encoded)

num_users = len(user_to_user_encoded)
print(num_users)

num_movie = len(movie_encoded_to_movie)
print(num_movie)

df['rating'] = df['rating'].values.astype(np.float32)

min_rating = min(df['rating'])

max_rating = max(df['rating'])

print('Number of User: {}, Number of Movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movie, min_rating, max_rating
))

"""#### Membagi Data untuk Training dan Validasi"""

df = df.sample(frac = 1, random_state = 42)
df

x = df[['user', 'movie']].values

y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""### Proses Training"""

import tensorflow as tf
class RecommenderNet(tf.keras.Model):

  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.movie_embedding = layers.Embedding(
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1)
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:, 0])
    user_bias = self.user_bias(inputs[:, 0])
    movie_vector = self.movie_embedding(inputs[:, 1])
    movie_bias = self.movie_bias(inputs[:, 1])
 
    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2) 
 
    x = dot_user_movie + user_bias + movie_bias
    
    return tf.nn.sigmoid(x)

model = RecommenderNet(num_users, num_movie, 50)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate = 0.001),
    metrics = [tf.keras.metrics.RootMeanSquaredError()]
)

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""### Visualisasi Metrik"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc = 'upper right')
plt.show()

"""### Mendapatkan Rekomendasi Movie"""

movie_df = movie_new
df = pd.read_csv('ratings.csv')

user_id = df.userId.sample(1).iloc[0]
movie_watched_by_user = df[df.userId == user_id]

movie_not_watched = movie_df[~movie_df['id'].isin(movie_watched_by_user.movieId.values)]['id'] 
movie_not_watched = list(
    set(movie_not_watched)
    .intersection(set(movie_to_movie_encoded.keys()))
)

movie_not_watched = [[movie_to_movie_encoded.get(x)] for x in movie_not_watched]
user_encoder = user_to_user_encoded.get(user_id)
user_movie_array = np.hstack(
    ([[user_encoder]] * len(movie_not_watched), movie_not_watched)
)

ratings = model.predict(user_movie_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_watched[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_watched_by_user.sort_values(
        by = 'rating',
        ascending = False
    )
    .head(5)
    .movieId.values
)

movie_df_rows = movie_df[movie_df['id'].isin(top_movie_user)]
for row in movie_df_rows.itertuples():
    print(row.title, ':', row.genre)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = movie_df[movie_df['id'].isin(recommended_movie_ids)]
for row in recommended_movie.itertuples():
    print(row.title, ':', row.genre)