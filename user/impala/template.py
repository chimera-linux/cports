pkgname = "impala"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["iwd"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "af476be1c36be1c60fbc629f281e7c32aaece704db77b96c7ecd40fb87e0f1a7"


def post_install(self):
    self.install_license("LICENSE")
