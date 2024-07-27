pkgname = "base-kernel"
pkgver = "0.2"
pkgrel = 1
depends = [
    "kmod",
    "procps",
    "virtual:cmd:findmnt!mount",
]
triggers = ["/usr/lib/modules"]
pkgdesc = "Common data and scripts for Linux kernels in Chimera"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check", "keepempty"]


def do_install(self):
    # kernel.d helpers
    self.install_dir("usr/libexec/base-kernel")

    for f in [
        "kernel-clean-initramfs",
        "kernel-root-detect",
        "kernel-pre-upgrade",
        "kernel-post-upgrade",
        "run-kernel-d",
        "script-funcs",
        "script-pre-deinstall",
        "script-pre-install",
        "script-pre-upgrade",
        "script-post-install",
        "script-post-upgrade",
    ]:
        self.install_file(
            self.files_path / "libexec" / f,
            "usr/libexec/base-kernel",
            mode=0o755,
        )

    # modprobe(8) files
    self.install_dir("etc/modprobe.d")
    self.install_dir("etc/modules-load.d")
    self.install_dir("usr/lib/modprobe.d")

    self.install_file(
        self.files_path / "modprobe.d/usb-load-ehci-first",
        "usr/lib/modprobe.d",
        name="usb-load-ehci-first.conf",
    )
    self.install_file(
        self.files_path / "modprobe.d/blacklist.conf", "usr/lib/modprobe.d"
    )

    # udev rules
    self.install_dir("usr/lib/udev/rules.d")

    for f in self.files_path.glob("udev/*.rules"):
        self.install_file(f, "usr/lib/udev/rules.d")

    self.install_file(
        self.files_path / "linux-version.sh",
        "usr/bin",
        mode=0o755,
        name="linux-version",
    )

    self.install_file(
        self.files_path / "chimera-buildkernel.sh",
        "usr/bin",
        mode=0o755,
        name="chimera-buildkernel",
    )
    self.install_file(
        self.files_path / "chimera-stripko.sh",
        "usr/bin",
        mode=0o755,
        name="chimera-stripko",
    )

    self.install_file(
        self.files_path / "chimera-prunekernels.sh",
        "usr/bin",
        mode=0o755,
        name="chimera-prunekernels",
    )


@subpackage("base-kernel-devel")
def _baseloc(self):
    self.subdesc = "development files"
    self.depends = [
        self.parent,
        # all the tooling one needs to use chimera-buildkernel
        "bash",
        "gmake",
        "gsed",
        "gtar",
        "xz",
        "zstd-progs",
        "flex",
        "bison",
        "findutils",
        "kmod",
        "pahole",
        "perl",
        "python",
        "u-boot-tools",
        "linux-headers",
        "elfutils-devel",
        "openssl-devel",
        "zlib-ng-compat-devel",
    ]

    return ["usr/bin/chimera-buildkernel", "usr/bin/chimera-stripko"]
