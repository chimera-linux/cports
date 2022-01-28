pkgname = "simple-scan"
pkgver = "40.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool"
]
makedepends = [
    "gtk+3-devel", "libglib-devel", "libhandy-devel", "cairo-devel",
    "gdk-pixbuf-devel", "libgusb-devel", "colord-devel", "libwebp-devel",
    "sane-backends-devel", "zlib-devel",
]
depends = ["hicolor-icon-theme", "sane-backends"]
pkgdesc = "GNOME scanning utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/simple-scan"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "7c551852cb5af7d34aa989f8ad5ede3cbe31828cf8dd5aec2b2b6fdcd1ac3d53"
