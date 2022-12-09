# Laporan Proyek Machine Learning - Andi Alfian Bahtiar

Ini adalah proyek akhir sistem rekomendasi untuk memenuhi submission dicoding. Proyek ini membangun model berbasis content-based filtering dan
collaborative filtering yang dapat menentukan top-N rekomendasi film bagi pengguna.

## Project Overview

### Latar Belakang

Film sudah menjadi salah satu media hiburan yang populer di kalangan masyarakat. Sejak tahun 1874 sampai 2015, sebanyak 3,361,741 judul film telah dikeluarkan oleh industri perfilman (http://imdb.com). Banyak-nya judul-judul film yang telah beredar membuat masyarakat sulit untuk menemukan film yang mereka inginkan. Data-data rating film yang terdapat dalam suatu website dapat diolah dan dimanfaatkan untuk merekomen-dasikan film kepada user lain. Pertimbangan-nya adalah menemukan film berdasarkan hubungan antara satu film dan film lainnya yang sudah diberi rating oleh user untuk dijadikan rekomendasi kepada user lain. Oleh karena itu, diperlukan suatu sistem yang dapat merekomendasikan film kepada user.

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Film.jpeg)

Sistem rekomendasi adalah suatu mekanisme yang dapat memberikan suatu informasi atau rekomendasi sesuai dengan kesukaan user berdasarkan informasi yang diperoleh dari user (Sarwar dkk, 2001). Oleh karena itu, diperlukan model rekomendasi yang tepat agar rekomendasi yang diberikan oleh sistem sesuai dengan kesukaan user, serta mempermudah user mengambil keputusan dalam menentukan item (film) yang akan dipilih (McGinty dan Smyth, 2006). Salah satu metode rekomendasi yang digunakan dalam sistem rekomendasi adalah Collaborative filltering. Collaborative filltering menghu-bungkan setiap user dengan kesukaan yang sama terhadap suatu item (film) berdasarkan rating yang diberikan user. Untuk meningkatkan keakurasian hubungan antara user dengan kesukaan yang sama terhadap suatu item (film) digunakan algoritma clustering (Gupta, 2009).

Dalam mencapai hal tersebut, maka dilakukan penelitian untuk menentukan top-N rekomendasi film menggunakan model berbasis content-based filtering dan collaborative filtering. Diharapkan model ini mampu merekomendasikan film yang sesuai dengan pengguna. Rekomendasi ini nantinya dijadikan acuan bagi pengguna dalam menonton film.

## Business Understanding

Proyek ini dibangun untuk perusahaan dengan karakteristik bisnis sebagai berikut :

+ Perusahaan pengembang situs atau sistem streaming film online.
+ Perusahaan pengembang situs rekomendasi dan informasi film.

### Problem Statement

1. Dapatkah sistem memberikan rekomendasi tanpa input dari pengguna baru?
2. Berdasarkan film yang baru saja disukai pengguna, bagaimana cara membuat daftar rekomendasi film dengan metode pendekatan content based filtering?
3. Berdasarkan kemiripan pengguna, bagaimana cara membuat daftar rekomendasi film dengan metode pendekatan collaborative filtering?

### Goals

1. Menampilkan daftar top rekomendasi film untuk pengguna baru.
2. Menghasilkan daftar rekomendasi film berdasarkan film yang disukai pengguna dengan metode pendekatan content-based filtering.
3. Menghasilkan daftar rekomendasi film berdasarkan kemiripan pengguna dengan metode pendekatan collaborative filtering.

### Solution Approach

1. Menyiapkan data agar bisa digunakan dalam membangun model.
2. Menganalisis data dengan melakukan univariate analysis dan multivariate analysis. Memahami data juga dapat dilakukan dengan visualisasi. Tahap ini dapat menyelesaikan *goals* nomor 1.
3. Melakukan pengembangan model dengan pendekatan content-based filtering serta melakukan evaluasi. Tahap ini dapat menyelesaikan *goals* nomor 2.
4. Melakukan pengembangan model dengan pendekatan collaborative filtering serta melakukan evaluasi. Tahap ini dapat menyelesaikan *goals* nomor 3.

