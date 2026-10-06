pkgname = "zsh-autosuggestions"
pkgver = "0.7.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Suggests commands as you type based on history and completions"
license = "MIT"
url = "https://github.com/zsh-users/zsh-autosuggestions"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0df7affff21cd87ed298e6a3970ed08a1dd66a6efa676454ee5b091ad503badf"
# tests not worth the effort (would require packaging ruby rspec)
options = ["!check"]


def install(self):
    for variant in [".zsh", ".plugin.zsh"]:
        self.install_file(
            f"zsh-autosuggestions{variant}",
            "usr/share/zsh/plugins/zsh-autosuggestions",
        )
    self.install_license("LICENSE")
