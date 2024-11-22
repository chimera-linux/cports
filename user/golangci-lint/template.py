pkgname = "golangci-lint"
pkgver = "1.62.0"
pkgrel = 1
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d3837b18bd70f6ab7e06a02d9759b5f4ad0bca9459bc27e6d27d4d105d3d0f88"
# some tests fail because of chroot and some need network
options = ["!check"]
