pkgname = "opus"
pkgver = "1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-float-approx"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
pkgdesc = "Totally open, royalty-free, highly versatile audio codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"https://downloads.xiph.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c9b32b4253be5ae63d1ff16eea06b94b5f0f2951b7a02aceef58e3a3ce49c51f"
# FIXME int
hardening = ["vis", "cfi", "!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("opus-devel")
def _devel(self):
    return self.default_devel()
