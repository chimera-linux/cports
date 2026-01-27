pkgname = "ripdrag"
pkgver = "0.4.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "gtk4-devel",
    "rust-std",
]
pkgdesc = "Drag and drop utilty"
license = "GPL-3.0-only"
url = "https://github.com/nik012003/ripdrag"
source = [f"{url}/archive/refs/tags/v{pkgver}.tar.gz"]
sha256 = ["269234abfc3977828e5fdcf0a915df00a130f03d3d7efde897d875607be19ada"]


def pre_prepare(self):
    # libc loongarch64
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.180",
        allow_network=True,
    )
