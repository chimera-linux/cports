pkgname = "zoxide"
pkgver = "0.9.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f733fabe5d25978f538a4d4cb7a2732a066adc21eeac8e8110f9aedd47f38470"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    self.install_completion("contrib/completions/zoxide.bash", "bash")
    self.install_completion("contrib/completions/zoxide.fish", "fish")
    self.install_completion("contrib/completions/_zoxide", "zsh")
