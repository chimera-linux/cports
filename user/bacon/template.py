pkgname = "bacon"
pkgver = "3.19.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2c49ca02687391d425f2cc9a19cae8227338def2d689d55ff5970cb70fd2b7f6"


def pre_prepare(self):
    # rustix loongarch64
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.174",
        allow_network=True,
    )


def post_install(self):
    self.install_license("LICENSE")
