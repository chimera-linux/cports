pkgname = "mbpfan"
pkgver = "2.4.0"
pkgrel = 0
build_style = "makefile"
makedepends = ["gmake", "dinit-chimera", "linux-headers"]
pkgdesc = "Daemon to control fan speed on MacBook/MacBook Pro"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-on-mac/mbpfan"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e1cdcffaba52be215ae40a8568949190866d500d6ae2a1e96b71ab5372f3580b"
hardening = ["vis", "cfi"]
# tests require a MacBook to run
options = ["!check"]


def post_install(self):
    self.install_service("^/mbpfan")
