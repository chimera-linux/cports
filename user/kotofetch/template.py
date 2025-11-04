pkgname = "kotofetch"
pkgver = "0.2.18"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Small, configurable CLI that displays Japanese quotes in the terminal"
license = "MIT"
url = "https://github.com/hxpe-dev/kotofetch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a1dc9ea996b4f026965c7413f1b7ec17abbd1e5108bd839da8e0fb4419f32399"
# no tests
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
