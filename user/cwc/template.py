pkgname = "cwc"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "clang",
    "cmake",
    "git",
    "meson",
    "ninja",
    "pkgconf",
    "wayland-protocols",
]
makedepends = [
    "cairo-devel",
    "hyprcursor-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "lua5.1-lgi",
    "luajit-devel",
    "pango-devel",
    "wayland-devel",
    "wlroots0.20-devel",
    "xwayland-devel",
    "xxhash-devel",
]
depends = ["lua5.1-lgi"]
pkgdesc = "Hackable dynamic wayland compositor"
license = "GPL-3.0-only"
url = "https://github.com/Cudiph/cwcwm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "285fd1d33f06877b1a73c5ef59341f37c064e67f2bba7762ac334f29909777e5"
