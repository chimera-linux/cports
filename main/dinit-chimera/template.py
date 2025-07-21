pkgname = "dinit-chimera"
pkgver = "0.99.19"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddefault-path-env=/usr/bin",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "kmod-devel",
    "libdinitctl-devel",
    "linux-headers",
    "udev-devel",
]
depends = [
    "cmd:awk!chimerautils",
    "cmd:fsck!util-linux-mount",
    "cmd:grep!chimerautils",
    "cmd:mkdir!chimerautils",
    "cmd:mount!util-linux-mount",
    "cmd:sd-tmpfiles!sd-tools",
    "cmd:sed!chimerautils",
    "cmd:snooze!snooze",
    "cmd:sulogin!shadow",
    "cmd:systemd-tmpfiles!sd-tools",
    "cmd:udevadm>=256.6-r1!udev",
    "dinit",
    "tzdb",
]
replaces = ["systemd-utils<255", "base-kernel<0.2"]
triggers = [
    "/usr/lib/binfmt.d",
    "/usr/lib/modprobe.d",
    "/usr/lib/modules-load.d",
    "/usr/lib/dinit.d/early/helpers",
]
pkgdesc = "Chimera core services suite"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/tags/v{pkgver}.tar.gz"
sha256 = "5f38c18bf8fb56268809828ea21046414b7c3d2d54617aa1f5a93e94310ad5d9"
hardening = ["vis", "cfi"]
options = ["brokenlinks"]

_have_kexec_tools = self.profile().arch in [
    "aarch64",
    "armhf",
    "armv7",
    "ppc64",
    "ppc64le",
    "x86_64",
]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_tmpfiles("^/dinit.conf", name="dinit")
    self.install_tmpfiles("^/utmp.conf", name="utmp")
    self.install_file("^/sd-tmpfiles-clean", "usr/lib", mode=0o755)
    self.install_service("^/tmpfiles-clean", enable=True)
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file("^/01dinit-env", "etc/X11/Xsession.d", mode=0o755)
    # sysctl additional distro files
    self.install_tmpfiles("^/sysctl.conf", name="sysctl")
    self.install_file(
        "^/sysctl.d/sysctl.conf", "usr/lib/sysctl.d", name="10-chimera.conf"
    )
    self.install_file(
        "^/sysctl.d/sysctl-user.conf",
        "usr/lib/sysctl.d",
        name="10-chimera-user.conf",
    )
    self.install_file(
        "^/sysctl.d/bpf.conf", "usr/lib/sysctl.d", name="20-bpf.conf"
    )
    # provided by base-files
    self.uninstall("usr/lib/tmpfiles.d/var.conf")
    self.uninstall("usr/lib/tmpfiles.d/tmp.conf")


@subpackage("dinit-chimera-kdump", _have_kexec_tools)
def _(self):
    self.subdesc = "kernel crash dump support"
    # don't install-if it, make it user choice to enable
    self.depends = [self.parent, "kexec-tools", "makedumpfile"]
    self.options = ["!splitdinit"]
    return [
        "usr/lib/dinit.d/early/scripts/kdump.sh",
    ]


@subpackage("dinit-chimera-x11")
def _(self):
    self.subdesc = "X11 support"
    self.depends = [self.parent]
    self.install_if = [self.parent, "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]
