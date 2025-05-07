pkgname = "golangci-lint"
pkgver = "2.1.5"
pkgrel = 1
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "57a29dfc7b9e81b5ee42b8f3e807d3c68f9e0e74ddc9e66649bdf625ebd92a12"
# some tests fail because of chroot and some need network
options = ["!check"]
