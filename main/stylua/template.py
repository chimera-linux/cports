pkgname = "stylua"
pkgver = "2.0.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/JohnnyMorganz/StyLua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0d88a55d4d33a7d7334bdef8ccaf1fb6524b21dd66d60be8efc0cf92f6d31ad3"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
