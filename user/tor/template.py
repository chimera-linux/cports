pkgname = "tor"
pkgver = "0.4.9.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--sysconfdir=/usr/share/etc"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "bash",
    "python",
]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://www.torproject.org"
source = f"https://dist.torproject.org/tor-{pkgver}.tar.gz"
sha256 = "a89aba97052e9963a654b40df2d46be07e8a6b6e24e5437917fd81acd90a7017"


def post_install(self):
    self.mv(">/usr/share/etc/tor/torrc.sample", ">/usr/share/etc/tor/torrc")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/tor")
    self.install_license("LICENSE")
