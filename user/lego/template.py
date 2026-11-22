pkgname = "lego"
pkgver = "5.7.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0d8c5583717559bd33631b366c73bd0b46b332a3e50362a84db2ad299e284c75"
hardening = []
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]

if self.profile.arch in ["ppc64le", "ppc64"]:
    # https://github.com/golang/go/issues/82324
    hardening += ["!pie"]


def post_install(self):
    self.install_license("LICENSE")
