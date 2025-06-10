pkgname = "simple-scan"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "itstool",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libadwaita-devel",
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libgusb-devel",
    "colord-devel",
    "libwebp-devel",
    "sane-backends-devel",
    "zlib-ng-compat-devel",
]
depends = ["sane-backends"]
pkgdesc = "GNOME scanning utility"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/simple-scan"
# tarball is missing on GNOME_SITE
# source = f"$(GNOME_SITE)/simple-scan/{pkgver[:-2]}/simple-scan-{pkgver}.tar.xz"
source = f"https://gitlab.gnome.org/GNOME/simple-scan/-/archive/{pkgver}/simple-scan-{pkgver}.tar.gz"
sha256 = "9f9d711e1b65c32ec088fc297b48040f8eebbe2e98565dfc18e7f6b994f8f300"
hardening = ["vis", "!cfi"]
