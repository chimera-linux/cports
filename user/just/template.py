pkgname = "just"
pkgver = "1.39.0"
pkgrel = 0
build_style = "cargo"
# skip tests that fail when run outside of git repo
make_check_args = ["--", "--skip", "completions::bash"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash", "python"]
pkgdesc = "Save and run commands from justfile"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = [
    f"{url}/archive/{pkgver}.tar.gz",
    f"{url}/releases/download/{pkgver}/just-{pkgver}-x86_64-unknown-linux-musl.tar.gz",
]
source_paths = [".", "docs-prebuilt"]
sha256 = [
    "8a900072d7f909bc91030df5896168752bb9108967dbb7149d2cfb11fdeb087a",
    "1c53fa85a8c021ce7b19814e1a5e1dc0aa10c04bddca75196f7ab6db6130d2cd",
]


def post_install(self):
    self.install_man("docs-prebuilt/just.1")
    self.install_completion("docs-prebuilt/completions/just.bash", "bash")
    self.install_completion("docs-prebuilt/completions/just.zsh", "zsh")
    self.install_completion("docs-prebuilt/completions/just.fish", "fish")
