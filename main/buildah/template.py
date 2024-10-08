pkgname = "buildah"
pkgver = "1.37.4"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "device-mapper-devel",
    "gpgme-devel",
    "libbtrfs-devel",
    "libseccomp-devel",
    "linux-headers",
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://buildah.io"
source = (
    f"https://github.com/containers/buildah/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6e81e01b6a4f6e14c9cd12766dfa1dcf272f6b832bf32bf78e0567eb44b9c065"
# needs subid config in the chroot
options = ["!check"]
