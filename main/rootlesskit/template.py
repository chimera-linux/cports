pkgname = "rootlesskit"
pkgver = "3.3.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["util-linux-ns"]
pkgdesc = "Fake root for rootless containers"
license = "Apache-2.0"
url = "https://github.com/rootless-containers/rootlesskit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "cd2045db33fe8900ac100eb85eaea3c24d3afcf950a82d76c3db7ab3f47dc441"
hardening = []
# no tests
options = ["!check"]


if self.profile.arch == "ppc64le":
    # https://github.com/golang/go/issues/82324
    hardening += ["!pie"]
