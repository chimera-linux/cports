pkgname = "jaq"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "59cd17e806a4797e28fa42073c6c8a4d6fb40e28efd7a63f3004d1d738d5be93"


def install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
