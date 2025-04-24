pkgname = "lagrange"
pkgver = "1.18.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_POPUP_MENUS=OFF",
    "-DENABLE_TUI=ON",
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
    "ncurses-devel",
    "openssl3-devel",
    "opusfile-devel",
    "pcre2-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Beautiful gemini client"
license = "BSD-2-Clause"
url = "https://gmi.skyjake.fi/lagrange"
source = f"https://github.com/skyjake/lagrange/releases/download/v{pkgver}/lagrange-{pkgver}.tar.gz"
sha256 = "1dded64803eef8ff162e79025fd6db60f4a19bac5f9b804f46d79e07cbda5c65"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
