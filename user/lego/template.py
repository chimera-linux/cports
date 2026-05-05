pkgname = "lego"
pkgver = "4.35.2"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}", "./cmd/lego"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0afa5397dff24643ab34773518063432ed939788435a16305c92f2090a899c3b"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
