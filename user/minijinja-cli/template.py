pkgname = "minijinja-cli"
pkgver = "2.12.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "minijinja-cli"]
make_build_env = {
    "ASSET_OUT_DIR": "assets",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Jinja implementation"
license = "Apache-2.0"
url = "https://github.com/mitsuhiko/minijinja"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b70d30f5165527d5b67712bf01226fb6add6b8ec38ada194c56f28889a4c6abe"
# check may be disabled
options = []

if self.profile().arch == "riscv64":
    # lots of undefined pyo3 references when linking
    options += ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/minijinja-cli")
    self.install_man("minijinja-cli/assets/man/minijinja-cli.1")
    with self.pushd("minijinja-cli/assets/completions"):
        self.install_completion("minijinja-cli.bash", "bash")
        self.install_completion("minijinja-cli.fish", "fish")
        self.install_completion("_minijinja-cli", "zsh")
        self.install_completion("minijinja-cli.nu", "nushell")
