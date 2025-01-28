pkgname = "rootlesskit"
pkgver = "2.3.2"
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
sha256 = "feb71a63864344f4cf72b6b230082e616aff4f4a43bd2cf13cebd4b04e277980"
# no tests
options = ["!check"]
