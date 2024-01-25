pkgname = "libskk"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
# old and doesn't reconf
configure_gen = []
make_cmd = "gmake"
# fails when 'basic' runs before 'user-dict'
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gobject-introspection",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "json-glib-devel",
    "libgee-devel",
    "libxkbcommon-devel",
    "vala-devel",
]
depends = ["skkdict"]
pkgdesc = "Japanese input method library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libskk"
source = f"{url}/releases/download/{pkgver}/libskk-{pkgver}.tar.xz"
sha256 = "b295eb9c248e353750c96474b2b55c4e627524fc6dc79439ff56f73ba09c3949"
tool_flags = {
    "CFLAGS": [
        "-Wno-incompatible-function-pointer-types",
        "-Wno-int-conversion",
    ]
}


@subpackage("libskk-devel")
def _devel(self):
    return self.default_devel()
