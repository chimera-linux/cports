pkgname = "gsm"
pkgver = "1.0.22"
pkgrel = 0
build_style = "makefile"
make_check_target = "tst"
make_use_env = True
hostmakedepends = ["pkgconf"]
pkgdesc = "GSM 06.10 lossy speech compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "TU-Berlin-2.0"
url = "http://www.quut.com/gsm"
source = f"{url}/gsm-{pkgver}.tar.gz"
sha256 = "f0072e91f6bb85a878b2f6dbf4a0b7c850c4deb8049d554c65340b3bf69df0ac"
patch_style = "patch"
# racey mess of a build system
options = ["!parallel", "!lto"]


def init_configure(self):
    _margs = [
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        "AR=" + self.get_tool("AR"),
        "CCFLAGS="
        + self.get_cflags(shell=True)
        + " -c -DNeedFunctionPrototypes=1",
    ]
    self.make_build_args += _margs
    self.make_check_args += _margs
    self.make_install_args += [
        f"INSTALL_ROOT={self.chroot_destdir / 'usr'}",
        f"GSM_INSTALL_INC={self.chroot_destdir / 'usr/include/gsm'}",
        f"GSM_INSTALL_MAN={self.chroot_destdir / 'usr/share/man/man3'}",
        f"TOAST_INSTALL_MAN={self.chroot_destdir / 'usr/share/man/man1'}",
    ]


def pre_install(self):
    self.install_dir("usr/bin")
    self.install_dir("usr/lib")
    self.install_dir("usr/include/gsm")
    self.install_dir("usr/share/man/man3")
    self.install_dir("usr/share/man/man1")


def post_install(self):
    self.install_file(
        "lib/libgsm.so", "usr/lib", name=f"libgsm.so.{pkgver}", mode=0o755
    )
    self.install_link("usr/lib/libgsm.so.1", f"libgsm.so.{pkgver}")
    self.install_link("usr/lib/libgsm.so", f"libgsm.so.{pkgver}")

    self.install_link("usr/include/gsm.h", "gsm/gsm.h")

    self.install_license("COPYRIGHT")


@subpackage("gsm-devel")
def _(self):
    return self.default_devel()
