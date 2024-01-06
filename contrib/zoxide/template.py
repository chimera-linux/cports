pkgname = "zoxide"
pkgver = "0.9.2"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a6c2d993a02211c3d23b242c2c6faab9a2648be7a45ad1ff0586651ac827e914"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    self.install_completion("contrib/completions/zoxide.bash", "bash")
    self.install_completion("contrib/completions/zoxide.fish", "fish")
    self.install_completion("contrib/completions/_zoxide", "zsh")
