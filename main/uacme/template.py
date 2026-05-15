pkgname = "uacme"
pkgver = "1.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-openssl"]
make_dir = "."
hostmakedepends = [
    "asciidoc",
    "automake",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "libev-devel",
    "openssl3-devel",
]
pkgdesc = "ACMEv2 client"
license = "GPL-3.0-or-later"
url = "https://github.com/ndilieto/uacme"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "921d0ad09edbb96d02adbdac5cafc1f6d7e5f929d833c375fd2028ada1a95d39"
hardening = ["vis", "cfi"]
