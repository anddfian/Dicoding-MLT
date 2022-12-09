# Laporan Proyek Machine Learning - Andi Alfian Bahtiar

Ini adalah proyek pertama predictive analytics untuk memenuhi submission dicoding. Proyek ini membangun model machine learning yang dapat memprediksi harga rumah di Kota Bandung.

## Domain Proyek

### Latar Belakang

Tempat tinggal seperti rumah adalah kebutuhan primer bagi manusia untuk berlindung dan hidup menetap. Tempat tinggal ini memiliki nilai tergantung dari karakteristik yang dimiliki seperti alamat, kamar, bangunan, lahan, serta fitur lainnya.

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Rumah.jpg)

Harga dari setiap rumah diukur dari nilai yang dimiliki oleh rumah tersebut. Namun, harga ini tidak selalu pasti dan sulit untuk melakukan prediksi akurat secara manual. Faktor ketidakpastian perlu dikurangi oleh makelar properti dengan membangun sistem prediksi yang dapat menentukan berapa harga yang pantas untuk karakteristik rumah tertentu.

Dalam mencapai hal tersebut, maka dilakukan penelitian untuk memprediksi harga rumah menggunakan model machine learning. Diharapkan model ini mampu memprediksi harga yang sesuai dengan harga pasar. Prediksi ini nantinya dijadikan acuan bagi makelar properti dalam menyewa rumah dengan harga yang dapat mendatangkan profit bagi makelar properti.

## Business Understanding

Proyek ini dibangun untuk makelar properti dengan karakteristik bisnis sebagai berikut :

+ Makelar properti memiliki atau membeli rumah kemudian menjual kembali ke konsumen.
+ Makelar properti membuka jasa konsultasi harga rumah ke konsumen.

### Problem Statement

1. Fitur apa yang paling berpengaruh terhadap harga rumah?
2. Bagaimana cara memproses data agar dapat dilatih dengan baik oleh model?
3. Berapa harga rumah di pasaran berdasarkan karakteristik tertentu?

### Goals

1. Mengetahui fitur yang paling berpengaruh pada harga rumah.
2. Melakukan persiapan data untuk dapat dilatih oleh model.
3. Membuat model machine learning yang dapat memprediksi harga rumah seakurat mungkin berdasarkan karakteristik tertentu.

### Solution Statement

1. Menganalisis data dengan melakukan univariate analysis dan multivariate analysis. Memahami data juga dapat dilakukan dengan visualisasi. Memahami data dapat membantu untuk mengetahui kolerasi antar fitur dan mendeteksi outlier.
2. Menyiapkan data agar bisa digunakan dalam membangun model.
3. Melakukan hyperparameter tuning menggunakan grid search dan membangun model regresi yang dapat memprediksi bilangan kontinu. ALgoritma yang dipakai dalam proyek ini adalah K-Nearest Neighbour, Random Forest, dan AdaBoost.

## Data Understanding & Removing Outlier

Dataset yang digunakan dalam proyek ini merupakan data harga rumah dengan berbagai karakteristik di Kota Bandung. Dataset ini dapat diunduh di [Kaggle : Dataset Harga Rumah Bandung](https://www.kaggle.com/datasets/rafliaping/dataset-harga-rumah-bandung).

Berikut informasi pada dataset :

+ Dataset memiliki format XLSX (Microsoft Excel Open XML Spreadsheet).
+ Dataset memiliki 1470 sample dengan 8 fitur.
+ Dataset memiliki 5 fitur bertipe int64 dan 3 fitur bertipe object.
+ Tidak ada missing value dalam dataset.

### Variable - variable pada dataset

+ Unnamed: 0: Index dalam dataset.
+ Judul: Judul penjualan rumah.
+ Alamat: Alamat penjualan rumah.
+ Deskripsi: Deskripsi penjualan rumah.
+ Kamar: Kamar penjualan rumah.
+ Bangunan: Bangunan penjualan rumah.
+ Lahan: Luas lahan penjualan rumah.
+ Harga: Harga penjualan rumah.

Dari ke 8 fitur dapat dilihat bahwa fitur Unnamed: 0, Judul dan Deskripsi tidak mempengaruhi harga rumah sehingga akan dihapus. Hal ini dikarenakan ketiga fitur tersebut tidak diperlukan dalam membangun model prediksi harga.

### Univariate Analysis

Univariate Analysis adalah menganalisis setiap fitur secara terpisah.

#### Analisis jumlah nilai unique pada setiap fitur kategorik

Fitur kategorik Alamat memiliki sebaran sample sebagai berikut.
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Categorical%20Features%20Univariate.png)

#### Analisis sebaran pada setiap fitur numerik

![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Numerical%20Features%20Univariate.png)
Berikut analisis dari grafik di atas :

+ Sebagian besar rumah memiliki 2 sampai 3 kamar.
+ Sebagian besar rumah memiliki bangunan dibawah 100.
+ Sebagian besar rumah memiliki lahan diantara 50-100.
+ Rentang harga cukup tinggi, yaitu dari 6.500000e+07 hingga 5.700000e+10. Namun, rata-rata harga rumah hanya 2.557354e+09.

### Multivariate Analysis

Multivariate Analysis menunjukkan hubungan antara dua atau lebih fitur dalam data.

#### Analisis fitur kategorik

Analisis ini dilakukan untuk melihat kolerasi antara fitur kategorik dengan fitur target (harga).

+ Fitur Alamat
  ![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Categorical%20Features%20Multivariate.png)
  
#### Analisis fitur numerik
  
