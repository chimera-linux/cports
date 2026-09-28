pkgname = "zoxide"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4fcd4272b013a10b637dbcc299c58a9924b94470a9042677ca1a204cc2e9150e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    with self.pushd("contrib/completions"):
        self.install_completion("zoxide.bash", "bash")
        self.install_completion("zoxide.fish", "fish")
        self.install_completion("_zoxide", "zsh")
        self.install_completion("zoxide.nu", "nushell")
