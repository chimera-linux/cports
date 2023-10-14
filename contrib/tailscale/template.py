pkgname = "tailscale"
pkgver = "1.50.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X tailscale.com/version.longStamp={pkgver} -X tailscale.com/version.shortStamp={pkgver}"
]
hostmakedepends = ["go"]
depends = ["iptables", "ca-certificates"]
pkgdesc = "Mesh VPN daemon based on WireGuard"
maintainer = "Val Packett <val@packett.cool>"
license = "BSD-3-Clause"
url = "https://github.com/tailscale/tailscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "183a7d559590a759dd77aa9c2b65486ab6e13c26f3c07fad0b536e318ad5e233"
options = ["!debug"]


def do_build(self):
    self.golang.build(wrksrc="cmd/tailscaled")
    self.golang.build(wrksrc="cmd/tailscale")


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled", enable=True)
