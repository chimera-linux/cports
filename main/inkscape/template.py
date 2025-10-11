pkgname = "inkscape"
pkgver = "1.4.2"
pkgrel = 6
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://inkscape.org"
source = (
    f"https://media.inkscape.org/dl/resources/file/inkscape-{pkgver}.tar.xz"
)
sha256 = "2000530c7917e5260c9e8575a7154ff6926643d2006487d714e304a963f0c782"
# TODO
hardening = ["!int"]
# long, heavy, etc
options = ["!check"]

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-DWITH_OPENMP=OFF"]
