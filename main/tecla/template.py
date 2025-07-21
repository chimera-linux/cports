pkgname = "tecla"
pkgver = "48.0.2"
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
sha256 = "783d3464d2a2cf7eb1507649dbd9ff09ce24852c2a6c9a0d365db84063d3d401"
