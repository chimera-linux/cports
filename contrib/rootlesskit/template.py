pkgname = "rootlesskit"
pkgver = "1.1.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["util-linux-ns"]
pkgdesc = "Fake root for rootless containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/rootless-containers/rootlesskit"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6bc1c4b873bf66766174cbf37046fca67737405ccfb393c1469d6ef7383ab5e2"
# no tests
options = ["!debug", "!check"]
