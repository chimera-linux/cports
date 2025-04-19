pkgname = "sops"
pkgver = "3.10.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/sops"]
hostmakedepends = ["go"]
pkgdesc = "Simple and flexible tool for managing secrets"
license = "MPL-2.0"
url = "https://getsops.io"
source = f"https://github.com/getsops/sops/archive/v{pkgver}.tar.gz"
sha256 = "2f7cfa67f23ccc553538450a1c3e3f7666ec934d94034457b3890dbcd49b0469"
# check: needs docker
options = ["!check"]


def pre_build(self):
    from cbuild.util import golang

    self.do("go", "generate", env=golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")
