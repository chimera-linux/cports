pkgname = "opentofu"
pkgver = "1.9.0"
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
sha256 = "95234f00bb8a6d73bcd3f3920e376a32189004df3aaf26cb95917cec5441f8a8"
