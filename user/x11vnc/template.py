pkgname = "x11vnc"
pkgver = "0.9.17"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "libvncserver-devel",
    "libx11-devel",
    "libxtst-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC server for real X displays"
license = "GPL-2.0-or-later WITH x11vnc-openssl-exception"
url = "https://github.com/LibVNC/x11vnc"
source = f"https://github.com/LibVNC/x11vnc/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3ab47c042bc1c33f00c7e9273ab674665b85ab10592a8e0425589fe7f3eb1a69"
