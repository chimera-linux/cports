pkgname = "rootlesskit"
pkgver = "2.2.0"
pkgrel = 0
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
sha256 = "0075af5f14ea7ff5b1431ba30671d7c0e18e0e57453be58600293b283a9d8e2e"
# no tests
options = ["!debug", "!check"]
