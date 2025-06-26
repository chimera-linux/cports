pkgname = "buildah"
pkgver = "1.40.1"
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
sha256 = "27678b7ced9f096c34d19c12922d8cc9eea2464e4c59dcb249f0f717b80c50bc"
# needs subid config in the chroot
options = ["!check"]
