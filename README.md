## Personal portfolio website for Jordan Manaksak Hutahaean


## Description
NAMA        : JORDAN MANAKSAK HUTAHAEAN
NPM         : 2506532580
KELAS       : PBP E
JURUSAN     : ILMU KOMPUTER
UNIVERSITAS : UNIVERSITAS INDONESIA


## Pertanyaan Reflektif

### Tugas 1

1. Ya, saya menggunakan beberapa elemen semantik HTML5 seperti <header>, <main>, <section>, <li>, <time>, dan <footer>.
   - <header> di website ini digunakan untuk menampung identitas dan navigasi sehingga bagian ini dapat dipisahkan dengan jelas dari konten utama. 
   - <main> digunakan sebagai penampung untuk konten utama seperti konten Profile, Education, dan Experience sehingga konten utama terpisah dengan bagian lain seperti <header> dan <footer>. 
   - <section> berfungsi untuk membagi konten utama secara spesifik menjadi 3 bagian yaitu Profile, Education, dan Experience melalui pengaplikasian class sehingga akan mudah jika ingin dilakukan perkembangan atau perubahan kedepannya. 
   - <li> berfungsi untuk membuat daftar/list education yg pernah dijalani dan experience yang sudah dilakukan 
   - <time> berfungsi untuk menandai durasi waktu per bagian spesifik di daftar education dan experience
   - <footer> digunakan untuk menampung informasi tambahan berupa penutup seperti copyright dan informasi tambahan agar tidak bercampur dengan konten utama

   Penggunaan elemen-elemen semantik ini telah membantu saya dalam membuat static web yg rapi dan mudah dipelihara. Selain itu, struktur kode HTML menjadi lebih readable dan terogranisir.

2. Tantangan utama yang ditemukan adalah menyesuaikan layout hero section ketika ditampilkan ke dalam 2 mode berbeda yaitu desktop dan mobile. Ketika mode desktop, deskripsi profil dan foto terletak berdampingan sedangkan ketika mode mobile, informasi profil dan foto terletak atas dan bawah. Disinilah digunakan sintaks css yaitu @media (max-width: 600px) yang berfungsi untuk menyelesaikan tantangan utama ini dengan mengubah atau menyesuaikan layout ketika suatu kondisi terpenuhi(dalam konteks ini ketika lebar layer sudah menyentuh 600px).

3. Karena website yang dibuat masih berbentuk static web, semua perubahan informasi yang dilakukan di education, experience, atau project harus dilakukan langsung pada HTML. Pada kesempatan selanjutnya, saya ingin menggunakan database dan backend agar data dapat diperbarui secara dinamis tanpa mengubah HTML secara manual. Selain itu, saya juga ingin memberikan penekanan interaktif tetapi tetap minimalis dan clean, seperti animasi sederhana saat pengguna melakukan hover, transisi antar elemen, dan interaksi pada bagian project atau experience. Dengan begitu, website tidak hanya informatif, tetapi juga memberikan kesan yang lebih menarik, clean, dan profesional.


## Progress

#### 31 Agustus
- Menambah kolom README.

#### 1 September
- Membuat struktur awal proyek Django.
- Memperbarui kolom README.

#### 2 September
- Mengatur ALLOWED_HOSTS untuk deployment.
- Mengatur WhiteNoise untuk static files pada production.
- Menambahkan requirements.txt.
- Merapikan .gitignore, .env, dan .env.prod.
- Mengatur SQLite untuk kebutuhan deployment.

#### 5 September
- Mengubah warna background dan font website.
- Menambahkan section Education.
- Menambahkan section Experience.
- Memperbaiki tampilan dan styling Education dan Experience.
- Menambahkan navigasi untuk Education dan Experience.
- Menambahkan informasi sekolah pada Education.

#### 6 September
- Memperbaiki spacing dan styling pada Education dan Experience.
- Menambahkan informasi pendidikan dan pengalaman tambahan.

### 7 September
- Penyempurnaan akhir 
- Update terakhir README


## AI Disclosure

### Saya menggunakan ChatGPT untuk cek kesalahan sintaks atau penulisan kode yang saya tulis dan pelajari secara manual melalui YouTube, merapikan struktur kode shingga readable dan rapi, dan menambah beberapa additional improvement di kode. 

