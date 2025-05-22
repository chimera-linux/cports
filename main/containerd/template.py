pkgname = "containerd"
pkgver = "2.1.1"
pkgrel = 0
_rootless_ver = "2.0.4"
build_style = "makefile"
make_build_args = [
    # invokes go, so slower in parallel since races for cache and overloads threads
    "-j1",
    "all",
    "man",
    f"REVISION=chimera-r{pkgrel}",
    f"VERSION={pkgver}",
]
make_install_args = [
    "install-man",
    f"VERSION={pkgver}",
    f"REVISION=chimera-r{pkgrel}",
]
make_check_target = "test"
make_check_args = ["TESTFLAGS_RACE="]
hostmakedepends = [
    "go",
    "go-md2man",
]
makedepends = [
    "btrfs-progs-devel",
    "libseccomp-devel",
    "linux-headers",
]
depends = [
    "cni-plugins",
    "oci-runtime",
    "rootlesskit",
    "slirp4netns",
]
# transitional, no longer a separate package
provides = ["containerd-rootless=3"]
pkgdesc = "Industry-standard container runtime"
license = "Apache-2.0"
url = "https://github.com/containerd/containerd"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"!https://raw.githubusercontent.com/containerd/nerdctl/refs/tags/v{_rootless_ver}/extras/rootless/containerd-rootless.sh>containerd-rootless-{pkgver}",
]
sha256 = [
    "6ac779e87926ac1fe4360ffee63efd9f829b15a887e612be9a7d2f8a652674e9",
    "1f8101ce7680ce4533ced18b4e3e39bd300c08210c336d30f6969c8cb1727a7c",
]
# can't run tests inside namespaces
options = ["!check"]


if self.profile().arch in ["loongarch64", "riscv64"]:
    broken = "cgo runtime stuff"


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_file(self.files_path / "config.toml", "etc/containerd")
    self.install_service(self.files_path / "containerd")
    self.install_service(self.files_path / "containerd.user")
    self.install_bin(
        self.sources_path / f"containerd-rootless-{pkgver}",
        name="containerd-rootless",
    )


@subpackage("containerd-stress")
def _(self):
    self.pkgdesc = "Containerd benchmarking utility"

    return ["usr/bin/containerd-stress"]


@subpackage("containerd-ctr")
def _(self):
    self.pkgdesc = "Debug / admin client for containerd"

    return ["usr/bin/ctr"]
