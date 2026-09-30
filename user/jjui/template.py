pkgname = "jjui"
pkgver = "0.10.11"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/jjui"]
hostmakedepends = ["go"]
depends = ["jj"]
pkgdesc = "TUI for Jujutsu VCS framework"
license = "MIT"
url = "https://github.com/idursun/jjui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f626daab6524a14955614b34c69fa3b35978821627d7a759e80d185dc0f5ff4f"


def post_install(self):
    self.install_license("LICENSE")
