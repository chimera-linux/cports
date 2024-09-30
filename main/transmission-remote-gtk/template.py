pkgname = "transmission-remote-gtk"
pkgver = "1.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream-glib",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "json-glib-devel", "libsoup-devel"]
pkgdesc = "GTK client for remote management of Transmission torrent client"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-2.0-or-later"
url = "https://github.com/transmission-remote-gtk/transmission-remote-gtk"
source = (
    f"{url}/releases/download/{pkgver}/transmission-remote-gtk-{pkgver}.tar.xz"
)
sha256 = "b090844f6a482e6f3588070ff3fdd54b79e8f85df02b39853cfb01fccee10cac"
patch_style = "patch"
