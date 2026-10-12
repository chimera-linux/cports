pkgname = "stylua"
pkgver = "2.6.0"
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
sha256 = "d58083b5d453df38b5c78c6839e80b256b434eb7d4aca3f529a1972b6c9115ac"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "stylua"))
