pkgname = "ibus-skk"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
# old and doesn't reconf
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = ["gtk+3-devel", "ibus-devel", "libskk-devel"]
depends = ["ibus"]
pkgdesc = "Japanese SKK engine for IBus"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/ueno/ibus-skk"
source = f"{url}/releases/download/ibus-skk-{pkgver}/ibus-skk-{pkgver}.tar.xz"
sha256 = "6661bd9d0bd7f8320d6041765a4bd307ec09b02e12d4191d035b4b698d39655d"
tool_flags = {
    "CFLAGS": [
        "-Wno-incompatible-function-pointer-types",
    ]
}
