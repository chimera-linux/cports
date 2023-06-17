pkgname = "simple-scan"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-tiny",
    "vala",
    "itstool",
]
makedepends = [
    "gtk+3-devel",
    "glib-devel",
    "libhandy-devel",
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libgusb-devel",
    "colord-devel",
    "libwebp-devel",
    "sane-backends-devel",
    "zlib-devel",
]
depends = ["hicolor-icon-theme", "sane-backends"]
pkgdesc = "GNOME scanning utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/simple-scan"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "39b870fd46f447f747eaecc2df26049ef773185099f0e13c675656264dd98e95"
# FIXME cfi
hardening = ["vis", "!cfi"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
