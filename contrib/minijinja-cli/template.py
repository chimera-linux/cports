pkgname = "minijinja-cli"
pkgver = "1.0.16"
pkgrel = 0
build_wrksrc = "minijinja-cli"
build_style = "cargo"
# cargo install rebuilds without these args in install to not ship feature at runtime
make_build_args = ["--features=completions"]
make_build_env = {
    "ASSET_OUT_DIR": "assets",
}
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Minimal jinja implementation"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/mitsuhiko/minijinja"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e6da58cbf6ac61a2a614b47694183ead32a9fcc6d9c4dbcc46e472164bbfac63"


def post_install(self):
    self.install_man("assets/man/minijinja-cli.1")
    self.install_completion("assets/completions/minijinja-cli.bash", "bash")
    self.install_completion("assets/completions/minijinja-cli.fish", "fish")
    self.install_completion("assets/completions/_minijinja-cli", "zsh")
