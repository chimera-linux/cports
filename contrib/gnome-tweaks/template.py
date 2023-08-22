pkgname = "gnome-tweaks"
pkgver = "42_beta"
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-5]}/{pkgname}-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "83f44cc1dc8adc770cdad717b403cb9a6cc3c0de50e38e6f1e678b43401ad868"
