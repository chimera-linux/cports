pkgname = "podman"
pkgver = "5.3.0"
pkgrel = 0
build_style = "go"
# for install.bin compat
make_dir = "bin"
make_build_args = [
    "./cmd/podman",
    "./cmd/rootlessport",
]
hostmakedepends = [
    "bash",
    "ggrep",
    "go",
    "go-md2man",
    "mandoc",
    "pkgconf",
    "python",
]
makedepends = [
    "device-mapper-devel",
    "gpgme-devel",
    "libassuan-devel",
    "libbtrfs-devel",
    "libseccomp-devel",
    "linux-headers",
    "sqlite-devel",
]
depends = [
    "aardvark-dns",
    "catatonit",
    "cni-plugins",
    "conmon",
    "containers-common",
    "fuse-overlayfs",
    "iptables",
    "netavark",
    "oci-runtime",
    "passt",
]
go_build_tags = [
    "apparmor",
    "containers_image_openpgp",
    "containers_image_ostree_stub",
    "libsqlite3",
    "seccomp",
]
pkgdesc = "Container and image management tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://podman.io"
source = f"https://github.com/containers/podman/archive/v{pkgver}.tar.gz"
sha256 = "e160ecb00f87d78d611f3b3d54c5ab833657f365442dce2631c92b435b2d3bfb"
# nah
options = ["!check"]


def post_build(self):
    self.do("make", "docs", "GREP=ggrep", "GOMD2MAN=/usr/bin/go-md2man")


def install(self):
    self.do(
        "make",
        "install.bin",
        "install.completions",
        "install.man",
        "PREFIX=/usr",
        "LIBEXECDIR=/usr/lib",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.install_service(self.files_path / "podman")
    self.install_service(self.files_path / "podman.user")
    self.install_service(self.files_path / "podman-docker")
    self.install_service(self.files_path / "podman-restart")
    self.install_file(
        self.files_path / "podman-docker.libexec",
        "usr/lib",
        name="podman-docker",
        mode=0o755,
    )
