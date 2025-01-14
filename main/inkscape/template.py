pkgname = "inkscape"
pkgver = "1.4"
pkgrel = 5
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
    "librevenge-devel",
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
    "python-tinycss2",
]
pkgdesc = "Vector graphics editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://inkscape.org"
source = (
    f"https://media.inkscape.org/dl/resources/file/inkscape-{pkgver}.tar.xz"
)
sha256 = "c59a85453b699addebcd51c1dc07684dd96a10c8aec716b19551db50562e13f5"
# TODO
hardening = ["!int"]
# long, heavy, etc
options = ["!check"]

if self.profile().arch in ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-DWITH_OPENMP=OFF"]
