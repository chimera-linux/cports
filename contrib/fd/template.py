pkgname = "fd"
pkgver = "8.7.1"
pkgrel = 0
build_style = "cargo"
# disable the default use-jemalloc and completions features
make_build_args = ["--no-default-features"]
make_install_args = ["--no-default-features"]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Simple, fast and user-friendly alternative to find"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/fd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2292cf6e4ba9262c592075b19ef9c241db32742b61ce613a3f42c474c01a3e28"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("doc/fd.1", "fd.1")
    self.install_completion("contrib/completion/_fd", "zsh")
