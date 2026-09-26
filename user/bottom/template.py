pkgname = "bottom"
pkgver = "0.14.9"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Process and system monitor"
license = "MIT"
url = "https://github.com/ClementTsang/bottom"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/completion.tar.gz>completion-{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/manpage.tar.gz>manpage-{pkgver}.tar.gz",
]
source_paths = [
    ".",
    "completions",
    "man",
]
sha256 = [
    "1dbb940c763fb583b7e1c7dfa165b73ed9a0ba712e72cc97311c5b1c098d5b72",
    "9faff2df2cb37d96f5229b041c49032a8af74f6e5a064b7caad1f5231ad694d5",
    "b244f0a6b2e5a6a53249c080540703c2aa44f3690cbfa7e4ccce9fe4bb926e5c",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/btm.1.gz")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
