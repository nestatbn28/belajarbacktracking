from django.contrib import admin

from .models import Matkul
from .models import Kelas
from .models import Sesi
from .models import Akun
from .models import Hari
from .models import Pengajar
from .models import Pengajar_Matkul_Kelas
from .models import Kategori

admin.site.register(Kategori)
admin.site.register(Matkul)
admin.site.register(Kelas)
admin.site.register(Pengajar)
admin.site.register(Sesi)
admin.site.register(Akun)
admin.site.register(Pengajar_Matkul_Kelas)
admin.site.register(Hari)