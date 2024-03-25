pkgname = "tecla"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libxkbcommon-devel",
]
pkgdesc = "GNOME keyboard layout viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/tecla"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4a081eab867a5a8b09758991cad7645920f323aabca954408290fb6f44591b0f"
