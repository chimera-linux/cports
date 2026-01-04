pkgname = "bottom"
pkgver = "0.12.3"
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
    "1c70894f0eceb7034075959ff3080cf4706c11d7c012912c24e777abe4e62b70",
    "1b8ec43e65d72610e29047ed811ad9534563f78a65275ad0fce5d8bd2ffbffe0",
    "e1f1219f9ad0742384a60a526237c290d309b8c8205698241f060c58c04af89d",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/btm.1.gz")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
