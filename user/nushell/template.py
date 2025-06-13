pkgname = "nushell"
pkgver = "0.105.1"
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
sha256 = "2c52ef5aef2ba1a3ae873e84bf72b52220f47c8fe47b99950b791e678a43d597"


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
