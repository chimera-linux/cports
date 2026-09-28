pkgname = "libkkc"
# abandoned repo, easier to build with all fixes
pkgver = "0.3.5_git20240902"
pkgrel = 0
build_style = "gnu_configure"
# otherwise doesn't find .vapi from inside build
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
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
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libkkc"
_gitrev = "ce17a35d3dca32706ae2dd48c7859a36531a9b59"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "4169cbd51a9223d70f6621632894b56e40b6883787d5c07c968eb51855f04e70"
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
def _(self):
    return self.default_devel()
