pkgname = "prometheus-node-exporter"
pkgver = "1.12.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/prometheus/common/version.Version={pkgver}",
    ".",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Prometheus exporter for machine metrics"
license = "Apache-2.0"
url = "https://github.com/prometheus/node_exporter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a90f1df0fde58d216d4a7d342e64831d2e3257db8084deadbe69754d34b15142"
# tests need race detector and a lot of host access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("NOTICE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "node-exporter")
