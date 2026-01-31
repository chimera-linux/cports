pkgname = "vttest"
pkgver = "20251205"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Tool for testing VT100 compatibility of terminals"
license = "MIT"
url = "https://invisible-island.net/vttest"
source = f"https://invisible-island.net/archives/vttest/vttest-{pkgver}.tgz"
sha256 = "cd6886f9aefe6a3f6c566fa61271a55710901a71849c630bf5376aa984bf77cc"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
