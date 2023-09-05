pkgname = "kmod"
pkgver = "30"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-zlib", "--with-xz", "--disable-test-modules"]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel", "xz-devel"]
checkdepends = ["bash"]
pkgdesc = "Linux kenrel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.xz"
sha256 = "f897dd72698dc6ac1ef03255cd0a5734ad932318e4adbaebc7338ef2f5202f9f"
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

    # compat
    for tool in ["lsmod", "insmod", "rmmod", "depmod", "modprobe", "modinfo"]:
        self.install_link("kmod", f"usr/bin/{tool}")

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


configure_gen = []
