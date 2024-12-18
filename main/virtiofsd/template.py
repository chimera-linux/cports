pkgname = "virtiofsd"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "libcap-ng-devel",
    "libseccomp-devel",
    "rust-std",
]
install_if = [self.with_pkgver("virtiofsd-meta")]
pkgdesc = "Daemon for virtio-fs for qemu"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 AND BSD-3-Clause"
url = "https://gitlab.com/virtio-fs/virtiofsd"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "05d80e3d35b2a0bcf7c9fd1bb4bcfea2760376125880e4ee4df395bda203982e"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/virtiofsd",
        "usr/libexec",
        mode=0o755,
    )
    self.install_license("LICENSE-BSD-3-Clause")
    self.install_file("50-virtiofsd.json", "usr/lib/qemu/vhost-user")
    # old qemu compat link; used to be shipped with qemu
    self.install_dir("usr/lib/qemu")
    self.install_link("usr/lib/qemu/virtiofsd", "../../libexec/virtiofsd")


@subpackage("virtiofsd-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
