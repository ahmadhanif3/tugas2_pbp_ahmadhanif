Nama    : Ahmad Hanif Adisetya<br>
NPM     : 2106750603<br>
Kelas   : PBP C<br>
Link    : https://katalog-hanif.herokuapp.com/mywatchlist/, https://katalog-hanif.herokuapp.com/mywatchlist/html/, 

### Jelaskan perbedaan antara JSON, XML, dan HTML!
**Pengertian**
- JSON (JavaScript Object Notation) adalah suatu text format untuk menyimpan dan memutarbalikkan data. JSON ditulis dalam notasi object JavaScript dan mudah bagi manusia untuk menulis dan membacanya. JSON dibangun dengan dasar 2 struktur, yaitu suatu koleksi dari pasangan name/value serta suatu ordered list dari values. JSON sendiri memiliki ekstensi file yaitu ".json". 
- XML (eXtensible Markup Language) adalah suatu markup language yang dirancang untuk menyimpan dan melakukan transportasi data. Tujuannya adalah berfokus pada simplisitas, generality, dan kegunaan untuk seluruh internet. XML sendiri memiliki ektensi file yaitu ".xml".
- HTML (HyperText Markup Language) adalah suatu markup language standar yang digunakan untuk di-display pada browser. Guna dari HTML untuk membuat page website. HTML terdiri dari berbagai rangkaian elemen yang menginstruksikan browser bagaimana menunjukkan konten. HTML sendiri memiliki ekstensi file yakni ".html".<br><br> 

**Perbedaan XML & HTML**<br>
XML dan HTML sama-sama merupakan markup language, namun keduanya memiliki perbedaannya masing-masing seperti:
 | XML          | HTML         |
 |--------------|--------------|
 | Digunakkan untuk menyimpan data | Digunakkan untuk menampilkan data |
 | Bersifat dinamis | Bersifat statis |
 | Tidak memperbolehkan adanya error | Memperbolehkan error minim |
 | Case sensitive | Case insensitive |
 | Tags ditentukan user | Sudah ada tags yang ditentukan |
 | Tags diperuntukkan menjelaskan data | Tags diperuntukkan menunjukkan data |<br><br>
 
 **Perbedaan XML & JSON**<br>
 | XML        | JSON       |
 | ---------- | ---------- |
 | Berasal dari SGML | Berdasarkan bahasa JavaScript |
 | Tidak mendukung array | Mendukung array |
 | Ada start dan end tags | Tidak menggunakan end tag |
 | Menggunakan struktur tag untuk merepresentasi data items | Untuk merepresentasi objek |
 | Mendukung namespaces | Tidak mendukung namespaces |
 | Sedikit lebih sulit dibaca | Lebih mudah dibaca |<br><br>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memperlukan data delivery dalam pengimplementasian sebuah platform dikarenakan adanya pertukaran data yang terjadi antara client serta juga server. Dengan adanya data delivery, request yang dikirim oleh client serta web page yang dikirim kembali oleh server dapat terjadi. Format untuk respone-request bisa dalam bentuk JSON, XML, dan umumnya HTML. Mengirim atau menerima dalam format JSON atau XML dapat menggunakan AJAX atau WebSocket. AJAX & WebSocket sendiri diimplementasi oleh jQuery atau Socket.js. Semua hal tersebut dijalankan di atas HTTP/HTTPS.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1)  **Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu.**<br>
Masuk terlebih dahulu ke folder tugas 2, lalu ke command prompt. Nyalakan virtual environment dengan command ```python -m venv env``` lalu dilanjutkan dengan ```env\Scripts\activate.bat``` (untuk Windows). Setelah itu, ketik command ```python manage.py startapp mywatchlist```.
2) **Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist.**<br>
Pergi ke folder project_django dan masuk ke urls.py. pada bagian urlpatterns, tambahkan ```path("mywatchlist/", include("mywatchlist.urls"))``` agar aplikasi mywatchlist dapat diakses. Tak lupa untuk menambahkan mywatchlist pada settings.py bagian INSTALLED_APPS.
3) **Membuat sebuah model MyWatchList yang memiliki atribut.**<br>
Pada folder mywatchlist, buka file models.py dan tambahkan class MyWatchList dengan parameter models.Model. Tambahkan atribut di dalam class MyWatchList. Sesuai petunjuk soal kita perlu menambahkan atribut watched dengan models.CharField() (Untuk menulis "Yes :D" atau "No :("), atribut title dengan models.CharField(), atribut rating dengan models.IntegerField(), atribut release date dengan models.DateField(), dan atribut review dengan model.TextField().
4) **Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas.**<br>
Buat folder fixtures dalam folder mywatchlist. Tambahkan file initial_watchlist_data.json dalam folder tersebut dan tuliskan data sebanyak 10. Tiap data harus mengandung model, pk, serta fields yang berisi atribut models yang telah dibuat pada step sebelumnya. 
5) **Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format.**<br>
Untuk ini buka views.py dan import model MyWatchList dari models.py, serta import HttpRespons & serializers. Buatlah 3 fungsi yakni show_watchlist, show_json, dan show_xml yang mengambil parameter request. Pada ketiga fungsi, set variable ```data = MyWatchList.objects.all()```. Untuk show_watchlist, set variable dictionary bernama context dan masukkan pasangan key:value yakni ```"watchlist":  data, "nama": nama_anda, "npm": npm_anda```. Lalu kembalikan dengan ```return render(request, "mywatchlist.html", context)```. Sedangkan untuk show_json tidak perlu variable context, dapat langsung ```return HttpResponse(serializers.serialize("json", data), content_type="application/json"), content_type="application/xml")```. show_xml mirip dengan show_json, hanya saja pada bagian return kita tulis ```return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")```.
6)  **Membuat routing sehingga data di atas dapat diakses melalui URL.**<br>
Buatlah file path pada folder mywatchlist dan import urls serta fungsi yang telah dibuat pada step sebelumnya. Buat variable app_name dan tambahkan nama aplikasi mywatchlist. Buat suatu list bernama urlpatterns dan tambahkan path yang diinginkan. URL dan apa yang terdapat pada url patterns adalah sebagai berikut:<br>
http://localhost:8000/mywatchlist -> ```path("", show_watchlist, name="show_watchlist")```<br>
http://localhost:8000/mywatchlist/html -> ```path("html/", show_watchlist, name="show_watchlist")```<br>
http://localhost:8000/mywatchlist/xml -> ```path("xml/", show_xml, name="show_xml")```<br>
http://localhost:8000/mywatchlist/json -> ```path("json/", show_json, name="show_json")```<br>
7) ***Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.***<br>
Dikarenakan kita membuat aplikasi mywatchlist pada project yang sama dengan tugas 2, kita tidak perlu melakukan deployment lagi (yeyy). Namun kita harus tetap melakukan makemigrations, migrate, dan loaddata. Lalu lakukan git add, commit, dan push pada repository. Setelah itu pergi ke heroku dan buka aplikasi untuk tugas 2. Pada bagian more, pilih run a console lalu ketik bash. Setelah itu akan muncul terminal, yang harus kita lakukan adalah ketik command ```python manage.py loaddata initial_watchlist_data.json```. Setelah selesai, aplikasi dapat diakses melewati link yang ada! (pada awal README.md) 

### Postman
HTML
![](images/postman_mywatchlist_html.png)
JSON
![](images/postman_mywatchlist_json.png)
XML
![](images/postman_mywatchlist_xml.png)