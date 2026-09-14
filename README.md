# Personal portfolio website for Jordan Manaksak Hutahaean

## Description

**NAMA : JORDAN MANAKSAK HUTAHAEAN**  
**NPM : 2506532580**  
**KELAS : PBP E**  
**JURUSAN : ILMU KOMPUTER**  
**UNIVERSITAS : UNIVERSITAS INDONESIA**

---

## Pertanyaan Reflektif Tugas 1

### 1.

Ya, saya menggunakan beberapa elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<ul>`, `<li>`, dan `<time>`.

- `<header>` digunakan untuk menampung identitas dan navigasi sehingga bagian ini dapat dipisahkan dengan jelas dari konten utama.
- `<main>` digunakan sebagai penampung untuk konten utama seperti konten Profile, Education, dan Experience sehingga konten utama terpisah dengan bagian lain seperti `<header>` dan `<footer>`.
- `<section>` berfungsi untuk membagi konten utama secara spesifik menjadi 3 bagian yaitu Profile, Education, dan Experience melalui pengaplikasian class sehingga akan mudah jika ingin dilakukan perkembangan atau perubahan kedepannya.
- `<ul>` dan `<li>` berfungsi untuk membuat daftar/list education yg pernah dijalani dan experience yang sudah dilakukan.
- `<time>` berfungsi untuk menandai durasi waktu per bagian spesifik di daftar education dan experience.
- `<footer>` digunakan untuk menampung informasi tambahan berupa penutup seperti copyright dan informasi tambahan agar tidak bercampur dengan konten utama.

Penggunaan elemen-elemen semantik ini telah membantu saya dalam membuat static web yg rapi dan mudah dipelihara. Selain itu, struktur kode HTML menjadi lebih readable dan terogranisir.

### 2.

Tantangan utama yang ditemukan adalah menyesuaikan layout hero section ketika ditampilkan ke dalam 2 mode berbeda yaitu desktop dan mobile. Ketika mode desktop, deskripsi profil dan foto terletak berdampingan sedangkan ketika mode mobile, informasi profil dan foto terletak atas dan bawah. Disinilah digunakan sintaks css yaitu `@media (max-width: 600px)` yang berfungsi untuk menyelesaikan tantangan utama ini dengan mengubah atau menyesuaikan layout ketika suatu kondisi terpenuhi(dalam konteks ini ketika lebar layer sudah menyentuh 600px).

### 3.

Karena website yang dibuat masih berbentuk static web, semua perubahan informasi yang dilakukan di education, experience, atau project harus dilakukan langsung pada HTML. Pada kesempatan selanjutnya, saya ingin menggunakan database dan backend agar data dapat diperbarui secara dinamis tanpa mengubah HTML secara manual. Selain itu, saya juga ingin memberikan penekanan interaktif tetapi tetap minimalis dan clean, seperti animasi sederhana saat pengguna melakukan hover, transisi antar elemen, dan interaksi pada bagian project atau experience. Dengan begitu, website tidak hanya informatif, tetapi juga memberikan kesan yang lebih menarik, clean, dan profesional.

---

## Progress Tugas 1

### 31 Agustus

- Menambah kolom README.

### 1 September

- Membuat struktur awal proyek Django.
- Memperbarui kolom README.

### 2 September

- Mengatur ALLOWED_HOSTS untuk deployment.
- Mengatur WhiteNoise untuk static files pada production.
- Menambahkan requirements.txt.
- Merapikan .gitignore, .env, dan .env.prod.
- Mengatur SQLite untuk kebutuhan deployment.

### 5 September

- Mengubah warna background dan font website.
- Menambahkan section Education.
- Menambahkan section Experience.
- Memperbaiki tampilan dan styling Education dan Experience.
- Menambahkan navigasi untuk Education dan Experience.
- Menambahkan informasi sekolah pada Education.

### 6 September

- Memperbaiki spacing dan styling pada Education dan Experience.
- Menambahkan informasi pendidikan dan pengalaman tambahan.

### 7 September

- Penyempurnaan akhir
- Update terakhir README

---

## AI Disclosure Tugas 1

### Saya menggunakan ChatGPT untuk cek kesalahan sintaks atau penulisan kode yang saya tulis dan pelajari secara manual melalui YouTube, merapikan struktur kode shingga readable dan rapi, dan menambah beberapa additional improvement di kode.

---

## Pertanyaan Reflektif Tugas 2

### 1.

- Ketika User membuka dan mengakses halaman portofolio baru melalui pengetikan URLl atau alamat spesifik di tab browser, maka browser akan mengirimkan HTTP Request ke Server Django
- Kemudian Server Django akan menerima request tersebut dan mencocokkan URL-nya. Di urls.py proyek, fungsi include() akan meneruskan dan mengarahkan rute request ke urls.py aplikasi
- Selanjutnya di urls.py aplikasi, request akan dipetakan rute spesifiknya dan diarahkan ke fungsi views.py aplikasi
- Fungsi views.py aplikasi adalah untuk mengambil data-data portofolio melalui pemanggilan model
- Model pun menganbil data dari database SQLite(db.sqlite3) dan mengembalikannya ke views.py aplikasi dalam bentuk objek Python/ QuerySet
- Selanjutnya views.py aplikasi akan memasukkan data QuerySet kedalam dictionary context, dan melakukan pemanggilan template HTML
- Melalui (contoh: `{% for experience in experience_list %}` & `{{ experience.title }}`) atau yang secara umum disebut Django Template Language akan disisipkan data-data dinamis ke struktur HTML
- Pada akhirnya, fungsi views.py aplikasi (spesifiknya pada return render…) akan mengembalikan hasil render template sebagai HTTP Response ke browser
- Browser pun akan menampilkan halaman portofolio yang utuh kepada User

### 2.

Alasan umumnya adalah karena dengan melakukan penyimpanan data pada Model dan tidak menulis secara langsung pada template, kita telah menerapkan prinsip dasar arsitektur Django yaitu Separation of Concern dimana tanggung jawab antara Model, Template, dan Views dipisahkan.

Untuk alasan-alasan spesifiknya adalah :

- Tanggung jawab tiap komponen akan terlihat jelas ketimbang melakukan hardcode pada template, hal tersebut akan merusak konsep MTV karena mencampur data dengan tampilan
- Aplikasi web juga akan mudah untuk dipelihara dan dikembangkan karena penambahan, penghapusan, atau pengubahan terhadap data portofolio dapat dilakukan secara fleksibel dengan mengakses database atau Django Admin sehingga kita tidak perlu mengotak-atik kode HTML
- Ketika melakukan penyimpanan data pada Model, kita menjadi tidak perlu takut untuk melakukan perubahan karena data nya sudah tersimpan di Model
- Data yang dikelola di Model pun tentunya bersifat reusable karena dapat dipanggil oleh fungsi views.py yg berbeda-beda

### 3.

- **makemigrations** : Membaca perubahan pada file main/models.py dan membuat file draf/skrip migrasi baru di folder main/migrations/. Perintah ini belum mengubah struktur database asli.
- **migrate**: Melakukan eksekusi file skrip migrasi di folder migrations/ untuk memperbarui atau menambah tabel di dalam database (db.sqlite3).
- Contoh : Misalkan pada main, ingin ditambahkan deskripsi (description) pada model Experience di file models.py, maka pertama, jalankan python manage.py makemigrations untuk mendeteksi penambahan field `description` dan mencatatnya ke dalam file migrasi baru. Selanjutnya, jalankan python manage.py migrate agar Django membaca file migrasi tersebut dan langsung membuat kolom `description` baru di tabel database `db.sqlite3`.

---

## Instruksi Setup Mingguan

- Membuat *Branch* Git Baru untuk tugas baru di minggu tertentu agar dokumentasi kode lebih terfokus.
- Mengaktifkan Virtual Environment sebelum menjalankan proyek.
- Menginstal Dependensi / Library Baru (jika ada/ disuruh dalam tutorial atau tugas)
- Menjalankan Migrasi Database agar tabel-tabel di database lokal sudah sesuai dengan struktur model terbaru.
- Menjalankan Server Lokal untuk memastikan aplikasi bisa berjalan tanpa error di server lokal.

---

## Progress Tugas 2

### 9 September

- Menambahkan unit testing untuk proyek Django.
- Mengubah status Experience dari sedang berlangsung menjadi selesai pada bagian Experience.
- Menghapus kode Experience pada file `index.html` untuk menghindari duplikasi.

### 12 September

- Memperbarui versi Django
- Melakukan redeploy untuk menerapkan environment variable baru.
- Memperbaiki database env keys fallback
- Melakukan merge dari branch main ke branch tutorial_2
- Memperbarui file `requirements.txt`.
- Menambahkan model Education beserta skrip migrasi awal.

### 13 September

- Menambahkan fungsi *view* `show_education` beserta konfigurasi rute URL
- Membuat berkas *template* `education.html` dan memperbarui navbar.
- Mengatur dan menyesuaikan tampilan serta desain halaman Education melalui `style.css`.
- Melakukan perbaikan (*refactor*) pada beberapa bagian struktur kode `education.html`

### 14 September

- Menambahkan unit test untuk pengujian halaman Education.
- Melakukan styling pada CSS dan finishing pada kode.

---

## AI Disclosure Tugas 2

### Saya menggunakan ChatGPT untuk memahami bagian-bagian yang dirasa kurang mengerti di petunjuk tutorial dalam pengerjaan tugas 2, melakukan cek kesalahan sintaks atau penulisan kode yang saya tulis, merapikan struktur kode sehingga readable dan rapi, membantu dalam styling sesuai desain yang saya mau, serta terakhir merapikan format penulisan README agar terasa rapi dalam box untuk dibaca
