pkgname = "podman"
pkgver = "5.1.2"
pkgrel = 2
build_style = "go"
# for install.bin compat
make_dir = "bin"
make_build_args = [
    "-mod",
    "vendor",
    "./cmd/podman",
    "./cmd/rootlessport",
]
hostmakedepends = [
    "bash",
    "ggrep",
    "gmake",
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
sha256 = "0e1c4202d25dc270b996583cff97d806eab88682beb9586a6813431559273fc9"
# nah
options = ["!check"]


def post_build(self):
    self.do("gmake", "docs", "GREP=ggrep", "GOMD2MAN=/usr/bin/go-md2man")


def do_install(self):
    self.do(
        "gmake",
        "install.bin",
        "install.completions",
        "install.man",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.install_service(self.files_path / "podman")
    self.install_service(self.files_path / "podman-docker")
    self.install_service(self.files_path / "podman-restart")
    self.install_file(
        self.files_path / "podman-docker.libexec",
        "usr/libexec",
        name="podman-docker",
        mode=0o755,
    )
