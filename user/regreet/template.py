pkgname = "regreet"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cargo"
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
sha256 = "7e26799dffdede183fc62d12aedbda5fea92d7d9802a180755d8a1d1fd93f2f7"
options = ["etcfiles"]


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
