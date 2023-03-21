pkgname = "simple-scan"
pkgver = "42.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool"
]
makedepends = [
    "gtk+3-devel", "glib-devel", "libhandy-devel", "cairo-devel",
    "gdk-pixbuf-devel", "libgusb-devel", "colord-devel", "libwebp-devel",
    "sane-backends-devel", "zlib-devel",
]
depends = ["hicolor-icon-theme", "sane-backends"]
pkgdesc = "GNOME scanning utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/simple-scan"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "05f5dfa4e9e206efa9d404c9861dd7c442091793e734c41719739917250e4050"
# FIXME cfi
hardening = ["vis", "!cfi"]
