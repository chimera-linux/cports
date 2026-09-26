pkgname = "cri-o"
pkgver = "1.36.2"
pkgrel = 0
build_style = "makefile"
make_build_env = {
    "BUILDTAGS": "seccomp containers_image_openpgp containers_image_ostree_stub"
}
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "pkgconf",
]
makedepends = [
    "btrfs-progs-devel",
    "dinit-chimera",
    "gpgme-devel",
    "libseccomp-devel",
    "linux-headers",
]
depends = ["cni-plugins", "conmon", "containers-common", "util-linux-ns"]
pkgdesc = "OCI-based implementation of Kubernetes Container Runtime Interface"
license = "Apache-2.0"
url = "https://cri-o.io"
source = f"https://github.com/cri-o/cri-o/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a0db3a69cb221a48283b08a1ebca5003b1a9ee14af6aeca8128dde01b6f6334"
# check: depends on networking (fetches a container)
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "crio")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "config.toml", "etc/crio/crio.conf.d/99-default.toml"
    )
    self.install_files("contrib/cni", "usr/share/examples/crio/cni")


@subpackage("cri-o-recommends")
def _(self):
    self.depends = [
        "crun",
    ]
    self.subdesc = "recommended dependencies"
    self.install_if = [self.parent]
    self.options = ["empty"]
    return []
