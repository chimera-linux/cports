pkgname = "nushell"
pkgver = "0.95.0"
pkgrel = 0
build_style = "cargo"
# We patch Cargo.toml and Cargo.lock
prepare_after_patch = True
make_env = {
    "PREFIX": "/usr",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "openssl-devel", "sqlite-devel", "zstd-devel"]
pkgdesc = "Shell with a focus on structured data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f41a0f41af3996581f9bd485cfe5d55f26dd486dc3812b386bd43439c72a6d16"
# Checks fail with libgit2 < 1.8.1
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
