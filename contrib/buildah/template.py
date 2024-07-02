pkgname = "buildah"
pkgver = "1.36.0"
pkgrel = 2
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
go_build_tags = ["libsqlite3"]
pkgdesc = "OCI image building tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://buildah.io"
source = (
    f"https://github.com/containers/buildah/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c2dd61b3d31576c71001eae1b7cabd7e714bdef8dd7b84d8d59496f26810840d"
# needs subid config in the chroot
options = ["!check"]
