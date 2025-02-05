pkgname = "containerd"
pkgver = "2.0.2"
pkgrel = 1
build_style = "makefile"
make_build_args = [
    # invokes go, so slower in parallel since races for cache and overloads threads
    "-j1",
    "all",
    "man",
    f"REVISION=chimera-r{pkgrel}",
    f"VERSION={pkgver}",
]
make_install_args = ["install-man"]
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containerd/containerd"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"!https://raw.githubusercontent.com/containerd/nerdctl/refs/tags/v{pkgver}/extras/rootless/containerd-rootless.sh>containerd-rootless-{pkgver}",
]
sha256 = [
    "472747a7a6b360a0864bab0ee00a8a6f51da5795171e6a60ab17aa80cbd850a2",
    "1f8101ce7680ce4533ced18b4e3e39bd300c08210c336d30f6969c8cb1727a7c",
]
# can't run tests inside namespaces
options = ["!check"]


if self.profile().arch == "riscv64":
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
