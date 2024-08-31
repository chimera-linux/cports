pkgname = "xed"
pkgver = "3.6.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared", "-Ddocs=true"]
hostmakedepends = [
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "itstool",
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
sha256 = "1a5b7163eba370c10a57eee6dde5d21d7ffca5ba09ebd98be737f909b0c63503"
# Tests require the "dogtail" Python module
options = ["!check", "!cross"]


@subpackage("xed-devel")
def _(self):
    return self.default_devel()
