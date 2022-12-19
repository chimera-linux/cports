pkgname = "linux-lts-zfs-bin"
_kernver = "6.1.0"
_zfsver = "2.1.7"
pkgver = f"{_zfsver}.{_kernver}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-config=kernel"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool", "perl", "python", "bash"
]
makedepends = ["linux-lts-devel"]
# provides the same thing as the ckms variant
depends = [f"linux-lts~{_kernver}", f"zfs~{_zfsver}"]
pkgdesc = f"OpenZFS modules for kernel {_kernver}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = f"https://github.com/openzfs/zfs/releases/download/zfs-{_zfsver}/zfs-{_zfsver}.tar.gz"
sha256 = "6462e63e185de6ff10c64ffa6ed773201a082f9dd13e603d7e8136fcb4aca71b"
env = {
    "LLVM": "1",
    "LLVM_IAS": "1",
    "LD": "ld.lld",
}
options = ["!cross"]

_script_pre = """
rm -f /boot/initramfs-@kernver@.img || :
rm -f /boot/initrd.img-@kernver@ || :
"""

# remove ckms-installed zfs of this version if necessary
_script_preinst = _script_pre + f"""
if [ -x /usr/bin/ckms ]; then
    ckms -q -k @kernver@ uninstall zfs > /dev/null 2>&1 || :
fi
"""

_script_post = """
if [ -f /boot/System.map-@kernver@ ]; then
    depmod -a -F /boot/System.map-@kernver@ @kernver@ || :
else
    depmod -a @kernver@ || :
fi
"""

def init_configure(self):
    from cbuild.core import paths

    kver = None
    for f in (paths.bldroot() / "usr/lib/modules").iterdir():
        if kver:
            self.error(f"kernel version already set: {kver}")
        kver = f.name

    if _kernver not in kver:
        self.error(f"kernel mismatch: {kver} (expected {_kernver})")

    self._linux_version = kver

    # we only know these after deps are in
    self.configure_args += [
        f"--with-linux=/usr/src/linux-headers-{kver}",
        f"--with-linux-obj=/usr/src/linux-headers-{kver}",
    ]

    prescript = _script_pre.replace("@kernver@", kver)
    postscript = _script_post.replace("@kernver@", kver)
    preinstscript = _script_preinst.replace("@kernver@", kver)

    # dynamically generate scriptlets for kernel version

    self.scriptlets["pre-install"] = preinstscript
    self.scriptlets["pre-upgrade"] = prescript
    self.scriptlets["pre-deinstall"] = prescript

    self.scriptlets["post-install"] = postscript
    self.scriptlets["post-upgrade"] = postscript
    self.scriptlets["post-deinstall"] = postscript

def pre_configure(self):
    self.do("autoreconf", "-if")

def do_install(self):
    modbase = f"usr/lib/modules/{self._linux_version}"
    modpath = f"{modbase}/extra"

    # exactly mimics dkms/ckms
    for modn, opath, dpath in [
        ("zavl", "avl", "avl/avl"),
        ("znvpair", "nvpair", "nvpair/znvpair"),
        ("zunicode", "unicode", "unicode/zunicode"),
        ("zcommon", "zcommon", "zcommon/zcommon"),
        ("zfs", "zfs", "zfs/zfs"),
        ("icp", "icp", "icp/icp"),
        ("zlua", "lua", "lua/zlua"),
        ("spl", "spl", "spl/spl"),
        ("zzstd", "zstd", "zstd/zzstd"),
    ]:
        self.log(f"compressing and installing: {modn}")
        srcmod = self.chroot_cwd / self.make_dir / "module" / opath / f"{modn}.ko"
        destmod = f"{modpath}/{dpath}"
        self.install_dir(destmod)
        with open(self.destdir / destmod / f"{modn}.ko.gz", "wb") as outf:
            self.do("gzip", "-9", "-c", srcmod, stdout = outf)

    # prevent ckms from managing it
    cdpath = f"{modbase}/ckms-disable/zfs"
    self.install_dir(cdpath)
    (self.destdir / cdpath / _zfsver).touch(0o644)

    self.install_license("COPYRIGHT")
    self.install_license("LICENSE")
    self.install_license("NOTICE")
