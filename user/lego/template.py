pkgname = "lego"
pkgver = "4.27.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}", "./cmd/lego"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bd5a07b0cc111e6848d4065581e1da46f1c474db2e32b5e71d9c3f9f7753f303"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
