pkgname = "base-files"
version = "0.142"
revision = 0
bootstrap = True
short_desc = "Chimera Linux base system files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Public Domain"
homepage = "https://chimera-linux.org"

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

def pre_pkg(self):
    # base root dirs
    for d in [
        "boot", "etc", "etc/modprobe.d", "etc/modules-load.d", "etc/skel",
        "home", "dev", "proc", "usr", "mnt", "opt", "sys", "media", "var",
        "run", "run/lock"
    ]:
        self.install_dir(d)

    # /usr dirs
    for d in [
        "local", "local/bin", "local/sbin", "local/include", "local/lib",
        "bin", "include", "lib", "src"
    ]:
        self.install_dir("usr/" + d)

    # /usr/share and /usr/local/share
    for d in [
        "locale", "misc", "terminfo", "zoneinfo", "doc", "info"
    ]:
        self.install_dir("usr/share/" + d)
        self.install_dir("usr/local/share/" + d)

    # mandirs
    for i in range(1, 9):
        self.install_dir("usr/share/man/man" + str(i))
        self.install_dir("usr/local/share/man/man" + str(i))

    # /var dirs
    for d in ["empty", "log", "opt", "cache", "lib", "mail", "spool"]:
        self.install_dir("var/" + d)

    # /var symlinks
    self.install_link("../run/lock", "var/lock")
    self.install_link("../run", "var/run")
    self.install_link("../mail", "var/spool/mail")

    # root's home dir
    self.install_dir("root")
    (self.destdir / "root").chmod(0o750)

    # /tmp and /var/tmp
    self.install_dir("tmp")
    (self.destdir / "tmp").chmod(0o777)
    self.install_dir("var/tmp")
    (self.destdir / "var/tmp").chmod(0o777)
