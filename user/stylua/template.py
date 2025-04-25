pkgname = "stylua"
pkgver = "2.1.0"
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
sha256 = "eeca8de825f7cd550a846bb2b0c409f112e8f16fe007863996cc49ca4b9641f9"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
