pkgname = "xreader"
pkgver = "4.4.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "-Dcomics=true",
    "-Ddjvu=true",
    "-Dmathjax-directory=/usr/share/yelp/mathjax",
    "-Dpixbuf=true",
]
hostmakedepends = ["intltool", "meson", "pkgconf"]
makedepends = [
    "cairo-devel",
    "djvulibre-devel",
    "glib-devel",
    "gtk+3-devel",
    "libarchive-devel",
    "libgxps-devel",
    "libice-devel",
    "libsecret-devel",
    "libsm-devel",
    "libspectre-devel",
    "libtiff-devel",
    "libx11-devel",
    "libxml2-devel",
    "poppler-devel",
    "webkitgtk-devel",
    "xapp-devel",
    "zlib-ng-compat-devel",
]
depends = ["yelp"]
pkgdesc = "Generic document reader"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/xreader/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "5a5e84588f88e96f3419168216d20729251bb75f2ab1cceace54619fc71ae09c"
# Tests require the "dogtail" Python module
options = ["!check"]


@subpackage("xreader-devel")
def _(self):
    return self.default_devel()
