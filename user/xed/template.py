pkgname = "xed"
pkgver = "3.6.7"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared", "-Ddocs=true"]
hostmakedepends = [
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "itstool",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gspell-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libpeas-devel",
    "libx11-devel",
    "libxml2-devel",
    "pango-devel",
    "xapp-devel",
]
depends = ["libpeas", "python-gobject"]
pkgdesc = "X-Apps text editor"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xed/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dc9af1c9175e03cc9c3a65d4c06191ca1adac1365b0f93b5cf242dcc03ae837a"
# Tests require the "dogtail" Python module
options = ["!check", "!cross"]


@subpackage("xed-devel")
def _(self):
    return self.default_devel()
