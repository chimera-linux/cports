pkgname = "libcap-ng"
pkgver = "0.8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-python", "--without-python3"]
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Alternate POSIX capabilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://people.redhat.com/sgrubb/libcap-ng"
source = f"http://people.redhat.com/sgrubb/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bed6f6848e22bb2f83b5f764b2aef0ed393054e803a8e3a8711cb2a39e6b492d"

@subpackage("libcap-ng-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()

@subpackage("libcap-ng-progs")
def _progs(self):
    return self.default_progs(man = "178")

configure_gen = []
