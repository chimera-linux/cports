pkgname = "celluloid"
pkgver = "0.30"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["glib-devel", "gettext", "meson", "pkgconf"]
makedepends = [
    "appstream-glib-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libepoxy-devel",
    "mpv-devel",
]
pkgdesc = "GTK frontend for mpv"
license = "GPL-3.0-or-later"
url = "https://celluloid-player.github.io"
source = f"https://github.com/celluloid-player/celluloid/releases/download/v{pkgver}/celluloid-{pkgver}.tar.xz"
sha256 = "7fef96431842c24e5ae78a9c42bc6523818a6c45213f23ceb146d037d6ec8559"
