pkgname = "tailscale"
pkgver = "1.64.2"
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
sha256 = "e5e46f6b6b716b2c4696dce0b92dc2e36f02b06b7ad9f055042a820ad61b2a47"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
