pkgname = "fuse"
pkgver = "3.11.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "-Duseroot=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers", "eudev-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Filesystem in USErspace"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8982c4c521daf3974dda8a5d55d575c988da13a571970f00aea149eb54fdf14c"
suid_files = ["usr/bin/fusermount3"]
# ld: error: default version symbol fuse_loop_mt@@FUSE_3.2 must be defined
options = ["!lto"]

def do_check(self):
    self.do("python", "-m", "pytest", "test/", wrksrc = self.make_dir)

def post_install(self):
    self.chmod(self.destdir / "usr/bin/fusermount3", 0o4755)
    self.rm(self.destdir / "etc/init.d/fuse3")

@subpackage("fuse-devel")
def _devel(self):
    return self.default_devel()
