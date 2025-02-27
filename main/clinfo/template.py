pkgname = "clinfo"
pkgver = "3.0.25.02.14"
pkgrel = 0
build_style = "makefile"
makedepends = ["ocl-icd-devel"]
pkgdesc = "OpenCL info dumper"
license = "CC0-1.0"
url = "https://github.com/Oblomov/clinfo"
source = f"https://github.com/Oblomov/clinfo/archive/{pkgver}.tar.gz"
sha256 = "48b77dc33315e6f760791a2984f98ea4bff28504ff37d460d8291585f49fcd3a"
# no tests available
options = ["!check"]


def install(self):
    self.install_bin("clinfo")
    self.install_man("man1/clinfo.1")
