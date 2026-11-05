pkgname = "include-what-you-use"
pkgver = "0.26"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["clang-devel", "llvm-devel"]
checkdepends = ["python"]
pkgdesc = "Analyze #includes in C and C++ source files"
license = "NCSA"
url = "https://include-what-you-use.org"
source = f"{url}/downloads/include-what-you-use-{pkgver}.src.tar.gz"
sha256 = "5247c0c9a59df9d14e8aa7408ffec4134c6a4aef12f590929111fbfeac930a08"


def post_install(self):
    self.install_license("LICENSE.TXT")
