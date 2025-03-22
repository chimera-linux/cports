pkgname = "triforce"
pkgver = "0.2.0"
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
sha256 = "b2b60a0b89c104fcc7f2d86801b715abdc6972eebde8d67a9a7b95ec713f0b46"
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
