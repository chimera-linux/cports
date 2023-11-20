pkgname = "apr"
pkgver = "1.7.4"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "libtool", "pkgconf"]
makedepends = ["libexpat-devel", "libuuid-devel", "linux-headers"]
pkgdesc = "Apache Portable Runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://apr.apache.org"
source = f"https://archive.apache.org/dist/apr/apr-{pkgver}.tar.gz"
sha256 = "a4137dd82a185076fa50ba54232d920a17c6469c30b0876569e1c2a05ff311d9"
# not even once
options = ["!cross"]


@subpackage("apr-devel")
def _devel(self):
    self.depends += ["libuuid-devel"]

    return self.default_devel()
