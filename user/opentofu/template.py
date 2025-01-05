pkgname = "opentofu"
pkgver = "1.8.8"
pkgrel = 0
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
sha256 = "c38000df221ad1dfcf773d9b620facaa0f8e5bfb3cbea866faa624474667d51d"
# OpenTofu tests failure when writing state file on the CI machine
options = ["!check"]
