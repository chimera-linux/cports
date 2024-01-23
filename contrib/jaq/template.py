pkgname = "jaq"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features"]
make_install_args = ["--no-default-features"]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "185c4b73d128d5af18245d4a514c017e24ddb98b02569357adf4394c865847cf"


def do_install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
