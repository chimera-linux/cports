pkgname = "aisleriot"
pkgver = "3.22.34"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/aisleriot"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "b56063ea5714d410dc186d945177c99b994fd113b28f66b75dd9d78918584a5a"
# not supported
options = ["!lto"]
