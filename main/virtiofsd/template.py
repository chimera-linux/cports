pkgname = "virtiofsd"
pkgver = "1.12.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND BSD-3-Clause"
url = "https://gitlab.com/virtio-fs/virtiofsd"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "e0d89aa211d5d8175f3d1fd5806451ddc3718d86392c33c941ecc2b4c9336ada"


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
