pkgname = "uacme"
pkgver = "1.7.6"
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
    "openssl-devel",
]
pkgdesc = "ACMEv2 client"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/ndilieto/uacme"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "484088abdcb8dd134f1334626b1a4df2d9c475e0e537cd498eb5c6dd621373c7"
hardening = ["vis", "cfi"]
