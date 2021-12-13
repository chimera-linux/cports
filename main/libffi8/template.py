pkgname = "libffi8"
pkgver = "3.4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include", "--disable-multi-os-directory", "--with-pic"
]
hostmakedepends = ["pkgconf"]
# actually only on x86 and arm (tramp.c code) but it does not hurt
makedepends = ["linux-headers"]
pkgdesc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://sourceware.org/libffi"
source = f"https://github.com/libffi/libffi/releases/download/v{pkgver}/libffi-{pkgver}.tar.gz"
sha256 = "540fb721619a6aba3bdeef7d940d8e9e0e6d2c193595bc243241b77ff9e93620"
# early bootstrap loop: elftoolchain -> libarchive -> zstd -> meson ->
# python -> libffi -> dejagnu -> expect -> libtool -> libarchive
options = ["!check"]

# do not pull dejagnu and thus tcl etc. into early stages
if self.stage >= 2:
    checkdepends = ["dejagnu"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libffi-static")
def _static(self):
    return self.default_static()

@subpackage("libffi-devel")
def _devel(self):
    return self.default_devel(man = True, extra = ["usr/share/info"])
