pkgname = "libconfig"
pkgver = "1.8.1"
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
sha256 = "e95798d2992a66ecd547ce3651d7e10642ff2211427c43a7238186ff4c372627"


@subpackage("libconfig-devel")
def _(self):
    return self.default_devel()
