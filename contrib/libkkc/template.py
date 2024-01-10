pkgname = "libkkc"
pkgver = "0.3.5"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "gobject-introspection",
    "intltool",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "json-glib-devel",
    "libgee-devel",
    "marisa-trie-devel",
    "vala-devel",
]
pkgdesc = "Japanese input method library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libkkc"
source = f"https://github.com/ueno/libkkc/releases/download/v{pkgver}/libkkc-{pkgver}.tar.gz"
sha256 = "89b07b042dae5726d306aaa1296d1695cb75c4516f4b4879bc3781fe52f62aef"


@subpackage("libkkc-devel")
def _devel(self):
    return self.default_devel()


tool_flags = {
    "CFLAGS": [
        "-Wno-incompatible-function-pointer-types",
        "-Wno-int-conversion",
    ],
}
