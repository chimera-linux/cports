pkgname = "regreet"
pkgver = "0.1.1"
pkgrel = 1
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
sha256 = "a658c91cdf242dfea814f0bfd0c4d877bd39e3af498d36e5024061e3d07ea76b"


def post_install(self):
    self.install_file(self.files_path / "regreet.toml", "etc/greetd")
    self.install_tmpfiles(self.files_path / "regreet.conf")
