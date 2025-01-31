pkgname = "x11vnc"
pkgver = "0.9.16"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "pkgconf"]
makedepends = [
    "libx11-devel",
    "libvncserver-devel",
    "libxtst-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC server for real X displays"
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-2.0-or-later WITH x11vnc-openssl-exception"
url = "https://github.com/LibVNC/x11vnc"
source = f"https://github.com/LibVNC/x11vnc/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "885e5b5f5f25eec6f9e4a1e8be3d0ac71a686331ee1cfb442dba391111bd32bd"
