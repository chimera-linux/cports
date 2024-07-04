pkgname = "conky"
pkgver = "1.21.4"
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
    "libcurl-devel",
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://conky.cc"
source = [
    f"https://github.com/brndnmtthws/conky/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/brndnmtthws/conky/releases/download/v{pkgver}/conky.1.gz",
]
source_paths = [".", "manpage"]
sha256 = [
    "567607122272f4d7d9c2665319b5c17c1aab1f953d388fbfcf4b22c5acab4480",
    "ce4d49dd9e1f9eafe668c21c456ad81257fff6975139e0bf0806e3d3f1ff19ed",
]
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# needs host tolua++
options = ["!cross"]


def post_install(self):
    self.install_man("manpage/conky.1")