## Data Understanding

Dataset yang digunakan dalam proyek ini merupakan data film dengan berbagai karakteristik. Dataset ini dapat diunduh di [Kaggle : Movie Recommendation Data](https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data).

Berikut informasi pada dataset :
1. Dataset movie
-- Dataset memiliki format CSV (Comma-Separated Values).
-- Dataset memiliki 9742 sample dengan 3 fitur.
-- Dataset memiliki 1 fitur bertipe int64 dan 2 fitur bertipe object.
-- Tidak ada missing value dalam dataset.
2. Dataset rating
-- Dataset memiliki format CSV (Comma-Separated Values).
-- Dataset memiliki 100836 sample dengan 4 fitur.
-- Dataset memiliki 3 fitur bertipe int64 dan 1 fitur bertipe float32.
-- Tidak ada missing value dalam dataset.

### Variable - variable pada dataset
1. Dataset movie
-- `movieId` : ID dari film.
-- `title` : Judul dari film.
-- `genres` : Genre dari film.
2. Dataset rating
-- `userId` : ID dari pengguna.
-- `movieId` : ID dari film.
-- `rating` : Rating pengguna dari film.
-- `timestamp` : Stempel waktu rating.

### Univariate Analysis

Univariate Analysis adalah menganalisis setiap fitur secara terpisah.

#### Analisis sebaran pada setiap fitur kategorik

Fitur kategorik genres memiliki sebaran sample sebagai berikut.
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Univariate%20Movie%20Variabel.png)

#### Analisis sebaran pada setiap fitur numerik

Fitur numerik rating memiliki sebaran sebagai berikut
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Univariate%20Rating%20Variabel.png)

### Multivariate Analysis

Multivariate Analysis menunjukkan hubungan antara dua atau lebih fitur dalam data.

+ 10 Kontribusi Peringkat Film Teratas
  ![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Multivariate%20Top%2010%20Movie%20Rating%20Contribution.png)
  Film Forrest Gump (1994) menyumbang kontribusi peringkat oleh pengguna terbanyak, diikuti oleh Shawshank Redemption, The (1994) dan Pulp Fiction (1994). Informasi ini dapat digunakan pengembang sistem dalam merekomendasikan film yang populer kepada penggunanya. Hal ini dikarenakan semakin banyakya kontribusi peringkat, semakin banyak pula pengguna yang menonton film tersebut (populer).

## Data Preprocessing

### Content-Based Filtering
+ Menggabungkan Film
  Dataset movie dan rating digabungkan dengan movieId sebagai primary key. Setelah itu di cek kembali data *missing value* dan *null*.

## Data Preparation

### Content-Based Filtering
+ Hapus Duplikasi
  Kita hanya akan menggunakan data unik untuk dimasukkan ke dalam proses pemodelan. Oleh karena itu, kita perlu menghapus data yang duplikat dengan fungsi **drop_duplicates()**. Dalma hal ini, kita membuang data duplikat pada kolom `movieId`.
+ Konversi Data
  Selanjutnya, kita perlu melakukan konversi data series menjadi list. Dalam hal ini, kita menggunakan fungsi [tolist()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html) dari library numpy. Dan mencetak jumlah data dari `movie_id`, `movie_title`, dan `movie_genres`
+ Membuat Dictionary
  Tahap berikutnya, kita akan membuat [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) untuk menentukan pasangan key-value pada data `movie_id`, `movie_title`, dan `movie_genres` yang telah kita siapkan sebelumnya.

### Collaborative Filtering
+ Menyandikan (encode) fitur `userId` dan `movieId` ke dalam indeks integer.
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Encode%20Fitur%20userId%20dan%20movieId.png)
+ Memetakan `userId` dan `movieId` ke dataframe yang berkaitan.
+ Mengecek beberapa hal dalam data seperti jumlah pengguna, jumlah film, kemudian mengubah nilai rating menjadi float.
+ Membagi Data untuk Training dan Validasi dengan komposisi 80:20 dengan menggunakan index slicing.

## Modeling and Result

### Content-Based Filtering
Sistem yang dibangun oleh proyek ini adalah sistem rekomendasi sederhana berdasarkan genre film berbasis content based filtering.

