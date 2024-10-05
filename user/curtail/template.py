pkgname = "curtail"
pkgver = "1.11.0"
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
sha256 = "38ee7d5ce79fc478366fce56f9bea7bf0d232e0291a62232467d0889ab9ecb8e"
