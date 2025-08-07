pkgname = "gocryptfs"
pkgver = "2.5.4"
pkgrel = 3
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
sha256 = "0db47fe41f46d1ff5b3ff4f1cc1088ab324a95af03995348435dcc20a5ff0282"
# requires fuse kernel module
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = "vendor/github.com/aperturerobotics/jacobsa-crypto/cmac/hash.go:97:3: undefined: xorBlock"


def post_install(self):
    self.install_man("Documentation/gocryptfs.1")
    self.install_man("Documentation/gocryptfs-xray.1")
    self.install_license("LICENSE")
