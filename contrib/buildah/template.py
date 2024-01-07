pkgname = "buildah"
pkgver = "1.34.0"
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
sha256 = "847d9943195360e3dad1132f46bfac4fa333c922f3079560a25ba1b9d9b40453"
# needs subid config in the chroot
options = ["!check"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)
