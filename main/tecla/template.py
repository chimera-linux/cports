pkgname = "tecla"
pkgver = "47_rc"
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
source = (
    f"$(GNOME_SITE)/tecla/{pkgver[:2]}/tecla-{pkgver.replace('_', '.')}.tar.xz"
)
sha256 = "c4bef86744b8a08d6a2298975a6f33b31f0f6e645d6dd4552760c876437e1c94"
