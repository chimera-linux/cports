pkgname = "stylua"
pkgver = "2.0.1"
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
sha256 = "ee0e70e38c8352e6534aac4394402a61ca8d8704e8c11403d9721536b517d66b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
