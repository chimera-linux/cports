pkgname = "ibus-hangul"
pkgver = "1.5.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "python",
    "swig",
]
makedepends = [
    "gtk+3-devel",
    "ibus-devel",
    "libhangul-devel",
]
depends = [
    "ibus",
    "python-gobject",
]
pkgdesc = "Korean input engine for IBus"
license = "GPL-2.0-or-later"
url = "https://github.com/libhangul/ibus-hangul"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a5aac88286cd18960229860e3e1a778978a7aeaa484ad9acfa48284b87fdc3bb"
# tests require interactive environment
options = ["!check"]
