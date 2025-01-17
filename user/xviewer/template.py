pkgname = "xviewer"
pkgver = "3.4.8"
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
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/xviewer/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "c8abe0e9a19ba867c620a1c417bb719b6c1e07e5baa444697d1e71ad8f676889"
options = ["!cross"]


@subpackage("xviewer-devel")
def _(self):
    return self.default_devel()
