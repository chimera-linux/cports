pkgname = "zimg"
pkgver = "3.0.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Image processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "WTFPL"
url = "https://github.com/sekrit-twc/zimg"
source = f"{url}/archive/release-{pkgver}.tar.gz"
sha256 = "5e002992bfe8b9d2867fdc9266dc84faca46f0bfd931acc2ae0124972b6170a7"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    self.install_license("COPYING")

@subpackage("zimg-devel")
def _devel(self):
    return self.default_devel()
