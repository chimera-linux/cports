pkgname = "simple-scan"
pkgver = "46.0"
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
source = f"$(GNOME_SITE)/simple-scan/{pkgver[:-2]}/simple-scan-{pkgver}.tar.xz"
sha256 = "c16e6590142fe563be5143122b3bbb53f6b00a7da9d952f61c47fa26f7b4f0a9"
hardening = ["vis", "!cfi"]
