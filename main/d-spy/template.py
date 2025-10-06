pkgname = "d-spy"
pkgver = "49.1"
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
    "libdex-devel",
]
pkgdesc = "D-Bus inspector and debugger"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/d-spy"
source = f"{url}/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "b8f7fa58d52af5da0691e7053eb78e0bcec481120e04f38143a097f5e8cc557d"
hardening = ["vis", "!cfi"]
