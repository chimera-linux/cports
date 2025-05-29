pkgname = "nushell"
pkgver = "0.104.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=shell::environment::env::env_shlvl_in_exec_repl",
    "--skip=shell::environment::env::env_shlvl_in_repl",
    "--skip=shell::environment::env::path_is_a_list_in_repl",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Shell with a focus on structured data"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3dafca8bf892f5a2afaac1122a88a7eb7f22a0b62ef901f550173a11d5cbdf6e"


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
