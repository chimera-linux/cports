pkgname = "zoxide"
pkgver = "0.9.9"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy cd command for interactive shells"
license = "MIT"
url = "https://github.com/ajeetdsouza/zoxide"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "eddc76e94db58567503a3893ecac77c572f427f3a4eabdfc762f6773abf12c63"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/*.1", glob=True)
    with self.pushd("contrib/completions"):
        self.install_completion("zoxide.bash", "bash")
        self.install_completion("zoxide.fish", "fish")
        self.install_completion("_zoxide", "zsh")
        self.install_completion("zoxide.nu", "nushell")
