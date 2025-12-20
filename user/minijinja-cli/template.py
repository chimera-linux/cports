pkgname = "minijinja-cli"
pkgver = "2.14.0"
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
sha256 = "1af4212143805bb4febbe29e9f0d32466f9f419b46dcdc5dc03b3f375241d60c"
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
