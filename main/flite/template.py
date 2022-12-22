pkgname = "flite"
pkgver = "2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-shared", "--with-audio=pulseaudio"]
make_cmd = "gmake"
make_dir = "."
make_check_target = ""
make_check_args = ["-C", "testsuite"]
hostmakedepends = ["gmake"]
makedepends = ["libpulse-devel"]
pkgdesc = "Lightweight speech synthesis engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-4-Clause"
url = "http://www.festvox.org/flite"
source = f"https://github.com/festvox/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "ab1555fe5adc3f99f1d4a1a0eb1596d329fd6d74f1464a0097c81f53c0cf9e5c"
# testsuite needs alsa lib
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("flite-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
