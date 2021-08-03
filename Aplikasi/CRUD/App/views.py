from django.shortcuts import render,redirect

from .models import Kelas, Pengajar
from .forms import KelasForm

from .models import Sesi
from .forms import SesiForm

from .models import Pengajar
from .forms import PengajarForm


from .models import Matkul
from .forms import MatkulForm

from .models import Akun
from .forms import AkunForm

def list(request):
    semua_sesi= Sesi.objects.all()

    context={
        'page_title':'List Seluruh Sesi',
        'semua_sesi':semua_sesi,
    }

    return render(request,'sesi/list.html',context)

def delete(request,delete_id):
    Sesi.objects.filter(id=delete_id).delete()
    return redirect('App:list')

def update(request,update_id):
    sesi_update=Sesi.objects.get(id=update_id)
    
    data={
        'nama':sesi_update.nama,
    }

    sesi_form=SesiForm(request.POST or None,initial=data,instance=sesi_update)

    if request.method=='POST':
        if sesi_form.is_valid:
            sesi_form.save()
        return redirect('App:list')
    
    context= {
        "page_title":"Update Sesi",
        "sesi_form":sesi_form,
    }
    return render(request,'sesi/create.html',context)

def create(request):
    sesi_form= SesiForm(request.POST or None)

    if request.method=='POST':
        if sesi_form.is_valid:
            sesi_form.save()
        return redirect('App:list')
    
    context= {
        "page_title":"Tambah Sesi",
        "sesi_form":sesi_form,
    }
    return render(request,'sesi/create.html',context)






def listpengajar(request):
    semua_pengajar= Pengajar.objects.all()

    context={
        'page_title':'List Seluruh Pengajaran',
        'semua_pengajar':semua_pengajar,
    }

    return render(request,'pengajar/list.html',context)

def deletepengajar(request,delete_id):
    Pengajar.objects.filter(id=delete_id).delete()
    return redirect('App:listpengajar')

def updatepengajar(request,update_id):
    pengajar_update=Pengajar.objects.get(id=update_id)
    
    data={
        'nama':pengajar_update.nama,
        'kategori':pengajar_update.kategori
    }

    pengajar_form=PengajarForm(request.POST or None,initial=data,instance=pengajar_update)

    if request.method=='POST':
        if pengajar_form.is_valid:
            pengajar_form.save()
        return redirect('App:listpengajar')
    
    context= {
        "page_title":"Update Pengajar",
        "pengajar_form":pengajar_form,
    }
    return render(request,'pengajar/create.html',context)

def createpengajar(request):
    pengajar_form= PengajarForm(request.POST or None)

    if request.method=='POST':
        if pengajar_form.is_valid:
            pengajar_form.save()
        return redirect('App:listpengajar')
    
    context= {
        "page_title":"Tambah Pengajar",
        "pengajar_form":pengajar_form,
    }
    return render(request,'pengajar/create.html',context)








def listkelas(request):
    semua_kelas= Kelas.objects.all()

    context={
        'page_title':'List Seluruh Kelas',
        'semua_kelas':semua_kelas,
    }
    return render(request,'kelas/list.html',context)

def deletekelas(request,delete_id):
    Kelas.objects.filter(id=delete_id).delete()
    return redirect('App:listkelas')

def updatekelas(request,update_id):
    kelas_update=Kelas.objects.get(id=update_id)
    
    data={
        'nama':kelas_update.nama,
        'kapasitas':kelas_update.kapasitas,
    }

    kelas_form=KelasForm(request.POST or None,initial=data,instance=kelas_update)

    if request.method=='POST':
        if kelas_form.is_valid:
            kelas_form.save()
        return redirect('App:listkelas')
    
    context= {
        "page_title":"Update Kelas",
        "kelas_form":kelas_form,
    }
    return render(request,'kelas/create.html',context)

def createkelas(request):
    kelas_form= KelasForm(request.POST or None)

    if request.method=='POST':
        if kelas_form.is_valid:
            kelas_form.save()
        return redirect('App:listkelas')
    
    context= {
        "page_title":"Tambah Kelas",
        "kelas_form":kelas_form,
    }
    return render(request,'kelas/create.html',context)







def listmatakuliah(request):
    semua_matakuliah= Matkul.objects.all()

    context={
        'page_title':'List Seluruh Mata Kuliah',
        'semua_matkul':semua_matakuliah,
    }

    return render(request,'matakuliah/list.html',context)

def deletematakuliah(request,delete_id):
    Matkul.objects.filter(id=delete_id).delete()
    return redirect('App:listmatakuliah')

def updatematakuliah(request,update_id):
    matakuliah_update=Matkul.objects.get(id=update_id)
    
    data={
        'nama':matakuliah_update.nama,
        'sks':matakuliah_update.sks,
        'kategori':matakuliah_update.kategori,
    }

    matakuliah_form=MatkulForm(request.POST or None,initial=data,instance=matakuliah_update)

    if request.method=='POST':
        if matakuliah_form.is_valid:
            matakuliah_form.save()
        return redirect('App:listmatakuliah')
    
    context= {
        "page_title":"Update Mata Kuliah",
        "matakuliah_form":matakuliah_form,
    }
    return render(request,'matakuliah/create.html',context)

def creatematakuliah(request):
    matakuliah_form= MatkulForm(request.POST or None)

    if request.method=='POST':
        if matakuliah_form.is_valid:
            matakuliah_form.save()
        return redirect('App:listmatakuliah')
    
    context= {
        "page_title":"Tambah Mata Kuliah",
        "matakuliah_form":matakuliah_form,
    }
    return render(request,'matakuliah/create.html',context)








def listakun(request):
    semua_akun= Akun.objects.all()

    context={
        'page_title':'List Seluruh Akun',
        'semua_akun':semua_akun,
    }

    return render(request,'akun/list.html',context)

def deleteakun(request,delete_id):
    Akun.objects.filter(id=delete_id).delete()
    return redirect('App:listakun')

def updateakun(request,update_id):
    akun_update=Akun.objects.get(id=update_id)
    
    data={
        'nama':akun_update.nama,
        'jumlah':akun_update.jumlah,
    }

    akun_form=AkunForm(request.POST or None,initial=data,instance=akun_update)

    if request.method=='POST':
        if akun_form.is_valid:
            akun_form.save()
        return redirect('App:listakun')
    
    context= {
        "page_title":"Update Akun",
        "akun_form":akun_form,
    }
    return render(request,'akun/create.html',context)

def createakun(request):
    akun_form= AkunForm(request.POST or None)

    if request.method=='POST':
        if akun_form.is_valid:
            akun_form.save()
        return redirect('App:listakun')
    
    context= {
        "page_title":"Tambah Akun",
        "akun_form":akun_form,
    }
    return render(request,'akun/create.html',context)
