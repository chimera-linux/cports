pkgname = "kmod"
pkgver = "34.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxz=disabled"]
hostmakedepends = [
    "bash",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "openssl3-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Linux kernel module handling"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.gz"
sha256 = "d60a79fb12a85feab75674ce5b86b2c8bae1714f775f481eae926bd2657b2ffe"


def post_install(self):
    self.install_file(
        self.files_path / "depmod-search.conf",
        "usr/lib/depmod.d",
        name="search.conf",
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    # initramfs-tools
    self.install_initramfs(self.files_path / "kmod.initramfs-tools")


@subpackage("kmod-devel")
def _(self):
    self.renames = ["libkmod-devel"]

    return self.default_devel()


@subpackage("kmod-libs")
def _(self):
    self.renames = ["libkmod"]

    return self.default_libs()
