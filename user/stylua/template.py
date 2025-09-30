pkgname = "stylua"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--features",
    "lua54,luajit,luau,fromstr,serialize",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua formatter"
license = "MPL-2.0"
url = "https://github.com/JohnnyMorganz/StyLua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e1dfdae2fcbeeae60d1e25102d1845a09501e0afa98a7d31f1e8a4f636695adc"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
