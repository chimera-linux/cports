pkgname = "rubberband"
pkgver = "3.1.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dfft=fftw", "-Dresampler=libsamplerate",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsamplerate-devel", "libsndfile-devel", "fftw-devel",
    "ladspa-sdk", "vamp-plugin-sdk-devel",
]
pkgdesc = "Time-stretching and pitch-shifting audio library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://breakfastquay.com/rubberband"
source = f"https://breakfastquay.com/files/releases/{pkgname}-{pkgver}.tar.bz2"
sha256 = "dda7e257b14c59a1f59c5ccc4d6f19412039f77834275955aa0ff511779b98d2"

@subpackage("rubberband-progs")
def _progs(self):
    return self.default_progs()

@subpackage("rubberband-devel")
def _devel(self):
    return self.default_devel()
