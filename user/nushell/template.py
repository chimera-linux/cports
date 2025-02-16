pkgname = "nushell"
pkgver = "0.102.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
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
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "97faa3626be944d83b26c43d0b5c9e1ae14dfc55ef4465ac00fc1c64dceda7ce"


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
