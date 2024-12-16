pkgname = "terraform"
pkgver = "1.10.2"
pkgrel = 0
build_style = "go"
makedepends = ["go"]
pkgdesc = "Tool for building and updating infrastructure as code idempotently"
maintainer = "LeFantome <fanome137@proton.me>"
license = "BUSL-1.1"
url = "https://github.com/hashicorp/terraform"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3be0296246a96acb5d45cb354ca32417bffd55d8086a4e3fcd71073e4295bb17"
# Tests cause a segfault - compiled program works
options = ["!check"]

def post_install(self):
     self.install_license("LICENSE")

