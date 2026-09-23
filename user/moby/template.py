pkgname = "moby"
pkgver = "29.8.1"
pkgrel = 0
# match to release
_commit = "464cd50c3d9e92877d56940ea160de6fca7bea23"
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
sha256 = "94be9d6940b613676335fc494e617b4acf98676435b3744f32649ed72114bd58"
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
