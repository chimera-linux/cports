pkgname = "d-spy"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext-devel",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "D-Bus inspector and debugger"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/d-spy"
source = f"{url}/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "e9f720f97b69a36374f182436324b01e4461916b1a649f7b15ff6d82e78b8206"
hardening = ["vis", "!cfi"]
