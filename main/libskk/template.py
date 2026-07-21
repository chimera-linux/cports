pkgname = "libskk"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
# old and doesn't reconf
configure_gen = []
# fails when 'basic' runs before 'user-dict'
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "gettext-devel",
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
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libskk"
source = f"{url}/releases/download/{pkgver}/libskk-{pkgver}.tar.xz"
sha256 = "2d4c15976d459ef0004ce1c0e47506c7859d0b6f4fb104ed837f3326d235bb56"
tool_flags = {
    "CFLAGS": [
        "-Wno-incompatible-function-pointer-types",
        "-Wno-int-conversion",
    ]
}


@subpackage("libskk-devel")
def _(self):
    return self.default_devel()
