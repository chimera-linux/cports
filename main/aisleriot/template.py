pkgname = "aisleriot"
pkgver = "3.22.35"
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
sha256 = "27d35055c710d4dd3de9a7a34bdda8461013478f629ae6b4779328884f74a77c"
# not supported
options = ["!lto"]
