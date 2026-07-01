pkgname = "vttest"
pkgver = "20251205"
pkgrel = 1
pkgdesc = "Tool for testing VT100 compatibility of terminals"
license = "MIT"
url = "https://invisible-island.net/vttest"
hardening = ["vis", "cfi"] # 'sst' results in SIGSEGV (address boundary error)

source = f"https://invisible-island.net/archives/vttest/vttest-{pkgver}.tgz"
sha256 = "cd6886f9aefe6a3f6c566fa61271a55710901a71849c630bf5376aa984bf77cc"


def build(self):
    self.do("./configure", "--prefix=/usr")
    self.do("make")


def install(self):
    self.install_bin("vttest")
    self.install_man("vttest.1")
    self.install_license("COPYING")
