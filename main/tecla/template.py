pkgname = "tecla"
pkgver = "51.0"
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
sha256 = "ddf1a8555044171d0d84b580d6d541c3c621ae77996f6bc5edde598de2f8625b"
