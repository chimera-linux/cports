pkgname = "popt"
pkgver = "1.18"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-tiny-devel"]
makedepends = ["gettext-tiny-devel"]
pkgdesc = "Command line option parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://rpm.org"
source = f"http://ftp.rpm.org/popt/releases/popt-1.x/popt-{pkgver}.tar.gz"
sha256 = "5159bc03a20b28ce363aa96765f37df99ea4d8850b1ece17d1e6ad5c24fdc5d1"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    self.install_license("COPYING")

@subpackage("popt-devel")
def _devel(self):
    return self.default_devel()
