pkgname = "stylua"
pkgver = "0.20.0"
pkgrel = 1
build_style = "cargo"
make_build_args = [
    "--features",
    "lua54,luau,fromstr,serialize",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Lua formatter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-2.0"
url = "https://github.com/JohnnyMorganz/StyLua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4a27b12669953d2edf55b89cc80381f97a2dfa735f53f95c6ae6015c8c35ffb"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/stylua")
