pkgname = "ibus-skk"
pkgver = "1.4.4"
pkgrel = 0
build_style = "gnu_configure"
# old and doesn't reconf
configure_gen = []
make_dir = "."
hostmakedepends = [
    "automake",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = ["gtk+3-devel", "ibus-devel", "libskk-devel"]
depends = ["ibus"]
pkgdesc = "Japanese SKK engine for IBus"
license = "GPL-2.0-or-later"
url = "https://github.com/ueno/ibus-skk"
source = f"{url}/releases/download/ibus-skk-{pkgver}/ibus-skk-{pkgver}.tar.xz"
sha256 = "2d98069104a3907a6deaca56d08da68ab0a511617c818b392c6a85a21e012e59"
# valol
tool_flags = {"CFLAGS": ["-Wno-incompatible-pointer-types"]}
