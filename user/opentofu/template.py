pkgname = "opentofu"
pkgver = "1.8.5"
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
sha256 = "07613c3b7d6c0a7c3ede29da6a4f33d764420326c07a1c41e52e215428858ef4"
