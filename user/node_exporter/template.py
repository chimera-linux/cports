pkgname = "node_exporter"
pkgver = "1.9.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-s \
    -X github.com/prometheus/common/version.Version=${pkgver} \
    -X github.com/prometheus/common/version.Revision=${pkgrel} \
    -X github.com/prometheus/common/version.Branch=release-${pkgrel} \
    ",
]
hostmakedepends = ["go"]
pkgdesc = "Prometheus exporter for machine metrics"
license = "Apache-2.0"
url = "https://github.com/prometheus/node_exporter"
source = f"https://github.com/prometheus/node_exporter/archive/v{pkgver}.tar.gz"
sha256 = "ac80b13ced462e88f243ad5e98c12bbcee2628bf552c0d19bb5ae125ce09730d"
# It's not possible to run tests in a chroot
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "node_exporter")
