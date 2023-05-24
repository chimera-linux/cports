pkgname = "gsm"
pkgver = "1.0.22"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "tst"
make_use_env = True
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "GSM 06.10 lossy speech compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TU-Berlin-2.0"
url = "http://www.quut.com/gsm"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f0072e91f6bb85a878b2f6dbf4a0b7c850c4deb8049d554c65340b3bf69df0ac"
# racey mess of a build system
options = ["!parallel", "!lto"]


def init_configure(self):
    self._margs = [
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        "AR=" + self.get_tool("AR"),
        "CCFLAGS="
        + self.get_cflags(shell=True)
        + " -c -DNeedFunctionPrototypes=1",
    ]


def do_build(self):
    self.make.build(self._margs)


def do_check(self):
    self.make.check(self._margs)


def do_install(self):
    self.install_dir("usr/bin")
    self.install_dir("usr/lib")
    self.install_dir("usr/include/gsm")
    self.install_dir("usr/share/man/man3")
    self.install_dir("usr/share/man/man1")

    self.make.install(
        [
            "INSTALL_ROOT=" + str(self.chroot_destdir / "usr"),
            "GSM_INSTALL_INC=" + str(self.chroot_destdir / "usr/include/gsm"),
            "GSM_INSTALL_MAN="
            + str(self.chroot_destdir / "usr/share/man/man3"),
            "TOAST_INSTALL_MAN="
            + str(self.chroot_destdir / "usr/share/man/man1"),
        ]
    )

    self.install_file(
        "lib/libgsm.so", "usr/lib", name=f"libgsm.so.{pkgver}", mode=0o755
    )
    self.install_link(f"libgsm.so.{pkgver}", "usr/lib/libgsm.so.1")
    self.install_link(f"libgsm.so.{pkgver}", "usr/lib/libgsm.so")

    self.install_link("gsm/gsm.h", "usr/include/gsm.h")

    self.install_license("COPYRIGHT")


@subpackage("gsm-devel")
def _devel(self):
    return self.default_devel()
