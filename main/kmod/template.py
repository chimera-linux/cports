pkgname = "kmod"
pkgver = "34.1"
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
sha256 = "a1e213f07390230b2b2d1869e703ad327c6ddbf33f5e49bcf018134d63e023ea"


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
    # transitional
    self.provides = [self.with_pkgver("libkmod-devel")]

    return self.default_devel()


@subpackage("kmod-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libkmod")]

    return self.default_libs()
