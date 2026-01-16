pkgname = "hare-gi"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "gobject-introspection-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "hare",
]
depends = ["gobject-introspection"]
pkgdesc = "GObject Introspection code generator for Hare"
license = "MPL-2.0"
url = "https://git.sr.ht/~yerinalexey/hare-gi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "3d70fde77c07be396d5e7cfc1344e72a3fb4b1ce8a58eeb938bd792c6a1a452e"
tools = {"AS": f"{self.profile().triplet}-as"}
# no tests
options = ["!check"]
