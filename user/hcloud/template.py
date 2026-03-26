pkgname = "hcloud"
pkgver = "1.62.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X github.com/hetznercloud/cli/internal/version.version={pkgver}"
    + " -X github.com/hetznercloud/cli/internal/version.versionPrerelease=",
    "./cmd/hcloud",
]
hostmakedepends = ["go"]
pkgdesc = "Command-line interface for Hetzner Cloud"
license = "MIT"
url = "https://github.com/hetznercloud/cli"
source = (
    f"https://github.com/hetznercloud/cli/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b49681282bd9ab376d3f250cad53f1356f7004763c39aa41255ec1c263b05673"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hcloud.{shell}", "w") as f:
            self.do(f"{self.make_dir}/hcloud", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hcloud.{shell}", shell)
