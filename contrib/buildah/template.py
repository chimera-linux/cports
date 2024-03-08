pkgname = "buildah"
pkgver = "1.35.0"
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
go_build_tags = ["libsqlite3"]
pkgdesc = "OCI image building tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://buildah.io"
source = (
    f"https://github.com/containers/buildah/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "da80378fb27f7520846531336ffd40ec329522fb88da0dadd22b9dcfb63b855d"
# needs subid config in the chroot
options = ["!check"]
