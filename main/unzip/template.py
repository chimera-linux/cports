pkgname = "unzip"
pkgver = "6.0"
pkgrel = 0
build_style = "makefile"
make_build_target = "unzips"
make_build_args = [
    "-f",
    "unix/Makefile",
    "prefix=/usr",
    "LF2=",
    "D_USE_BZ2=-DUSE_BZIP2",
    "L_BZ2=-lbz2",
]
make_install_args = [*make_build_args]
make_check_target = "test"
make_check_args = ["-f", "unix/Makefile"]
make_use_env = True
makedepends = ["bzip2-devel"]
pkgdesc = "List, test and extract compressed files in a ZIP archive"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Info-ZIP"
url = "http://infozip.sf.net"
source = "$(SOURCEFORGE_SITE)/infozip/unzip60.tar.gz"
sha256 = "036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37"
patch_style = "patch"
tool_flags = {
    "CFLAGS": [
        "-DWILD_STOP_AT_DIR",
        "-DLARGE_FILE_SUPPORT",
        "-DUNICODE_SUPPORT",
        "-DUNICODE_WCHAR",
        "-DUTF8_MAYBE_NATIVE",
        "-DNO_LCHMOD",
        "-DDATE_FORMAT=DF_YMD",
        "-DUSE_BZIP2",
        "-DNATIVE",
    ]
}
hardening = ["vis", "cfi"]


def init_build(self):
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)

    self.make_build_args += [
        "LOCAL_UNZIP=" + cfl,
        "CC=" + self.get_tool("CC"),
        "CFLAGS=" + cfl,
        "LFLAGS1=" + cfl + " " + ldfl,
    ]
    self.make_install_args += [
        "prefix=" + str(self.chroot_destdir / "usr"),
        "INSTALL_PROGRAM=install",
    ]


def post_install(self):
    # hardlink
    self.uninstall("usr/bin/zipinfo")
    self.install_link("usr/bin/zipinfo", "unzip")
    self.rename("usr/man", "share/man")
    self.install_license("LICENSE")
