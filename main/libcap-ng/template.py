pkgname = "libcap-ng"
pkgver = "0.8.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-python3"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Alternate POSIX capabilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://people.redhat.com/sgrubb/libcap-ng"
source = f"{url}/libcap-ng-{pkgver}.tar.gz"
sha256 = "3ba5294d1cbdfa98afaacfbc00b6af9ed2b83e8a21817185dfd844cc8c7ac6ff"


@subpackage("libcap-ng-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libcap-ng-progs")
def _(self):
    return self.default_progs(man="178")
