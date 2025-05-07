pkgname = "buildah"
pkgver = "1.40.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "btrfs-progs-devel",
    "gpgme-devel",
    "libseccomp-devel",
    "linux-headers",
    "lvm2-devel",
    "sqlite-devel",
]
depends = [
    "cni-plugins",
    "containers-common",
    "oci-runtime",
    "slirp4netns",
]
go_build_tags = [
    "libsqlite3",
    "seccomp",
]
pkgdesc = "OCI image building tool"
license = "Apache-2.0"
url = "https://buildah.io"
source = (
    f"https://github.com/containers/buildah/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e7fd0a862c22b57aabe4c2f57a0d628f54f80992f958b17651c490d391fb2095"
# needs subid config in the chroot
options = ["!check"]
