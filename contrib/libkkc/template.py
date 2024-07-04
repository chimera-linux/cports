pkgname = "libkkc"
# abandoned repo, easier to build with all fixes
pkgver = "0.3.5_git20210928"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
# otherwise doesn't find .vapi from inside build
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gobject-introspection",
    "intltool",
    "libtool",
    "pkgconf",
    "python-marisa",
    "vala-devel",
]
makedepends = [
    "json-glib-devel",
    "libgee-devel",
    "marisa-trie-devel",
]
depends = ["libkkc-data"]
pkgdesc = "Japanese kana-kanji conversion library"
maintainer = "Nasado <hi@nasado.name>"
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libkkc"
_gitrev = "cdcaf4dceaf273bfe7b018a4a651a92f786c6ec6"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "7ea73e568cf551f756f0bc6721484ba901623d4c73b027ff36cd14e0dee66996"
tool_flags = {
    "CFLAGS": [
        "-Wno-incompatible-function-pointer-types",
        "-Wno-int-conversion",
    ]
}
# cross: gobject-introspection
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/share/libkkc/templates/libkkc-data/configure.ac.in")
    self.uninstall("usr/share/libkkc/templates/libkkc-data/data/Makefile.am")
    self.uninstall("usr/share/libkkc/templates/libkkc-data/tools/Makefile.am")


@subpackage("libkkc-devel")
def _devel(self):
    return self.default_devel()
