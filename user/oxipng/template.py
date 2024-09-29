pkgname = "oxipng"
pkgver = "9.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8eae13e5aa6f500b231b4d15b9fefdeb5f6cc566ddab959b9b7a03a00bb3a520"


def post_extract(self):
    # makes aarch64 run in qemu lol
    self.rm(".cargo/config.toml")


def post_install(self):
    self.install_license("LICENSE")
