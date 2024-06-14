pkgname = "tailscale"
pkgver = "1.68.1"
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
sha256 = "d7fe30282d2f5eabdc76a5a89f11d935ed3a5d93d55f5fd5b40f9a9f49e19490"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
