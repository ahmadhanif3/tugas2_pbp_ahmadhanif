Nama    : Ahmad Hanif Adisetya<br>
NPM     : 2106750603<br>
Kelas   : PBP C<br>
Link    : https://katalog-hanif.herokuapp.com/todolist/,  https://katalog-hanif.herokuapp.com/todolist/login/, https://katalog-hanif.herokuapp.com/todolist/register/, https://katalog-hanif.herokuapp.com/todolist/new-task/, https://katalog-hanif.herokuapp.com/todolist/logout/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Fungsionalitasnya mirip, namun terdapat beberapa perbedaan. Inline CSS merupakan CSS yang dituliskan di dalam tag di HTML. Internal CSS merupakan CSS yang dituliskan di dalam file HTML tersebut, namun terdapat di dalam tag ```<style>```. External CSS merupakan CSS yang dituliskan dalam file .css sendiri, baru setelah itu diimport ke dalam file HTML yang koresponden.<br>
- Inline CSS efektif untuk penataan satu tag. Jika kita hanya ingin merubah sedikit dari elemen/tag, inline cocok untuk hal tersebut. Namun, inline CSS kurang cocok untuk merubah semua elemen pada halaman ataupun halaman yang banyak dikarenakan kita harus menambahkan ke satu-persatu halaman tersebut. Selain itu juga akan mempengaruhi ukuran file HTML kita.
- Internal CSS efektif untuk penataaan satu halaman. Dikarenakan terdapat pada 1 file HTML itu, yang akan berubah hanya halaman tersebut. Sehingga jika hanya 1 halaman yang ingin diubah masih tidak apa-apa, namun jika banyak halaman yang diubah akan menjadi kurang efektif karena harus menambahkannya satu persatu ke tiap halaman. Selain itu juga akan mempengaruhi ukuran file HTML.
- External CSS efektif jika kita ingin menata website yang memiliki banyak halaman. Dikarenakan dengan hanya satu file .css, kita dapat merubah seluruh tampilan halaman dengan sekaligus. Keuntungan lain adalah file HTML menjadi lebih rapih. Namun, halaman dapat tidak ter-render dengan baik sampai external CSS termuat. Selain itu, merujuk ke banyak file .css bisa meningkatkan download time dari site.

## Jelaskan tag HTML5 yang kamu ketahui.
- ```<br>``` merupakan single line break
- ```<hn>``` n yang dimaksud dapat diubah dari 1-6. h sendiri merupakan tag untuk header
- ```<p>``` merupakan tag untuk paragraf
- ```<div>``` merupakan tag division, atau mengelompokkan tag di dalamnya.
- ```<a>``` merupakan tag untuk menambahkan link
- ```<img>``` merupakan tag untuk image atau gambar
- ```<table>``` merupakan tag untuk sesuai dengan namanya, yaitu table

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
CSS selector terdapat 3 yaitu class selector, ID selector, dan elemen selector. <br>
Class selector merujuk kepada tiap elemen yang memiliki class yang sama. Misal terdapat ```class="example"```, maka untuk memodifikasi class tersebut, kita gunakan class selector dengan syntax ```.example```.<br>
ID selector merujuk kepada elemen berdasarkan dari value dari ID. Misal terdapat ```id="toc"```, maka untuk memodifikasi ID tersebut, kita gunakan ID selector dengan syntax ```#toc```.<br>
Elemen selector merujuk kepada elemen dengan tag tersebut saja. Misal kita terdapat ```<h1>```, maka untuk memodifikasi tag tersebut, kita gunakan elemen selector dengan syntax ```h1 { yang ingin kita ubah atributnya }```.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Buka file base.html pada folder templates. Di dalam file tersebut tambahkan potongan kode berikut agar bisa link ke framework bootstrap:
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```
Selanjutnya, masuk ke folder todolist dan ke templates. Di dalamnya terdapat 4 file html yang dapat diubah yaitu:<br>
```todolist.html, login.html, register.html, new_task.html ```<br>
Saya menggunakan Internal CSS sehingga pada masing-masing file html saya menambahkan ```<style>``` di dalamnya. Khusus untuk file ```todolist.html```, kita implementasikan card untuk menampilkan task yang kita miliki. Caranya adalah menggunakan for loop. Kalau dulu kita menggunakan table (td, th, dsb.), sekarang kita hanya tinggal menaruh tiap data di card (card-title, card-body, dsb.). Setelah selesai menerapkan card dan styling, kita buat web menjadi responsive dengan menambahkan tag:<br>
```<meta name="viewport" content="width=device-width, initial-scale=1.0">```