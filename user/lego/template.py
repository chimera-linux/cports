pkgname = "lego"
pkgver = "5.5.2"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5e0ead0ff177a3f896136817842a420eadc55cccaab9d3afe957b05506f17d27"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
