pkgname = "libuv"
pkgver = "1.42.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "371e5419708f6aaeb8656671f89400b92a9bba6443369af1bb70bcd6e4b3c764"
options = ["lto"]

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuv-static")
def _static(self):
    return self.default_static()

@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
