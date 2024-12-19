pkgname = "love"
pkgver = "11.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = [
    "freetype-devel",
    "libmodplug-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libx11-devel",
    "luajit-devel",
    "mpg123-devel",
    "openal-soft-devel",
    "sdl-devel",
    "zlib-ng-devel",
]
pkgdesc = "Lua 2D graphics library"
maintainer = "sudan <sudanchapagain@proton.me>"
license = "Zlib"
url = "https://love2d.org"
source = f"https://github.com/love2d/love/releases/download/{pkgver}/love-{pkgver}-linux-src.tar.gz"
sha256 = "066e0843f71aa9fd28b8eaf27d41abb74bfaef7556153ac2e3cf08eafc874c39"


if self.profile().endian == "big":
    broken = "not implemented"
