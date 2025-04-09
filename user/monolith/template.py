pkgname = "monolith"
pkgver = "2.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "CLI tool for saving complete web pages as a single HTML file"
license = "CC0-1.0"
url = "https://github.com/Y2Z/monolith"
source = f"{url}/archive/v{pkgver}/monolith-{pkgver}.tar.gz"
sha256 = "1afafc94ba693597f591206938e998fcf2c78fd6695e7dfd8c19e91061f7b44a"


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
