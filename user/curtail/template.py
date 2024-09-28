pkgname = "curtail"
pkgver = "1.10.0"
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
sha256 = "f5e80862faa6d2dc9beb266a7eceb05197c261f4bba52a9211d75d10862833af"
