pkgname = "stylua"
pkgver = "2.3.1"
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
sha256 = "aba628d721380290a334ae899eff1aec9d3d14302d2af336f67d8d7af72d35e3"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
