pkgname = "bottom"
pkgver = "0.11.3"
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
    "f5d286c2950379a310be2042271c4bd772ef66947bf1ca16e5a169115774745c",
    "c0886df4fd34e0d76b6a45f75f485c37c60014b9b9d0e0cf543961fd62535480",
    "968da47965adaddc73d5ad0f315645d14b7b34810f745f1363620fed19969c43",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/btm.1.gz")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
