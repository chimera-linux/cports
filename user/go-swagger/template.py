pkgname = "go-swagger"
pkgver = "0.32.3"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/swagger"]
hostmakedepends = ["go"]
pkgdesc = "Swagger implementation for Go"
license = "Apache-2.0"
url = "https://github.com/go-swagger/go-swagger"
# temporary until next release (fixes build on go 1.25)
_commit = "717e3cb29becaaf00e56953556c6d80f8a01b286"
# source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "ce1c542ae0a560768279a0352fa495302b30ef620f7da3f557c3cfcb38aed208"
# needs network
options = ["!check"]
