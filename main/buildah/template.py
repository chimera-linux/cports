pkgname = "buildah"
pkgver = "1.44.1"
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
source = f"https://github.com/podman-container-tools/buildah/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ac022c60c84f0dd447f1982ae9e28e89d73892d0da24276fa6662cd1d045885e"
# needs subid config in the chroot
options = ["!check"]
