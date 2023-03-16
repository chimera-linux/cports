pkgname = "libheif"
pkgver = "1.15.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "libde265-devel", "x265-devel", "libaom-devel", "dav1d-devel",
    "libjpeg-turbo-devel", "libpng-devel"
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "0333924bf63d2cd09a021d18d02860eb218cf81b8e6f57d490c505207a59285b"
hardening = ["!cfi"] # TODO

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
