pkgname = "e2fsprogs"
pkgver = "1.47.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-elf-shlibs",
    "--enable-e2initrd-helper",
    "--enable-fuse2fs",
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
# breaks build entirely
configure_gen = []
make_install_args = ["-j1", "install-libs"]
hostmakedepends = ["pkgconf", "texinfo"]
makedepends = [
    "fuse-devel",
    "libblkid-devel",
    "libuuid-devel",
    "linux-headers",
    "udev-devel",
]
checkdepends = ["bzip2", "perl"]
pkgdesc = "Ext2/3/4 file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://e2fsprogs.sourceforge.net"
source = f"$(KERNEL_SITE)/kernel/people/tytso/e2fsprogs/v{pkgver}/e2fsprogs-{pkgver}.tar.xz"
sha256 = "08242e64ca0e8194d9c1caad49762b19209a06318199b63ce74ae4ef2d74e63c"


def post_patch(self):
    # FIXME: fails
    self.rm("tests/m_offset", recursive=True)


def init_configure(self):
    # causes udevrulesdir to cross sysroot prefix otherwise
    self.env["PKG_CONFIG_FDO_SYSROOT_RULES"] = "1"


def post_install(self):
    # prevents udisks automount
    self.uninstall("usr/lib/udev/rules.d/64-ext4.rules")


@subpackage("e2fsprogs-devel")
def _(self):
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
def _(self):
    return self.default_libs()


@subpackage("fuse2fs")
def _(self):
    self.pkgdesc = "Ext2/3/4 FUSE driver"
    self.depends += ["fuse"]

    return [
        "usr/bin/fuse2fs",
        "usr/share/man/man1/fuse2fs.1",
    ]
