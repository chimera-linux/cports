pkgname = "bankstown"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["lv2"]
pkgdesc = "Barebones bass enhancer"
license = "MIT"
url = "https://github.com/chadmed/bankstown"
source = (
    f"https://github.com/chadmed/bankstown/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "e877508b73fe90774d74526d838f75e8ea278bdbcee0a1f92e3eca67ed734675"
# no tests
options = ["!check"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/libbankstown.so",
        "usr/lib/lv2/bankstown.lv2",
        mode=0o755,
        name="bankstown.so",
    )
    self.install_file("*.ttl", "usr/lib/lv2/bankstown.lv2", glob=True)
    self.install_license("LICENSE")
