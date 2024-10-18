pkgname = "curtail"
pkgver = "1.11.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "meson",
    "pkgconf",
]
depends = [
    "jpegoptim",
    "libadwaita",
    "libwebp-progs",
    "oxipng",
    "pngquant",
    "python-gobject",
    "python-scour",
]
pkgdesc = "GTK image compressor"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/Huluti/Curtail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b5a33041ff64edbdcad293113d472a9de93f4b83be6efd99661cb2555050a068"
