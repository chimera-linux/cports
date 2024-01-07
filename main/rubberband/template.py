pkgname = "rubberband"
pkgver = "3.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dfft=fftw",
    "-Dresampler=libsamplerate",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsamplerate-devel",
    "libsndfile-devel",
    "fftw-devel",
    "ladspa-sdk",
    "vamp-plugin-sdk-devel",
]
pkgdesc = "Time-stretching and pitch-shifting audio library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://breakfastquay.com/rubberband"
source = f"https://breakfastquay.com/files/releases/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d9ef89e2b8ef9f85b13ac3c2faec30e20acf2c9f3a9c8c45ce637f2bc95e576c"


@subpackage("rubberband-progs")
def _progs(self):
    return self.default_progs()


@subpackage("rubberband-devel")
def _devel(self):
    return self.default_devel()
