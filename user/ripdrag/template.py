pkgname = "ripdrag"
pkgver = "0.4.12"
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
sha256 = ["ffa685c42e84558cc47d8bd5713f8a68f8cd8e313be55a111a0bc43bf1e220de"]


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
