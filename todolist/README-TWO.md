Nama    : Ahmad Hanif Adisetya<br>
NPM     : 2106750603<br>
Kelas   : PBP C<br>
Link    : https://katalog-hanif.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Synchronous (sync) dan asynchronous (async) programming merupakan 2 tipe dari model pemrograman. Perbedaan utama dari dua model tersebut adalah arsitekturnya. Async merupakan non-blocking architecture, sehingga suatu task tidak bergantung pada task lain & dapat berjalan secara bersamaan. Sedangkan sync merupakan blocking architecture, sehingga eksekusi suatu task bergantung pada keselesaian task sebelumnya.<br> 
Terdapat beberapa perbedaan lainnya di antara keduanya. Pertama, async merupakan multi-thread sedangkan sync adalah single-thread. Selain itu async meningkatkan throughput karena operasi bisa berjalan secara paralel, sedangkan sync tidak.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Event-Driven Programming merupakan suatu paradigma pemrograman di mana alur pemrograman ditentukan oleh events seperti keyboard/mouse yang ditekan, output sensor, ataupun message passing. Pada suatu event-driven application, umumnya terdapat main loop yang menunggu panggilan dari event dan akan menjalankan function yang berkoresponden.<br>
Pada tugas pemrograman kali ini, terdapat penerapan event-driven programming. Salah satu contoh event-driven programming adalah saat ``onClick``. Saat user menekan ``onClick``, aplikasi website akan menjalankan fungsi yang koresponden.

## Jelaskan penerapan asynchronous programming pada AJAX
AJAX sendiri merupakan singkatan dari **Asynchronous JavaScript and XML**, maka tentu AJAX async. Penerapan asynchronous pada AJAX ialah browser tidak perlu melakukan reload seluruh halaman jika terjadi sedikit perubahan data pada halaman. AJAX hanya akan mengembalikan informasi yang di-update ke dan dari server.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Pertama kita tambahkan fungsi untuk mengembalikan JSON dan add task di views.py. Lalu lakukan routing terhadap fungsi yang telah dibuat. Setelah itu kita ke HTML.
Pada HTML, buatlah suatu container yang akan menampung cards milik kita. Untuk menampilkan cards, pada script kita harus buat pengambilan task yang memanfaatkan AJAX GET. Lalu untuk penambahan task, kita dapat manfaatkan AJAX POST. Pertama kita buat modal terlebih dahulu, pada kode ini saya menggunakan dialog yang mengimplementasikan modal. Setelah kita buat form pada modal tersebut, kita buat script untuk melakukan POST serta juga menghubungkan dengan fungsi yang telah dibuat pada views.py. Setelah itu, kita tambahkan objek baru tersebut ke database dan jangan lupa untuk mengkosongkan value field pada form. Untuk remove task, pastikan tiap cards memiliki tombol remove task yang pada atribut onclick merujuk pada fungsi deleteDone. Pada deleteDone, kita gunakan method DELETE untuk menghapus serta mengambil objek yang ingin dihilangkan. Baru setelah itu kita lakukan remove terhadap objek tersebut.