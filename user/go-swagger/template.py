pkgname = "go-swagger"
pkgver = "0.33.2"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/swagger"]
hostmakedepends = ["go"]
pkgdesc = "Swagger implementation for Go"
license = "Apache-2.0"
url = "https://github.com/go-swagger/go-swagger"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c4fd019595342d052b5190051b62bd6f654f286cdc426f5541ccac4ff074418"
# needs network
options = ["!check"]
