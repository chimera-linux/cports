pkgname = "axel"
pkgver = "2.17.14"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "pkgconf",
    "txt2man",
]
makedepends = ["gettext-devel", "openssl3-devel"]
pkgdesc = "Lightweight CLI download accelerator"
license = "GPL-2.0-or-later"
url = "https://github.com/axel-download-accelerator/axel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f6f2a5369d78003ab162a774cff0be71096bea6929333a79c8168c82caced07d"
hardening = ["vis", "cfi"]
