pkgname = "gocryptfs"
pkgver = "2.4.0"
pkgrel = 5
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X main.GitVersion={pkgver}"
    + " -X main.GitVersionFuse=[vendored]",
    ".",
    "./gocryptfs-xray",
]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
]
depends = [
    "fuse",
]
pkgdesc = "Encrypted overlay filesystem"
maintainer = "Nasado <hi@nasado.name>"
license = "MIT"
url = "https://github.com/rfjakob/gocryptfs"
source = (
    f"{url}/releases/download/v{pkgver}/gocryptfs_v{pkgver}_src-deps.tar.gz"
)
sha256 = "45158daf20df7f94e0c9ec57ba07af21df2e25e15b8584bf3c7de96adbbc2efd"
# requires fuse kernel module
options = ["!check"]


def post_install(self):
    self.install_man("Documentation/gocryptfs.1")
    self.install_man("Documentation/gocryptfs-xray.1")
    self.install_license("LICENSE")
