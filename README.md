
# Pre-eclampsia Risk Classification Web Application

## English Version (Scroll down to read in Bahasa Indonesia)

This is a web application to classify the risk of pre-eclampsia based on user inputs. It uses a machine learning model, Flask as the backend server, and a simple HTML form for user interaction.

### Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.6+** - The application is written in Python and requires Python 3.6 or higher.
2. **Flask** - A micro web framework for Python.
3. **Joblib** - To load and save the machine learning model.
4. **Scikit-Learn** - For building and running the machine learning model.
5. **NumPy** - For handling numerical data.

### Installation

Follow these steps to set up the application:

#### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd preeclampsia-classification
```

#### Step 2: Set up a Virtual Environment (Recommended)

Setting up a virtual environment helps manage dependencies. Run the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

#### Step 3: Install Required Python Packages

Install the necessary packages by running:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, use the following commands instead:

```bash
pip install flask joblib scikit-learn numpy
```

#### Step 4: Prepare the Model

Ensure that the trained machine learning model (`model.pkl`) is placed in the same directory as `app.py`. If you don’t have a model, you will need to train one and save it as `model.pkl` using `joblib`.

### Running the Application

Once everything is set up, you can start the Flask application.

#### Step 1: Run the Flask Server

In your terminal, make sure you’re in the project directory and your virtual environment is activated. Then run:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`. You should see output indicating the server is running.

#### Step 2: Access the Web Application

Open your web browser and navigate to `http://127.0.0.1:5000/`.

#### Step 3: Fill Out the Form

Fill out the fields in the form, including the radio buttons for options like "Tingkat aktivitas" and "Kesibukan pekerjaan". Once filled, click the "Klasifikasi Risiko" button to submit the form.

#### Step 4: View the Result

After submitting, the application will display the predicted risk level on the same page.

## API Testing

You can also test the API endpoint directly using **Postman** or `curl`.

For example, using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/classify -H "Content-Type: application/json" -d "{\"age\": 30, \"gest_age\": 20, \"height\": 160, ...}"
```

## Troubleshooting

- **ModuleNotFoundError**: Ensure all required packages are installed and that you are using the correct virtual environment.
- **Server Not Starting**: Check that Flask is installed and that `app.py` is in the correct directory.
- **Model Loading Error**: Verify that `model.pkl` exists in the directory and is compatible with the code.

---

## Versi Bahasa Indonesia

Aplikasi web ini digunakan untuk mengklasifikasikan risiko pre-eklamsia berdasarkan input pengguna. Aplikasi ini menggunakan model machine learning, Flask sebagai server backend, dan formulir HTML sederhana untuk interaksi pengguna.

### Prasyarat

Sebelum memulai, pastikan Anda sudah menginstal:

1. **Python 3.6+** - Aplikasi ini ditulis dalam Python dan memerlukan Python versi 3.6 atau lebih tinggi.
2. **Flask** - Framework web micro untuk Python.
3. **Joblib** - Untuk memuat dan menyimpan model machine learning.
4. **Scikit-Learn** - Untuk membuat dan menjalankan model machine learning.
5. **NumPy** - Untuk mengelola data numerik.

### Instalasi

Ikuti langkah-langkah berikut untuk menyiapkan aplikasi:

#### Langkah 1: Clone Repository

Clone repository ke komputer lokal Anda:

```bash
git clone <repository-url>
cd preeclampsia-classification
```

#### Langkah 2: Buat Virtual Environment (Direkomendasikan)

Membuat virtual environment membantu dalam mengelola dependensi. Jalankan perintah berikut:

```bash
python -m venv venv
source venv/bin/activate  # Pada macOS/Linux
# ATAU
venv\Scripts\activate     # Pada Windows
```

#### Langkah 3: Instal Paket Python yang Dibutuhkan

Instal paket yang diperlukan dengan menjalankan:

```bash
pip install -r requirements.txt
```

Jika tidak memiliki `requirements.txt`, gunakan perintah berikut:

```bash
pip install flask joblib scikit-learn numpy
```

#### Langkah 4: Siapkan Model

Pastikan model machine learning yang telah dilatih (`model.pkl`) ditempatkan di direktori yang sama dengan `app.py`. Jika Anda tidak memiliki model, Anda perlu melatih dan menyimpannya sebagai `model.pkl` menggunakan `joblib`.

### Menjalankan Aplikasi

Setelah semuanya siap, Anda bisa memulai aplikasi Flask.

#### Langkah 1: Jalankan Server Flask

Di terminal Anda, pastikan Anda berada di direktori proyek dan virtual environment aktif. Kemudian jalankan:

```bash
python app.py
```

Aplikasi akan dimulai di `http://127.0.0.1:5000/`. Anda akan melihat output yang menunjukkan server sedang berjalan.

#### Langkah 2: Akses Aplikasi Web

Buka web browser dan buka `http://127.0.0.1:5000/`.

#### Langkah 3: Isi Formulir

