pkgname = "ripdrag"
pkgver = "0.4.13"
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
sha256 = ["f3d546233b8ba979f5ea4778f61267968a088e5b3b3035dd391ac9e6cc96162b"]


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