Sistem rekomendasi berbasis konten adalah sistem yang merekomendasikan konten yang mirip dengan konten yang disukai pengguna sebelumnya. Apabila suatu konten memiliki karakteristik yang sama atau hampir sama dengan konten lainnya, maka kedua konten tersebut dapat dikatakan mirip.

Misalkan dalam sistem rekomendasi film, jika pengguna menyukai film Toy Story (1995), sistem dapat merekomendasikan film dengan genre Adventure, Animation, Children, Comedy, dan Fantasy lainnya.
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Content-Based%20Filtering.png)

#### TF-IDF
TF-IDF atau Term Frequency - Inverse Document Frequency, Bahasa adalah ukuran statistik yang menggambarkan pentingnya istilah dalam dokumen dalam kumpulan atau korpus. Metrik ini biasanya digunakan sebagai faktor pembobotan untuk pencarian informasi, penambangan teks, dan pemodelan pengguna. Nilai TF-IDF meningkat secara linier dengan jumlah kemunculan suatu term dan bergantung pada jumlah dokumen dalam korpus yang memuat term tersebut.

TF-IDF digunakan pada sistem rekomendasi film untuk menentukan representasi fitur penting dari setiap genre film. Untuk menjalankan TF-IDF digunakan fungsi [tfidfvectorizer()](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) dari library sklearn.

Setelah itu hasil TF-IDF tadi ditransformasikan ke dalam bentuk matriks dengan fungsi todense().

Dataframe baru dibuat untuk menunjukkan matriks TF-IDF untuk beberapa film dan genre. Semakin tinggi nilai matriks menunjukkan semakin erat hubungan antara film dengan genre tersebut. Misalkan film Bad Boy Bubby (1993) merupakan genre drama terlihat dari nilai matriks 1.0 yang didapat film tersebut pada genre drama.

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/TF-IDF.png)

#### Cosine Similarity
Cosine Similarity mengukur kesamaan antara dua vektor dan menentukan apakah kedua vektor menunjuk ke arah yang sama. Teknik ini bekerja dengan menghitung sudut cosinus antara dua vektor. Semakin kecil sudut cosinus antara dua vektor, semakin besar nilai kemiripan cosinusnya.

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Cosine%20Similarity.jpg)

Cosine similarity digunakan untuk menghitung derajat kesamaan antar film. Untuk menjalankan cosine similarity digunakan fungsi [cosine_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) dari library sklearn.

Tahap ini menghitung cosise similarity pada dataframe tfidf_matrix yang diperoleh dari tahapan TF-IDF sebelumnya.

Dataframe baru dibuat untuk melihat kesamaan antar film (hasil dari cosine similarity). Dataframe ini menunjukkan nilai kesamaan antar film. Semakin tinggi nilai cosline similarity, kedua film akan semakin memiliki kesamaan. Misalnya, Mama Puri!?, Dark Blue, dan Anata dake Konbanwa memiliki kesamaan dengan anime Kisaku Spirit terlihat dari nilai cosine similarity 1.0 antar kedua anime tersebut.

