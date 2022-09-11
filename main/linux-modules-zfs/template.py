pkgname = "linux-modules-zfs"
_kernver = "5.19.8"
_zfsver = "2.1.5"
pkgver = f"{_zfsver}.{_kernver}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-config=kernel"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool","perl",  "python", "bash"
]
makedepends = ["linux-devel"]
# provides the same thing as the ckms variant
depends = [f"linux~{_kernver}", f"zfs~{_zfsver}", "!zfs-ckms"]
pkgdesc = f"OpenZFS modules for kernel {_kernver}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = f"https://github.com/openzfs/zfs/releases/download/zfs-{_zfsver}/zfs-{_zfsver}.tar.gz"
sha256 = "1913041e5c44ff07ca384346ad8145aeedf77e77cd1cea9ec5d533246691e10c"
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

    # dynamically generate scriptlets for kernel version

    self.scriptlets["pre-upgrade"] = prescript
    self.scriptlets["pre-install"] = prescript
    self.scriptlets["pre-deinstall"] = prescript

    self.scriptlets["post-upgrade"] = postscript
    self.scriptlets["post-install"] = postscript
    self.scriptlets["post-deinstall"] = postscript

def pre_configure(self):
    self.do("autoreconf", "-if")

def do_install(self):
    modpath = f"usr/lib/modules/{self._linux_version}/extra"

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

    self.install_license("COPYRIGHT")
    self.install_license("LICENSE")
    self.install_license("NOTICE")
