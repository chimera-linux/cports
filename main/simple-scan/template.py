pkgname = "simple-scan"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "cairo-devel",
    "colord-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgusb-devel",
    "libwebp-devel",
    "sane-backends-devel",
    "zlib-ng-compat-devel",
]
depends = ["sane-backends"]
pkgdesc = "GNOME scanning utility"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/simple-scan"
# tarball is missing on GNOME_SITE
# source = f"$(GNOME_SITE)/simple-scan/{pkgver[:-4]}/simple-scan-{pkgver}.tar.xz"
source = f"https://gitlab.gnome.org/GNOME/simple-scan/-/archive/{pkgver}/simple-scan-{pkgver}.tar.gz"
sha256 = "a27e0412b36fb7c03b810532d220eb7a606898c06131fb1757af4745587abcbb"
hardening = ["vis", "!cfi"]
