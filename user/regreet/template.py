pkgname = "regreet"
pkgver = "0.4.0"
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
sha256 = "dd11f6dc82a929ac51a51750b3268028fe5aa46e5fe1d1cbd11b43ad57b3006a"


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
