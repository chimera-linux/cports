pkgname = "lagrange"
pkgver = "1.18.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
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
    "pcre2-devel",
    "sdl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Beautiful gemini client"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://gmi.skyjake.fi/lagrange"
source = f"https://github.com/skyjake/lagrange/releases/download/v{pkgver}/lagrange-{pkgver}.tar.gz"
sha256 = "d23a89bfcdbd654f2b54c2406e359d7687595bc1b5dbbd13882e02397d546345"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
