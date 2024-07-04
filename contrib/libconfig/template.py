pkgname = "libconfig"
pkgver = "1.7.3"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://hyperrealm.com/libconfig/libconfig.html"
source = f"https://github.com/hyperrealm/libconfig/archive/v{pkgver}.tar.gz"
sha256 = "68757e37c567fd026330c8a8449aa5f9cac08a642f213f2687186b903bd7e94e"


@subpackage("libconfig-devel")
def _devel(self):
    return self.default_devel()
