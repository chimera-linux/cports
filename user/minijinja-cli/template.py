pkgname = "minijinja-cli"
pkgver = "2.22.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "minijinja-cli"]
make_build_env = {
    "ASSET_OUT_DIR": "assets",
}
make_check_args = ["--package", "minijinja-cli"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Jinja implementation"
license = "Apache-2.0"
url = "https://github.com/mitsuhiko/minijinja"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c7a5bae5afae29987e948ea14ad4ad8c5dfc0ea2ad98e40d9eef5636da38baf2"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/minijinja-cli")
    self.install_man("minijinja-cli/assets/man/minijinja-cli.1")
    with self.pushd("minijinja-cli/assets/completions"):
        self.install_completion("minijinja-cli.bash", "bash")
        self.install_completion("minijinja-cli.fish", "fish")
        self.install_completion("_minijinja-cli", "zsh")
        self.install_completion("minijinja-cli.nu", "nushell")
