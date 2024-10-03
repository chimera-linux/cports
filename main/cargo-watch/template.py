pkgname = "cargo-watch"
pkgver = "8.5.3"
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
sha256 = "1884674d19492727d762da91b9aebc05d29bdb34cdb1903cde36d81edbcc6514"


def post_install(self):
    self.install_man("cargo-watch.1")
    self.install_completion("completions/zsh", "zsh")
