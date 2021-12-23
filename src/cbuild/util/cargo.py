import re

def clear_vendor_checksums(pkg, crate, vendor_dir = "vendor"):
    p = (pkg.cwd / vendor_dir / crate / ".cargo-checksum.json")
    p.write_text(re.sub(r"""("files":{)[^}]*""", r"\1", p.read_text()))

def get_environment(pkg, jobs = None):
    if not jobs:
        jobs = pkg.make_jobs

    sroot = pkg.profile().sysroot

    env = {
        "CARGO_BUILD_TARGET": pkg.profile().triplet,
        "CARGO_BUILD_JOBS": str(jobs),
        "CARGO_HOME": "/tmp/.cargo",
        # gettext-rs
        "GETTEXT_BIN_DIR": "/usr/bin",
        "GETTEXT_LIB_DIR": str(sroot / "usr/lib/gettext"),
        # libssh2-sys
        "LIBSSH2_SYS_USE_PKG_CONFIG": "1",
        # sodium-sys
        "SODIUM_LIB_DIR": str(sroot / "usr/lib"),
        "SODIUM_INC_DIR": str(sroot / "usr/include"),
        # openssl-sys
        "OPENSSL_NO_VENDOR": "1",
        # pcre2-sys
        "PCRE2_SYS_STATIC": "0",
        # cc-rs: make sure host compiler autoguess behavior is bypassed
        "HOST_CC": "clang",
        "HOST_CFLAGS": "-02",
    }

    if pkg.profile().cross:
        env["PKG_CONFIG_ALLOW_CROSS"] = "1"

class Cargo:
    def __init__(self, tmpl, jobs = None, env = {}, wrksrc = None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def _invoke(self, command, args, jobs, base_env, env, wrksrc):
        tmpl = self.template

        if not jobs:
            jobs = self.jobs

        if not jobs:
            jobs = tmpl.make_jobs

        renv = get_environment(tmpl, jobs = jobs)
        renv.update(tmpl.make_env)

        if base_env:
            renv.update(base_env)

        renv.update(self.env)
        renv.update(env)

        if not wrksrc:
            wrksrc = self.wrksrc
        if not wrksrc:
            wrksrc = tmpl.make_dir

        return self.template.do(
            "cargo", command, "--target", tmpl.profile().triplet,
            *tmpl.configure_args, *args, env = renv, wrksrc = wrksrc
        )

    def invoke(
        self, command, args = [], jobs = None, env = {}, wrksrc = None
    ):
        return self._invoke(command, args, jobs, None, env, wrksrc)

    def vendor(self, args = [], env = {}, wrksrc = None):
        return self._invoke("vendor", args, 1, None, env, wrksrc)

    def build(self, args = [], jobs = None, env = {}, wrksrc = None):
        tmpl = self.template
        return self._invoke(
            "build", "--release", tmpl.make_build_args + args,
            jobs, tmpl.make_build_env, env, wrksrc
        )

    def install(self, args = [], jobs = None, env = {}, wrksrc = None):
        tmpl = self.template
        return self._invoke(
            "install", [
                "--root", str(tmpl.chroot_destdir / "usr"), "--path", "."
            ] + tmpl.make_install_args + args,
            jobs, tmpl.make_install_env, env, wrksrc
        )

    def check(self, args = [], jobs = None, env = {}, wrksrc = None):
        tmpl = self.template
        return self._invoke(
            "test", "--release", tmpl.make_check_args + args,
            jobs, tmpl.make_check_env, env, wrksrc
        )

