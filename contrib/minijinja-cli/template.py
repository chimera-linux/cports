pkgname = "minijinja-cli"
pkgver = "2.2.0"
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
pkgdesc = "Jinja implementation"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/mitsuhiko/minijinja"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fcf800a574a864f62e197e11d509bae29ef409877c59214bbd6c42b215012677"


def post_install(self):
    self.install_man("assets/man/minijinja-cli.1")
    with self.pushd("assets/completions"):
        self.install_completion("minijinja-cli.bash", "bash")
        self.install_completion("minijinja-cli.fish", "fish")
        self.install_completion("_minijinja-cli", "zsh")
        self.install_completion("minijinja-cli.nu", "nushell")
