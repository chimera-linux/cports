pkgname = "dnsproxy"
pkgver = "0.84.2"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "DNS proxy server"
license = "Apache-2.0"
url = "https://github.com/AdguardTeam/dnsproxy"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a7a6fe89dd1ec34e94fecf78a980696ae1b5f95424e2b9cf62602bf8fee89a2d"
# uses network
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_service(self.files_path / "dnsproxy")
    self.install_file("config.yaml.dist", "etc/dnsproxy", name="config.yaml")
