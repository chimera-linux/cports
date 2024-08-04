pkgname = "bottom"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Process and system monitor"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/ClementTsang/bottom"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/completion.tar.gz",
    f"{url}/releases/download/{pkgver}/manpage.tar.gz",
]
source_paths = [
    ".",
    "completions",
    "man",
]
sha256 = [
    "c0e507cc3a5246e65521e91391410efc605840abe3b40194c5769265051fa1cc",
    "87a722518bbed7012214ff77425aa69b582c8ab1d50817f427b1c920da420710",
    "a320f028f728fbdbdea1d309840544a1da15243f158477a537bb8eeab05259f7",
]


def post_install(self):
    self.install_license("LICENSE")
    self.do("gunzip", self.chroot_cwd / "man/btm.1.gz")
    self.install_man("man/btm.1")
    self.install_completion("completions/btm.bash", "bash", "btm")
    self.install_completion("completions/btm.fish", "fish", "btm")
    self.install_completion("completions/_btm", "zsh", "btm")
    self.install_file("desktop/bottom.desktop", "usr/share/applications")
