pkgname = "oxipng"
pkgver = "9.1.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "90c5e32c556c49e8fb2170f281586e87f7619fd574b4ccf1bc76e2f6819bba77"


def post_extract(self):
    # makes aarch64 run in qemu lol
    self.rm(".cargo/config.toml")


def post_install(self):
    self.install_license("LICENSE")
