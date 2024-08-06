pkgname = "skopeo"
pkgver = "1.16.0"
pkgrel = 1
build_style = "go"
# for compatibility with Makefile targets
make_dir = "bin"
make_build_args = [
    "./cmd/skopeo",
]
hostmakedepends = [
    "bash",
    "gmake",
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
depends = [
    "containers-common",
]
go_build_tags = [
    "libsqlite3",
]
pkgdesc = "OCI image and repo manipulation tool"
maintainer = "Radosław Piliszek <radek@piliszek.it>"
license = "Apache-2.0"
url = "https://github.com/containers/skopeo"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fed91fd067605460ef33431163227471b1e85c8768203fc393345d6ffd645448"


def post_build(self):
    self.do("gmake", "docs")


def do_check(self):
    # only unit tests; others assume docker daemon, gawk, network access, etc.
    self.do("gmake", "test-unit-local")


def post_install(self):
    self.do(
        "gmake",
        "install-docs",
        "install-completions",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
    )
