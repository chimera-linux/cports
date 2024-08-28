pkgname = "clinfo"
pkgver = "3.0.23.01.25"
pkgrel = 0
build_style = "makefile"
makedepends = ["ocl-icd-devel"]
pkgdesc = "OpenCL info dumper"
maintainer = "eater <=@eater.me>"
license = "CC0-1.0"
url = "https://github.com/Oblomov/clinfo"
source = f"https://github.com/Oblomov/clinfo/archive/{pkgver}.tar.gz"
sha256 = "6dcdada6c115873db78c7ffc62b9fc1ee7a2d08854a3bccea396df312e7331e3"
# no tests available
options = ["!check"]


def install(self):
    self.install_bin("clinfo")
    self.install_man("man1/clinfo.1")
