pkgname = "libconfig"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-examples"]
make_dir = "."
hostmakedepends = [
    "automake",
    "byacc",
    "flex",
    "libtool",
    "pkgconf",
    "texinfo",
]
pkgdesc = "Configuration file library"
license = "LGPL-2.1-or-later"
url = "https://hyperrealm.com/libconfig/libconfig.html"
source = f"https://github.com/hyperrealm/libconfig/archive/v{pkgver}.tar.gz"
sha256 = "22e13253e652ec583ba0dd5b474bd9c7bd85dc724f2deb0d76a6299c421358ef"


@subpackage("libconfig-devel")
def _(self):
    return self.default_devel()
