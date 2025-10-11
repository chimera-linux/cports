pkgname = "xed"
pkgver = "3.8.4"
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
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xed/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1660fd85506ff1c12ff09953f70abcd67e425d5a7a0c3f6ba7f49a0a38458c4f"
# Tests require the "dogtail" Python module
options = ["!check", "!cross"]


@subpackage("xed-devel")
def _(self):
    return self.default_devel()
