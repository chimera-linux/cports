pkgname = "bottom"
pkgver = "0.15.0"
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
    "9b38fd551ef9e67bb8dc09a658e7c9594913fc5c43154f264d5b776416ad1c4d",
    "a257001464e30b51c426b24f371f94fa6dd7f8b35ad66fa04b7203122bf24cdb",
    "25b5df33a5c91ef885c8ea4f1e4890d0e6dcb3240cf36e5de3cc77aedc679159",
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/btm.1.gz")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
