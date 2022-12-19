pkgname = "linux-lts-zfs-bin"
_kernver = "6.1.0"
_zfsver = "2.1.7"
pkgver = f"{_zfsver}.{_kernver}"
pkgrel = 0
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool", "perl", "python", "bash", "ckms"
]
makedepends = ["linux-lts-devel", "zfs-ckms"]
# provides the same thing as the ckms variant
depends = [f"linux-lts~{_kernver}", f"zfs~{_zfsver}"]
pkgdesc = f"OpenZFS modules for kernel {_kernver}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
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

def _call_ckms(self, *args):
    return self.do(
        "ckms", "-s", self.chroot_cwd, "-k", self._linux_version, *args
    )

def do_configure(self):
    _call_ckms(self, "add", f"/usr/src/zfs-{_zfsver}")

def do_build(self):
    _call_ckms(self, "build", f"zfs={_zfsver}")

def do_install(self):
    from cbuild.core import paths

    modbase = "usr/lib/modules"
    moddest = f"{modbase}/{self._linux_version}"

    self.install_dir(moddest)
    _call_ckms(
        self, "-d", self.chroot_destdir / modbase, "-D", "-x", "gz",
        "install", f"zfs={_zfsver}"
    )

    # prevent ckms from managing it
    cdpath = f"{moddest}/ckms-disable/zfs"
    self.install_dir(cdpath)
    (self.destdir / cdpath / _zfsver).touch(0o644)

    srcp = paths.bldroot() / f"usr/src/zfs-{_zfsver}"
    self.install_license(srcp / "COPYRIGHT")
    self.install_license(srcp / "LICENSE")
    self.install_license(srcp / "NOTICE")
