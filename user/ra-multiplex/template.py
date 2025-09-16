pkgname = "ra-multiplex"
pkgver = "0.2.5"
pkgrel = 3
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera", "dinit-dbus", "rust-std"]
depends = ["dinit-dbus"]
pkgdesc = "Share a language server instance between multiple clients"
license = "MIT"
url = "https://github.com/pr2502/ra-multiplex"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c24a7e277adce9bbfb86641905d75f166e46459cf4e5b5f3aaa7456b052392dc"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "ra-multiplex.user")
