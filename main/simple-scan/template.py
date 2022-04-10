pkgname = "simple-scan"
pkgver = "42.0"
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
sha256 = "ac1f857afd0bc8897dd2045023ad7c5713e5ceefca56b0b3cc5e9a4795329586"
