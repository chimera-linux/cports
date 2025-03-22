pkgname = "triforce"
pkgver = "0.3.2"
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
sha256 = "1d081222d0bfe2c961ac44b368c9f1d2dd9ec0833a35bab87863bac07e9df019"
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
