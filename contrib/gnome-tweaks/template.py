pkgname = "gnome-tweaks"
pkgver = "45.1"
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
sha256 = "95ffa7f38d9b1dfd5e4cebefb752419fea21cd407021395adc9f112854416d4f"
