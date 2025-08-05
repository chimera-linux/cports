pkgname = "showmethekey"
pkgver = "1.18.4"
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
sha256 = "ab0d921aa8daf7b56db9579c1b48e89ff177a42232ca1c6dbb17f352b766574b"