|                                               | We Could Be King (2014) |
|-----------------------------------------------|-------------------------|
| Richie Rich (1994) | 0.0 |
| Heidi (1937) | 0.0 |
| Winged Migration (Peuple migrateur, Le) (2001) | 1.0 |
| Basketball Diaries, The (1995) | 0.0 |
| They (2002) | 0.0 |
| Sweet Bird of Youth (1962) | 0.0 |
| One Fine Day (1996) | 0.0 |
| Kill Command (2016) | 0.0 |
| Moulin Rouge (2001) | 0.0 |
| Eight Crazy Nights (Adam Sandler's Eight Crazy Nights) (2002) | 0.0 |

#### Result
Fungsi `movie_recommendations` dibuat untuk menemukan rekomendasi film menggunakan similarity yang telah didefinisikan sebelumnya. Fungsi ini bekerja dengan cara mengambil film dengan similarity terbesar dari index yang ada.

Selanjutnya adalah menemukan rekomendasi yang mirip dengan anime Toy Story :

| id | title | genre |
|----|-------|-------|
| 1  | Toy Story (1995) | Adventure\|Animation\|Children\|Comedy\|Fantasy |

Berikut top 5 rekomendasi :

| title | genre |
|-------|-------|
| Turbo (2013) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| Toy Story 2 (1999) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| The Good Dinosaur (2015) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| Monsters, Inc. (2001) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| Moana (2016) | Adventure\|Animation\|Children\|Comedy\|Fantasy |

Sistem telah berhasil merekomendasikan top 5 persen film yang mirip dengan Toy Story (1995), yaitu beberapa film dan seri dari Toy Story itu sendiri. Jadi, jika pengguna menyunkai Toy Story, maka sistem dapat merekomendasikan seri atau movie Toy Story lainnya.

### Collaborative Filtering
### RecommenderNet
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/RecommenderNet.png)
Model yang kita gunakan adalah `RecommenderNet` yang terinspirasi dari tutorial dalam situs [Keras](https://keras.io/examples/structured_data/collaborative_filtering_movielens/). Model menghitung skor kecocokan antara pengguna dan film dengan teknik embedding. Pertama kita melakukan proses embedding terhadap **user** dan **movie**. Selanjutnya, lakukan operasi perkalian dot product antara embedding user dan movie. Selain itu, kita juga dapat menambahkan bias untuk setiap user dan movie. Skor kecocokan ditetapkan dalam skala [0, 1] dengan fungsi aktivasi sigmoid.

#### Compile
| Loss | Optimizer | Metrics |
|----|-------|-------|
| Binary Crossentropy  | Adam (Adaptive Moment Estimation) | Root Mean Squared Erorr (RMSE) |

#### Training
| x | y | batch_size | epochs | validation_data |
|----|-------|-------|-------|-------|
| x_train  | y_train | 8 | 100 | (x_val, y_val) |

#### Result
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Result%20Collaborative%20Filtering.png)
Dari hasil di atas film yang bergenre Drama menjadi film yang paling tinggi ratingnya. Kemudian Top 10 Film yang direkomendasikan sistem adalah film dengan genre Drama dan Comedy.
## Evaluation

### Content-Based Filtering
Evaluasi hasil sistem dengan recommender system precision dalam menemukan rekomendasi dari film Toy Story (1995) adalah sebesar 5/5 atau 100% karena Toy Story (1995) termasuk ke dalam genre Adventure|Animation|Children|Comedy|Fantasy. Dari 5 item yang direkomendasikan, 5 item yang memiliki Adventure|Animation|Children|Comedy|Fantasy (similar).
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Evaluasi%20Content-Based%20Filtering.png)
### Collaborative Filtering
RMSE adalah metode pengukuran dengan mengukur perbedaan nilai dari prediksi sebuah model sebagai estimasi atas nilai yang diobservasi. Root Mean Square Error adalah hasil dari akar kuadrat Mean Square Error. Keakuratan metode estimasi kesalahan pengukuran ditandai dengan adanya nilai RMSE yang kecil. Metode estimasi yang mempunyai Root Mean Square Error (RMSE) lebih kecil dikatakan lebih akurat daripada metode estimasi yang mempunyai Root Mean Square Error (RMSE) lebih besar.
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/RMSE.png)

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%202/Evaluasi%20Collaborative%20Filtering.png)
Proses training model cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, kita memperoleh nilai error akhir sebesar sekitar 0.17 dan error pada data validasi sekitar 0.20. Nilai tersebut cukup bagus untuk sistem rekomendasi.

# Referensi
[Sistem Rekomendasi Film menggunakan Bisecting K-Means dan Collaborative Filtering](https://citisee.amikompurwokerto.ac.id/assets/proceedings/2017/TI08.pdf)

[Referensi gambar latar belakang](https://www.detik.com/jabar/bisnis/d-6382368/8-film-terbaru-yang-tayang-di-bulan-november-2022)

[Toggle the table of contents tf-idf](https://id.wikipedia.org/wiki/Tf%E2%80%93idf)

[Referensi gambar cosine similarity](https://www.engati.com/glossary/cosine-similarity)


