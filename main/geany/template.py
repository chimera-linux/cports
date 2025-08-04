pkgname = "geany"
pkgver = "2.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "gtk+3-devel",
]
checkdepends = ["bash"]
pkgdesc = "Gtk+3 IDE"
license = "GPL-2.0-or-later"
url = "https://geany.org"
source = f"https://github.com/geany/geany/releases/download/{pkgver}/geany-{pkgver[:-2]}.tar.gz"
sha256 = "8da944e82f78f3c4c6e6b054b7c562ab64ea37d4a3e7dc8576bed8a8160d3c2a"


@subpackage("geany-devel")
def _(self):
    return self.default_devel()
