pkgname = "zimg"
pkgver = "3.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers"]  # hwcap on arm etc.
pkgdesc = "Image processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "WTFPL"
url = "https://github.com/sekrit-twc/zimg"
source = f"{url}/archive/release-{pkgver}.tar.gz"
sha256 = "a9a0226bf85e0d83c41a8ebe4e3e690e1348682f6a2a7838f1b8cbff1b799bcf"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("zimg-devel")
def _devel(self):
    return self.default_devel()
