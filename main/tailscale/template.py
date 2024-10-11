pkgname = "tailscale"
pkgver = "1.76.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X tailscale.com/version.longStamp={pkgver}"
    + f" -X tailscale.com/version.shortStamp={pkgver}",
    "./cmd/tailscale",
    "./cmd/tailscaled",
]
hostmakedepends = ["go"]
depends = ["iptables", "ca-certificates"]
pkgdesc = "Mesh VPN daemon based on WireGuard"
maintainer = "Val Packett <val@packett.cool>"
license = "BSD-3-Clause"
url = "https://github.com/tailscale/tailscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eaec1fa9a882d877ce6e5fb6ef47b3387124321a8963c66c4c37319106b5c5c2"
# check: needs network access
# cross: completions with host bin
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"tailscale.{shell}", "w") as outf:
            self.do(
                f"{self.make_dir}/tailscale",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"tailscale.{shell}", shell)
