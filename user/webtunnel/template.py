pkgname = "webtunnel"
pkgver = "0.0.3"
pkgrel = 0
build_style = "go"
make_build_args = ["./main/client", "./main/server"]
hostmakedepends = ["go"]
pkgdesc = "Pluggable Transport based on HTTP Upgrade(HTTPT)"
license = "MIT"
url = "https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/webtunnel"
source = f"{url}/-/archive/v{pkgver}/webtunnel-v{pkgver}.tar.gz"
sha256 = "4e91d4038cb425cf7b925d0e4a0bb11e68bc3fb20c27814c37979046525e8e2c"


def post_install(self):
    self.mv(">/usr/bin/client", ">/usr/bin/webtunnel-client")
    self.mv(">/usr/bin/server", ">/usr/bin/webtunnel-server")
    self.install_license("LICENSE")
