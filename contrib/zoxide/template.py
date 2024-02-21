pkgname = "zoxide"
pkgver = "0.9.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ec002bdca37917130ae34e733eb29d4baa03b130c4b11456d630a01a938e0187"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    self.install_completion("contrib/completions/zoxide.bash", "bash")
    self.install_completion("contrib/completions/zoxide.fish", "fish")
    self.install_completion("contrib/completions/_zoxide", "zsh")
