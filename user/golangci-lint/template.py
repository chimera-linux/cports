pkgname = "golangci-lint"
pkgver = "1.64.5"
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
sha256 = "fa773db33252b38233364859cbceaa746cd4cd607b9fefedce6845aa65d2ee71"
# some tests fail because of chroot and some need network
options = ["!check"]
