pkgname = "bottom"
pkgver = "0.11.2"
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
    "213fbea68a315e012a0ab37e3382a287f0424675a47de04801aef4758458e64b",
    "d966b7fce0b1c0923b5513305522f0de8aaae318703c5ff3bd2ffa41e968732c",
    "fb9de1d1fcd7df814adddfbcf8f1d0673c46313f57a9463dad75482a7c5b5009",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/btm.1.gz")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
