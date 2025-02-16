pkgname = "minijinja-cli"
pkgver = "2.7.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "minijinja-cli"]
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
sha256 = "f644285a69f064e2ef951bbbc1aadbd2161229e1ee38076b15564e9d9a3923da"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/minijinja-cli")
    self.install_man("minijinja-cli/assets/man/minijinja-cli.1")
    with self.pushd("minijinja-cli/assets/completions"):
        self.install_completion("minijinja-cli.bash", "bash")
        self.install_completion("minijinja-cli.fish", "fish")
        self.install_completion("_minijinja-cli", "zsh")
        self.install_completion("minijinja-cli.nu", "nushell")
