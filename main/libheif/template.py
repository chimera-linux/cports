pkgname = "libheif"
pkgver = "1.12.0"
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
sha256 = "086145b0d990182a033b0011caadb1b642da84f39ab83aa66d005610650b3c65"

if self.profile().arch == "aarch64":
    # fails to resolve some symbols from compiler-rt builtins
    # e.g. __aarch64_ldadd8_acq_rel
    tool_flags = {
        "CFLAGS": ["-mno-outline-atomics"],
        "CXXFLAGS": ["-mno-outline-atomics"]
    }

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
