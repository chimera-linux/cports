pkgname = "lagrange"
pkgver = "1.17.2"
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
sha256 = "17500698dd9f90ef46dc2c360f00b392f24ddc85d4f07e664834ee05a4a40f62"
# FIXME cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
