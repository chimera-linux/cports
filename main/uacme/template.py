pkgname = "uacme"
pkgver = "1.7.5"
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
    "libcurl-devel",
    "libev-devel",
    "openssl-devel",
]
pkgdesc = "ACMEv2 client"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/ndilieto/uacme"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f75a375d95567145625366058fc8ed5359c575f62ec89e6b06b060de4c669d25"
hardening = ["vis", "cfi"]
