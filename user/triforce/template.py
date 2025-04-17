pkgname = "triforce"
pkgver = "0.2.1"
pkgrel = 0
archs = ["aarch64"]
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["lv2"]
pkgdesc = "Beamformer for Apple Silicon laptops"
license = "GPL-2.0-only"
url = "https://github.com/chadmed/triforce"
source = (
    f"https://github.com/chadmed/triforce/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "cfd3e8da2d099defae46a4176d53f14e3ec0b0ed12e4fcbe72b15d900c6b49e9"
# no tests
options = ["!check"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/libtriforce.so",
        "usr/lib/lv2/triforce.lv2",
        mode=0o755,
        name="triforce.so",
    )
    self.install_file("*.ttl", "usr/lib/lv2/triforce.lv2", glob=True)
    self.install_license("LICENCE.txt")
