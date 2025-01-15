pkgname = "zziplib"
pkgver = "0.13.78"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DZZIPWRAP=OFF", "-DZZIPSDL=OFF", "-DZZIP_TESTCVE=OFF"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "bash", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["zip", "unzip", "python"]
pkgdesc = "Library to read zip files"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.0-or-later"
url = "https://github.com/gdraheim/zziplib"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "feaeee7c34f18aa27bd3da643cc6a47d04d2c41753a59369d09102d79b9b0a31"


@subpackage("zziplib-devel")
def _(self):
    return self.default_devel()


@subpackage("zziplib-progs")
def _(self):
    return self.default_progs()
