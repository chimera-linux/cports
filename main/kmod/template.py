pkgname = "kmod"
pkgver = "29"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-zlib", "--with-xz", "--disable-test-modules"]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel", "liblzma-devel"]
checkdepends = ["bash"]
pkgdesc = "Linux kenrel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.xz"
sha256 = "0b80eea7aa184ac6fd20cafa2a1fdf290ffecc70869a797079e2cc5c6225a52a"
# broken testsuite build system
options = ["!check"]

def post_install(self):
    self.install_file(
        self.files_path / "depmod-search.conf", "usr/lib/depmod.d",
        name = "search.conf"
    )

    # empty dirs
    self.install_dir(f"etc/depmod.d", empty = True)
    self.install_dir(f"etc/modprobe.d", empty = True)
    self.install_dir(f"usr/lib/modprobe.d", empty = True)

    # compat
    for tool in ["lsmod", "insmod", "rmmod", "depmod", "modprobe", "modinfo"]:
        self.install_link("kmod", f"usr/bin/{tool}")

    # initramfs-tools
    self.install_file(
        self.files_path / "kmod.initramfs-tools",
        "usr/share/initramfs-tools/hooks",
        mode = 0o755, name = "kmod"
    )

@subpackage("libkmod-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()

@subpackage("libkmod")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()
