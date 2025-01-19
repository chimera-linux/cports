pkgname = "zoxide"
pkgver = "0.9.6"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e1811511a4a9caafa18b7d1505147d4328b39f6ec88b88097fe0dad59919f19c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    self.install_completion("contrib/completions/zoxide.bash", "bash")
    self.install_completion("contrib/completions/zoxide.fish", "fish")
    self.install_completion("contrib/completions/_zoxide", "zsh")
