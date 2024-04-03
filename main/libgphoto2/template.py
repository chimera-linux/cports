pkgname = "libgphoto2"
pkgver = "2.5.31"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-rpath",
    "udevscriptdir=/usr/lib/udev",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libgd-devel",
    "libexif-devel",
    "libusb-devel",
    "libxml2-devel",
    "libltdl-devel",
]
pkgdesc = "Digital camera access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.gphoto.org"
source = f"https://github.com/gphoto/libgphoto2/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8fc7bf40f979459509b87dd4ff1aae9b6c1c2b4724d37db576081eec15406ace"
options = ["linkundefver"]

if self.profile().cross:
    hostmakedepends += ["libgphoto2"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/udev", recursive=True)

    self.install_dir("usr/lib/udev/hwdb.d")
    self.install_dir("usr/lib/udev/rules.d")

    if not self.profile().cross:
        cexe = self.chroot_destdir / "usr/lib/libgphoto2/print-camera-list"
        cenv = {
            "LD_LIBRARY_PATH": str(self.chroot_destdir / "usr/lib"),
            "CAMLIBS": str(self.chroot_destdir / "usr/lib/libgphoto2" / pkgver),
        }
    else:
        cexe = "/usr/lib/libgphoto2/print-camera-list"
        cenv = None

    upath = self.destdir / "usr/lib/udev"

    with open(upath / "rules.d/40-gphoto.rules", "w") as uf:
        self.do(cexe, "udev-rules", "version", "201", env=cenv, stdout=uf)
    with open(upath / "hwdb.d/20-gphoto.hwdb", "w") as uf:
        self.do(cexe, "hwdb", env=cenv, stdout=uf)


@subpackage("libgphoto2-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])
