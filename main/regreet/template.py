pkgname = "regreet"
pkgver = "0.2.0"
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
sha256 = "6ce1f948feb75e12436eccc41557ad6a7127672f0658a9c9fbd5a412cebafc8a"


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
