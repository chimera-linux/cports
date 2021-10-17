pkgname = "libcap-ng"
pkgver = "0.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-python", "--without-python3"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Alternate POSIX capabilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://people.redhat.com/sgrubb/libcap-ng"
source = f"http://people.redhat.com/sgrubb/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "52c083b77c2b0d8449dee141f9c3eba76e6d4c5ad44ef05df25891126cb85ae9"

@subpackage("libcap-ng-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("libcap-ng-progs")
def _progs(self):
    return self.default_progs(extra = ["usr/share"])
