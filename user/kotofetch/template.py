pkgname = "kotofetch"
pkgver = "0.2.23"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Displays Japanese quotes in the terminal"
license = "MIT"
url = "https://github.com/hxpe-dev/kotofetch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "19afeff83d166bb31410b2fd7c69b12468f918534f22a435ce2e6e3b620d5594"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
