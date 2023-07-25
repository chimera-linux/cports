pkgname = "inkscape"
pkgver = "1.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DBUILD_TESTING=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "gettext-tiny",
    "glib-devel",
]
# TODO: graphicsmagick once we have it
makedepends = [
    "gtk+3-devel",
    "boost-devel",
    "gc-devel",
    "gtkmm3.0-devel",
    "gspell-devel",
    "lcms2-devel",
    "libcdr-devel",
    "libwpg-devel",
    "libvisio-devel",
    "librevenge-devel",
    "libjpeg-turbo-devel",
    "libsoup-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libpoppler-glib-devel",
    "popt-devel",
    "potrace-devel",
    "gsl-devel",
    "double-conversion-devel",
    "libomp-devel",
    "python-devel",
    "libedit-readline-devel",
]
depends = [
    "desktop-file-utils",
    "python-scour",
    "python-appdirs",
    "python-lxml",
    "python-pillow",
]
pkgdesc = "Vector graphics editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://inkscape.org"
source = (
    f"https://media.inkscape.org/dl/resources/file/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "bf4f286b025e0169b8948cc14d5199a9b4c204d761c894c4b48496571ec76307"
# TODO
hardening = ["!int"]
# long, heavy, etc
options = ["!check"]
