pkgname = "kmod"
pkgver = "32"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-zlib",
    "--with-zstd",
    "--disable-test-modules",
]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["automake", "gmake", "libtool", "pkgconf"]
makedepends = ["zlib-devel", "zstd-devel"]
checkdepends = ["bash"]
pkgdesc = "Linux kenrel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.gz"
sha256 = "415ed9997376ea58ccea64bf86b1d63acd31524a6baab09a9c11de6bed667a05"
# broken testsuite build system
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "depmod-search.conf",
        "usr/lib/depmod.d",
        name="search.conf",
    )

    # empty dirs
    self.install_dir("etc/depmod.d", empty=True)
    self.install_dir("etc/modprobe.d", empty=True)
    self.install_dir("usr/lib/modprobe.d", empty=True)

    # initramfs-tools
    self.install_file(
        self.files_path / "kmod.initramfs-tools",
        "usr/share/initramfs-tools/hooks",
        mode=0o755,
        name="kmod",
    )


@subpackage("libkmod-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()


@subpackage("libkmod")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()
