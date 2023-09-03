pkgname = "podman"
pkgver = "4.6.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["BUILDFLAGS=-x -buildmode=pie"]
make_check_target = "localunit"
hostmakedepends = [
    "gmake",
    "go",
    "bash",
    "pkgconf",
    "btrfs-progs",
    "python",
    "go-md2man",
]
makedepends = [
    "linux-headers",
    "gpgme-devel",
    "libseccomp-devel",
    "libassuan-devel",
]
depends = [
    "gpgme",
    "libseccomp",
    "libassuan",
    "conmon",
    "crun",
    "slirp4netns",
    "netavark",
    "aardvark-dns",
]
checkdepends = ["git"]
pkgdesc = "Tool for managing OCI containers and pods"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "Apache-2.0"
url = "https://github.com/containers/podman"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2d8e04f0c3819c3f0ed1ca5d01da87e6d911571b96ae690448f7f75df41f2ad1"


if self.profile().cross:
    make_build_args += [f"GOARCH={self.profile().goarch}"]


def pre_check(self):
    self.make.invoke(".install.ginkgo")


def post_install(self):
    self.make.invoke("docker-docs")
    self.install_link("podman", "usr/bin/docker")
    self.install_man("docs/build/man/docker*.1", glob=True)
    self.install_man("docs/build/man/docker*.5", glob=True)
    self.rm(self.destdir / "usr/share/man/man1/podman-generate-systemd.1")
    self.rm(self.destdir / "usr/share/man/man5/quadlet.5")
    self.rm(self.destdir / "usr/share/man/man5/podman-systemd.unit.5")
    self.install_file(self.files_path / "policy.json", "etc/containers")
    self.install_file(self.files_path / "registries.conf", "etc/containers")
    self.install_completion("completions/bash/podman-remote", "bash")
    self.install_completion("completions/zsh/_podman-remote", "zsh")
    self.install_completion("completions/fish/podman-remote.fish", "fish")


@subpackage("podman-docker")
def _docker(self):
    self.pkgdesc = f"{pkgdesc} (Docker CLI emulation)"
    self.depends = ["podman", "!docker"]
    return [
        "usr/bin/docker",
        "usr/share/man/man1/docker*.?",
        "usr/share/man/man5/docker*.?",
    ]
