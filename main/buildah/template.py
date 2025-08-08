pkgname = "buildah"
pkgver = "1.41.1"
pkgrel = 0
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
sha256 = "4113470f783dd1c61e8169795dbe7d13802403b8e195049ca2492c970f0b5f62"
# needs subid config in the chroot
options = ["!check"]
