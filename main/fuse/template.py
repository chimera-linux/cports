pkgname = "fuse"
pkgver = "3.16.2"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dexamples=false", "-Duseroot=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers", "udev-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Filesystem in USErspace"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f797055d9296b275e981f5f62d4e32e089614fc253d1ef2985851025b8a0ce87"
file_modes = {"usr/bin/fusermount3": ("root", "root", 0o4755)}
# ld: error: default version symbol fuse_loop_mt@@FUSE_3.2 must be defined
# tests need examples and are useless in chroot
options = ["!lto", "!check"]


def do_check(self):
    self.do("python", "-m", "pytest", "test/", wrksrc=self.make_dir)


def post_install(self):
    self.uninstall("etc/init.d/fuse3")
    # compat links
    self.install_link("usr/bin/fusermount", "fusermount3")
    self.install_link("usr/bin/mount.fuse", "mount.fuse3")
    self.install_link("usr/share/man/man1/fusermount.1", "fusermount3.1")
    self.install_link("usr/share/man/man8/mount.fuse.8", "mount.fuse3.8")


@subpackage("fuse-devel")
def _devel(self):
    return self.default_devel()
