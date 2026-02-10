pkgname = "gocryptfs"
pkgver = "2.6.1"
pkgrel = 2
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X main.GitVersion={pkgver}"
    + " -X main.GitVersionFuse=[vendored]",
    ".",
    "./gocryptfs-xray",
]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["openssl3-devel"]
depends = ["fuse"]
pkgdesc = "Encrypted overlay filesystem"
license = "MIT"
url = "https://github.com/rfjakob/gocryptfs"
source = (
    f"{url}/releases/download/v{pkgver}/gocryptfs_v{pkgver}_src-deps.tar.gz"
)
sha256 = "9a966c1340a1a1d92073091643687b1205c46b57017c5da2bf7e97e3f5729a5a"
# requires fuse kernel module
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = "vendor/github.com/aperturerobotics/jacobsa-crypto/cmac/hash.go:97:3: undefined: xorBlock"


def post_install(self):
    self.install_man("Documentation/gocryptfs.1")
    self.install_man("Documentation/gocryptfs-xray.1")
    self.install_license("LICENSE")
