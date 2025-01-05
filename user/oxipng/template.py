pkgname = "oxipng"
pkgver = "9.1.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5f34bc3a9eba661a686106261720061b1136301ccd67cc653c9c70d71fa33c09"


def post_extract(self):
    # makes aarch64 run in qemu lol
    self.rm(".cargo/config.toml")


def post_install(self):
    self.install_license("LICENSE")
