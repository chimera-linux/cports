pkgname = "lagrange"
pkgver = "1.18.4"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gmi.skyjake.fi/lagrange"
source = f"https://github.com/skyjake/lagrange/releases/download/v{pkgver}/lagrange-{pkgver}.tar.gz"
sha256 = "6972750acfcbb836ec33fe7ddace9415081b926353d7d2eab7a2cf8faee66d30"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
