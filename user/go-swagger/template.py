pkgname = "go-swagger"
pkgver = "0.33.1"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/swagger"]
hostmakedepends = ["go"]
pkgdesc = "Swagger implementation for Go"
license = "Apache-2.0"
url = "https://github.com/go-swagger/go-swagger"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2957f08ca2f12efb11050c3aecacb74b11dfe97b47bc05c6395072c8a2cca481"
# needs network
options = ["!check"]
