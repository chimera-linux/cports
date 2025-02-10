pkgname = "zoxide"
pkgver = "0.9.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d93ab17a01de68529ef37b599524f882dc654835cc121a9097dd3f2952fd207e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    self.install_completion("contrib/completions/zoxide.bash", "bash")
    self.install_completion("contrib/completions/zoxide.fish", "fish")
    self.install_completion("contrib/completions/_zoxide", "zsh")