+ Melihat kolerasi antara semua fitur numerik
  ![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Numerical%20Features%20Multivariate.png)
  Fitur kamar berkorelasi tidak signifikan dengan fitur target (harga). Hal ini mungkin disebabkan oleh kurangnya data dalam penelitian ini. Fitur lahan dan bangunan berkolerasi signifikan dengan fitur target (harga). Hal ini sudah sesuai harapan dari penghapusan outlier yang sudah dilakukan sebelumnya.

+ Correlation matriks fitur numerik
  ![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Correlation%20Matrix.png)
  Fitur kamar, bangunan dan lahan memiliki skor korelasi yang besar dengan fitur target (harga). Artinya, fitur bangunan berkorelasi tinggi dengan keempat fitur tersebut. Sementara itu, fitur kamar memiliki korelasi yang paling rendah (0.6) terhadap fitur target (harga).

## Data preparation

+ One Hot Encoding

  One hot encoding adalah teknik mengubah data kategorik menjadi data numerik dimana setiap kategori menjadi kolom baru dengan nilai 0 atau 1. Fitur yang akan diubah menjadi numerik pada proyek ini adalah Alamat.
  
+ Train Test Split

  Train test split aja proses membagi data menjadi data latih dan data uji. Data latih akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji performa model. Pada proyek ini dataset sebesar 1264 dibagi menjadi 1200 untuk data latih dan 64 untuk data uji.
  
+ Normalization

  Algoritma machine learning akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data seragam yang memiliki skala relatif sama. Salah satu teknik normalisasi yang digunakan pada proyek ini adalah Standarisasi dengan sklearn.preprocessing.StandardScaler.

## Modeling

+ Algoritma
  Penelitian ini melakukan pemodelan dengan 3 algoritma, yaitu K-Nearest Neighbour, Random Forest, dan
  + K-Nearest Neighbour
    K-Nearest Neighbour bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Proyek ini menggunakan [sklearn.neighbors.KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_neighbors` = Jumlah k tetangga tedekat. Dengan nilai 15

  + Random Forest
    Algoritma random forest adalah teknik dalam machine learning dengan metode ensemble. Teknik ini beroperasi dengan membangun banyak decision tree pada waktu pelatihan. Proyek ini menggunakan [sklearn.ensemble.RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_estimators` = Jumlah maksimum estimator di mana boosting dihentikan. Dengan nilai 50.
    + `max_depth` = Kedalaman maksimum setiap tree. Dengan nilai 32.
    + `random_state` = Mengontrol seed acak yang diberikan pada setiap base_estimator pada setiap iterasi boosting. Dengan nilai 33.

  + Adaboost
    AdaBoost juga disebut Adaptive Boosting adalah teknik dalam machine learning dengan metode ensemble.  Algoritma yang paling umum digunakan dengan AdaBoost adalah pohon keputusan (decision trees) satu tingkat yang berarti memiliki pohon Keputusan dengan hanya 1 split. Pohon-pohon ini juga disebut Decision Stumps. Algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi dengan cara menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) secara berurutan sehingga membentuk suatu model yang kuat (strong ensemble learner). Proyek ini menggunakan [sklearn.ensemble.AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_estimators` = Jumlah maksimum estimator di mana boosting dihentikan. Dengan nilai 25.
    + `learning_rate` = Learning rate memperkuat kontribusi setiap regressor. Dengan nilai 0.1.
    + `random_state` = Mengontrol seed acak yang diberikan pada setiap base_estimator pada setiap iterasi boosting. Dengan nilai 55.

+ Hyperparameter Tuning (Grid Search)
  Hyperparameter tuning adalah cara untuk mendapatkan parameter terbaik dari algoritma dalam membangun model. Salah satu teknik dalam hyperparameter tuning yang digunakan dalam proyek ini adalah grid search. Berikut adalah hasil dari Grid Search pada proyek ini :
  | model    | best_params                                                     |
  |----------|-----------------------------------------------------------------|
  | knn      | {'n_neighbors': 15}                                             |
  | random_forest | {'max_depth': 32, 'n_estimators': 50, 'random_state': 33}  |
  | boosting | {'learning_rate': 0.1, 'n_estimators': 25, 'random_stste': 55}  |

## Evaluation

Metrik evaluasi yang digunakan pada proyek ini adalah akurasi dan mean squared error (MSE). Akurasi menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test). Mean squared error (MSE) mengukur error dalam model statistik dengan cara menghitung rata-rata error dari kuadrat hasil aktual dikurang hasil prediksi. Berikut formulan MSE :
![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/Rumus%20MSE.png)

Berikut hasil evaluasi pada proyek ini :

+ Akurasi
  | model    | accuracy |
  |----------|----------|
  | knn      | 0.680707 |
  | rf       | 0.683812 |
  | boosting | 0.69424  |

+ Mean Squared Error (MSE)
  ![](https://raw.githubusercontent.com/anddfian/Dicoding-MLT/main/Submission%201/MSE.png)

Dari hasil evaluasi dapat dilihat bahwa model dengan algoritma Boosting memiliki akurasi lebih tinggi dan tingkat error lebih kecil dibandingkan algoritma lainnya dalam proyek ini.

# Referensi
[Prediksi Harga Rumah Menggunakan General Regression Neural Network](https://ejournal.bsi.ac.id/ejurnal/index.php/ji/article/download/9036/pdf)
[Referensi gambar](https://blog.tribunjualbeli.com/43051/kini-cari-rumah-idaman-makin-mudah-lewat-online-cek-kisaran-harganya-di-wilayah-bandung)

