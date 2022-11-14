pkgname = "rubberband"
pkgver = "3.1.1"
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
sha256 = "a442551fe7d26fb4a54dd1c34178733dc9c76ac9ce051a02325f5cb35d154381"

@subpackage("rubberband-progs")
def _progs(self):
    return self.default_progs()

@subpackage("rubberband-devel")
def _devel(self):
    return self.default_devel()
