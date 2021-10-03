pkgname = "libffi"
pkgver = "3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include", "--disable-multi-os-directory", "--with-pic"
]
checkdepends = ["dejagnu"]
pkgdesc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://sourceware.org/libffi"
sources = [f"ftp://sourceware.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"]
sha256 = ["72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056"]

options = ["bootstrap", "!check", "!lint", "!spdx"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libffi-devel")
def _devel(self):
    self.pkgdesc = pkgdesc + " - development files"
    self.depends = [f"libffi={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share",
    ]
