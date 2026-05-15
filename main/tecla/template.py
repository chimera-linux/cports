pkgname = "tecla"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libxkbcommon-devel",
]
pkgdesc = "GNOME keyboard layout viewer"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/tecla"
source = f"$(GNOME_SITE)/tecla/{pkgver.split('.')[0]}/tecla-{pkgver}.tar.xz"
sha256 = "2542acb24850082e0ccf6aa17af9651db71d22f0e233fdbf5ed0cffe2e45bc06"
