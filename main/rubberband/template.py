pkgname = "rubberband"
pkgver = "3.0.0"
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
sha256 = "df6530b403c8300a23973df22f36f3c263f010d53792063e411f633cebb9ed85"

@subpackage("rubberband-progs")
def _progs(self):
    return self.default_progs()

@subpackage("rubberband-devel")
def _devel(self):
    return self.default_devel()
