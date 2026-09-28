pkgname = "fuse"
pkgver = "3.18.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "-Duseroot=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers", "udev-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Filesystem in USErspace"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/fuse-{pkgver}/fuse-{pkgver}.tar.gz"
sha256 = "bcd19582c5e30f7fe45dd86a5540e998590aa01903afc7ebcbeea6c8ac5421ee"
file_modes = {"usr/bin/fusermount3": ("root", "root", 0o4755)}
# ld: error: default version symbol fuse_loop_mt@@FUSE_3.2 must be defined
# tests need examples and are useless in chroot
options = ["etcfiles", "!lto", "!check"]


def check(self):
    self.do("python", "-m", "pytest", "test/", wrksrc=self.make_dir)


def post_install(self):
    self.uninstall("etc/init.d/fuse3")
    # compat links
    self.install_link("usr/bin/fusermount", "fusermount3")
    self.install_link("usr/bin/mount.fuse", "mount.fuse3")
    self.install_link("usr/share/man/man1/fusermount.1", "fusermount3.1")
    self.install_link("usr/share/man/man8/mount.fuse.8", "mount.fuse3.8")


@subpackage("fuse-devel")
def _(self):
    return self.default_devel()
