pkgname = "golangci-lint"
pkgver = "1.60.3"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "038510ae3d094ef1553ee9d4a29a5514b46c83fe68b86279a33d4f284c0a71b2"
# some tests fail because of chroot and some need network
options = ["!check"]
