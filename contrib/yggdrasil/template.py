pkgname = "yggdrasil"
pkgver = "0.5.6"
pkgrel = 2
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildName={pkgname}"
    + f" -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildVersion={pkgver}",
    "./cmd/yggdrasil/",
    "./cmd/yggdrasilctl/",
]
make_check_args = ["./src/..."]
hostmakedepends = ["go"]
pkgdesc = "Experiment in scalable routing as an encrypted IPv6 overlay network"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "LGPL-3.0-only"
url = "https://yggdrasil-network.github.io"
source = f"https://github.com/yggdrasil-network/yggdrasil-go/archive/v{pkgver}.tar.gz"
sha256 = "2e5a0874d29efd97147b98818afc1a457bc1d1cf42208df12d234962cb44379e"


def pre_build(self):
    self.do("rm", "build")


def post_install(self):
    self.install_license("LICENSE")

    self.install_file(
        self.files_path / "yggdrasil.conf", "usr/lib/modules-load.d"
    )
    self.install_service(self.files_path / "yggdrasil")
    self.install_file(
        self.files_path / "yggdrasil.wrapper", "usr/libexec", mode=0o755
    )
