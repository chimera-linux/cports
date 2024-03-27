pkgname = "gimp"
pkgver = "2.99.18"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcheck-update=no",
    "-Dbug-report-url=https://github.com/chimera-linux/cports/issues",
    "-Dlibbacktrace=false",
    "-Ddefault_library=shared",
    # this needs luajit and prints junk into the console
    "-Dlua=disabled",
]
hostmakedepends = [
    "gegl",
    "gettext-devel",
    "gjs",
    "glib-devel",
    "gobject-introspection",
    "iso-codes",
    "meson",
    "perl",
    "pkgconf",
    "python-gobject",
    "shared-mime-info",
    "xsltproc",
]
makedepends = [
    "alsa-lib-devel",
    "appstream-glib-devel",
    "at-spi2-core-devel",
    "babl-devel",
    "cairo-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "gegl-devel",
    "gexiv2-devel",
    "glib-devel",
    "gtk+3-devel",
    "harfbuzz-devel",
    "json-glib-devel",
    "lcms2-devel",
    "libarchive-devel",
    "libgs-devel",
    "libgudev-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libmypaint-devel",
    "libpng-devel",
    "libpoppler-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libunwind-devel",
    "libwebp-devel",
    "libxcursor-devel",
    "libxmu-devel",
    "libxpm-devel",
    "linux-headers",
    "mypaint-brushes",
    "openjpeg-devel",
    "pango-devel",
    "poppler-data",
    "webkitgtk-devel",
    "xz-devel",
    "zlib-devel",
]
depends = [
    "iso-codes",
    "gjs",
    "mypaint-brushes",
    # prevent scripts from crashing (which prints annoying messages)
    "python-gobject",
]
checkdepends = ["dbus"]
pkgdesc = "GNU Image Manipulation Program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://www.gimp.org"
source = f"https://download.gimp.org/pub/{pkgname}/v{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8c1bb7a94ac0d4d0cde4d701d8b356387c2ecd87abbd35bbf7d222d40f6ddb6e"
# FIXME: it worksish but crashes often/early
hardening = ["!int"]
options = ["!cross"]


@subpackage("gimp-libs")
def _libs(self):
    return self.default_libs()


@subpackage("gimp-devel")
def _devel(self):
    return self.default_devel()
