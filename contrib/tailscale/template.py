pkgname = "tailscale"
pkgver = "1.58.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    f" -X tailscale.com/version.longStamp={pkgver}"
    f" -X tailscale.com/version.shortStamp={pkgver}",
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
sha256 = "452f355408e4e2179872387a863387e06346fc8a6f9887821f9b8a072c6a5b0a"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
