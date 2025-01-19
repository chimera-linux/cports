pkgname = "just"
pkgver = "1.38.0"
pkgrel = 1
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
    "3d47e27755d39f40e1ca34bc0ef535fa514e7ed547b2af62311dcadd8bd6d564",
    "c803e67fd7b0af01667bd537197bc3df319938eacf9e8d51a441c71d03035bb5",
]


def post_install(self):
    self.install_man("docs-prebuilt/just.1")
    self.install_completion("docs-prebuilt/completions/just.bash", "bash")
    self.install_completion("docs-prebuilt/completions/just.zsh", "zsh")
    self.install_completion("docs-prebuilt/completions/just.fish", "fish")
