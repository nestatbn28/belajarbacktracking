from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^Sesi/$',views.list,name='list'),
    url(r'^Sesi/create/$',views.create,name='create'),
    url(r'^Sesi/delete/(?P<delete_id>[0-9])$',views.delete,name='delete'),
    url(r'^Sesi/update/(?P<update_id>[0-9])$',views.update,name='update'),


    url(r'^Pengajar/$',views.listpengajar,name='listpengajar'),
    url(r'^Pengajar/create/$',views.createpengajar,name='createpengajar'),
    url(r'^Pengajar/delete/(?P<delete_id>[0-9])$',views.deletepengajar,name='deletepengajar'),
    url(r'^Pengajar/update/(?P<update_id>[0-9])$',views.updatepengajar,name='updatepengajar'),


    url(r'^Kelas/$',views.listkelas,name='listkelas'),
    url(r'^Kelas/create/$',views.createkelas,name='createkelas'),
    url(r'^Kelas/delete/(?P<delete_id>[0-9])$',views.deletekelas,name='deletekelas'),
    url(r'^Kelas/update/(?P<update_id>[0-9])$',views.updatekelas,name='updatekelas'),


    url(r'^Matkul/$',views.listmatakuliah,name='listmatakuliah'),
    url(r'^Matkul/create/$',views.creatematakuliah,name='creatematakuliah'),
    url(r'^Matkul/delete/(?P<delete_id>[0-9])$',views.deletematakuliah,name="deletematakuliah"),
    url(r'^Matkul/update/(?P<update_id>[0-9])$',views.updatematakuliah,name='updatematakuliah'),


    url(r'^Akun/$',views.listakun,name='listakun'),
    url(r'^Akun/create/$',views.createakun,name='createakun'),
    url(r'^Akun/delete/(?P<delete_id>[0-9])$',views.deleteakun,name='deleteakun'),
    url(r'^Akun/update/(?P<update_id>[0-9])$',views.updateakun,name='updateakun'),

]
