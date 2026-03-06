pkgname = "iamb"
pkgver = "0.0.11"
pkgrel = 0
build_style = "cargo"
make_env = {"VERGEN_GIT_SHA": pkgver}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "sqlite-devel"]
pkgdesc = "Matrix chat client that uses Vim keybindings"
license = "Apache-2.0"
url = "https://iamb.chat"
source = f"https://github.com/ulyssa/iamb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a5cf4f248e0893b5657c5ad1234207c09968018c5462d4063c096f0db459dd7c"


def install(self):
    self.install_license("LICENSE")
    self.install_bin(f"target/{self.profile().triplet}/release/iamb")
    self.install_man("docs/iamb.1")
    self.install_man("docs/iamb.5")
    self.install_file("config.example.toml", "usr/share/examples/iamb")
