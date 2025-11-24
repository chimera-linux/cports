pkgname = "go-away"
pkgver = "0.7.0"
pkgrel = 3
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.internalMainVersion={pkgver}",
    "./cmd/go-away",
]
hostmakedepends = ["go"]
pkgdesc = "Abuse detection and rule enforcement"
license = "MIT"
url = "https://git.gammaspectra.live/git/go-away"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1c330c0fa07aaf59011710c8bbc64d93f5a4a828cc6899ea42edb02fa4fe323e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_files("examples", "usr/share/goaway")
