pkgname = "jjui"
pkgver = "0.10.12"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/jjui"]
hostmakedepends = ["go"]
depends = ["jj"]
pkgdesc = "TUI for Jujutsu VCS framework"
license = "MIT"
url = "https://github.com/idursun/jjui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "736692b7ee62ba7a4f368868f690bdccca62bcfaf7f6b79acd9e364b75055dc2"


def post_install(self):
    self.install_license("LICENSE")
