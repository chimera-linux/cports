pkgname = "aisleriot"
pkgver = "3.22.33"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtheme_kde=false",
]
hostmakedepends = [
    "bash",
    "gettext",
    "guile",
    "itstool",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "guile-devel",
    "libcanberra-devel",
    "librsvg-devel",
]
pkgdesc = "Collection of solitaire and other card games"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/aisleriot"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "9ec344a94207ec4b1c1118acc1cc014ecdc66bf247f643c3e2433303ead20b3e"
# not supported
options = ["!lto"]
