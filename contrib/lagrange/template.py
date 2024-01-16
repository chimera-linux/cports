pkgname = "lagrange"
pkgver = "1.17.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_POPUP_MENUS=OFF",
    "-DENABLE_X11_XLIB=OFF",
    "-DTFDN_ENABLE_SSE41=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "zip",
]
makedepends = [
    "fribidi-devel",
    "harfbuzz-devel",
    "libunistring-devel",
    "libwebp-devel",
    "mpg123-devel",
    "openssl-devel",
    "sdl-devel",
    "pcre2-devel",
    "zlib-devel",
]
pkgdesc = "Beautiful gemini client"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://gmi.skyjake.fi/lagrange"
source = f"https://github.com/skyjake/lagrange/releases/download/v{pkgver}/lagrange-{pkgver}.tar.gz"
sha256 = "b9d0982617fec495565ac9c09fb788a0be207d6fdf2324edc390e5cac8b1523b"
# FIXME cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
