pkgname = "opentofu"
pkgver = "1.12.6"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X github.com/opentofu/opentofu/version.dev=no",
    "./cmd/tofu",
]
hostmakedepends = ["go"]
checkdepends = ["bash"]
pkgdesc = "Tool for building, changing and versioning infrastructure"
license = "MPL-2.0"
url = "https://github.com/opentofu/opentofu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d6b49908a66ad277d7de33e9a218ae11b956cd094e39c82300b9b75cac2479ba"
