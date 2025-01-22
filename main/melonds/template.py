pkgname = "melonds"
pkgver = "0.9.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUSE_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libarchive-devel",
    "libslirp-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "sdl2-compat-devel",
]
pkgdesc = "DS emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://melonds.kuribo64.net"
source = (
    f"https://github.com/melonDS-emu/melonDS/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "52c6b99340b8bba8c52b11a2242591f05e838c34ddd9ec20dcf1a6039405434a"
