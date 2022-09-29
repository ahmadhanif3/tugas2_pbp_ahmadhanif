Nama    : Ahmad Hanif Adisetya<br>
NPM     : 2106750603<br>
Kelas   : PBP C<br>
Link    : https://katalog-hanif.herokuapp.com/todolist/,  https://katalog-hanif.herokuapp.com/login/, https://katalog-hanif.herokuapp.com/register/, https://katalog-hanif.herokuapp.com/new-task/, https://katalog-hanif.herokuapp.com/logout/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF Token merupakan sebuah tag dari django yang diimplementasikan untuk menghindari/menjaga/mencegah dari serangan CSRF atau Cross Site Request Forgery. Tujuan dari serangan CSRF sendiri adalah untuk menyebabkan user melakukan aksi yang sebenarnya tidak ingin user lakukan. Dibutuhkan lah CSRF Token untuk memastikan keamanan dari hal tersebut. Kita dapat menggunakan CSRF Token dengan mudah, dengan hanya menyisipkan {% csrf_token %} ke dalam form di file html dapat menjamin sekuritas post request dari user ke server. <br>
Jika kita tidak menggunakan {% csrf_token %}, maka keamanan form dari serangan CSRF tidak terjamin. Sehingga tidak akan diketahui secara pasti apakah request yang diberikan berasal dari user yang terautentikasi atau tidak.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen dari form secara manual. Tentunya kita buat pada file html. Langkah pertama untuk membuat secara manual adalah dengan mempunyai tag ```<form></form>```, tag untuk membuat form. Di dalam tag form, kita bisa gunakan tag ```<table></table>``` juga agar lebih terstruktur tampilannya. Kemudian di dalam cell dari table tersebut, kita dapat gunakan ```<input>``` untuk menjadi field dari form kita. Setelah itu, kita perlu juga ```<input>``` untuk melakukan submit, caranya adalah kita set type dari input tersebut menjadi submit. Contoh membuat form secara manual dapat dilihat pada login.html. Potongan kodenya adalah sebagai berikut:
```
<form method="POST" action="">
    {% csrf_token %}
    <table>
        <tr>
            <td>Username: </td>
            <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
        </tr>
                
        <tr>
            <td>Password: </td>
            <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
        </tr>

        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login"></td>
        </tr>
    </table>
</form>
```

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama user harus sudah mengisi form yang ada sesuai dengan fieldnya (valid), lalu dilakukan juga submit. Dikarenakan method dari form tersebut adalah POST, maka form tersebut akan mengirimkan hasil dari form. Lalu dalam views.py, terdapat fungsi untuk melakukan penyimpanan dari hasil form. Sebagai contoh adalah fungsi dari new_task, fungsi ketika user menambahkan task baru:
```
@login_required(login_url='/todolist/login/')
def new_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = Task(
                user = request.user,
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
            )
            task_data.save()
            return redirect('todolist:show_todolist')

    context = {"form":form}
    return render(request, "new_task.html", context)
```
Dapat kita lihat bahwa kita sudah pastikan bahwa methodnya adalah POST serta form valid. Selanjutnya adalah membuat objek baru dari model kita. Dalam contoh kode di atas adalah pada bagian task_data. Kita membuat objek Task() dengan atribut yang sudah kita peroleh dari form. Setelah itu, kita simpan dengan melakukan task_data.save(). Karena sudah tersimpan, kita dapat menampilkannya ke file html utama kita. Dalam aplikasi ini fungsinya adalah show_todolist dan memanggil Task.objects. Kita dapat memanggil semua objek (.all()), atau filter yang kita inginkan saja (.filter())

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1) **Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.**<br>
Masuk terlebih dahulu ke folder tugas 2, lalu ke command prompt. Nyalakan virtual environment dengan command ```python -m venv env``` lalu dilanjutkan dengan ```env\Scripts\activate.bat``` (untuk Windows). Setelah itu, ketik command ```python manage.py startapp todolist```.
2) **Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.**<br>
Pergi ke folder project_django dan masuk ke urls.py. pada bagian urlpatterns, tambahkan ```path("todolist/", include("todolist.urls"))``` agar aplikasi todolist dapat diakses. Tak lupa untuk menambahkan todolist pada settings.py bagian INSTALLED_APPS.
3) **Membuat sebuah model Task yang memiliki atribut**<br>
Pada folder todolist, buka file models.py dan tambahkan class Task dengan parameter models.Model. Tambahkan atribut di dalam class tersebut. Sesuai petunjuk soal kita perlu menambahkan atribut user dengan ```models.ForeignKey(User, on_delete=models.CASCADE)```, atribut date dengan ```models.DateField(default=datetime.date.today)```, atribut title dengan ```models.CharField(max_length=255)```, description dengan ```models.TextField()```, serta is_finished dengan ```models.BooleanField(default=False)``` (untuk bonus).
4) **Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**<br>
Pertama kita buat fungsi show_todolist terlebih dahulu. Fungsi tersebut untuk tampilan utama dari todolist kita. Kita mengambil object yang sesuai dengan user yang login, lalu return ```return render(request, "todolist.html", context)```
Buatlah fungsi register untuk melakukan pendaftaran user (sign up). Kita memanfaatkan ```UserCreationForm()``` yang sudah disediakan oleh django. Di dalamnya kita cek apakah method merupakan POST, lalu juga apakah form yang diisi valid. Setelah benar, kita simpan isinya dan redirect ke halaman login. Berikut adalah fungsinya:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is successfully made!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Buatlah fungsi login_user untuk masuk/login ke user yang telah dibuat. Kita cek dahulu apakah methodnya POST. Kemudian kita ambil/get isi dari form yang telah dibuat. Terdapat dua yang diambil yaitu username dan password. Selanjutnya kita lakukan autentikasi. Jika user bukan none, kita login dan redirect ke halaman utama todolist. Tidak lupa juga untuk set cookie nya. Jika user none, maka kita kembalikan pesan bahwa username atau password salah. Berikut adalah fungsinya:
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'login.html', context)
```
Buatlah fungsi logout_user untuk keluar/logout dari user yang digunakan. Fungsi ini lebih sederhana dibanding redirect dan login. Kita buat variable response yang isinya HttpResponseRedirect dari login yang telah kita buat. Kita juga hapus cookie, baru setelah itu kita return response kita dan akan kembali ke halaman login. Berikut adalah fungsinya:
```
logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```
5) **Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.**<br>
Buatlah folder templates dan buat file todolist.html. Pertama tambahkan nama dan npm terlebih dahulu, setelah itu kita tampilkan username dengan memanfaatkan ```{{user.get_username}}```. Selanjutnya untuk tombol menambah task, kita bisa gunakan tag button serta a. Berikut adalah potongannya ```<button class="btn"><a href="{% url 'todolist:new_task' %}">New Task</a></button>```. Selanjutnya kita buat tabel dengan memanfaatkan tag table. Di dalam table tersebut, kita bikin table header atau row teratas untuk menyatakan atribut dari models kita (seperti Title, Description, dsb.) dan dibawahnya kita manfaatkan for loop untuk mengiterasi task dari user yang sudah difilter dari fungsi show_todolist. Terdapat date, title, dan description. Lalu untuk bonus terdapat is_finished, tombol untuk mengganti status task, serta tombol untuk menghilangkan/membuang task. Setelah tabel selesai terakhir kita masukkan untuk last login dengan memanfaatkan {{last_login}} serta button untuk logout yang potongan kodenya adalah ```<button><a href="{% url 'todolist:logout' %}">Logout</a></button>```.
6) **Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**<br>
Sebelum membuat halaman, kita buat class TaskForm serta fungsi new_task pada views.py. Kita dapat membuat form dengan memanfaatkan forms.Form dan di dalamnya adalah untuk isi dari form. Terdapat title yang memanfaatkan forms.CharField(label="Title") dan description yang memanfaatkan forms.CharField(label="Description", widget=forms.Textarea()). Lalu untuk fungsi new_task sedikit mirip dengan fungsi yang dibuat pada langkah 4, yaitu sebagai berikut:
```
@login_required(login_url='/todolist/login/')
def new_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = Task(
                user = request.user,
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
            )
            task_data.save()
            return redirect('todolist:show_todolist')

    context = {"form":form}
    return render(request, "new_task.html", context)
