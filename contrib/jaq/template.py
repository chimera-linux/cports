pkgname = "jaq"
pkgver = "1.5.1"
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
sha256 = "a4052d93f761274036e40fdb27f186ffe9555a93d88fee8e2364b6a677ae6426"


def do_install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
