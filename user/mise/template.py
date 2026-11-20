pkgname = "mise"
pkgver = "2026.11.12"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=native-tls",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "lua5.1-devel",
    "openssl3-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Development environment setup tool"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5b20b1175cb3b8396c08fa216abdeb2f3b447794be6750d99fd0badec0a24c75"
# check: takes forever
options = ["!check"]

if self.profile.wordsize == 32:
    # lol
    broken = "memory allocation of 13107204 bytes failed"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "mise"))
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
