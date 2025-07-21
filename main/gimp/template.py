pkgname = "gimp"
pkgver = "3.0.4"
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
    "bison",
    "flex",
    "gettext-devel",
    "gjs",
    "glib-devel",
    "gobject-introspection",
    "iso-codes",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-gobject",
    "shared-mime-info",
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
    "ghostscript-devel",
    "glib-devel",
    "gtk+3-devel",
    "harfbuzz-devel",
    "json-glib-devel",
    "lcms2-devel",
    "libarchive-devel",
    "libgudev-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libmypaint-devel",
    "libomp-devel",
    "libpng-devel",
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
    "poppler-devel",
    "webkitgtk-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = [
    "gjs",
    "iso-codes",
    "mypaint-brushes",
    # prevent scripts from crashing (which prints annoying messages)
    "python-gobject",
]
checkdepends = ["dbus"]
pkgdesc = "GNU Image Manipulation Program"
license = "GPL-3.0-only"
url = "https://www.gimp.org"
source = f"https://download.gimp.org/pub/gimp/v{pkgver[:3]}/gimp-{pkgver.replace('_', '-').upper()}.tar.xz"
sha256 = "8caa2ec275bf09326575654ac276afc083f8491e7cca45d19cf29e696aecab25"
# FIXME: it worksish but crashes often/early
hardening = ["!int"]
# needs graphical env (gtk3 broken in weston headless)
options = ["!cross", "!check"]

if self.profile().endian == "big":
    broken = "hangs forever in last build step"


@subpackage("gimp-libs")
def _(self):
    return self.default_libs()


@subpackage("gimp-devel")
def _(self):
    return self.default_devel()
