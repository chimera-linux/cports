pkgname = "jpm"
pkgver = "1.2.0"
pkgrel = 0
hostmakedepends = ["janet"]
depends = ["janet-devel-static"]
pkgdesc = "Project manager for Janet"
license = "MIT"
url = "https://github.com/janet-lang/jpm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4282b36b44a9b35367d128982f2cfaa67370e4e5a305b3999d86a64fadd308d2"


def install(self):
    self.do(
        "janet",
        "bootstrap.janet",
        env={"PREFIX": "/usr", "DESTDIR": self.chroot_destdir},
    )
    self.install_license("LICENSE")
