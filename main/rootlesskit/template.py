pkgname = "rootlesskit"
pkgver = "2.3.1"
pkgrel = 2
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/rootless-containers/rootlesskit/pkg/version.Version={pkgver}",
    "./cmd/...",
]
hostmakedepends = ["go"]
depends = ["util-linux-ns"]
pkgdesc = "Fake root for rootless containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/rootless-containers/rootlesskit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dc2177648304ef29f5668605dec3a2d29c6b5639bba407224de2b7993f438898"
# no tests
options = ["!check"]
