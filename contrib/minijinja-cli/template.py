pkgname = "minijinja-cli"
pkgver = "2.0.1"
pkgrel = 0
build_wrksrc = "minijinja-cli"
build_style = "cargo"
# cargo install rebuilds without these args in install to not ship feature at runtime
make_build_args = ["--features=completions"]
make_build_env = {
    "ASSET_OUT_DIR": "assets",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Minimal jinja implementation"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/mitsuhiko/minijinja"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9ba95d52c7d5addcd9cc0f52ba03b9bb9298c2f9650154e1f12c36c4f9e46213"


def post_install(self):
    self.install_man("assets/man/minijinja-cli.1")
    self.install_completion("assets/completions/minijinja-cli.bash", "bash")
    self.install_completion("assets/completions/minijinja-cli.fish", "fish")
    self.install_completion("assets/completions/_minijinja-cli", "zsh")
