pkgname = "virtiofsd"
pkgver = "1.13.1"
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
license = "Apache-2.0 AND BSD-3-Clause"
url = "https://gitlab.com/virtio-fs/virtiofsd"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "84b34c359c45565adb495ffe9e4f6afdde8ef5b05cbfd47e49140bb58e470a2a"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


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
