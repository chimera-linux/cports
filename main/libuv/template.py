pkgname = "libuv"
pkgver = "1.41.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "6cfeb5f4bab271462b4a2cc77d4ecec847fdbdc26b72019c27ae21509e6f94fa"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh", [])

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
