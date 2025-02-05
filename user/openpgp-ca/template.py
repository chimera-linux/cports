pkgname = "openpgp-ca"
pkgver = "0.14.0"
pkgrel = 1
build_wrksrc = "openpgp-ca-bin"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "nettle-devel",
    "openssl3-devel",
    "pcsc-lite-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "CA tool for OpenPGP certificates"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "https://openpgp-ca.org"
source = f"https://gitlab.com/openpgp-ca/openpgp-ca/-/archive/openpgp-ca/v{pkgver}/openpgp-ca-openpgp-ca-v{pkgver}.tar.gz"
sha256 = "f923593ef73c906656b816b0884482bf6442f6a3db377ab2f5681e8d18916a73"
# Test suite requires gpg-agent set up and running
options = ["!check"]
