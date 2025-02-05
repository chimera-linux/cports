pkgname = "kmod"
pkgver = "33"
pkgrel = 5
build_style = "gnu_configure"
configure_args = [
    "--with-zlib",
    "--with-zstd",
    "--disable-test-modules",
]
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "scdoc",
    "slibtool",
]
makedepends = ["zlib-ng-compat-devel", "zstd-devel"]
checkdepends = ["bash"]
pkgdesc = "Linux kernel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.gz"
sha256 = "d7c59c76bb3dd0eeeecdb1302365cf4bd5cb54e977be43a00efa2c96c519c1dc"
# broken testsuite build system
options = ["!check"]


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
    self.depends += makedepends
    # transitional
    self.provides = [self.with_pkgver("libkmod-devel")]

    return self.default_devel()


@subpackage("kmod-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libkmod")]

    return self.default_libs()
