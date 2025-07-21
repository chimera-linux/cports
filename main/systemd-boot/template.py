pkgname = "systemd-boot"
pkgver = "256.11"
pkgrel = 5
archs = ["aarch64", "loongarch64", "riscv64", "x86_64"]
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dacl=disabled",
    "-Dadm-group=false",
    "-Danalyze=false",
    "-Dapparmor=disabled",
    "-Daudit=disabled",
    "-Dbacklight=false",
    "-Dbinfmt=false",
    "-Dbootloader=enabled",
    "-Dbpf-framework=disabled",
    "-Dbzip2=disabled",
    "-Dcoredump=false",
    "-Ddbus=disabled",
    "-Defi=true",
    "-Delfutils=disabled",
    "-Denvironment-d=false",
    "-Dfdisk=disabled",
    "-Dgcrypt=disabled",
    "-Dglib=disabled",
    "-Dgshadow=false",
    "-Dgnutls=disabled",
    "-Dhibernate=false",
    "-Dhostnamed=false",
    "-Didn=false",
    "-Dima=false",
    "-Dinitrd=false",
    "-Dfirstboot=false",
    "-Dkernel-install=false",
    "-Dldconfig=false",
    "-Dlibcryptsetup=disabled",
    "-Dlibcurl=disabled",
    "-Dlibfido2=disabled",
    "-Dlibidn=disabled",
    "-Dlibidn2=disabled",
    "-Dlibiptc=disabled",
    "-Dlocaled=false",
    "-Dlogind=false",
    "-Dlz4=disabled",
    "-Dmachined=false",
    "-Dmicrohttpd=disabled",
    "-Dnetworkd=false",
    "-Dnscd=false",
    "-Dnss-myhostname=false",
    "-Dnss-resolve=disabled",
    "-Dnss-systemd=false",
    "-Doomd=false",
    "-Dopenssl=enabled",
    "-Dp11kit=disabled",
    "-Dpam=disabled",
    "-Dpcre2=disabled",
    "-Dpolkit=disabled",
    "-Dportabled=false",
    "-Dpstore=false",
    "-Dpwquality=disabled",
    "-Drandomseed=false",
    "-Dresolve=false",
    "-Drfkill=false",
    "-Dseccomp=disabled",
    "-Dselinux=disabled",
    "-Dsmack=false",
    "-Dsysext=false",
    "-Dsysusers=false",
    "-Dtimedated=false",
    "-Dtimesyncd=false",
    "-Dtmpfiles=false",
    "-Dtpm=false",
    "-Dtpm2=enabled",
    "-Dqrencode=disabled",
    "-Dquotacheck=false",
    "-Duserdb=false",
    "-Dukify=enabled",
    "-Dutmp=false",
    "-Dvconsole=false",
    "-Dwheel-group=false",
    "-Dxdg-autostart=false",
    "-Dxkbcommon=disabled",
    "-Dxz=disabled",
    "-Dzlib=disabled",
    "-Dzstd=disabled",
    "-Dhwdb=false",
    "-Dman=enabled",
    "-Dstandalone-binaries=true",
    "-Dstatic-libudev=false",
    "-Dtests=false",
    "-Dlink-boot-shared=false",
    "-Dlink-journalctl-shared=false",
    "-Dlink-networkd-shared=false",
    "-Dlink-systemctl-shared=false",
    "-Dlink-timesyncd-shared=false",
    "-Dlink-udev-shared=false",
    "-Dsplit-bin=false",
    "-Dsysvinit-path=",
    "-Drpmmacrosdir=no",
    "-Dpamconfdir=no",
    # secure boot
    "-Dsbat-distro=chimera",
    "-Dsbat-distro-summary=Chimera Linux",
    "-Dsbat-distro-pkgname=systemd-boot",
    "-Dsbat-distro-url=https://chimera-linux.org",
    f"-Dsbat-distro-version={self.full_pkgver}",
]
hostmakedepends = [
    "bash",
    "docbook-xsl-nons",
    "gperf",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-jinja2",
    "python-pyelftools",
]
makedepends = [
    "acl-devel",
    "kmod-devel",
    "libcap-devel",
    "linux-headers",
    "openssl3-devel",
    "tpm2-tss-devel",
    "util-linux-blkid-devel",
    "util-linux-mount-devel",
]
depends = [self.with_pkgver("systemd-boot-efi")]
checkdepends = ["xz", "perl"]
pkgdesc = "UEFI boot manager"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = (
    f"https://github.com/systemd/systemd/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5038424744b2ed8c1d7ecc75b00eeffe68528f9789411da60f199d65762d9ba5"
# the tests that can run are mostly useless
options = ["!check"]


def init_configure(self):
    # bypass some ugly configure checks
    self.configure_args.append(f"-Dtime-epoch={self.source_date_epoch}")


def post_install(self):
    # put measure into lib, we want it for ukify
    self.rename(
        "usr/lib/systemd/systemd-measure",
        "usr/lib/systemd-measure",
        relative=False,
    )

    # drop some more systemd bits
    for f in [
        "etc/systemd",
        "etc/udev",
        "usr/bin/udevadm",
        "usr/include",
        "usr/lib/libsystemd.*",
        "usr/lib/libudev.*",
        "usr/lib/pkgconfig",
        "usr/lib/udev",
        "usr/share/bash-completion/completions/udevadm",
        "usr/share/dbus-1",
        "usr/share/man/man3",
        "usr/share/man/man5/udev*",
        "usr/share/man/man7/udev*",
        "usr/share/man/man7/hw*",
        "usr/share/man/man8",
        "usr/share/pkgconfig",
        "usr/share/polkit-1",
        "usr/share/zsh/site-functions/_udevadm",
    ]:
        self.uninstall(f, glob=True)

    for f in (self.destdir / "usr/lib/systemd").iterdir():
        # keep efi stubs
        if f.name == "boot":
            continue
        self.rm(f, recursive=True, glob=True)

    self.install_file("build/systemd-bless-boot", "usr/lib", mode=0o755)
    self.install_file(
        self.files_path / "99-gen-systemd-boot.sh",
        "usr/lib/kernel.d",
        mode=0o755,
    )
    self.install_bin(
        self.files_path / "gen-systemd-boot.sh", name="gen-systemd-boot"
    )
    self.install_file(self.files_path / "systemd-boot", "usr/lib/systemd/boot")


@subpackage("systemd-boot-efi")
def _(self):
    self.pkgdesc = "UEFI boot manager"
    self.subdesc = "EFI binaries"

    return [
        "usr/lib/systemd/boot/efi",
        "usr/share/man/man7/linux*.efi.stub.7",
        "usr/share/man/man7/systemd-stub.7",
        "usr/share/man/man7/sd-stub.7",
    ]


# only practical for efi so we constrain it by sd-boot
@subpackage("systemd-boot-ukify")
def _(self):
    self.pkgdesc = "Tool to generate Unified Kernel Images"
    self.provides = [self.with_pkgver("ukify")]
    self.depends = [
        self.with_pkgver("systemd-boot-efi"),
        "cmd:readelf!llvm-binutils",
        "python-pefile",
        "python-zstandard",
        "tpm2-tss",  # dlopened
    ]

    return [
        "cmd:ukify",
        # only used here, don't bring in tss2 deps elsewhere
        "usr/lib/systemd-measure",
    ]
