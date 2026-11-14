pkgname = "jjui"
pkgver = "0.10.13"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/jjui"]
hostmakedepends = ["go"]
depends = ["jj"]
pkgdesc = "TUI for Jujutsu VCS framework"
license = "MIT"
url = "https://github.com/idursun/jjui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1f68ab9431b1ddb2bd24db68735397167d590d6fcc66035056918b97b283089"


def post_install(self):
    self.install_license("LICENSE")
