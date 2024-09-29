pkgname = "tecla"
pkgver = "47.0"
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
source = f"$(GNOME_SITE)/tecla/{pkgver[:-2]}/tecla-{pkgver}.tar.xz"
sha256 = "0790b99ec29137a54b546c510661a99aa6f039c8d75f10c08e928682c0804fe5"
