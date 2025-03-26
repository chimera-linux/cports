pkgname = "conky"
pkgver = "1.22.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_CURL=ON",
    "-DBUILD_HTTP=ON",
    "-DBUILD_IMLIB2=ON",
    "-DBUILD_INTEL_BACKLIGHT=ON",
    "-DBUILD_LUA_CAIRO=ON",
    "-DBUILD_PULSEAUDIO=ON",
    "-DBUILD_RSS=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_WAYLAND=ON",
    "-DBUILD_WLAN=ON",
    "-DBUILD_XDAMAGE=ON",
    "-DBUILD_XFIXES=ON",
    "-DRELEASE=ON",
]
hostmakedepends = [
    "cmake",
    "gperf",
    "ninja",
    "pkgconf",
    "python-pyyaml",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "freetype-devel",
    "imlib2-devel",
    "curl-devel",
    "libmicrohttpd-devel",
    "libmpdclient-devel",
    "libpulse-devel",
    "libxdamage-devel",
    "libxfixes-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxml2-devel",
    "linux-headers",
    "lua5.4-devel",
    "ncurses-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
    "wireless-tools-devel",
]
pkgdesc = "System-monitor with various OS integrations"
license = "GPL-3.0-or-later"
url = "https://conky.cc"
source = [
    f"https://github.com/brndnmtthws/conky/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/brndnmtthws/conky/releases/download/v{pkgver}/conky.1.gz>conky-{pkgver}.1.gz",
]
source_paths = [".", "manpage"]
sha256 = [
    "9959fde719d3d4340ab973aadbeb97a03e9f6bf4f928be0de69cfb02871d522e",
    "66cd1bc57e8166d1ee6ed1c08c584942262f0044d1da9b4b37ddb4d0fad9abdc",
]
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# needs host tolua++
options = ["!cross"]


def post_install(self):
    self.install_man(f"manpage/conky-{pkgver}.1", name="conky")
