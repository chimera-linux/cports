pkgname = "nnn"
pkgver = "5.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["chimerautils-devel", "libedit-readline-devel"]
pkgdesc = "Unorthodox terminal file manager"
license = "BSD-2-Clause"
url = "https://github.com/jarun/nnn"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9faaff1e3f5a2fd3ed570a83f6fb3baf0bfc6ebd6a9abac16203d057ac3fffe3"
tool_flags = {"LDFLAGS": ["-lfts"]}
hardening = ["vis", "cfi"]
# it does not have any tests
options = ["!check"]


def post_install(self):
    self.install_file("misc/desktop/nnn.desktop", "usr/share/applications")
    for i in [64, 128]:
        self.install_file(
            f"misc/logo/logo-{i}x{i}.png",
            f"usr/share/icons/hicolor/{i}x{i}/apps",
            name="nnn.png",
        )
    self.install_file(
        "misc/logo/logo.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="nnn.svg",
    )
    self.install_completion(
        "misc/auto-completion/bash/nnn-completion.bash", "bash"
    )
    self.install_completion("misc/auto-completion/fish/nnn.fish", "fish")
    self.install_completion("misc/auto-completion/zsh/_nnn", "zsh")
    self.install_license("LICENSE")
