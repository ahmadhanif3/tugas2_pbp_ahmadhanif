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