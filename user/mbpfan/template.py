pkgname = "mbpfan"
pkgver = "2.5.0"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
hostmakedepends = ["dos2unix"]
makedepends = ["dinit-chimera", "linux-headers"]
pkgdesc = "Daemon to control fan speed on MacBook/MacBook Pro"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-on-mac/mbpfan"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "39abc610472958b8bfc0812072fc6fc9461bcef5bf0b9d6ece854ecea37f87c5"
hardening = ["vis", "cfi"]
# tests require a MacBook to run
options = ["etcfiles", "!check"]


def post_extract(self):
    # some patched files have windows line endings
    self.do("dos2unix", "src/settings.h")
    self.do("dos2unix", "src/settings.c")


def post_install(self):
    self.install_service(self.files_path / "mbpfan")
