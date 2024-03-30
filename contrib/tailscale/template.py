pkgname = "tailscale"
pkgver = "1.62.1"
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
sha256 = "22737fae37e971fecdf49d6b741b99988868aa3f1e683e67e14b872a2c49ca1c"
# debug: fails to split on powerpc
# check: needs network access
options = ["!debug", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
