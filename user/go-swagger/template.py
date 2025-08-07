pkgname = "go-swagger"
pkgver = "0.31.0"
pkgrel = 5
build_style = "go"
make_build_args = ["./cmd/swagger"]
hostmakedepends = ["go"]
pkgdesc = "Swagger implementation for Go"
license = "Apache-2.0"
url = "https://github.com/go-swagger/go-swagger"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fd8d2a165f12cec1b4cd73392dc91955cc6ae378417c9e105fb67f6b29862c86"
# needs network
options = ["!check"]
