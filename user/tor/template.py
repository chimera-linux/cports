pkgname = "tor"
pkgver = "0.4.9.5"
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
sha256 = "c949c2f86b348e64891976f6b1e49c177655b23df97193049bf1b8cd3099e179"


def post_install(self):
    self.mv(">/usr/share/etc/tor/torrc.sample", ">/usr/share/etc/tor/torrc")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/tor")
    self.install_license("LICENSE")
