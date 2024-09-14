pkgname = "jaq"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features"]
make_install_args = ["--no-default-features"]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "64b3431970cd4c27f3c4e665913218f44a0f44be7e22401eea34d52d8f3745a9"


def install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
