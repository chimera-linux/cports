pkgname = "cargo-watch"
pkgver = "8.5.2"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--", "--skip=with_cargo"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["cargo"]
pkgdesc = "Executes action on cargo project's source change"
maintainer = "ttyyls <contact@behri.org>"
license = "CC0-1.0"
url = "https://github.com/watchexec/cargo-watch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "850b8de75c618fa1fcf5e2d56a6b2477e7224fbdfa793f5b5f30b31bf63fb358"


def post_install(self):
    self.install_man("cargo-watch.1")
    self.install_completion("completions/zsh", "zsh")
