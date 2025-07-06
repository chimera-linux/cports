pkgname = "apr"
pkgver = "1.7.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-installbuilddir=/usr/lib/apr/build-1"]
make_check_args = ["-j1"]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
makedepends = ["libexpat-devel", "util-linux-uuid-devel", "linux-headers"]
pkgdesc = "Apache Portable Runtime"
license = "Apache-2.0"
url = "https://apr.apache.org"
source = f"https://archive.apache.org/dist/apr/apr-{pkgver}.tar.gz"
sha256 = "6a10e7f7430510600af25fabf466e1df61aaae910bf1dc5d10c44a4433ccc81d"
# not even once
options = ["!cross"]


@subpackage("apr-devel")
def _(self):
    self.depends += ["util-linux-uuid-devel"]

    return self.default_devel()
