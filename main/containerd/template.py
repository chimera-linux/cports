pkgname = "containerd"
pkgver = "2.4.2"
pkgrel = 0
_rootless_ver = "2.4.2"
build_style = "makefile"
make_build_args = [
    # invokes go, so slower in parallel since races for cache and overloads threads
    "-j1",
    "all",
    "man",
    f"REVISION=chimera-r{pkgrel}",
    f"VERSION={pkgver}",
    "SHIM_CGO_ENABLED=1",
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
    "dinit-chimera",
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
    "02cbbecd0ef78a521d124afa791b843ba5458ef206e1f7f017999ff45c80c0b4",
    "7ec0fe765e13d3a0d93fa3c6cf2a00a82e9de41c634f4fb8c7b2e8edbf8c4f7a",
]
# can't run tests inside namespaces
options = ["etcfiles", "!check"]


if self.profile.arch in ["loongarch64", "riscv64"]:
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
