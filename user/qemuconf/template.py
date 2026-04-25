pkgname = "qemuconf"
pkgver = "0.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc"]
pkgdesc = "Utility to configure virtual machines for QEMU"
license = "MIT"
url = "https://github.com/zeppe-lin/qemuconf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b398b7717a6eefd54388fe9cd783527e822871771316bc268061db67052d587"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
