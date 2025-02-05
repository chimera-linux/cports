pkgname = "curtail"
pkgver = "1.12.0"
pkgrel = 0
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/Huluti/Curtail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7ca6f13012d7cb3ddc94b625c5cad5aefc9d535511dec67e55774c0429c43fb0"
