from django import forms

from .models import Kelas
from .models import Sesi
from .models import Matkul
from .models import Pengajar
from .models import Akun


class KelasForm(forms.ModelForm):
    class Meta:
        model=Kelas
        fields = [
            'nama',
            'kapasitas',
        ]
        labels = {
            'nama' : 'Nama Kelas',
            'kapasitas' : 'Jumlah mahasiswa'
        }
        
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan nama kelas.....'
                }
            ),
            'kapasitas' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan jumlah mahasiwa....'
                }
            )
        }

class SesiForm(forms.ModelForm):
    class Meta:
        model=Sesi
        fields = [
            'nama',
        ]
        labels = {
            'nama' : 'Nama Sesi'
        }
        
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan Sesi.....'
                }
            )
        }

class PengajarForm(forms.ModelForm):
    class Meta:
        model=Pengajar
        fields = [
            'nama',
            'kategori'
        ]
        labels = {
            'nama' : 'Nama Dosen',
            'kategori' : 'Kategori'
        }
        
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan nama Dosen.....'
                }
            ),
            'kategori' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan kategori'
                }
            )
        }



class AkunForm(forms.ModelForm):
    class Meta:
        model=Akun
        fields = [
            'nama',
            'kapasitas',
        ]
        labels = {
            'nama' : 'Nama Akun',
            'kapasitas' : 'Jumlah kapasitas Partisipan'
        }
        
        widgets = {
            'nama' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan nama akun.....'
                }
            ),
            'kapasitas' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan kapasitas partisipan akun....'
                }
            )
        }


class MatkulForm(forms.ModelForm):
    class Meta:
        model=Matkul
        fields = [
            'kode',
            'nama',
            'sks',
            'kategori',
        ]
        labels = {
            'kode':'Masukkan Kode Matakuliah',
            'nama' : 'Nama Mata Kuliah',
            'sks' : 'Jumlah SKS',
            'kategori' : 'kategori'
        }
        
        widgets = {
            'kode' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan Kode Mata Kuliah'
                }
            ),
            'nama' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Masukkan nama mata kuliah.....'
                }
            ),
            'sks' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan jumlah sks...'
                }
            ),
            'kategori' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan kategori'
                }
            )
        }