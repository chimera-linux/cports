pkgname = "simple-scan"
pkgver = "42.1"
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
sha256 = "859bc0611c1769b5bdaba9639deed359f50474c2eecf58bbbfd7ce21911b2226"
