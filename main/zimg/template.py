pkgname = "zimg"
pkgver = "3.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers"] # hwcap on arm etc.
pkgdesc = "Image processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "WTFPL"
url = "https://github.com/sekrit-twc/zimg"
source = f"{url}/archive/release-{pkgver}.tar.gz"
sha256 = "219d1bc6b7fde1355d72c9b406ebd730a4aed9c21da779660f0a4c851243e32f"
# FIXME cfi
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("zimg-devel")
def _devel(self):
    return self.default_devel()
