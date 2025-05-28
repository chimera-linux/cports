pkgname = "zoxide"
pkgver = "0.9.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1b276edbf328aafc86afe1ebce41f45ccba3a3125412e89c8c5d8e825b0c7407"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    with self.pushd("contrib/completions"):
        self.install_completion("zoxide.bash", "bash")
        self.install_completion("zoxide.fish", "fish")
        self.install_completion("_zoxide", "zsh")
        self.install_completion("zoxide.nu", "nushell")
