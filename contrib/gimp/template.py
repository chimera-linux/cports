pkgname = "gimp"
pkgver = "2.99.14"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcheck-update=no",
    "-Dbug-report-url=https://github.com/chimera-linux/cports/issues",
    "-Dlibbacktrace=false",
    "-Ddefault_library=shared",
    # this needs luajit and prints junk into the console
    "-Dlua=false",
]
hostmakedepends = [
    "meson", "pkgconf", "perl", "gegl", "gettext-tiny-devel", "glib-devel",
    "gobject-introspection", "xsltproc", "bash", "iso-codes",
    "shared-mime-info", "python-gobject", "gjs",
]
makedepends = [
    "babl-devel", "gegl-devel", "gtk+3-devel", "glib-devel", "librsvg-devel",
    "gdk-pixbuf-devel", "libtiff-devel", "libpng-devel", "libwebp-devel",
    "libjpeg-turbo-devel", "openjpeg-devel", "libheif-devel", "libxpm-devel",
    "gexiv2-devel", "zlib-devel", "liblzma-devel", "libarchive-devel",
    "libpoppler-glib-devel", "poppler-data", "libgs-devel", "cairo-devel",
    "freetype-devel", "harfbuzz-devel", "pango-devel", "fontconfig-devel",
    "lcms2-devel", "webkitgtk-devel", "libxcursor-devel", "libxmu-devel",
    "alsa-lib-devel", "libmypaint-devel", "mypaint-brushes",
    "at-spi2-core-devel", "appstream-glib-devel", "json-glib-devel",
    "libgudev-devel", "libunwind-devel", "linux-headers",
]
depends = [
    "desktop-file-utils", "hicolor-icon-theme", "mypaint-brushes", "iso-codes",
    # prevent scripts from crashing (which prints annoying messages)
    "python-gobject", "gjs"
]
checkdepends = ["dbus"]
pkgdesc = "GNU Image Manipulation Program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://www.gimp.org"
source = f"https://download.gimp.org/pub/{pkgname}/v{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "313a205475d1ff03c5c4d9602f09f5c975ba6c1c79d8843e2396f9fe2abdf7a8"
# FIXME: it worksish but crashes often/early
hardening = ["!int"]
options = ["!cross"]

@subpackage("gimp-libs")
def _libs(self):
    return self.default_libs()

@subpackage("gimp-devel")
def _devel(self):
    return self.default_devel()
