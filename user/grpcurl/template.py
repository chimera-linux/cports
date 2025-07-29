pkgname = "grpcurl"
pkgver = "1.9.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version=v{pkgver}",
    "./cmd/grpcurl",
]
hostmakedepends = ["go"]
pkgdesc = "Cli tool for interacting with grpc servers"
license = "MIT"
url = "https://github.com/fullstorydev/grpcurl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bb555087f279af156159c86d4d3d5dd3f2991129e4cd6b09114e6851a679340d"


def post_install(self):
    self.install_license("LICENSE")
