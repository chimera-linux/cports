pkgname = "moby"
pkgver = "29.10.0"
pkgrel = 0
# match to release
_commit = "06db1734267bf7770914b417bff6556d835bf8cc"
hostmakedepends = ["bash", "cmake", "go", "ninja", "pkgconf"]
makedepends = [
    "containerd-dinit",
    "dinit-chimera",
    "dinit-dbus",
    "linux-headers",
    "nftables-devel",
]
depends = [
    "containerd",
    "dbus",
    "e2fsprogs",
    "iptables",
    "pigz",
    "procps",
    "rootlesskit",
    "slirp4netns",
    "tini",
    "xfsprogs",
    "xz",
]
pkgdesc = "Container management daemon"
license = "Apache-2.0"
url = "https://docker.io"
source = (
    f"https://github.com/moby/moby/archive/refs/tags/docker-v{pkgver}.tar.gz"
)
sha256 = "52ee9d504b0ff278fb591956d761f6f5a8f0008b6bc6d19bc2916856b3f725b9"
env = {
    "DOCKER_GITCOMMIT": _commit,
    "VERSION": pkgver,
}
# points to tini
broken_symlinks = ["usr/bin/docker-init"]
# the build system was originally designed to be ran in a container so tests are a mess
# also likely wouldnt work in a cbuild environment anyways
options = ["!check"]


def prepare(self):
    self.do("make", wrksrc="man")


def build(self):
    from cbuild.util import golang

    self.do("hack/make.sh", "dynbinary", env=golang.get_go_env(self))


def install(self):
    self.install_service(self.files_path / "dockerd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_bin("bundles/dynbinary-daemon/dockerd")
    self.install_bin("bundles/dynbinary-daemon/docker-proxy")
    self.install_link("usr/bin/docker-init", "tini-static")
    # rootless
    self.install_service(self.files_path / "dockerd.user")
    self.install_bin("contrib/dockerd-rootless.sh", name="dockerd-rootless")
    # manpages
    self.do(
        "make",
        "install",
        f"prefix={self.chroot_destdir}/usr/share",
        wrksrc="man",
    )
