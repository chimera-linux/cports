pkgname = "dnsproxy"
pkgver = "0.81.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Simple DNS proxy server that supports all existing DNS protocols"
license = "Apache-2.0"
url = "https://github.com/AdguardTeam/dnsproxy"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d7a1b9d5b6a1f9bb3b3ecc51e8cb61d38f3e35e3b956fe65abd26ef5fd2ee862"
# TODO: Figure out how to make networking work in check phase...
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "dnsproxy")
    self.install_file(
        "config.yaml.dist", "usr/share/etc/dnsproxy/", name="config.yaml"
    )
    self.install_file(
        self.files_path / "dnsproxy.wrapper", "usr/libexec", mode=0o755
    )
    self.install_license("LICENSE")
