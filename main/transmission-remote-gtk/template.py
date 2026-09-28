pkgname = "transmission-remote-gtk"
pkgver = "1.7.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = ["gtk+3-devel", "json-glib-devel", "libsoup-devel"]
pkgdesc = "GTK client for remote management of Transmission torrent client"
license = "GPL-2.0-or-later"
url = "https://github.com/transmission-remote-gtk/transmission-remote-gtk"
source = (
    f"{url}/releases/download/{pkgver}/transmission-remote-gtk-{pkgver}.tar.xz"
)
sha256 = "5ef98bd96b3b77eb3880474a2d904e316bb29cbd22dfa0ca85d43b04a28fba34"
