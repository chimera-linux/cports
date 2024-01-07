pkgname = "tailscale"
pkgver = "1.54.0"
pkgrel = 1
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
sha256 = "c895a0f489706535ed400b0599d7d932d9eebc5f1bad2c236408a1e4b86620e7"
options = ["!debug"]


def do_build(self):
    self.golang.build(wrksrc="cmd/tailscaled")
    self.golang.build(wrksrc="cmd/tailscale")


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tailscaled")