Isi kolom-kolom dalam formulir, termasuk pilihan radio untuk "Tingkat aktivitas" dan "Kesibukan pekerjaan". Setelah selesai, klik tombol "Klasifikasi Risiko" untuk mengirimkan formulir.

#### Langkah 4: Lihat Hasil

Setelah dikirim, aplikasi akan menampilkan tingkat risiko yang diprediksi di halaman yang sama.

## Pengujian API

Anda juga dapat menguji endpoint API langsung menggunakan **Postman** atau `curl`.

Contohnya, menggunakan `curl`:

```bash
curl -X POST http://127.0.0.1:5000/classify -H "Content-Type: application/json" -d "{\"age\": 30, \"gest_age\": 20, \"height\": 160, ...}"
```

## Pemecahan Masalah

- **ModuleNotFoundError**: Pastikan semua paket yang diperlukan telah terinstal dan Anda menggunakan virtual environment yang benar.
- **Server Tidak Berjalan**: Pastikan Flask telah diinstal dan `app.py` berada di direktori yang benar.
- **Kesalahan Memuat Model**: Verifikasi bahwa `model.pkl` ada di direktori dan kompatibel dengan kode.



## Versi Bahasa Indonesia

Aplikasi web ini digunakan untuk mengklasifikasikan risiko pre-eklamsia berdasarkan input pengguna. Aplikasi ini menggunakan model machine learning, Flask sebagai server backend, dan formulir HTML sederhana untuk interaksi pengguna.

### Prasyarat

Sebelum memulai, pastikan Anda sudah menginstal:

1. **Python 3.6+** - Aplikasi ini ditulis dalam Python dan memerlukan Python versi 3.6 atau lebih tinggi.
2. **Flask** - Framework web micro untuk Python.
3. **Joblib** - Untuk memuat dan menyimpan model machine learning.
4. **Scikit-Learn** - Untuk membuat dan menjalankan model machine learning.
5. **NumPy** - Untuk mengelola data numerik.

### Instalasi

Ikuti langkah-langkah berikut untuk menyiapkan aplikasi:

#### Langkah 1: Clone Repository

Clone repository ke komputer lokal Anda:

```bash
git clone <repository-url>
cd preeclampsia-risk-classification
```

#### Langkah 2: Buat Virtual Environment (Direkomendasikan)

Membuat virtual environment membantu dalam mengelola dependensi. Jalankan perintah berikut:

```bash
python -m venv venv
source venv/bin/activate  # Pada macOS/Linux
# ATAU
venv\Scripts\activate     # Pada Windows
```

#### Langkah 3: Instal Paket Python yang Dibutuhkan

Instal paket yang diperlukan dengan menjalankan:

```bash
pip install -r requirements.txt
```

Jika tidak memiliki `requirements.txt`, gunakan perintah berikut:

```bash
pip install flask joblib scikit-learn numpy
```

#### Langkah 4: Siapkan Model

Pastikan model machine learning yang telah dilatih (`model.pkl`) ditempatkan di direktori yang sama dengan `app.py`. Jika Anda tidak memiliki model, Anda perlu melatih dan menyimpannya sebagai `model.pkl` menggunakan `joblib`.

### Menjalankan Aplikasi

Setelah semuanya siap, Anda bisa memulai aplikasi Flask.

#### Langkah 1: Jalankan Server Flask

Di terminal Anda, pastikan Anda berada di direktori proyek dan virtual environment aktif. Kemudian jalankan:

```bash
python app.py
```

Aplikasi akan dimulai di `http://127.0.0.1:5000/`. Anda akan melihat output yang menunjukkan server sedang berjalan.

#### Langkah 2: Akses Aplikasi Web

Buka web browser dan buka `http://127.0.0.1:5000/`.

#### Langkah 3: Isi Formulir

Isi kolom-kolom dalam formulir, termasuk pilihan radio untuk "Tingkat aktivitas" dan "Kesibukan pekerjaan". Setelah selesai, klik tombol "Klasifikasi Risiko" untuk mengirimkan formulir.

#### Langkah 4: Lihat Hasil

Setelah dikirim, aplikasi akan menampilkan tingkat risiko yang diprediksi di halaman yang sama.

## Pengujian API

Anda juga dapat menguji endpoint API langsung menggunakan **Postman** atau `curl`.

Contohnya, menggunakan `curl`:

```bash
curl -X POST http://127.0.0.1:5000/classify -H "Content-Type: application/json" -d "{\"age\": 30, \"gest_age\": 20, \"height\": 160, ...}"
```

## Pemecahan Masalah

- **ModuleNotFoundError**: Pastikan semua paket yang diperlukan telah terinstal dan Anda menggunakan virtual environment yang benar.
- **Server Tidak Berjalan**: Pastikan Flask telah diinstal dan `app.py` berada di direktori yang benar.
- **Kesalahan Memuat Model**: Verifikasi bahwa `model.pkl` ada di direktori dan kompatibel dengan kode.


