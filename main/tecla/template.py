pkgname = "tecla"
pkgver = "49.0"
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
sha256 = "2ca424e402baf60cd6b13777703b701ebb1faf8f3d0f2f971144d823f651249f"
