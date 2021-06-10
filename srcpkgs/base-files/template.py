pkgname = "base-files"
version = "0.142"
revision = 11
bootstrap = True
depends = ["xbps-triggers"]
short_desc = "Void Linux base system files"
maintainer = "Enno Boland <orphan@voidlinux.org>"
license = "Public Domain"
homepage = "https://www.voidlinux.org"

conf_files = [
    "/etc/inputrc",
    "/etc/profile",
    "/etc/hosts",
    "/etc/host.conf",
    "/etc/securetty",
    "/etc/skel/.bash_profile",
    "/etc/skel/.bash_logout",
    "/etc/skel/.bashrc",
    "/etc/skel/.inputrc",
    "/etc/subuid",
    "/etc/subgid",
    "/etc/issue",
    "/etc/passwd",
    "/etc/group",
    "/etc/fstab",
    "/etc/crypttab",
    "/etc/nsswitch.conf",
]

def do_install(self):
    from cbuild import cpu

    # Create bin and lib dirs and symlinks
    for d in ["bin", "lib"]:
        self.install_dir("usr/" + d)
        self.install_link("usr/" + d, d)

    # Symlink sbin paths to /usr/bin
    self.install_link("usr/bin", "sbin")
    self.install_link("bin", "usr/sbin")

    # Symlink word-specific lib paths
    self.install_link("usr/lib", "lib" + str(cpu.target_wordsize()))
    self.install_link("lib", "usr/lib" + str(cpu.target_wordsize()))

    # Install misc config files
    self.install_dir("etc/skel")

    for f in ["bash_logout", "bash_profile", "bashrc", "inputrc"]:
        self.install_file(
            self.files_path / ("dot_" + f), "etc/skel", name = "." + f
        )

    self.install_file(self.files_path / "securetty", "etc", mode = 0o600)

    for f in [
        "profile", "hosts", "host.conf", "issue", "subuid", "subgid",
        "inputrc", "fstab", "passwd", "group", "crypttab", "nsswitch.conf"
    ]:
        self.install_file(self.files_path / f, "etc")

    self.install_dir("etc/colors")
    self.install_dir("etc/profile.d")

    for f in self.files_path.glob("*.sh"):
        self.install_file(f, "etc/profile.d")

    for f in self.files_path.glob("DIR_COLORS*"):
        self.install_file(f, "etc/colors")

    # modprobe(8) files
    self.install_dir("usr/lib/modprobe.d")

    self.install_file(
        self.files_path / "usb-load-ehci-first", "usr/lib/modprobe.d",
        name = "usb-load-ehci-first.conf"
    )
    self.install_file(self.files_path / "blacklist.conf", "usr/lib/modprobe.d")

    # sysctl(8) files
    self.install_dir("usr/lib/sysctl.d")

    self.install_file(
        self.files_path / "sysctl.conf", "usr/lib/sysctl.d",
        name = "10-void.conf"
    )
    self.install_file(
        self.files_path / "sysctl-user.conf", "usr/lib/sysctl.d",
        name = "10-void-user.conf"
    )
    self.install_file(
        self.files_path / "bpf.conf", "usr/lib/sysctl.d", name = "20-bpf.conf"
    )

    # Install common licenses
    self.install_dir("usr/share/licenses")

    for f in (self.files_path / "licenses").iterdir():
        self.install_file(f, "usr/share/licenses")

    # vkpurge
    self.install_bin(self.files_path / "vkpurge")
    self.install_man(self.files_path / "vkpurge.8")

    self.install_bin(self.files_path / "lsb_release")

    # Install default dracut configuration
    self.install_dir("usr/lib/dracut/dracut.conf.d")

    self.install_file(
        self.files_path / "dracut.conf.d.voidlinux.conf",
        "usr/lib/dracut/dracut.conf.d", name = "00-void.conf"
    )

    # Create /proc/self/mounts -> /etc/mtab symlink
    self.install_link("/proc/self/mounts", "etc/mtab")

    # udev rules
    self.install_dir("usr/lib/udev/rules.d")

    for f in self.files_path.glob("*.rules"):
        self.install_file(f, "usr/lib/udev/rules.d")
