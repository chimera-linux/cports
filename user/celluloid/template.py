pkgname = "celluloid"
pkgver = "0.29"
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
sha256 = "5b9991557cc2764a8281a24aa726a645287eb075cde0f0ae7c737965264a119c"
