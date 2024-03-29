pkgname = "openpgp-ca"
pkgver = "0.13.1"
pkgrel = 0
build_wrksrc = "openpgp-ca-bin"
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "nettle-devel",
    "openssl-devel",
    "pcsc-lite-devel",
    "sqlite-devel",
]
pkgdesc = "CA tool for OpenPGP certificates"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "https://openpgp-ca.org"
source = f"https://gitlab.com/openpgp-ca/openpgp-ca/-/archive/openpgp-ca/v{pkgver}/openpgp-ca-openpgp-ca-v{pkgver}.tar.gz"
sha256 = "dc5be7d691b9c0b09fc5acb0c4ea0d6cdb3e0cd226da75100277c7a89f471f6d"
# Test suite requires gpg-agent set up and running
options = ["!check"]
