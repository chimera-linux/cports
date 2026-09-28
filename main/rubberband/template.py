pkgname = "rubberband"
pkgver = "4.0.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dfft=fftw",
    "-Dresampler=libsamplerate",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "fftw-devel",
    "ladspa-sdk",
    "libsamplerate-devel",
    "libsndfile-devel",
    "lv2",
    "vamp-plugin-sdk-devel",
]
pkgdesc = "Time-stretching and pitch-shifting audio library"
license = "GPL-2.0-or-later"
url = "https://breakfastquay.com/rubberband"
source = f"https://breakfastquay.com/files/releases/rubberband-{pkgver}.tar.bz2"
sha256 = "af050313ee63bc18b35b2e064e5dce05b276aaf6d1aa2b8a82ced1fe2f8028e9"


@subpackage("rubberband-progs")
def _(self):
    return self.default_progs()


@subpackage("rubberband-devel")
def _(self):
    return self.default_devel()
