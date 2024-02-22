pkgname = "rootlesskit"
pkgver = "2.0.1"
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
sha256 = "4e984e7f581d226c12b5627415a7bfc3284a0b25534e5dd0c44964a8bc784906"
# no tests
options = ["!debug", "!check"]
