pkgname = "lego"
pkgver = "4.20.2"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}", "./cmd/lego"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8b295378d4b2d3fed4f0df6d4d5d6aa712082729334848f89f776a8fec912f97"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
