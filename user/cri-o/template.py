pkgname = "cri-o"
pkgver = "1.35.0"
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
sha256 = "cd455dab1df69f88672d46e3cf2fe92fd95256d388a9b5d058194f5e60731922"
# check: depends on networking (fetches a container)
options = ["!check"]


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
