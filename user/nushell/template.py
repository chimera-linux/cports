pkgname = "nushell"
pkgver = "0.106.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=plugin,trash-support,sqlite,native-tls",
]
make_install_args = [*make_build_args]
make_check_args = [
    "--",
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
sha256 = "3e24044c354d050a850b69dc77c99cc503542c3d9d75fed0aef1c12fefdf380b"

def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
