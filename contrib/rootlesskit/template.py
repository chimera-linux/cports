pkgname = "rootlesskit"
pkgver = "2.0.2"
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
sha256 = "8324faa8ae2bab7b79d9b3b5acb9568ab28a3e3df4900001dc4a8b01adaff161"
# no tests
options = ["!debug", "!check"]
