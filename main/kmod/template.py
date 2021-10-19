pkgname = "kmod"
pkgver = "27"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-zlib", "--with-xz", "--disable-test-modules",
    "--disable-dependency-tracking"
]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel", "liblzma-devel"]
pkgdesc = "Linux kenrel module handling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git"
source = f"$(KERNEL_SITE)/utils/kernel/kmod/kmod-{pkgver}.tar.xz"
sha256 = "c1d3fbf16ca24b95f334c1de1b46f17bbe5a10b0e81e72668bdc922ebffbbc0c"
# needs bash
options = ["!check"]

def post_install(self):
    self.install_file(
        self.files_path / "depmod-search.conf", "usr/lib/depmod.d",
        name = "search.conf"
    )

    # empty dirs
    self.install_dir(f"etc/depmod.d")
    (self.destdir / f"etc/depmod.d/.empty").touch(mode = 0o644)
    self.install_dir(f"etc/modprobe.d")
    (self.destdir / f"etc/modprobe.d/.empty").touch(mode = 0o644)
    self.install_dir(f"usr/lib/modprobe.d")
    (self.destdir / f"usr/lib/modprobe.d/.empty").touch(mode = 0o644)

    # compat
    for tool in ["lsmod", "insmod", "rmmod", "depmod", "modprobe", "modinfo"]:
        self.install_link("kmod", f"usr/bin/{tool}")

@subpackage("libkmod-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()

@subpackage("libkmod")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()
