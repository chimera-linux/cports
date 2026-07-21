pkgname = "rebos"
pkgver = "3.5.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "NixOS-style repeatability for any Linux distribution"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/Oglo12/rebos"
source = f"{url}/-/archive/v{pkgver}/rebos-v{pkgver}.tar.gz"
sha256 = "fb5bd9c9d11712187bc0a4fcd8b438228d73951f920f08d35f23cb52dd051696"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rebos")
