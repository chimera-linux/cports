pkgname = "jaq"
pkgver = "1.4.0"
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
sha256 = "20d53c2c992db9bbe3e4e8636015cdd1429b936fd897cd4b3ff02c3abdd3a9ed"


def do_install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
