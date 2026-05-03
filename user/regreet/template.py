pkgname = "regreet"
pkgver = "0.3.0"
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
depends = ["accountsservice", "greetd"]
pkgdesc = "Clean and customizable greeter for greetd"
license = "GPL-3.0-or-later"
url = "https://github.com/rharish101/ReGreet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0d8855b98c868f89f62ed1ce0eff2e34c5eba903040fcf8acd96e6b18ab69dc6"


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
