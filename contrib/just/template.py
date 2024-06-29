pkgname = "just"
pkgver = "1.29.1"
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
    "3e909245038295b6935448d48bb93418b4bc1b0b5621116d1568e12dd872512b",
    "42c47bd34b511c43a4d51a13c425c0e0f51e59e20b9f390fbd8838b85ee8db1b",
]


def post_install(self):
    self.install_man("docs-prebuilt/just.1")
    self.install_completion("docs-prebuilt/completions/just.bash", "bash")
    self.install_completion("docs-prebuilt/completions/just.zsh", "zsh")
    self.install_completion("docs-prebuilt/completions/just.fish", "fish")
