pkgname = "apr"
pkgver = "1.7.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-installbuilddir=/usr/lib/apr/build-1"]
make_check_args = ["-j1"]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
makedepends = ["libexpat-devel", "libuuid-devel", "linux-headers"]
pkgdesc = "Apache Portable Runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://apr.apache.org"
source = f"https://archive.apache.org/dist/apr/apr-{pkgver}.tar.gz"
sha256 = "3375fa365d67bcf945e52b52cba07abea57ef530f40b281ffbe977a9251361db"
# not even once
options = ["!cross"]


@subpackage("apr-devel")
def _(self):
    self.depends += ["libuuid-devel"]

    return self.default_devel()
