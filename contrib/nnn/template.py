pkgname = "nnn"
pkgver = "4.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["musl-fts-devel", "libedit-readline-devel"]
pkgdesc = "Unorthodox terminal file manager"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/jarun/nnn"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e25465a856d3ba626d6163046669c0d4010d520f2fb848b0d611e1ec6af1b22"
tool_flags = {"LDFLAGS": ["-lfts"]}
hardening = ["vis", "cfi"]
# it does not have any tests
options = ["!check"]


def post_install(self):
    self.install_completion(
        "misc/auto-completion/bash/nnn-completion.bash", "bash"
    )
    self.install_completion("misc/auto-completion/fish/nnn.fish", "fish")
    self.install_completion("misc/auto-completion/zsh/_nnn", "zsh")
    self.install_license("LICENSE")
