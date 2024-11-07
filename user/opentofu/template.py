pkgname = "opentofu"
pkgver = "1.8.4"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X github.com/opentofu/opentofu/version.dev=no",
    "./cmd/tofu",
]
hostmakedepends = ["go"]
pkgdesc = "Tool for building, changing and versioning infrastructure"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MPL-2.0"
url = "https://github.com/opentofu/opentofu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "89eb05e7ed1b20e3d0c799758b2cfc8d6dc212e8a09b20d9eaf03017be4d74e6"
