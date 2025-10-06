pkgname = "simple-scan"
pkgver = "49.0.1"
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
sha256 = "f123e0e3c319381a4749e01f51a5e3764028fc9aa8a6afb2696426ce96706315"
hardening = ["vis", "!cfi"]
