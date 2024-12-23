pkgname = "regreet"
pkgver = "0.1.2"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--features=gtk4_8",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "rust-std",
]
depends = ["greetd"]
pkgdesc = "Clean and customizable greeter for greetd"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later"
url = "https://github.com/rharish101/ReGreet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7358f5536d1fbbf36e0d9ba152a393d85d733ea5946bdc0c720f460de2c5e8e4"


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
