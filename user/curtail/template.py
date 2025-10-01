pkgname = "curtail"
pkgver = "1.13.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
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
license = "GPL-3.0-or-later"
url = "https://github.com/Huluti/Curtail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5794d466ff58805a68249b0b8e27bef8e7470d24d930c4211dcee905d05e728e"
