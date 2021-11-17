pkgname = "libffi"
pkgver = "3.4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include", "--disable-multi-os-directory", "--with-pic"
]
hostmakedepends = ["pkgconf"]
checkdepends = ["dejagnu"]
pkgdesc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://sourceware.org/libffi"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "540fb721619a6aba3bdeef7d940d8e9e0e6d2c193595bc243241b77ff9e93620"
# missing checkdepends for now
options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libffi-devel")
def _devel(self):
    return self.default_devel()
