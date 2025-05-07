pkgname = "podman"
pkgver = "5.4.2"
pkgrel = 1
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
    "btrfs-progs-devel",
    "gpgme-devel",
    "libassuan-devel",
    "libseccomp-devel",
    "linux-headers",
    "lvm2-devel",
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
license = "Apache-2.0"
url = "https://podman.io"
source = f"https://github.com/containers/podman/archive/v{pkgver}.tar.gz"
sha256 = "8da62c25956441b14d781099e803e38410a5753e5c7349bcd34615b9ca5ed4f2"
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
