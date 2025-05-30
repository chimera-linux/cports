pkgname = "showmethekey"
pkgver = "1.18.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libevdev-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "udev-devel",
]
pkgdesc = "Show keys you typed on screen"
license = "Apache-2.0"
url = "https://github.com/AlynxZhou/showmethekey"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dee790c12e4946587d5b9979ad3ec37862a0f59e300756db5c93e39cc4efa0ff"
