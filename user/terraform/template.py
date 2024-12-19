pkgname = "terraform"
pkgver = "1.10.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/hashicorp/terraform/version.dev=no",
]
makedepends = ["go"]
pkgdesc = "Tool for building infrastructure as code"
maintainer = "LeFantome <fanome137@proton.me>"
license = "BUSL-1.1"
url = "https://github.com/hashicorp/terraform"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3be0296246a96acb5d45cb354ca32417bffd55d8086a4e3fcd71073e4295bb17"

def post_extract(self):
    self.rm("internal/cloud/*_test.go", glob=True)

def post_install(self):
    self.install_license("LICENSE")
