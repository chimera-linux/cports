pkgname = "lego"
pkgver = "4.17.4"
pkgrel = 2
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}", "./cmd/lego"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "27f873708c904ce6c6347f47cae1eba3a00a7948e2b915982f8a209f069c1277"
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
