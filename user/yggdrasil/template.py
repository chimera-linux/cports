pkgname = "yggdrasil"
pkgver = "0.5.15"
pkgrel = 0
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
makedepends = ["dinit-chimera"]
pkgdesc = "Experiment in scalable routing as an encrypted IPv6 overlay network"
license = "LGPL-3.0-only"
url = "https://yggdrasil-network.github.io"
source = f"https://github.com/yggdrasil-network/yggdrasil-go/archive/v{pkgver}.tar.gz"
sha256 = "f1b2202d27e7a250eead4f76e4f83c3e9d9eee7ca5b148c3ae1504d430e7c7ee"
hardening = []

if self.profile.arch == "ppc64le":
    # https://github.com/golang/go/issues/82324
    hardening += ["!pie"]


def pre_build(self):
    self.rm("build")


def post_install(self):
    self.install_license("LICENSE")

    self.install_file(
        self.files_path / "yggdrasil.conf", "usr/lib/modules-load.d"
    )
    self.install_service(self.files_path / "yggdrasil")
    self.install_file(
        self.files_path / "yggdrasil.wrapper", "usr/lib", mode=0o755
    )
