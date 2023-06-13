pkgname = "zoxide"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Fuzzy cd command for interactive shells"
maintainer = "aurelia <git@elia.garden>"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7af5965e0f0779a5ea9135ee03c51b1bb1d84b578af0a7eb2bd13dbf34a342dd"


def post_install(self):
    self.install_man("man/man1/*.1", glob=True)
    self.install_file(
        "contrib/completions/zoxide.bash",
        "usr/share/bash-completion/completions",
        name="zoxide",
    )
    self.install_file(
        "contrib/completions/_zoxide",
        "usr/share/zsh/site-functions",
    )
    self.install_file(
        "contrib/completions/zoxide.fish",
        "usr/share/fish/completions",
    )
