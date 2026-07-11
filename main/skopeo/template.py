pkgname = "skopeo"
pkgver = "1.23.0"
pkgrel = 0
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
    "btrfs-progs-devel",
    "gpgme-devel",
    "linux-headers",
    "sqlite-devel",
]
depends = ["containers-common"]
go_build_tags = ["libsqlite3"]
pkgdesc = "OCI image and repo manipulation tool"
license = "Apache-2.0"
url = "https://github.com/podman-container-tools/skopeo"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "de96bfc2bb523c852af675ffdadd934484812ce190aa8620e1d5fd6c51442e25"


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
