pkgname = "inkscape"
pkgver = "1.3.2"
pkgrel = 14
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=OFF",
    "-DWITH_INTERNAL_2GEOM=OFF",
    "-DWITH_INTERNAL_CAIRO=OFF",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "glib-devel",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "double-conversion-devel",
    "gc-devel",
    "graphicsmagick-devel",
    "gsl-devel",
    "gspell-devel",
    "gtk+3-devel",
    "gtkmm3.0-devel",
    "gtksourceview4-devel",
    "lcms2-devel",
    "lib2geom-devel",
    "libcdr-devel",
    "libedit-readline-devel",
    "libjpeg-turbo-devel",
    "libomp-devel",
    "librevenge-devel",
    "libsoup-devel",
    "libvisio-devel",
    "libwpg-devel",
    "libxml2-devel",
    "libxslt-devel",
    "poppler-devel",
    "popt-devel",
    "potrace-devel",
    "python-devel",
]
depends = [
    "python-appdirs",
    "python-cssselect",
    "python-lxml",
    "python-numpy",
    "python-pillow",
    "python-scour",
]
pkgdesc = "Vector graphics editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://inkscape.org"
source = (
    f"https://media.inkscape.org/dl/resources/file/inkscape-{pkgver}.tar.xz"
)
sha256 = "dbd1844dc443fe5e10d3e9a887144e5fb7223852fff191cfb5ef7adeab0e086b"
# TODO
hardening = ["!int"]
# long, heavy, etc
options = ["!check"]
