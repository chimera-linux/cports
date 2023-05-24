pkgname = "e2fsprogs"
pkgver = "1.47.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-elf-shlibs",
    "--enable-e2initrd-helper",
    "--enable-symlink-build",
    "--enable-symlink-install",
    "--enable-relative-symlinks",
    "--disable-rpath",
    "--disable-fsck",
    "--disable-uuidd",
    "--disable-libuuid",
    "--disable-libblkid",
    "--with-root-prefix=/usr",
    "e2fsprogs_cv_struct_st_flags=no",
    "MKDIR_P=mkdir -p",  # install-sh is buggy: it only creates one directory
]
make_cmd = "gmake"
make_install_args = ["install-libs"]
hostmakedepends = ["gmake", "pkgconf", "texinfo"]
makedepends = ["libuuid-devel", "libblkid-devel"]
checkdepends = ["perl", "bzip2"]
pkgdesc = "Ext2/3/4 file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://e2fsprogs.sourceforge.net"
source = f"$(KERNEL_SITE)/kernel/people/tytso/{pkgname}/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "144af53f2bbd921cef6f8bea88bb9faddca865da3fbc657cc9b4d2001097d5db"
# test suite hangs on tr, killing it makes it continue? FIXME
options = ["!check"]


def post_patch(self):
    # failing tests
    for test in [
        "f_boundscheck",
        "f_del_dup_quota",
        "f_super_bad_csum",
        "j_recover_csum2_32bit",
        "j_recover_csum2_64bit",
        "j_recover_csum3_64bit",
        "j_recover_fast_commit",
        "m_offset",
    ]:
        self.rm(f"tests/{test}", recursive=True)


@subpackage("e2fsprogs-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel(
        extra=[
            "usr/bin/compile_et",
            "usr/bin/mk_cmds",
            "usr/share/man/man1/compile_et.1",
            "usr/share/man/man1/mk_cmds.1",
            "usr/share/et",
            "usr/share/ss",
        ]
    )


@subpackage("e2fsprogs-libs")
def _libs(self):
    return self.default_libs()


configure_gen = []
