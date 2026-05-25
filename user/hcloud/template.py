pkgname = "hcloud"
pkgver = "1.65.0"
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
sha256 = "85a9d35760c0f694c32a7aa07eac454f48e47b8e826fef8c9d28a720b3d3a17e"
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
