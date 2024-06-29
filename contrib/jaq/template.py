pkgname = "jaq"
pkgver = "1.5.0"
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
sha256 = "318e9344a85e96b43acca2615c8d47b7e061f8ed4c664728a0b9528d7ac1782a"


def do_install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
