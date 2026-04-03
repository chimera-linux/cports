pkgname = "dnsproxy"
pkgver = "0.83.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "DNS proxy server"
license = "Apache-2.0"
url = "https://github.com/AdguardTeam/dnsproxy"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "53a586f02ca9c5e3e39ccf70c8e8dade7302b3b17800ade171357dc08fc4e89c"
# uses network
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_service(self.files_path / "dnsproxy")
    self.install_file("config.yaml.dist", "etc/dnsproxy", name="config.yaml")
