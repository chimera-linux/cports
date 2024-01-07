pkgname = "libsamplerate"
pkgver = "0.1.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libsndfile-devel", "fftw-devel", "linux-headers"]
pkgdesc = "Sample Rate Converter for audio"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.mega-nerd.com/SRC"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0a7eb168e2f21353fb6d84da152e4512126f7dc48ccb0be80578c565413444c1"
tool_flags = {"CFLAGS": ["-fPIC"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("libsamplerate-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
