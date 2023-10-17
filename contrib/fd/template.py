pkgname = "fd"
pkgver = "8.7.0"
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
sha256 = "13da15f3197d58a54768aaad0099c80ad2e9756dd1b0c7df68c413ad2d5238c9"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("doc/fd.1", "fd.1")
    self.install_completion("contrib/completion/_fd", "zsh")
