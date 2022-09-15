Nama    : Ahmad Hanif Adisetya<br>
NPM     : 2106750603<br>
Kelas   : PBP C<br>
Link    : https://katalog-hanif.herokuapp.com/katalog/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
Link bagan: https://github.com/ahmadhanif3/tugas2_pbp_ahmadhanif/blob/main/bagan.jpg.jpg<br><br>
Client <(<- Web Page)   Melalui Internet    (Request ->)> Server<br>
Di dalam Server {
    Run manage.py -> (views.py <-> (models.py <-> DB)) -> index.html -> Balik dikirim ke client
}<br>
Pertama client akan request kepada server dengan menggunakan url dari web page. Kemudian, manage.py akan dijalankan. Kemudian url.py akan dicek. manage.py akan meng-extract argumen dari request lalu dilanjutkan ke views.py. Setelah itu, views.py dan models.py akan bekerja secara sinkron untuk web page-nya. models.py akan mengambil data dari database, dan views.py akan punya cara atau fungsi untuk menampilkan data tersebut. Setelah itu akan dilanjutkan ke berkas html untuk dibangun web page-nya. Setelah selesai dibangun, web page akan diteruskan ke client atau memberikan respons.  

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Sejatinya kita dapat membangun suatu aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, disarankan untuk menggunakan virtual environment. Alasan pertama adalah tiap project membutuhkan requirements/dependencies yang berbeda. Dengan venv juga berguna untuk mengisolasi requirements/packages/dependencies agar tidak mempengaruhi versi lain

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1) Pembuatan fungsi pada views.py dilakukan agar bisa melakukan pengambilan data dari models.py dan dikembalikan ke katalog.html. Pertama yang dilakukan adalah melakukan import CatalogItem dari catalog.models. Selanjutnya, kita buat fungsi yang menunjukkan data show_catalog() yang akan mengembalikan HttpResponse render(request, "katalog.html", context)<br>
2) Lalu kita buat routing untuk memetakan fungsi yang telah dibuat pada views.py. Di urls.py, kita import show_catalog dari katalog.views. Kemudian kita tambahkan app_name kita, serta urlpatterns yakni path("", show_catalog, name="show_katalog")<br>
3) Selanjutnya kita memetakan data yang didapat ke HTML. Kita gunakan variable yang telah dibuat seperti nama dan npm, serta melakukan for loop untuk menampilkan isi tabel dari katalog yang telah dibuat.<br>
4) Terakhir kita lakukan deployment app yang telah dibuat ke Heroku. Pertama kita buat aplikasi di Heroku. Kemudian di repo github, kita tambahkan pada bagian secrets yakni HEROKU_APP_NAME dan HEROKU_API_KEY. Terakhir pada bagian actions kita lakukan deploy ulang dan rerun all jobs. Setelah selesai, aplikasi yang telah dibuat bisa dibuka!