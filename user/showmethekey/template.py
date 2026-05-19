pkgname = "showmethekey"
pkgver = "1.21.0"
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
sha256 = "db36e7bac76262e6155d48ae72e126b29b9aff711c72f073bc390a424c6bf86d"
