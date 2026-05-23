pkgname = "stylua"
pkgver = "2.5.2"
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
sha256 = "26a220c7bf3a8f50d12b76c952fc4569a1162e2d002440faac3344a3634db4f2"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
