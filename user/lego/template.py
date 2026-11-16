pkgname = "lego"
pkgver = "5.6.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Let's Encrypt/ACME client"
license = "MIT"
url = "https://github.com/go-acme/lego"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3ea1e82a23e001ed90ff48e7ad1f19d14ce7a50d211ad5c37610f54a918e26d1"
hardening = []
# check: tests need network access: https://github.com/go-acme/lego/issues/560
options = ["!check"]

if self.profile.arch in ["ppc64le", "ppc64"]:
    # https://github.com/golang/go/issues/82324
    hardening += ["!pie"]


def post_install(self):
    self.install_license("LICENSE")
