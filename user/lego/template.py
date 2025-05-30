pkgname = "lego"
pkgver = "4.23.1"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}", "./cmd/lego"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e86e62946397964d6f2db2a2487cc75acac08e9ad7811c2302d56c35ca521699"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
