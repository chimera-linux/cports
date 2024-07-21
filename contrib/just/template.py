pkgname = "just"
pkgver = "1.32.0"
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
    "7c3522d2fae123deebea592cb0ce2a8be65b145efadce8b0965669a4337f8494",
    "a678f6b82c6643055899bcc7cc4fb168d9d24bd65833dfd0a6ad5b8e65c25003",
]


def post_install(self):
    self.install_man("docs-prebuilt/just.1")
    self.install_completion("docs-prebuilt/completions/just.bash", "bash")
    self.install_completion("docs-prebuilt/completions/just.zsh", "zsh")
    self.install_completion("docs-prebuilt/completions/just.fish", "fish")
