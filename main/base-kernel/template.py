pkgname = "base-kernel"
pkgver = "0.1"
pkgrel = 0
depends = ["base-udev", "kmod", "procps-ng"]
triggers = ["/boot"]
pkgdesc = "Common data and scripts for Linux kernels in Chimera"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]

def do_install(self):
    # modprobe(8) files
    self.install_dir("usr/lib/modprobe.d")

    self.install_file(
        self.files_path / "modprobe.d/usb-load-ehci-first",
        "usr/lib/modprobe.d",
        name = "usb-load-ehci-first.conf"
    )
    self.install_file(
        self.files_path / "modprobe.d/blacklist.conf", "usr/lib/modprobe.d"
    )

    # sysctl(8) files
    self.install_dir("usr/lib/sysctl.d")

    self.install_file(
        self.files_path / "sysctl.d/sysctl.conf", "usr/lib/sysctl.d",
        name = "10-chimera.conf"
    )
    self.install_file(
        self.files_path / "sysctl.d/sysctl-user.conf", "usr/lib/sysctl.d",
        name = "10-chimera-user.conf"
    )
    self.install_file(
        self.files_path / "sysctl.d/bpf.conf",
        "usr/lib/sysctl.d", name = "20-bpf.conf"
    )

    # udev rules
    self.install_dir("usr/lib/udev/rules.d")

    for f in self.files_path.glob("udev/*.rules"):
        self.install_file(f, "usr/lib/udev/rules.d")

    self.install_file(
        self.files_path / "linux-version.sh", "usr/bin", mode = 0o755,
        name = "linux-version"
    )

    self.install_file(
        self.files_path / "chimera-buildkernel.sh", "usr/bin", mode = 0o755,
        name = "chimera-buildkernel"
    )

@subpackage("base-kernel-devel")
def _baseloc(self):
    self.pkgdesc = f"{pkgdesc} (development files)"
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        # TODO: fill in remaining deps that make sense
    ]

    return ["usr/bin/chimera-buildkernel"]
