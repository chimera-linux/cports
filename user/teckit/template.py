pkgname = "teckit"
pkgver = "2.5.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-system-zlib"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libexpat-devel", "zlib-ng-compat-devel"]
checkdepends = ["perl"]
pkgdesc = "Text Encoding Conversion toolkit"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://software.sil.org/teckit"
source = f"https://github.com/silnrsi/teckit/releases/download/v{pkgver}/teckit-{pkgver}.tar.gz"
sha256 = "7ef10e5bb79ea6437b7a06b4a92b314d3f142292758288efce50e12a455b6e7f"
tool_flags = {
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": ["-DNDEBUG"],
}


@subpackage("teckit-devel")
def _(self):
    return self.default_devel()


@subpackage("teckit-progs")
def _(self):
    return self.default_progs()
