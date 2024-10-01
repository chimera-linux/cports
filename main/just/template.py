pkgname = "just"
pkgver = "1.36.0"
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
    "bc2e2ff0268c2818659c524b21663564864b50ba102afb0a44fe73c08cf35ff0",
    "bc7c9f377944f8de9cd0418b11d2955adebfa25a488c0b5e3dd2d2c0e9d732da",
]


def post_install(self):
    self.install_man("docs-prebuilt/just.1")
    self.install_completion("docs-prebuilt/completions/just.bash", "bash")
    self.install_completion("docs-prebuilt/completions/just.zsh", "zsh")
    self.install_completion("docs-prebuilt/completions/just.fish", "fish")