```
Setelah kita buat keduanya, kita dapat lanjutkan membangun new_task.html. Dalamnya sedikit mirip dengan register.html, hanya bedanya pada bagian input dengan value yaitu Add Task. Berikut adalah new_task.html:
```
{% extends 'base.html' %}

{% block meta %}
<title>Add New Task</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Add New Task</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Add Task"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
7) **Membuat routing sehingga beberapa fungsi dapat diakses melalui URL**<br>
Buatlah file urls.py pada folder todolist dan import urls serta fungsi yang telah dibuat pada views.py. Buat variable app_name dan tambahkan nama aplikasi todolist. Buat suatu list bernama urlpatterns dan tambahkan path yang diinginkan. URL dan apa yang terdapat pada url patterns adalah sebagai berikut:
 http://localhost:8000/todolist -> ```path("", show_todolist, name="show_todolist")```<br>
 http://localhost:8000/todolist/login -> ```path('login/', login_user, name='login')```<br>
 http://localhost:8000/todolist/register -> ```path('register/', register, name='register')```<br> 
 http://localhost:8000/todolist/new-task -> ```path("new-task/", new_task, name="new_task")```<br>
 http://localhost:8000/todolist/logout -> ```path('logout/', logout_user, name='logout')```
8) **Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**<br>
Dikarenakan kita membuat aplikasi todolist pada project yang sama dengan tugas 2, kita tidak perlu melakukan deployment lagi (yeyy). Namun kita harus tetap melakukan makemigrations dan migrate. Lalu lakukan git add, commit, dan push pada repository. Setelah selesai, aplikasi dapat diakses melewati link yang ada! (pada awal README.md) 
9) **Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**<br>
Berikut adalah 2 akun yang masing-masing memiliki 3 task<br>
```
Username = dumbydummy, Password = thisisatest
Username = dumberdummy, Password = thisisatest
```