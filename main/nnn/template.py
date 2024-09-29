pkgname = "nnn"
pkgver = "5.0"
pkgrel = 1
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["chimerautils-devel", "libedit-readline-devel"]
pkgdesc = "Unorthodox terminal file manager"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/jarun/nnn"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "31e8fd85f3dd7ab2bf0525c3c0926269a1e6d35a5343a6714315642370d8605a"
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
