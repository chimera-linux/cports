pkgname = "gnome-tweaks"
pkgver = "45.2"
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
sha256 = "01bf5e723a1d18b1025401e32b5f64eb29b79e8a17ad010bbbd1e23b137b9069"
