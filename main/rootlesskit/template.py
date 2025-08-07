pkgname = "rootlesskit"
pkgver = "2.3.4"
pkgrel = 4
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/rootless-containers/rootlesskit/pkg/version.Version={pkgver}",
    "./cmd/...",
]
hostmakedepends = ["go"]
depends = ["util-linux-ns"]
pkgdesc = "Fake root for rootless containers"
license = "Apache-2.0"
url = "https://github.com/rootless-containers/rootlesskit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a4b28fdf7a712db2429b5b5c54161585f2a34d4fcb765ed8447e3466dc83b065"
# no tests
options = ["!check"]
