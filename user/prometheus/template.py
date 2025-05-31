pkgname = "prometheus"
pkgver = "3.4.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/prometheus/common/version.Version={pkgver} -X github.com/prometheus/common/version.Revision={pkgrel}",
    "./cmd/prometheus",
    "./cmd/promtool",
]
hostmakedepends = ["go"]
go_build_tags = ["netgo"]
pkgdesc = "Monitoring system and time series database"
license = "Apache-2.0"
url = "https://prometheus.io"
source = [
    f"https://github.com/prometheus/prometheus/archive/v{pkgver}.tar.gz",
    f"https://github.com/prometheus/prometheus/releases/download/v{pkgver}/prometheus-web-ui-{pkgver}.tar.gz",
]
source_paths = [".", "static"]
sha256 = [
    "8990ccef432b81b2106e39b8ff3ab8012b1d92c189c4e6c13303dff50797bf4a",
    "19ceafadf839b8d64b8f0e14f591edcb076add8f789297d981b3650b4ac5d79d",
]
# check needs network connection
options = ["!check"]


def post_install(self):
    self.install_files("static", "usr/share/prometheus/web/ui")
    self.install_file("documentation/examples/prometheus.yml", "etc/prometheus")

    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_service("^/prometheus")
