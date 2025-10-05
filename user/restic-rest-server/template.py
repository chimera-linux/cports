pkgname = "restic-rest-server"
pkgver = "0.14.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/rest-server"]
hostmakedepends = ["go"]
pkgdesc = "Restic server backend"
license = "BSD-2-Clause"
url = "https://github.com/restic/rest-server"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8b3f91d561819ba9bce454505958fcca6d61ecd12e10086954ebfc92ba163ba4"


def post_install(self):
    self.install_license("LICENSE")
