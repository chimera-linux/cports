pkgname = "riff"
pkgver = "3.3.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Diff filter highlighting which line parts have changed"
license = "MIT"
url = "https://github.com/walles/riff"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6db6ac7525f00c4a4cb45351b9a229e253b3e9053ab365d6f881c0144159f8da"


def post_install(self):
    self.install_license("LICENSE")
