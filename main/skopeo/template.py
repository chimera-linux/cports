pkgname = "skopeo"
pkgver = "1.16.1"
pkgrel = 1
build_style = "go"
# for compatibility with Makefile targets
make_dir = "bin"
make_build_args = ["./cmd/skopeo"]
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "pkgconf",
]
makedepends = [
    "gpgme-devel",
    "libbtrfs-devel",
    "linux-headers",
    "sqlite-devel",
]
depends = ["containers-common"]
go_build_tags = ["libsqlite3"]
pkgdesc = "OCI image and repo manipulation tool"
maintainer = "Radosław Piliszek <radek@piliszek.it>"
license = "Apache-2.0"
url = "https://github.com/containers/skopeo"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9402e71f3fba979d0c0509240b963847bfeda2eac60be83eb5a628fd67d098e6"
patch_style = "patch"


def post_build(self):
    self.do("make", "docs")


def check(self):
    # only unit tests; others assume docker daemon, gawk, network access, etc.
    self.do("make", "test-unit-local")


def post_install(self):
    self.do(
        "make",
        "install-docs",
        "install-completions",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
    )
