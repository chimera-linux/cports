pkgname = "virtiofsd"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "libcap-ng-devel",
    "libseccomp-devel",
]
install_if = [f"virtiofsd-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Daemon for virtio-fs for qemu"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND BSD-3-Clause"
url = "https://gitlab.com/virtio-fs/virtiofsd"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "df1abc88fd9becd5547580a5a7f88447d237146e1b6ac6f8231b5698a5222832"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/virtiofsd",
        "usr/libexec",
        mode=0o755,
    )
    self.install_license("LICENSE-BSD-3-Clause")
    self.install_file("50-virtiofsd.json", "usr/share/qemu/vhost-user")
    # old qemu compat link; used to be shipped with qemu
    self.install_dir("usr/lib/qemu")
    self.install_link("usr/lib/qemu/virtiofsd", "../../libexec/virtiofsd")


@subpackage("virtiofsd-meta")
def _meta(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
