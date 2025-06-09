pkgname = "node_exporter"
pkgver = "1.9.1"
pkgrel = 0
build_style = "go"
_ld_flag_x_prefix = "github.com/prometheus/common/version"
make_build_args = [
    f"-ldflags=-X {_ld_flag_x_prefix}.Version={pkgver} -X {_ld_flag_x_prefix}.Revision={pkgrel}",
]
hostmakedepends = ["go"]
pkgdesc = "Prometheus exporter for machine metrics"
license = "Apache-2.0"
url = "https://github.com/prometheus/node_exporter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ac80b13ced462e88f243ad5e98c12bbcee2628bf552c0d19bb5ae125ce09730d"
# check needs network connection
options = ["!check"]


def post_install(self):
    self.install_sysusers("^/sysusers.conf")
    self.install_service("^/node_exporter")
