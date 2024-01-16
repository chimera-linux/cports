pkgname = "libcap-ng"
pkgver = "0.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-python3"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Alternate POSIX capabilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://people.redhat.com/sgrubb/libcap-ng"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "68581d3b38e7553cb6f6ddf7813b1fc99e52856f21421f7b477ce5abd2605a8a"


@subpackage("libcap-ng-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libcap-ng-progs")
def _progs(self):
    return self.default_progs(man="178")
