pkgname = "celluloid"
pkgver = "0.27"
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
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-3.0-or-later"
url = "https://celluloid-player.github.io"
source = f"https://github.com/celluloid-player/celluloid/releases/download/v{pkgver}/celluloid-{pkgver}.tar.xz"
sha256 = "216656c4495bb3ca02dc4ad9cf3da8e8f15c8f80e870eeac8eb1eedab4c3788b"
