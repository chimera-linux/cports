pkgname = "minijinja-cli"
pkgver = "2.10.2"
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
sha256 = "d3d87f55bc6c36345602023946ddc1c68d345a51f5f1e8891176efc2dc0e7ec2"
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
