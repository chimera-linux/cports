pkgname = "yggdrasil"
pkgver = "0.5.5"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    f" -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildName={pkgname}"
    f" -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildVersion={pkgver}",
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
sha256 = "cdbb56b19b91b828afa282554862efb2a79dd4ada26dfb5a7bf3b0c5220f6c17"


def pre_build(self):
    self.do("rm", "build")


def post_install(self):
    self.install_license("LICENSE")

    self.install_service(self.files_path / "yggdrasil")
    self.install_file(
        self.files_path / "yggdrasil.wrapper", "usr/libexec", mode=0o755
    )
