pkgname = "zita-convolver"
pkgver = "4.0.3"
pkgrel = 0
build_wrksrc = "source"
build_style = "makefile"
make_install_args = ["SUFFIX="]
make_use_env = True
makedepends = ["fftw-devel"]
pkgdesc = "Real-time C++ convolution library"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://kokkinizita.linuxaudio.org/linuxaudio"
source = f"https://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-convolver-{pkgver}.tar.bz2"
sha256 = "9aa11484fb30b4e6ef00c8a3281eebcfad9221e3937b1beb5fe21b748d89325f"
# vis breaks symbols
hardening = []
# no tests
options = ["!check"]


@subpackage("zita-convolver-devel")
def _devel(self):
    return self.default_devel()
