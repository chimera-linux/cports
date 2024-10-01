pkgname = "golangci-lint"
pkgver = "1.61.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4efcc09dde3eb81ba7e2fc4230d3e99375a4b176dd28c31cab07371cf5c07db"
# some tests fail because of chroot and some need network
options = ["!check"]
