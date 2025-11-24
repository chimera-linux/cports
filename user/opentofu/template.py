pkgname = "opentofu"
pkgver = "1.10.6"
pkgrel = 2
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X github.com/opentofu/opentofu/version.dev=no",
    "./cmd/tofu",
]
hostmakedepends = ["go"]
pkgdesc = "Tool for building, changing and versioning infrastructure"
license = "MPL-2.0"
url = "https://github.com/opentofu/opentofu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c6712629ef05f461d72c158de32bd009c29844a21bbcfa7bd7f582a341267f29"
