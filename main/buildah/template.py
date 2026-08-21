pkgname = "buildah"
pkgver = "1.45.0"
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
sha256 = "d2bc03332c9f6ad5fcc210c68ad3190fe11d358214c88fb12a233f5045d5eddd"
# needs subid config in the chroot
options = ["!check"]
