pkgname = "nushell"
pkgver = "0.101.0"
pkgrel = 1
build_style = "cargo"
prepare_after_patch = True
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
sha256 = "43e4a123e86f0fb4754e40d0e2962b69a04f8c2d58470f47cb9be81daabab347"


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
