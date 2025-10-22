pkgname = "hcloud"
pkgver = "1.55.0"
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
sha256 = "824e6e5fe39574a6219e483b7f8dc3ca14458d9077ae54b97fff9389cc2b5424"
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
