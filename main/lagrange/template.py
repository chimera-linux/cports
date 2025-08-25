pkgname = "lagrange"
pkgver = "1.18.6"
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
sha256 = "8a0a78aea79f287c5bf2161c8c2e3546bd1ab7b44ac8536b00beb1fb2e7189f4"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
