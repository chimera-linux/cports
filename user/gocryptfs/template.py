pkgname = "gocryptfs"
pkgver = "2.5.0"
pkgrel = 1
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
sha256 = "eed73d59a3f5019ec5ce6a2026cbff95789c2280308781bfa7da4aaf84126a67"
# requires fuse kernel module
options = ["!check"]


def post_install(self):
    self.install_man("Documentation/gocryptfs.1")
    self.install_man("Documentation/gocryptfs-xray.1")
    self.install_license("LICENSE")


@subpackage("plasma-vault-gocryptfs")
def _(self):
    self.subdesc = "plasma-vault backend"
    self.provides = [self.with_pkgver("plasma-vault-backend")]
    self.options = ["empty"]

    return []
