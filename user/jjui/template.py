pkgname = "jjui"
pkgver = "0.10.9"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/jjui"]
hostmakedepends = ["go"]
depends = ["jj"]
pkgdesc = "TUI for Jujutsu VCS framework"
license = "MIT"
url = "https://github.com/idursun/jjui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e6f74b3e00bb652f533331a15e4e0b9d6139a0db6f3f0f1e5b348ce547f72d0"


def post_install(self):
    self.install_license("LICENSE")
