pkgname = "golangci-lint"
pkgver = "1.63.4"
pkgrel = 0
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4424d5e3437fdb723e912c3f4636a69d45155124568132d4440cde9a24be6dac"
# some tests fail because of chroot and some need network
options = ["!check"]
