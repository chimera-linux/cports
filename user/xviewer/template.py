pkgname = "xviewer"
pkgver = "3.4.12"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "gtk-doc-tools",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "cinnamon-desktop-devel",
    "exempi-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libexif-devel",
    "libjpeg-turbo-devel",
    "libpeas-devel",
    "librsvg-devel",
    "libx11-devel",
    "xapp-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Generic image viewer"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/xviewer/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "323b7e9799a1f0e57501a6c1b0886a2a5a899ea3ccb0993ca0d7fbcfb987cc0e"
options = ["!cross"]


@subpackage("xviewer-devel")
def _(self):
    return self.default_devel()
