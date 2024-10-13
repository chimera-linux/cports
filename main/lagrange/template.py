pkgname = "lagrange"
pkgver = "1.18.2"
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
    "openssl-devel",
    "opusfile-devel",
    "pcre2-devel",
    "sdl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Beautiful gemini client"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://gmi.skyjake.fi/lagrange"
source = f"https://github.com/skyjake/lagrange/releases/download/v{pkgver}/lagrange-{pkgver}.tar.gz"
sha256 = "12589f8df485f35506ebdc3bfe298227db2f6e8f289ca49a1ba522368b94477b"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
