pkgname = "fuse"
pkgver = "3.15.1"
pkgrel = 0
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
sha256 = "13ef77cda531a21c2131f9576042970e98035c0a5f019abf661506efd2d38a4e"
suid_files = ["usr/bin/fusermount3"]
# ld: error: default version symbol fuse_loop_mt@@FUSE_3.2 must be defined
# tests need examples and are useless in chroot
options = ["!lto", "!check"]


def do_check(self):
    self.do("python", "-m", "pytest", "test/", wrksrc=self.make_dir)


def post_install(self):
    self.chmod(self.destdir / "usr/bin/fusermount3", 0o4755)
    self.rm(self.destdir / "etc/init.d/fuse3")
    # compat links
    self.install_link("fusermount3", "usr/bin/fusermount")
    self.install_link("mount.fuse3", "usr/bin/mount.fuse")
    self.install_link("fusermount3.1", "usr/share/man/man1/fusermount.1")
    self.install_link("mount.fuse3.8", "usr/share/man/man8/mount.fuse.8")


@subpackage("fuse-devel")
def _devel(self):
    return self.default_devel()
