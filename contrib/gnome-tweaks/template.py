pkgname = "gnome-tweaks"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext"]
makedepends = ["libhandy-devel"]
depends = [
    "gtk+3",
    "dconf",
    "mutter",
    "gnome-settings-daemon",
    "libnotify",
    "libhandy",
    "python-gobject",
]
pkgdesc = "GNOME tweak tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://wiki.gnome.org/Apps/Tweaks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "253994658ae861794d0c6e0e0f475dfe1caf277e3674b8792790238f34cfd6ee"
