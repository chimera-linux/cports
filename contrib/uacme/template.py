pkgname = "uacme"
pkgver = "1.7.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-openssl"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "asciidoc",
    "automake",
    "gmake",
    "pkgconf",
]
makedepends = [
    "libcurl-devel",
    "libev-devel",
    "openssl-devel",
]
pkgdesc = "ACMEv2 client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/ndilieto/uacme"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0fd3e35218d575321e70dc3489ec3463d015c56c138e99e5add32ab7e5a48d09"
hardening = ["vis", "cfi"]
