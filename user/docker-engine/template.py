pkgname = "docker-engine"
pkgver = "28.2.1"
pkgrel = 0
_commit = "0e2cc22d36ae3013f83863c8da2e1b808f25e78e"
_tiniver = "0.19.0"
hostmakedepends = ["bash", "cmake", "go", "ninja"]
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "linux-headers",
    "musl-devel-static",
]
depends = [
    "containerd",
    "e2fsprogs",
    "iptables",
    "pigz",
    "procps",
    "xfsprogs",
    "xz",
]
pkgdesc = "Container management daemon"
license = "Apache-2.0"
url = "https://docker.io"
source = [
    f"https://github.com/moby/moby/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/krallin/tini/archive/refs/tags/v{_tiniver}.tar.gz",
]
source_paths = [".", "tini"]
sha256 = [
    "a8c306c6c1351fe1060b70645e0161c3076e8dac4e239de51f9f793e6dca4b66",
    "0fd35a7030052acd9f58948d1d900fe1e432ee37103c5561554408bdac6bbf0d",
]
env = {
    "DOCKER_GITCOMMIT": _commit,
    "VERSION": pkgver,
}
# the build system was originally designed to be ran in a container so tests are a mess
# also likely wouldnt work in a cbuild environment anyways
options = ["!check"]


def prepare(self):
    self.do("make", wrksrc="man")


def configure(self):
    from cbuild.util import cmake

    cmake.configure(
        self, "tini", "tini", ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
    )


def build(self):
    from cbuild.util import golang

    self.do("hack/make.sh", "dynbinary", env=golang.get_go_env(self))


def post_build(self):
    from cbuild.util import cmake

    cmake.build(self, "tini", ["--target", "tini-static"])


def install(self):
    self.install_service(self.files_path / "docker")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_bin("bundles/dynbinary-daemon/dockerd")
    self.install_bin("bundles/dynbinary-daemon/docker-proxy")
    self.install_bin("tini/tini-static", name="docker-init")
    # rootless
    self.install_service(self.files_path / "docker.user")
    self.install_bin("contrib/dockerd-rootless.sh", name="dockerd-rootless")


def post_install(self):
    self.do(
        "make",
        "install",
        f"prefix={self.chroot_destdir}/usr/share",
        wrksrc="man",
    )


@subpackage("docker-engine-rootless")
def _(self):
    self.subdesc = "rootless support"
    self.depends = [self.parent, "dbus", "rootlesskit", "slirp4netns"]
    return [
        "usr/bin/dockerd-rootless",
        "usr/lib/dinit.d/user",
    ]
